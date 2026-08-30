import QOU.Mathlib.YoungDiagramAddable

/-!
# QOU.Mathlib.YoungLatticeExchange — the corner/addable exchange, on the `YoungDiagramAddable` API

The `(λ, removable corner) ≃ (λ ∖ c, that corner, now addable)` exchange, built on
`QOU.Mathlib.YoungDiagramAddable` so that it can sit in `QOU.lean`'s import cone.

## Why this file exists rather than reusing `YoungDiagramAddCell`

`QOU.Mathlib.YoungDiagramAddCell` already has this exchange (`cornerAddEquiv`). It cannot
be used here: `YoungDiagramAddCell` and `YoungDiagramAddable` both declare
`QOU.Mathlib.IsAddableCell` and `QOU.Mathlib.addCell`, so **no module can import both** —

    error: import QOU.Mathlib.YoungDiagramAddable failed, environment already contains
           'QOU.Mathlib.mem_addCell._simp_1' from QOU.Mathlib.YoungDiagramAddCell

and `QOU.lean` imports `YoungDiagramAddable`. Since the two `addCell` definitions are
*character-identical* (`insert c μ.cells`, same `IsAddableCell` hypothesis), the four
round-trip lemmas port verbatim; they are re-proved here against `YoungDiagramAddable`'s
copy. The duplication is main's (bean `qou-dup1`), not introduced here — this file simply
picks the side `QOU.lean` already uses.

Names are deliberately distinct from `YoungDiagramAddCell`'s (`SizedCornerPair` vs
`CornerPair`, etc.) so that this module does not re-create the very collision it works
around.

Pure combinatorics; nothing archimedean (§7c).
-/

namespace QOU.Mathlib

open YoungDiagram Finset

variable {μ : YoungDiagram}

/-! ## Round-trips between `addCell` and `eraseCorner` -/

/-- The added cell is a removable corner of the result. -/
theorem isCornerCell_addCell' (c : ℕ × ℕ) (hc : IsAddableCell μ c) :
    IsCornerCell (addCell μ c hc) c := by
  refine ⟨(mem_addCell μ c c hc).mpr (Or.inl rfl), ?_, ?_⟩
  · rw [mem_addCell]
    rintro (h | h)
    · exact absurd h (by simp [Prod.ext_iff])
    · exact hc.1 (μ.up_left_mem (by omega) le_rfl h)
  · rw [mem_addCell]
    rintro (h | h)
    · exact absurd h (by simp [Prod.ext_iff])
    · exact hc.1 (μ.up_left_mem le_rfl (by omega) h)

/-- Adding then erasing is the identity. -/
theorem eraseCorner_addCell' (c : ℕ × ℕ) (hc : IsAddableCell μ c) :
    eraseCorner (addCell μ c hc) c (isCornerCell_addCell' c hc) = μ := by
  ext x
  simp only [YoungDiagram.mem_cells]
  rw [mem_eraseCorner, mem_addCell]
  constructor
  · rintro ⟨h | h, hne⟩
    · exact absurd h hne
    · exact h
  · intro h
    exact ⟨Or.inr h, fun hx => hc.1 (hx ▸ h)⟩

/-- A removable corner is addable to the erased diagram. -/
theorem isAddableCell_eraseCorner' (c : ℕ × ℕ) (hc : IsCornerCell μ c) :
    IsAddableCell (eraseCorner μ c hc) c := by
  refine ⟨by rw [mem_eraseCorner]; rintro ⟨-, h⟩; exact h rfl, ?_, ?_⟩
  · by_cases h0 : c.1 = 0
    · exact Or.inl h0
    · refine Or.inr ?_
      rw [mem_eraseCorner]
      refine ⟨μ.up_left_mem (by omega) le_rfl hc.1, ?_⟩
      intro hh; rw [Prod.ext_iff] at hh; omega
  · by_cases h0 : c.2 = 0
    · exact Or.inl h0
    · refine Or.inr ?_
      rw [mem_eraseCorner]
      refine ⟨μ.up_left_mem le_rfl (by omega) hc.1, ?_⟩
      intro hh; rw [Prod.ext_iff] at hh; omega

/-- Erasing then adding is the identity. -/
theorem addCell_eraseCorner' (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (ha : IsAddableCell (eraseCorner μ c hc) c) :
    addCell (eraseCorner μ c hc) c ha = μ := by
  ext x
  simp only [YoungDiagram.mem_cells]
  rw [mem_addCell, mem_eraseCorner]
  constructor
  · rintro (rfl | ⟨h, _⟩)
    · exact hc.1
    · exact h
  · intro h
    by_cases hx : x = c
    · exact Or.inl hx
    · exact Or.inr ⟨h, hx⟩

/-! ## The exchange

Both sides are phrased as subtypes of ONE product type rather than as `Sigma`s over the
diagram — that keeps the round-trips at `Subtype.ext` with no `HEq` transport. -/

/-- A diagram of size `n + 1` together with one of its removable corners. -/
def SizedCornerPair (n : ℕ) : Type :=
  {p : YoungDiagram × (ℕ × ℕ) // p.1.cells.card = n + 1 ∧ IsCornerCell p.1 p.2}

/-- A diagram of size `n` together with one of its addable cells. -/
def SizedAddPair (n : ℕ) : Type :=
  {p : YoungDiagram × (ℕ × ℕ) // p.1.cells.card = n ∧ IsAddableCell p.1 p.2}

/-- **The exchange.** `(λ, removable corner) ↔ (λ ∖ c, that corner as an addable one)`. -/
def sizedCornerAddEquiv (n : ℕ) : SizedCornerPair n ≃ SizedAddPair n where
  toFun p :=
    ⟨(eraseCorner p.1.1 p.1.2 p.2.2, p.1.2), by
      refine ⟨?_, isAddableCell_eraseCorner' p.1.2 p.2.2⟩
      show (eraseCorner p.1.1 p.1.2 p.2.2).cells.card = n
      have h1 := card_eraseCorner p.1.1 p.1.2 p.2.2
      have h2 := p.2.1
      omega⟩
  invFun p :=
    ⟨(addCell p.1.1 p.1.2 p.2.2, p.1.2), by
      refine ⟨?_, isCornerCell_addCell' p.1.2 p.2.2⟩
      show (addCell p.1.1 p.1.2 p.2.2).cells.card = n + 1
      rw [card_addCell, p.2.1]⟩
  left_inv := by
    rintro ⟨⟨L, c⟩, hL, hc⟩
    refine Subtype.ext ?_
    show (addCell (eraseCorner L c hc) c (isAddableCell_eraseCorner' c hc), c) = (L, c)
    rw [addCell_eraseCorner']
  right_inv := by
    rintro ⟨⟨M, s⟩, hM, hs⟩
    refine Subtype.ext ?_
    show (eraseCorner (addCell M s hs) s (isCornerCell_addCell' s hs), s) = (M, s)
    rw [eraseCorner_addCell']

/-! ## Bridge to the branching theorem's index type

`QOU.Mathlib.numStandardYoungTableaux_branching` sums over the SUBTYPE
`{c // IsCornerCell μ c}`; `YoungDiagramAddable` counts with the FINSET `cornerCells μ`.
`mem_cornerCells` makes the two agree. -/

theorem card_cornerCells_eq_card_subtype (μ : YoungDiagram)
    [Fintype {c : ℕ × ℕ // IsCornerCell μ c}] :
    (cornerCells μ).card = Fintype.card {c : ℕ × ℕ // IsCornerCell μ c} :=
  (Fintype.card_of_subtype (cornerCells μ) (fun _ => mem_cornerCells μ _)).symm

/-- The number of summands in the branching sum is one less than the number of addable
cells — the differential property in the form the branching sum sees it. -/
theorem card_subtype_corners_add_one (μ : YoungDiagram)
    [Fintype {c : ℕ × ℕ // IsCornerCell μ c}] :
    Fintype.card {c : ℕ × ℕ // IsCornerCell μ c} + 1 = (addableCells μ).card := by
  rw [← card_cornerCells_eq_card_subtype, card_addableCells_eq_card_cornerCells_succ]

/-! ## Non-vacuity

`card_addableCells_eq_card_cornerCells_succ` asserts nothing if both families are empty —
it would read `1 = 0 + 1` on every diagram. Both are shown inhabited structurally. -/

theorem addableCells_nonempty (μ : YoungDiagram) : (addableCells μ).Nonempty := by
  refine ⟨(0, μ.rowLen 0), ?_⟩
  rw [mem_addableCells]
  exact (addable_iff μ 0 (μ.rowLen 0)).mpr ⟨rfl, Or.inl rfl⟩

/-- Any non-empty diagram has a removable corner: the last non-empty row carries one. -/
theorem cornerCells_nonempty (μ : YoungDiagram) (h : 0 < μ.colLen 0) :
    (cornerCells μ).Nonempty := by
  refine ⟨(μ.colLen 0 - 1, μ.rowLen (μ.colLen 0 - 1) - 1), ?_⟩
  rw [mem_cornerCells]
  have h1 : 0 < μ.rowLen (μ.colLen 0 - 1) := (rowLen_pos_iff μ _).mpr (by omega)
  have h2 : ¬ (0 < μ.rowLen (μ.colLen 0 - 1 + 1)) := by
    rw [rowLen_pos_iff]; omega
  exact (corner_iff μ _ _).mpr ⟨by omega, by omega⟩

end QOU.Mathlib
