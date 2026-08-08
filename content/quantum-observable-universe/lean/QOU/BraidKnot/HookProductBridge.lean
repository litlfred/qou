import QOU.BraidKnot.StandardYoungTableau
import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# Reconciling the two hook-length products

`QOU/BraidKnot/StandardYoungTableau.lean` defines the hook product as a
`Finset` product over the cells of a `YoungDiagram`:

  `hookProduct μ = ∏ c ∈ μ.cells, hookLength μ c.1 c.2`

while `QOU/BraidKnot/IdentityIContentDecomposition.lean` defines it as a nested
`List` product over row lengths:

  `prodHooks l = ∏_{i < l.length} ∏_{j < l.getD i 0} ((l.getD i 0 - j) + (colLen l j - i) - 1)`

Both are "the" denominator of the Frame–Robinson–Thrall formula, and the
downstream identities freely assume they agree. This file proves it.

Nothing here depends on FRT itself; the `sorry` on `numSYT_mul_hookProduct`
is untouched. This is the definitional groundwork beneath it.
-/

namespace QOU.BraidKnot

open Finset
open QOU.BraidKnot.IdentityI (prodHooks colLen)

/-- A `Finset.range` product is the corresponding `List.range` product. Used to
convert `hookProduct_eq_nested` (Finset-indexed) into `prodHooks` (List-indexed). -/
theorem prod_range_eq_list_prod {M : Type*} [CommMonoid M] (n : ℕ) (f : ℕ → M) :
    ∏ i ∈ Finset.range n, f i = ((List.range n).map f).prod := by
  rw [Finset.prod_eq_multiset_prod, Finset.range_val]
  rfl

/-- The list-side `colLen` of the row-length list is the diagram's `colLen`.
Definitionally `colLen l j = (l.filter (j < ·)).length`, so this is exactly
`length_filter_rowLens` restated in `IdentityI`'s vocabulary. -/
theorem colLen_rowLens (μ : YoungDiagram) (j : ℕ) :
    IdentityI.colLen μ.rowLens j = μ.colLen j :=
  length_filter_rowLens μ j

/-- **The two hook products agree.**

`StandardYoungTableau.hookProduct` (a `Finset` product over cells) equals
`IdentityIContentDecomposition.prodHooks` applied to the diagram's row lengths.

Every ingredient was proved in `StandardYoungTableau`:
`hookProduct_eq_nested` turns the cell product into `∏_i ∏_j`, and
`rowLens_getD` / `length_filter_rowLens` identify the list-side row lengths and
column lengths with the diagram's. -/
theorem hookProduct_eq_prodHooks (μ : YoungDiagram) :
    hookProduct μ = prodHooks μ.rowLens := by
  rw [hookProduct_eq_nested, prodHooks]
  rw [YoungDiagram.length_rowLens]
  rw [prod_range_eq_list_prod]
  refine congrArg List.prod (List.map_congr_left ?_)
  intro i _
  simp only [rowLens_getD]
  rw [prod_range_eq_list_prod]
  refine congrArg List.prod (List.map_congr_left ?_)
  intro j _
  rw [colLen_rowLens]

end QOU.BraidKnot
