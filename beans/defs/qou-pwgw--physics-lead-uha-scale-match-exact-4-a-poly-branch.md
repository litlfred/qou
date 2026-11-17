---
# qou-pwgw
title: 'physics lead: |u|=HA scale-match, exact 4₁ A-poly branch tracking + phase'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T14:42:20Z
updated_at: 2026-10-04T15:22:04Z
parent: c7vs
---

## Round 73 Progress (`litlfred/qou#8257`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/HabiroCyclotomicRecurrenceAndHopfCSBrick.lean` (`figure_eight_branch_discriminant_and_norm_one_phase_lock`)
- **Summary**: Proved norm-one branch discriminant `(L1 - L2)^2 = b^2 - 4`, second power sum `L1^2 + L2^2 = b^2 - 2`, and strict negativity `b^2 - 4 < 0` in the elliptic scale-match window `b^2 < 4`.
- **80-dps Probe & Witness**: `computations/probes/habiro_cyclotomic_recurrence_and_hopf_cs_brick_probe.py` -> `computations/probes/habiro-cyclotomic-recurrence-and-hopf-cs-brick.witness.json` (`scriptCommitSha: aee44290d86add18624df3d3bce0a730246dc422`, PR head `eb8e68feba9367aa951532accb9ea1ab3a723c3a`)
- **PR**: https://github.com/litlfred/qou/pulls (`status: in-progress` pending merge)
