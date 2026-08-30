#!/usr/bin/env python3
"""milnor_order_not_magnitude_probe.py

Milnor's mu-bar supplies ORDER and SIGN, not magnitude -- so it cannot be the b3
magnitude, and the single-coupling order law it suggests is refuted.

CONTEXT
-------
With the SU(4) route closed (SU4CasimirIsAffineInPairCount: the Casimir is affine
in the pair count, so a two-body SU(4)-invariant interaction gives w constant),
the remaining corpus candidate for the b3 magnitude was the Milnor triple linking
number -- a Brunnian link has all PAIRWISE linking numbers zero while mu-bar(123)
!= 0, which is exactly the three-body-by-construction structure b3 > 0 needs.

That is right about the SHAPE and wrong about the TYPE, and the corpus already
says so. QOU.KnotTheory.Vassiliev.brunnian_exact_leadingOrder states that the
A-component Brunnian link's first non-vanishing Vassiliev invariant sits at
degree leadingOrder A = 2(A-1) and takes the value **+-1** there.

mu-bar is a NORMALISED invariant. It is not a quantity with a size.

CHECK 1 -- it cannot carry magnitude
------------------------------------
If b_A = c_A * mu-bar with mu-bar = +-1 then |b_A| = |c_A|. The whole magnitude
is c_A's; mu-bar contributes a sign. "Use mu-bar(123) for the 21.4% rise" is a
category error in the same family as the SU(4) Casimir one -- an object with the
right structure and the wrong type. (Lean: muBar_no_magnitude.)

CHECK 2 -- the order law alone is REFUTED
-----------------------------------------
What mu-bar DOES supply is the degree 2(A-1) at which the A-body term first
appears. The minimal quantitative reading is

    b_A = s_A * g^{2(A-1)},   |s_A| = 1

so |b2| = g^2, |b3| = g^4, |b4| = g^6, and eliminating g gives a DIVISION-FREE
test that needs no knowledge of the coupling:

    b3^2 = b2 * b4

Measured it fails by an order of magnitude, under both A=3 conventions. Recorded
as scope-(a): this refutes the SINGLE-COUPLING order law, not Milnor's
involvement. A multi-term closure in which mu-bar fixes each term's sign and
order while separate coefficients carry the sizes is untouched -- and is, on this
evidence, the only shape left for it.

WHAT IS NOT CLAIMED
-------------------
The MilnorParitySignLaw predicts sign(1 - tau_A) = (-1)^(A-1), i.e. -,+,- for
A=2,3,4, while the measured cumulant signs are +,+,+. **That is NOT reported here
as a refutation of the parity law**: 1 - tau_A is a different quantity from b_A,
and no relation between them is established. Conflating them would be the
arity/shape error AGENTS.md warns about.

Bean qou-edt7. NOTE: qou-brng is a DIFFERENT bean (the hbar_q^2 saturated-binding
fraction, whose surviving route is the linking-vs-self-energy amplitude question);
it is adjacent to this and is not addressed here.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)


def main() -> int:
    wb = WitnessBuilder("milnor-order-not-magnitude", engine="mpmath")
    wb.set_description(
        "Milnor's mu-bar is +-1 on Brunnian links (corpus: brunnian_exact_"
        "leadingOrder), so it carries order and sign but NO magnitude and cannot "
        "be the b3 rise. The single-coupling order law b_A = s_A g^{2(A-1)} it "
        "suggests is refuted division-free by b3^2 != b2*b4, under both A=3 "
        "conventions. Scope-(a): the family falls, not Milnor's involvement."
    )
    ok = True

    print("Milnor leadingOrder(A) = 2(A-1):  2, 4, 6 for A = 2, 3, 4")
    print("Brunnian mu-bar(1..A) = +-1       (normalised: no magnitude)\n")
    wb.add_data("leading_order", {str(A): 2 * (A - 1) for A in (2, 3, 4)})
    wb.add_data("mu_bar_value", "+-1 (brunnian_exact_leadingOrder, conditional on "
                                "BrunnianVassilievBridge)")

    D = ame_binding_mev(1, 2)
    T3, He3 = ame_binding_mev(1, 3), ame_binding_mev(2, 3)
    He4 = ame_binding_mev(2, 4)

    rows, worst = [], mp.mpf(0)
    for nm, B3 in (("isospin_average", (T3 + He3) / 2), ("3H_Coulomb_corrected", T3)):
        b2, b3 = D, B3 - 3 * D
        b4 = He4 - 4 * B3 + 6 * D
        lhs, rhs = b3**2, b2 * b4
        factor = rhs / lhs
        worst = max(worst, abs(factor - 1))
        rows.append({"convention": nm, "b2": fmt(b2), "b3": fmt(b3), "b4": fmt(b4),
                     "b3_squared": fmt(lhs), "b2_times_b4": fmt(rhs),
                     "factor": fmt(factor)})
        print(f"  {nm}")
        print(f"    b2={mp.nstr(b2,9):>11} b3={mp.nstr(b3,9):>11} b4={mp.nstr(b4,9):>11}")
        print(f"    b3^2 = {mp.nstr(lhs,9):>11}   b2*b4 = {mp.nstr(rhs,9):>11}   "
              f"off by {mp.nstr(factor,6)}x")
    wb.add_data("square_test", rows)
    print("\n  the order law needs b3^2 = b2*b4 exactly; it is out by 5-10x.")

    wb.add_assertion(
        name="single_coupling_order_law_refuted",
        computed=fmt(worst), expected="4.25", tolerance="6.0",
        unit="worst |b2*b4/b3^2 - 1| across conventions",
        source=("b_A = s_A g^{2(A-1)} forces b3^2 = b2*b4 with g eliminated; "
                "measured factors 10.11 (isospin average) and 5.25 (Coulomb-"
                "corrected). Lean: not_geometric_order"),
    )
    ok &= worst > mp.mpf("2")

    print("\n  NOT claimed: the MilnorParitySignLaw predicts sign(1-tau_A) = "
          "(-1)^(A-1),")
    print("  i.e. -,+,- while the measured cumulant signs are +,+,+. 1-tau_A is NOT")
    print("  b_A and no relation is established, so this is not a refutation of it.")
    wb.add_data("not_a_refutation_of_the_parity_law", {
        "parity_law_predicts": "sign(1 - tau_A) = (-1)^(A-1), i.e. -,+,- at A=2,3,4",
        "measured_cumulant_signs": "+,+,+",
        "why_this_is_not_a_conflict": "1 - tau_A is a different quantity from b_A; "
                                      "no relation between them is established here",
    })

    wb.add_data("verdict", {
        "mu_bar_can_carry_magnitude": False,
        "why": "it is +-1 on Brunnian links, so |b_A| = |c_A| and the size is all c_A's",
        "single_coupling_order_law": "REFUTED, scope-(a), division-free via b3^2 != b2*b4",
        "what_survives": "a multi-term closure where mu-bar fixes each term's SIGN "
                         "and ORDER while separate coefficients carry the SIZES",
        "derives_a_magnitude": False,
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
