import QOU.Mathlib.YoungDiagramCorner
import QOU.Mathlib.StandardYoungTableau

/-!
# QOU.Mathlib.SYTMaxCorner — the maximum entry of a standard tableau sits at a removable corner

The conceptual crux of the Greene–Nijenhuis–Wilf branching rule: in a `StandardYoungTableau μ`, the
cell carrying the **maximum** value `|μ|` is a **removable corner** of `μ`.  Nothing can lie to its
right or below, because a cell there would carry a *strictly larger* value by the strict row/column
laws — impossible, as `|μ|` is already the largest value the bijection takes.

This is exactly the fact that lets one *delete the cell holding `|μ|`* to land in
`StandardYoungTableau (μ ∖ c)`, the forward half of the branching bijection.

Pure combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open YoungDiagram

/-- **The max-value cell is a removable corner.** If a cell `c` of a standard tableau `T` carries the
top value `|μ|`, then `c` is a removable corner of `μ`: both `(c.1+1, c.2)` and `(c.1, c.2+1)` lie
outside `μ`, since either would carry a value `> |μ|` by the strict column/row law. -/
theorem isCornerCell_of_entry_eq_card {μ : YoungDiagram} (T : StandardYoungTableau μ) (c : ℕ × ℕ)
    (hc : c ∈ μ) (hmax : T.entry c.1 c.2 = μ.cells.card) : IsCornerCell μ c := by
  refine ⟨hc, ?_, ?_⟩
  · -- no cell below: (c.1+1, c.2) ∉ μ
    intro hr
    have hlt : T.entry c.1 c.2 < T.entry (c.1 + 1) c.2 :=
      T.toSsyt.col_strict (Nat.lt_succ_self c.1) hr
    have hle : T.entry (c.1 + 1) c.2 ≤ μ.cells.card :=
      (T.mapsTo_cells (StandardYoungTableau.mem_coe_cells hr)).2
    omega
  · -- no cell to the right: (c.1, c.2+1) ∉ μ
    intro hd
    have hlt : T.entry c.1 c.2 < T.entry c.1 (c.2 + 1) :=
      T.row_strict (Nat.lt_succ_self c.2) hd
    have hle : T.entry c.1 (c.2 + 1) ≤ μ.cells.card :=
      (T.mapsTo_cells (StandardYoungTableau.mem_coe_cells hd)).2
    omega

/-- **A non-empty diagram has a max-value corner.** Some cell of `T` carries the top value `|μ|`, and
that cell is a removable corner — the cell the forward branching map deletes.  (Existence comes from
surjectivity of the entry bijection onto `{1, …, |μ|}`; cornerness from the lemma above.) -/
theorem exists_corner_entry_eq_card {μ : YoungDiagram} (T : StandardYoungTableau μ)
    (hne : 0 < μ.cells.card) :
    ∃ c, c ∈ μ ∧ IsCornerCell μ c ∧ T.entry c.1 c.2 = μ.cells.card := by
  have hmem : μ.cells.card ∈ Set.Icc 1 μ.cells.card := ⟨hne, le_refl _⟩
  obtain ⟨c, hccells, hce⟩ := T.bijOn.surjOn hmem
  rw [Finset.mem_coe, YoungDiagram.mem_cells] at hccells
  exact ⟨c, hccells, isCornerCell_of_entry_eq_card T c hccells hce, hce⟩

end QOU.Mathlib
