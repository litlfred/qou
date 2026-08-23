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

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
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
    "deuteron": mp.mpf("2.224566"),
    "tritium": mp.mpf("8.481798"),
    "helium-3": mp.mpf("7.718041"),
    "helium-4": mp.mpf("28.295674"),
}

ISOTOPES = {
    "deuteron": (1, 1),
    "tritium": (1, 2),
    "helium-3": (2, 1),
    "helium-4": (2, 2),
}


def _load_chi_witness(path: Path) -> dict[tuple, mp.mpf]:
    """{λ_tuple: chi_value_mpf} from a chi-cache witness JSON."""
    w = json.loads(path.read_text())
    return {
        tuple(e["partition"]): mp.mpf(e["chi_lambda"])
        for e in w["by_partition"]
    }


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
        cached_q = w.get("q_str", w.get("q_0_50dps_str", w.get("q_inv_50dps_str")))
        cached_dps = w.get("dps")
        if (not w.get("partial", False)
                and cached_q == q_str
                and cached_dps == dps):
            return {tuple(e["partition"]): mp.mpf(e["chi_lambda"])
                    for e in w["by_partition"]}, legacy
        if cached_q is not None and cached_q != q_str:
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
    legacy.write_text(json.dumps({
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
    }, indent=2))
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
        E0 = m_e / (q0 * (q0 - 1))

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
        "B_arch_MeV": float(B_arch),
        "B_bar_MeV": float(B_bar),
        "AME_MeV": float(ame),
        "err_arch_pct": float(err_arch * 100),
        "err_bar_pct": float(err_bar * 100),
        "growth_channels_free": n_growth_free,
        "growth_channels_atom": n_growth_atom,
    }


def main(argv: list[str]) -> int:
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
        print(f"{r['atom']:<10}"
              f"{r['B_arch_MeV']:>10.4f}{r['B_bar_MeV']:>10.4f}"
              f"{r['AME_MeV']:>10.4f}"
              f"{r['err_arch_pct']:>+10.2f}{r['err_bar_pct']:>+10.2f}"
              f"{r['growth_channels_free']:>5d}/{r['growth_channels_atom']:<4d}",
              flush=True)
    out = HERE / "bar-pairing-binding-observable-extension.witness.json"
    witness = {
        "computation": "bar-pairing-binding-observable-extension",
        "description": (
            "Extension of PR #1742's bar-pairing observable to T, ³He, "
            "⁴He using the PR #1748 patched Rust kernel.  Confirms "
            "or refutes the deuteron's 'mirror underbinds by ~70%' "
            "finding across the light series."
        ),
        "results": results,
    }
    # Provenance envelope. This producer writes its witness as raw JSON, so
    # nothing stamps `scriptHash` — and a witness without one cannot be
    # compared against its producer, so it drops OUT of the self-staleness
    # audit and reads as "not stale" forever. Regenerating it then looks
    # like progress while removing it from the count: a false drain.
    # Full rationale and the detector: computations/witness_drain_audit.py.
    #
    # The dict was inlined into the `json.dumps` call; it is bound to a name
    # here so the stamp has something to mutate. NOTE: the OTHER raw write in
    # this file (the `legacy.write_text` at ~L152) is deliberately left alone
    # — that one rewrites three COMMITTED chi witnesses as this script's own
    # cache records, which is a separate defect (a producer and a cache must
    # not share a path) and is being tracked separately.
    #
    # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
    # fields in place and leaves the on-disk shape untouched.
    try:
        from witness_base import WitnessBuilder  # noqa: E402
    except ImportError:  # cluster subdir without the _path_bridge bootstrap
        import sys as _sys
        from pathlib import Path as _Path
        _sys.path.insert(0, str(next(
            _a / "substrate" for _a in _Path(__file__).resolve().parents
            if (_a / "substrate" / "witness_base.py").is_file())))
        from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__,
        engine=witness.get("engine", "rust+mpmath"))
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out.name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
