import QOU.Mathlib.SchenstedWordSurjectivity

/-!
# QOU.Mathlib.SchenstedCornersAlong — insertion always creates a corner (brick 15)

Brick 14 (`SchenstedWordSurjectivity`) proved that a reverse run rebuilds the tableau it was peeled
from, under two hypotheses about the *positions*:

* `CornersAlong T is` — every step removes a corner of the tableau as it stands at that step;
* `(uninsertSteps T is).1 = []` — the run empties the tableau.

Both were stated as the interface to the recording tableau, and left to be discharged one level up.
**This file discharges both for every insertion-built run**, which is what shows the hypotheses are
satisfiable rather than an empty class.

The load-bearing fact turns out not to be about the recording tableau at all:

> **`insert_isCorner`** — the cell `insert T x` adds is always a corner of the result.

Why: if the new cell lands at the end of row `i` (making it length `L`), then before the insertion
row `i` had length `L - 1`, and `ColStrict`'s length half gave row `i + 1` at most that. So row
`i + 1` is at most `L - 1 < L` — a corner. The row below being *as long* would have violated the
Young shape of the tableau we started from.

From there, `cornersAlong_rowIndices` follows by induction, with brick 3's `uninsertSteps_foldl`
supplying the bridge: after undoing the later steps, the tableau standing at step `k` is exactly
the tableau after `k + 1` insertions, so the corner condition at that step *is* `insert_isCorner`.

## What this does and does not settle

It settles that brick 14's hypotheses hold for every `P` that arises from a word — which is the
anti-vacuity check, and it makes `insertWord_uninsertSteps` applicable rather than merely true.

It does **not** settle surjectivity of `rskPair`. That needs `CornersAlong P is` for an *arbitrary*
standard pair `(P, Q)`, where `is` is read off `Q` rather than off an insertion history. The
argument there is different — the cell carrying the largest remaining entry of a standard tableau
is a corner, because a cell below it would carry a larger one — and it is a later brick of epic
`qou-nrex`. Nothing here claims it, and `RSKBurnsideHolds` for general `n` stays open.

Pure combinatorics on `ℕ`; nothing archimedean.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

/-- The first row of a column-strict tableau bounds the second. -/
theorem headD_tail_length_le {r : List ℕ} {T : List (List ℕ)} (hc : ColStrict (r :: T)) :
    (T.headD []).length ≤ r.length := by
  cases T with
  | nil => simp
  | cons row rest => exact (strictBelow_head hc (by simp)).1

/-- **Insertion always creates a corner.** The cell `insert T x` adds sits at the end of its row
with the row below strictly shorter.

The no-bump case is the whole content: the row grows from `L - 1` to `L`, and `ColStrict` had
already bounded the row below by `L - 1`. Had the row below been as long, the tableau we started
from would not have been a Young shape. The bumping case is the recursion. -/
theorem insert_isCorner : ∀ (T : List (List ℕ)), ColStrict T → ∀ (x : ℕ),
    IsCorner (insert T x) (newRowIndex T x)
  | [], _, x => by simp [insert, newRowIndex, IsCorner]
  | r :: T, hc, x => by
      rw [insert, newRowIndex]
      -- `cases h : e` substitutes `e` in the goal, so no `rw [hb]` is needed (and it would fail).
      cases hb : (rowInsert r x).2 with
      | none =>
          simp only
          rw [isCorner_cons_zero, rowInsert_length_none hb]
          have := headD_tail_length_le hc
          omega
      | some y =>
          simp only
          rw [isCorner_cons_succ]
          exact insert_isCorner T (colStrict_tail hc) y

/-- **Every insertion-built run removes corners.** The corner condition at step `k` is checked
against the tableau after the later steps are undone, which brick 3's `uninsertSteps_foldl` says is
the tableau after `k + 1` insertions — so it is exactly `insert_isCorner`. -/
theorem cornersAlong_rowIndices : ∀ (w : List ℕ) (T : List (List ℕ)),
    RowsSorted T → ColStrict T → NoEmptyRows T →
    CornersAlong (w.foldl insert T) (rowIndices T w)
  | [], T, _, _, _ => trivial
  | x :: rest, T, hs, hc, hne => by
      rw [List.foldl_cons, rowIndices_cons, cornersAlong_cons]
      refine ⟨cornersAlong_rowIndices rest (insert T x) (insert_rowsSorted hs x)
        (insert_colStrict hc x) (insert_noEmptyRows hne x), ?_⟩
      rw [uninsertSteps_foldl rest (insert T x) (insert_rowsSorted hs x)
        (insert_noEmptyRows hne x)]
      exact insert_isCorner T hc x

/-- **No insertion tableau has an empty row.** The fold of brick 2's `insert_noEmptyRows`.

`insertWord_rowsSorted` and `insertWord_colStrict` are both in `SchenstedInsertion`, but this third
one is not: `insert_noEmptyRows` is defined downstream, in `SchenstedReverseCascade`, so the fold
was never taken. -/
theorem insertWord_noEmptyRows (w : List ℕ) : NoEmptyRows (insertWord w) := by
  suffices h : ∀ (T : List (List ℕ)), NoEmptyRows T → NoEmptyRows (w.foldl insert T) by
    exact h [] noEmptyRows_nil
  induction w with
  | nil => intro T hT; exact hT
  | cons a rest ih =>
      intro T hT
      rw [List.foldl_cons]
      exact ih _ (insert_noEmptyRows hT a)

/-- The corner condition, at the empty starting tableau. -/
theorem cornersAlong_insertWord (w : List ℕ) : CornersAlong (insertWord w) (rowIndices [] w) :=
  cornersAlong_rowIndices w [] rowsSorted_nil colStrict_nil noEmptyRows_nil

/-- The emptying condition, at the empty starting tableau — brick 3, read off its first component. -/
theorem uninsertSteps_insertWord_fst (w : List ℕ) :
    (uninsertSteps (insertWord w) (rowIndices [] w)).1 = [] := by
  rw [uninsertSteps_insertWord]

/-- **Brick 14's hypotheses are satisfiable.** Both discharged, for every word.

The conclusion is weaker than brick 3's `uninsertSteps_insertWord` (which pins the recovered word
on the nose, not merely its insertion tableau), and that is the point: this is a consistency check
on brick 14, not a new result about `insertWord`. What it buys is that
`insertWord_uninsertSteps` is a theorem with inhabited hypotheses. -/
theorem insertWord_uninsertSteps_insertWord (w : List ℕ) :
    insertWord (uninsertSteps (insertWord w) (rowIndices [] w)).2 = insertWord w :=
  insertWord_uninsertSteps (insertWord w) (rowIndices [] w)
    (insertWord_rowsSorted w) (insertWord_colStrict w) (insertWord_noEmptyRows w)
    (cornersAlong_insertWord w) (uninsertSteps_insertWord_fst w)

end QOU.Mathlib.Schensted
