---
# qou-6a2z
title: 'base-ring-audit post-merge findings: 5 new files add Field on the algebraic side'
status: todo
type: task
created_at: 2026-11-27T19:42:33Z
updated_at: 2026-11-27T19:42:33Z
parent: qou-dk7p
---

First post-merge run of scripts/base-ring-audit.py --check (main after #9613, 2026-11-27) reports NEW field markers in 5 files merged after the check landed:
- CompactQuantumMetrics/OqSU2HaarState.lean: field-class 1, field_simp 6
- QCalculus/HabiroCyclotomicSeries.lean: field-class 1
- QOU/Core/KashaevHabiroBridge.lean: field-class 1
- QOU/Nuclear/NucleonDownStrandSelfEnergy.lean: field-class 1, field_simp 1
- QOU/Nuclear/NucleonSplitFullTower.lean: field-class 1, field_simp 1
An automatic Field->CommRing swap compiles on none of them (2 could not be baseline-compiled here: missing oleans for new deps). Each needs a hand restatement over Rˣ / clearing denominators, or a recorded reason it needs a field. Not absorbed into the baseline on purpose.
