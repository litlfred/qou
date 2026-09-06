---
# qou-yaig
title: 'Take over qou-pdg9''s open orders: settle c2(4He) and c3 under Borromean'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T13:34:53Z
updated_at: 2026-09-06T13:40:32Z
---

## What this takes over, and from whom

PR #6931 (merged `fb13d307c7`) refuted the CENTRAL FINDING of #6559 — that the
ratio `c2.h^2 / c1.h` is monotone through 1 across `A` — and deliberately left
two things unsettled, both flagged as `qou-pdg9`'s call on their probe rather
than done unilaterally:

1. **`c2(4He)`** — the committed `P_OF["4He"] = 3`. One series order is lost to
   the 0/0 seminormal quotients, so `d.p = 2` and `d.coeff(2)` is unavailable.
   Every other case already has its `c2`. Without this one number, #6559's
   surviving claim *"the expansion crosses over between A = 3 and A = 4"* is
   **untested, not disproved**.
2. **`c3`** — not re-measured at all under Borromean, so #6607 is
   grouped-CONDITIONAL rather than refuted.

Owner instruction 2026-09-06 13:2x: *"Take over derivation and keep going."*

## Measured before running anything: `c2` has NO closed form

`c1` HAS one — `(a.Z + b.N)(2^-(A+1) - 2^-2A) - 4(i_pp - i_nn)2^-2A` — which is
how `c1(4He) = 7/128` was PREDICTED and then confirmed twice over (#6931). The
obvious move was to predict `c2(4He)` the same way. **It does not work, and this
was established rather than assumed.**

Exhaustive search over subsets of a 15-function basis
(`Z.D, N.D, dI.E, D, E, Z.E, N.E, A.E, A.D, ZZ.D, NN.D, ZN.D, ZZ.E, NN.E, ZN.E`),
requiring an exact fit to **all six** grouped values AND **all five** known
Borromean values: **ZERO subsets up to size 5.**

The quadratic terms were in the basis on purpose, not as padding. `tr_M`
factorises across the two nucleons (disjoint strand sets, #6919), which makes
the **log**-derivative additive at first order — so second order was expected to
carry a `phi_p.phi_n` cross term. **It does not fit either.** So `c1`'s
per-letter additivity is special to first order, there is nothing to predict
from, and the number has to be computed.

That negative is worth as much as the measurement it justifies: it says the
closed form does NOT propagate up the h_q expansion.

## Scope

Scope-(a) throughout: a statement about a series ordering in one braid-word
convention, not about the physics. And note that no value of `c2(4He)` restores
#6559's ARGUMENT — the Borromean column is `0.8174, 1.2385, INFINITE, 4.9045,
0.9722`, neither monotone nor ordered by `A`. Only its `A = 4` CONCLUSION is in
question here.

## Route for `c3`, once `c2` lands

Same producer, one order further: `c3` needs `a3`, hence `d.p > 3`. The five
small cases already sit at committed `P` values that reach it (`pp/pn/nn` at
`P = 6`, `T/3He` at `P = 5`); only `4He` would need `P = 5`, which is the
expensive one. So `c3` at `A = 2, 3` is cheap and `c3` at `A = 4` is not.


## MEASURED 2026-09-06 — item 1 settled, and the answer SPLITS

    c2(4He) borromean = 439/512      a0 = 7/128   a1 = 7/128   a2 = 411/512
    ratio c2.h^2 / c1.h = 1.5535     (295 s at P = 4, d.p = 3)

**The endpoint SURVIVES; the location does NOT.** #6559 said the expansion
"crosses over BETWEEN A = 3 and A = 4", which asserts two things:

- **ratio > 1 at A = 4** — TRUE, 1.5535, and by MORE than under grouped (1.4639).
- **ratio < 1 below** — FALSE. Under Borromean it is already 4.9045 at `T`
  (A = 3) and 1.2385 at `pn` (A = 2). There is no crossing THERE.

So the conclusion is right at its endpoint and wrong about where the crossing
happens, and the argument stays refuted (#6931). The full Borromean column:

    pp 0.8174   pn 1.2385   nn INFINITE   T 4.9045   3He 0.9722   4He 1.5535

**I caught my own over-claim in the probe's own output.** Its first verdict
printed "#6559's crossover CLAIM survives" — too generous, since it decides only
one of the two conjuncts. Fixed in the probe before the result was written up
anywhere else.

## The controls matter as much as the number

Three passed before the new value was trusted: `a0 = 7/128` against the derived
floor two ways, and `a1 = 7/128` against the `c1(4He)` measured in #6931.

That second one is worth naming: **#6931's own probe could only assert
`c1(4He) = 7/128` circularly** — it was the closed-form prediction fed back in as
its own target, and the PR body said so. This run reaches it by an independent
route (exact series at P = 4, no closed form involved) and gets the same value.
The circular row is now closed.

Also noted, unexplained: `a0 = a1 = 7/128` exactly at 4He under Borromean — the
classical floor and the leading coefficient coincide. Not claimed as meaningful.

## Item 2 (`c3`) — still open, and now better scoped

Same producer, one order further: `c3` needs `a3`, hence `d.p > 3`. The five
small cases already sit at committed `P` that reach it; only `4He` needs `P = 5`.
Given P = 4 cost 295 s and the per-order growth here is steep (the [8,4] and
[7,5] blocks alone were 50 s and 59 s at P = 4), P = 5 at n = 12 is the expensive
one and should be launched with the long-compute logging discipline.
