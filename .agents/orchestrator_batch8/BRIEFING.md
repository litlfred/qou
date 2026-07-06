# BRIEFING — 2026-06-24T00:20:00-04:00

## Mission
Prove the 10 target Lean files in Batch 8, verify them, and commit to branch.

## 🔒 My Identity
- Archetype: Project Orchestrator
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /Users/litlfred/space_cats/qou/.agents/orchestrator_batch8/
- Original parent: parent
- Original parent conversation ID: 6d37ee5b-d998-4962-b4ad-e8849799d11e

## 🔒 My Workflow
- **Pattern**: Project Pattern
- **Scope document**: /Users/litlfred/space_cats/qou/.agents/orchestrator_batch8/PROJECT.md
1. **Decompose**: Decomposed into 10 parallel proof-discharge tasks (one for each target file).
2. **Dispatch & Execute**:
   - **Direct (iteration loop)**: Iterate over 10 target files, spawning teamwork_preview_worker or self subagents, verifying each via lean-direct or lean-verify.sh, and pushing results.
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: Self-succeed at 16 spawns.
- **Work items**:
  1. ParticleInteractions/atomic_nf_witness.lean [done]
  2. ParticleInteractions/parity_regime_selection.lean [done]
  3. ParticleInteractions/four_term_pair_nucleon.lean [done]
  4. ParticleInteractions/confinement_frobenius_reciprocity.lean [done]
  5. ParticleInteractions/operator_selection_lp.lean [done]
  6. ParticleInteractions/ground_state_ordering.lean [done]
  7. ParticleInteractions/mass_categorical_descent.lean [done]
  8. ParticleInteractions/transfer_matrix_identities.lean [done]
  9. ParticleInteractions/deuterium_derived_binding.lean [done]
  10. ParticleInteractions/frobenius_positivity_filter.lean [done]
- **Current phase**: 4
- **Current focus**: Complete and report victory

## 🔒 Key Constraints
- Throttled to max 10 concurrent active worker subagents at a time.
- Never write, modify, or create source code files directly.
- Never run build/test commands yourself — require workers to do so.
- Insert `import Mathlib` at top of files using ℝ, ℕ, or | | to prevent synthesis issues.
- Never reuse a subagent after it has delivered its handoff — always spawn fresh.

## Current Parent
- Conversation ID: 6d37ee5b-d998-4962-b4ad-e8849799d11e
- Updated: not yet

## Key Decisions Made
- Use teamwork_preview_worker for Lean proof discharges.
- Verify using lean-direct or scripts/lean-verify.sh run by the worker.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| worker_atomic_nf_witness | teamwork_preview_worker | Prove ParticleInteractions/atomic_nf_witness.lean | completed | 8a26666b-401d-4613-9121-450db7fa24b6 |
| worker_parity_regime_selection | teamwork_preview_worker | Prove ParticleInteractions/parity_regime_selection.lean | completed | 062c1fdf-e497-4749-b183-945200160c97 |
| worker_four_term_pair_nucleon | teamwork_preview_worker | Prove ParticleInteractions/four_term_pair_nucleon.lean | completed | 81c2dae4-7bc6-4c18-8160-7ff37021543a |
| worker_confinement_frobenius_reciprocity | teamwork_preview_worker | Prove ParticleInteractions/confinement_frobenius_reciprocity.lean | completed | f6f1ab53-6253-4907-b53f-668ad12ce5b3 |
| worker_operator_selection_lp | teamwork_preview_worker | Prove ParticleInteractions/operator_selection_lp.lean | completed | 55bc22a9-8db4-490c-b8d4-7cf470258c5c |
| worker_ground_state_ordering | teamwork_preview_worker | Prove ParticleInteractions/ground_state_ordering.lean | completed | 57652cf6-1d08-4d21-9087-8ea54275ea5f |
| worker_mass_categorical_descent | teamwork_preview_worker | Prove ParticleInteractions/mass_categorical_descent.lean | completed | 5103b68d-a008-47b2-8f1b-4311d5453754 |
| worker_transfer_matrix_identities | teamwork_preview_worker | Prove ParticleInteractions/transfer_matrix_identities.lean | completed | cc223507-1417-4c36-bacc-f65d4335ee2a |
| worker_deuterium_derived_binding | teamwork_preview_worker | Prove ParticleInteractions/deuterium_derived_binding.lean | completed | 55dfcd1e-672a-45f9-aad2-1d6d1cced8a4 |
| worker_frobenius_positivity_filter | teamwork_preview_worker | Prove ParticleInteractions/frobenius_positivity_filter.lean | completed | c243ce40-8b75-4cc2-bdb1-7e316258827a |

## Succession Status
- Succession required: no
- Spawn count: 10 / 16
- Pending subagents: none
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: stopped
- Safety timer: none
- On succession: kill all timers before spawning successor
- On context truncation: run `manage_task(Action="list")` — re-create if missing

## Artifact Index
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch8/PROJECT.md — Scope document
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch8/plan.md — Detailed work plan
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch8/progress.md — Progress tracker
