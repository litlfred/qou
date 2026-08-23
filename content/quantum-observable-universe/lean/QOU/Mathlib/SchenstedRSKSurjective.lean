import QOU.Mathlib.SchenstedReinsertRow
import QOU.Mathlib.SchenstedRecordingTrunc

/-!
# QOU.Mathlib.SchenstedRSKSurjective — every standard pair is hit

Brick 32 of epic `qou-nrex` (RSK inverse), and the point the P and Q sides meet.

**`insertWordRec_uninsertSteps_of_standard`** — for a pair `(P, Q)` of the right shape, the word the
reverse cascade recovers from `P` at `Q`'s positions has `insertWordRec w = (P, Q)`: not merely the
right insertion tableau, but the right recording tableau too.

The three inputs, each proved elsewhere:

* `insertWord_uninsertSteps_of_standard` (brick 27) — the recovered word's insertion tableau is `P`;
* `rowIndices_uninsertSteps` (brick 29) — the recovered word's row-index record is the position list
  it was recovered from;
* `qAppendSteps_qPositions_self` (brick 31) — replaying that position list rebuilds `Q`,

joined by brick 4's identification of the recording tableau with the record of `rowIndices`. The
second is the one that was missing: without it the recovered word's recording tableau is
unconstrained, and "the insertion tableau came out right" says nothing about `Q`.

## What the hypotheses say

`hrange` and `hlt` together say `Q`'s entries are exactly `0, …, n-1`; with `hQstrict`, `hQc` and
`hQnd` that is standardness. `hshape` says `P` has the shape those positions build — the pair is a
*pair*, not two unrelated tableaux.

## Scope

Surjectivity of `rskPair` onto standard pairs of a common shape, at the level of this
representation. It is **not** bijectivity: injectivity is `SchenstedRSKInjective`, and combining
them into a bijection — with the shape and standardness conditions matched to whatever `rskPair`'s
codomain is — is the next brick. `RSKBurnsideHolds` for general `n` remains open; it is proved only
for `n ≤ 12`, by the unrelated `rskBurnsideHolds_le12` route with no RSK correspondence in it.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

/-- **A run that empties the shape empties the tableau.** `tableauShape` is a `map`, so it preserves
length, and a tableau of empty shape is empty. -/
theorem uninsertSteps_fst_eq_nil {T : List (List ℕ)} {is : List ℕ}
    (hs : RowsSorted T) (hc : ColStrict T) (hne : NoEmptyRows T)
    (hsca : ShapeCornersAlong (tableauShape T) is)
    (hempty : removeCornerSteps (tableauShape T) is = []) :
    (uninsertSteps T is).1 = [] := by
  have hshape := tableauShape_uninsertSteps hs hc hne hsca
  rw [hempty] at hshape
  have hlen : (uninsertSteps T is).1.length = 0 := by
    have := congrArg List.length hshape
    simpa [tableauShape] using this
  exact List.eq_nil_of_length_eq_zero hlen

/-- **The recovered word's record, read from the empty tableau** — the form brick 4 consumes. -/
theorem rowIndices_uninsertSteps_of_shape {T : List (List ℕ)} {is : List ℕ}
    (hs : RowsSorted T) (hc : ColStrict T) (hne : NoEmptyRows T)
    (hsca : ShapeCornersAlong (tableauShape T) is)
    (hempty : removeCornerSteps (tableauShape T) is = []) :
    rowIndices [] (uninsertSteps T is).2 = is := by
  have h := rowIndices_uninsertSteps is T hs hc hne (cornersAlong_of_shape hs hc hne hsca)
  rwa [uninsertSteps_fst_eq_nil hs hc hne hsca hempty] at h

/-- **Every standard pair of a common shape is an insertion pair.**

The word is the one the reverse cascade recovers from `P` at the positions `Q` records. Its
insertion tableau is `P` by brick 27; its recording tableau is `Q` because its row-index record is
`Q`'s position list (brick 29) and replaying that list rebuilds `Q` (brick 31). -/
theorem insertWordRec_uninsertSteps_of_standard {P Q : List (List ℕ)}
    (hPs : RowsSorted P) (hPc : ColStrict P) (hPn : NoEmptyRows P)
    (hQc : ColStrict Q) (hQstrict : ∀ row ∈ Q, row.Sorted (· < ·)) (hQnd : Q.flatten.Nodup)
    (hQn : NoEmptyRows Q) {n : ℕ}
    (hrange : ∀ t, t < n → t ∈ Q.flatten) (hlt : ∀ a ∈ Q.flatten, a < n)
    (hshape : tableauShape P = addCellSteps [] (qPositions Q n)) :
    insertWordRec (uninsertSteps P (qPositions Q n)).2 = (P, Q) := by
  have haa : AddableAlong [] (qPositions Q n) :=
    addableAlong_qPositions hQc hQstrict hQnd n hrange
  obtain ⟨hsca, hempty⟩ := shapeCornersAlong_and_empty haa
  rw [← hshape] at hsca hempty
  have h1 : (insertWordRec (uninsertSteps P (qPositions Q n)).2).1 = P := by
    rw [insertWordRec_fst]
    exact insertWord_uninsertSteps_of_shape hPs hPc hPn hsca hempty
  have h2 : (insertWordRec (uninsertSteps P (qPositions Q n)).2).2 = Q := by
    rw [insertWordRec_snd_eq_qAppendSteps,
      rowIndices_uninsertSteps_of_shape hPs hPc hPn hsca hempty]
    exact qAppendSteps_qPositions_self hQc hQstrict hQnd hQn hrange hlt
  exact Prod.ext_iff.mpr ⟨h1, h2⟩

end QOU.Mathlib.Schensted
