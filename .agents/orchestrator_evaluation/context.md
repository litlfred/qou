# Context: QA Backlog Evaluation

## Location Paths
- Project Root: `/home/litlfred/space_cats/qou`
- Backlog Queue: `todos/qa-agent-drain-queue.json`
- Write Script: `folio-assistant/src/qa-agent-write.ts`
- Check Script: `content/pipeline/qa-agent-drain-queue.ts`

## Explorer Findings Summary
- There are multiple batches containing blocks.
- The write script enforces rubric score bands matching results (`frac >= 0.66` $\implies$ pass, etc.).
- Proof stubs should be evaluated with specific scores:
  - `proof-rater-goal-plausibility`: 1.0 (pass, no sorries), ~0.9 (pass, routine sorries), 0.34 (warn, core proof stub), 0.0 (fail, vacuous/empty proof).
  - Other proof criteria (`proof-statement-integrity`, `proof-no-bare-sorries`, `proof-narrative-lean-equiv`, `proof-no-self-assuming-projection`) are mapped to pass/fail.
