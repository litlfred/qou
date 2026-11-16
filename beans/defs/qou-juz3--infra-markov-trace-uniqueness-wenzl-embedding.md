---
# qou-juz3
title: 'Infra: Markov trace uniqueness + Wenzl embedding'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-04T01:39:43Z
updated_at: 2026-11-16T19:27:00Z
parent: qou-rtxm
---

Blocks: prop_rigid_monoidal_structural_gap_invariance (1), markov_trace_recursive_reducer (1), delta_q_decoration (1). Need Jones Markov-trace uniqueness [jones1985] + Wenzl block decomposition [wenzl1988].

## 2026-11-16 — Markov Trace Uniqueness & Wenzl Block Weights (`QOU.Foundations.ConventionDFrobeniusMarkovTower`, PR #8166)
- Formalized `markovCosetEval`, `markov_trace_unique_on_coset_tower`, and `wenzl_two_block_weights_unique` in `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDFrobeniusMarkovTower.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `246ab0f17af473b433e680ddc0223712e5c0d13c` | PR: `https://github.com/litlfred/qou/pull/8166`
- Kept at `status: in-progress` per merge-manager protocol.
