---
# qou-x10g
title: 'SW-5b: assemble range = top from connectivity and both-orientation matrix units'
status: todo
type: task
priority: normal
created_at: 2026-08-19T19:43:43Z
updated_at: 2026-08-19T19:44:36Z
parent: qou-59vq
blocking:
    - qou-jfr8
---

## Statement

`AlgHom.range (seminormalRep q hq0 hq2 n hN) = top` — SW-5 in the range form the
owner chose, and what SW-7 (`qou-0h5k`) consumes.

## Everything except one input is already on main

- `single_self_mem_range` — every DIAGONAL unit (via DiagonalSeparation + the
  simple spectrum). #5307.
- `single_mem_range_of_entry_ne_zero` — a nonzero (T',T) entry promotes to the
  off-diagonal unit. #5307.
- `eq_top_of_single_mem` — matrix units generate everything. #5307.
- `syt_swapStep_connected` — any two SYT of one shape are joined by admissible
  swaps. #5321.
- **blocked on** `qou-qyy0`: offDiag != 0 at admissible distances, which is what
  makes BOTH orientations of each edge usable.

## Assembly once qou-qyy0 lands

1. Per edge: `genMat_swap` gives entry `offDiag q (axialDist T k)` at
   `(swapTableau T k, T)`; nonzero by qou-qyy0 (admissible => |d| >= 2 by
   `swapAdmissible_of_sq_axialDist_ne_one`'s converse — CHECK that direction
   exists, only `d^2 != 1 -> SwapAdmissible` is proved so far).
2. `single_mem_range_of_entry_ne_zero` with `x = sigma_k` gives
   `single (swapTableau T k) T 1` in the range.
3. Induct along `Relation.ReflTransGen`, composing with
   `Matrix.single_mul_single_same`.
4. `eq_top_of_single_mem`.

## Watch item

Step 1 needs `SwapAdmissible T k -> (axialDist T k)^2 != 1`, the CONVERSE of what
`swapAdmissible_of_sq_axialDist_ne_one` proves. Do not assume it is symmetric:
admissibility is 'different row AND different column', and ruling out |d| = 1
from that needs the standard-tableau argument in the other direction. Budget for
it; it may already be somewhere in TableauCells under a different name — grep
before writing.
