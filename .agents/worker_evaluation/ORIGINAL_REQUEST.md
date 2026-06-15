## 2026-06-15T13:17:04Z
You are the teamwork_preview_worker. Your working directory is `/home/litlfred/space_cats/qou/.agents/worker_evaluation/`.
Please perform the implementation and verification task described below.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT
hardcode test results, create dummy/facade implementations, or
circumvent the intended task. A Forensic Auditor will independently
verify your work. Integrity violations WILL be detected and your
work WILL be rejected.

### Objective
Complete the QA Backlog by evaluating the blocks in `todos/qa-agent-drain-queue.json` and writing the verdicts via `bun run folio-assistant/src/qa-agent-write.ts`.

### Task Instructions
1. Inspect the unique list of `need` criteria in `todos/qa-agent-drain-queue.json`.
2. Write a Node/TS script at `todos/evaluate-backlog.ts` to automate the evaluation.
3. For each block in the queue:
   - Read its manifest `.ts` file to get metadata (e.g. `lean.ref`).
   - Check if a sibling `.lean` file exists. If not, resolve the canonical Lean file (you can import `resolveCanonicalLean` from `content/pipeline/qa-utils.ts` or implement the resolution logic).
   - Read the Lean file content.
   - Implement the following evaluation heuristics:
     - **proof-rater-goal-plausibility**:
       - If the Lean file contains no `sorry` or `sorryAx`: result = `"pass"`, score = `1.0`, score-max = `1`, notes = `"No remaining goals or sorries in formalization."`
       - If it contains `sorry` or `sorryAx`:
         - Determine if it is a trivial skeleton: e.g., if the Lean file is very small (<15 lines or <500 characters) or the theorem body is just `:= sorry` or `:= by sorry` or `True := by trivial` without other non-trivial definitions. If trivial skeleton: result = `"fail"`, score = `0.0`, score-max = `1`, notes = `"Trivial skeleton proof stub restating the target."`
         - Otherwise (core proof stub): result = `"warn"`, score = `0.34`, score-max = `1`, notes = `"Proof stub with core gaps but carries math structure and definitions."`
     - **proof-statement-integrity**:
       - If it contains `sorry` or `sorryAx` $\implies$ result = `"fail"`, notes = `"Declaration contains sorryAx or unexpected axioms."`
       - Else $\implies$ result = `"pass"`, notes = `"No unexpected axioms or sorryAx."`
     - **proof-no-bare-sorries**:
       - If it contains `sorry` or `sorryAx`: check if all occurrences have `-- Ref: [key]` preceding or on the same line. If so $\implies$ result = `"pass"`, notes = `"All sorry occurrences are cited."` Otherwise $\implies$ result = `"fail"`, notes = `"Contains bare sorry without citation."`
       - Else $\implies$ result = `"pass"`, notes = `"No sorries in the proof."`
     - **proof-narrative-lean-equiv**:
       - If it contains `sorry` or `sorryAx` $\implies$ result = `"fail"`, notes = `"Narrative claims completed proof but Lean uses a sorry stub."`
       - Else $\implies$ result = `"pass"`, notes = `"Narrative and formalization are equivalent."`
     - **proof-no-self-assuming-projection**:
       - If it is a placeholder stub (has `sorry`/`sorryAx` or is a trivial skeleton) $\implies$ result = `"fail"`, notes = `"Placeholder stub is unformalised."`
       - Else $\implies$ result = `"pass"`, notes = `"No self-assuming projection detected."`
     - **proof-no-trivial-true**:
       - If it is a placeholder stub or the conclusion is `True`/`x = x`/`0 = 0` $\implies$ result = `"fail"`, notes = `"Goal or proof is trivial/vacuous."`
       - Else $\implies$ result = `"pass"`, notes = `"Not a trivial true goal."`
     - **proof-no-false-premise**:
       - If the premise contains `False` or `0 = 1` or similar contradiction $\implies$ result = `"fail"`.
       - Else $\implies$ result = `"pass"`.
     - **proof-no-unused-hypotheses**:
       - If the proof has unused hypotheses $\implies$ result = `"fail"`.
       - Else $\implies$ result = `"pass"`.
     - **proof-no-decide-masking**:
       - If it is a stub or has decide-masking $\implies$ result = `"fail"`, notes = `"Stub uses decide/trivial masking."`
       - Else $\implies$ result = `"pass"`.
     - **For other criteria (voice-*, fit-*, wall-*)**:
       - If any exist, default to `pass` or apply simple checks.
   - For each block/criterion, execute the CLI tool:
     ```bash
     bun run folio-assistant/src/qa-agent-write.ts \
       --block <block> \
       --criterion <criterion> \
       --result <result> \
       [--score <score> --score-max 1] \
       --notes "<notes>"
     ```
4. Run the script and make sure it completes successfully.
5. Verify the final queue status by running:
   ```bash
   bun run content/pipeline/qa-agent-drain-queue.ts content/quantum-observable-universe
   ```
   Check that it outputs exactly `"0 batches, 0 blocks, 0 gaps"`.
6. Run `git status` to confirm that the `.qa.json` files have been modified.
7. Clean up the temporary script `todos/evaluate-backlog.ts`.
8. Write a detailed handoff report in `/home/litlfred/space_cats/qou/.agents/worker_evaluation/handoff.md` and send a message back to the parent (conversation ID: 49e0f52a-d52a-481c-878a-c23c9da54456).
