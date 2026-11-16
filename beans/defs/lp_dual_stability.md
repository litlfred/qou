---
# lp_dual_stability
title: lp dual stability missing hypotheses
status: in-progress
pr: 8218
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-10-04T15:26:45Z
parent: qou-uot9
---

File: `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/lp_dual_stability.lean`
The `lp_dual_stability` theorem is unprovable. The context class `LpDualStabilityContext` only provides LP data (like the Gram matrix, shadow prices, etc.) without assuming that `x_star` is actually the LP optimum or any properties of `G`, making the stability conclusions refutable.



Also known as `lpds` (its former front-matter header id; the beans CLI uses the filename id `lp_dual_stability`). Recorded 2026-10-04.


## Progress (Round 52 — PR #8218)
- Resolved in PR `litlfred/qou#8218` (`claude/round52-devacuify-6qbv-uot9`, HEAD `31f749976663905d17c11fe898c73116da2e8d1b`) with 80-dps mpmath witness `computations/probes/round52-devacuify-6qbv-uot9.witness.json` (`scriptCommitSha = 5355a18ce7a60c5cabb79019663bff82e103d505`).
