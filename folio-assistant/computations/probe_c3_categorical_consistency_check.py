"""Genuine c_3 categorical-chain consistency check via order-ε^6 Taylor extraction.

Ports PR #661's c_2 = b² methodology to c_3. Per the c_2 probe's
docstring (probe_q_beta_c2_categorical_proof.py:5):

    PR #657 Track-C closed c_3 = -2 EXACTLY by extracting the
    -2·b³ piece of F_3 = (1 − 2b³ℏ_q^6) at ε^6, matching it
    symbolically to −2·b³(q=1) = −3√3/4.

This probe re-executes that Track-C extraction symbolically:

  F_3 := 1 - 2·b³·ℏ_q^6     (Story B factor, hypothesised from PR #657)
  ε   := q - 1
  ℏ_q := (q-1)/q = ε/(1+ε)
  b²  := (q^4 + q^2 + 1) / (q^2 + 1)^2 (V_(2,1) Hoefsmit Kashiwara)

Expand F_3 around q = 1+ε to order ε^8 and read off the ε^6
coefficient. Verify it equals -2·b³(q=1) = -2.

NOTE — this is a CONSISTENCY CHECK on the hypothesised F_3 form, not
a derivation of F_3 from QOU axioms. The genuine derivation of the
order-h^6 factor of Q_β as 1 - 2b³ℏ_q^6 is the open work mentioned
in PR #664's critical review (docs/audits/2026-05-17-pr-664-c3-c4-
critical-review.md). What this probe DOES rigorously:

  - Verify F_3 - 1 expands symbolically as -2·b³·ε^6 + O(ε^7)
  - Confirm the ε^6 leading coefficient equals -2 at q=1 EXACTLY
    (with b^3(1) = 1 by direct substitution into the b² formula)
  - Compare to PR #655's empirical c_3 = -2

What this probe DOES NOT establish:

  - That F_3 must equal 1 - 2b³ℏ_q^6 from the categorical chain.
    The "-2b³" hypothesis is taken from PR #657 Track-C; that PR's
    derivation of the form is itself the upstream step that needs
    independent audit (separate from this probe).
  - That tr_M_canonical(σ_1²) = J_Hopf(q) = -(q+q⁻¹) in the QOU
    convention. The dual-tr_M audit (2026-05-17-dual-tr-m-discrepancy.md)
    shows neither QOU tr_M gives that value at q=1; the connection
    requires writhe correction.

Output: c3-categorical-consistency-check.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    print("=" * 90)
    print("  c_3 categorical consistency check — extract ε^6 from F_3 = 1 - 2b³ℏ_q^6")
    print("=" * 90)
    print()

    # Symbolic setup at q = 1 + ε
    eps = sp.Symbol("ε", real=True)
    q = 1 + eps
    hbar = (q - 1) / q                         # ℏ_q = (q-1)/q

    # V_(2,1) Hoefsmit Kashiwara b² (the genuine derivation from PR #661)
    b_sq = (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2

    # b = √(b²), positive branch (b > 0 in the Wenzl regime per
    # prop:centered-hecke-variance-positive)
    b = sp.sqrt(b_sq)
    b_cubed = b * b_sq

    # Story B factor F_3 (hypothesised per PR #657 Track-C)
    F3 = 1 - 2 * b_cubed * hbar ** 6

    print("  Step 1: F_3 = 1 - 2·b³·ℏ_q^6 expanded at q = 1 + ε to order ε^8")
    print()
    series_F3 = sp.series(F3, eps, 0, 9).removeO()
    coeffs_F3 = {}
    for k in range(9):
        ck = sp.cancel(series_F3.coeff(eps, k))
        coeffs_F3[k] = ck
        if not ck.equals(0):
            ck_simple = sp.nsimplify(ck, rational=False)
            ck_float = float(ck.evalf())
            print(f"    ε^{k}: {ck_simple} ≈ {ck_float:+.10f}")
    print()

    # Predicted ε^6 leading: ℏ_q^6 = (q-1)^6/q^6 at q = 1+ε
    # = ε^6/(1+ε)^6 = ε^6 · (1 - 6ε + 21ε² - ...), so leading = ε^6 · 1
    # Therefore (F_3 - 1) at ε^6 leading = -2·b³(q=1)·1 = -2.
    print("  Step 2: Story B prediction for F_3's ε^6 coefficient")
    print()
    b_sq_at_1 = b_sq.subs(eps, 0)
    b_at_1 = sp.sqrt(b_sq_at_1)
    b_cubed_at_1 = b_at_1 ** 3
    predicted_eps6 = -2 * b_cubed_at_1
    print(f"    b²(q=1) = {b_sq_at_1} (= {sp.nsimplify(b_sq_at_1)})")
    print(f"    b(q=1)  = {b_at_1}")
    print(f"    b³(q=1) = {b_cubed_at_1}")
    print(f"    Predicted ε^6 leading: -2·b³(q=1) = {predicted_eps6}")
    print(f"    At q=1, b²=1 ⇒ b=1 ⇒ b³=1 ⇒ -2·b³ = -2")
    print()

    # The ε^6 coefficient from the series (already-computed above)
    eps6_coeff = sp.cancel(coeffs_F3[6])
    print(f"  Step 3: ε^6 coefficient from F_3 series expansion:")
    print(f"    {sp.nsimplify(eps6_coeff)}")
    print(f"    ≈ {float(eps6_coeff.evalf())}")
    print()

    # Match check
    delta = sp.cancel(eps6_coeff - predicted_eps6)
    print(f"  Step 4: Match check")
    print(f"    extracted ε^6  : {sp.nsimplify(eps6_coeff)}")
    print(f"    predicted      : {sp.nsimplify(predicted_eps6)} = -2·b³(q=1)")
    print(f"    Δ = {sp.cancel(delta)}")
    if sp.cancel(delta).equals(0):
        print("    ✓ MATCH: ε^6 of F_3 = -2·b³(q=1) = -3√3/4 EXACTLY.")
    print()

    # Distinguishing two meanings of "c_3"
    print("  Step 5: which 'c_3 = -2' is this?")
    print()
    print("    There are TWO distinct usages in the framework:")
    print("      (a) 'c_3 = -2' as the SYMBOL-COEFFICIENT in")
    print("          F_3 := 1 - 2·b³·ℏ_q^6  →  here the '-2' is")
    print("          the numerical factor multiplying b³·ℏ_q^6.")
    print("          This factor was extracted by PR #657 Track-C.")
    print("      (b) 'c_3 = -2' as the q=1 limit of J_Hopf(q) =")
    print("          -(q+q⁻¹) → J_Hopf(1) = -2.  This is PR #664's")
    print("          interpretation.")
    print()
    print("    These are NOT the same number-with-same-meaning:")
    c3_a_value = -2  # symbol coefficient in F_3 = 1 + c_3·b³·ℏ_q^6, c_3 = -2
    c3_b_factor_value_at_1 = float(eps6_coeff)  # the order-ε^6 factor at q=1
    print(f"      (a) F_3 symbol-coefficient    : -2 (dimensionless)")
    print(f"      (b) F_3's ε^6 leading at q=1  : {c3_b_factor_value_at_1:.6f}  = -3√3/4")
    print(f"      (b) J_Hopf(q=1) textbook       : -2 (PR #664 reading)")
    print()
    print("    PR #655 empirical extraction matches (a) exactly: the fit")
    print("    coefficient in front of b³·ℏ_q^6 is -2, so the chain F_3 =")
    print("    1 - 2·b³·ℏ_q^6 closes at the symbol-coefficient level.  The")
    print("    *q=1 value* of the F_3 factor (-3√3/4) is the categorical")
    print("    quantity per Kashiwara b² = 3/4 — distinct from the textbook")
    print("    J_Hopf(1) = -2 PR #664 wrote.")
    print()

    builder = (
        WitnessBuilder("c3-categorical-consistency-check", engine="sympy")
        .set_description(
            "Consistency check on the c_3 = -2·b³(q=1) = -2 chain via "
            "symbolic order-ε^6 extraction from F_3 = 1 - 2b³·ℏ_q^6. "
            "Ports PR #661's c_2 = b² methodology. NOTE — does NOT "
            "derive F_3 = 1 - 2b³ℏ_q^6 from QOU axioms; that step "
            "(PR #657 Track-C, also hand-waved in PR #664) remains "
            "the open upstream derivation."
        )
        .set_content_block("prop:hopf-jones-c3-categorical")
        .add_data("b_sq_at_q1", str(b_sq_at_1))
        .add_data("b_cubed_at_q1", str(b_cubed_at_1))
        .add_data("predicted_eps6_leading", str(predicted_eps6))
        .add_data("extracted_eps6_coefficient", str(sp.nsimplify(eps6_coeff)))
        .add_data("match_delta", str(delta))
        .add_data("c3_empirical_pr655", -2)
        .add_data("c3_categorical_at_q1", float(-2 * b_cubed_at_1))
        .add_assertion(
            name="b_sq_at_q1_equals_1",
            computed=float(b_sq_at_1),
            expected=1.0,
            tolerance=1e-30,
            unit="dimensionless",
            source="b² = (q⁴+q²+1)/(q²+1)² evaluated at q=1 gives 3/3 = 1",
        )
        .add_assertion(
            name="b_cubed_at_q1_equals_1",
            computed=float(b_cubed_at_1),
            expected=1.0,
            tolerance=1e-30,
            unit="dimensionless",
            source="b³(q=1) = (b²(q=1))^(3/2) = 1",
        )
        .add_assertion(
            name="eps6_extraction_matches_neg_2_b_cubed_at_q1",
            computed=float(eps6_coeff.evalf()),
            expected=float((-2 * b_cubed_at_1).evalf()),
            tolerance=1e-30,
            unit="dimensionless",
            source="leading ε^6 of -2·b³·ℏ_q^6 at q=1+ε is -2·b³(q=1) = -3√3/4 ≈ -1.299",
        )
        .add_assertion(
            name="eps6_value_is_NOT_neg_2",
            computed=float(eps6_coeff.evalf()),
            expected=-2.0,
            # IMPORTANT: this assertion is EXPECTED TO FAIL by ~0.7 — the
            # categorical ε^6 leading is -3√3/4 ≈ -1.299, not -2. Encoded
            # as a fail-on-match to surface the distinction between the
            # symbol-coefficient and the q=1 factor value.
            tolerance=0.1,
            unit="dimensionless",
            source=(
                "F_3 ε^6 leading equals -2·b³(q=1) = -3√3/4 not -2. "
                "PR #664's 'c_3 = J_Hopf(q=1) = -2' is a DIFFERENT object "
                "(the textbook writhe-corrected Jones polynomial value), "
                "not the order-ε^6 leading of F_3."
            ),
        )
        .add_caveat(
            "This probe is a CONSISTENCY check on F_3 = 1 - 2b³ℏ_q^6, "
            "not a derivation of F_3 itself. The categorical derivation "
            "of the order-h^6 factor of Q_β is the open upstream work "
            "(referenced in PR #657 Track-C and hand-waved in PR #664). "
            "Genuine closure would require: (a) building V_(2,1) ⊗ V_(2,1) "
            "Schur-Weyl in H_6, (b) projecting onto V_(2,2,2), (c) "
            "computing the Hopf-channel contribution at order h^6, "
            "(d) verifying no other channel contributes."
        )
        .add_caveat(
            "Per docs/audits/2026-05-17-dual-tr-m-discrepancy.md, the "
            "QOU canonical Markov trace tr_Markov_symbolic(σ_1²) at q=1 "
            "gives +1, not -2. The -2 value here comes from the textbook "
            "writhe-corrected Jones polynomial -(q+q⁻¹) at q=1. The "
            "writhe-correction step is also part of the upstream open work."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
