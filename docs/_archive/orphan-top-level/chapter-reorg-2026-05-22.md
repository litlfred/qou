# Chapter reorganization — detailed proposal

**Status:** draft for author review (2026-05-22). Owner: repo author.
Drafted on branch `claude/eager-gauss-S36Uk` (PR #882) per session
directive. Once accepted, the implementation lands in its own
dedicated branch — this PR is intentionally not the place to execute
a paper-wide restructure of this scale.

## 0. User directive (verbatim)

> I think I want the chapter order as:
>
> 0: intro
> 1: QU
> 2: QOU
> 3: brings surface (not the whole thing but introduce the coordinates
>    systems, explain relevance and explicate ch 1 and 2 on brings.
>    this may help fix some forward referencing). then rather than put
>    all the brings content into one chapter, we provide more specific
>    results relevant to brings in the appropriate subsequent chapter.
> 4: Models of QOU. introduces the models. we also need to rename
>    Descartes universe to Archimedean universe and align language so
>    Descartes is after the archimedean functor. do this across paper.
>    will need to be thorough review.
> 5: Knots and Braids and Particles: ...

Five concrete asks underneath this directive:

- (A) Insert a new Ch 3 "Bring's surface" containing only the
  coordinate-system / relevance / first-pass narrative; leave the
  deep results in the chapters that consume them.
- (B) Rename "Descartes universe" → "Archimedean universe"
  everywhere, including the chapter directory `descartes-universe/`,
  the chapter label `chap:descartes-universe`, the Lean namespace
  `QOU.DescartesUniverse`, and 132 verbatim mentions across `.md`
  bodies (+ 633 total "Descartes" word occurrences to triage).
- (C) Align language so the Descartes specialisation is positioned
  *after* the Archimedean functor narratively — i.e. the Archimedean
  functor introduces the wall, *then* the (renamed) Archimedean
  universe lives downstream.
- (D) Lifting-and-descent (current Ch 3) does not appear in the
  proposed order 0-5. The proposal must say whether it disappears,
  merges into another chapter, or moves to the appendix.
- (E) Combine knots + braids + particles into one chapter — what
  scope, what drops, what splits.

This document proposes specifics for each.

## 1. Current chapter order (16 chapters)

| # | Dir | Sections | Blocks | Files |
|---|---|---:|---:|---:|
| 0a | `introduction` | 5 | 36 | 38 |
| 0b | `notation` | n/a | n/a | n/a |
| 1 | `quantum-universes` | 5 | 52 | 54 |
| 2 | `quantum-observable-universes` | 24 | 259 | 260 |
| 3 | `lifting-and-descent` | 11 | 122 | 128 |
| 4 | `braids-and-knots` | 49 | 554 | 593 |
| 5 | `models-of-qous` | 6 | 46 | 47 (45 after this PR) |
| 6 | `descartes-universe` | 21 | 261 | 276 |
| 7 | `particle-interactions` | 9 | 97 | 99 |
| 8 | `observations` | 17 | 158 | 163 |
| 9 | `molecular-construction` | 7 | 33 | 34 |
| 10 | `organic-chemistry` | 3 | 17 | 18 |
| 11 | `fluid-dynamics` | 7 | 66 | 67 |
| 12 | `information-theory` | 11 | 83 | 84 |
| 13 | `q-geometric-langlands` | 8 | 43 | 44 |
| — | back matter (glossary, 6 appendices, index) | — | — | — |

Distribution problem: 554 blocks in `braids-and-knots` alone (≈ 31%
of all content), and 261 + 97 + 158 = 516 blocks across the
descartes + particle-interactions + observations triple — so 60% of
the paper sits in just four chapters, while quantum-universes /
lifting-and-descent / molecular-construction / organic-chemistry /
fluid-dynamics carry the categorical foundations + applications in
~350 blocks combined.

## 2. Proposed chapter order

| # | New chapter | Source(s) | Approx. blocks | Notes |
|---|---|---|---:|---|
| 0 | Introduction | `introduction` (kept) | 36 | Unchanged. |
| 1 | Quantum universes (QU) | `quantum-universes` (kept) | 52 | Unchanged. |
| 2 | Quantum observable universes (QOU) | `quantum-observable-universes` (kept) | 259 | Unchanged. |
| 3 | **Bring's surface and coordinate systems** | NEW; pull `≈ 30` introductory blocks from current `descartes-universe` + selective lifts from current Ch 2 (`quantum-observable-universes/brings-*`) | ~30-40 | First-pass narrative only; deep results stay in downstream chapters. See §5. |
| 4 | Models of QOUs | `models-of-qous` (kept; renamed inline language as needed) | 45 | Introduces the models including the renamed Archimedean universe. |
| 5 | **Knots, braids, and particles** | merge of `braids-and-knots` + `particle-interactions` + parts of `descartes-universe` | ~700 (too large — see §6) | Combined per directive (E). Requires internal section restructure to stay readable. |
| 6 | Archimedean universe | renamed from `descartes-universe/` after removing the Bring's-surface intro material that becomes new Ch 3 | ~220 | Survives as the deep specialisation chapter; renamed everywhere. |
| 7 | Observations | `observations` (kept) | 158 | Unchanged location. |
| 8 | Molecular construction | `molecular-construction` (kept) | 33 | Unchanged location. |
| 9 | Organic chemistry | `organic-chemistry` (kept) | 17 | Unchanged location. |
| 10 | Fluid dynamics | `fluid-dynamics` (kept) | 66 | Unchanged location. |
| 11 | Information theory | `information-theory` (kept) | 83 | Unchanged location. |
| 12 | q-Geometric Langlands | `q-geometric-langlands` (kept) | 43 | Unchanged location. |
| — | back matter | unchanged | — | Including `lifting-and-descent` — see §3. |

### Drops from interior to appendix

The user's enumerated order goes 0-5 and then "...", so chapters
6-12 above are my proposed extrapolation. The notable change is
that **`lifting-and-descent` does not appear at its current position**
(current Ch 3). I propose moving it to the **appendix** as
`appendix-lifting-and-descent`. Reason: it's 122 blocks of pure
Yekutieli-tower machinery that the main narrative consumes but
rarely needs to *expose*; pushing it to the appendix is consistent
with the proposed mental model where Ch 3 = "Bring's coordinate
intuition", not "tower machinery". Alternative: keep it as a
final main-text chapter under "machinery", before back matter.
**Decision needed (see §10 Question 1).**

## 3. The "Descartes → Archimedean" rename — scope assessment

This is the biggest sub-task. Estimated total footprint:

| Target | Count | Mechanical? |
|---|---:|---|
| `chap:descartes-universe` label | 1 declaration + 22 cross-refs in `.md` | yes — sed |
| `descartes-universe/` directory name | 1 (with 276 nested files) | yes — `git mv` + manifest update |
| `descartes-universe.ts` chapter manifest filename | 1 | yes — `git mv` |
| `qou:QOU.DescartesUniverse.*` lean-ref URIs in `.ts` manifests | 125 | yes — sed |
| `QOU/DescartesUniverse/` Lean directory | 1 (with 94 `.lean` files) | yes — `git mv` + import-path rewrites |
| `import QOU.DescartesUniverse` statements in Lean files | unknown (≥ 2 just from the spot check) | yes — sed across `*.lean` |
| `qou:QOU.Descartes*` (other Descartes-prefixed namespace, e.g. `QOU.Descartes/PauliWitness`) | 1 | yes — `git mv` + sed |
| Verbatim "Descartes universe" in `.md` prose | 132 | semi — many but mechanical |
| Generic "Descartes" mentions in `.md` prose | 633 (less the 132 above) | **manual review** — many refer to *René Descartes* (the philosopher / Cartesian coordinates) and must NOT be renamed |
| Glossary entries | 1 in `glossary.json` | yes — regenerated by build |
| Bibliography references | unknown — check `references.ts` for Descartes-authored entries | manual |

The mechanical changes are straightforward. The 501 generic
"Descartes" mentions (633 − 132) are the risk: many of them
correctly reference *René Descartes* / *Cartesian coordinates* /
*Cartesian product* and must be preserved. A find-and-replace
without context review would corrupt those references.

**Recommended approach.** Two-pass:

1. **Pass 1 (mechanical).** Rename the directory, the chapter
   label, the Lean namespace, the lean-ref URIs, and the 132
   verbatim "Descartes universe" mentions. Single commit per
   target type. ~6 commits.
2. **Pass 2 (manual).** Hand-review the remaining 501 generic
   "Descartes" mentions, flagging which are the renamed concept
   (rewrite) vs the philosopher / coordinate system (keep). Likely
   ≥ 30 blocks affected. One commit per chapter touched. ~10-15
   commits.

Total: ~16-21 commits, single branch
`claude/descartes-archimedean-rename-2026-05-XX`, opened as a
separate PR from #882. Estimated wall-clock 4-6 hours.

## 4. Narrative repositioning — "Descartes after the Archimedean functor"

User directive (C). The current organisation is:

```
Ch 4 (braids-and-knots) ─── derives the Hecke / Markov machinery
Ch 5 (models-of-qous) ─── introduces the Archimedean functor (sec:archimedean-realisations-and-wall after this PR)
Ch 6 (descartes-universe) ─── specialises to Bring's surface, χ = −6
```

The directive aligns content with this flow: Archimedean functor
narrative *precedes* the renamed Archimedean-universe chapter.
After the rename and the new Ch 3 split (see §5), the order is:

```
Ch 3 (Bring's surface) ─── coordinate intuition only
Ch 4 (Models of QOUs) ─── Archimedean functor + the wall (already done by this PR)
Ch 5 (Knots, braids, particles) ─── unchanged ordering of derivation
Ch 6 (Archimedean universe) ─── deep specialisation, downstream of Ch 4
```

Implementation steps under (4):

1. The current `descartes-universe/intro.md` opens with "the
   Descartes universe" without first sketching how it relates to
   the Archimedean functor's wall. Rewrite the intro to:
   - Reference the (renamed) Archimedean functor from `models-of-qous/`.
   - State explicitly that this chapter is the
     "deep specialisation downstream of the functor" — not a
     parallel construction.
2. Audit cross-references in `descartes-universe/` for forward
   references back to `braids-and-knots`. The detangler-no-forward-
   ref axis currently flags 63 blocks chapter-wide; some fraction
   will be in `descartes-universe`. Resolve by moving the
   referenced content into the new Ch 3 (Bring's coordinates)
   when the reference is to coordinate-system facts; otherwise
   accept the forward ref or refactor.

## 5. The new Ch 3 — Bring's surface (proposal)

User directive (A). Content to populate the new chapter, drawn
from:

| Source | Blocks (approx.) | Stays / moves |
|---|---:|---|
| `descartes-universe/brings-*` (Bring's surface intro material) | ~12-18 | move to new Ch 3 |
| `descartes-universe/coord-*` and similar coordinate-system intros | ~8-10 | move to new Ch 3 |
| `quantum-observable-universes/brings-geometric-connection.md` and ~11 sibling Brings blocks | ~12 | partially move (the introductory subset) |
| Selected `lifting-and-descent` blocks that explain coordinate systems | ~3-5 | move if applicable |

**Filter rule** for what moves vs stays:

- *Moves to new Ch 3* if the block introduces a coordinate system,
  states a basic property of Bring's surface, or relates Bring's
  to the χ = −6 genus calculation at an introductory level.
- *Stays in current chapter* if the block proves a specific result
  *about* Bring's surface (e.g. recursive corner formulas, mass
  predictions, knot-table embeddings) — these are "applications"
  and belong with their consumers.

Estimated new Ch 3: ~30-40 blocks across 4-6 sections. Within the
detangler band (3-18) per section.

**Expected forward-reference improvement.** Currently, 121 of 276
`descartes-universe/` blocks reference Bring's surface; if the
intro 30-40 move out, the downstream consumers in
`braids-and-knots`, `observations`, etc. stop emitting forward
references to `descartes-universe` for coordinate facts (they
reference the new Ch 3 instead, which sits earlier).

## 6. The merged Ch 5 — "Knots, braids, and particles"

User directive (E). The naïve merge produces a 554 + 97 + (parts of
261) ≈ 700+ block chapter, which is structurally unmanageable —
the existing `braids-and-knots` already triggers TOC clutter at 554
blocks (the renderer fix in commit `2dbd50e6` partially addresses
the symptom; the underlying volume is unchanged).

**Recommended path:** treat the merger as a *narrative* change,
not a *file-system* change. Keep two directories (`braids-and-knots`
and `particle-interactions`), but render them as one chapter via a
new `chapterRef` aggregator OR by treating one directory as a
sub-chapter of the other.

The build pipeline's `chapterRef` mechanism currently maps 1 dir →
1 chapter. Extending it to support N dirs → 1 chapter ("sub-chapter
mode") is a real change to `content/pipeline/build.ts` and
`folio/schema/builders.ts`. **Decision needed (§10 Question 2):**

- **Option E1.** Merge file-system-wise (`git mv particle-interactions/*
  braids-and-knots/`). Renames are flat; cross-refs need
  updating; the chapter directory grows to ~700 files.
- **Option E2.** Add sub-chapter capability to the build pipeline
  and stitch braids-and-knots + particle-interactions under one
  chapter heading. ~1 day of pipeline work.
- **Option E3.** Keep them as two adjacent chapters with a
  shared narrative banner ("Part II: Knots, braids, and
  particles"), no merge. Simplest.

I recommend **E3** as the first iteration; revisit E2 if Part II
banner doesn't read coherently after the rename + Ch 3 split.

## 7. Forward-reference impact

The detangler-no-forward-ref axis currently has 63 stale/missing
findings (per `qa-staleness.ts` on this branch). Two of the
proposed moves materially affect them:

- The new Ch 3 (Bring's surface intro) **reduces** forward refs
  from `braids-and-knots` and earlier chapters into
  `descartes-universe` for coordinate facts.
- The Archimedean-universe rename **does not change** forward-ref
  topology — labels stay the same after the rename, only the
  display name changes.

After the proposed reorg lands, re-run `qa-sweep --only
detangler-no-forward-ref` to verify. Expected: open count drops by
20-40 findings (the coordinate-system forward refs are typically
the simplest to resolve by moving the target earlier).

## 8. Risk + sequencing

Recommended commit/PR sequence (each on its own branch):

1. **PR-R1.** Mechanical Descartes → Archimedean rename: directory,
   chapter label, Lean namespace, lean-ref URIs, 132 verbatim
   "Descartes universe" → "Archimedean universe" prose changes.
   No semantic changes; CI must stay green. **Reviewer cost: low**
   (mechanical sed-style diff).
2. **PR-R2.** Manual review of remaining 501 "Descartes" mentions
   to distinguish Cartesian / philosopher / coordinate-system
   uses from the renamed concept. Per-chapter commits.
3. **PR-R3.** Extract the Bring's-surface intro into a new `bring-
   coordinates/` directory; add the chapterRef to the paper
   manifest in position 3; move ~30-40 blocks. Update cross-refs.
4. **PR-R4.** Narrative repositioning of Descartes-becomes-
   Archimedean chapter to "downstream of the functor": rewrite
   intros, dissolve forward refs.
5. **PR-R5 (optional).** Knots/braids/particles merger (E3 banner
   approach OR E2 sub-chapter approach pending Question 2 answer).

PR-R1 is the highest-value lowest-risk lead. The 1921 voice/QA
sidecars on this branch already cover the renamed paths after the
rename lands (the `script-sidecars/*.script.json` keys are by
criterion ID, not file path).

## 9. What this proposal does NOT cover

- Detailed block-by-block manifest for the new Ch 3 (proposal §5
  gives the rule; the actual filter requires reading each Bring's-
  surface block).
- Renaming the `references.bib` entries authored by *René
  Descartes* — they should stay as-is, but a final QA pass should
  confirm no false-positive renames.
- Bibliography / glossary regeneration after the rename — handled
  by existing `bun run export-bibtex` + `bun run build-glossary`
  flows.
- Whether the deprecated `chap:descartes-universe` label gets a
  redirect for external citations (e.g. on `gh-pages`). Likely yes;
  see §10 Question 3.

## 10. Questions for the author

1. **`lifting-and-descent` placement.** Move to appendix
   (`appendix-lifting-and-descent`), keep at end of main text as
   final machinery chapter before back matter, or keep at its
   current position (Ch 3 in the *current* order, displaced to
   later in the *new* order)?
2. **Knots/braids/particles merger.** E1 (file-system merge), E2
   (sub-chapter pipeline change), or E3 (Part II banner, no merge)?
   I recommend E3.
3. **Old chap label redirect.** Should the gh-pages viewer keep a
   stub at `/chap:descartes-universe` redirecting to the new
   `chap:archimedean-universe`? Cost: ~10 LoC in the viewer
   router.
4. **"Archimedean universe" — exact phrase.** The renamed concept
   could be "Archimedean universe", "archimedean universe"
   (lowercase per `Archimedean realisations`), "the archimedean
   specialisation", or another phrasing. Pick the canonical form
   so downstream content uses it consistently. Recommendation:
   **"Archimedean universe"** (capitalised "A" matching the
   current notation register's bold-A convention for the
   archimedean side of the wall).

## 11. Out of scope for this proposal

- Migrating sibling papers (`unital-groebner-bases`,
  `fred2005-formal-groups`) — no scope overlap.
- Re-numbering theorems / propositions inside chapters — those
  use `[section]` counters and re-flow automatically.
- The 1921-block agent-only one-voice backlog drain — already
  scoped as a separate follow-up (see PR #882 description).
