# Atomic-content QA drain — workplan (2026-06-28)

Owner directive: *"fix all qa audits. i want atomic content"* → *"do audit first
as high quality swarm"* → *"once swarm completes, have another set of swarm
agents to fix"* → *"auto prepare-merge in batches. just drain away audits and
fixes."*

## Context / why this doc exists

The prior session on this branch (`claude/split-first-wave-3-po4f16`) chased a
**nonexistent criterion** `clarity-remark-single-topic` (not in the skill, not in
`content/pipeline/definition-clarity-audit.ts`) and lost all its uncommitted work
to container reclaim (branch was byte-identical to `origin/main`). This drain is
the corrected, durable redo: agent-judgment detector (not phantom regex),
committed+pushed every batch.

## Pipeline

1. **Audit swarm** (Workflow `atomic-content-audit-swarm`, 90 chapter-coherent
   batches over 850 regex-flagged blocks). Each agent adjudicates the high-recall
   regex candidates (filters false positives) and emits a concrete atomization
   plan per genuine violation. Output: schema-validated verdicts → committed report.
2. **Fix swarm** — second agent set applies the confirmed plans, batched **by
   chapter** (no two agents touch the same chapter manifest), validates with
   `bun run scripts/run-validate.ts content/<paper>`.
3. **Batched prepare-merge drain** — one PR per chapter batch, `/prepare-merge`,
   merge when green. Drain until the work-list is clear.

## Atomicity criteria (the "atomic content" axis)

`remark-multi-topic` (398 candidate remarks), `clarity-defn-single`,
`clarity-defn-tight`, `clarity-stmt-tight`, `clarity-stmt-pure`,
`clarity-proof-pure`, `clarity-defterm-bold`, `clarity-defn-misplaced`.

## Work-list

`2026-06-28-atomic-content-worklist.json` — 850 blocks, 32 chapters
(mass-theory 226, particle-interactions 89, predicted-spectra 82, …). Regenerate
batches from this file. Real **fail** candidates only (the raw 9645 figure counted
pass/na records too).

## Durability rule

Commit + push after EVERY batch. Track in beans (epic `dd3f`; phases `k4bk`
audit, `l98u` fix, `v93v` merge-drain). Never accumulate uncommitted work.
