# BRIEFING — 2026-06-24T00:36:20-04:00

## Mission
Replace sorry in SymmetricCrystalPairProduction.lean with rfl, check mathlib imports, and verify compilation using lean-verify.sh.

## 🔒 My Identity
- Archetype: teamwork_preview_orchestrator
- Roles: [orchestrator, user_liaison, human_reporter, successor]
- Working directory: /Users/litlfred/space_cats/qou/.agents/worker_SymmetricCrystal/
- Original parent: parent
- Original parent conversation ID: 50cdb3c0-bac7-43f7-adc3-1e88330d5f22

## 🔒 My Workflow
- **Pattern**: Project
- **Scope document**: /Users/litlfred/space_cats/qou/.agents/worker_SymmetricCrystal/SCOPE.md
1. **Decompose**: The scope is a single file proof replacement, which is simple. We will use a single iteration loop (Explorer -> Worker -> Reviewer -> Challenger -> Auditor) with a single milestone.
2. **Dispatch & Execute**:
   - Direct (iteration loop): Explorer -> Worker -> Reviewer -> Challenger -> Auditor -> Gate.
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: Self-succeed at 16 spawns.
- **Work items**:
  1. Replace sorry in SymmetricCrystalPairProduction.lean and check imports [pending]
  2. Verify compilation [pending]
- **Current phase**: 1
- **Current focus**: Replace sorry and check imports

## 🔒 Key Constraints
- Never write, modify, or create source code files directly.
- Never run build/test commands yourself — require workers to do so.
- Never reuse a subagent after it has delivered its handoff — always spawn fresh

## Current Parent
- Conversation ID: 50cdb3c0-bac7-43f7-adc3-1e88330d5f22
- Updated: not yet

## Key Decisions Made
- Use Project pattern. Since the task is simple, we will use a direct iteration loop rather than sub-milestone subagents. We will spawn an Explorer first to verify imports/approach, then a Worker, then a Reviewer and Auditor.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| worker_sorry_rfl | teamwork_preview_worker | Replace sorry, check imports, verify | completed | 0143143a-bd6b-4ded-bcb2-48356cb45c7e |
| auditor_sorry_rfl | teamwork_preview_auditor | Run integrity audit on sorry change | in-progress | 5e7dc707-3593-458c-bc0d-ee5b787bd347 |

## Succession Status
- Succession required: no
- Spawn count: 2 / 16
- Pending subagents: [5e7dc707-3593-458c-bc0d-ee5b787bd347]
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: task-31
- Safety timer: task-56

## Artifact Index
- /Users/litlfred/space_cats/qou/.agents/worker_SymmetricCrystal/ORIGINAL_REQUEST.md — Original request
- /Users/litlfred/space_cats/qou/.agents/worker_SymmetricCrystal/progress.md — Progress and liveness heartbeat
- /Users/litlfred/space_cats/qou/.agents/worker_SymmetricCrystal/SCOPE.md — Scope document
