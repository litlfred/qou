---
# qou-qt8b
title: 'Session: SDP analysis + substrate-phase recursion (light cone = γγ base case)'
status: todo
type: milestone
priority: normal
created_at: 2026-09-16T01:38:58Z
updated_at: 2026-09-16T02:01:58Z
---

Owner, 2026-09-16: 'Merge what's ready. Do SDP analysis. … the current value of the substrate phase is the evaluation of the entanglement history of all particles of the previous computational time step. So we're doing maybe the categorical trace of the common affine light cone of the two particles. That's what gets passed to the knot convolution and we use Frobenius for self-dual. And [with] no history the light cone is the γγ production.' Branch claude/sdp-analysis-light-cone-recursion-2026-09-16 from main 66f61c738a. Merges of #7430/#7429/#7432 dispatched to a merge-coordinator agent in parallel. Predecessor: qou-0nrt (q-stochastic tranche, PR #7432).


## 2026-09-16 — tranche state

Lean (qou-hlbx, derived half), measurement (qou-7dal, 10/10) and doc (qou-42jx) done; branch stacked on PR #7432 (rebase after the coordinator merges it). Owner decisions framed in the doc §8: O1 nothing; O2 rule reading 3's scope (bond/nucleon only vs composite vs deviation); O3 SubstratePhaseRecursion class with a chosen phaseOf; O4 composition feasibility program (needs the off-diagonal H_{3A} Gram / pyhecke_native); O5 γγ base-case selector. Recommendation: O2 then O4.
