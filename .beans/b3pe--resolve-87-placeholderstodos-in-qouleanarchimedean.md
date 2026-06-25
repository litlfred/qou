---
# b3pe
title: Resolve 87 placeholders/TODOs in qou/lean/Archimedean
status: todo
type: task
priority: normal
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-06-25T17:05:00Z
---

resweep 2026-06-22: honest counter = 4 actionable (claimed 87) via scripts/count-actionable-placeholders.ts.

resweep 2026-06-23 (#2637): honest actionable = 4 (claimed 87): SnapPyAxioms 2, EmCouplingBringZeroMode 1, BorromeanVolumeCatalan 1. See docs/audits/2026-06-23-placeholder-bean-resweep.md.

drain 2026-06-23 (#2651): actionable uncited-sorry 1 -> 0 — cited the BringZeroModeBlochClass conjecture instance in EmCouplingBringZeroMode.lean (§1+§3b; comment-only). Remaining 3 are intentional research-grade TODO markers (SnapPyAxioms 2 future-migration rows, BorromeanVolumeCatalan 1 open-questions §6) — left per the resweep guidance. b3pe is drained of actionable sorries.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 3 TODO/FIXME markers (claimed 87) in QOU/Archimedean, 0 sorries — the Archimedean sorries (HyperbolicVolumeIndependence, SingleVolumeIrrationality, BorelZagierQouVolumes, EmCouplingBringZeroMode) are §3b conjecture-INSTANCES, not missing proofs. Recommend re-scope to the 3 markers.
