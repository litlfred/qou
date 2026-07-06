# Plan - Lean Sorry Stub Proof Migration Batch 12

## Objectives
1. Prove the 9 target Lean files in parallel using worker subagents.
2. Throttled to max 10 concurrent agents (we have 9 target files, so all can run in parallel).
3. Validate each proof compiles successfully using `lean`-direct or `lake build`.
4. Commit to `claude/prove-stubs-batch12-2026-06-23` and push.

## Steps
1. **Initial setup**: Set up the git branch `claude/prove-stubs-batch12-2026-06-23` (create if missing, switch to it, coordinate with sibling branches).
2. **Fetch Lean cache**: Run cache restore to speed up compile times.
3. **Dispatch Workers**:
   - Spawn a worker for each of the 9 files.
   - Provide each worker with instructions to read the corresponding `.md` file, understand the math, implement the proof, verify it, and hand it back.
4. **Monitor and Verify**:
   - Check the progress of each worker.
   - If any worker gets stuck, retry or replace.
   - Collect and review verified proofs.
5. **Commit and Push**:
   - Commit files.
   - Push changes.
   - Report success.
