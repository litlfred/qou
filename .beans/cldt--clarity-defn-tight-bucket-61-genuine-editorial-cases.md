---
# cldt
title: 'Clarity EPIC: clarity-defn-tight bucket — 61 genuine editorial cases (drain deliberately, per-block rewriting)'
status: todo
type: task
priority: normal
created_at: 2026-07-12T00:55:00Z
updated_at: 2026-07-12T00:55:00Z
---

## Assessment (2026-07-12)

`definition-clarity-audit.ts clarity-defn-tight` reports **61 fails** (pass 208).
Unlike `clarity-defn-misplaced` (11/11 false positives, bean `clab`) and
`clarity-defterm-bold` (~50% checker artifacts, fixed in PR #3632), this bucket is
**genuine editorial debt** — the flags are objective structural measurements, not
term-normalization artifacts:

| reason | count (approx) | meaning |
|---|---|---|
| `rambling: N sub-sections (>=3)` | ~23 | definition block has ≥3 bold sub-headers; should be one tight statement |
| `rambling: N-word preamble (>60)` | ~20 | too much context before the actual definition |
| `rambling: N prose words (>250)` | ~18 | the definition block is over-long overall |

These are **real** "the definition rambles" cases. Draining them is **per-block
rewriting** (move the definitional statement up-front, trim preamble to the
essential setup, split multi-concept sub-sections into follow-on `remark`s,
condense prose) — with `scientific-accuracy` + `readability-editing` judgment so
no necessary mathematical setup is lost. NOT mechanical; NOT a checker fix.

## Why not drained here

Deliberately deferred: rushing 61 definition rewrites at the tail of a long session
risks dropping necessary setup from a `definition` block (worse than the rambling).
This bucket wants fresh-context, careful per-block editorial attention.

## Worst offenders (start here — longest/rambliest first)

- `def:sign-sequence-of-braid` (331-word preamble + 331 prose words)
- `def:birthday-grading` (335 words, 105-word preamble)
- `def:surreal-blowup-calculus` (122-word preamble)
- `def:categorical-mordell-weil` (252 words)
- `def:hopf-diquark`, `def:substrate-line-bundle` (≥3 sub-sections)
- (full list: run `bun run content/pipeline/definition-clarity-audit.ts --json /tmp/c.json`
  then filter `criterion==clarity-defn-tight && result==fail`)

## Definition of done

Each flagged `definition` block reads as one tight statement (defterm-bold term,
minimal setup, interpretation moved to a follow-on `remark`), re-verified
`clarity-defn-tight pass`. Route through `scientific-accuracy` (claim integrity) +
`readability-editing` (prose) per block; do NOT delete mathematical content to
satisfy the word count.
