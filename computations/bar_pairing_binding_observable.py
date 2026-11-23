"""Bar-pairing binding observable — Rust-engine extension of PR #1742.

Reads two parallel chi-cache witnesses per atom:
  - `chi-{atom}-h{n}-at-q0-50dps.witness.json`    (substrate anchor)
  - `chi-{atom}-h{n}-at-qinv-50dps.witness.json`  (Hecke bar image)

and computes:

  B_arch(atom) = E_0 · Σ_λ y_λ · ( |χ^λ(W_free)|  −  |χ^λ(W_atom)| )
  B_bar(atom)  = E_0 · Σ_λ y_λ · ( ‖χ^λ(W_free)‖_bar
                                  − ‖χ^λ(W_atom)‖_bar )

where:
  - `|·|`      = ARCHIMEDEAN modulus at q_0 (conjugation bar; trivial
                  at real q_0 — the #1738 / #1742 convention)
  - `‖·‖_bar`  = HECKE/KL bar pairing length √(χ(q_0)·χ(q_0^{-1}))
  - y_λ        = canonical Wenzl weight (bar-symmetrized over q_0,
                  q_0^{-1}: (y_λ(q_0) + y_λ(q_0^{-1})) / 2 — real
                  by construction)
  - E_0 = m_e / (q_0 (q_0 − 1))  (#1742 calibration; CAL-1)

Inputs (per atom):
  - W_free is the "free" reference braid (Z protons + N neutrons each
    on their own H_3 → 3A strands free of inter-nucleon entanglement;
    `include_inter=False`)
  - W_atom is the bound braid with inter-nucleon entanglement
    (`include_inter=True`)

This script CONSUMES the witnesses produced by:
  - `chi_at_q0_via_hoefsmit_mpfr.py` (q_0  cache)
  - `chi_at_q_inv_via_native_mpfr.py` (q_0^{-1} cache, PR #1748 follow-up)

#1742 (`derive_binding_bar_pairing.py`) used pure-Python Hoefsmit
χ at TWO q-values per partition — minutes-slow for T, infeasible
for ⁴He.  This script uses the Rust kernel from PR #1748 (chi-cache
JSONs), so T/³He become instant and ⁴He becomes feasible (~10 min
wall per q-evaluation on a 4-core box).

q-usage discipline (per AGENTS.md §7c, §q-usage / fixed q_0 leak):

  - q_0 ≈ 1.110:  real, > 1, archimedean place ⇒ |·| is the
    conjugation bar (TRIVIAL on real χ — Im(χ(q_0)) = 0)
  - q_0^{-1} ≈ 0.901:  real, ∈ (0, 1), STILL archimedean — distinct
    archimedean evaluation, NOT a unit-circle / root-of-unity
    construction
  - Both points respect `lusztig_q_0_imaginary_part_zero` (the
    archimedean Im-zero constraint applies at the chosen anchor)
  - The bar-PAIRING `χ(q_0)·χ(q_0^{-1})` is a two-archimedean-point
    construction (fibre-level Hecke involution restricted to ℝ),
    not the conjugation bar of a single observation

Free/atom braid construction is delegated to:
  `mass_at_3A_proper.atom_braid_word_3A(Z, N, include_inter=…)`
which is the SAME source-of-truth used by the q_0 chi-cache.
"""
from __future__ import annotations

import json
import time
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401, E402

from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV  # noqa: E402,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from per_irrep_pole_atom import parts_of  # noqa: E402


# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# AME 2020 binding energies (MeV), for comparison only.
AME_B_MEV = {
    "deuteron": AME_B_DEUTERON_MEV_VALIDATION,
    "tritium": AME_B_TRITIUM_MEV_VALIDATION,
    "helium-3": AME_B_HE3_MEV_VALIDATION,
    "helium-4": AME_B_HE4_MEV_VALIDATION,
}

ISOTOPES = {
    "deuteron": (1, 1),
    "tritium": (1, 2),
    "helium-3": (2, 1),
    "helium-4": (2, 2),
}


def _os_path_basename(p: str) -> str:
    """Basename of a path, for the cache-ownership check (bean qou-w8rv)."""
    import os
    return os.path.basename(p)


def _load_chi_witness(path: Path) -> dict[tuple, mp.mpf]:
    """{λ_tuple: chi_value_mpf} from a chi-cache witness JSON."""
    w = json.loads(path.read_text())
    return {
        tuple(e["partition"]): mp.mpf(e["chi_lambda"])
        for e in w["by_partition"]
    }


# Field names under which a chi cache records the q it was computed at, PER CACHE KIND.
#
# WHY THIS IS KEYED ON `q_tag` AND NOT AN ORDERED FALLBACK CHAIN (bean qou-w8rv).  It was an
# inline chain looking for `q_str`, `q_0_50dps_str`, `q_inv_50dps_str`.  The canonical q0 caches,
# written by `chi_at_q0_via_hoefsmit_mpfr.py`, spell it **`q_0_50dps`** (no `_str`), so the chain
# returned None on every one of them, and the consequences compounded:
#
#   * `cached_q == q_str` became `None == <str>`, always False, so the cache NEVER hit;
#   * both diagnostics below are guarded by `cached_q is not None`, so nothing printed;
#   * the miss fell through to recompute-and-persist, OVERWRITING the canonical witness.
#
# A guard added to stop a stale witness being loaded was silently destroying the fresh one instead.
#
# AND AN ORDERED CHAIN CANNOT FIX IT, which is the part worth keeping.  A qinv witness records
# BOTH values -- `q_inv_50dps_str` (the q it was computed at) AND `q_0_50dps` (the anchor, as
# provenance).  Appending `q_0_50dps` to a shared chain therefore reads the ANCHOR off a qinv
# cache and reports a spurious miss on the qinv leg, which is exactly what the first version of
# this fix did.  Measured, not reasoned: the run printed
#
#   cache miss: chi-deuteron-h6-at-qinv-...json computed at q_str='1.1099...',
#               requested '0.9009...' -- recomputing
#
# The disambiguator is not an ordering, it is WHICH CACHE WE ARE READING.
_Q_CACHE_FIELDS = {
    # `q_str` first in both: this producer writes it with the q it was actually called with, so it
    # is unambiguous on a witness this producer wrote.
    "q0":   ("q_str", "q_0_50dps", "q_0_50dps_str"),
    "qinv": ("q_str", "q_inv_50dps_str", "q_inv_50dps"),
}


def _cached_q(w: dict, q_tag: str):
    """The q a chi-cache witness was computed at, for the cache kind `q_tag`.

    Returns None only when the witness records no q for that kind -- which must stay
    distinguishable from 'records a different q', because the caller prints different diagnostics
    for the two, and a None silences both.
    """
    for k in _Q_CACHE_FIELDS.get(q_tag, ()):
        v = w.get(k)
        if v is not None:
            return v
    return None


def _self_test() -> int:
    """Assert the guard reads the right q from every shape a chi cache is known to take.

    This exists because both failures it protects against were INVISIBLE: a lookup that names no
    field the data carries returns None and is indistinguishable from a legitimate cache miss, and
    a lookup that names the wrong one of two present fields reports a miss that looks legitimate.
    """
    Q0 = "1.1099785827513808075916690956107688798744991218736"
    QI = "0.90091828395574149216082288248109393601474162661054"
    cases = [
        # (name, q_tag, witness, expected)
        ("this producer, q0",        "q0",   {"q_str": Q0}, Q0),
        ("hoefsmit q0 cache",        "q0",   {"q_0_50dps": Q0}, Q0),
        ("suffixed q0",              "q0",   {"q_0_50dps_str": Q0}, Q0),
        ("this producer, qinv",      "qinv", {"q_str": QI}, QI),
        # THE REGRESSION: a qinv cache carries the anchor too.  Reading q_0_50dps here is the bug
        # the first version of this fix introduced.
        ("qinv cache, BOTH present", "qinv", {"q_inv_50dps_str": QI, "q_0_50dps": Q0}, QI),
        ("no q recorded",            "q0",   {"dps": 50}, None),
    ]
    fails = []
    for name, tag, w, want in cases:
        got = _cached_q(w, tag)
        if got != want:
            fails.append(f"{name}: got {got!r}, want {want!r}")
    # Against the real committed witnesses, both kinds, so the test cannot pass on toy data alone.
    for pat, tag, want in ((f"chi-deuteron-h6-at-q0-50dps.witness.json", "q0", Q0),
                           (f"chi-deuteron-free-h6-at-qinv-50dps.witness.json", "qinv", QI)):
        f = HERE / pat
        if f.exists():
            got = _cached_q(json.loads(f.read_text()), tag)
            if got != want:
                fails.append(f"committed {pat}: got {got!r}, want the {tag} value")
    for f in fails:
        print(f"bar-pairing SELF-TEST FAILED: {f}", file=sys.stderr)
    if not fails:
        print(f"bar-pairing: cache-key self-test passed ({len(cases) + 2}/{len(cases) + 2})")
    return 1 if fails else 0


def _load_or_compute_chi(atom: str, n: int, kind: str, q_str: str,
                         q_tag: str, dps: int, word_signed):
    """{λ: χ} for one (atom, kind, q-value).

    Looks for `chi-{atom}-{kind}-h{n}-at-{q_tag}-50dps.witness.json`
    (kind ∈ {"atom", "free"}).  Backward compatible with the old
    ATOM-only naming `chi-{atom}-h{n}-at-q0-50dps.witness.json` and
    `chi-{atom}-h{n}-at-qinv-50dps.witness.json`.  If absent OR
    partial, recomputes via the Rust kernel and persists.
    """
    import pyhecke_native as pn
    if kind == "atom":
        legacy = HERE / f"chi-{atom}-h{n}-at-{q_tag}-50dps.witness.json"
    else:
        legacy = HERE / f"chi-{atom}-{kind}-h{n}-at-{q_tag}-50dps.witness.json"
    if legacy.exists():
        w = json.loads(legacy.read_text())
        # Cache-key validation (Copilot review PR #1748): the filename
        # alone does NOT encode q_str + dps.  A future q_0 re-pin or a
        # different precision request would otherwise silently load a
        # stale witness.  Re-run if the on-disk fields disagree.
        cached_q = _cached_q(w, q_tag)
        cached_dps = w.get("dps")
        if (not w.get("partial", False)
                and cached_q == q_str
                and cached_dps == dps):
            return {tuple(e["partition"]): mp.mpf(e["chi_lambda"])
                    for e in w["by_partition"]}, legacy
        # Checked BEFORE the diagnostics below, so the 'recomputing'
        # messages are only printed on paths that really do recompute.
        # Refuse to destroy a file another producer owns. Reaching here
        # means the cache genuinely disagrees, and overwriting a
        # canonical at-q0 witness with this script's schema is never the
        # right repair -- re-run its own producer instead.
        _owner = w.get("producer")
        if _owner and _owner != _os_path_basename(__file__):
            raise RuntimeError(
                f"{legacy.name} was written by {_owner!r}, not by this "
                f"script, and its cached q ({cached_q!r}) does not match "
                f"the requested {q_str!r}. Refusing to overwrite it with "
                f"a different schema (bean qou-w8rv). Re-run {_owner} to "
                f"regenerate it, then re-run this script."
            )
        if cached_q is None:
            # Was silent before: both diagnostic branches below are
            # guarded on `cached_q is not None`, so an unrecognised
            # schema recomputed and clobbered without printing anything.
            print(f"[{atom}] cache miss: {legacy.name} carries no "
                  f"recognised q field (keys: "
                  f"{sorted(k for k in w if k != 'by_partition')}) "
                  f"— recomputing", flush=True)
        elif cached_q != q_str:
            print(f"[{atom}] cache miss: {legacy.name} computed at "
                  f"q_str={cached_q!r}, requested {q_str!r} — recomputing",
                  flush=True)
        elif cached_dps is not None and cached_dps != dps:
            print(f"[{atom}] cache miss: {legacy.name} computed at "
                  f"dps={cached_dps}, requested {dps} — recomputing",
                  flush=True)
    # Compute fresh.
    print(f"[{atom}] computing {kind}@{q_tag} (n={n}, "
          f"{len(word_signed)}fac) — caching to {legacy.name}",
          flush=True)
    t0 = time.time()
    out = pn.chi_lambda_all_partitions_mpfr(n, word_signed, q_str, dps)
    elapsed = time.time() - t0
    print(f"[{atom}] {kind}@{q_tag} done in {elapsed:.2f}s", flush=True)
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload_1 = {
        "computation": f"chi-{atom}-{kind}-h{n}-at-{q_tag}-50dps",
        "atom": atom, "kind": kind,
        "n_strands": n,
        "dps": dps,
        "q_str": q_str,
        "n_partitions": len(out),
        "n_partitions_total": len(out),
        "partial": False,
        "compute_time_sec": round(elapsed, 2),
        "by_partition": [{"partition": list(lam), "chi_lambda": s}
                         for lam, s in out],
        "_provenance": {
            "engine": "pyhecke_native",
            "rust_fn": "chi_lambda_all_partitions_mpfr",
            "pr_landing_kernel": 1748,
            "pr_consumer": 1742,
        },
    }
    _prov_payload_1.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload_1, script_path=__file__, engine=None, q0_anchor=None)
    legacy.write_text(json.dumps(_prov_payload_1, indent=2))
    return {tuple(lam): mp.mpf(s) for lam, s in out}, legacy


def _free_atom_chi_via_native(atom: str, Z: int, N: int, q_str: str,
                              q_tag: str, dps: int) -> tuple[dict, dict]:
    """χ_λ over the FREE-reference + ATOMIC braid words at q = q_str.

    Cache-aware (PR #1748 follow-up): reuses
    `chi-{atom}(-{kind})-h{n}-at-{q_tag}-50dps.witness.json` when
    available; only the missing one(s) trigger a fresh Rust call.

    The Rust kernel takes the same signed-word translation as
    `chi_at_q_inv_via_native_mpfr._word_to_signed`.
    """
    from chi_at_q_inv_via_native_mpfr import _word_to_signed

    A = Z + N
    n = 3 * A
    word_free = atom_braid_word_3A(Z, N, include_inter=False)
    word_atom = atom_braid_word_3A(Z, N, include_inter=True)
    ws_free = _word_to_signed(word_free)
    ws_atom = _word_to_signed(word_atom)
    free, _ = _load_or_compute_chi(atom, n, "free", q_str, q_tag, dps,
                                    ws_free)
    atom_chi, _ = _load_or_compute_chi(atom, n, "atom", q_str, q_tag, dps,
                                       ws_atom)
    return free, atom_chi


def compute_atom(atom: str) -> dict:
    """B_arch + B_bar for one atom via the Rust kernel.

    Uses CACHED chi at q_0 (from chi_at_q0_via_hoefsmit_mpfr.py output)
    where available; otherwise recomputes via Rust.  The bar-image
    chi at q_0^{-1} must come from chi_at_q_inv_via_native_mpfr.py.
    """
    Z, N = ISOTOPES[atom]
    A = Z + N
    n = 3 * A
    q0_str = Q_50_DIGIT_STR
    with mp.workdps(60):
        q0 = mp.mpf(q0_str)
        qi = 1 / q0
        qi_str = mp.nstr(qi, 50, strip_zeros=False)
        m_e = mp.mpf(str(M_E_MEV))
        import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
        E0 = _qbeta_e0.order_zero_scaled(m_e, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

    print(f"[{atom}] computing B_arch + B_bar  "
          f"(n={n}, Z={Z}, N={N}, A={A})", flush=True)

    # We need the ATOMIC-braid chi and the FREE-reference braid chi
    # at BOTH q_0 and q_0^{-1}.  The current q_0 cache is ATOMIC-only;
    # re-run via Rust to cover both free + atom at both q-values.
    print(f"[{atom}]   q_0 evaluation …", flush=True)
    free_q0, atom_q0 = _free_atom_chi_via_native(atom, Z, N, q0_str, "q0", 50)
    print(f"[{atom}]   q_0^-1 evaluation …", flush=True)
    free_qi, atom_qi = _free_atom_chi_via_native(atom, Z, N, qi_str, "qinv", 50)

    # y_λ at both q-values — #1742 bar-symmetrizes
    # (y(q_0) + y(q_0^{-1})) / 2 as the real bar-invariant weight.
    y0 = {}
    yi = {}
    for shape in parts_of(n):
        lam = tuple(shape)
        y0[lam] = y_lambda_wenzl_bridge_numeric(lam, q0_str, dps=50)
        yi[lam] = y_lambda_wenzl_bridge_numeric(lam, qi_str, dps=50)

    B_arch = mp.mpf(0)
    B_bar = mp.mpf(0)
    n_growth_free = 0
    n_growth_atom = 0
    for lam in free_q0:
        chi_free_0 = free_q0.get(lam)
        chi_atom_0 = atom_q0.get(lam)
        chi_free_i = free_qi.get(lam)
        chi_atom_i = atom_qi.get(lam)
        if any(x is None for x in
               (chi_free_0, chi_atom_0, chi_free_i, chi_atom_i)):
            continue
        y0_lam = y0.get(lam)
        yi_lam = yi.get(lam)
        if y0_lam is None or yi_lam is None:
            continue
        # Archimedean per-block: |χ(q_0)| (conjugation bar at real q_0
        # is trivial, so reduces to the modulus; we take re(y0) ·
        # |re(χ)| to mirror #1742's convention exactly).
        B_arch += mp.re(y0_lam) * (abs(mp.re(chi_free_0))
                                   - abs(mp.re(chi_atom_0)))
        # Bar pairing: √(χ(q_0)·χ(q_0^{-1})) per channel.
        y_bar = mp.re((y0_lam + yi_lam) / 2)
        pair_free = mp.re(chi_free_0 * chi_free_i)
        pair_atom = mp.re(chi_atom_0 * chi_atom_i)
        if pair_free < 0:
            n_growth_free += 1
            length_free = mp.sqrt(-pair_free)   # |imaginary length|
        else:
            length_free = mp.sqrt(pair_free)
        if pair_atom < 0:
            n_growth_atom += 1
            length_atom = mp.sqrt(-pair_atom)
        else:
            length_atom = mp.sqrt(pair_atom)
        B_bar += y_bar * (length_free - length_atom)

    B_arch *= E0
    B_bar *= E0
    ame = AME_B_MEV[atom]
    err_arch = (B_arch - ame) / ame
    err_bar = (B_bar - ame) / ame
    return {
        "atom": atom, "Z": Z, "N": N, "A": A, "n_strands": n,
        # `fmt`, NOT `float`. All five are mpf at this point -- `B_arch` and
        # `B_bar` are accumulated in mpmath, `ame` is an mpf constant
        # (`AME_B_*_MEV_VALIDATION`), and the two errors are mpf ratios -- so
        # `float()` was a pure truncation applied at serialization time, and
        # the witness recorded binary64. That is what the raw-float64 ratchet
        # saw (this witness read 5 -> 20 REGRESSED).
        #
        # NOTE the two audits disagree about this line ON PURPOSE, and both
        # are right about their own question. `audits/float64_leak_audit.py`
        # EXEMPTS it by `DICT_VALUE_RX`, citing `"B_arch_MeV": float(B_arch)`
        # by name as its worked false positive -- correctly, because it asks
        # "did a float enter a COMPUTE path?" and the answer is no. The
        # ratchet asks "did a float enter a WITNESS?" and the answer is yes.
        # Do not read the leak audit's exemption as a licence here.
        "B_arch_MeV": fmt(B_arch),
        "B_bar_MeV": fmt(B_bar),
        "AME_MeV": fmt(ame),
        "err_arch_pct": fmt(err_arch * 100),
        "err_bar_pct": fmt(err_bar * 100),
        "growth_channels_free": n_growth_free,
        "growth_channels_atom": n_growth_atom,
    }


def main(argv: list[str]) -> int:
    # Both spellings, so neither `precision-gates.sh` (--self-test) nor a hand run (--selftest)
    # can report a sound detector as a no-op -- the qou-7u0d failure, avoided by construction.
    if argv and argv[0] in ("--self-test", "--selftest"):
        return _self_test()
    set_compute_dps()
    if argv:
        atoms = argv
    else:
        atoms = list(ISOTOPES)
    print(f"{'atom':<10}{'B_arch':>10}{'B_bar':>10}{'AME':>10}"
          f"{'arch%':>10}{'bar%':>10}{'growth':>10}", flush=True)
    results = []
    for atom in atoms:
        r = compute_atom(atom)
        results.append(r)
        # These five row fields are now serialized strings (see `compute_atom`),
        # so re-parse for the console table. `float()` inside an f-string is
        # display, which is the one place the NO-FLOAT64 rule permits it.
        print(f"{r['atom']:<10}"
              f"{float(r['B_arch_MeV']):>10.4f}{float(r['B_bar_MeV']):>10.4f}"
              f"{float(r['AME_MeV']):>10.4f}"
              f"{float(r['err_arch_pct']):>+10.2f}"
              f"{float(r['err_bar_pct']):>+10.2f}"
              f"{r['growth_channels_free']:>5d}/{r['growth_channels_atom']:<4d}",
              flush=True)
    out = HERE / "bar-pairing-binding-observable-extension.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload_2 = {
        "computation": "bar-pairing-binding-observable-extension",
        "description": (
            "Extension of PR #1742's bar-pairing observable to T, ³He, "
            "⁴He using the PR #1748 patched Rust kernel.  Confirms "
            "or refutes the deuteron's 'mirror underbinds by ~70%' "
            "finding across the light series."
        ),
        "results": results,
    }
    _prov_payload_2.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload_2, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(_prov_payload_2, indent=2))
    print(f"\nWitness: {out.name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
