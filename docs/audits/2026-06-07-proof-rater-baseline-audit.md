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

## First batch results — mass-theory (12 blocks, 48 entries)

A background agent scored the 12 provable-kind blocks returned by the proof-block
grep (0 skipped; the CLI handled all 48 writes first try). The run doubled as a
scale-test and surfaced a **band↔score consistency gap** in `qa-agent-write` (a
`--result`/`--score` mismatch was possible) — now closed with a band guard
(`≥0.66 pass, ≥0.33 warn, else fail`) that errors on mismatch; 3 mis-banded
entries were corrected, and all 39 scored entries are now consistent.

**Strategy-clarity was uniformly 1.0** (every block states its plan / case-split
/ cited lemmas up front). The rate half surfaced these lowest-score
**improve-backlog** items:

| Block | Finding | Score |
|---|---|---|
| `alpha-k-derivation-procedure` | **statement-integrity FAIL (critical)** — Lean `theorem … := ⟨_, rfl⟩` is a vacuous existence tautology, not the `.md`'s real claim (character-matrix invertibility ⇒ unique `y_λ`) | integrity fail |
| `alpha-shift-torus-knot` | core gap — maximality pt 1 only case-by-case (6 pairs) + conjectured/deferred categorical argument | plausibility 0.3 |
| `atom-knot-mass-derivation` | core gap — ~173× m_p shortfall acknowledged; key Lean is a substrate `axiom`; `MassIdentity` weakened to a 25 %-tolerance proxy | plausibility 0.3 |
| `beta-decay-transfer-matrix` | **md↔Lean mismatch** — `.md` boxes `Δ_β = ½(q−q⁻¹)𝕀` (diagonal) but sorry-free Lean proves off-diagonal `(1−q²)/2 ≠ 0` (Lean self-consistent ⇒ integrity passes; correctness follow-up) | flag |

These are recorded as the **baseline, not fixed here** — the improve half
(`/integration-backlog proof`, ascending-score) routes `alpha-k-derivation-procedure`
→ `lean-proof-review`, the two core-gap blocks → `proof-triage`, and files the
beta-decay mismatch for a correctness pass.

## Rollout (remaining corpus)

The full baseline is drained in **≤ 49-file batches** via `/integration-backlog
proof`, which now orders `proof-rater-*` by **ascending score** and re-rates
after each improver pass (the rate→improve loop). Targets are enumerated by the
needs-agent queue; each block is scored with `qa-agent-write --score`. Batches
proceed chapter-by-chapter so a mis-calibrated rubric is caught early rather
than across the whole corpus at once.

**Status:** infra + worked example + first batch (mass-theory, 12 blocks)
landed. Baseline scores are a *starting point* — the backlog's job is to raise them.
