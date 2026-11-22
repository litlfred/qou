---
# qou-67xn
title: markov identification missing hypotheses
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-22T21:55:07Z
parent: qou-jc9f
---

File: `folio/quantum-observable-universe/lean/QOU/FeynmanPathIntegrals/markov_identification.lean`
The `markovTrace_branching` theorem is unprovable. It posits an equality between opaque constants `markovTrace` and `sum (markovWeight * spechtPartialTrace)` without any axiomatic branching / Wenzl-bridge decomposition rules that would make it derivable.



Also known as `mrid` (its former front-matter header id; the beans CLI uses the filename id `markov_identification`). Recorded 2026-10-04.

## Round 91 Lean 4 + 80-dps Witness Formalization (PR #8487)
- Module: `QOU.Foundations.SeminormalInversionDescentBranchingBridgeHypothesisLinkStabilisationConjugationFourComponentOperFiltrationJointPeriodBraidSplit`
- Commit 1 (code + probe): `ac300d2c8e5f49854ec28ab33d09e033225201c1`
- Commit 2 (`.witness.json`): `e92637de21c829df89a2f80bfc1da64dc805a438`
- PR: https://github.com/litlfred/qou/pull/8487

## 2026-11-22 — id renamed `markov_identification` → `qou-67xn` (bean-hygiene, owner-approved)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. The old id contained underscores, which the tracker's id pattern `[A-Za-z0-9-]+` rejects, so `scripts/check-beans.sh` reported this file as having no id and every `beans` query missed it. Renamed on the owner's approval of qou-w3yy (project-chat card, 2026-11-22 21:53Z). Content unchanged; the old id stays greppable here.
