# Proof rater-rubric — baseline audit

**Date:** 2026-06-07
**PR:** (this branch `claude/proof-rater-baseline-audit-2026-06-07`)
**Depends on:** the rater-rubric QA framework merged in #1936
([`2026-06-07-google-paper-qa-rubrics-and-tooling.md`](2026-06-07-google-paper-qa-rubrics-and-tooling.md)).

Goal: establish the **baseline `score` set** for the four
AlphaProof-Nexus-derived proof criteria across the corpus's proof blocks, so
the watch→backlog *rate-and-improve* loop has a starting point to raise.

## Hand-in-hand scale fix (found while starting the baseline)

The framework registered the criteria but the **agent write path
(`qa-agent-write.ts`) had no `score` support** — so a rater score could not be
persisted. Fixed here: `--score <0–1> [--score-max N] [--score-rubric JSON]`
now writes `QaCriterionEntry.score`. This is exactly the kind of
"QA issue at scale" the hand-in-hand approach was meant to surface before a
corpus-wide rollout.

```bash
bun run content/pipeline/qa-agent-write.ts \
  --block <base-path> --criterion proof-rater-strategy-clarity \
  --result pass --score 0.9 --skill local/proof-integration-watcher
```

## Scoring rubric (0–1; band → `result`)

| Criterion | 1.0 | 0.5 | 0.0 |
|---|---|---|---|
| `proof-rater-strategy-clarity` | plan stated up front | recoverable but implicit | opaque step-dump |
| `proof-rater-goal-plausibility` | sorry-free (or all gaps `routine`) | mixed | a `core`/`restates-target` gap |
| `proof-rater-novelty` | novel argument | standard, not duplicated | redundant (consolidate) |

Band → `result`: `≥ 0.66 → pass`, `0.33–0.66 → warn`, `< 0.33 → fail` (minor).
`proof-statement-integrity` is pass/fail (no score). Scores are
**informational, not merge gates**.

## Worked example (this PR)

`lem:crystal-demazure-w0-refuted-deuteron` (merged #1923) — the first complete
baseline entry: strategy-clarity 0.9, goal-plausibility 1.0, novelty 0.85,
statement-integrity pass. Demonstrates the end-to-end write path.

## Rollout (remaining corpus)

The full baseline is drained in **≤ 49-file batches** via `/integration-backlog
proof`, which now orders `proof-rater-*` by **ascending score** and re-rates
after each improver pass (the rate→improve loop). Targets are enumerated by the
needs-agent queue; each block is scored with `qa-agent-write --score`. Batches
proceed chapter-by-chapter so a mis-calibrated rubric is caught early rather
than across the whole corpus at once.

**Status:** infra + worked example landed; first chapter batch in progress.
Baseline scores are a *starting point* — the backlog's job is to raise them.
