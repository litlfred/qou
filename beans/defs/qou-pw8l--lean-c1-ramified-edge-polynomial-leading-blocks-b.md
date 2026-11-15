---
# qou-pw8l
title: 'Lean: C1 ramified edge polynomial + leading blocks B = ±sqrt(q-1)/q'
status: completed
type: task
priority: high
created_at: 2026-08-07T08:44:24Z
updated_at: 2026-08-07T09:11:28Z
---

Formalise the two results of agent 4656 that SURVIVED (both algebraic, which is why they held while the numerical readings failed):

1. Newton polygon of L1 = (q^2 x - 1) s^2 - (q-1) s - (q-1) at infinity.
   Points (i, -deg a_i) = (0,0), (1,0), (2,-1). Lower hull drops (1,0)
   (it sits at 0 > -1/2 on the segment), leaving the single edge
   (0,0)-(2,-1) of slope -1/2. NON-INTEGRAL => companion nilpotent at
   infinity => no leading block readable unramified.

2. Ramify with index 2 (x = z^2, q = p^2). Hull becomes (0,0),(2,-2),
   slope -1, INTEGRAL. Edge polynomial p^4 T^2 - p^2 + 1, whose roots
   are the two leading blocks B_1,2 = ±sqrt(p^2-1)/p^2 = ±sqrt(q-1)/q.

Lean-provable targets (all sorry-free, generic base ring where possible):
   - edge-poly root characterisation (field with sqrt(q-1))
   - B_1 + B_2 = 0, B_1 * B_2 = -(q-1)/q^2
   - sectors distinct <=> q != 1
   - the hull/slope combinatorics as an explicit finite check

SCOPE: this is the leading EXPONENTIAL data indexing the two Stokes
sectors. It is NOT the Stokes multipliers. Do not overclaim.

Witness: computations/qbeta/c3-w2-c1-ramification-leading-blocks.witness.json
