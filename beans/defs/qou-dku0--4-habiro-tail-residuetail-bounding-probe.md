---
# qou-dku0
title: 4₁ Habiro-tail residue↔tail bounding probe
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-18T17:24:43Z
updated_at: 2026-10-04T15:16:05Z
parent: qou-n4nr
---

## Round 73 Progress (`litlfred/qou#8257`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/HabiroCyclotomicRecurrenceAndHopfCSBrick.lean` (`figure_eight_habiro_tail_geometric_majorant_identity`)
- **Summary**: Proved exact 3-term geometric telescoping identity `(1 - r) * (t0 + r * t0 + r^2 * t0) + r^3 * t0 = t0` and strict positivity `0 < r^3 * t0` of the cubic Habiro tail remainder for `0 < r` and `0 < t0`.
- **80-dps Probe & Witness**: `computations/probes/habiro_cyclotomic_recurrence_and_hopf_cs_brick_probe.py` -> `computations/probes/habiro-cyclotomic-recurrence-and-hopf-cs-brick.witness.json` (`scriptCommitSha: aee44290d86add18624df3d3bce0a730246dc422`, PR head `eb8e68feba9367aa951532accb9ea1ab3a723c3a`)
- **PR**: https://github.com/litlfred/qou/pulls (`status: in-progress` pending merge)
