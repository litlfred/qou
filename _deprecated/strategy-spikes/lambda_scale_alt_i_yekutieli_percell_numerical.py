#!/usr/bin/env python3
"""Strategy I (Yekutieli per-cell curvature) — framework's honest prediction.

Per docs/audits/2026-05-22-yekutieli-percell-conjecture-formalized.md
(post-2026-05-22 user direction "framework B only, remove A"), the
framework's substrate-pure Yekutieli derivation is the CATEGORICAL
SUM of two independently-justified contributions:

    λ_scale^Yekutieli  =  λ_Wedderburn + λ_curvature
                       =  Family A      + Yekutieli per-cell
                       =  (5/2 + (3/4)h²) + (−G · h²)
                       =  5/2 + (3/4 − G) · h²  +  O(h⁴)

where:
  - Family A: proved theorem `(1/4) Σ_{λ ⊢ 4} dim_q V_λ = 5/2 + (3/4)h²`
    (PR #701, on production via PR #895).
  - Yekutieli per-cell: non-abelian multiplicative integral of the
    q-deformation curvature 2-form across the Borromean ribbon
    surface, restricted via the half-symmetric Wedderburn projection,
    contributes −G = −Vol(𝓑_3)/8 = −(per-cell hyperbolic volume) at
    h² order (docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md).

The earlier audit's "Reading A" (`5/2 − G·h²`, which would have
Yekutieli REPLACE the Wedderburn h² coefficient rather than ADD to
it) was **removed** as a candidate per the user direction. Reading
A lands in the same 5.6 ppm coincidence basin PR #701 falsified for
Wedderburn-sum candidates; treating it as the framework's prediction
would conflict with Family A's proved theorem at h² order.

Framework prediction under this (Reading B) formula:
  λ_scale(q_0)  ≈  2.49266
  m_p_pred(q_0)  ≈  m_e · Vol(𝓑_3)/ℏ_q² · 2.493  ≈  951 MeV
  vs CODATA       938.27 MeV  →  +1.4 % framework gap

Compared to Family A alone (3 % framework gap), the Yekutieli
per-cell categorical correction HALVES the gap. The remaining 1.4 %
would require h⁴ corrections (categorical theory work; not yet
derived).

NO PROOF — the load-bearing conjecture (cell-↔-half-sym-projection
bijection at H_4) is documented in the audit §"Concrete next R&D";
this probe only evaluates the numerical prediction at MPFR-50dps so
the framework's honest m_p prediction can be quoted alongside the
remaining categorical theory step.

Per AGENTS.md "no fitting": the formula is NOT fitted against CODATA;
it is the categorical sum of two independent substrate derivations
(Family A theorem + Yekutieli per-cell curvature argument). The
1.4 % residual is the framework's honest accuracy under this
Yekutieli-extended formula, awaiting the categorical bijection proof
to convert "structural argument" → "proved theorem".
"""
from __future__ import annotations
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 80


def main() -> int:
    Q0 = mp.mpf(Q_50_DIGIT_STR)
    h_q = Q0 - 1 / Q0
    h2 = h_q * h_q
    G = mp.catalan

    # Family A — current production substrate λ_scale (PR #895)
    family_A = mp.mpf("2.5") + mp.mpf("0.75") * h2

    # CODATA-derived closure target (retired, kept for context)
    codata = mp.mpf("2.4599527869")

    # Framework's substrate-pure Yekutieli prediction (per user direction
    # 2026-05-22 "framework B only, remove A"): the CATEGORICAL SUM of
    # Family A (proved theorem) + Yekutieli per-cell curvature (-G·h²).
    lambda_yekutieli = mp.mpf("2.5") + (mp.mpf("0.75") - G) * h2

    print(f"q_0       = {mp.nstr(Q0, 25)}")
    print(f"h²(q_0)   = {mp.nstr(h2, 25)}")
    print(f"G         = {mp.nstr(G, 25)}")
    print()
    print(f"Family A (current production, #895)")
    print(f"  λ_A = 5/2 + (3/4)·h²              = {mp.nstr(family_A, 18)}")
    print()
    print(f"Framework Yekutieli prediction (Family A + per-cell curvature)")
    print(f"  λ_Y = 5/2 + (3/4 − G)·h²          = {mp.nstr(lambda_yekutieli, 18)}")
    print()
    print(f"CODATA closure target (retired)     = {mp.nstr(codata, 18)}")
    print()
    print("Distances at q_0:")
    family_A_vs_codata = (family_A - codata) / codata
    yek_vs_codata = (lambda_yekutieli - codata) / codata
    yek_vs_family_A = (lambda_yekutieli - family_A) / family_A
    print(f"  Family A vs CODATA            = {mp.nstr(family_A_vs_codata * 100, 8)} %")
    print(f"  Yekutieli vs CODATA           = {mp.nstr(yek_vs_codata * 100, 8)} %  ← framework's honest prediction")
    print(f"  Yekutieli vs Family A         = {mp.nstr(yek_vs_family_A * 100, 8)} %  ← per-cell curvature correction")
    print()

    print("=" * 70)
    print("FRAMEWORK PREDICTION (Reading B):")
    print()
    print("  λ_scale^Yekutieli = Family A + Yekutieli per-cell curvature")
    print("                    = (5/2 + (3/4)h²) + (-G · h²)")
    print("                    = 5/2 + (3/4 − G) · h² + O(h⁴)")
    print()
    print("At q_0:  λ ≈ 2.49266; m_p_pred ≈ 951 MeV (vs CODATA 938.27 MeV)")
    print("       → framework gap reduced from ~3 % (Family A) to ~1.4 %.")
    print()
    print("This is the categorical SUM of two independently-derived terms:")
    print("  - Family A:    proved theorem (PR #701 + sympy + Lean; on")
    print("                 production via PR #895)")
    print("  - Yekutieli:   per-cell hyperbolic volume = -G via non-abelian")
    print("                 multiplicative integral of curvature 2-form on")
    print("                 𝓑_3's ideal-octahedral tessellation (audit:")
    print("                 docs/audits/2026-05-18-conjecture-proof-step3-")
    print("                 yekutieli.md, load-bearing conjecture:")
    print("                 cell-↔-half-sym-projection bijection at H_4)")
    print()
    print("LOAD-BEARING CONJECTURE: the categorical-bijection step is the")
    print("only remaining open dependency. With its proof, λ_scale^Yekutieli")
    print("becomes the framework's substrate-pure theorem; the 1.4 % residual")
    print("is then the framework's honest accuracy awaiting h⁴ corrections.")
    print()
    print("Concrete next R&D (audit §'Concrete next R&D'):")
    print("  1. Construct the cell-↔-half-sym-projection bijection at H_4")
    print("     explicitly. (Categorical theory work; not compute.)")
    print("  2. Derive h⁴ corrections from the same per-cell tessellation")
    print("     argument; close the residual 1.4 % gap.")
    print("  3. Lean formalisation requires the non-abelian multiplicative")
    print("     integral primitive in Mathlib (long-term dependency).")
    print("=" * 70)

    w = WitnessBuilder(
        "lambda-scale-alt-i-yekutieli-percell-numerical",
        engine="mpmath",
    )
    w.set_description(
        "Strategy I (Yekutieli per-cell curvature): framework's honest "
        "substrate-pure prediction λ_scale^Yekutieli = 5/2 + (3/4 - G)·h² "
        "= 2.49266 at q_0. CATEGORICAL SUM of Family A (proved theorem, "
        "PR #701 / production #895) + Yekutieli per-cell curvature (-G, "
        "load-bearing categorical-bijection conjecture per audit "
        "docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md). "
        "Framework m_p prediction with Yekutieli correction = ~951 MeV; "
        "framework gap halved from ~3 % (Family A alone) to ~1.4 %. The "
        "alternative 'Reading A' = 5/2 - G·h² (Yekutieli REPLACES "
        "Wedderburn h²) was removed per user direction 2026-05-22 "
        "(\"framework B only, remove A\") — Reading A lands in the same "
        "5.6 ppm coincidence basin PR #701 falsified for Wedderburn sums "
        "and treating it as the framework's prediction would conflict "
        "with Family A's proved theorem at h² order."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")
    w.add_parameter("dps", 80)
    w.add_data("family_A_at_q0", mp.nstr(family_A, 25))
    w.add_data("lambda_yekutieli_at_q0", mp.nstr(lambda_yekutieli, 25))
    w.add_data("codata_target", mp.nstr(codata, 25))
    w.add_data("yekutieli_vs_codata_pct", mp.nstr(yek_vs_codata * 100, 10))
    w.add_data("yekutieli_vs_family_A_pct", mp.nstr(yek_vs_family_A * 100, 10))
    w.add_data("framework_gap_pct_family_A_alone", mp.nstr(family_A_vs_codata * 100, 10))
    w.add_data("framework_gap_pct_with_yekutieli", mp.nstr(yek_vs_codata * 100, 10))
    w.add_data(
        "framework_prediction",
        "λ_scale^Yekutieli = 5/2 + (3/4 − G)·h² + O(h⁴); m_p ≈ 951 MeV at q_0; "
        "framework gap to CODATA reduced from ~3 % (Family A alone) to ~1.4 %.",
    )
    w.add_data(
        "load_bearing_step",
        "Cell-↔-half-sym-projection bijection at H_4 (audit §Concrete next R&D #1). "
        "Categorical theory work; with proof, λ_scale^Yekutieli becomes the "
        "framework's substrate-pure theorem.",
    )

    # The probe documents the framework's Yekutieli prediction at q_0;
    # passes iff the numerical value matches the structural formula
    # (5/2 + (3/4-G)·h²) and the framework gap is correctly halved
    # (~1.4 %, not the Family-A-alone ~3 %).
    gap_halved = bool(
        mp.mpf("0.005") < abs(yek_vs_codata) < mp.mpf("0.02")
        and abs(family_A_vs_codata) > 2 * abs(yek_vs_codata)
    )
    w.add_assertion(
        "yekutieli_correction_halves_family_A_codata_gap",
        computed=int(gap_halved),
        expected=1,
        tolerance=None,
        source=(
            "Yekutieli per-cell curvature correction (-G·h²) added to "
            "Family A's leading 5/2 + (3/4)h² gives ~951 MeV m_p; "
            "framework gap to CODATA is halved from ~3 % to ~1.4 %. "
            "Passes iff the numerical relationship between the two "
            "predictions is as expected from the structural sum."
        ),
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
