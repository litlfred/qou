# Plan - Lean Sorry Stub Proof Migration - Batch 6

This plan outlines the steps for replacing the `sorry` statements in 10 target Lean files with valid Lean proofs and verifying their correctness.

## Strategy
1. **Prepare Workspace**: Create `progress.md` and `plan.md` (this file) and start the heartbeat timer.
2. **Dispatch Worker Subagents**:
   - Spawn worker subagents (`teamwork_preview_worker`) for each of the 10 files.
   - Limit concurrency to 10 concurrent active agents.
   - For each target file, the worker subagent will:
     a. Read the target Lean file and corresponding `.md` content.
     b. Understand the math.
     c. Replace the `sorry` statements with valid Lean proofs.
     d. Add `import Mathlib` at the top of the file if the file uses `ℝ`, `ℕ`, or `| |` and doesn't already have it.
     e. Run verification tools (`lake build` or `scripts/lean-verify.sh`) to verify the file compiles successfully.
     f. Report back with the changes and proof verification results.
3. **Verify and Integrate**:
   - Track each worker's progress.
   - If verification fails or a worker gets stuck, apply the fault tolerance protocol (retry or replace).
4. **Commit and Push**:
   - Commit all successfully verified files to the branch `claude/prove-stubs-batch6-2026-06-23`.
   - Push the branch to `origin`.
5. **Report Victory**: Present a summary of the completed work and report completion to the user.

## Target Files
1. `variational_equations.lean`
2. `q_gl_obstruction_calc.lean`
3. `orbital_fourier_decomposition.lean`
4. `qou_canonical_action.lean`
5. `MassEndomorphism/PhiQConvergence.lean`
6. `Interactions/BorromeanUnique.lean`
7. `Interactions/QIntegerMassFormula.lean`
8. `Archimedean/skein_finiteness_bound.lean`
9. `Archimedean/torus_knot_shell_binding.lean`
10. `Archimedean/shell_structure_eigenvalues.lean`
