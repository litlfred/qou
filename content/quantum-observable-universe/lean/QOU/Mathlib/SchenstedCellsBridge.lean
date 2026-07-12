import QOU.Mathlib.SchenstedRecordingShift
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Fin

/-!
# Cells-content bridge for row-length Young diagrams

**Brick 9b crux.**  To realise the recording tableau as a
`QOU.Mathlib.StandardYoungTableau` we must discharge its `bijOn` obligation — the
entry map bijects the diagram cells onto `{1, …, n}`.  The single fact all four
`BijOn` components (`card`, `InjOn`, `MapsTo`, `SurjOn`) reduce to is:

    (ofRowLens (tableauShape Q) _).cells.val.map (fun c => (Q.getD c.1 []).getD c.2 0)
      = content Q

i.e. the multiset of entries read off the cells of the row-length diagram equals
the flattened list `content`.  The proof decomposes `μ.cells` by rows
(`cells_biUnion`, built from `Finset.ext` + `mem_row_iff`), rewrites each row as a
product (`row_eq_prod`), and matches it to the list content
(`map_getD_range`, `content_eq_sum_range`).

Supporting general-purpose lemmas about `YoungDiagram.ofRowLens` (`rowLen_getD`,
`cells_biUnion`, `rows_pairwiseDisjoint`) are stated for an arbitrary sorted
row-length list, independent of the RSK development.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted
open YoungDiagram Finset

theorem rowLen_getD (L : List ℕ) (hsort : L.Sorted (· ≥ ·)) (i : ℕ) :
    (ofRowLens L hsort).rowLen i = L.getD i 0 := by
  by_cases hi : i < L.length
  · have h := rowLen_ofRowLens (w := L) (hw := hsort) ⟨i, hi⟩
    rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi, Option.getD_some]
    simpa using h
  · push_neg at hi
    rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none hi, Option.getD_none]
    by_contra h
    have hpos : 0 < (ofRowLens L hsort).rowLen i := Nat.pos_of_ne_zero h
    have hmem : (i, 0) ∈ ofRowLens L hsort := mem_iff_lt_rowLen.mpr hpos
    rw [mem_ofRowLens] at hmem
    obtain ⟨hlt, _⟩ := hmem
    omega

theorem cells_biUnion (L : List ℕ) (hsort : L.Sorted (· ≥ ·)) :
    (ofRowLens L hsort).cells = (Finset.range L.length).biUnion (ofRowLens L hsort).row := by
  ext ⟨i, j⟩
  simp only [mem_cells, mem_biUnion, mem_range, mem_row_iff]
  constructor
  · intro hij
    refine ⟨i, ?_, hij, rfl⟩
    rw [mem_ofRowLens] at hij; exact hij.1
  · rintro ⟨i', _, hij, rfl⟩; exact hij

theorem map_getD_range (l : List ℕ) :
    (List.range l.length).map (fun j => l.getD j 0) = l := by
  apply List.ext_getElem
  · simp
  · intro k h1 h2
    simp only [List.getElem_map, List.getElem_range]
    rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h2, Option.getD_some]

theorem val_map_eq_sum {α β : Type*} [DecidableEq α] (s : Finset α) (f : α → β) :
    s.val.map f = ∑ c ∈ s, ({f c} : Multiset β) := by
  induction s using Finset.induction with
  | empty => simp
  | @insert a t ha ih =>
      rw [Finset.sum_insert ha, ← ih, Finset.insert_val,
        Multiset.ndinsert_of_notMem (by simpa using ha), Multiset.map_cons,
        Multiset.singleton_add]

theorem rows_pairwiseDisjoint (μ : YoungDiagram) (n : ℕ) :
    (↑(Finset.range n) : Set ℕ).PairwiseDisjoint μ.row := by
  intro i _ i' _ hne
  rw [Function.onFun, Finset.disjoint_left]
  rintro ⟨a, b⟩ hc hc'
  rw [mem_row_iff] at hc hc'
  exact hne (hc.2.symm.trans hc'.2)

/-- Sum-over-rows form of `content`. -/
theorem content_eq_sum_range (Q : List (List ℕ)) :
    content Q = ∑ i ∈ Finset.range Q.length, (↑(Q.getD i []) : Multiset ℕ) := by
  induction Q with
  | nil => simp [content]
  | cons r T ih =>
      rw [content_cons, ih, List.length_cons, Finset.sum_range_succ']
      simp only [List.getD_cons_succ, List.getD_cons_zero]
      rw [add_comm]

/-- A row as a multiset via `getD`-indexed sum over its length. -/
theorem sum_range_getD (l : List ℕ) :
    ∑ j ∈ Finset.range l.length, ({l.getD j 0} : Multiset ℕ) = ↑l := by
  rw [← val_map_eq_sum, Finset.range_val,
    show Multiset.range l.length = (↑(List.range l.length) : Multiset ℕ) from rfl,
    Multiset.map_coe, map_getD_range]

/-- **The content bridge.**  The multiset of entries over the cells of the
    row-length diagram equals the tableau content. -/
theorem content_eq_cells_map (Q : List (List ℕ))
    (hsort : (tableauShape Q).Sorted (· ≥ ·)) :
    ((ofRowLens (tableauShape Q) hsort).cells.val.map
        (fun c => (Q.getD c.1 []).getD c.2 0)) = content Q := by
  rw [val_map_eq_sum, cells_biUnion (tableauShape Q) hsort,
    Finset.sum_biUnion (rows_pairwiseDisjoint _ (tableauShape Q).length)]
  have hlen : (tableauShape Q).length = Q.length := by simp [tableauShape]
  rw [content_eq_sum_range, hlen]
  apply Finset.sum_congr rfl
  intro i _
  rw [row_eq_prod, Finset.sum_product, Finset.sum_singleton, rowLen_getD, shape_getD,
    sum_range_getD]

end QOU.Mathlib.Schensted
