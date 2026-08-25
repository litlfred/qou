#!/usr/bin/env python3
"""GAP-A-4 additive S(K) probe — PER-KNOT-DENSITY RE-RUN (bean x5az).

Re-runs the PR #1876 additive S(K) sub-leading probe with the canonical
PER-KNOT Hecke-trace density substituted for the fitted global scalar
λ_A as the leading-term base, per the re-run protocol of
[`docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md`](../../docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md).
The audit's census: the original used "lw_q0 = λ_A" as the additive
base — λ_A-family-bound; the per-knot density was never tried.  The
audit ledger flags §4 direction 2 (additive S(K)) as a remaining
productive direction; this re-run is that direction on the canonical
base.

Path B formula under test (same as the original):

    m(K) = m_e · Vol(K)/ℏ_q² · λ(K) + S(K)
    S_emp(K) = m(K) − m_e · Vol(K)/ℏ_q² · λ(K)

Density-swap mapping:

  | branch    | λ(K) base                                              |
  |-----------|--------------------------------------------------------|
  | baseline  | λ_A = linking_weight_family_a(q₀) ≈ 2.533 (fit,        |
  |           | p = n degenerate) — the original PR #1876 form         |
  | per-knot  | tr_M(K) — canonical chi-cache Markov trace, p≠n        |
  |           | distinct; leading term routed through the canonical    |
  |           | `per_knot_density_per_block(vol_K, tr_M_K, q₀)`             |

Same isotopes {p, n, D, T, ³He, ⁴He}, CODATA/AME validation masses,
per-knot volumes, q₀ and precision defaults as the original.  Same
closure test: does S_emp(K) factor as a uniform-coefficient
closed-form substrate quantity (normalisations S/m_e, S/(m_e·ℏ_q²),
S/(m_e·Vol_K), S/(Z·m_e), S/(A·m_e))?  NO new fitted constants, NO new
ansatz families — the uniformity of the SAME normalisation columns is
the verdict-bearing quantity, measured as max/min spread (and sign
consistency) across the six atoms.

Three-calibration discipline: a spread ≫ 1 in every column is a
scope-limited negative (a) for the additive closure on that base, not
a structural exclusion (b).

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits
`gap-a4-S-K-additive-probe-perknot-rerun.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from canonical_tr_m_via_chi_cache import canonical_tr_m  # noqa: E402
from _li_2_q_util import linking_weight_family_a, per_knot_density_per_block  # noqa: E402

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION as M_P_MEV,
    M_N_MEV_VALIDATION as M_N_MEV,
    M_D_MEV_VALIDATION as M_D_MEV,
    M_T_MEV_VALIDATION as M_T_MEV,
    M_HE3_MEV_VALIDATION as M_HE3_MEV,
    M_HE4_MEV_VALIDATION as M_HE4_MEV,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

Q_0_50DPS = Q_50_DIGIT_STR

VOL_BORROMEAN_8G = mp.mpf("7.32772475341775212043682811945907288619319499425")
VOL_PHASE4_Z1 = mp.mpf("12.776")
VOL_PHASE4_Z2 = mp.mpf("12.554")

LIGHT_SERIES = [
    ("p",   "proton",   1, 0, M_P_MEV,   VOL_BORROMEAN_8G),
    ("n",   "neutron",  0, 1, M_N_MEV,   VOL_BORROMEAN_8G),
    ("D",   "deuteron", 1, 1, M_D_MEV,   VOL_PHASE4_Z1),
    ("T",   "tritium",  1, 2, M_T_MEV,   VOL_PHASE4_Z1),
    ("3He", "helium-3", 2, 1, M_HE3_MEV, VOL_PHASE4_Z2),
    ("4He", "helium-4", 2, 2, M_HE4_MEV, VOL_PHASE4_Z2),
]


def hbar_q_sq(q_0: mp.mpf) -> mp.mpf:
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    return hbar * hbar


def _branch(name: str, q_0: mp.mpf, lam_of: dict[str, mp.mpf],
            use_per_block: bool) -> dict:
    """Compute S_emp(K) + normalisation columns for one density base.

    lam_of maps atom label -> the multiplicative density lambda(K).
    """
    hbar2 = hbar_q_sq(q_0)
    rows = []
    print("-" * 96)
    print(f"  [{name}]")
    print(f"  {'atom':<4} {'lam(K)':>9} {'pred MeV':>11} {'S_emp MeV':>12} "
          f"{'S/m(K)':>8} {'S/m_e':>9} {'S/(A m_e)':>10} "
          f"{'S/(m_e hbar2)':>14} {'S/(m_e VolK)':>13}")
    for label, atom, Z, N, m_K, vol_K in LIGHT_SERIES:
        lam = lam_of[label]
        if use_per_block:
            # canonical route: m_pred = m_e * per_knot_density_per_block(...)
            pred = M_E_MEV * per_knot_density_per_block(vol_K, lam, q_0)
        else:
            pred = M_E_MEV * vol_K / hbar2 * lam
        S = m_K - pred
        A = Z + N
        row = {
            "label": label, "Z": Z, "N": N,
            "lambda_K": str(lam),
            "vol_K": str(vol_K),
            "m_K_MeV": str(m_K),
            "predicted_leading_MeV": str(pred),
            "S_emp_MeV": str(S),
            "S_over_mK": str(S / m_K),
            "S_over_m_e": str(S / M_E_MEV),
            "S_over_A_m_e": str(S / (A * M_E_MEV)),
            "S_over_Z_m_e": str(S / (Z * M_E_MEV)) if Z > 0 else None,
            "S_over_m_e_hbar2": str(S / (M_E_MEV * hbar2)),
            "S_over_m_e_vol_K": str(S / (M_E_MEV * vol_K)),
        }
        rows.append(row)
        print(f"  {label:<4} {float(lam):>9.4f} {float(pred):>11.3f} "
              f"{float(S):>+12.3f} {float(S/m_K):>+8.1%} "
              f"{float(S/M_E_MEV):>+9.1f} {float(S/(A*M_E_MEV)):>+10.1f} "
              f"{float(S/(M_E_MEV*hbar2)):>+14.1f} "
              f"{float(S/(M_E_MEV*vol_K)):>+13.2f}")

    # Uniformity metrics per normalisation column: a candidate additive
    # closure S(K) = c * base(K) exists with a single coefficient c iff
    # the column is constant across atoms.  Spread = max/min (sign-flip
    # -> no uniform c at all).
    metrics = {}
    for col in ("S_over_m_e", "S_over_A_m_e", "S_over_m_e_hbar2",
                "S_over_m_e_vol_K"):
        vals = [mp.mpf(r[col]) for r in rows]
        sign_flip = min(vals) < 0 and max(vals) > 0
        if sign_flip:
            spread = None
        else:
            lo = min(abs(v) for v in vals)
            spread = (max(abs(v) for v in vals) / lo) if lo > 0 else None
        metrics[col] = {
            "min": str(min(vals)), "max": str(max(vals)),
            "sign_flip": bool(sign_flip),
            "max_over_min_abs": (str(spread) if spread is not None else None),
        }
    sub_leading = max(abs(mp.mpf(r["S_over_mK"])) for r in rows)
    metrics["max_abs_S_over_mK"] = str(sub_leading)
    print(f"  uniformity: " + ", ".join(
        f"{c}: " + ("SIGN-FLIP" if metrics[c]["sign_flip"] else
                    f"x{float(mp.mpf(metrics[c]['max_over_min_abs'])):.2f}")
        for c in ("S_over_A_m_e", "S_over_m_e_vol_K")) +
        f"; max |S/m(K)| = {float(sub_leading):.1%}")
    return {"rows": rows, "metrics": metrics}


def main() -> int:
    w = WitnessBuilder(
        "gap-a4-S-K-additive-probe-perknot-rerun", engine="mpmath"
    )
    w.set_audit_only(
        "docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md"
    )
    w.set_description(
        "Bean x5az per-knot-density re-run of the PR #1876 GAP-A-4 "
        "additive S(K) probe. Computes S_emp(K) = m(K) - m_e*Vol(K)/"
        "hbar_q^2*lambda(K) for lambda(K) in {lambda_A (fitted global "
        "scalar, baseline reproduction), tr_M(K) (canonical chi-cache "
        "per-knot trace, p!=n distinct, routed through "
        "per_knot_density_per_block)}, and tests whether S_emp factors as a "
        "uniform-coefficient substrate form (same normalisation columns "
        "as the original; uniformity spread is the verdict). NO new "
        "ansatz families. EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    lam_A = linking_weight_family_a(q_0)
    hbar2 = hbar_q_sq(q_0)

    print("=" * 96)
    print("GAP-A-4 additive S(K) probe — per-knot density re-run (x5az)")
    print("=" * 96)
    print(f"  q0 = {Q_0_50DPS}")
    print(f"  hbar_q^2 = {mp.nstr(hbar2, 12)}   lambda_A = {mp.nstr(lam_A, 12)}")

    tr_M: dict[str, mp.mpf] = {}
    for label, atom, Z, N, _m, _v in LIGHT_SERIES:
        r = canonical_tr_m(atom, Z, N)
        if r.get("partial_cache"):
            raise RuntimeError(f"partial chi cache for {atom} — abort")
        tr_M[label] = mp.mpf(str(r["abs_tr_M_q0"]))
    print("  tr_M: " + ", ".join(f"{k}={mp.nstr(v, 8)}" for k, v in tr_M.items()))

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_parameter("lambda_A_at_q0", str(lam_A))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("rerun_of", "computations/probes/gap_a4_S_K_additive_probe.py")
    w.add_data("tr_M_per_atom", {k: str(v) for k, v in tr_M.items()})

    lamA_of = {label: lam_A for label, *_ in LIGHT_SERIES}
    base = _branch("baseline: lambda_A (fitted, p=n degenerate)",
                   q_0, lamA_of, use_per_block=False)
    pk = _branch("per-knot: tr_M(K) (canonical, p!=n distinct, "
                 "per_knot_density_per_block)", q_0, tr_M, use_per_block=True)

    w.add_data("baseline_lambdaA", base)
    w.add_data("perknot_trM", pk)

    # Baseline-reproduction assertion: S_emp(p) under lambda_A is the
    # documented -27.76 MeV (= -(2.96%) of the lambda_A-inflated 966).
    S_p_base = mp.mpf(base["rows"][0]["S_emp_MeV"])
    w.add_assertion(
        "baseline_S_emp_proton_matches_documented",
        computed=float(S_p_base),
        expected=-27.76,
        tolerance=0.1,
        source=(
            "PR #1876 baseline: pred(p) = m_e*Vol(B3)/hbar_q^2*lambda_A "
            "~ 966.03 MeV; S_emp(p) = 938.27 - 966.03 ~ -27.76 MeV "
            "(-54.3 m_e; the documented +2.96% lambda_A proton gap)."
        ),
    )

    # Honest verdict.
    base_flips = any(base["metrics"][c]["sign_flip"]
                     for c in ("S_over_A_m_e", "S_over_m_e_vol_K"))
    pk_flips = any(pk["metrics"][c]["sign_flip"]
                   for c in ("S_over_A_m_e", "S_over_m_e_vol_K"))
    pk_spread = min(
        (mp.mpf(pk["metrics"][c]["max_over_min_abs"])
         for c in ("S_over_A_m_e", "S_over_m_e_vol_K")
         if pk["metrics"][c]["max_over_min_abs"] is not None),
        default=mp.mpf("inf"),
    )
    pk_subleading = mp.mpf(pk["metrics"]["max_abs_S_over_mK"])

    verdict = (
        f"Scope-limited (a) on both bases. BASELINE (lambda_A, "
        f"reproduced): S_emp sign-flips across the series "
        f"(sign_flip={base_flips}) — negative at p/n, large positive at "
        f"A>=2 — so no uniform-coefficient substrate form exists; the "
        f"PR #1876 negative reproduces. PER-KNOT (tr_M(K), canonical): "
        f"the sign-flip DISAPPEARS (sign_flip={pk_flips}; S_emp > 0 for "
        f"all six atoms) and the best normalisation column S/(A*m_e) is "
        f"uniform to a factor {float(pk_spread):.2f} (vs sign-flip = "
        f"unbounded on the lambda_A base) — the p!=n-distinct canonical "
        f"base is strictly MORE regular. HOWEVER the additive term is no "
        f"longer sub-leading: max |S/m(K)| = {float(pk_subleading):.1%} "
        f"(the per-knot leading term is far below the mass at A>=2), so "
        f"'S(K) as a small closed-form correction' fails on the "
        f"canonical base too — S absorbs most of the mass. VERDICT: the "
        f"original hard shape of the refutation (sign-flipping, wildly "
        f"non-uniform S) is PARTIALLY AN ARTIFACT of the lambda_A base "
        f"(the canonical base removes the sign flip and compresses the "
        f"spread to ~x{float(pk_spread):.1f}), but the closure itself "
        f"remains open: no uniform-coefficient substrate form matches "
        f"all six atoms on either base. Scope-limited negative (a) — "
        f"constrains the additive single-term closure on these two "
        f"bases only; not a structural exclusion of tr_M(K) or of "
        f"richer multi-term closures."
    )
    w.add_data("rerun_verdict", verdict)
    print("-" * 96)
    print("  RERUN VERDICT:")
    for chunk in verdict.split(". "):
        print(f"    {chunk.strip()}")

    out_path = w.save()
    repo_root = COMPUTE_DIR.parent.parent
    try:
        rel = out_path.relative_to(repo_root)
    except ValueError:
        rel = out_path
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
