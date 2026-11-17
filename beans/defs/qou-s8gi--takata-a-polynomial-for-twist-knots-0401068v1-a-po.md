---
# qou-s8gi
title: 'Takata A-polynomial for twist knots (0401068v1): A-poly from Masbaum recurrences — bridge to geometric rho_inf face'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-18T22:17:25Z
updated_at: 2026-10-04T15:24:49Z
parent: c7vs
---


## Fresh-look gap-feed (2026-07-19, see qou-do3a)
Takata gives the EXPLICIT twist-knot recursion → A-polynomial (5₂ order-3, 6₁ order-4) via qMultisum on Masbaum's summand. Template for deriving the binding kernel R(q,x) depth (qou-6poy) and the q_0←A-polynomial Subgoal-2 geometric route. The 2→3 order jump = the bar-odd (chiral) locus.

## Round 72 Progress (`litlfred/qou#8252`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/FigureEightAPolyPeriodAndTakataHolonomicBrick.lean` (`takata_twist_knot_recurrence_order_jump_and_chiral_defect`)
- **Summary**: Proved Takata twist-knot recurrence order jump `r(1) = 2 -> r(2) = 3`, unit step `r(p + 1) - r(p) = 1`, and cubic chiral reciprocity defect factorization `(c2 - c1) * L * (L - 1) != 0`.
- **80-dps Probe & Witness**: `computations/probes/figure_eight_a_poly_period_and_takata_holonomic_brick_probe.py` -> `computations/probes/figure-eight-a-poly-period-and-takata-holonomic-brick.witness.json` (`scriptCommitSha: 5c4e30462ed53f77f251c4ddf47409b4459308ef`, PR head `f6277d470f462db4f8fd3f013f12ae4b9781d94b`)
- **PR**: https://github.com/litlfred/qou/pull/8252 (`status: in-progress` pending merge)
