---
# qou-1uul
title: Is the c5 sign robust across bond orderings, and what is c6?
status: completed
type: task
priority: normal
created_at: 2026-09-03T03:33:04Z
updated_at: 2026-09-03T04:03:41Z
---


RESOLVED 2026-09-03 -- computations/probes/c5_sign_is_robust_convergence_claim_is_not_probe.py,
6/6. SPLIT VERDICT: the sign survives, the convergence claim does not.

TESTED over 12 bond orderings at A=5 (canonical production + 11 random shuffles
of the ten bonds), 5He 'pnpnn', n=15.

    trial      c2         c3         c4         c5      |c5/c4|  signs
    0 canon    7.27262   -3.78605   -1.23080   +1.60450  1.3036  + - - +
    1..11      7.27262   -2.40..-3.12  -2.50..-4.19  +2.24..+3.26  0.71..0.94

c5 > 0 in 12/12, range +1.60..+3.26, sign pattern + - - + IDENTICAL in every
ordering. So the correction to qou-bc09 / qou-38i9 STANDS -- "every many-body
term is negative" is false from A=5, regardless of bond-order convention.

|c5/c4| > 1 in 1/12 -- AND THE ONE IS THE CANONICAL ORDERING, the only one
qou-441t tested. Range 0.7077..1.3036, STRADDLING 1. So "the hierarchy does not
converge" was an artifact of its convention and IS WITHDRAWN. What can be said:
at A=5 the ratio is of order one and its position relative to 1 is
convention-dependent -- neither demonstrably convergent nor divergent.

WHY THEY DIFFER: c2 is EXACTLY ordering-independent (spread 3e-15; a
two-element subset has one bond and no internal order). From c3 up the
individual cumulants swing by 1.6-3.4x while the tail sum c3+c4+c5 moves 23.5%
-- the artifact REDISTRIBUTES weight between orders. A sign survives that; a
ratio of two swinging quantities does not. That applies to anything else in this
arc quoted as a cumulant ratio at fixed convention.

UNTOUCHED: qou-441t's cumulant IDENTIFICATION (L additive on disjoint blocks =>
Moebius inversion is a genuine cumulant expansion). Exact algebraic fact, no
ordering affects it.

SAMPLE: 12 of 3.63e6 orderings -- enough to FALSIFY a universal claim (11
counterexamples) and NOT enough to characterise a distribution. No
distributional statement made. One nucleon ordering only; nucleon ordering is a
separate artifact and is not varied.
