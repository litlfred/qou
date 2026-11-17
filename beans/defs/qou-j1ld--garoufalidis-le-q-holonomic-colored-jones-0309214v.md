---
# qou-j1ld
title: 'Garoufalidis-Le q-holonomic colored Jones (0309214v3): C_{K,n} linear q-recursion for odd-channel Habiro element'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-18T22:17:25Z
updated_at: 2026-10-04T15:20:36Z
parent: c7vs
---


## Fresh-look gap-feed (2026-07-19, see qou-do3a)
Garoufalidis–Lê q-holonomicity GUARANTEES the (Borromean) colored Jones has a FINITE-depth linear q-difference recursion. Order is 2 for 4₁ (corpus-confirmed AJFigureEight.lean), 3 for 5₂. Feeds GAP-3 R(q,x) kernel (qou-6poy) + Borromean AJ (n920/moqg): fixes the binding-genfun-qdifference conjectural kernel depth from structure, not fit.

## Round 72 Progress (`litlfred/qou#8252`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/FigureEightAPolyPeriodAndTakataHolonomicBrick.lean` (`garoufalidis_le_q_holonomic_second_order_step_elimination`)
- **Summary**: Proved two-step state elimination `a0 * c3 = (a0 * a1 + b1) * c2 - b1 * b0 * c0` in a second-order Garoufalidis-Le linear `q`-holonomic recurrence.
- **80-dps Probe & Witness**: `computations/probes/figure_eight_a_poly_period_and_takata_holonomic_brick_probe.py` -> `computations/probes/figure-eight-a-poly-period-and-takata-holonomic-brick.witness.json` (`scriptCommitSha: 5c4e30462ed53f77f251c4ddf47409b4459308ef`, PR head `f6277d470f462db4f8fd3f013f12ae4b9781d94b`)
- **PR**: https://github.com/litlfred/qou/pull/8252 (`status: in-progress` pending merge)
