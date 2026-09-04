---
# qou-bq9l
title: Can the substrate carry a fractional twist at all?
status: completed
type: task
priority: normal
created_at: 2026-09-02T21:08:47Z
updated_at: 2026-09-02T21:15:03Z
---


RESOLVED 2026-09-02 -- computations/probes/can_the_substrate_carry_a_fractional_twist_probe.py,
6/6. YES -- and it needed no new ingredient. The two physics targets then come
out OPPOSITE, which is the actual finding.

THE MECHANISM WAS ALREADY IN THE BRAID GROUP. The Coxeter element
c_n = s_1 s_2 ... s_(n-1) satisfies c_n^n = Delta^2, the full twist and centre
generator of B_n -- so c_n is a genuine n-th ROOT of a twist. Verified: Delta^2
acts as a scalar on every block at n = 3,4,5, and

    |eigenvalue of c_n on block lambda| = q^( 2 c(lambda) / n )   EXACTLY

(worst deviation 1e-8 or better), where c(lambda) = sum over cells of (j-i) is
the content sum. Twist exponents are therefore RATIONAL with denominator
dividing n.

WHERE FRACTIONALITY STARTS. 2c(lambda) is always even, so it is divisible by n
at n=3 and n=4 for every partition:
    n=3  exponents  2, 0, -2                  all integer
    n=4  exponents  3, 1, 0, -1, -3           all integer
    n=5  exponents  4, 2, 4/5, 0, -4/5, -2,-4 FRACTIONAL at (3,2) and (2,2,1)
n = 5 IS THE FIRST STRAND COUNT CARRYING A FRACTIONAL TWIST. The arc had been
working at n=2 and n=3, exactly where the fractional part vanishes -- which is
why the ingredient looked absent.

Contrast the ribbon twist read directly off the content sum, theta = q^(2c):
an INTEGER power at every n. The fractionality lives in taking a ROOT of the
twist, not in the twist itself.

THE AVAILABLE SET (exhaustive over partitions, n <= 12; t = -2c/n in (0,1)):
    t      ratio   first realisation
    2/11   13/9    n=11 (5,2,2,1,1)
    2/9    11/7    n=9  (4,2,2,1)
    2/7    9/5     n=7  (3,2,2)
    1/3    2       n=12 (4,4,2,1,1)     <== QCD colour ratio, EXACTLY
    4/11   15/7    n=11 (4,3,2,2)
    1/2    3       n=8  (3,3,1,1)
    3/5    4       n=10 (4,3,1,1,1)
    2/3    5       n=9  (3,3,2,1)
    8/11   19/3    n=11 (4,3,2,1,1)
    4/5    9       n=5  (2,2,1)
    6/7    13      n=7  (3,2,1,1)
    8/9    17      n=9  (4,2,1,1,1)
    10/11  21      n=11 (5,2,1,1,1,1)
Thirteen distinct twists, and EVERY achievable ratio is rational -- a direct
consequence of t being rational.

THE TWO TARGETS COME OUT OPPOSITE.
 * QCD: t = 1/3 gives ratio EXACTLY 2, which is the 3bar/6 colour-factor ratio
   from 3(x)3 -- exact SU(3) group theory, no error bar, nothing fitted on
   either side. Realised at n=12 by (4,4,2,1,1) and (4,3,3,2), and at no
   smaller n.
 * NUCLEAR: 33.7055 requires t = 0.942372 and is NOT in the set. Nearest is
   10/11 giving 21, which would need the np 1S0 virtual state at 105.9 keV
   against the accepted ~66 keV -- a 60 % shift, far outside its uncertainty.

THE FINDING IS THE ASYMMETRY. A construction whose achievable ratios are
RATIONAL can meet a group-theory target and cannot meet a DYNAMICAL one -- and
the nuclear 33.7 is dynamical, set by how close two shallow states sit to
threshold.

CAVEATS, stated in the probe and the witness:
 - the t=1/3 hit is exact and unfitted but SUGGESTIVE, NOT EVIDENTIAL: thirteen
   small-denominator rationals is not a sparse set and 1/3 is not an unlikely
   member. No significance test is offered and none should be inferred.
 - this shows the twist EXISTS, not that the construction USES it. Nothing here
   attaches c_n to a bond, recomputes a binding energy, or gives any reason the
   physical bond should carry c_n rather than another element.
 - n <= 12 is a CUTOFF, so "not in the set" for the nuclear target is a
   statement about that range, not a theorem. The substantive point survives:
   the set is rational at every n while the target is a measured ratio.
