# Plan - Lean Sorry Stub Proof Migration Batch 13

## Objectives
1. Prove the 1 target Lean file in Batch 13 using a worker subagent.
2. Validate the proof compiles successfully using `scripts/lean-verify.sh`.
3. Commit to `claude/prove-stubs-batch13-2026-06-23` and push.

## Steps
1. **Initial setup**: Set up the git branch `claude/prove-stubs-batch13-2026-06-23`.
2. **Dispatch Worker**:
   - Spawn a worker for `Archimedean/rj_canonical_inner_product.lean`.
   - Provide instructions to read the corresponding `.md` file, understand the math, implement the proof, verify it, and hand it back.
3. **Monitor and Verify**:
   - Check the progress of the worker.
   - Collect and review verified proofs.
4. **Commit and Push**:
   - Commit files.
   - Push changes.
   - Report success.
