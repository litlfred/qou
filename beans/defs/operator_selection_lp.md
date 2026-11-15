---
# operator_selection_lp
title: operator selection lp missing hypotheses
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-10-04T15:26:48Z
parent: qou-uot9
---

File: `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/operator_selection_lp.lean`
The `operator_selection_lp` theorem is unprovable. `OperatorSelectionLpContext` provides `x_star` and `y_0_star` as unconstrained data fields, meaning it does not assume they actually satisfy the optimality conditions or strong duality, making the theorem refutable.



Also known as `opsl` (its former front-matter header id; the beans CLI uses the filename id `operator_selection_lp`). Recorded 2026-10-04.
