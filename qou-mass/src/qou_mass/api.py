"""Public API for qou_mass — thin orchestration over the
canonical-derivation pipeline.

P2 (Lookup): The predict() and predict_nucleon() functions are currently
data-facades. They read from vendored per-Z shards
(canonical-isotope-witness-Z<NN>.witness.json) shipped with the
package — so external researchers can `pip install qou-mass` and
immediately query the canonical pipeline's outputs for any AME 2020
nuclide.

P3 (Live Compute): The compute_tr_M() function performs live computation
by calling the vendored `markov_peel` chain for on-demand recomputation.
Future revisions will migrate the full `predict()` stack to live compute.

For a given atom request:
  - "binding_energy" — return B_pred from L1/L2/L3 cascade (per-Z
    shard row, layer field tells which layer covered it).
  - "mass" — return composite mass N·m_n + Z·m_p − B (L4) using
    Borromean nucleon masses; or for free p/n the direct Borromean
    prediction.
  - "tr_M" — recompute |tr_M(β_atom, q_0)| via markov_peel; cached
    in user $HOME / .cache / qou_mass / by (Z, N, dps).
"""
from __future__ import annotations

import json
from decimal import Decimal
from importlib import resources
from pathlib import Path
from typing import Iterable, Literal

from .prediction import BraidWord, Prediction, Witness


AtomLabel = str | tuple[int, int]
Observable = Literal["binding_energy", "mass", "tr_M", "mass_excess"]
Method = Literal["auto", "markov_peel", "rust_canonical_chi",
                 "alpha_cluster", "borromean"]
Particle = Literal["p", "n", "mu"]


# ── Atom-label parser ─────────────────────────────────────────────

_ELEMENT_TO_Z = {
    "n": 0, "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6,
    "N": 7, "O": 8, "F": 9, "Ne": 10, "Na": 11, "Mg": 12, "Al": 13,
    "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19,
    "Ca": 20,  # ... (extended in P3)
}


def parse_atom_label(label: AtomLabel) -> tuple[int, int]:
    """Parse '4He', 'He-4', 'helium-4', or (Z, N) tuples → (Z, N)."""
    if isinstance(label, tuple):
        return int(label[0]), int(label[1])
    s = str(label).strip()
    # Special particle aliases.
    aliases = {
        "p": (1, 0), "proton": (1, 0), "1H": (1, 0),
        "n": (0, 1), "neutron": (0, 1),
        "D": (1, 1), "2H": (1, 1), "deuteron": (1, 1),
        "T": (1, 2), "3H": (1, 2), "triton": (1, 2),
        "3He": (2, 1), "He-3": (2, 1),
        "4He": (2, 2), "He-4": (2, 2),
    }
    if s in aliases:
        return aliases[s]
    # Generic "<A><El>" or "<El>-<A>" parse.
    import re
    m = re.match(r"^(\d+)([A-Za-z]+)$", s)
    if not m:
        m = re.match(r"^([A-Za-z]+)-(\d+)$", s)
        if m:
            el, a = m.group(1), int(m.group(2))
        else:
            raise ValueError(f"cannot parse atom label: {label!r}")
    else:
        a, el = int(m.group(1)), m.group(2)
    Z = _ELEMENT_TO_Z.get(el)
    if Z is None:
        # Try first-letter capitalisation.
        Z = _ELEMENT_TO_Z.get(el.capitalize())
    if Z is None:
        raise ValueError(f"unknown element symbol {el!r} in label {label!r}")
    N = a - Z
    return Z, N


# ── Shard loader (vendored data) ──────────────────────────────────

_SHARD_CACHE: dict[int, dict] = {}


def _load_shard(Z: int) -> dict:
    """Load `canonical-isotope-witness-Z<NN>.witness.json` from the
    package's vendored data directory. Cached per process."""
    if Z in _SHARD_CACHE:
        return _SHARD_CACHE[Z]
    filename = f"canonical-isotope-witness-Z{Z:02d}.witness.json"
    try:
        data = resources.files("qou_mass.data.isotopes").joinpath(filename).read_text()
    except (FileNotFoundError, ModuleNotFoundError):
        raise ValueError(f"no vendored shard for Z={Z}")
    shard = json.loads(data, parse_float=Decimal)
    _SHARD_CACHE[Z] = shard
    return shard


def _lookup_row(Z: int, N: int) -> dict | None:
    """Return the per-isotope row, or None if (Z, N) absent."""
    try:
        shard = _load_shard(Z)
    except ValueError:
        return None
    for r in shard.get("data", {}).get("rows", []):
        if r.get("Z") == Z and r.get("N") == N:
            return r
    return None


# ── Public API ────────────────────────────────────────────────────

def predict(
    atom: AtomLabel,
    observable: Observable = "binding_energy",
    *,
    q: Decimal | float | None = None,
    precision_dps: int = 50,
    method: Method = "auto",
    emit_witness: bool = False,
    witness_path: str | None = None,
) -> Prediction:
    """Predict a physical observable for the given atom.

    Reads from the vendored per-Z shards (current: f64 precision,
    matching the paper's canonical-isotope-witness data). For
    higher precision or alternative methods, use the lower-level
    `compute_tr_M()` directly.
    """
    if q is not None:
        raise NotImplementedError(
            "q != q_0 (canonical substrate) not yet wired in P2; use "
            "compute_tr_M() directly for custom q."
        )
    Z, N = parse_atom_label(atom)
    row = _lookup_row(Z, N)
    if row is None:
        raise ValueError(f"no AME 2020 entry for (Z={Z}, N={N})")

    pt = row.get("prediction_type", "binding_energy")
    if observable == "tr_M":
        # Per-row tr_M not yet plumbed in shards; defer to compute_tr_M.
        return Prediction(
            atom=row.get("element", "?") + str(Z + N),
            Z=Z, N=N,
            observable="tr_M",
            value=compute_tr_M(Z, N, precision_dps=precision_dps),
            units="dimensionless",
            method=method,
            precision_dps=precision_dps,
        )
    if observable == "mass":
        cm = row.get("composite_mass") or {}
        m_pred = cm.get("M_pred_MeV")
        m_ref = cm.get("M_AME_MeV")
        ppm = cm.get("err_ppm")
        if m_pred is None:
            if pt == "mass":
                m_pred = row.get("prediction_MeV_50dps")
                m_ref = row.get("reference_MeV_50dps")
                ppm = row.get("err_ppm")
        if m_pred is None:
            raise ValueError(
                f"no mass prediction available for (Z={Z}, N={N}); "
                "framework B_pred unavailable for this isotope"
            )
        return Prediction(
            atom=str(atom),
            Z=Z, N=N,
            observable="mass",
            value=Decimal(str(m_pred)),
            units="MeV",
            ppm_vs_codata=(Decimal(str(ppm)) if ppm is not None else None),
            method=row.get("layer", "?"),
            method_status="experimental" if row.get("layer") == "experimental" else None,
            precision_dps=precision_dps,
        )
    if observable == "binding_energy":
        if pt != "binding_energy":
            raise ValueError(
                f"(Z={Z}, N={N}) has prediction_type={pt!r}; binding "
                "energy is undefined for free nucleons (use "
                "observable='mass')"
            )
        b_pred = row.get("prediction_MeV_50dps")
        b_ref = row.get("reference_MeV_50dps")
        err_pct = row.get("err_pct")
        if b_pred is None:
            raise ValueError(
                f"no framework B prediction for (Z={Z}, N={N}); "
                f"layer = {row.get('layer','L?-pending')}"
            )
        return Prediction(
            atom=str(atom),
            Z=Z, N=N,
            observable="binding_energy",
            value=Decimal(str(b_pred)),
            units="MeV",
            ppm_vs_codata=(
                # `err_pct` arrives as a Decimal — the witness is loaded with
                # `parse_float=Decimal` to keep full precision — so `* 1e4`
                # raised TypeError: Decimal and float do not mix. This made
                # `predict()` raise for EVERY atom and every observable that
                # reaches this branch, which is most of them. Scaling by a
                # Decimal keeps the exactness the parse_float was chosen for;
                # `float(err_pct) * 1e4` would have silently thrown it away.
                Decimal(err_pct) * Decimal(10_000)
                if err_pct is not None else None
            ),
            method=row.get("layer", "?"),
            method_status="experimental" if row.get("layer") == "experimental" else None,
            precision_dps=precision_dps,
        )
    if observable == "mass_excess":
        # M − A·u (in MeV) = M_pred − A·u_MeV.
        #
        # READ from the registry, never retyped. The literal that stood below
        # was Decimal("931.49410242") — the CODATA-**2018** value — while
        # codata_constants moved this conversion to CODATA-2022
        # (931.49410372) deliberately in bean me3r, noting the AME2020
        # metadata carries the 2018 figure and the registry should not. So the
        # public facade was handing out a constant one edition behind the
        # registry it wraps. Owner ruling 2026-09-06: CODATA 2022.
        #
        # Lazy import, matching canonical_braid_crossings below: `_internal/`
        # is generated by scripts/sync-qou-mass-vendor.py and must not be
        # imported at module scope here.
        from ._internal.codata_constants import U_MEV  # noqa: PLC0415
        from mpmath import mp  # noqa: PLC0415

        # mp.nstr at an explicit width — `str(mpf)` renders at the AMBIENT
        # mp.dps and would silently truncate. U_MEV is 11 published digits, so
        # 20 is comfortably clear of it and adds no invented precision.
        with mp.workdps(60):
            _u_mev = Decimal(mp.nstr(U_MEV, 20, strip_zeros=True))
        m_pred_pred = predict(atom, "mass", precision_dps=precision_dps).value
        A = Z + N
        return Prediction(
            atom=str(atom),
            Z=Z, N=N,
            observable="mass_excess",
            value=Decimal(str(m_pred_pred)) - Decimal(A) * _u_mev,
            units="MeV",
            method=row.get("layer", "?"),
            method_status="experimental" if row.get("layer") == "experimental" else None,
            precision_dps=precision_dps,
        )
    raise ValueError(f"unknown observable: {observable!r}")


def predict_nucleon(
    particle: Particle,
    *,
    precision_dps: int = 50,
    emit_witness: bool = False,
    witness_path: str | None = None,
) -> Prediction:
    """Predict the mass of a single nucleon (or muon) via the
    Borromean tower."""
    if particle == "mu":
        # Muon not in per-Z shards; vendor from Borromean witness body.
        from importlib.resources import files
        b = json.loads(files("qou_mass.data").joinpath(
            "m-p-borromean-verification-50dps.witness.json"
        ).read_text(), parse_float=Decimal)
        d = b.get("data", b).get("muon_check", {})
        return Prediction(
            atom="mu",
            Z=0, N=0,
            observable="mass",
            value=Decimal(str(d["m_mu_pred_MeV"])),
            units="MeV",
            ppm_vs_codata=Decimal(str(d.get("rel_diff_ppm", "0"))),
            method="borromean-tower",
            precision_dps=precision_dps,
        )
    if particle == "p":
        return predict("p", observable="mass", precision_dps=precision_dps)
    if particle == "n":
        return predict("n", observable="mass", precision_dps=precision_dps)
    raise ValueError(f"unknown particle: {particle!r}")


def predict_table(
    atoms: Iterable[AtomLabel],
    **kwargs,
) -> list[Prediction]:
    """Predict every observable for every atom in the iterable."""
    return [predict(a, **kwargs) for a in atoms]


def compute_tr_M(
    Z: int,
    N: int,
    *,
    q: Decimal | None = None,
    precision_dps: int = 50,
    backend: Literal["python_mpmath", "rust"] = "python_mpmath",
    cache: bool = True,
) -> Decimal:
    """Compute |tr_M(β_atom(Z,N), q_0)| via the vendored markov_peel
    chain. P2 currently only supports the Python mpmath path."""
    if q is not None:
        raise NotImplementedError("custom q not yet wired in P2")
    if backend != "python_mpmath":
        raise NotImplementedError(
            "rust backend pending P3 (PyO3 bindings or subprocess)"
        )
    # Fast path: read from the L1 canonical-mass-table-extended
    # witness vendored in package data.
    cmte = json.loads(
        resources.files("qou_mass.data").joinpath(
            "canonical-mass-table-extended.witness.json"
        ).read_text(),
        parse_float=Decimal
    )
    for r in cmte.get("data", {}).get("rows", []):
        if r.get("Z") == Z and r.get("N") == N:
            tr = r.get("tr_M_q0_canonical_50dps")
            if tr:
                return Decimal(str(tr))
    raise ValueError(
        f"no |tr_M| value available for (Z={Z}, N={N}); P2 reads "
        "pre-computed values from vendored shards. Live recomputation "
        "via markov_peel is P3 work."
    )


def canonical_braid(Z: int, N: int) -> BraidWord:
    """Return the canonical braid word for atom (Z, N).

    Reads from the L1 canonical-mass-table-extended witness vendored in
    package data (covers p..⁶Li with full braid words). Outside that range
    it now COMPUTES the word from the vendored
    `_internal.canonical_braid_crossings`, which is live as of v1.0.0.

    The shard is still tried first, and deliberately: it is the recorded
    artifact, so preferring it keeps answers reproducible against a
    published witness rather than varying with the installed dependency
    set. The live path is the fallback, not the default.

    If the live path is unavailable — it needs `qou-substrate` and
    `pyhecke`, both real installs — the old behaviour returns: `n_strands`
    with an empty word, rather than an exception. Callers that only need
    the strand count keep working on a minimal install.
    """
    # Try the L1 canonical witness first.
    try:
        cmte = json.loads(
            resources.files("qou_mass.data").joinpath(
                "canonical-mass-table-extended.witness.json"
            ).read_text(),
            parse_float=Decimal
        )
        for r in cmte.get("data", {}).get("rows", []):
            if r.get("Z") == Z and r.get("N") == N:
                word = r.get("braid_word_canonical") or []
                n_strands = r.get("n_strands") or 3 * (Z + N)
                return BraidWord(
                    n_strands=n_strands,
                    generators=tuple(int(g[0]) for g in word),
                    crossing_types=tuple(str(g[1]) for g in word),
                )
    except (FileNotFoundError, ModuleNotFoundError):
        pass

    # Live path (v1.0.0). The whole transitive cone is vendored under
    # `_internal/` and generated by scripts/sync-qou-mass-vendor.py, so this
    # no longer depends on the caller having a `computations/` checkout.
    try:
        from ._internal.canonical_braid_crossings import (  # noqa: PLC0415
            atom_canonical_crossings,
        )
        word = atom_canonical_crossings(Z, N)
        return BraidWord(
            n_strands=3 * (Z + N),
            generators=tuple(int(g) for g, _ in word),
            crossing_types=tuple(str(t) for _, t in word),
        )
    except Exception:
        # Deliberately broad. The cone reaches numpy/sympy/mpmath plus
        # `qou-substrate` and `pyhecke`, and a partial install can fail in
        # more ways than ImportError -- the first attempt at this raised
        # NameError from a half-applied vendoring transform, and later
        # FileNotFoundError from a data file resolved by a path convention.
        # None of those should turn a strand-count query into a crash, so
        # the documented degraded answer below stands for all of them.
        pass

    # Degraded: strand count only, empty word.
    return BraidWord(
        n_strands=3 * (Z + N),
        generators=(),
        crossing_types=(),
    )
