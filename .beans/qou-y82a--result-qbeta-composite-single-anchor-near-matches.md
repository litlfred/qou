---
# qou-y82a
title: 'RESULT: qbeta composite single_anchor_near_matches collapses 25 -> 4 from muon to proton'
status: todo
type: task
priority: normal
created_at: 2026-08-24T17:35:38Z
updated_at: 2026-08-24T17:36:23Z
---

## The number

`qbeta_composite_crossanchor_2factor_sweep`, re-run at the proton anchor:

    data.single_anchor_near_matches:  25  ->  4

Nothing else in the witness changes shape. The whole 39% payload delta is that
one list.

## Why it is worth its own bean

It is a statement about the q_beta composite search, not about the migration:
**most of the single-anchor near-matches were artifacts of the muon pin.** A
near-match that survives one anchor and not the other is evidence about the
candidate, and 21 of 25 did not survive.

## It is NOT a truncation, and the guard says otherwise

`witness_shape_guard.py` flags it: "payload collapsed: 161 -> 98 leaves (39%
gone, tolerance 30%) ... almost certainly a partial write (the producer writes
incrementally and was interrupted)."

That heuristic is wrong here. Measured: a completed, uninterrupted 900 s run
(rc=0, no timeout) reproduces 98 leaves exactly. The guard is right to be
suspicious of a shrinking payload in general -- it exists because a gutted
witness scores zero raw floats and reads as a perfect drain (qou-h4xk) -- but a
real anchor-dependent result set can shrink legitimately.

The witness was left UNCOMMITTED in PR #5664 rather than committed with the
gate red or the guard widened. Whoever picks this up should decide whether the
25 -> 4 collapse is a result to report, and only then how the guard should
learn about it. Do not widen the tolerance to make this green.
