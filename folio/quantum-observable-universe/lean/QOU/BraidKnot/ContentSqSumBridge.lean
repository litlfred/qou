import QOU.BraidKnot.JucysMurphy
import QOU.BraidKnot.IdentityIContentDecomposition
import QOU.Mathlib.SchenstedCellsBridge

/-!
# QOU.BraidKnot.ContentSqSumBridge — the two content-square sums are the same sum

The corpus computes `Σ_{c ∈ λ} c(c)²` twice, over different indices and by different formulas:

* `JucysMurphy.contentSqSum (μ : YoungDiagram) := ∑ c ∈ μ.cells, (cellContent c)^2` — a `Finset`
  sum over the diagram's cells, which is the form the Jucys–Murphy / Okounkov–Vershik layer speaks;
* `IdentityI.sumSqContents (l : List ℕ)` — nested `List` sums over the
  row-length list, which is the form the Identity-I / Plancherel layer speaks.

**`contentSqSum_ofRowLens`** identifies them. Nothing in the corpus did, which is what kept
`identityB_general` (Identity (ii) for general `n`, stated with `contentSqSum`) from reaching
`PlancherelSnData` (whose field is stated with `sumSqContents`, and whose instances therefore
stopped at `n = 12`).  `PlancherelSnDataGeneral` is the consumer: with this lemma the datum is
built at every `n`, and Identity I comes off that cap.

The proof is the weighted analogue of `QOU.Mathlib.card_cells_ofRowLens`: the cells are the disjoint
union of the rows (`cells_biUnion`, `rows_pairwiseDisjoint`) and a row is a singleton times a range
(`row_eq_prod`), so the cell sum reorganises into the nested row sum. As there, the pieces come from
`SchenstedCellsBridge`, whose lemmas are general even though its headline theorem is stated only for
a `tableauShape`.

Pure combinatorics on `ℕ`/`ℤ`; nothing archimedean; no fit.
-/

namespace QOU.BraidKnot.ContentSqSumBridge

open YoungDiagram Finset

/-- **The cell-indexed and row-list-indexed content-square sums agree.** -/
theorem contentSqSum_ofRowLens (L : List ℕ) (hsort : L.Sorted (· ≥ ·)) :
    JucysMurphy.contentSqSum (ofRowLens L hsort)
      = IdentityI.sumSqContents L := by
  rw [JucysMurphy.contentSqSum, QOU.Mathlib.Schensted.cells_biUnion L hsort,
    Finset.sum_biUnion (QOU.Mathlib.Schensted.rows_pairwiseDisjoint _ L.length)]
  show ∑ i ∈ Finset.range L.length, _
      = ∑ i ∈ Finset.range L.length,
          ∑ j ∈ Finset.range (L.getD i 0), ((j : ℤ) - (i : ℤ)) ^ 2
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [row_eq_prod, Finset.sum_product, Finset.sum_singleton,
    QOU.Mathlib.Schensted.rowLen_getD]
  rfl

/-- Subtracting the row-list content-square sum from the cell-indexed content-square sum cancels to zero (`qou-ircb`). -/
theorem contentSqSum_ofRowLens_sub_eq_zero (L : List ℕ) (hsort : L.Sorted (· ≥ ·)) :
    JucysMurphy.contentSqSum (ofRowLens L hsort) - IdentityI.sumSqContents L = 0 := by
  rw [contentSqSum_ofRowLens L hsort, sub_self]

end QOU.BraidKnot.ContentSqSumBridge
