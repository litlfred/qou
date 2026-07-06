# Plan — Lean Sorry Stub Proof Migration - Batch 5

## Selected Targets
1. `FluidDynamics/q_ns_wellposedness.lean`
2. `FluidDynamics/vorticity_lower_bound.lean`
3. `FluidDynamics/acoustic_horizon_conditions.lean`
4. `FluidDynamics/kelvin_dispersion_derivation.lean`
5. `Molecular/shell_filling_rule.lean`
6. `Brings/coral_elliptic.lean`
7. `Brings/brings_is_qou.lean`
8. `Observations/brane_tower_q_laplacian_decay.lean`
9. `Observations/strangelet_crossing_energy.lean`
10. `Observations/substrate_consistency_window.lean`

## Execution Steps
1. **Decomposition & Milestones**: (Done) Registered target files as milestones in `PROJECT.md`.
2. **Dispatch Worker Agents**: Spawn 10 `teamwork_preview_worker` subagents (one for each target file) to:
   - Read the corresponding `.md` content file to understand the math.
   - Insert `import Mathlib` at the top of the file if it uses `ℝ`, `ℕ`, or `| |`.
   - Write a valid Lean proof to replace the `sorry` statement.
   - Run `lake build` or `./scripts/lean-verify.sh` to compile and verify.
   - Save a handoff.md in their working directory containing passing build/test output.
3. **Throttled Monitoring**: Keep concurrent worker count <= 10. Wait until all 10 report completion and successful build.
4. **Integration & Final Verification**:
   - Verify all 10 files compile successfully.
   - Run a project-wide validation.
5. **Commit & Push**: Commit all modifications on branch `claude/prove-stubs-batch5-2026-06-23` and push.
6. **Victory Report**: Report completion to the user.
