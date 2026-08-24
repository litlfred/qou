#!/usr/bin/env python3
"""GAP-A-4 ³He L1b residual probe — PER-KNOT-DENSITY RE-RUN (bean x5az).

Re-runs the PR #1882 ³He L1b residual structural probe with the
canonical PER-KNOT Hecke-trace density substituted for the fitted
global scalar λ_A in the λ_A-family candidate ansätze, per the re-run
protocol of
[`docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md`](../../docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md).
The audit's census: this probe "tests λ_A/2, (λ_A/[2]_q)^½ ansätze" —
λ_A-family-bound; the per-knot density was never tried.

The probe target is UNCHANGED (it contains no λ_A): the residual ratio

    residual_ratio = λ_emp(³He) / L1b(³He) ≈ 1.2218
    (equivalently PR #1874's −18.15 % L1b ³He rel_err)

Density-swap mapping (same functional forms, base swapped; NO new
ansatz families):

  | λ_A baseline (PR #1882)  | per-knot re-run analogue                       |
  |--------------------------|------------------------------------------------|
  | λ_A / 2                  | base / 2                                       |
  | (λ_A / [2]_q)^½          | (base / [2]_q)^½                               |
  | (λ_A bare — implicit)    | base (bare)                                    |

with TWO per-knot bases, exposing the p≠n structure the degenerate
λ_A erases:

  base₁ = tr_M(³He)                — the atom's own canonical H₉ trace
                                     (chi-cache, ≈ 0.2066)
  base₂ = tr_M(p)²·tr_M(n)         — constituent per-nucleon product
                                     (Z=2, N=1; p ≈ 1.0653 ≠ n ≈ 0.9232)

Same q₀, masses, volumes, precision defaults and verdict thresholds
(<0.5 % / <5 % / <25 % / REFUTED) as the original.

Three-calibration discipline: no new fitted constants; a failure here
is a scope-limited negative (a) for these functional forms on these
bases, never a structural exclusion (b).

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits
`gap-a4-He3-residual-probe-perknot-rerun.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from canonical_tr_m_via_chi_cache import canonical_tr_m  # noqa: E402
from _li_2_q_util import linking_weight_family_a  # noqa: E402
from codata_constants import M_E_MEV, M_HE3_MEV_VALIDATION as M_HE3_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

Q_0_50DPS = Q_50_DIGIT_STR

VOL_BORROMEAN_8G = mp.mpf("7.32772475341775212043682811945907288619319499425")
VOL_PHASE4_Z2 = mp.mpf("12.554")


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    if n == 0:
        return sp.Integer(0)
    return sp.Add(*(q ** (2 * k - (n - 1)) for k in range(n)))


def hbar_q_sq(q_0: mp.mpf) -> mp.mpf:
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    return hbar * hbar


def evaluate(expr: sp.Expr, q_0: mp.mpf) -> mp.mpf:
    dps = mp.mp.dps
    q_float = sp.Float(str(q_0), dps)
    subs = {sym: q_float for sym in expr.free_symbols}
    return mp.mpf(str(sp.N(expr.subs(subs), dps)))


def _verdict(rel: mp.mpf) -> str:
    a = abs(rel)
    if a < mp.mpf("5e-3"):
        return "EXACT-MATCH (<0.5%)"
    if a < mp.mpf("5e-2"):
        return "NEAR-MATCH (<5%)"
    if a < mp.mpf("0.25"):
        return "NEAR-MATCH (<25%)"
    return "REFUTED"


def main() -> int:
    w = WitnessBuilder(
        "gap-a4-He3-residual-probe-perknot-rerun", engine="sympy+mpmath"
    )
    w.set_audit_only(
        "docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md"
    )
    w.set_description(
        "Bean x5az per-knot-density re-run of the PR #1882 3He L1b "
        "residual probe. The residual target lambda_emp/L1b ~ 1.2218 is "
        "density-independent (reproduced as baseline). The lambda_A-family "
        "candidates (lambda_A/2, sqrt(lambda_A/[2]_q)) are re-tested with "
        "the canonical per-knot bases tr_M(3He) (chi-cache H9) and "
        "tr_M(p)^2*tr_M(n) (p!=n constituent product) substituted for "
        "lambda_A — same functional forms, no new ansatz families. "
        "EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    q_sym = sp.Symbol("q", positive=True)
    lam_A = linking_weight_family_a(q_0)
    two_q = evaluate(q_number_sym(2, q_sym), q_0)

    # --- Baseline target reproduction (identical to the original) ---
    A_he3 = (VOL_PHASE4_Z2 / evaluate(q_number_sym(8, q_sym), q_0)
             * evaluate(q_number_sym(3, q_sym) ** 2, q_0)
             * evaluate((sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** 4, q_0))
    L1b_he3 = A_he3 * VOL_PHASE4_Z2 / VOL_BORROMEAN_8G * hbar_q_sq(q_0)
    lambda_emp_he3 = M_HE3_MEV * hbar_q_sq(q_0) / (M_E_MEV * VOL_PHASE4_Z2)
    residual_ratio = lambda_emp_he3 / L1b_he3

    # --- Per-knot bases (chi-cache, p != n distinct) ---
    tr_he3 = mp.mpf(str(canonical_tr_m("helium-3", 2, 1)["abs_tr_M_q0"]))
    tr_p = mp.mpf(str(canonical_tr_m("proton", 1, 0)["abs_tr_M_q0"]))
    tr_n = mp.mpf(str(canonical_tr_m("neutron", 0, 1)["abs_tr_M_q0"]))
    tr_constituent = tr_p ** 2 * tr_n  # Z=2, N=1

    print("=" * 78)
    print("GAP-A-4 3He L1b residual probe — per-knot density re-run (x5az)")
    print("=" * 78)
    print(f"  A_Phase-4(3He)             = {mp.nstr(A_he3, 12)}")
    print(f"  L1b(3He)                   = {mp.nstr(L1b_he3, 12)}")
    print(f"  lambda_emp(3He)            = {mp.nstr(lambda_emp_he3, 12)}")
    print(f"  residual_ratio (target)    = {mp.nstr(residual_ratio, 12)}")
    print(f"  (PR #1874 check: 1 - 1/r   = {float(1 - 1/residual_ratio):.4%})")
    print(f"  lambda_A (fitted)          = {mp.nstr(lam_A, 12)}")
    print(f"  tr_M(3He)  [H9 chi-cache]  = {mp.nstr(tr_he3, 12)}")
    print(f"  tr_M(p), tr_M(n)  [H3]     = {mp.nstr(tr_p, 12)}, {mp.nstr(tr_n, 12)}")
    print(f"  tr_M(p)^2*tr_M(n)          = {mp.nstr(tr_constituent, 12)}")

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("residual_ratio_target", str(residual_ratio))
    w.add_parameter("lambda_A_at_q0", str(lam_A))
    w.add_parameter("tr_M_He3", str(tr_he3))
    w.add_parameter("tr_M_p", str(tr_p))
    w.add_parameter("tr_M_n", str(tr_n))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("rerun_of", "computations/probes/gap_a4_He3_residual_probe.py")

    # Same functional forms; base in {lambda_A (baseline), tr_M(3He),
    # tr_M(p)^2*tr_M(n)}.
    def family(tag: str, base: mp.mpf) -> list[tuple[str, mp.mpf]]:
        return [
            (f"{tag}",               base),
            (f"{tag}/2",             base / 2),
            (f"sqrt({tag}/[2]_q)",   mp.sqrt(base / two_q)),
        ]

    candidates = (
        [(lbl, v, "lambdaA_baseline") for lbl, v in family("lambda_A", lam_A)]
        + [(lbl, v, "perknot_atom") for lbl, v in family("tr_M(3He)", tr_he3)]
        + [(lbl, v, "perknot_pn_product")
           for lbl, v in family("tr_M(p)^2*tr_M(n)", tr_constituent)]
    )

    print("-" * 78)
    print(f"  {'candidate':<28s} {'family':<20s} {'value':>12s} {'rel_err':>10s} {'verdict':>18s}")
    print("-" * 78)
    results = []
    best = ("", mp.mpf("inf"), "")
    for label, val, fam in candidates:
        rel = (val - residual_ratio) / residual_ratio
        verdict = _verdict(rel)
        if abs(rel) < abs(best[1]):
            best = (label, rel, fam)
        print(f"  {label:<28s} {fam:<20s} {float(val):>12.6f} "
              f"{float(rel):>+10.2%} {verdict:>18s}")
        results.append({
            "label": label, "family": fam,
            "value_at_q0": str(val),
            "relative_error": str(rel),
            "verdict": verdict,
        })
    w.add_data("candidates", results)
    w.add_data("best_candidate", {
        "label": best[0], "relative_error": str(best[1]), "family": best[2],
    })
    print("-" * 78)
    print(f"  best: {best[0]} ({best[2]})  rel_err {float(best[1]):+.2%}")

    # Baseline-reproduction assertion (PR #1874's -18.15 % L1b verdict).
    pr1874_rel_err = (L1b_he3 - lambda_emp_he3) / lambda_emp_he3
    w.add_assertion(
        "L1b_He3_matches_PR1874_value",
        computed=float(pr1874_rel_err),
        expected=-0.1815,
        tolerance=2e-3,
        source="Re-derived L1b(3He) must reproduce PR #1874's -18.15% rel_err.",
    )
    # Baseline lambda_A/2 near-match reproduction (the PR #1882 best row).
    lamA_half_rel = (lam_A / 2 - residual_ratio) / residual_ratio
    w.add_assertion(
        "lambdaA_over_2_baseline_reproduced",
        computed=float(lamA_half_rel),
        expected=0.0365,
        tolerance=2e-3,
        source=(
            "PR #1882 baseline: lambda_A/2 ~ 1.2664 vs target 1.2218 "
            "(+3.65%, NEAR-MATCH <5%, filed as numerology)."
        ),
    )

    perknot_rels = [mp.mpf(r["relative_error"]) for r in results
                    if r["family"] != "lambdaA_baseline"]
    baseline_rels = [mp.mpf(r["relative_error"]) for r in results
                     if r["family"] == "lambdaA_baseline"]
    perknot_best = min(abs(r) for r in perknot_rels)
    baseline_best = min(abs(r) for r in baseline_rels)
    if perknot_best < mp.mpf("5e-3"):
        verdict = (
            "ARTIFACT-INDICATIVE: a per-knot form is an EXACT-MATCH "
            "(<0.5%) of the residual target — the original single-factor "
            "conclusion was density-family-bound. Numerology gate still "
            "applies (cross-isotope closure + categorical identification "
            "required before any promotion)."
        )
    elif perknot_best < baseline_best:
        verdict = (
            "MIXED (scope-limited, class (a)): the per-knot analogues "
            "beat the lambda_A-family best but reach no exact match. "
            "The original 'no clean single-factor closure' negative "
            "stands on both bases; the improvement is a like-for-like "
            "observation only."
        )
    else:
        verdict = (
            "ROBUST (scope-limited, class (a)): the density swap does not "
            "flip the original negative. The original probe's conclusion "
            "('no exact single-factor substrate match; best row lambda_A/2 "
            "at +3.65% filed as numerology') survives — the per-knot "
            "analogues do WORSE than the lambda_A-family best (per-knot "
            "best |rel| > baseline best |rel|), so the lambda_A/2 "
            "near-match is confirmed as lambda_A-family numerology rather "
            "than a shadow of the canonical density. NOTE (honest "
            "like-for-like observation): the bare p!=n constituent "
            "product tr_M(p)^2*tr_M(n) lands within 25% of the residual "
            "target with NO rescaler, while the lambda_A family needed "
            "the /2 or sqrt(./[2]_q) rescaling to get near — the p!=n "
            "structure is not nothing here, but it does not close the "
            "residual. Scope: constrains only these single-factor forms "
            "on these bases; not a structural exclusion of tr_M(K)."
        )
    w.add_data("rerun_verdict", verdict)
    print("-" * 78)
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
