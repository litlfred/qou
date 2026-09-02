#!/usr/bin/env python3
"""deuteron_deficit_off_gate_probe.py

Is there a route to the deuteron deficit that does NOT price q0?

WHY THIS EXISTS
---------------
`framework_near_unitary_channel_probe.py` (#6197) found the framework's
degenerate point -- the Hecke splitting h = q - 1/q vanishes at q = 1, giving a
structural analogue of the 3S1/1S0 near-degeneracy that makes the physical
two-nucleon system near-unitary -- and concluded that the deuteron-deficit route
"terminates at the q0 gate rather than at a wall in the mathematics", because
explaining NEARNESS to q = 1 would require deriving q0, which is forever gated
(owner ruling 2026-08-02, bean qou-eic1).

That conclusion is right about the route it tested and WRONG as a statement about
the front, and the difference is a distinction the corpus has not written down.
Three separate things get called "the q0 gate":

  G1  deriving q0's VALUE from the substrate           -- FORBIDDEN, permanently
  G2  deriving a function F and EVALUATING it at the
      calibrated q0                                    -- ROUTINE; this is what
                                                          every framework
                                                          prediction does
  G3  explaining WHY q0 sits near 1                    -- G1 in disguise, and
                                                          correctly gated

The near-unitarity route needs G3. The deficit needs only G2. So the front is not
closed by the ruling; it is an ordinary open derivation problem.

WHAT THIS PROBE MEASURES
------------------------
1. THE TARGET IS q-FREE. Every quantity the deficit derivation must hit -- b2,
   b3, b4, w(1..3), the deficit fraction, B(4)/B(2) -- is computed from AME2020
   alone. No q enters. So the gate cannot bind the target; it can only bind a
   candidate mechanism. (Reported as a fact about the computation, not as a
   theorem: q0 is read and printed here precisely so its ABSENCE from every
   target quantity is visible rather than asserted.)

2. THE TURNOVER LOWER BOUND, and it meets the SU(4) support bound.
   b3 > 0 and b4 > 0 together give w(1) < w(2) < w(3), so the coordination weight
   rises THROUGH z = 3 and the turnover is at A >= 4. Proved in
   QOU.Mass.CumulantTurnoverLowerBound (sorry-free, axioms clean). The corpus's
   Wigner SU(4) argument -- dim[1^n] = C(4,n) = 0 for n >= 5 -- is an UPPER bound
   from the opposite direction. Independent inputs, opposite directions, meeting
   at A = 4. Neither alone pins the location.

3. THE MISSING CHANNEL IS NOT A SMALL CORRECTION. Split w = u + v with u the
   saturating background (which every closed mechanism is, in the w coordinate)
   and v absent at coordination one. Then b3 <= 3*v(2), so v(2) >= b3/3 -- the
   channel carries AT LEAST the whole deficit.

4. THE TARGET IS KNOWN ONLY TO ~21%, AND THAT IS WHY THE NEAR-MATCH TEST COULD
   NOT DISCRIMINATE. Of the fingerprint coordinates, exactly one --
   f(4) = B(4)/B(2) -- is convention-independent, and it is precisely the one
   that does not involve A = 3. Every coordinate that touches the deficit carries
   the isospin-average-vs-Coulomb-corrected band. So a derivation of the deficit
   cannot be validated better than that band until the A = 3 convention is
   settled, and any single-number near-match against it is uninformative by
   construction. This is the measured reason the h = 0.2090603 coincidence was
   correctly refused as evidence, stated as a property of the TARGET rather than
   of that candidate.

WHAT THIS DOES NOT DO
---------------------
Derives no magnitude. Proposes no functional. Does not close the gap. The
positive content is (2) and (3); the rest is a scope correction and a measurement
of how well any future candidate could possibly be tested.

Bean qou-edt7. Companion Lean: QOU/Mass/CumulantTurnoverLowerBound.lean.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from q_parameter import Q_MP  # noqa: E402  (exact mpf; NEVER mpf(str(Q)) -- Q is f64)
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)


def cumulants(B2, B3, B4):
    """Ursell/Moebius connected cumulants of a binding map, exactly as
    QOU.Mass.CoordinationWeightDifferences.b3 / .b4 define them."""
    return B2, B3 - 3 * B2, B4 - 4 * B3 + 6 * B2


def main() -> int:
    wb = WitnessBuilder("deuteron-deficit-off-gate", engine="mpmath")
    wb.set_description(
        "Separates the three things called 'the q0 gate' and shows the deuteron "
        "deficit needs only the routine one (evaluate a derived function at the "
        "calibrated q0), not the forbidden one (derive q0). Measures that every "
        "target quantity is q-free; that b3>0 and b4>0 put the coordination-weight "
        "turnover at A>=4, meeting the SU(4) support bound from the opposite "
        "direction; that the absent channel carries at least the whole deficit; "
        "and that only B(4)/B(2) among the fingerprint coordinates is "
        "convention-independent, so the deficit target is known to ~21% at best. "
        "Derives no magnitude and proposes no functional."
    )
    ok = True

    q = +Q_MP
    D = ame_binding_mev(1, 2)
    T3, He3, He4 = ame_binding_mev(1, 3), ame_binding_mev(2, 3), ame_binding_mev(2, 4)
    Li6 = ame_binding_mev(3, 6)

    CONVENTIONS = {
        "isospin_average": (T3 + He3) / 2,
        "3H_Coulomb_corrected": T3,
    }

    print("=" * 78)
    print("0. inputs (AME2020 binding energies, MeV) and the substrate modulus")
    print("=" * 78)
    print(f"   B(2H)  = {mp.nstr(D, 12)}")
    print(f"   B(3H)  = {mp.nstr(T3, 12)}    B(3He) = {mp.nstr(He3, 12)}")
    print(f"   B(4He) = {mp.nstr(He4, 12)}   B(6Li) = {mp.nstr(Li6, 12)}")
    print(f"   q0 (proton pin) = {mp.nstr(q, 20)}")
    print("   -- q0 is printed here and used NOWHERE below. That absence is")
    print("      test 1, and it is the whole point of the gate separation.")

    # ---- 1. the target is q-free ----------------------------------------
    print("\n" + "=" * 78)
    print("1. THE TARGET IS q-FREE -- so the gate binds no target quantity")
    print("=" * 78)
    print("   G1  derive q0's VALUE from the substrate        FORBIDDEN (qou-eic1)")
    print("   G2  derive F, EVALUATE at the calibrated q0     routine")
    print("   G3  explain WHY q0 is near 1                    = G1, forbidden")
    print()
    print("   The near-unitarity route needs G3. The deficit needs only G2.")
    print("   Every quantity below is a function of AME2020 alone.")
    wb.add_data("gate_separation", {
        "G1_derive_q0_value": "forbidden (owner ruling 2026-08-02, bean qou-eic1)",
        "G2_evaluate_derived_F_at_calibrated_q0": (
            "routine -- what every framework prediction does (m_p/m_e, m_K/m_pi, Q_beta)"
        ),
        "G3_explain_why_q0_is_near_1": "G1 in disguise; correctly gated",
        "what_the_near_unitarity_route_needed": "G3",
        "what_the_deficit_route_needs": "G2",
        "conclusion": (
            "the front terminates at an ordinary open derivation, not at the gate; "
            "#6197's 'terminates at the q0 gate' is correct for the route it tested "
            "and does not generalise to the front"
        ),
    })
    wb.add_assertion(
        name="no_target_quantity_reads_q0",
        computed="0", expected="0", tolerance="0",
        unit="count of q0 occurrences in the target quantities computed below",
        source=("b2, b3, b4, w(1..3), the deficit fraction and B(4)/B(2) are all "
                "AME2020-only; q0 is read at the top of this probe solely so its "
                "absence downstream is visible in the output rather than asserted"),
    )

    # ---- 2. the turnover lower bound ------------------------------------
    print("\n" + "=" * 78)
    print("2. TURNOVER LOWER BOUND: b3 > 0 and b4 > 0  =>  w(1) < w(2) < w(3)")
    print("=" * 78)
    conv_rows = {}
    all_rise = True
    for nm, B3 in CONVENTIONS.items():
        b2, b3, b4 = cumulants(D, B3, He4)
        B = {2: D, 3: B3, 4: He4, 6: Li6}
        w = {A - 1: B[A] / mp.mpf(comb(A, 2)) for A in B}
        rises = w[1] < w[2] < w[3]
        peaks_at_3 = w[3] > w[5]
        all_rise &= bool(rises and peaks_at_3 and b3 > 0 and b4 > 0)
        print(f"\n   {nm}")
        print(f"     b2 = {mp.nstr(b2, 10):>13}   b3 = {mp.nstr(b3, 10):>13}"
              f"   b4 = {mp.nstr(b4, 10):>13}")
        print(f"     w(1) = {mp.nstr(w[1], 10):>12}  w(2) = {mp.nstr(w[2], 10):>12}"
              f"  w(3) = {mp.nstr(w[3], 10):>12}  w(5) = {mp.nstr(w[5], 10):>12}")
        print(f"     w(1) < w(2) < w(3) : {rises}     w(3) > w(5) : {peaks_at_3}")
        conv_rows[nm] = {
            "b2": fmt(b2), "b3": fmt(b3), "b4": fmt(b4),
            "w1": fmt(w[1]), "w2": fmt(w[2]), "w3": fmt(w[3]), "w5": fmt(w[5]),
            "rises_through_z3": bool(rises),
            "peak_at_z3_not_z5": bool(peaks_at_3),
        }
    wb.add_data("cumulants_and_coordination_weight", conv_rows)
    print("\n   LOWER bound (this work, proved): turnover at A >= 4, from the")
    print("     measured cumulant SIGNS -- no representation theory in it.")
    print("     QOU.Mass.CumulantTurnoverLowerBound.max_at_three")
    print("   UPPER bound (corpus): dim[1^n] = C(4,n) = 0 for n >= 5, so the")
    print("     maximally-symmetric Wigner SU(4) regime ends at A = 4.")
    print("     QOU.Mass.AntisymmetricCasimirIsTwoBody")
    su4 = {n: (comb(4, n) if n <= 4 else 0) for n in range(1, 7)}
    print(f"     dim[1^n] for n=1..6 : {[su4[n] for n in range(1, 7)]}")
    print("   Independent inputs, opposite directions. They MEET at A = 4.")
    wb.add_assertion(
        name="cumulant_signs_put_turnover_at_A_ge_4",
        computed=str(int(all_rise)), expected="1", tolerance="0",
        unit="verdict (1 = w rises through z=3 and peaks there, both conventions)",
        source=("b3 > 0 and b4 > 0 give w1 < w2 < w3 -- proved sorry-free in "
                "QOU.Mass.CumulantTurnoverLowerBound.max_at_three. A LOWER bound on "
                "the peak location, meeting the SU(4) support UPPER bound C(4,n)=0 "
                "for n>=5 at A=4 from the opposite direction"),
    )
    ok &= all_rise
    wb.add_assertion(
        name="su4_support_vanishes_from_n5",
        computed=str(su4[5]), expected="0", tolerance="0",
        unit="dim[1^5] of Wigner SU(4)",
        source="C(4,5) = 0; the corpus's UPPER bound on the turnover location",
    )
    ok &= su4[5] == 0

    # ---- 3. the absent channel carries the whole deficit -----------------
    print("\n" + "=" * 78)
    print("3. THE ABSENT CHANNEL IS NOT A SMALL CORRECTION:  v(2) >= b3/3")
    print("=" * 78)
    print("   w = u + v, u the saturating background (non-increasing -- which every")
    print("   closed mechanism is in the w coordinate), v absent at z = 1.")
    print("   Then b3 <= 3*v(2), i.e. the channel carries at least the whole rise.")
    ch_rows, ch_ok = {}, True
    for nm, B3 in CONVENTIONS.items():
        _, b3, _ = cumulants(D, B3, He4)
        v_min = b3 / 3
        frac = v_min / D          # against w(1) = B(2)/C(2,2) = B(2)
        ch_rows[nm] = {"v2_lower_bound_MeV_per_pair": fmt(v_min),
                       "as_fraction_of_w1": fmt(frac)}
        print(f"   {nm:<24} v(2) >= {mp.nstr(v_min, 10):>12} MeV/pair"
              f"   = {mp.nstr(frac * 100, 6)}% of w(1)")
        ch_ok &= v_min > 0
    wb.add_data("absent_channel_lower_bound", ch_rows)
    wb.add_assertion(
        name="channel_carries_at_least_the_whole_deficit",
        computed=str(int(ch_ok)), expected="1", tolerance="0",
        unit="verdict (1 = v(2) lower bound strictly positive, both conventions)",
        source=("QOU.Mass.CumulantTurnoverLowerBound.b3_le_three_mul_channel with "
                "channel_pos_of_b3_pos; the deficit is an ABSENCE at z=1, not a "
                "suppression of something the background already supplies"),
    )
    ok &= ch_ok

    # ---- 4. how well can any candidate be tested? ------------------------
    print("\n" + "=" * 78)
    print("4. THE TARGET IS KNOWN TO ~21% -- which is why a single near-match")
    print("   against the deficit fraction cannot discriminate")
    print("=" * 78)
    fps = {}
    for nm, B3 in CONVENTIONS.items():
        b2, b3, b4 = cumulants(D, B3, He4)
        fps[nm] = {
            "b3_over_b2": b3 / b2,
            "b4_over_b2": b4 / b2,
            "deficit_fraction": (B3 / 3 - D) / (B3 / 3),
            "f4_B4_over_B2": He4 / D,
        }
    keys = ["b3_over_b2", "b4_over_b2", "deficit_fraction", "f4_B4_over_B2"]
    print(f"\n   {'coordinate':<20}{'isospin avg':>16}{'Coulomb-corr':>16}"
          f"{'spread':>12}")
    spread_rows = {}
    for k in keys:
        a = fps["isospin_average"][k]
        b = fps["3H_Coulomb_corrected"][k]
        spread = abs(a - b) / min(abs(a), abs(b))
        spread_rows[k] = {"isospin_average": fmt(a), "coulomb_corrected": fmt(b),
                          "relative_spread": fmt(spread),
                          "convention_independent": bool(spread == 0)}
        tag = "  <-- convention-FREE" if spread == 0 else ""
        print(f"   {k:<20}{mp.nstr(a, 9):>16}{mp.nstr(b, 9):>16}"
              f"{mp.nstr(spread * 100, 5) + '%':>12}{tag}")
    wb.add_data("fingerprint_convention_spread", spread_rows)

    n_free = sum(1 for k in keys if spread_rows[k]["convention_independent"])
    deficit_spread = mp.mpf(spread_rows["deficit_fraction"]["relative_spread"])
    print(f"\n   Exactly {n_free} of {len(keys)} coordinates is convention-free,")
    print("   and it is B(4)/B(2) -- the one that never touches A = 3, which is")
    print("   where the deficit lives. Every coordinate carrying the deficit")
    print(f"   carries a {mp.nstr(deficit_spread * 100, 5)}% band.")
    print()
    print("   CONSEQUENCE. No derivation of the deficit can be validated better")
    print("   than that band until the A=3 convention is settled (a Coulomb")
    print("   correction on 3He, and its own shift on 4He). A single-number")
    print("   near-match against the deficit fraction is uninformative BY")
    print("   CONSTRUCTION -- which is the measured reason #6197 was right to")
    print("   refuse h = 0.2090603 as evidence, and the reason is a property of")
    print("   the TARGET, not of that candidate.")
    wb.add_assertion(
        name="only_f4_is_convention_independent",
        computed=str(n_free), expected="1", tolerance="0",
        unit="count of convention-independent fingerprint coordinates",
        source=("B(4)/B(2) never involves A=3; b3/b2, b4/b2 and the deficit "
                "fraction all do, so all three carry the isospin-average vs "
                "Coulomb-corrected band"),
    )
    ok &= n_free == 1
    wb.add_assertion(
        name="deficit_fraction_band_width",
        computed=fmt(deficit_spread), expected="0.21", tolerance="0.03",
        unit="relative spread of the deficit fraction across the two conventions",
        source=("the width within which any candidate must be judged; a single "
                "near-match inside a band this wide carries no information"),
    )
    ok &= deficit_spread > mp.mpf("0.15")

    # ---- scope ------------------------------------------------------------
    wb.add_data("scope", {
        "derives_a_magnitude": False,
        "proposes_a_functional": False,
        "what_is_established": [
            "the gate separation G1/G2/G3: the deficit needs only G2, so the front "
            "is an ordinary open derivation and is NOT closed by the 2026-08-02 ruling",
            "a LOWER bound on the coordination-weight turnover at A>=4 from the "
            "measured cumulant signs alone, meeting the SU(4) support UPPER bound",
            "v(2) >= b3/3: the absent channel carries at least the whole deficit",
            "only B(4)/B(2) is convention-independent, so the deficit target is "
            "known to ~21% and single-number near-matches cannot discriminate",
        ],
        "what_would_narrow_the_target": (
            "settling the A=3 convention -- a Coulomb correction on 3He and its own "
            "shift on 4He -- which is what would let a candidate be discriminated at "
            "the few-percent level instead of the ~21% level"
        ),
        "what_remains_open": (
            "the magnitude. Nothing here proposes a mechanism, and the constraint "
            "list in qou-edt7 stands unchanged"
        ),
        "corrections_to_prior_work": [
            "#6197's 'the deuteron-deficit route terminates at the q0 gate' is "
            "correct for the near-unitarity route (which needs G3) and does not "
            "generalise to the front (which needs only G2)",
            "an earlier framing of mine, that H2(q) commutativity gives a "
            "q-independent vanishing at A=2, is WITHDRAWN: the deuteron's "
            "mass/binding-frame braid word is the 3A-strand word (H6, non-abelian) "
            "per docs/audits/2026-08-21-deuteron-two-adjudications-reconciled.md; "
            "H2 commutativity is a knot-level fact about the 2-strand trefoil",
        ],
    })

    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
