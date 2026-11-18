---
# qou-dcvv
title: 'Entanglement history in the GS filtration: is the trace the only lossy step, or is the normal form lossy too?'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T20:01:42Z
updated_at: 2026-11-18T10:57:30Z
parent: 08a2
---

## 2026-09-16 — status cross-reference (session qou-0nrt; not my bean, appended only)

Q1 of jet_history_retention_probe.py is MEASURED: two histories reaching the same element have the same GS profile and different jet logs — the normal form is history-free, so the trace is NOT the only lossy step. Q2/Q4 are PROVED: QOU/Knot/JetGradePromotion.lean (fresh generator ⇒ whole profile +1, nothing splits; 4 theorems, sorry-free). Q3: negatives enter only via T_i^{-1} = T_i − A (inverse-crossing sector). What stays open is the partition-side carrier of the history: all three word-depth J^• are excluded (2026-08-16/26 audits) and any idempotent-graded filtration puts the unit at the top — abstract form proved this session as level_one_eq_top in QOU/MassTheory/BlockMeasureFromFrobeniusPairing.lean. Analysis: docs/audits/2026-09-16-q-stochastic-phase-space-shadow-prices-analysis.md §4. Status left todo.

- Round 81 (`lane-e667`): Formalized `rttg`, `qou-50vf`, `qou-aezg`, `qou-dcvv`, `qou-fwah` in `QOU.Foundations.FramedTangleSnakeCoherenceFourTermChordRelationSingularResolutionAlternationFiltrationProfileShiftCubePairBoundaryLift` with 80-dps `mpmath` 2-commit witness stamp (`202f38f5def66efc61fb7c2f38594348be909ef6` -> `8be6d39b672d7e4c20d56580366adaf778190be7`, `scriptHash=08594954abfff6ef5f50f03f78c3a5e07152d5280835430790282602d58a4a45`) in PR `litlfred/qou#8437` (`status: in-progress`).
