# Paper voice: audit and agent commentary in Chapters 1–2

**Date:** 2026-10-11. **Scope:** Chapter 1 `quantum-universes` (62 blocks) and
Chapter 2 `quantum-observable-universes` (314 blocks), the first two chapters
after the Introduction in `quantum-observable-universe.ts`.

**Rule (owner, 2026-10-11).** Paper prose carries mathematics and, at the
comparison points, physics. It does not carry audit commentary (dated
corrections, "measured …", "corrected", "retracted", bean IDs, PR numbers,
staleness or precision-gate notes, provenance stories, formalisation
bookkeeping) or agent-discussion commentary ("an agent found", "this session",
"we tried X", the corpus narrating its own history). An open conjecture may
carry one brief scholarly remark on its status and possible routes.

## Method

1. Six readers read all 376 blocks in full and classified each passage.
2. A keyword grep found almost nothing (4 weak hits), so detection had to be
   by reading. The new detector `folio/pipeline/paper-commentary-audit.ts`
   was written from the reader findings, then run back over the pre-edit tree.
3. No number and no mathematical claim was changed. Commentary was moved to the
   block's `authorNotes` (AGENTS.md §4d), cut to a brief status remark, or
   deleted.

## What changed

| chapter | block | passage | action |
|---|---|---|---|
| 1 | `quantum-universe-axiom-motivation` | "in the loosest terms that are still honest" | deleted |
| 1 | `quantum-universe-axiom-motivation` | "This axiom is what earlier drafts asserted, less directly, as a numerical identity." | deleted |
| 2 | `categorical-self-duality` | "The Lean backing … does not carry it … not formalised." | moved to `authorNotes` |
| 2 | `dilog-pentagon-is-associator` | ", sorry-free" | moved to `authorNotes` |
| 2 | `dilog-pentagon-is-associator` | "sorry-free and axiom-free (`#print axioms` …) … not a self-assuming projection" | moved to `authorNotes` |
| 2 | `dilog-pentagon-is-associator` | scope boundary: "genuinely open … pending shuffle-Hopf infrastructure absent from Mathlib … honest conjecture class" | cut to a brief scope remark; details to `authorNotes` |
| 2 | `quantum-observable-universe` | "Earlier statements of this definition wrote …" | reworded neutrally; history to `authorNotes` |
| 2 | `quantum-observable-universe` | backticked path `lean/QOU/BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean` | path moved to `authorNotes`; declaration names kept |
| 2 | `su2-emergence` | "an earlier formulation derived 'which subgroup' …" | moved to `authorNotes` |
| 2 | `su2-emergence` | "sorry-free", "previously proved" in the Lean-structure note | moved to `authorNotes` |
| 2 | `frobenius-hopf-substrate` | paragraph "An earlier version of this definition opened …" | moved to `authorNotes` |
| 2 | `q-dilogarithm-pentagon-associator` | "not formalised … cited rather than machine-checked … conjecture class" | cut to a brief status remark; status to `authorNotes` |
| 2 | `g-action-on-substrate` (conjecture) | subsection "What rests on this residual" pointing at an audit-flag ledger | folded into the conjecture's existing one-sentence status remark |
| 2 | `g-action-on-substrate-table3-data` | the whole table: an audit-flag ledger (`current` / `post-discharge` columns) | block removed from the paper; content recorded below |

**Counts.** Chapter 1: 0 moved, 0 cut, 2 deleted (1 block). Chapter 2: 9
moved, 3 cut, 0 deleted, 1 table block removed (7 blocks).

### Relocated: the `g-action-on-substrate` audit-flag ledger

Formerly `tbl:g-action-on-substrate-table3-data`, rendered in the paper:

| flag | current | post-discharge |
|------|---------|----------------|
| non-vanishing | inconclusive | closed via this trace formula + corrected residual |
| HIGGS-SLOT | retraction | Higgs scalar slot identified as residual of $A^{(H)}$ |
| U2 (force-carrier dichotomy) | premise | derived from G-1 |
| U4 (EW mass eigenstate count) | premise | derived from G-1 (3 broken + 1 scalar) |
| categorical Higgs idempotent | sketch | explicit construction (G-4) |
| §3.A v4 calibration | wrong direction | calibrated via Higgs trace |

## Left in place (borderline, for author review)

These read as scholarly scope statements and were not changed:

- `braiding-eigenvalue-extraction-novelty`: "A derivation of $q_0$ from the
  substrate is not claimed here and is not part of the framework." (advisory hit)
- `q-dilogarithm-pentagon-associator` §"The observable is a pairing": "…that
  datum is genuinely resurgent and remains open." (advisory hit)
- `hochschild-homology`, `su2-characters-and-quantum-dimension`,
  `chern-character`: sentences naming the Lean declarations that state a
  result ("the Lean sibling proves …"). Naming the formal statement is allowed;
  grading it is not.
- `q-exponential-unique`, `q-logarithm-unique` and their proofs: "stated as a
  hypothesis rather than discharged" — brief, scholarly.
- `quantum-universe` (the `IsQGeneric` paragraph), `tannaka-krein-overview`
  ("CAL-2"), `braiding-induced-ordering-proof` (novelty claim),
  `categorical-q-ext-deriv-unique` (an "Archimedean specialisation" template
  paragraph with nothing archimedean after it), `germ-commutator-q-curvature`
  ("narrative bridge").

## Found while reading, outside this rule

- `q-dilogarithm-pentagon-associator` says the pentagon has "exactly one
  level-2 primitive", while `q-dilogarithm-unique` makes uniqueness conditional
  on rigidity.
- `q-logarithm-unique` line 9 describes the logarithm's rigidity with the
  exponential's $D_q$ flow condition.
- `su2-emergence-volume-determinant-proof` still uses the weak "non-degenerate
  epimorphism" reading that `quantum-observable-universe` now explains is
  insufficient.
- Chapter numbering disagrees: `quantum-universe-intro` vs
  `quantum-universes-intro` ("Chapter 2" and "Chapter 3"); 
  `quantum-universe-axiom-motivation` refers to "Chapter 9".

## Why the existing QA missed it

The platform's voice checkers (`qa-checkers-voice.ts` in folio-assistant) key
on blockquote banners (`> **Status …**`), PR numbers and commit SHAs, ISO
dates, model names, and a short list of agent words ("wired in", "flip-flop").
Run directly on the nine pre-edit blocks, the 13 `voice-*` checkers failed none
of them on any of these passages (the single hit was an unrelated `→` glyph).
The passages here use none of those forms: they are inline sentences such as
"earlier drafts asserted", "sorry-free", "not formalised", "absent from
Mathlib", or a backticked repository path. `voice-author-notes-pollution` P4
also explicitly exempts "measured … <date>", which is exactly a provenance
story. A re-run of the existing QA would therefore not have found them.

## The new check

`folio/pipeline/paper-commentary-audit.ts` (guard:
`paper-commentary-audit.test.ts`, 10 tests). Criteria:
`commentary-formal-status`, `commentary-corpus-history`, `commentary-repo-ref`,
`commentary-provenance`, `commentary-agent` (failing);
`commentary-witness-ref` (advisory); `commentary-open-status` (silent in a
conjecture context up to 3 sentences, advisory elsewhere, failing beyond 3).

- Chapters 1–2 before the edits: **9 of 376** blocks fail, one per edited block.
- After: **0 of 375** fail, 2 advisory.
- Whole corpus: **240 of 3634** blocks fail, 112 advisory-only. A random sample
  of 14 hits (taken before witness pointers were made advisory) found 13 real
  commentary passages: migration stories, PR numbers, "proved sorry-free in …",
  provenance. Those blocks are outside this tranche and were not edited.
