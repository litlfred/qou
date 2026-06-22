# Project: Lean Code Audit & QA Backlog Drain

## Architecture
- Target: 184 newly flagged `proof-no-placeholder-stub` Lean files and `.qa.json` sidecar verification.
- Target: Draining the `qa-agent-drain-queue.json` backlog.
- Rating: Audit quality evaluation using `proof-rater` rubrics.
- Validation: CI checks (`lean_ci`, `qa-sweep`, `lean_verify`).

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Inventory & Setup | Identify target files, verify queue status, partition work | None | DONE |
| 2 | Placeholder Audit | Audit/stub 184 files, delete shadow stubs, update genuine ones | M1 | DONE |
| 3 | QA Queue Drain | Adjudicate pending agent-checked QA criteria in queue | M1 | DONE |
| 4 | Proof Rating | Apply `proof-rater` rubrics to audited files | M2, M3 | DONE |
| 5 | Validation Sweeps | Run validation tools (`lean_ci`, `qa-sweep`, `lean_verify`) | M2, M3, M4 | DONE |
| 6 | Forensic Audit | Perform integrity checks and verify clean status | M5 | DONE |
| 7 | Handoff & Reports | Generate final handoff.md and notify Sentinel | M6 | DONE |

## Subagent Delegation
1. **worker_stub_audit** (Conv ID: `c2cdac43-eb39-4d40-aa03-a969eb33228d`): Audits the 184 placeholder stubs under `content/quantum-observable-universe/lean/QOU/`. Deletes shadow stubs and updates genuine placeholders to pass `proof-no-placeholder-stub` checks. (Completed)
2. **worker_qa_drain** (Conv ID: `7fe56456-225f-47d6-b6dd-0a105b5905b3`): Adjudicates pending agent-checked QA criteria from `.beans/qa-agent-drain-queue.json` using `qa-agent-write.ts`. (Completed)

## Interface Contracts
- Subagents will write audit decisions directly to the relevant `.qa.json` sidecars using standard tools.
- Subagents will update the queue status in `.beans/qa-agent-drain-queue.json`.
- Programmatic validations will run across all targeted directories.
