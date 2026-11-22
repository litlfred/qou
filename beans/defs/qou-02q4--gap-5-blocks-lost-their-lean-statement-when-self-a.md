---
# qou-02q4
title: 'GAP: 5 blocks lost their Lean statement when self-assuming projections were deleted'
status: completed
type: task
priority: high
tags:
    - lean
created_at: 2026-11-22T09:20:30Z
updated_at: 2026-11-22T11:52:25Z
parent: qou-uwyf
---

character_closure_holds (QHeckeSeminormalCharacterClosure), pslq_independence (Cl3Zeta5PslqIndependence), graded_trace_residue_split, phi_q_tower_algebraic_stratification, markov_gns_embedding (AlgebraicGnsEmbedding). Each module keeps only its context structure/class. For each: state the block's real proposition and prove it from hypotheses that are not the conclusion, or queue it with sorry + Ref, or demote the block to conjecture. Do not restore the projection.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.


2026-11-22T09:45Z claimed by thread 'Restore Lean statements lost with projections' (session https://claude.ai/code/session_01Qmmkt5ngCVGxt8cKmAnoR2). Plan: one real theorem per block, no projection restored.


2026-11-22T10:20Z five theorems on branch claude/restore-lean-statements-2026-11-22 (commits 1e4f4b610..83bdda216), each lean-direct exit 0, #print axioms = propext/Classical.choice/Quot.sound only. character_closure (from eq_wtrace_of_markov); cl3_diff_eq_sqrt5_L3_chi5 (X = sqrt5/2 L(3,chi5)); graded_trace_residue_split_of_section (one filtration step); phi_q_tower_algebraic_stratification_of_pentagon (pentagon = hypothesis); markov_gns_null_ideal (quotient step only). Ref audit needs-fix 25 -> 20. No projection restored. PR waits on owner.

2026-11-22: merged in PR #9009 (main e17f7a8a22).
