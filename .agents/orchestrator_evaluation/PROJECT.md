# Project: QA Agent Backlog Evaluation Orchestrator

## Architecture
- **Work Queue**: `todos/qa-agent-drain-queue.json` containing batches of blocks.
- **Target Files**: Sibling `.md`, `.lean`, and `.ts` files per block.
- **QA Sidecars**: `${block}.qa.json` modified via `folio-assistant/src/qa-agent-write.ts`.
- **Drain Check Script**: `content/pipeline/qa-agent-drain-queue.ts`.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Analysis & Prep | Analyze backlog, target files, and write scripts | None | DONE |
| 2 | Automation Script Design | Write Node/TS script to parse queue and apply heuristics | M1 | DONE |
| 3 | Execution & Logging | Run the script to write verdicts for all pending blocks | M2 | DONE |
| 4 | Verification & Validation | Verify 0 batches, 0 blocks, 0 gaps output and check Git status | M3 | DONE |

## Code Layout
- Queue: `todos/qa-agent-drain-queue.json`
- Script: `folio-assistant/src/qa-agent-write.ts`
- Queue Check: `content/pipeline/qa-agent-drain-queue.ts`
- Work directory: `/home/litlfred/space_cats/qou`
- Agent metadata: `/home/litlfred/space_cats/qou/.agents/orchestrator_evaluation`
