#!/usr/bin/env python3
"""body_order_is_finite_difference_of_coordination_weight_probe.py

The body-order cumulant tower IS the finite-difference tower of one function.

WHAT THIS IS
------------
`qou-edt7` asks what assembly can produce the measured `b3 > 0`, given that both
corpus assemblies provably cannot: the multiplicative Mayer form `W = 1 - PROD f`
forces `b3 < 0` (QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos) and the
pairwise-additive form forces `b3 = 0` exactly
(QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_of_isPairwise).

This probe does NOT propose a functional. Proposing a functional because it lands
`b3 > 0` is the anchor inversion the bean explicitly forbids. It changes
variables, and the change of variables turns the question into a different and
much smaller one.

THE CHANGE OF VARIABLES
-----------------------
Any binding map on the mass number can be written

    B(A) = C(A,2) * w(A-1),          z := A-1,   w(z) := B(A) / C(A,2)

This is a DEFINITION, not a model: `w` is just the mean binding per nucleon pair
of a nucleus whose every nucleon has coordination `z = A-1` in the complete graph. No
content is added by writing it, and none is lost.

Under it, the Ursell/Moebius cumulant of order `n` becomes, EXACTLY,

    b_n = C(n,2) * Delta^{n-2} w (1)

where `Delta` is the forward difference `Delta w (z) = w(z+1) - w(z)`. The proof
is term-by-term, not a summation identity: the subset-of-a-subset rule
`C(n,k) C(k,2) = C(n,2) C(n-2,k-2)` matches the two sums entry by entry under
`k = j+2`, signs included.

WHAT THAT BUYS
--------------
An infinite tower of unknown many-body coefficients `b_2, b_3, b_4, ...` is
exactly one unknown function `w(z)`. And the three facts the corpus has proved
separately become three statements about `w`:

  * `w` CONSTANT            <=>  b_n = 0 for all n >= 3.   (the pairwise wall)
  * `w` NON-INCREASING      =>   b3 <= 0.                  (so nature's b3 > 0
                                 forces `w` to RISE at z=1)
  * b4 > 0                  <=>  `w` CONVEX at z = 1.

So `b3 > 0` is not exotic. It says one thing: the mean binding per pair is
LARGER at coordination 2 than at coordination 1. The question "what assembly
gives b3 > 0" becomes "why does w rise", which is a question about one function
of one integer variable.

WHAT IT DOES NOT BUY
--------------------
The identity is a reparameterisation and is therefore tautologically available.
It derives no magnitude. It cannot: `w` is DEFINED by inverting `B`, so fitting
`w` to AME is fitting `B` to AME with extra steps. Its value is that it says
what a derivation has to produce, and that it explains the two failures and the
A >= 5 blow-up with one object instead of three.

Checks (all exact, mpmath at 50 dps; no float64 anywhere):
  1. the identity, term-by-term, on a RANDOM w for n = 2..8 (algebraic, no AME)
  2. the identity against the AME2020 cumulants for n = 3, 4
  3. the constant-w corollary: all cumulants above order 2 vanish
  4. the measured shape of w across A = 2..56
  5. the blow-up: high differences of the measured w, which is where the
     A >= 5 divergence comes from

Bean qou-edt7 (successor question). Companion Lean:
QOU/Mass/CoordinationWeightDifferences.lean
"""
from __future__ import annotations

import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb  # noqa: E402
from random import Random  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)


def cumulant(B, n):
    """Ursell b_n by Moebius inversion over the subset lattice, B(0)=B(1)=0."""
    return sum((-1) ** (n - k) * mp.mpf(comb(n, k)) * B(k) for k in range(2, n + 1))


def fwd_diff(w, m, z):
    """Delta^m w (z), forward difference."""
    return sum(
        (-1) ** (m - j) * mp.mpf(comb(m, j)) * w(z + j) for j in range(m + 1)
    )


def main() -> int:
    wb = WitnessBuilder(
        "body-order-is-finite-difference-of-coordination-weight",
        engine="mpmath",
    )
    wb.set_description(
            "The Ursell body-order cumulants of any complete-graph assembly are "
            "the finite differences of its coordination weight w(z) = B(A)/C(A,2): "
            "b_n = C(n,2) * Delta^{n-2} w(1). A reparameterisation, exact, deriving "
            "no magnitude — it turns an infinite tower of many-body coefficients "
            "into one function of one integer variable, and gives the pairwise wall "
            "(w constant), the Mayer sign (w non-increasing) and the A>=5 blow-up "
        "(finite differences of a peaked w) a single common cause."
    )

    ok = True

    # ---- check 1: the identity on a RANDOM w, n = 2..8 -------------------
    # Algebraic: no AME input, so this tests the identity and nothing else.
    rng = Random(20260830)
    wvals = {z: mp.mpf(rng.uniform(-3, 3)) for z in range(1, 10)}
    w_rand = lambda z: wvals[z]                                  # noqa: E731
    B_rand = lambda A: mp.mpf(comb(A, 2)) * w_rand(A - 1)        # noqa: E731

    print("1. identity  b_n = C(n,2) * Delta^{n-2} w(1)  on a RANDOM w")
    max_dev = mp.mpf(0)
    for n in range(2, 9):
        lhs = cumulant(B_rand, n)
        rhs = mp.mpf(comb(n, 2)) * fwd_diff(w_rand, n - 2, 1)
        dev = abs(lhs - rhs)
        max_dev = max(max_dev, dev)
        print(f"   n={n}  b_n={mp.nstr(lhs, 12):>18}   C(n,2)D^{n-2}w(1)={mp.nstr(rhs, 12):>18}   |dev|={mp.nstr(dev, 3)}")
    wb.add_assertion(
        name="identity_holds_for_arbitrary_w",
        computed=fmt(max_dev),
        expected=fmt(mp.mpf(0)),
        tolerance="1e-45",
        unit="MeV (arbitrary units here — w is random)",
        source="term-by-term via C(n,k)C(k,2) = C(n,2)C(n-2,k-2); n = 2..8",
    )
    ok &= max_dev < mp.mpf(10) ** -45

    # ---- check 2: the same identity against AME2020 ----------------------
    D = ame_binding_mev(1, 2)
    A3 = (ame_binding_mev(1, 3) + ame_binding_mev(2, 3)) / 2   # charge-symmetric
    He4 = ame_binding_mev(2, 4)

    def B_ame(A):
        return {2: D, 3: A3, 4: He4}[A]

    w_ame = {1: D / 1, 2: A3 / 3, 3: He4 / 6}
    b3 = cumulant(B_ame, 3)
    b4 = cumulant(B_ame, 4)
    b3_via_w = mp.mpf(3) * (w_ame[2] - w_ame[1])
    b4_via_w = mp.mpf(6) * (w_ame[3] - 2 * w_ame[2] + w_ame[1])

    print("\n2. against AME2020 (vendored table, NOT a hardcoded literal)")
    print(f"   w(1)={mp.nstr(w_ame[1], 12)}  w(2)={mp.nstr(w_ame[2], 12)}  w(3)={mp.nstr(w_ame[3], 12)}")
    print(f"   b3 = {mp.nstr(b3, 12)}   3*(w2-w1)      = {mp.nstr(b3_via_w, 12)}")
    print(f"   b4 = {mp.nstr(b4, 12)}   6*(w3-2w2+w1)  = {mp.nstr(b4_via_w, 12)}")
    dev_ame = max(abs(b3 - b3_via_w), abs(b4 - b4_via_w))
    wb.add_assertion(
        name="identity_holds_at_ame_orders_3_and_4",
        computed=fmt(dev_ame),
        expected=fmt(mp.mpf(0)),
        tolerance="1e-45",
        unit="MeV",
        source="AME2020 via codata_constants.ame_binding_mev; A=3 isospin-averaged",
    )
    ok &= dev_ame < mp.mpf(10) ** -45

    # the two sign facts, stated as what they are: readings of w, not fits
    print(f"\n   b3 > 0  <=>  w rises at z=1:   w(2)-w(1) = {mp.nstr(w_ame[2]-w_ame[1], 10)}  (> 0)")
    print(f"   b4 > 0  <=>  w convex at z=1:  D^2 w(1)  = {mp.nstr(w_ame[3]-2*w_ame[2]+w_ame[1], 10)}  (> 0)")
    wb.add_assertion(
        name="ame_w_rises_at_z1",
        computed=fmt(w_ame[2] - w_ame[1]),
        expected="0.4754067",
        tolerance="1e-6",
        unit="MeV per nucleon pair",
        source="w(2)-w(1); positive, which is exactly the content of b3 > 0",
    )

    # ---- check 3: constant w kills every cumulant above order 2 ----------
    c = mp.mpf("1.234567890123456789")
    B_const = lambda A: mp.mpf(comb(A, 2)) * c                   # noqa: E731
    worst = max(abs(cumulant(B_const, n)) for n in range(3, 9))
    print(f"\n3. constant w: max |b_n| over n=3..8  =  {mp.nstr(worst, 3)}   (the pairwise wall)")
    wb.add_assertion(
        name="constant_w_gives_vanishing_higher_cumulants",
        computed=fmt(worst),
        expected=fmt(mp.mpf(0)),
        tolerance="1e-45",
        unit="MeV",
        source="recovers QOU.Mass.PairwiseCumulantVanishing as the Delta w = 0 case",
    )
    ok &= worst < mp.mpf(10) ** -45

    # ---- check 4: the measured shape of w --------------------------------
    print("\n4. measured w(z) = B(A)/C(A,2)")
    table = [("2H", 1, 2), ("3H/3He avg", None, 3), ("4He", 2, 4), ("5Li", 3, 5),
             ("6Li", 3, 6), ("7Li", 3, 7), ("9Be", 4, 9), ("12C", 6, 12),
             ("16O", 8, 16), ("40Ca", 20, 40), ("56Fe", 26, 56)]
    wmeas = {}
    rows = []
    for name, Z, A in table:
        b = A3 if A == 3 else ame_binding_mev(Z, A)
        wz = b / mp.mpf(comb(A, 2))
        wmeas[A - 1] = wz
        rows.append({"nuclide": name, "A": A, "z": A - 1,
                     "B_MeV": fmt(b), "B_per_A_MeV": fmt(b / A), "w_z_MeV": fmt(wz)})
        print(f"   A={A:<3} z={A-1:<3} {name:<11} B/A={mp.nstr(b/A, 6):>9}   w(z)={mp.nstr(wz, 8):>12}")
    wb.add_data("coordination_weight_table", rows)

    peak_z = max(wmeas, key=lambda z: wmeas[z])
    print(f"\n   w peaks at z = {peak_z}  (A = {peak_z+1}, the alpha particle), then decays monotonically")
    wb.add_assertion(
        name="w_peaks_at_the_alpha_particle",
        computed=str(peak_z),
        expected="3",
        tolerance="0.5",
        unit="coordination number z = A-1",
        source="max over the measured table; w rises 1->3 then falls monotonically to A=56",
    )
    ok &= peak_z == 3

    # ---- check 5: where the A>=5 blow-up comes from ----------------------
    # High forward differences of a peaked function grow and alternate. The
    # cumulant tower inherits that, multiplied by a growing C(n,2).
    print("\n5. the blow-up, as finite differences of the measured w at z=1")
    zs = [1, 2, 3, 4, 5, 6]
    wfun = lambda z: wmeas[z]                                     # noqa: E731
    diffs = []
    for m in range(0, 5):
        dm = fwd_diff(wfun, m, 1)
        bn = mp.mpf(comb(m + 2, 2)) * dm
        diffs.append({"order_n": m + 2, "delta_m": fmt(dm), "b_n_MeV": fmt(bn)})
        print(f"   n={m+2}  D^{m} w(1) = {mp.nstr(dm, 10):>14}   b_n = C(n,2)*D^m = {mp.nstr(bn, 10):>14}")
    wb.add_data("blowup_as_differences", diffs)
    print("   -> the tower diverges because it expands a PEAKED w around z=1,")
    print("      three steps below its maximum. That is an expansion-point defect,")
    print("      not evidence against the assembly.")

    wb.add_data("scope", {
        "is_a_derivation": False,
        "why_not": (
            "w(z) := B(A)/C(A,2) is defined by inverting B, so fitting w to AME is "
            "fitting B to AME. The identity derives no magnitude and cannot."
        ),
        "what_it_establishes": (
            "that the infinite body-order tower is one function of one integer "
            "variable, and that the pairwise wall (w constant), the Mayer sign "
            "(w non-increasing) and the A>=5 blow-up (differences of a peaked w) "
            "are three readings of that single function"
        ),
        "open": (
            "derive w(z). b3 > 0 is exactly 'w rises from z=1 to z=2'; saturation "
            "of B/A is exactly 'z*w(z) is bounded', so w must be non-monotone. "
            "Neither is supplied here."
        ),
    })

    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
