import QOU.BraidKnot.GarnirShape
import QOU.Mathlib.SchenstedPartitionShape

/-!
# The Garnir shape has the same size — the connector 3.14's outer induction needs

`GarnirShape.garnirShape_lexGt` gives `garnirShape μ i j >ₗ μ`, and
`PartitionLexWellFounded.lexGtOn` is the well-founded order 3.14's case (i) inducts along.
They do **not** compose as they stand: `lexGtOn n` lives on `PartOf n`, shapes of a *fixed*
size, so feeding the Garnir shape into it needs

    `(garnirShape μ i j).cells.card = μ.cells.card`

which was **not** in the corpus.  This file supplies the arithmetic half — that the Garnir
composition has the same total — and records precisely what blocks the rest.

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

/-! ## The remaining step, and the Mathlib gap that blocks it

`sum_garnirComp` is the mathematical content: the Garnir composition and the original shape
have the same total.  Turning that into

    `(garnirShape μ i j).cells.card = μ.cells.card`

needs one more link — that `ofRowLens` preserves the sum of its input list — and **that is
not available**:

* `YoungDiagram.rowLens_ofRowLens_eq_self` requires `∀ x ∈ w, 0 < x`, and `garnirComp` can
  legitimately contain **zeros** (`j = 0`, or `rowLen (i+1) - j - 1 = 0`), so it does not
  apply.  The same positivity hypothesis blocks `rowLens_length_ofRowLens`.
* Mathlib has no `card_ofRowLens` / `sum_rowLens_ofRowLens` at all — checked by enumerating
  the environment, since a source grep is worthless in this checkout
  ([`scripts/lean-probes/`](../../../../../scripts/lean-probes/README.md)).

The route, for whoever takes it: `ofRowLens` drops trailing zeros (the list is sorted
descending, so zeros are exactly a suffix), and dropping zeros does not change a sum.  So
the missing lemma is

    `(YoungDiagram.ofRowLens w hw).rowLens.sum = w.sum`   (no positivity hypothesis)

and it belongs upstream of this file, next to `card_cells_eq_rowLens_sum`.  The corpus's
`PartitionOfComposition.colLen_ofComposition` gives a second, column-side route via the
identity `l.sum = Σ_m l.countP (m < ·)`, should the row side prove awkward.

This is recorded rather than attempted because it is a general `YoungDiagram` lemma with a
real Mathlib gap behind it, not a step of the Garnir argument — and a rushed proof of it at
the end of a long session is exactly the kind of thing this corpus asks agents not to
produce.
-/

end QOU.BraidKnot.GarnirShapeCard
