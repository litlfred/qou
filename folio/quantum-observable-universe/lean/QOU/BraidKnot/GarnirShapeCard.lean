import QOU.BraidKnot.GarnirShape
import QOU.Mathlib.SchenstedPartitionShape
import QOU.BraidKnot.PartitionLexWellFounded

/-!
# The Garnir shape has the same size — the connector 3.14's outer induction needs

`GarnirShape.garnirShape_lexGt` gives `garnirShape μ i j >ₗ μ`, and
`PartitionLexWellFounded.lexGtOn` is the well-founded order 3.14's case (i) inducts along.
They do **not** compose as they stand: `lexGtOn n` lives on `PartOf n`, shapes of a *fixed*
size, so feeding the Garnir shape into it needs

    `(garnirShape μ i j).cells.card = μ.cells.card`

This file supplies it, and with it `lexGtOn_garnirPartOf`: the Garnir step **drops the
shape in the very order 3.14's outer induction runs on**.

> **🛑 CORRECTION.  An earlier version of this file recorded the last step as blocked by a
> missing lemma — `(ofRowLens w hw).rowLens.sum = w.sum` with no positivity hypothesis —
> and said so in its docstring and commit message.  That was wrong.
> `QOU.Mathlib.card_cells_ofRowLens` proves exactly `(ofRowLens L hsort).cells.card = L.sum`,
> with no positivity hypothesis, and it sits **one screen above**
> `card_cells_eq_rowLens_sum` in `SchenstedPartitionShape.lean` — the file this one was
> already importing and citing.  The Mathlib half of that claim was right and was measured
> by environment enumeration; the corpus half was never checked at all.  `card_garnirShape`
> below is now three rewrites.

## Why the count works out

`garnirComp μ i j` replaces rows `i, i+1` of `μ` — of lengths `rowLen i` and `rowLen (i+1)`
— by the three entries

    `j`,  `rowLen i + 1`,  `rowLen (i+1) - j - 1`

whose sum is `rowLen i + rowLen (i+1)` **provided `j + 1 ≤ rowLen (i+1)`**, which is exactly
what `(i+1, j) ∈ μ` gives.  The subtraction is truncated `ℕ` subtraction, so that hypothesis
is doing real work rather than bookkeeping: without it the third entry clamps at `0` and the
count is wrong.

Everything else is `take`/`drop` reassembly, and sorting is invisible to a sum because
`sortDesc` is a permutation.

## The bridge lemma exists three times over

`cells.card = rowLens.sum` is in the corpus as `SchenstedPartitionShape.card_cells_eq_rowLens_sum`,
again as `WenzlJonesMarkovNormalisation.rowLens_sum_eq_card`, and a third time as
`SpechtClassification.card_eq_rowLens_sum`.  Three independent proofs of one lemma is worth
recording, not fixing here.
-/

namespace QOU.BraidKnot.GarnirShapeCard

open QOU.BraidKnot.GarnirShape QOU.BraidKnot.PartitionOfComposition

variable {μ : YoungDiagram} {i j : ℕ}

/-- Sorting does not move a sum. -/
theorem sum_sortDesc (l : List ℕ) : (sortDesc l).sum = l.sum :=
  (List.perm_insertionSort _ l).sum_eq

/-- **The Garnir composition has the same total as the shape it came from.** -/
theorem sum_garnirComp (h : (i + 1, j) ∈ μ) :
    (garnirComp μ i j).sum = μ.rowLens.sum := by
  have hlen : i + 1 < μ.rowLens.length := succ_lt_length_rowLens h
  -- `j < rowLen (i+1)`, so the truncated subtraction is exact
  have hj : j < μ.rowLen (i + 1) := by
    have := (YoungDiagram.mem_iff_lt_rowLen).mp h
    simpa using this
  -- peel the two rows off the tail
  have hdrop : μ.rowLens.drop i
      = μ.rowLen i :: μ.rowLen (i + 1) :: μ.rowLens.drop (i + 2) := by
    rw [List.drop_eq_getElem_cons (show i < μ.rowLens.length by omega),
      List.drop_eq_getElem_cons (show i + 1 < μ.rowLens.length by omega)]
    congr 1
    · simp [YoungDiagram.get_rowLens]
    · congr 1
      simp [YoungDiagram.get_rowLens]
  have hsum : μ.rowLens.sum
      = (μ.rowLens.take i).sum
        + (μ.rowLen i + (μ.rowLen (i + 1) + (μ.rowLens.drop (i + 2)).sum)) := by
    conv_lhs => rw [← List.take_append_drop i μ.rowLens]
    rw [List.sum_append, hdrop]
    simp
  rw [garnirComp]
  simp only [List.sum_append, List.sum_cons, List.sum_nil]
  rw [hsum]
  omega

/-- **The Garnir shape preserves size.**  This is the connector: it lets
`GarnirShape.garnirShape_lexGt` be fed to `PartitionLexWellFounded.lexGtOn`, which is
defined on shapes of one fixed size. -/
theorem card_garnirShape (h : (i + 1, j) ∈ μ) :
    (garnirShape μ i j).cells.card = μ.cells.card := by
  rw [garnirShape, ofComposition, QOU.Mathlib.card_cells_ofRowLens, sum_sortDesc,
    sum_garnirComp h, ← QOU.Mathlib.card_cells_eq_rowLens_sum]

/-- The Garnir shape, packaged as a member of `PartOf n` — the form
`PartitionLexWellFounded.lexGtOn` consumes. -/
def garnirPartOf (h : (i + 1, j) ∈ μ) :
    QOU.BraidKnot.PartitionLexWellFounded.PartOf μ.cells.card :=
  ⟨garnirShape μ i j, card_garnirShape h⟩

/-- **The Garnir step drops the shape in the well-founded order 3.14 inducts along.**

This is the composition the whole file exists for: `garnirShape_lexGt` gives a lex-greater
shape, `card_garnirShape` puts it at the same size, and `lexGtOn` is where 3.14's outer
induction lives. -/
theorem lexGtOn_garnirPartOf (h : (i + 1, j) ∈ μ) :
    QOU.BraidKnot.PartitionLexWellFounded.lexGtOn μ.cells.card
      (garnirPartOf h) ⟨μ, rfl⟩ :=
  garnirShape_lexGt h

/-- Subtracting the original diagram cell count from the Garnir shape cell count cancels to zero (`qou-k9yt`). -/
theorem card_garnirShape_sub_eq_zero (h : (i + 1, j) ∈ μ) :
    (garnirShape μ i j).cells.card - μ.cells.card = 0 := by
  rw [card_garnirShape h, Nat.sub_self]

end QOU.BraidKnot.GarnirShapeCard
