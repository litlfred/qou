---
# qou-3yel
title: UGB carries a second generation of itself — 13 blocks absent from the paper
status: todo
type: task
created_at: 2026-08-15T21:40:32Z
updated_at: 2026-08-15T21:40:32Z
---


## Measurement

`bun run --preload ./scripts/preload-registry.ts content/pipeline/block-manifest-audit.ts --orphans`

    unital-groebner-bases: chapters 1/3 in the paper, 20 blocks listed, 5 unlisted
      EXCLUDED CHAPTER  introduction        (4 blocks)
      EXCLUDED CHAPTER  buchberger-and-pbw  (4 blocks)
      unlisted block    unital-groebner-bases-chapter/leading-terms
      unlisted block    unital-groebner-bases-chapter/lemma-generator-choice
      unlisted block    unital-groebner-bases-chapter/remainder-modules
      unlisted block    unital-groebner-bases-chapter/ugb-main-theorem-proof
      unlisted block    unital-groebner-bases-chapter/unital-groebner-basis

QOU (36/36 chapters), `fred2005-formal-groups`, `bach2013-double-slit` and
`visualizer` are clean at the chapter level. UGB is the only paper that
excludes whole chapters.

## The two generations

`content/unital-groebner-bases/unital-groebner-bases.ts` lists exactly one
chapter, `unital-groebner-bases-chapter`. Everything else on disk is a
**second, self-consistent generation** of the same paper:

| live (rendered) | parallel (absent) |
|---|---|
| `leading-term-data` — `def:leading-term-data` | `leading-terms` — `def:leading-terms` |
| `generator-choice-lemma` — `lem:generator-choice` | `lemma-generator-choice` — `lem:ugb-generator-choice` |
| `remainder-module` | `remainder-modules` — `def:remainder-modules` |
| `groebner-basis` | `unital-groebner-basis` — `def:unital-groebner-basis` |
| `main-theorem-proof` — `prf:unital-groebner-decomposition` | `ugb-main-theorem-proof` — `prf:ugb-main` |
| — | `introduction/` (4), `buchberger-and-pbw/` (4) |

The parallel set is internally closed: the excluded chapters' `uses[]` point
at the unlisted blocks (`introduction/ugb-main-theorem-statement` declares
`thm:ugb-main` and uses `def:unital-groebner-basis`;
`buchberger-and-pbw/pbw-corollary` uses `thm:ugb-main`). So this reads as a
**superseded rewrite whose files were never removed**, not as damage — no live
block depends on a missing one.

Dating supports that. The parallel set is April/May
(`e0894538a7` 2026-04-25, `b3c2a20024` 2026-05-19); the live set was revised
later (`924733dec3` 2026-06-29, "split 2 multi-definienda definitions"), which
is what produced the renamed smaller blocks alongside the originals.

Diffing `main-theorem-proof.md` against `ugb-main-theorem-proof.md` confirms
the direction: the parallel copy hardcodes "Theorem 2" / "Lemma 6" and uses an
undefined `\LT` macro; the live copy names its references and uses
`\mathrm{LT}`. The live one is the later, better text.

## Why validate does not catch it

`run-validate` reports UGB `✓ Valid — 0 issue(s)`. Inclusion is a two-level
walk (paper → `chapters[]` → chapter → `sections[].blocks[]`) and validation
follows it downward, so anything not reached is simply never considered.
Nothing asserts the reverse direction — that every block on disk is reached.
`--orphans` is that assertion.

## Decision needed

1. **Delete the parallel generation** (13 blocks + 2 chapter dirs). Nothing
   live references it; the live text is the later revision. Cheapest, and
   restores "on disk == in the paper" for UGB.
2. **Re-include the excluded chapters** if the intended structure was a
   4-chapter UGB and the single-chapter manifest is the stale artifact — then
   the *live* 20-block chapter is the duplicate and the resolution runs the
   other way. Worth a moment's check before picking option 1.
3. **Park** and let `--orphans` keep reporting.

Note for whoever takes this: PR #5138 fixed the label prefix on
`ugb-main-theorem-proof` (`proof:` -> `prf:`) as a mechanical manifest repair,
before the duplicate structure was understood. That fix is on a file option 1
would delete. It is not wrong — it made an unloadable manifest load — but do
not read it as a decision that this generation is the keeper.
