---
# qou-441t
title: 'Cumulant hierarchy: measure the tower decay rate from order-zero correlations'
status: completed
type: task
priority: normal
created_at: 2026-09-02T21:49:31Z
updated_at: 2026-09-02T21:55:00Z
---


RESOLVED 2026-09-02 -- computations/probes/cumulant_hierarchy_does_not_converge_probe.py,
6/6. The measurement is legitimate AND it corrects two of my own claims.

WHY IT IS A MEASUREMENT (owner's framing, now made precise). The Markov trace is
the order-zero observable and higher graded orders are not readable from it. But
the higher orders are reachable INDIRECTLY through correlations BETWEEN
order-zero observables -- subtract the parts from the whole and what remains is
the correlation, and the correlation is indicative of higher-order behaviour.

THE IDENTIFICATION IS EXACT, NOT AN ANALOGY. The Markov trace is multiplicative
on disjoint strand blocks, so L = log(tr_free/tr_atom) is ADDITIVE on them.
Measured with bonds only INSIDE each part and no cross bonds:
    L[{0,1}]          = 0.676821592386
    L[{3,4}]          = 0.907262265533
    L[both, no cross] = 1.584083857920   residual 0.000e+00
Additivity on disjoint blocks is EXACTLY the condition making a Moebius
inversion over subsets a CUMULANT expansion. So c_k is the k-th cumulant -- what
the k-body correlation contributes beyond every lower one -- not a loosely-named
"many-body term". Verified two independent ways (recursive vs direct Moebius),
agreeing to 2.7e-15 across all 26 subsets.

(NOTE: my first additivity test was mis-specified -- the "union" subset included
the CROSS bonds, giving residual 1.227. Fixed by placing bonds only within each
part.)

THE HIERARCHY AT A=5 (5He, pnpnn, n=15):
    k   terms   sum c_k          MeV        ratio     partial sum
    2   10      +7.272615735    +30.44303   --        7.272615735
    3   10      -3.786046394    -15.84832   0.520589  3.486569341
    4    5      -1.230795704     -5.15209   0.325087  2.255773637
    5    1      +1.604498983     +6.71640   1.303627  3.860272620
    reconstruction sum_k c_k = L_full = 3.860272620 exactly

IT DOES NOT CONVERGE. Ratios fall 0.52, 0.33, then RISE PAST ONE to 1.30. c_5 is
larger than c_4 and comparable to c_3; partial sums oscillate rather than settle.

AND c_5 FLIPS SIGN POSITIVE. Signs: c_2 +, c_3 -, c_4 -, c_5 +.

THIS CORRECTS qou-bc09 AND qou-38i9, both mine. Both reported EVERY measured
many-body term as negative and used it to argue a naive pairwise sum is an UPPER
bound on binding. Both stopped at c_4 -- because 4He is A=4 and HAS no fifth
order. At A=5 the sign flips.
  * 4He IS UNAFFECTED: orders 2,3,4 exhaust A=4, all were measured negative, and
    the bound argument there stands.
  * THE GENERAL CLAIM DOES NOT: "every many-body term is negative" and "the naive
    sum is an upper bound" are false from A=5 onward.

c_5 IS NOT NOISE. 32 signed terms, sum of |terms| = 42.179648 so cancellation is
only 26.3x; largest single term 3.860273; f64 floor ~9.3e-15; c_5 sits 1.7e14x
above it.

WHAT IT SAYS ABOUT THE TOWER: the higher orders are NOT SUPPRESSED. A convergent
cumulant hierarchy would say the tower is dominated by low orders and truncation
is safe; this says the opposite at the first order testable beyond c_4.
CONSEQUENCE: everything in this arc computed at A <= 4 is complete for its own A
(the expansion terminates at k = A) but gives NO licence to extrapolate. Any
claim of the form "the many-body terms behave like X, so at larger A ..." is
unsupported, including several of mine.

CAVEATS:
 - ONE ordering and ONE bond order (production 'pnpnn', interleaved). qou-38i9
   measured bond order worth 38-40 % at A=4, so MAGNITUDES here are
   convention-dependent at that level. The SIGN of c_5 and the non-convergence
   are NOT re-tested across orderings and should be before either is quoted as
   ordering-independent.
 - A=5 is the FIRST AND ONLY order tested beyond c_4. One non-convergent step is
   not an asymptotic statement; c_6 needs A=6 (n=18, ~172 s/trace x 64 subsets,
   ~3 hours). "Does not converge" means the ratio exceeds one at the first
   opportunity to test it.
 - Still an evaluation at q = q0. The cumulants are correlations BETWEEN
   order-zero observables -- the intended indirect route -- but no graded piece
   is computed and none is claimed.
