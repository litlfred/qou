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

## Integration-watcher wiring

The rater is not a one-off audit — it is part of the standing
**proof-integration-watcher** axis, so "score the baseline" and "drain the
findings" are the same machine:

- The four criteria (`proof-rater-strategy-clarity`, `-goal-plausibility`,
  `-novelty`, and `proof-statement-integrity`) are registered in
  [`content/pipeline/qa-criteria-registry.ts` §PROOF](../../content/pipeline/qa-criteria-registry.ts)
  alongside the gating proof checks (`proof-lean-compiles`,
  `proof-no-bare-sorries`, `proof-no-axiom-growth`, `proof-narrative-lean-equiv`,
  `proof-no-conj-propagation-violation`, …).
- `/integration-watch proof` runs them across incoming changes **and** the
  standing corpus; `proof-integration-watcher` Slot C maps each criterion to its
  improve-skill.
- `/integration-backlog proof` drains the findings ascending-by-score into
  ≤ 49-file fix-PRs, dispatching the mapped skill per criterion:
  `proof-statement-integrity` → `lean-proof-review` (Review Type 4);
  `proof-rater-goal-plausibility` → `proof-triage` / `lean-build-fix`;
  `proof-rater-novelty` → `proposition-consolidation-audit`;
  `proof-rater-strategy-clarity` → `proof-simplifier` / `proof-conciseness`.

## Baseline coverage snapshot — 6 chapters (2026-06-07)

The first scoring pass extended past the mass-theory batch above. Verified
coverage of the four proof-rater criteria across the corpus's
proof-rater-applicable blocks (provable kinds — theorem / lemma / proposition /
corollary, plus `conjecture` for goal-plausibility — per
[`qa-criteria-registry.ts §PROOF`](../../content/pipeline/qa-criteria-registry.ts)):

| Chapter | Scored | Applicable | Coverage |
|---|---:|---:|---:|
| braids-and-knots | 20 | 23 | 87 % |
| fluid-dynamics | 20 | 27 | 74 % |
| mass-theory | 13 | 259 | 5 % |
| particle-interactions | 30 | 73 | 41 % |
| predicted-spectra | 30 | 51 | 59 % |
| quantum-observable-universes | 30 | 70 | 43 % |
| **6 chapters** | **143** | **≈ 776 corpus-wide** | **≈ 18 %** |

A further 15 chapters with proof-rater-applicable blocks are **not yet started**
(brings-surface, lifting-and-descent, mass-endomorphism, observations,
information-theory, …); 13 chapters carry no provable blocks. The three
30-block chapters hit the per-batch cap, not chapter completion.

All 143 scored blocks are **fully scored on every applicable criterion** with
band↔score consistency — no half-written or malformed entries. The partial
coverage is a stopping point, not corrupted data.

### Improve-backlog surfaced (baseline, not fixed here)

The pass recorded — but per the rate-and-improve design does **not** fix — a
substantial backlog for `/integration-backlog proof` to drain:

- **68 blocks** with `proof-statement-integrity = fail` (Lean does not faithfully
  encode the `.md` claim — `True`-stubs, weakened proxies, vacuous existence
  tautologies, unsound `Subsingleton` axioms over free real fields, duplicate
  `class` declarations).
- **99 blocks** with at least one rater score `< 0.5` (low novelty —
  refuted-categorical-interpretation residue, recorded numerical coincidences;
  low plausibility — `core` / `restates-target` gaps, axiomatised headlines).

fluid-dynamics (18 integrity fails) and the particle-interactions /
predicted-spectra axiom-and-proxy clusters are the densest backlog regions.

### Lean-library build state (inherited, not introduced here)

The QOU Lean library target is currently **red on `main`**: the PR base
(`fc2e4e4e`) fails to compile at `QOU/MathlibExt/PosSemidefTraceZero.lean`
(Mathlib API drift — `PosSemidef.sqrt` resolves to the non-existent `And.sqrt`)
and `QOU/HeckeAlgebra/Formal.lean`. Both files are **byte-identical to the base**
on this branch — the red is inherited, not caused by this PR. Consequence: the
two mass-theory Lean refinements landed here (`alpha-k` faithful `∃!`,
`beta-decay` convention alignment) are sorry-free but cannot be *build*-verified
until the inherited red clears. Fixing it needs a dedicated `lean-build-fix`
branch and is out of scope for this baseline audit; the `proof-lean-compiles`
gate for blocks downstream of those files reflects the library state, not this PR.

## Rollout (remaining corpus)

The full baseline is drained in **≤ 49-file batches** via `/integration-backlog
proof`, which now orders `proof-rater-*` by **ascending score** and re-rates
after each improver pass (the rate→improve loop). Targets are enumerated by the
needs-agent queue; each block is scored with `qa-agent-write --score`. Batches
proceed chapter-by-chapter so a mis-calibrated rubric is caught early rather
than across the whole corpus at once.

**Status:** infra + write-path fix + worked example landed; baseline scoring is
**partial** — 143 blocks across 6 chapters (≈ 18 % of ≈ 776 applicable),
surfacing the improve-backlog above (68 integrity fails + 99 low-score blocks).
Baseline scores are a *starting point* — completing coverage and raising scores
is `/integration-backlog proof`'s job, drained chapter-by-chapter.
