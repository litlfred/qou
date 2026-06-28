# Definition / statement clarity audit — 2026-06-28

Scanner: [`content/pipeline/definition-clarity-audit.ts`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/pipeline/definition-clarity-audit.ts). Skill: [`local/definition-clarity-audit`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/.claude/skills/local/definition-clarity-audit.md).

High-recall heuristic candidates — a `fail` is a candidate the `definition-clarity-audit` skill confirms, not a verdict.

## Summary

Lead with the **major** column — those are the high-confidence
candidates. `minor` candidates (e.g. an unbolded term, a slightly
over-length statement) are cheaper, lower-stakes fixes.

| Criterion | pass | fail · major | fail · minor | n/a |
|---|--:|--:|--:|--:|
| `clarity-defterm-bold` | 0 | 0 | 0 | 0 |
| `clarity-defn-single` | 0 | 0 | 0 | 0 |
| `clarity-defn-tight` | 0 | 0 | 0 | 0 |
| `clarity-stmt-tight` | 0 | 0 | 0 | 0 |
| `clarity-stmt-pure` | 0 | 0 | 0 | 0 |
| `clarity-grad-style` | 0 | 0 | 0 | 0 |
| `clarity-rhetorical-header` | 0 | 0 | 0 | 0 |
| `clarity-defn-misplaced` | 0 | 0 | 0 | 0 |
| `clarity-remark-single-topic` | 0 | 0 | 0 | 0 |
| `clarity-remark-embeds-statement` | 667 | 3 | 14 | 0 |

Blocks scanned: **684**. Total candidate fails: **17**.

## `clarity-defterm-bold` — 0 candidate(s)

_No candidates._

## `clarity-defn-single` — 0 candidate(s)

_No candidates._

## `clarity-defn-tight` — 0 candidate(s)

_No candidates._

## `clarity-stmt-tight` — 0 candidate(s)

_No candidates._

## `clarity-stmt-pure` — 0 candidate(s)

_No candidates._

## `clarity-grad-style` — 0 candidate(s)

_No candidates._

## `clarity-rhetorical-header` — 0 candidate(s)

_No candidates._

## `clarity-defn-misplaced` — 0 candidate(s)

_No candidates._

## `clarity-remark-single-topic` — 0 candidate(s)

_No candidates._

## `clarity-remark-embeds-statement` — 17 candidate(s)

| block | sev | evidence | metrics |
|---|---|---|---|
| [`rem:bar-involution-properties`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/braids-and-knots/bar-involution-properties.md) | major | remark embeds formal content: 27 embedded statement-labels (17×proposition, 10×theorem) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=27, proofSection=0 |
| [`rem:F3-eps6-leading-eq-neg-2b-cubed`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/stochastic-mechanics/F3-eps6-leading-eq-neg-2b-cubed.md) | major | remark embeds formal content: a `## Proof(s)` catalog — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=0, proofSection=1 |
| [`rem:alpha-em-derivation-exploration-options`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/predicted-spectra/alpha-em-derivation-exploration-options.md) | major | remark embeds formal content: 4 embedded statement-labels (4×claim) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=4, proofSection=0 |
| [`rem:fivefold-symmetry`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/brings-surface/fivefold-symmetry.md) | minor | remark embeds formal content: 1 embedded statement-label (1×theorem) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:shell-threading-energy`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/shell-threading-conjecture.md) | minor | remark embeds formal content: 1 embedded statement-label (1×conjecture) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:cfs-comparison-summary`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/cfs-comparison-summary.md) | minor | remark embeds formal content: 1 embedded statement-label (1×corollary) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:qou-obstruction-reduction-interpretation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/stochastic-mechanics/qou-obstruction-reduction-interpretation.md) | minor | remark embeds formal content: 1 embedded statement-label (1×corollary) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:aeon-boundary-generates-chart`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/information-theory/aeon-boundary-generates-chart.md) | minor | remark embeds formal content: 1 embedded statement-label (1×conjecture) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:reeb-contact-universal-computer`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/quantum-observable-universes/reeb-contact-universal-computer.md) | minor | remark embeds formal content: 1 embedded statement-label (1×corollary) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:phi-q-tower-jsj-bridge`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/mass-theory/phi-q-tower-jsj-bridge.md) | minor | remark embeds formal content: 1 embedded statement-label (1×conjecture) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:phi-d-syt-count-conjecture`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/mass-endomorphism/phi-d-syt-count-conjecture.md) | minor | remark embeds formal content: 1 embedded statement-label (1×conjecture) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:em-coupling-chern-simons`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.md) | minor | remark embeds formal content: 1 embedded statement-label (1×conjecture) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:elliptic-stability-locus`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/predicted-spectra/elliptic-stability-locus.md) | minor | remark embeds formal content: 1 embedded statement-label (1×conjecture) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:Q-value-transition-properties`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/predicted-spectra/q-value-transition-properties.md) | minor | remark embeds formal content: 1 embedded statement-label (1×corollary) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:skein-shell-correction`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/predicted-spectra/skein-shell-correction.md) | minor | remark embeds formal content: 1 embedded statement-label (1×conjecture) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=1, proofSection=0 |
| [`rem:periodic-table-demand`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/particle-interactions/periodic-table-demand-conjecture.md) | minor | remark embeds formal content: 2 embedded statement-labels (2×conjecture) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=2, proofSection=0 |
| [`rem:q-holonomy-locality-derivation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/particle-interactions/q-holonomy-locality-derivation.md) | minor | remark embeds formal content: 2 embedded statement-labels (1×theorem, 1×claim) — promote each to its own `proposition`/`theorem`/`lemma` block (with Lean sibling); keep the remark interpretive | embeddedStatements=2, proofSection=0 |

