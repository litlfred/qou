# Plan: Lean Sorry Stub Proof Migration - Batch 10

## Goal
Successfully migrate 10 sorry stub Lean files to verified proofs, committing changes to `claude/prove-stubs-batch10-2026-06-23`.

## Detailed Steps
1. **Setup Branch**: Switch to/create branch `claude/prove-stubs-batch10-2026-06-23`. (Wait, let's have a subagent or command do this. Actually, can the orchestrator run a git command to switch branch? The rule says "NEVER write, modify, or create source code files directly. NEVER run build/test commands yourself — require workers to do so." But what about git commands? To be safe, git commands don't modify source files directly or run builds/tests. But I can also have a worker switch branches, or I can run the command `git checkout -B ...` myself if it's permitted. Let's see if we should just run command. Let's do `git checkout -b` or check if the branch exists.)
Wait! Let's check branch conventions first:
"Structured branch names. All new branches follow the existing pattern: claude/<theme>-<utc-ymd>... Naming is pre-authorized."
The user request specifically asks: "7. Commit all work to the branch `claude/prove-stubs-batch10-2026-06-23` and push it." So we will switch to/create that branch.
2. **Decompose Tasks**:
   We have 10 target files. We will spawn 10 worker subagents (using `teamwork_preview_worker` or `self`) to implement proofs for them in parallel.
3. **Dispatch Workers**:
   Spawn one worker for each file:
   - Worker 1: `FluidDynamics/root_of_unity_truncation.lean`
   - Worker 2: `FluidDynamics/helicity_conservation.lean`
   - Worker 3: `HyperellipticQuintic/minimal_z5_classification.lean`
   - Worker 4: `BaryonWeight/beta4_hook.lean`
   - Worker 5: `LiftingDescent/JetProlongation.lean`
   - Worker 6: `LiftingDescent/jp_categorical_jet.lean`
   - Worker 7: `LiftingDescent/tm_eigenspace_decomp.lean`
   - Worker 8: `LiftingDescent/tm_descended_is_holonomy.lean`
   - Worker 9: `LiftingDescent/tm_dilogarithm_evaluation.lean`
   - Worker 10: `LiftingDescent/tm_transient_localisation.lean`
4. **Monitor and Verify**:
   Track progress. Each worker is responsible for editing its file, adding `import Mathlib` if needed, running verification tools, and reporting back.
5. **Verify Entire Build**:
   Verify everything compiles cleanly on the target branch.
6. **Commit & Push**:
   Commit and push changes.
7. **Report Victory**:
   Inform user and parent agent.
