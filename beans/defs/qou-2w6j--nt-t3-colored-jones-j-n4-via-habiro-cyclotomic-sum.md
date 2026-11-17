---
# qou-2w6j
title: 'NT-T3: colored Jones J_N(4₁) via Habiro cyclotomic sum in Lean + prove its order-2 inhomogeneous recurrence (q-WZ certificate identity, pure algebra)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T03:21:57Z
updated_at: 2026-10-04T15:21:44Z
parent: c7vs
---

## Round 73 Progress (`litlfred/qou#8257`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/HabiroCyclotomicRecurrenceAndHopfCSBrick.lean` (`habiro_cyclotomic_one_step_inhomogeneous_recurrence`)
- **Summary**: Proved order-2 inhomogeneous recurrence certificate `J^{(1)}(u_{N+1}, c1) - t * J^{(1)}(u_N, c1) + J^{(1)}(u_{N-1}, c1) = (2 - t) * (1 + 2 * c1)` under the Chebyshev step `u_{N+1} + u_{N-1} = t * u_N`.
- **80-dps Probe & Witness**: `computations/probes/habiro_cyclotomic_recurrence_and_hopf_cs_brick_probe.py` -> `computations/probes/habiro-cyclotomic-recurrence-and-hopf-cs-brick.witness.json` (`scriptCommitSha: aee44290d86add18624df3d3bce0a730246dc422`, PR head `eb8e68feba9367aa951532accb9ea1ab3a723c3a`)
- **PR**: https://github.com/litlfred/qou/pulls (`status: in-progress` pending merge)
