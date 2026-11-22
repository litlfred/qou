---
# qou-ey25
title: nsi q deformed kernel missing hypotheses
status: in-progress
pr: 8218
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-22T21:55:07Z
parent: qou-uot9
---

File: `folio/quantum-observable-universe/lean/QOU/BraidsKnots/nsi_q_deformed_kernel.lean`
The `nsi_q_deformed_kernel` theorem is unprovable. Its class lacks constraints on the data fields and has `*_unconstrained_false` lemmas proving that the conclusion is independent and refutable from the provided data alone.



Also known as `nqdk` (its former front-matter header id; the beans CLI uses the filename id `nsi_q_deformed_kernel`). Recorded 2026-10-04.


## Progress (Round 52 — PR #8218)
- Resolved in PR `litlfred/qou#8218` (`claude/round52-devacuify-6qbv-uot9`, HEAD `31f749976663905d17c11fe898c73116da2e8d1b`) with 80-dps mpmath witness `computations/probes/round52-devacuify-6qbv-uot9.witness.json` (`scriptCommitSha = 5355a18ce7a60c5cabb79019663bff82e103d505`).

## 2026-11-22 — id renamed `nsi_q_deformed_kernel` → `qou-ey25` (bean-hygiene, owner-approved)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. The old id contained underscores, which the tracker's id pattern `[A-Za-z0-9-]+` rejects, so `scripts/check-beans.sh` reported this file as having no id and every `beans` query missed it. Renamed on the owner's approval of qou-w3yy (project-chat card, 2026-11-22 21:53Z). Content unchanged; the old id stays greppable here.
