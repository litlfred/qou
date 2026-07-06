# BRIEFING — 2026-06-16T01:36:50Z

## Mission
Audit and rewrite the QOU expository literature and computational codebase (Python/Rust) to purge the interpretation of q as a rigid global constant, realigning around the 3 calibration points, asserting q is synonymous with local mass ratio, and verifying implementation.

## 🔒 My Identity
- Archetype: teamwork_preview_orchestrator
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /home/litlfred/space_cats/qou/.agents/orchestrator_q_purge/
- Original parent: parent
- Original parent conversation ID: 6e47398d-42d8-41e4-b087-a0e49ebf9d67

## 🔒 My Workflow
- **Pattern**: Project
- **Scope document**: /home/litlfred/space_cats/qou/.agents/orchestrator_q_purge/SCOPE.md
1. **Decompose**: Decompose the task into milestones: investigation, markdown audit, python/rust refactor, execution validation, and reviewer/auditor validation.
2. **Dispatch & Execute** (pick ONE):
   - **Direct (iteration loop)**: Iterate via Explorer -> Worker -> Reviewer -> Challenger -> Auditor.
   - **Delegate (sub-orchestrator)**: For large milestones, spawn sub-orchestrators.
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: Spawn successor at 16 spawns, write handoff.md, cancel crons.
- **Work items**:
  1. Project Setup and Initial Investigation [in-progress]
  2. Implement R1: QA Sidecar Audit (Markdown) [pending]
  3. Implement R2: Codebase Refactoring (Python/Rust) [pending]
  4. Implement R3: Execution Validation [pending]
  5. Final Integration & Verification [pending]
- **Current phase**: 1
- **Current focus**: Project Setup and Initial Investigation

## 🔒 Key Constraints
- NEVER write, modify, or create source code files directly.
- NEVER run build/test commands yourself — require workers to do so.
- Never reuse a subagent after it has delivered its handoff — always spawn fresh
- Succession threshold: 16 spawns.

## Current Parent
- Conversation ID: 6e47398d-42d8-41e4-b087-a0e49ebf9d67
- Updated: not yet

## Key Decisions Made
- [TBD]

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| explorer_m1 | teamwork_preview_explorer | Scan scope files and code for q constant and calibration issues. | in-progress | bef42011-d115-4f6d-a501-6ad16568cd60 |

## Succession Status
- Succession required: no
- Spawn count: 1 / 16
- Pending subagents: bef42011-d115-4f6d-a501-6ad16568cd60
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: task-15
- Safety timer: none
- On succession: kill all timers before spawning successor
- On context truncation: run `manage_task(Action="list")` — re-create if missing

## Artifact Index
- /home/litlfred/space_cats/qou/.agents/orchestrator_q_purge/ORIGINAL_REQUEST.md — Original User Request Copy
