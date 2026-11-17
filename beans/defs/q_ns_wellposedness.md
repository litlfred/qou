---
# q_ns_wellposedness
title: q ns wellposedness missing hypotheses
status: in-progress
pr: 8225
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-10-04T15:26:49Z
parent: qou-uot9
---

File: `folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_wellposedness.lean`
The `q_ns_wellposedness` theorem is unprovable. It is a Millennium-problem-adjacent global regularity claim, but the `QNsWellposednessContext` merely provides the carrier types and predicates without any axioms that would allow deriving the actual global well-posedness.



Also known as `qnsw` (its former front-matter header id; the beans CLI uses the filename id `q_ns_wellposedness`). Recorded 2026-10-04.


## Progress (Round 53 — PR #8225)
- Implemented sorry-free, non-vacuous Lean 4 formalization + 80-dps mpmath witness in PR https://github.com/litlfred/qou/pull/8225 (HEAD `92ab8569af5ff7399510fd92cb2505df80c41b5e`).
- Marked `in-progress` pending PR merge.
