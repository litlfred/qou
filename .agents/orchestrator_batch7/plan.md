# Plan — Lean Sorry Stub Proof Migration Project (Batch 7)

## Objectives
1. Retrieve the list of 10 target files from `PROJECT.md`.
2. Spawn 10 worker subagents (up to 10 concurrently) to handle the stubs.
3. Keep stubs containing open conjectures intact as permanent `sorry` exceptions per `AGENTS.md` §3b-cond.
4. Replace non-conjectural stubs with valid Lean proofs based on context fields.
5. For files using `ℝ`, `ℕ`, or `| |`, ensure `import Mathlib` is placed at the top.
6. Verify proofs compile via `scripts/lean-verify.sh`.
7. Commit all work to the branch `claude/prove-stubs-batch7-2026-06-23` and push it.
8. Report victory.

## Milestones and Assignments
| # | File Path | Type | Strategy | Worker Conv ID | Status |
|---|---|---|---|---|---|
| 1 | `Archimedean/HyperbolicVolumeIndependence.lean` | Conjectural | Keep `sorry` / Import Mathlib | 989c5471-8e88-42e5-9fff-f34d6abf6e33 | In Progress |
| 2 | `Archimedean/EmCouplingBringZeroMode.lean` | Conjectural | Keep `sorry` | 030fe65d-e461-40a1-94e8-597ccb2ed08c | In Progress |
| 3 | `Archimedean/skein_polynomial_transfer_matrix.lean` | Proof | Context projection | 7c1b781c-370a-464b-8b68-95b80677eeb6 | In Progress |
| 4 | `Archimedean/em_coupling_projection.lean` | Proof | Context projection | 43a2f3ff-c070-4b4b-8184-99c9d12f5253 | In Progress |
| 5 | `Archimedean/parity_violation_skein.lean` | Proof | Context projection | bd296361-2187-437a-8a61-753c36f06e00 | In Progress |
| 6 | `Archimedean/skew_poisson_integration.lean` | Proof | Context projection | b82a166e-228e-4b62-b37f-9d1a1df7030b | In Progress |
| 7 | `Archimedean/reidemeister_action_table.lean` | Proof | Context projection | d6bf49ba-245a-4b34-aaa0-e8e8aa15ad73 | In Progress |
| 8 | `QuantumBloch/pentagon_uv_commutation.lean` | Proof | Context projection / Fix syntax | 169f9b6b-8b9c-4d65-ac8e-c6b5dddcb5cf | In Progress |
| 9 | `ParticleInteractions/tritium_qvalue_symbolic.lean` | Proof | `rw [ctx.h_Q, ← ctx.h_closed_form]` / Import Mathlib | 289e7d77-8fbd-4ef4-a45c-1ed78db035db | In Progress |
| 10 | `ParticleInteractions/demand_stability.lean` | Proof | Context projection / Import Mathlib | 301fba8f-5267-4ec6-9af6-bfd38cc5ec3f | In Progress |
