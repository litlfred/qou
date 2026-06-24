# BRIEFING — 2026-06-24T09:48:27Z

## Mission
Coordinate the formal proof migration for Batch 12, replacing sorrys with verified Lean 4 proofs in 9 target files.

## 🔒 My Identity
- Archetype: teamwork_preview
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /Users/litlfred/space_cats/qou/.agents/orchestrator_batch12/
- Original parent: parent
- Original parent conversation ID: 6d37ee5b-d998-4962-b4ad-e8849799d11e

## 🔒 My Workflow
- **Pattern**: Project
- **Scope document**: /Users/litlfred/space_cats/qou/.agents/orchestrator_batch12/PROJECT.md
1. **Decompose**: The scope is pre-decomposed into 9 files in PROJECT.md. Each file is treated as a separate work item.
2. **Dispatch & Execute**:
   - **Direct (iteration loop)**: Spawn worker subagents to replace sorrys in parallel (throttled to 10 concurrent).
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: Self-succeed at 16 subagent spawns. Write handoff.md, spawn successor.
- **Work items**:
  1. `ArchimedeanUniverse/mi_sw_cartan_reduction.lean` [pending]
  2. `ArchimedeanUniverse/heisenberg_commutator.lean` [pending]
  3. `FrobeniusHopfData/frobeniusForm.lean` [pending]
  4. `Observations/QPlancherelAsymptoticSkeleton.lean` [pending]
  5. `Observations/SDPRegimeSwitch.lean` [pending]
  6. `Observations/centered_hecke_variance_positive.lean` [pending]
  7. `Observations/hecke_satisfies_blitvic_hypothesis.lean` [pending]
  8. `FeynmanPathIntegrals/markov_identification.lean` [pending]
  9. `Descent/descended_level_zero.lean` [pending]
- **Current phase**: 1
- **Current focus**: Launching workers for the 9 target files.

## 🔒 Key Constraints
- Throttled to a maximum of 10 concurrent worker subagents.
- Ensure `import Mathlib` at the top of files using ℝ, ℕ, or | | to prevent synthesis errors.
- Never write, modify, or create source code files directly (delegate to workers).
- Never run build/test commands directly (delegate to workers or verify at the end).
- Never reuse a subagent after it has delivered its handoff.

## Current Parent
- Conversation ID: 6d37ee5b-d998-4962-b4ad-e8849799d11e
- Updated: not yet

## Key Decisions Made
- Pre-decomposed into 9 parallel worker dispatches since the files are independent.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|

## Succession Status
- Succession required: no
- Spawn count: 0 / 16
- Pending subagents: none
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: not started
- Safety timer: none
- On succession: kill all timers before spawning successor
- On context truncation: run `manage_task(Action="list")` — re-create if missing

## Artifact Index
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch12/PROJECT.md — Global index, architecture, milestones, interfaces, code layout
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch12/ORIGINAL_REQUEST.md — Verbatim record of user request
