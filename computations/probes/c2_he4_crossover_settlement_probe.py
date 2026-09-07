"""Settle the A = 3 -> 4 crossover under the Borromean word: measure c2(4He).

WHY THIS EXISTS
---------------
PR #6931 refuted the CENTRAL FINDING of `2026-09-04-c2-does-not-continue-the-
cancellation.md` (#6559) -- that the ratio `c2.h^2 / c1.h` is monotone through 1
across A -- but left ONE claim untested rather than disproved:

    "the h_q expansion crosses over between A = 3 and A = 4"

because `c1_leading_coefficient_derived_probe` carries `P_OF["4He"] = 3`. One
series order is lost to the 0/0 seminormal quotients, so `d.p = 2` and
`d.coeff(2)` is unavailable -- `c2(4He)` comes back `None`. Every other case has
its `c2`. This probe raises the 4He order to P = 4 and measures the one missing
number.

WHY IT IS MEASURED AND NOT PREDICTED
------------------------------------
`c1` HAS a closed form -- `(a.Z + b.N)(2^-(A+1) - 2^-2A) - 4(i_pp - i_nn)2^-2A`
-- which is how `c1(4He) = 7/128` was predicted before it was measured and then
confirmed twice over (#6931).

**c2 has no closed form IN (Z, N), and that is a narrower fact than this file
originally claimed.** An exhaustive search over subsets of a 13-function basis
-- `Z.D, N.D, dI.E, D, E, Z.E, N.E, A.E, A.D, ZZ.D, NN.D, ZN.D, ZZ.E, NN.E,
ZN.E` -- found **ZERO** subsets up to size 5 reproducing all six grouped values
AND all five known Borromean values. That measurement stands. The quadratic
terms were included on purpose: `tr_M` factorises across the two nucleons
(disjoint strand sets), which makes the LOG-derivative additive at first order,
so second order was expected to carry a `phi_p.phi_n` cross term. It does not
fit either.

🛑 **BUT THE CONCLUSION I DREW FROM IT WAS WRONG, AND IS RETRACTED HERE.** This
file said "there is nothing to predict from, and the number has to be computed",
and PR #6966 generalised that to "c1's per-letter additivity is special to first
order and does not propagate up the expansion". **A closed form for c2 exists.**
`atom_bond_product_closed_form_probe.py` (bean `qou-qqm4`, landed 369f4bb0a7)
gives

    tr(atom) = PROD_nucleons a(1 + r.e + q.e^2)
             * PROD_bonds  (1/2)(1 + rho_b.e + tau_b.e^2)

and reproduces **c0, c1 AND c2 for A = 2..5, 9/9, with no free parameter** --
every factor measured on a smaller object. Verified here by running it directly
rather than trusting the commit message: `9/9 -- c0, c1 and c2 all reproduced`.

The two results do not conflict; my FRAMING of mine did. In that author's words,
c2's closed form "is just not a form in (Z, N) alone ... it is a form in the
ORDERING". Multiplicativity DOES propagate to second order -- over **blocks and
bonds**, not per letter. My basis had no bond variable in it, so it could not
have found this however many subsets it enumerated, and a negative result about
a basis is not a negative result about the quantity.

Their form carries its own scope: sorted orderings only, orders 0-2, A <= 5, and
not proved. So this is a narrower closed form than "c2 is solved" -- but it is
decisively more than "nothing to predict from".

**The 439/512 measured below is unaffected and is now independently
corroborated** -- their 9/9 includes 4He. The number was right; the story I told
around it was too strong.

WHAT IT DECIDES
---------------
Ratio `r = c2.h^2 / (c1.h)` at the proton pin, with `c1(4He) = 7/128`:

    r > 1  -> second order exceeds first at A = 4. #6559's crossover claim
              SURVIVES the ordering change even though its supporting pattern
              (a monotone column) does not.
    r < 1  -> it does not survive, and the crossover reading is fully retired.

Either way this is scope-(a): a statement about a series ordering in one braid
word convention, not about the physics.

The Borromean column already measured (#6931), for context:

    pp  0.8174   pn  1.2385   nn  INFINITE (c1 = 0)   T  4.9045   3He  0.9722

It is not monotone and not ordered by A, so no value of r here restores #6559's
argument -- only its A = 4 conclusion is in question.

NO FLOAT in the extraction: exact `fractions.Fraction` power series throughout.
mpmath only for the final ratio display, at 30 dps.
"""
from __future__ import annotations

import os
import sys
import time
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMP = os.path.dirname(_HERE)
for _p in (_COMP, _HERE, os.path.join(_COMP, "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from c1_leading_coefficient_derived_probe import tr_M_series, c0_derived  # noqa: E402

# Measured in #6931 by re-running the c1 probe on main under the Borromean word.
C1_HE4_BORROMEAN = F(7, 128)
C0_HE4 = F(7, 128)
HBAR_Q = "0.099081716044258508"   # proton pin

# The five Borromean ratios already measured, for the report.
KNOWN = (("pp", 2, "0.8174"), ("pn", 2, "1.2385"), ("nn", 2, "INFINITE (c1=0)"),
         ("T", 3, "4.9045"), ("3He", 3, "0.9722"))


def main() -> int:
    t0 = time.time()

    def log(m):
        print(f"  [{time.time()-t0:7.1f}s] {m}", flush=True)

    mp.mp.dps = 30
    P = 4
    log(f"4He (Z=2, N=2, n=12) at series precision P = {P} "
        f"(committed probe uses 3, which cannot reach c2)")

    log("free word ...")
    tf = tr_M_series(2, 2, False, P, log=log)
    log("atom word ...")
    ta = tr_M_series(2, 2, True, P, log=log)
    d = tf - ta
    log(f"difference precision after pipeline: d.p = {d.p} (need > 2 for c2)")

    a0, a1 = d.coeff(0), d.coeff(1)
    a2 = d.coeff(2) if d.p > 2 else None
    log(f"a0 = {a0}   a1 = {a1}   a2 = {a2}")

    failures = []

    # -- controls: this run must reproduce what is already known ---------------
    if a0 != C0_HE4:
        failures.append(f"a0 = {a0} != derived floor c0 = {C0_HE4}")
    if a0 != c0_derived(4):
        failures.append(f"a0 = {a0} != c0_derived(4) = {c0_derived(4)}")
    if a1 != C1_HE4_BORROMEAN:
        failures.append(f"a1 = {a1} != the c1(4He) = {C1_HE4_BORROMEAN} measured in #6931")
    if a2 is None:
        failures.append(f"c2 still unavailable at P = {P}: d.p = {d.p}")
        for f in failures:
            print(f"FAIL  {f}")
        return 1

    c2 = a1 + a2            # the committed probe's convention
    h = mp.mpf(HBAR_Q)
    c1f = mp.mpf(C1_HE4_BORROMEAN.numerator) / C1_HE4_BORROMEAN.denominator
    c2f = mp.mpf(c2.numerator) / c2.denominator
    ratio = (c2f * h ** 2) / (c1f * h)

    print()
    print("=" * 74)
    print(f"  c2(4He) borromean = {c2}   ({float(c2):.6f})")
    print(f"  c1(4He) borromean = {C1_HE4_BORROMEAN}   ({float(C1_HE4_BORROMEAN):.6f})")
    print(f"  ratio c2.h^2 / c1.h = {float(ratio):.4f}")
    print("=" * 74)
    print("  the Borromean column, with A = 4 now filled in:")
    for name, A, r in KNOWN:
        print(f"    {name:>4s}  A={A}   {r}")
    print(f"    {'4He':>4s}  A=4   {float(ratio):.4f}")
    print()
    # Be precise about WHICH claim this settles. #6559 said the expansion
    # "crosses over BETWEEN A = 3 and A = 4", which asserts two things: the
    # ratio exceeds 1 at A = 4, AND it does not below. Only the first is
    # decided here, and the second is already FALSE under Borromean -- T
    # (A = 3) is 4.90 and pn (A = 2) is 1.24, both above 1.
    if ratio > 1:
        print("  VERDICT: at A = 4 the second order EXCEEDS the first.")
        print()
        print("  What that does and does NOT settle:")
        print("    SURVIVES  the endpoint fact -- ratio > 1 at A = 4.")
        print("    STILL FALSE  the LOCATION. #6559 said the expansion crosses")
        print("      over BETWEEN A = 3 and A = 4, which also requires ratio < 1")
        print("      below. Under Borromean it is already > 1 at T (4.90, A = 3)")
        print("      and at pn (1.24, A = 2), so there is no crossing THERE.")
        print("    STILL REFUTED  the argument -- the monotone column (#6931).")
    else:
        print("  VERDICT: at A = 4 the second order does NOT exceed the first.")
        print("  #6559's conclusion fails at its own endpoint; the reading is")
        print("  retired in full -- argument (#6931) and conclusion alike.")
    print()

    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        return 1
    print(f"PASS  3/3 controls (a0 = c0 two ways, a1 = the recorded c1) "
          f"and c2(4He) = {c2} measured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
