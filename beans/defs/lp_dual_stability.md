---
# lp_dual_stability
title: lp dual stability missing hypotheses
status: completed
pr: 8218
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-22T21:31:33Z
parent: qou-uot9
---

File: `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/lp_dual_stability.lean`
The `lp_dual_stability` theorem is unprovable. The context class `LpDualStabilityContext` only provides LP data (like the Gram matrix, shadow prices, etc.) without assuming that `x_star` is actually the LP optimum or any properties of `G`, making the stability conclusions refutable.



Also known as `lpds` (its former front-matter header id; the beans CLI uses the filename id `lp_dual_stability`). Recorded 2026-10-04.


## Progress (Round 52 — PR #8218)
- Resolved in PR `litlfred/qou#8218` (`claude/round52-devacuify-6qbv-uot9`, HEAD `31f749976663905d17c11fe898c73116da2e8d1b`) with 80-dps mpmath witness `computations/probes/round52-devacuify-6qbv-uot9.witness.json` (`scriptCommitSha = 5355a18ce7a60c5cabb79019663bff82e103d505`).

## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.

`QOU/ParticleInteractions/lp_dual_stability.lean:119` is derived sorry-free: claims (1) and (4) from feasibility and the in-repo duality lemma (docstring line 114). PR #8218 is superseded.

## 2026-11-22 — applicability review (owner instruction 2026-11-22, retroactive)
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF. Checked against docs/coordination/owner-rulings.md on origin/main.

Verdict: ALREADY-DONE for claims (1) and (4), which are derived. Claims (2) and (3) concern the specific 6×6 Gram matrix at q₀ and stay unproved (lean docstring lines 39, 116). That matrix must be convention D at the proton pin to be current; this was not re-verified here, and it sits in the convention lane (qou-cdx1/cds1).
