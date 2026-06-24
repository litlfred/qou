# BRIEFING — 2026-06-24T04:29:00Z

## Mission
Coordinate proving and verifying the 10 target Lean files for Batch 9, checking out the branch, managing workers, and compiling successfully.

## 🔒 My Identity
- Archetype: teamwork_preview_orchestrator
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /Users/litlfred/space_cats/qou/.agents/orchestrator_batch9/
- Original parent: parent
- Original parent conversation ID: 6d37ee5b-d998-4962-b4ad-e8849799d11e

## 🔒 My Workflow
- Pattern: Project Pattern
- Scope document: /Users/litlfred/space_cats/qou/.agents/orchestrator_batch9/PROJECT.md
1. **Decompose**: Decomposed into 10 target files as milestones.
2. **Dispatch & Execute**:
   - **Direct (iteration loop)**: Iterate over the 10 files using workers and verifiers.
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: Self-succeed at 16 spawns, write handoff.md, spawn successor.
- **Work items**:
  1. ParticleInteractions/lp_dual_stability.lean [done]
  2. ParticleInteractions/PerNucleonChannelDecomposition.lean [done]
  3. ParticleInteractions/positron_correction.lean [done]
  4. ParticleInteractions/SpectatorNormalization.lean [done]
  5. QuantumObservableUniverse/fibre_functor_atlas.lean [done]
  6. QuantumObservableUniverse/fai_projector_coadjoint_orbit.lean [done]
  7. Substrate/ProtonMassSubstrateIdentity.lean [done]
  8. FluidDynamics/quantum_peter_weyl.lean [done]
  9. FluidDynamics/core_levi_form.lean [done]
  10. FluidDynamics/q_turbulence_spectrum.lean [done]
- **Current phase**: 4
- **Current focus**: Verification, staging, commit, and push.

## 🔒 Key Constraints
- Throttled to maximum of 10 concurrent active worker subagents.
- Run validation tools (lake build or scripts/lean-verify.sh) via workers.
- Commit all work to the branch claude/prove-stubs-batch9-2026-06-23 and push.
- Keep progress.md and plan.md updated.
- Never reuse a subagent after it has delivered its handoff — always spawn fresh

## Current Parent
- Conversation ID: 6d37ee5b-d998-4962-b4ad-e8849799d11e
- Updated: not yet

## Key Decisions Made
- Use teamwork_preview_worker for resolving sorry stubs in parallel.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| worker_lp_dual_stability | teamwork_preview_worker | lp_dual_stability.lean | completed | d6728b00-2197-45c1-ac11-ba7cd38ae800 |
| worker_PerNucleonChannelDecomposition | teamwork_preview_worker | PerNucleonChannelDecomposition.lean | completed | 4a811553-18d4-4daa-97f3-875c3d9e319c |
| worker_positron_correction | teamwork_preview_worker | positron_correction.lean | completed | d5090649-b940-41b2-8b6a-0313903b0836 |
| worker_SpectatorNormalization | teamwork_preview_worker | SpectatorNormalization.lean | completed | 8f4319d1-b3ac-48ba-87e0-6b194691db5a |
| worker_fibre_functor_atlas | teamwork_preview_worker | fibre_functor_atlas.lean | completed | ce88ef00-045a-4895-8810-353b33104706 |
| worker_fai_projector_coadjoint_orbit | teamwork_preview_worker | fai_projector_coadjoint_orbit.lean | completed | b3f764ab-7dac-4e03-8c27-a2e4a488b18b |
| worker_ProtonMassSubstrateIdentity | teamwork_preview_worker | ProtonMassSubstrateIdentity.lean | completed | 073a3fc0-1028-46f0-b21e-e778aaf5481c |
| worker_quantum_peter_weyl | teamwork_preview_worker | quantum_peter_weyl.lean | completed | fc64b0f0-dc0b-4d16-8100-44d2cb3133fe |
| worker_core_levi_form | teamwork_preview_worker | core_levi_form.lean | completed | 0cac86e0-0525-49f9-b555-e82bb7e616d2 |
| worker_q_turbulence_spectrum | teamwork_preview_worker | q_turbulence_spectrum.lean | completed | 9f22f115-8c60-467a-a451-868321627a48 |

## Succession Status
- Succession required: no
- Spawn count: 10 / 16
- Pending subagents: none
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: task-65
- Safety timer: none
- On succession: kill all timers before spawning successor
- On context truncation: run manage_task(Action="list") — re-create if missing

## Artifact Index
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch9/progress.md — progress tracking
- /Users/litlfred/space_cats/qou/.agents/orchestrator_batch9/plan.md — work plan
