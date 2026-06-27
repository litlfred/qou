# Plan — worker_qa_infra_fix

This plan describes the steps to fix relative import paths in `folio-assistant/src/qa-agent-write.ts` and `folio-assistant/src/qa-agent-drain-queue.ts`.

## Steps

1. **Verify Initial Failures**
   - Run both TS scripts via Bun to confirm they fail with the expected "Cannot find module" errors.
   - *Verification*: Done, observed `Cannot find module '../../content/pipeline/qa-utils'` and `Cannot find module './qa-utils'`.

2. **Modify `folio-assistant/src/qa-agent-write.ts`**
   - Replace import `"../../content/pipeline/qa-utils"` with `"../content/pipeline/qa-utils"`.
   - Replace import `"../../schemas/block-qa"` with `"../schemas/block-qa"`.
   - *Verification*: View the modified file to check line edits are clean and correct.

3. **Modify `folio-assistant/src/qa-agent-drain-queue.ts`**
   - Replace import `"./qa-utils"` with `"../content/pipeline/qa-utils"`.
   - Replace import `"./qa-criteria-registry"` with `"../content/pipeline/qa-criteria-registry"`.
   - *Verification*: View the modified file to check line edits are clean and correct.

4. **Verify Final Success**
   - Run `bun run folio-assistant/src/qa-agent-write.ts` and ensure it outputs the argument validation error (not "Cannot find module").
   - Run `bun run folio-assistant/src/qa-agent-drain-queue.ts` and ensure it runs successfully or outputs the validation error (not "Cannot find module").
   - *Verification*: Confirm exit code and standard error output.

5. **Commit and Push Changes**
   - Stage the changes.
   - Commit as `fix(qa-infra): correct relative import paths in folio-assistant scripts`.
   - Push to the current branch.
   - *Verification*: Run `git status` and `git log -1` to confirm.

6. **Submit Handoff Report**
   - Write `handoff.md` in our working directory.
   - Notify the parent agent with a status message.
