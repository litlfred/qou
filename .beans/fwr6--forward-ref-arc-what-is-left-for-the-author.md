---
# fwr6
title: 'forward-ref arc: what is left, and why an agent should not decide it'
status: open
type: task
priority: normal
created_at: 2026-08-10T00:45:00Z
updated_at: 2026-08-10T00:45:00Z
parent: fwr1
---
Closes out the `fwr1`-`fwr5` arc. **Forward `uses[]` references went 274 -> 193**
across three PRs. Everything mechanically decidable, and everything an agent
could decide by reading, is done. What is listed here is not leftover work of
the same kind — each item is a judgement an agent should not make unilaterally,
and each is recorded with what it would take to settle it.

## 1. The 49-block vertex-factorisation chain

`mass-theory.ts` records at its own line 425 that this chain was consolidated in
from `climax-volume-mass` in May 2026 and landed mid-chapter. Three section
intros still narrate the pre-consolidation order — the chapter's opening block
says "*the previous section identified the Feynman amplitude through vertex
factorisation*" when that section now sits at 268-298.

Two viable answers: move the chain to the chapter seam, or push it back to
`climax-volume-mass` where it came from. Costed at **-3/+2**. This is a
structural decision about what the chapter is, not an ordering defect.

## 2. Seven edges that want an edit, not a move

Chasing these with reordering optimises toward a wrong fact. Two were verified
directly against the text:

- `prop:gram-determinant-plancherel-ratio` -> `rem:gram-matrix-spectral-connection`
  (497 positions) **runs backwards**. The target opens "*Remark (where the Gram
  matrix fits in the spectral-sequence / Frobenius framework)*" and itself cites
  `prop:frobenius-gram-matrix`; the source never names it.
- `prop:markov-pair-z2` -> `rem:mass-endomorphism-jet-tower` is a parenthetical
  "(cf. ...)". A "cf." is not a prerequisite.

Reported but unverified: `rem:motivic-mass-rationale` (512) should point at the
cross-chapter statement rather than the in-chapter restatement;
`prop:frobenius-s-classification` (447) at `thm:wedderburn-mass-formula`; and the
two-row definitions (149/150) want `foreshadows:` for the notational `y_lambda`.

Deletions and retargetings both need the adversarial second read `fwr1` used —
that pass overturned 3 of 35 deletions, so a single reading is not the standard.

## 3. A section title that no longer describes its contents

"Geometric face: pentagon and volume bridges" is thin on pentagons: an earlier
pass re-homed the pentagon flavours to `sec:kashiwara-jones-quantum-dilog` with
the note "*the pentagon identities belong with the quantum dilogarithm*". Rename
the section, or route the flavours back and undo that note. Both editorial.

## 4. Two near-verbatim duplications the moves exposed

Harmless at 300 positions apart, glaring adjacent:

- `vhat-pair-commutation-trace-proof.md:61-89` ("## Operator lift") against
  `pentagon-uv-commutation.md:27-46` — same quantization, same tau-hat, same
  U-V commutation relation.
- `geom-yekutieli-alignment.md:131-136` against
  `geometric-invariant-piecewise.md:76-80` — the figure-eight amphicheiral
  paragraph.

Choosing which passage survives is authorial. Note these are *consequences* of
consolidating related material, not defects the consolidation introduced — the
duplication was always there, and moving the blocks together is what made it
visible.

## 5. Prose defects the review turned up, unfixed

- `em-coupling-projection-discussion.md:57` says "See
  `prop:em-coupling-bring-zero-mode` for the repair routes". That discussion
  exists only in the target's `.ts` `authorNotes`, and the `AuthorNote` contract
  is "Default render behavior: SKIP" — the pointer sends a reader to something
  they cannot see. The routes are in `rem:alpha-em-derivation-open-problems`,
  which the same block already cites twice.
- `rem:motivic-mass-rationale` defers to "the archimedean realization functor
  **of the next subsection**". It is 21 sections and ~309 blocks away. No
  ordering fixes this without breaking the adelic dependency, because the
  functor cannot precede `def:adelic-substrate`, its own domain. The sentence is
  what is wrong.
- `rem:beta-decay-energy-scale` and `rem:energy-scale-planck` both derive
  E0 ~ 4.186 MeV from CAL-1/CAL-2 — visible duplication now that a move put them
  near each other.

## 6. The completeness question nobody has asked

513 blocks corpus-wide carry an empty `uses[]`, and `fwr5` found the pattern is
often an artefact rather than a judgement: `def:q-navier-stokes` links **eight**
prior blocks inline and declared none of them — its only entry was a single
forward reference, which was spurious. That is the `uses-editorial-completeness`
axis, and it is a much larger pass than this arc was.
