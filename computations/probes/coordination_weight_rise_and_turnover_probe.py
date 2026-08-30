#!/usr/bin/env python3
"""coordination_weight_rise_and_turnover_probe.py

Why the coordination weight rises at z=1 and turns over at the alpha.

CONTEXT
-------
`QOU.Mass.CoordinationWeightDifferences` reduces the whole body-order cumulant
tower to one function, w(z) = B(A)/C(A,2) at coordination z = A-1, via
b_n = C(n,2) * Delta^{n-2} w(1). The measured b3 > 0 is exactly "w rises at z=1",
and saturation of B/A is exactly "z*w(z) is bounded", so w must be non-monotone.

`QOU.Mass.UniformBondSimpleGraphExclusion` then closes the NEGATIVE half: no
uniform-bond simple-graph assembly can produce the rise, for any graph family,
because a simple graph on 3 vertices has at most 3 edges. So the rise is not
about WHICH pairs bind; it requires the bond WEIGHT to differ between the pair
and the triple.

This probe measures what that non-transferability has to look like, and tests the
candidate mechanisms. It DERIVES NO MAGNITUDE. Every candidate here is either
refuted or explicitly labelled as locating a feature without predicting its size.

TESTS
-----
1. The rise, measured. eps(z) := w(z) is the bond weight at coordination z.
2. SINGLE-RATIO SCALING, REFUTED. The QOU-native mechanism for
   non-transferability is the Markov property: tr_{n+1}(beta sigma_n^{+-1}) =
   z^{+-1} tr_n(beta), so embedding a 2-strand bond in an n-strand braid
   multiplies by a power of the Markov parameter. The simplest quantitative form
   of that is eps(z) = eps(1) * r^(z-1) for SOME constant r. Measured, the two
   available ratios disagree by ~44%, so NO r fits -- the whole single-ratio
   family is refuted, independent of what r is or of the convention that fixes
   it. (Reported for both convention D and convention C so the refutation is
   visibly convention-independent.)
3. TURNOVER LOCATION, forced by the SU(4) supermultiplet. The fully
   antisymmetric spin-isospin representation [1^n] of Wigner SU(4) has
   dim = C(4,n), which VANISHES for n >= 5. So the regime in which every nucleon
   shares one maximally symmetric spatial state ends exactly at A = 4. This
   locates the peak with no free parameter. It does NOT give its height, and the
   step from "maximal spatial symmetry" to "maximal binding" is Wigner's physical
   assumption, not something derived in this corpus. Both caveats are asserted
   below, not just written here.

   NOTE ON A PRIOR OVER-CLAIM, so it is not repeated: an earlier probe of mine
   argued from C(4,n) > 0 to a statement about the SIGN of a body-order term.
   That was wrong -- positivity is analytic, true of any positive-weight object,
   and discriminates nothing. The claim HERE is different and is a finite support
   bound: C(4,n) = 0 for n >= 5. Vanishing is not positivity.
4. SAME-ORBITAL FRACTION, REFUTED as a general law. If only pairs sharing the
   s-shell carried the full weight, w would fall like the same-orbital pair
   fraction. That holds to <8% for A = 5,6,7 with a single normalisation and then
   fails by >20% at A = 9 and >70% at A = 12. Three points at 8% followed by a
   23% miss at the next point is a coincidence, not a law, and is recorded as a
   scope-(a) negative.

Bean qou-edt7. Companion Lean: QOU/Mass/UniformBondSimpleGraphExclusion.lean.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from q_parameter import Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)

# s-shell capacity: 2 protons x 2 spin states = 4 nucleons, the Wigner SU(4)
# fully-antisymmetric supermultiplet [1^n], dim = C(4,n), zero for n >= 5.
S_SHELL = 4


def main() -> int:
    wb = WitnessBuilder("coordination-weight-rise-and-turnover", engine="mpmath")
    wb.set_description(
        "Measures the non-transferability the b3 > 0 rise requires, and tests "
        "candidate mechanisms for the rise and the alpha turnover. Refutes the "
        "single-ratio (Markov-power) scaling family and the same-orbital-fraction "
        "law; locates the turnover at A=4 from the SU(4) [1^n] support bound "
        "C(4,n) = 0 for n >= 5, without predicting its height. Derives no magnitude."
    )
    ok = True

    q = mp.mpf(str(Q))
    B = {2: ame_binding_mev(1, 2),
         3: (ame_binding_mev(1, 3) + ame_binding_mev(2, 3)) / 2,
         4: ame_binding_mev(2, 4), 5: ame_binding_mev(3, 5),
         6: ame_binding_mev(3, 6), 7: ame_binding_mev(3, 7),
         9: ame_binding_mev(4, 9), 12: ame_binding_mev(6, 12),
         16: ame_binding_mev(8, 16)}
    w = {A - 1: B[A] / mp.mpf(comb(A, 2)) for A in B}

    # ---- 1. the rise -----------------------------------------------------
    print("1. the bond weight eps(z) = w(z), MeV per nucleon pair")
    for z in sorted(w):
        print(f"   z={z:<3} (A={z+1:<3}) eps = {mp.nstr(w[z], 10)}")
    rise = w[2] / w[1]
    print(f"\n   eps(2)/eps(1) = {mp.nstr(rise, 10)}   -> the bond is "
          f"{mp.nstr((rise - 1) * 100, 6)}% STRONGER at coordination 2")
    wb.add_assertion(
        name="bond_strengthens_from_z1_to_z2",
        computed=fmt(rise), expected="1.213707607", tolerance="1e-8",
        unit="dimensionless ratio",
        source="w(2)/w(1); the entire content of b3 > 0, per lt_of_b3_pos",
    )
    ok &= rise > 1

    # ---- 2. single-ratio scaling: REFUTED --------------------------------
    r12 = w[2] / w[1]
    r23 = w[3] / w[2]
    disagree = abs(r23 - r12) / r12
    print("\n2. single-ratio scaling eps(z) = eps(1) * r^(z-1)  -- REFUTED")
    print(f"   r from z=1->2 : {mp.nstr(r12, 10)}")
    print(f"   r from z=2->3 : {mp.nstr(r23, 10)}")
    print(f"   disagreement  : {mp.nstr(disagree * 100, 6)}%  -> NO constant r fits")
    # the two Markov parameters, so the refutation is visibly convention-free
    z_D = q**3 / (q**2 + 1)
    z_C = mp.sqrt(q) / (q + 1)
    print(f"   (for reference: Markov z_D = {mp.nstr(z_D, 10)}, "
          f"z_C = {mp.nstr(z_C, 10)}; 1/z_D = {mp.nstr(1/z_D, 10)})")
    print("   The refutation does not depend on which of these r is -- a single")
    print("   ratio of ANY value cannot produce two ratios 44% apart.")
    wb.add_assertion(
        name="single_ratio_scaling_refuted",
        computed=fmt(disagree), expected="0.4390", tolerance="0.01",
        unit="relative disagreement between the two measured ratios",
        source=("eps(z)=eps(1)*r^(z-1) requires w(2)/w(1) = w(3)/w(2); they differ "
                "by ~44%, refuting the family for every r, convention-independently"),
    )
    ok &= disagree > mp.mpf("0.2")

    # ---- 3. turnover location from the SU(4) support bound ---------------
    print("\n3. turnover location: SU(4) [1^n] supermultiplet, dim = C(4,n)")
    dims = {n: comb(4, n) if n <= 4 else 0 for n in range(1, 8)}
    for n in range(1, 8):
        print(f"   n={n}  dim [1^n] = {dims[n]}")
    peak_z = max(w, key=lambda z: w[z])
    last_n = max(n for n in dims if dims[n] > 0)
    print(f"\n   last n with a fully antisymmetric state : A = {last_n}")
    print(f"   measured peak of eps(z)                 : A = {peak_z + 1}")
    print("   -> the peak LOCATION is forced, with no free parameter.")
    print("      It does NOT give the peak HEIGHT, and 'maximal spatial symmetry")
    print("      => maximal binding' is Wigner's physical assumption, not derived here.")
    wb.add_assertion(
        name="su4_support_bound_locates_the_turnover",
        computed=str(peak_z + 1), expected=str(last_n), tolerance="0",
        unit="mass number A",
        source=("dim[1^n] = C(4,n) vanishes for n >= 5, so the fully antisymmetric "
                "spin-isospin regime ends at A=4; the measured eps peak is at A=4. "
                "A SUPPORT bound (C(4,n)=0), NOT a positivity claim -- an earlier "
                "probe's C(4,n)>0 sign argument was wrong and is not reused."),
    )
    ok &= (peak_z + 1) == last_n
    wb.add_data("su4_locates_but_does_not_size", {
        "locates_peak_position": True,
        "predicts_peak_height": False,
        "wigner_assumption_derived_in_corpus": False,
    })

    # ---- 4. same-orbital-fraction law: REFUTED ---------------------------
    print("\n4. same-orbital pair fraction (s-shell holds 4)  -- REFUTED beyond A=7")

    def same_orbital_pairs(A):
        s = min(A, S_SHELL)
        p = A - s
        return comb(s, 2) + comb(p, 2)

    rows, worst_low, worst_high = [], mp.mpf(0), mp.mpf(0)
    for A in (5, 6, 7, 9, 12, 16):
        frac = mp.mpf(same_orbital_pairs(A)) / mp.mpf(comb(A, 2))
        pred = w[3] * frac                     # normalised at the alpha, 1 parameter
        err = abs(pred - w[A - 1]) / w[A - 1]
        rows.append({"A": A, "fraction": fmt(frac), "predicted": fmt(pred),
                     "measured": fmt(w[A - 1]), "rel_err": fmt(err)})
        print(f"   A={A:<3} frac={mp.nstr(frac, 6):>9}  pred={mp.nstr(pred, 8):>11}"
              f"  meas={mp.nstr(w[A-1], 8):>11}  err={mp.nstr(err*100, 5):>8}%")
        if A <= 7:
            worst_low = max(worst_low, err)
        else:
            worst_high = max(worst_high, err)
    wb.add_data("same_orbital_fraction_table", rows)
    print(f"\n   worst error A<=7 : {mp.nstr(worst_low*100, 5)}%")
    print(f"   worst error A>=9 : {mp.nstr(worst_high*100, 5)}%")
    print("   -> three points at <8% then a >20% miss at the next point is a")
    print("      coincidence, not a law. Scope-(a): THIS model, ALONE, fails.")
    # Encode the VERDICT, not the error magnitude: an assertion whose job is to
    # record a refutation must PASS when the refutation holds, or the witness
    # reads "FAILURES" for a result that came out exactly as stated.
    verdict = 1 if (worst_high > mp.mpf("0.2") and worst_low < mp.mpf("0.10")) else 0
    wb.add_data("same_orbital_fraction_errors", {
        "worst_rel_err_A_le_7": fmt(worst_low),
        "worst_rel_err_A_ge_9": fmt(worst_high),
    })
    wb.add_assertion(
        name="same_orbital_fraction_fails_beyond_A7",
        computed=str(verdict), expected="1", tolerance="0",
        unit="verdict (1 = close below A=7 and refuted above, as claimed)",
        source=("normalised at the alpha (one parameter); <8% for A=5,6,7 then "
                ">20% at A=9 and >70% at A=12. Recorded as a scope-(a) negative: "
                "this model ALONE does not reproduce w, which does not exclude "
                "the ingredient from a multi-term closure."),
    )
    ok &= worst_high > mp.mpf("0.2") and worst_low < mp.mpf("0.10")

    wb.add_data("scope", {
        "derives_a_magnitude": False,
        "what_is_proved_elsewhere": (
            "the NEGATIVE half: QOU.Mass.UniformBondSimpleGraphExclusion shows no "
            "uniform-bond simple-graph assembly can give the rise, for any graph "
            "family (a simple graph on 3 vertices has at most 3 edges)"
        ),
        "what_is_refuted_here": [
            "single-ratio scaling eps(z) = eps(1)*r^(z-1), for EVERY r "
            "(the two measured ratios differ by ~44%) -- kills the simplest form "
            "of the Markov-power mechanism, convention-independently",
            "the same-orbital-fraction law beyond A=7 (scope-(a))",
        ],
        "what_survives": (
            "the turnover LOCATION at A=4 from the SU(4) [1^n] support bound "
            "C(4,n)=0 for n>=5 -- parameter-free, but it locates only, and it "
            "rests on Wigner's symmetry-to-binding assumption which this corpus "
            "does not derive"
        ),
        "still_open": (
            "the SIZE of the rise: why eps(2)/eps(1) = 1.2137 and eps(3)/eps(1) "
            "= 2.1200. No mechanism tested here predicts either number."
        ),
    })

    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
