---
# qou-q05m
title: 5₂ cross-knot narrowed the bar-odd normalization fork (qou-yh67/qou-pzzl) to 'which ι-odd combination of {3,4}'
status: in-progress
pr: 8236
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:38:29Z
updated_at: 2026-11-17T06:55:00Z
parent: qou-avtq
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

Files: `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoDTSpectrumSplit.lean`,
`computations/probes/fivetwo_crossknot_34_distinguisher.py`,
`docs/audits/2026-08-02-fivetwo-crossknot-34-resolution.md`.
Parent forks: qou-yh67, qou-pzzl. Sibling keystones: #4554, #4553.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** The refutation of the single-scalar A_ω = 3 reading is structural and stands. Which ι-odd combination the observable inherits is still undecided; qou-rtm0's grading gives the odd component 1 but does not identify the observable with it.

Evidence: `QOU/QBeta/FiveTwoDTSpectrumSplit.lean`: no sorry/axiom (decide-proofs). `qou-rtm0` (completed) added the bar-eigenspace grading (dtPair52_grading = (7,1)). Witness `probes/fivetwo-crossknot-34-distinguisher.witness.json`: fractions-exact, `allPassed: True`. Parent `qou-pzzl` is scrapped; `qou-yh67` is todo.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-11-17 — Round 52 formalization & probe witness (PR #8236, status: in-progress)

- [x] PR #8236 (`62b8fce5d1e824cf9dd59a1d9845d15631382086`): formalized `linear_functional_iota_odd_on_52_iff`, `linear_functional_iota_odd_properties`, and `iota_even_sum_multiple_never_iota_odd` in `QOU/QBeta/StokesDiagonalVsOffDiagonalAndCrossKnotSplit.lean` (`0 sorry`, `0 axiom`, `0 vacuity`), classifying all integer linear iota-odd functionals (`alpha + beta = 0`).
- [ ] Awaiting Merge Manager integration and owner review (kept `in-progress` per no-unilateral-closure policy).
