---
# fwr7
title: 'retarget the seven edges that want an edit, not a move'
status: completed
type: task
priority: normal
created_at: 2026-08-10T01:25:00Z
updated_at: 2026-08-10T02:55:00Z
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

---

**Outcome: no edits. All eight edges keep, on independent unanimous readings.**

Two readers took all eight edges in parallel without seeing each other's
verdicts. Both returned **8 keep, 0 delete, 0 retarget, 0 foreshadow**, agreeing
row for row, and — this is the part that matters — each refuted the proposals
with **positive evidence of a lean**, not by falling back on the "when in doubt,
keep" tie-break.

**The premise of this bean was wrong.** Seven edges were held back from the arc
on the grounds that "the edge is wrong, not the ordering". Reading says the edges
are right.

**Including the two I claimed to have verified myself.** Both of my
verifications were `.md`-only keyword searches, which is precisely the failure
mode this repo's own skill warns about, and which overturned a deletion earlier
in the same arc:

- `prop:gram-determinant-plancherel-ratio` -> `rem:gram-matrix-spectral-connection`.
  I reported "the source never names it". The source's **extracted proof child**
  cites the target by label for the exact identity the boxed formula is built
  from, and that proof block declares no `uses[]` of its own — so this entry is
  the sole declaration of the dependency. Deleting it would have removed the only
  record of a real lean.
- `prop:markov-pair-z2` -> `rem:mass-endomorphism-jet-tower`. I reported "a cf.
  is not a prerequisite". True as a rule, false here: the cf. carries the
  sentence's only non-trivial claim, and the target's extracted table child *is*
  the empirically-verified all-pairs set on atoms A >= 6 that the cf. points at.

The other six:

| edge | proposed | why it failed |
|---|---|---|
| `rem:motivic-mass-rationale` -> `prop:mass-endomorphism-tower` | retarget to "the cross-chapter statement" | **No such block exists.** Exactly one manifest in the corpus carries that label, and the source's first sentence links it inline under its own title. |
| `prop:frobenius-s-classification` -> `prop:confined-knot-binding` | retarget to `thm:wedderburn-mass-formula` | The retarget's *second* half is true and its first half is false: the theorem is genuinely leaned on and genuinely missing, but the current target supplies the notation the source runs on (W_sym/std/alt, chi^sym/alt, the transfer form) and the theorem supplies none of it. That is a **completeness** finding, not a swap. |
| `def:two-row-stratum` -> `prop:wedderburn-weight-canonical` | foreshadow | No deferral aimed at the target; the source never names it. Its one hand-off points at a different block. |
| `def:two-row-projection` -> `prop:wedderburn-weight-canonical` | foreshadow | "where y_lambda is the Wenzl weight from [target]" is a bare attribution — the skill's canonical non-deferral. |
| `conj:gs-spectral-decomposition-existence` -> `thm:knot-mass-formula-unified` | unspecified | It wants an **ordering** fix, not an edge edit: the conjecture re-decomposes the target's own quantity, reusing its m, its T_w and its term "descended". |
| `prop:rigid-monoidal-structural-gap-invariance` -> `prop:spin-involution-lp-dual-invariance` | never adjudicated | The source states the target's conclusion verbatim and reasons onward from it. Consuming a result is the opposite of deferring to it. Clean keep on a first reading. |

**Two real findings survive, both for other axes:**

1. `prop:frobenius-s-classification` is missing `thm:wedderburn-mass-formula`
   from `uses[]` — it names it in sentence one. That is
   `uses-editorial-completeness`, the axis `fwr5` opened.
2. `def:two-row-projection` carries a transitive-redundancy hygiene warn via
   `def:two-row-stratum`. Tidiness; the graph is correct, just not minimal.

**Process note, mine to own:** I branched for `fwr6` while both readers were
mid-run, switching the shared worktree under them. Both noticed, diffed every
file they had read across the two branches, and confirmed the drift was harmless
before reporting. It was luck that it was harmless — a shared worktree is not a
safe place to change branches while agents are reading it.
