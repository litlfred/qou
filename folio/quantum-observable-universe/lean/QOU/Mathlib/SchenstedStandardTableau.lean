import QOU.Mathlib.SchenstedCellsBridge
import QOU.Mathlib.StandardYoungTableau
import Mathlib.Order.Interval.Finset.Nat

/-!
# The RSK recording tableau as a standard Young tableau

**Brick 9b (final assembly).**  Assembles the pieces — the shifted recording SSYT
`recordingSSYT` (Brick 9a), the cells↔content bridge `content_eq_cells_map`
(Brick 9b crux), and `content_shiftT_recording` (`content Q̃ = {1,…,|w|}`, `Nodup`)
— into the standard-tableau `bijOn`, yielding

    insertWordSYT w : QOU.Mathlib.StandardYoungTableau (recordingShape w)

the recording tableau `Q̃(w)` of a word as a genuine standard Young tableau.  Its
entry map bijects the cells of the recording shape onto `Set.Icc 1 |w|`:
injectivity is the `Nodup` of the bridge multiset (`nodup_map_iff_injOn`), and the
image is `{1,…,|w|}` because the bridge multiset is `(range |w|).map (·+1)`.

This is the first bridge from the QOU RSK program into Mathlib's SYT world at the
level of a concrete `StandardYoungTableau` object; the `Sym n → Σ_λ SYT(λ)²` map
and Identity-I cardinality (`Σ_{λ⊢n} (f^λ)² = n!`) build on it.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted
open YoungDiagram Finset

/-- The **recording shape** of a word: the Young diagram of the (standard-labelled)
    recording tableau `Q̃(w)`. -/
noncomputable def recordingShape (w : List ℕ) : YoungDiagram :=
  ofRowLens (tableauShape (shiftT (insertWordRec w).2))
    (tableauShape_sorted (shiftT_colStrict (insertWordRec_colStrict w)))

/-- The entries read off the recording shape's cells are the multiset `{1, …, |w|}`. -/
theorem recordingCells_val_map (w : List ℕ) :
    ((recordingShape w).cells.val.map
      (fun c : ℕ × ℕ => ((shiftT (insertWordRec w).2).getD c.1 []).getD c.2 0))
      = (↑(List.range w.length) : Multiset ℕ).map (· + 1) := by
  rw [recordingShape, content_eq_cells_map, content_shiftT_recording]

/-- The recording shape has exactly `|w|` cells. -/
theorem recordingCells_card (w : List ℕ) : (recordingShape w).cells.card = w.length := by
  have h := congrArg Multiset.card (recordingCells_val_map w)
  simpa [Multiset.card_map] using h

/-- **The standard Young tableau `Q̃(w)`.**  The (standard-labelled) recording
    tableau of a word, realised as a `QOU.Mathlib.StandardYoungTableau`: its entry
    map bijects the cells of the recording shape onto `{1, …, |w|}`. -/
noncomputable def insertWordSYT (w : List ℕ) : StandardYoungTableau (recordingShape w) where
  toSsyt := recordingSSYT w
  bijOn := by
    rw [recordingCells_card]
    have hnodup : ((recordingShape w).cells.val.map
        (fun c : ℕ × ℕ => ((shiftT (insertWordRec w).2).getD c.1 []).getD c.2 0)).Nodup := by
      rw [recordingCells_val_map, Multiset.map_coe, Multiset.coe_nodup]
      exact List.nodup_range.map Nat.succ_injective
    have hinj : Set.InjOn (fun c : ℕ × ℕ => ((shiftT (insertWordRec w).2).getD c.1 []).getD c.2 0)
        ↑(recordingShape w).cells := nodup_map_iff_injOn.mp hnodup
    have himg : (fun c : ℕ × ℕ => ((shiftT (insertWordRec w).2).getD c.1 []).getD c.2 0) ''
        ↑(recordingShape w).cells = Set.Icc 1 w.length := by
      rw [← Finset.coe_image]
      have hfin : (recordingShape w).cells.image
          (fun c : ℕ × ℕ => ((shiftT (insertWordRec w).2).getD c.1 []).getD c.2 0)
          = Finset.Icc 1 w.length := by
        ext y
        simp only [Finset.mem_image, Finset.mem_Icc]
        constructor
        · rintro ⟨⟨i, j⟩, hc, rfl⟩
          have hm := Multiset.mem_map_of_mem
            (fun c : ℕ × ℕ => ((shiftT (insertWordRec w).2).getD c.1 []).getD c.2 0)
            (show (i, j) ∈ (recordingShape w).cells.val by simpa using hc)
          rw [recordingCells_val_map] at hm
          simp only [Multiset.mem_map, Multiset.mem_coe, List.mem_range] at hm
          obtain ⟨a, ha, hay⟩ := hm
          rw [← hay]; omega
        · rintro ⟨h1, h2⟩
          have hm : y ∈ (recordingShape w).cells.val.map
              (fun c : ℕ × ℕ => ((shiftT (insertWordRec w).2).getD c.1 []).getD c.2 0) := by
            rw [recordingCells_val_map]
            simp only [Multiset.mem_map, Multiset.mem_coe, List.mem_range]
            exact ⟨y - 1, by omega, by omega⟩
          rw [Multiset.mem_map] at hm
          obtain ⟨c, hc, hfc⟩ := hm
          exact ⟨c, by simpa using hc, hfc⟩
      rw [hfin, Finset.coe_Icc]
    exact himg ▸ hinj.bijOn_image

end QOU.Mathlib.Schensted
