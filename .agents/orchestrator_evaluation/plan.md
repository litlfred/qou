# Plan: QA Backlog Evaluation and Automation

## Objective
Drain all blocks from `todos/qa-agent-drain-queue.json` by running heuristic reviews on markdown and Lean files, calling the pipeline write script, and verifying that the final backlog is empty.

## Execution Strategy
1. **Script Development (Node/TypeScript)**:
   - Read and parse `todos/qa-agent-drain-queue.json`.
   - Identify all unique blocks and their associated criteria.
   - For each block/criterion pair:
     - Check sibling files: `.ts` (manifest), `.md` (narrative), and `.lean` (formalization, resolving canonical lean file if missing).
     - Implement heuristics for proof-related criteria.
     - Call `bun run folio-assistant/src/qa-agent-write.ts` with correct arguments (including result, score, evidence, and notes).
2. **Execute**:
   - Run the script across all batches.
3. **Verify**:
   - Run `bun run content/pipeline/qa-agent-drain-queue.ts content/quantum-observable-universe` and ensure output is exactly "0 batches, 0 blocks, 0 gaps".
   - Run `git status` to verify modified files.
4. **Audit**:
   - Spawn the Forensic Auditor to verify the integrity of the work and check for any violations.
