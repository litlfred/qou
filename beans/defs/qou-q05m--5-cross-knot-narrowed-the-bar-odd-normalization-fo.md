---
# qou-q05m
title: 5₂ cross-knot narrowed the bar-odd normalization fork (qou-yh67/qou-pzzl) to 'which ι-odd combination of {3,4}'
status: todo
type: task
created_at: 2026-08-02T09:38:29Z
updated_at: 2026-08-02T09:38:29Z
---

**PR #4567 finding.** 5₂ (chiral, 3×3 Stokes block) splits the DT spectrum
{3,4} across chirality — S⁺(0) carries 4 (the (96) constant), S⁻(0) carries 3
(the (97) constant); amphichiral 4₁'s 2×2 carries only the single 3. The
single-scalar A_ω=3 reading of the bar-odd normalization is **REFUTED**
[scope-(a), structural]. The bar-odd observable is ι-odd
(`BarOddAntisymOffDiagonal.omega_iota_odd`) and vanishes at 4₁, so the ι-even
scalar sum cannot carry it.

**OPEN:** which ι-odd combination of {3,4} the observable inherits (member 4,
member 3, difference 1, or a combination). **Constraint:** must be ι-odd
(difference-type), never the ι-even sum.

Files: `content/quantum-observable-universe/lean/QOU/QBeta/FiveTwoDTSpectrumSplit.lean`,
`computations/probes/fivetwo_crossknot_34_distinguisher.py`,
`docs/audits/2026-08-02-fivetwo-crossknot-34-resolution.md`.
Parent forks: qou-yh67, qou-pzzl. Sibling keystones: #4554, #4553.
