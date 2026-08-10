---
# fwr7
title: 'retarget the seven edges that want an edit, not a move'
status: in-progress
type: task
priority: normal
created_at: 2026-08-10T01:25:00Z
updated_at: 2026-08-10T01:25:00Z
parent: fwr6
---
Branch: `claude/fwr7-edge-retargeting-2026-08-10`.

`fwr6` item 2 and item 5. The forward-ref arc took the paper 274 -> 192 by
adjudicating edges and moving blocks. Seven edges were deliberately left alone
because **reordering is the wrong instrument for them** — the edge itself is
wrong, and moving blocks to satisfy it optimises toward a wrong fact.

Two were verified directly against the text during the arc:

- `prop:gram-determinant-plancherel-ratio` -> `rem:gram-matrix-spectral-connection`
  (497 positions) runs backwards. The target opens *"Remark (where the Gram
  matrix fits in the spectral-sequence / Frobenius framework)"* and itself cites
  `prop:frobenius-gram-matrix`; the source never names it.
- `prop:markov-pair-z2` -> `rem:mass-endomorphism-jet-tower` is a parenthetical
  "(cf. ...)". A "cf." is not a prerequisite.

Five were reported by a reader but never verified: `rem:motivic-mass-rationale`
(512) should point at the cross-chapter statement rather than the in-chapter
restatement; `prop:frobenius-s-classification` (447) at
`thm:wedderburn-mass-formula`; the two-row definitions (149/150) want
`foreshadows:` for the notational `y_lambda`; and
`conj:gs-spectral-decomposition-existence` -> `thm:knot-mass-formula-unified`.

**Standard of evidence.** `fwr1`'s adversarial pass overturned 3 of 35 deletions
and 17 of 23 foreshadow declarations, so one reading is not the standard here
either — every deletion and every retarget gets a second reader briefed to
refute it. A *retarget* is two claims at once (this edge is wrong AND that one
is right), so it carries the burden of both a deletion and an addition.

Also in scope, from `fwr6` item 5 — three prose defects the review traced but
did not fix:

- `em-coupling-projection-discussion.md:57` points at "repair routes" that live
  only in an `authorNotes` field the `AuthorNote` contract renders as SKIP.
- `rem:motivic-mass-rationale` defers to a functor "of the next subsection"
  that is 21 sections away, and no ordering fixes it — the functor cannot
  precede `def:adelic-substrate`, its own domain.
- `rem:beta-decay-energy-scale` and `rem:energy-scale-planck` both derive
  E0 ~ 4.186 MeV from CAL-1/CAL-2, now visibly adjacent.
