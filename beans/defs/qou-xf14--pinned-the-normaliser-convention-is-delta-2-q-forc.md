---
# qou-xf14
title: 'PINNED: the normaliser convention is delta = [2]_q, forced by the identity sqrt(b_pp.b_nn) = 1/[2]_q at every q — qou-59j5/qou-78pt family span 1.33x collapses to one member'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T05:47:43Z
updated_at: 2026-10-04T15:13:29Z
parent: qou-v2om
---

`computations/qbeta/qbeta_loop_value_pinned_probe.py` (8/8), symbolic in `q`.

## The identity

Two of the three interface letters are PURE crossings — `b_pp` is `sigma`,
`b_nn` is `sigma^-1`. Their product collapses:

    b_pp . b_nn = q^3/(q^2+1) . 1/(q^3+q) = q^2/(q^2+1)^2 = 1/[2]_q^2

so the geometric mean of the two pure-crossing bonds is **exactly the inverse
loop value**, and each bond is a `q^(+/-2)` twist of it:

    sqrt(b_pp.b_nn) = 1/[2]_q      b_pp = q^2/[2]_q      b_nn = q^-2/[2]_q

Hence the additive law's per-strand coefficient is exactly `ln [2]_q`.

## Why it is a pinning, not a choice

It holds **identically in `q`**, and among `qou-59j5`'s five-member family only
`[2]_q` satisfies it — the others agree only at `q = 1`, the classical point
where every factor in this arc collapses to `z = 1/2` anyway. A fit would land at
`q0` and nowhere else.

Corroboration: `1/[2]_q = 0.4972905456...` is exactly the `1/delta =
0.497290545` bean `qou-98g5` records the corpus already carrying.

## What it closes

`qou-59j5` measured the family span at **1.33x** and observed that this is the
same size as the deficit it would explain, "which is exactly the condition that
makes choosing a member a fit"; `qou-78pt` reverted to "unfalsifiable as written"
on that basis, with the verdict *"pinning the convention from the axioms is the
actual work"*. The probe reproduces the span (1.32964x) and then collapses it to
one member. **After this a residual is a residual, not a convention choice.**

## The honest caveat, stated because it cuts against the argument

`[2]_q` is ALSO the closest-landing member — `3.E_0.ln[2]_q = 8.77274`
MeV/nucleon vs the measured peak `B/A = 8.79456` (0.25 %), next best Kauffman at
0.83 %. Two independent facts, and the coincidence means the ENERGY comparison
has little discriminating power here. The pinning does not rest on it: the
identity is symbolic and mentions no energy, no anchor and no measured binding
value.

## What it does NOT close

`E_0` is still CAL-1 — a calibration, not a derivation — so the absolute scale is
still unpinned. And the factor-of-3 gap stands: the colour tube that would supply
it is unrealisable in this construction family (`qou-0c19`,
`QOU/Hecke/LayoutConflict.lean`).

Also worth recording: `b_pn` is NOT of this form (`b_pn . [2]_q = 1.021998`, not
a power of `q0`) — as expected, since it is a weight-1 average of the two
crossings rather than a crossing. The identity is about the two PURE letters and
is stated that way.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
