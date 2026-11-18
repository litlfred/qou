---
# b3pe
title: qou/lean/Archimedean — track 3 intentional research-grade TODO markers (0 actionable sorries; §3b excluded) [re-scoped from 87]
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-10-04T15:23:05Z
parent: qou-5p7n
---

resweep 2026-06-22: honest counter = 4 actionable (claimed 87) via scripts/count-actionable-placeholders.ts.

resweep 2026-06-23 (#2637): honest actionable = 4 (claimed 87): SnapPyAxioms 2, EmCouplingBringZeroMode 1, BorromeanVolumeCatalan 1. See docs/audits/2026-06-23-placeholder-bean-resweep.md.

drain 2026-06-23 (#2651): actionable uncited-sorry 1 -> 0 — cited the BringZeroModeBlochClass conjecture instance in EmCouplingBringZeroMode.lean (§1+§3b; comment-only). Remaining 3 are intentional research-grade TODO markers (SnapPyAxioms 2 future-migration rows, BorromeanVolumeCatalan 1 open-questions §6) — left per the resweep guidance. b3pe is drained of actionable sorries.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 3 TODO/FIXME markers (claimed 87) in QOU/Archimedean, 0 sorries — the Archimedean sorries (HyperbolicVolumeIndependence, SingleVolumeIrrationality, BorelZagierQouVolumes, EmCouplingBringZeroMode) are §3b conjecture-INSTANCES, not missing proofs. Recommend re-scope to the 3 markers.



[2026-06-26 grep-inflated] Claimed 87; naive 49; refined actionable ~11 (subset are §3b instances, NOT to-resolve per AGENTS.md §3b). Re-scope excluding §3b. Audit: docs/audits/2026-06-26-lean-placeholder-bean-grep-inflation.md

[2026-06-26 RE-SCOPED — owner-authorized, rsseq-even-part session] Title now reflects the verified scope: 0 actionable sorries (the Archimedean sorries — HyperbolicVolumeIndependence, SingleVolumeIrrationality, BorelZagierQouVolumes, EmCouplingBringZeroMode — are §3b conjecture INSTANCES, not missing proofs); the only residual is 3 intentional research-grade `-- TODO` markers (SnapPyAxioms 2 future-migration rows, BorromeanVolumeCatalan open-questions §6). Kept open as a low-priority tracking bean, NOT a drainable count.

## Round 88 Formalization (`litlfred/qou#8471`)
- Formalized in `QOU.Foundations.BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit` (`folio/quantum-observable-universe/lean/QOU/Foundations/BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`e47fb91c9186e83c35ba5f8afe823fc02682f7fa` -> `eb5a105f27408ec654ee82cac266aca18e9361f3`, `scriptHash = scriptSha256 = 76b0a54b7612529d0460197f1a503d128d9ca3acb85f7c16e201490dd4b263d6`).
- PR: https://github.com/litlfred/qou/pull/8471
