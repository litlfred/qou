---
# qou-r1si
title: Scaffold Quantum Dilog
status: in-progress
pr: 8210
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-08T14:00:13Z
updated_at: 2026-10-04T15:24:19Z
parent: qou-r9ih
---

## Progress Note (2026-11-16, PR #8210)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/CompactQuantumDilogAndSaddleOffset.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 8 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/compact_quantum_dilog_and_saddle_offset_probe.py` and witness `computations/probes/compact-quantum-dilog-and-saddle-offset.witness.json` (`scriptCommitSha: 4755c87e9f5eee61dab667d125dbf7cba1a93d8b`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8210 (`539652a881d79d302fbe60283d4f961bd748a742`).
