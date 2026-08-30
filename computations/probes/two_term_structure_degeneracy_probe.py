#!/usr/bin/env python3
"""two_term_structure_degeneracy_probe.py

The shell+saturation pairing is DEGENERATE on the data, and the convex half then
faces a two-number fingerprint with no free parameters.

THE PROPOSAL BEING TESTED
-------------------------
SaturationSignGateTension proved that b3 > 0, b4 > 0 and a saturating binding
force >= 2 contributions of opposite curvature. The natural pairing, and the one
I proposed, was the corpus's own two pieces: a CONVEX s-shell term (support-
bounded, dying at A=5) plus a SATURATING bounded-degree coordination term
(CoordinationSaturation).

RESULT 1 -- THE SATURATING HALF IS INERT WHERE THE DATA IS
-----------------------------------------------------------
A degree cap at k gives bond count f_k(A) = A*min(A-1,k)/2. For A <= k+1 the cap
DOES NOT BIND, so f_k is identically the complete-graph count C(A,2) there. With
k >= 3 that covers the whole A <= 4 window, and C(A,2) contributes exactly zero:

    k=1:  b3-contrib -1.5   b4-contrib  2.0    (a pure dimer model; wrong sign)
    k=2:  b3-contrib  0.0   b4-contrib -2.0
    k=3:  b3-contrib  0.0   b4-contrib  0.0
    k>=3: identical to k=3 -- the cap never binds below A=5

**A coordination cap at k >= 2 contributes NOTHING to b3.** Every (saturating,
convex) pair I set up came back with a singular 2x2 system, and the singularity
is this fact, not a numerical accident. Lean: SaturationInvisibleToCumulants.

This is NOT a contradiction with the two-term necessity theorem: the two terms
act in DISJOINT REGIMES (convex below A=5, saturating above) rather than
together. But it changes the test completely.

RESULT 2 -- SO THE CONVEX TERM FACES A ZERO-PARAMETER FINGERPRINT
------------------------------------------------------------------
With the saturating half inert, ONE term carries b2, b3 and b4. That is three
constraints on one coefficient, and since scaling by gamma cancels in a ratio
(ratios_are_scale_free), it leaves TWO PARAMETER-FREE PREDICTIONS:

    isospin average       b3/b2 = 0.6411228   b4/b2 = 4.1551403
    Coulomb-corrected     b3/b2 = 0.8127866   b4/b2 = 3.4684851

Nothing tested is close:

    dim[1^A] = C(4,A)   (-2.333,  3.5)     wrong sign on b3/b2
    A^3                 ( 0.375,  0.5)     b4/b2 out by ~8x
    A!                  ( 0.0  ,  6.0)     b3/b2 vanishes
    indicator [A<=4]    (-2.0  ,  3.0)     wrong sign
    k=1 dimer           (-1.5  ,  2.0)     wrong sign
    2^A                 (-1.0  ,  2.0)     wrong sign

WHY THIS IS PROGRESS ANYWAY
---------------------------
The programme's target was a single ratio, eps(2)/eps(1), which a 9.4% convention
band made nearly unfalsifiable -- many candidates sit inside it and hitting it is
not evidence. The fingerprint is TWO numbers that a candidate must hit with ZERO
free parameters. That is the discriminator the earlier work said was needed and
did not have.

SCOPE
-----
Refutes the SPECIFIC pairing (shell + saturation) as an explanation of the
cumulants, by showing the saturating half has no signature in their window. Does
NOT touch CoordinationSaturation itself, which is a statement about A -> infinity
and is unaffected by having no A <= 4 signature. Does NOT refute two-term
structures in general. Derives no magnitude.

Bean qou-edt7.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb, factorial  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)


def capped(k):
    return lambda A: mp.mpf(A * min(A - 1, k)) / 2


def main() -> int:
    wb = WitnessBuilder("two-term-structure-degeneracy", engine="mpmath")
    wb.set_description(
        "The shell+saturation pairing is degenerate on the data: a coordination "
        "cap at k >= 2 contributes exactly zero to b3 (and k >= 3 zero to b4), "
        "because the cap does not bind below A=5. So the convex half alone "
        "carries b2, b3, b4 -- three constraints on one coefficient, leaving a "
        "TWO-NUMBER parameter-free fingerprint (b3/b2, b4/b2) that nothing tested "
        "hits. Refutes the pairing, not CoordinationSaturation."
    )
    ok = True

    print("RESULT 1 -- a degree cap is inert below A=5\n")
    rows, n_zero = [], 0
    for k in (1, 2, 3, 4, 6, 10):
        f = capped(k)
        c3 = f(3) - 3 * f(2)
        c4 = f(4) - 4 * f(3) + 6 * f(2)
        z = abs(c3) < mp.mpf("1e-30")
        n_zero += z
        rows.append({"k": k, "f2": fmt(f(2)), "f3": fmt(f(3)), "f4": fmt(f(4)),
                     "b3_contrib": fmt(c3), "b4_contrib": fmt(c4),
                     "b3_contrib_is_zero": bool(z)})
        print(f"  k={k:<3} f(2,3,4)=({mp.nstr(f(2),4)},{mp.nstr(f(3),4)},{mp.nstr(f(4),4)})"
              f"   b3-contrib {mp.nstr(c3,5):>7}   b4-contrib {mp.nstr(c4,5):>7}")
    wb.add_data("capped_bond_counts", rows)
    wb.add_assertion(
        name="cap_k_ge_2_contributes_nothing_to_b3",
        computed=str(n_zero), expected="5", tolerance="0",
        unit="values of k in {1,2,3,4,6,10} with zero b3 contribution",
        source=("the cap does not bind for A <= k+1, so f_k = C(A,2) on the "
                "window and C(A,2) has zero b3 and b4 contributions; only k=1 "
                "contributes, with the wrong sign. Lean: "
                "SaturationInvisibleToCumulants.complete_contributes_nothing"),
    )
    ok &= n_zero == 5

    D = ame_binding_mev(1, 2)
    T3, He3, He4 = ame_binding_mev(1, 3), ame_binding_mev(2, 3), ame_binding_mev(2, 4)

    print("\nRESULT 2 -- the convex term alone must hit a two-number fingerprint\n")
    fps = {}
    for nm, B3 in (("isospin_average", (T3 + He3) / 2), ("3H_Coulomb_corrected", T3)):
        b2, b3 = D, B3 - 3 * D
        b4 = He4 - 4 * B3 + 6 * D
        fps[nm] = {"b3_over_b2": fmt(b3 / b2), "b4_over_b2": fmt(b4 / b2)}
        print(f"  {nm:<22} b3/b2 = {mp.nstr(b3/b2,8):>11}   b4/b2 = {mp.nstr(b4/b2,8):>11}")
    wb.add_data("target_fingerprint", fps)

    tgt3 = ((T3 + He3) / 2 - 3 * D) / D
    tgt4 = (He4 - 4 * (T3 + He3) / 2 + 6 * D) / D
    cands = {
        "dim[1^A] = C(4,A)": lambda A: mp.mpf(comb(4, A)) if A <= 4 else mp.mpf(0),
        "A^3": lambda A: mp.mpf(A ** 3),
        "A!": lambda A: mp.mpf(factorial(A)),
        "indicator [A<=4]": lambda A: mp.mpf(1) if A <= 4 else mp.mpf(0),
        "k=1 dimer": capped(1),
        "2^A": lambda A: mp.mpf(2 ** A),
    }
    print(f"\n  {'candidate':<22} {'b3/b2':>11} {'b4/b2':>11}   (target "
          f"{mp.nstr(tgt3,6)} / {mp.nstr(tgt4,6)})")
    crows, n_miss = [], 0
    for nm, f in cands.items():
        r3 = (f(3) - 3 * f(2)) / f(2)
        r4 = (f(4) - 4 * f(3) + 6 * f(2)) / f(2)
        miss = abs(r3 - tgt3) / abs(tgt3) > mp.mpf("0.2") or \
               abs(r4 - tgt4) / abs(tgt4) > mp.mpf("0.2")
        n_miss += miss
        crows.append({"candidate": nm, "b3_over_b2": fmt(r3), "b4_over_b2": fmt(r4),
                      "misses": bool(miss)})
        print(f"  {nm:<22} {mp.nstr(r3,7):>11} {mp.nstr(r4,7):>11}   "
              f"{'MISS' if miss else 'within 20%'}")
    wb.add_data("fingerprint_candidates", crows)
    wb.add_assertion(
        name="no_tested_convex_term_hits_the_fingerprint",
        computed=str(n_miss), expected=str(len(cands)), tolerance="0",
        unit="candidates missing the fingerprint by >20% on either ratio",
        source="three constraints on one coefficient leave two parameter-free "
               "predictions; scaling cancels (ratios_are_scale_free)",
    )
    ok &= n_miss == len(cands)

    wb.add_data("verdict", {
        "pairing_refuted": "shell + saturation, as an explanation of the cumulants",
        "why": "the saturating half has no signature below A=5, so it cannot be "
               "one of the two terms in the window where b3 and b4 live",
        "not_touched": ["CoordinationSaturation itself (a statement about A -> inf)",
                        "two-term structures in general"],
        "what_replaces_the_target": ("a TWO-number fingerprint (b3/b2, b4/b2) hit "
                                     "with ZERO free parameters, replacing the "
                                     "single ratio a 9.4% convention band made "
                                     "nearly unfalsifiable"),
        "derives_a_magnitude": False,
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
