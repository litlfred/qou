# BRIEFING — 2026-06-24T00:00:30Z

## Mission
Orchestrate a fleet of worker agents to replace sorry stubs in 10 QOU Lean files with valid proofs and verify them.

## 🔒 My Identity
- Archetype: teamwork_preview_worker
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /Users/litlfred/space_cats/qou/.agents/orchestrator_batch4
- Original parent: parent
- Original parent conversation ID: 637c81af-e2b1-4ca1-9f54-cc8f6a7beac9

## 🔒 My Workflow
- **Pattern**: Project Pattern
- **Scope document**: /Users/litlfred/space_cats/qou/.agents/orchestrator_batch4/PROJECT.md
1. **Decompose**: Select 10 sorry-containing Lean files under QOU/, verify they are not in Batch 1, 2, or 3, and assign each to a worker agent.
2. **Dispatch & Execute**:
   - **Delegate (sub-orchestrator)**: Dispatch work to worker subagents (up to 10 concurrently).
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: Self-succeed at spawn count >= 16.
- **Work items**:
  1. nkx4 completed
- **Current phase**: 4
- **Current focus**: Verification & Commit completed

## 🔒 Key Constraints
- Max 10 concurrent subagents active.
- Skip stubs completed in Batch 1, 2, 3.
- Critical: Insert `import Mathlib` at the top of the files if they use `ℝ`, `ℕ`, or `| |` to avoid synthesis errors.
- Never reuse a subagent after it has delivered its handoff — always spawn fresh.

## Current Parent
- Conversation ID: 637c81af-e2b1-4ca1-9f54-cc8f6a7beac9
- Updated: not yet

## Key Decisions Made
- Branched off `claude/prove-stubs-batch3-2026-06-23` to form `claude/prove-stubs-batch4-2026-06-23`.
- Cherry-picked `geom_yekutieli_alignment` commit `bde1cfef92` to resolve branch conflict.
- Micro-committed each proof change separately.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| a78c715d-dfdb-4be3-a9c4-ffe606bd9894 | teamwork_preview_explorer | Triage Explorer for Batch 4 | completed | a78c715d-dfdb-4be3-a9c4-ffe606bd9894 |
| 2053f6aa-147d-4dcc-ae12-bd89b2a75f3e | teamwork_preview_worker | Prove eos_borromean_cfl | completed | 2053f6aa-147d-4dcc-ae12-bd89b2a75f3e |
| c4439dd3-cbe3-4b96-ab99-76df1ee28ea4 | teamwork_preview_worker | Prove genus_filtration_ideal | completed | c4439dd3-cbe3-4b96-ab99-76df1ee28ea4 |
| c610b85b-e726-4231-9ba4-37b7be18a8a6 | teamwork_preview_worker | Prove genus_maximal_descent | completed | c610b85b-e726-4231-9ba4-37b7be18a8a6 |
| c15b4d9e-c2ee-4585-96ca-283b00a7ca3c | teamwork_preview_worker | Prove gram_weighted_qvalue | completed | c15b4d9e-c2ee-4585-96ca-283b00a7ca3c |
| 18e129d1-9ca0-4561-ad57-6594d81a1211 | teamwork_preview_worker | Prove brings_euler_characteristic | completed | 18e129d1-9ca0-4561-ad57-6594d81a1211 |
| 3942cd60-1e8d-4213-8477-686e0a642e0d | teamwork_preview_worker | Prove brings_riemann_hurwitz | completed | 3942cd60-1e8d-4213-8477-686e0a642e0d |
| d1733fa5-0de5-4108-9a62-53c5113b1408 | teamwork_preview_worker | Prove geom_yekutieli_alignment | completed | d1733fa5-0de5-4108-9a62-53c5113b1408 |
| 7ff3ff9b-ff98-48c3-82ae-a217fc3e20d5 | teamwork_preview_worker | Prove ofWeightDecomposition | completed | 7ff3ff9b-ff98-48c3-82ae-a217fc3e20d5 |
| 93c62303-9e8c-4b69-8ab7-b913f4d4e849 | teamwork_preview_worker | Prove u1EquivariantReduction | completed | 93c62303-9e8c-4b69-8ab7-b913f4d4e849 |
| 0c7bca89-971d-4394-9891-223d3a59a4fc | teamwork_preview_worker | Prove discrete_vortex_spectrum | completed | 0c7bca89-971d-4394-9891-223d3a59a4fc |

## Succession Status
- Succession required: no
- Spawn count: 11 / 16
- Pending subagents: none
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: 1df9c14e-d3d9-4c36-bfa0-cc5374d68b1c/task-69 (to be killed)
- Safety timer: none
- On succession: kill all timers before spawning successor
- On context truncation: run `manage_task(Action="list")` — re-create if missing

## Artifact Index
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch4/PROJECT.md — scope/milestone layout
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch4/progress.md — liveness and checklists
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch4/ORIGINAL_REQUEST.md — verbatim original request
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch4/handoff.md — final handoff report
