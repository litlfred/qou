---
# qou-3yel
title: UGB carries a second generation of itself — 13 blocks absent from the paper
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T21:40:32Z
updated_at: 2026-08-21T15:16:59Z
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

## CORRECTION 2026-08-21 — born orphaned, not superseded

The section above says the parallel set "reads as a superseded rewrite
whose files were never removed". **That mechanism is wrong**, and the
difference matters for the disposition.

Traced the manifest's whole history. `chapters:` has named exactly one
directory at every commit since the original import:

    968d503c3e  2026-03-25  chapterRef({ dir: "ch1-unital-groebner-bases" })
    4239de9d0d  2026-04-06  chapterRef({ dir: "unital-groebner-bases-chapter" })

`4239de9d0d` is a **pure rename** — every path in it is `R100`
(100 % similarity): `ch0-introduction/` → `introduction/`,
`ch1-unital-groebner-bases/` → `unital-groebner-bases-chapter/`,
`ch2-buchberger-and-pbw/` → `buchberger-and-pbw/`. It renamed the
directories and updated the one `chapterRef` to match. It did not drop a
chapter.

So the import of Leitner–Pawloski 2004 laid down a **three-chapter**
directory structure and wired only `ch1`, which is itself a self-complete
monolith carrying its own introduction and its own Buchberger/PBW
material. `ch0` and `ch2` have been unreferenced since the day they
landed. Nothing superseded them because nothing ever included them.

**What this changes.** Dating cannot adjudicate which generation is
canonical — both were written at once, by the same import. My earlier
argument leaned on the live set being "the later revision"; between the
*chapters* that is simply false. (The separate finding about the five
unlisted blocks INSIDE the included chapter still stands on its own
evidence: there the live `main-theorem-proof` names its references and
uses `\mathrm{LT}`, while the unlisted `ugb-main-theorem-proof` hardcodes
"Theorem 2" and uses an undefined `\LT`.)

**Disposition, unchanged in substance but now for the right reason.**
Still an author call, and still not urgent: the paper renders correctly
from the monolith, and nothing live depends on the orphans. The question
is editorial — whether UGB should present as one chapter or three — and
the corpus holds both drafts of that decision from the same day. I am not
deleting an imported paper's alternate chapter structure on my own
judgement, and there is no defect forcing the choice.
