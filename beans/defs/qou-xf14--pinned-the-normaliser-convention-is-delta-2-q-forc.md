---
# qou-xf14
title: 'PINNED: the normaliser convention is delta = [2]_q, forced by the identity sqrt(b_pp.b_nn) = 1/[2]_q at every q — qou-59j5/qou-78pt family span 1.33x collapses to one member'
status: in-progress
pr: 8197
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T05:47:43Z
updated_at: 2026-11-16T20:55:10Z
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

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Progress Update (PR #8197 — `status: in-progress`)

- [x] Formalized pure Lean 4 module(s) (`QOU/MassTheory/BorromeanShadowCycleMerge.lean`, `QOU/MassTheory/SecondOrderContentCancellation.lean`, `QOU/Hecke/DeltaLongEMinusOrderingSplit.lean`, `QOU/MassTheory/LoopValueNormaliserAndFrameDiff.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` + exact rational probe `computations/probes/borromean_shadow_c2_deltal_loop_frame_probe.py` and 2-commit stamped witness `computations/probes/borromean-shadow-c2-deltal-loop-frame-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8197](https://github.com/litlfred/qou/pull/8197) (`ready: 4a2ed9a21b68b7d23b2e693b68f472d7dcf102a6`).
