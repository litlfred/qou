---
# qou-2c0w
title: q ns wellposedness missing hypotheses
status: in-progress
pr: 8225
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-27T15:30:00Z
parent: qou-uot9
---

File: `folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_wellposedness.lean`
The `q_ns_wellposedness` theorem is unprovable. It is a Millennium-problem-adjacent global regularity claim, but the `QNsWellposednessContext` merely provides the carrier types and predicates without any axioms that would allow deriving the actual global well-posedness.



Also known as `qnsw` (its former front-matter header id; the beans CLI uses the filename id `q_ns_wellposedness`). Recorded 2026-10-04.


## Progress (Round 53 — PR #8225)
- Implemented sorry-free, non-vacuous Lean 4 formalization + 80-dps mpmath witness in PR https://github.com/litlfred/qou/pull/8225 (HEAD `92ab8569af5ff7399510fd92cb2505df80c41b5e`).
- Marked `in-progress` pending PR merge.

## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.

Not closed. The Lean is now honest §3b-cond (`QOU/FluidDynamics/q_ns_wellposedness.lean`, Disposition line 22): existence and smoothness are assumed as class inputs, energy and decay are proved. The assumed part is an open problem, so per the no-close-on-open-conjecture rule this stays open.

## 2026-11-22 — id renamed `q_ns_wellposedness` → `qou-2c0w` (bean-hygiene, owner-approved)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. The old id contained underscores, which the tracker's id pattern `[A-Za-z0-9-]+` rejects, so `scripts/check-beans.sh` reported this file as having no id and every `beans` query missed it. Renamed on the owner's approval of qou-w3yy (project-chat card, 2026-11-22 21:53Z). Content unchanged; the old id stays greppable here.

## 2026-11-27: PR #8225 closed unmerged (stale reference)

PR #8225 was closed unmerged on 2026-11-22 as superseded, on the owner's decision. The front-matter `pr: 8225` and the "pending PR merge" line in the Round 53 block are stale. The honest §3b-cond state recorded in the 2026-11-22 section above is what is on main. Status unchanged (open conjecture).
