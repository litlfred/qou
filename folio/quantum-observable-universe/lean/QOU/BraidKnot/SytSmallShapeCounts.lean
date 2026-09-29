import QOU.BraidKnot.SeminormalCharacterConnector

/-!
# Concrete `#SYT` counts for small self-conjugate shapes → tabulated `c_λ`

Toward the tabulated `c_λ ∈ {1,3,8,10}` of `symbolic_character_table` (bean
`qou-tqab`). This file pins the smallest self-conjugate shape by direct
enumeration: `#SYT = 2`, hence `c_λ(σ₁) = #SYT/2 = 1`, for the hook `(2,1)`.
Larger `c_λ` values need the hook-length formula (a genuine Mathlib gap; tracked
separately).
-/

namespace QOU.BraidKnot.SytSmallShapeCounts

open QOU.Mathlib YoungDiagram QOU.BraidKnot.SeminormalCharacterConnector
open scoped Classical

/-- The hook shape `(2,1)` (self-conjugate). -/
def mu21 : YoungDiagram := YoungDiagram.ofRowLens [2, 1] (by decide)

/-- The three cells of `(2,1)` — the workhorse for every enumeration below. -/
theorem mem_mu21 {i j : ℕ} (h : (i, j) ∈ mu21) :
    (i = 0 ∧ j = 0) ∨ (i = 0 ∧ j = 1) ∨ (i = 1 ∧ j = 0) := by
  simp only [mu21, mem_ofRowLens] at h
  obtain ⟨hil, hjb⟩ := h
  have hi2 : i < 2 := hil
  interval_cases i
  · simp only [List.getElem_cons_zero] at hjb; omega
  · simp only [List.getElem_cons_succ, List.getElem_cons_zero] at hjb; omega

theorem mem_mu21_iff {i j : ℕ} :
    (i, j) ∈ mu21 ↔ (i = 0 ∧ j = 0) ∨ (i = 0 ∧ j = 1) ∨ (i = 1 ∧ j = 0) := by
  refine ⟨mem_mu21, ?_⟩
  rintro (⟨a, b⟩ | ⟨a, b⟩ | ⟨a, b⟩) <;> subst a <;> subst b <;> decide

theorem mu21_transpose : mu21.transpose = mu21 := by
  ext ⟨i, j⟩
  simp only [YoungDiagram.mem_cells, mem_transpose_iff, mem_mu21_iff]
  omega

theorem mu21_card : mu21.cells.card = 3 := by decide

/-- Explicit filling: `1` at `(0,0)`, `2` at `(0,1)`, `3` at `(1,0)`. -/
def Ta_ssyt : SemistandardYoungTableau mu21 where
  entry i j := if i = 0 ∧ j = 0 then 1 else if i = 0 ∧ j = 1 then 2
    else if i = 1 ∧ j = 0 then 3 else 0
  row_weak' := by
    intro i j1 j2 hj hcell
    rcases mem_mu21 hcell with ⟨ha, hb⟩ | ⟨ha, hb⟩ | ⟨ha, hb⟩
    · subst ha; subst hb; exfalso; omega
    · subst ha; subst hb; interval_cases j1 <;> decide
    · subst ha; subst hb; exfalso; omega
  col_strict' := by
    intro i1 i2 j hi hcell
    rcases mem_mu21 hcell with ⟨ha, hb⟩ | ⟨ha, hb⟩ | ⟨ha, hb⟩
    · subst ha; subst hb; exfalso; omega
    · subst ha; subst hb; exfalso; omega
    · subst ha; subst hb; interval_cases i1 <;> decide
  zeros' := by
    intro i j h
    have n1 : ¬(i = 0 ∧ j = 0) := fun ⟨a, b⟩ => by subst a; subst b; exact h (by decide)
    have n2 : ¬(i = 0 ∧ j = 1) := fun ⟨a, b⟩ => by subst a; subst b; exact h (by decide)
    have n3 : ¬(i = 1 ∧ j = 0) := fun ⟨a, b⟩ => by subst a; subst b; exact h (by decide)
    show (if i = 0 ∧ j = 0 then (1 : ℕ) else if i = 0 ∧ j = 1 then 2
      else if i = 1 ∧ j = 0 then 3 else 0) = 0
    rw [if_neg n1, if_neg n2, if_neg n3]

theorem card_ge_one : 1 ≤ mu21.cells.card := by simp [mu21_card]
theorem card_ge_two : 2 ≤ mu21.cells.card := by simp [mu21_card]

/-- The explicit standard tableau `T_a` (2 in the first row). -/
def Ta : StandardYoungTableau mu21 where
  toSsyt := Ta_ssyt
  bijOn := by
    refine ⟨?_, ?_, ?_⟩
    · -- MapsTo
      intro c hc
      simp only [Finset.mem_coe, YoungDiagram.mem_cells] at hc
      obtain ⟨i, j⟩ := c
      rcases mem_mu21 hc with ⟨a, b⟩ | ⟨a, b⟩ | ⟨a, b⟩
      · subst a; subst b; show (1 : ℕ) ∈ Set.Icc 1 mu21.cells.card
        rw [Set.mem_Icc, mu21_card]; omega
      · subst a; subst b; show (2 : ℕ) ∈ Set.Icc 1 mu21.cells.card
        rw [Set.mem_Icc, mu21_card]; omega
      · subst a; subst b; show (3 : ℕ) ∈ Set.Icc 1 mu21.cells.card
        rw [Set.mem_Icc, mu21_card]; omega
    · -- InjOn
      intro c hc c' hc' heq
      simp only [Finset.mem_coe, YoungDiagram.mem_cells] at hc hc'
      obtain ⟨i, j⟩ := c; obtain ⟨i', j'⟩ := c'
      rcases mem_mu21 hc with ⟨a, b⟩ | ⟨a, b⟩ | ⟨a, b⟩ <;> subst a <;> subst b <;>
        rcases mem_mu21 hc' with ⟨a', b'⟩ | ⟨a', b'⟩ | ⟨a', b'⟩ <;> subst a' <;> subst b' <;>
        first | rfl | (exfalso; revert heq; decide)
    · -- SurjOn
      intro v hv
      rw [Set.mem_Icc, mu21_card] at hv
      obtain ⟨hv1, hv2⟩ := hv
      interval_cases v
      · exact ⟨(0, 0), by simp [YoungDiagram.mem_cells, mem_mu21_iff], rfl⟩
      · exact ⟨(0, 1), by simp [YoungDiagram.mem_cells, mem_mu21_iff], rfl⟩
      · exact ⟨(1, 0), by simp [YoungDiagram.mem_cells, mem_mu21_iff], rfl⟩

theorem Ta_entry_00 : Ta.entry 0 0 = 1 := by decide
theorem Ta_entry_01 : Ta.entry 0 1 = 2 := by decide
theorem Ta_entry_10 : Ta.entry 1 0 = 3 := by decide

theorem cellOf_Ta_one : cellOf Ta 1 = (0, 0) := cellOf_one Ta card_ge_one

theorem cellOf_Ta_two : cellOf Ta 2 = (0, 1) := by
  apply cellOf_eq_of_entry Ta (c := (0, 1))
  · rw [YoungDiagram.mem_cells]; exact mem_mu21_iff.mpr (Or.inr (Or.inl ⟨rfl, rfl⟩))
  · exact Ta_entry_01

theorem Ta_sameRow12 : sameRow12 Ta := by
  unfold sameRow12; rw [cellOf_Ta_one, cellOf_Ta_two]

theorem Ta_mem_rowClass : Ta ∈ rowClass mu21 := by
  rw [rowClass, Finset.mem_filter]; exact ⟨Finset.mem_univ _, Ta_sameRow12⟩

/-- Pin a cell of `T` from its entry value and a membership proof. -/
private theorem entry_pin (T : StandardYoungTableau mu21) {k : ℕ}
    (hk : (k : ℕ) ∈ Set.Icc 1 mu21.cells.card) {p : ℕ × ℕ}
    (hpm : p ∈ mu21) (hpe : T.entry p.1 p.2 = k) : cellOf T k = p :=
  cellOf_eq_of_entry T ((YoungDiagram.mem_cells _).mpr hpm) hpe

/-- **Uniqueness**: every standard tableau of `(2,1)` with `1,2` in the same row
    is `T_a`. Determined by pinning the three cell entries (`encode` sees only the
    cells). -/
theorem eq_Ta (T : StandardYoungTableau mu21) (hT : sameRow12 T) : T = Ta := by
  have c1 : cellOf T 1 = (0, 0) := cellOf_one T card_ge_one
  have eT00 : T.entry 0 0 = 1 := entry_zero_zero_eq_one T card_ge_one
  have hk2 : (2 : ℕ) ∈ Set.Icc 1 mu21.cells.card := Set.mem_Icc.mpr ⟨by norm_num, card_ge_two⟩
  have hk3 : (3 : ℕ) ∈ Set.Icc 1 mu21.cells.card := Set.mem_Icc.mpr ⟨by norm_num, by simp [mu21_card]⟩
  obtain ⟨hmem2, hval2⟩ := cellOf_spec T (exists_cell_entry T hk2)
  obtain ⟨hmem3, hval3⟩ := cellOf_spec T (exists_cell_entry T hk3)
  have hrow2 : (cellOf T 2).1 = 0 := by
    have hh := hT; unfold sameRow12 at hh; rw [c1] at hh; exact hh.symm
  -- cellOf T 2 = (0,1)
  have c2 : cellOf T 2 = (0, 1) := by
    have hne : cellOf T 2 ≠ (0, 0) := by
      intro he; rw [he] at hval2
      have hv : T.entry 0 0 = 2 := hval2; omega
    rcases mem_mu21 ((YoungDiagram.mem_cells _).mp hmem2) with ⟨q1, q2⟩ | ⟨q1, q2⟩ | ⟨q1, q2⟩
    · exact absurd (Prod.ext_iff.mpr ⟨q1, q2⟩) hne
    · exact Prod.ext_iff.mpr ⟨q1, q2⟩
    · exact absurd (hrow2.symm.trans q1) Nat.zero_ne_one
  have eT01 : T.entry 0 1 = 2 := by have hh := hval2; rw [c2] at hh; exact hh
  -- cellOf T 3 = (1,0)
  have c3 : cellOf T 3 = (1, 0) := by
    have hne1 : cellOf T 3 ≠ (0, 0) := by
      intro he; rw [he] at hval3
      have hv : T.entry 0 0 = 3 := hval3; omega
    have hne2 : cellOf T 3 ≠ (0, 1) := by
      intro he; rw [he] at hval3
      have hv : T.entry 0 1 = 3 := hval3; omega
    rcases mem_mu21 ((YoungDiagram.mem_cells _).mp hmem3) with ⟨q1, q2⟩ | ⟨q1, q2⟩ | ⟨q1, q2⟩
    · exact absurd (Prod.ext_iff.mpr ⟨q1, q2⟩) hne1
    · exact absurd (Prod.ext_iff.mpr ⟨q1, q2⟩) hne2
    · exact Prod.ext_iff.mpr ⟨q1, q2⟩
  have eT10 : T.entry 1 0 = 3 := by have hh := hval3; rw [c3] at hh; exact hh
  -- ext over the cells (encode sees only cells)
  apply StandardYoungTableau.encode_injective
  funext c
  apply Fin.ext
  obtain ⟨⟨i, j⟩, hc⟩ := c
  show T.entry i j = Ta.entry i j
  rcases mem_mu21 ((YoungDiagram.mem_cells _).mp hc) with ⟨a, b⟩ | ⟨a, b⟩ | ⟨a, b⟩ <;>
    subst a <;> subst b
  · rw [eT00, Ta_entry_00]
  · rw [eT01, Ta_entry_01]
  · rw [eT10, Ta_entry_10]

/-- `rowClass (2,1) = {T_a}` — the same-row class is the single tableau `T_a`. -/
theorem rowClass_mu21 : rowClass mu21 = {Ta} := by
  apply Finset.eq_singleton_iff_unique_mem.mpr
  refine ⟨Ta_mem_rowClass, fun T hT => ?_⟩
  rw [rowClass, Finset.mem_filter] at hT
  exact eq_Ta T hT.2

/-- **`c_λ((2,1)) = 1`** — the σ₁ character coefficient for the hook `(2,1)`. -/
theorem card_rowClass_mu21 : (rowClass mu21).card = 1 := by
  rw [rowClass_mu21, Finset.card_singleton]

/-- **`#SYT((2,1)) = 2`** — the hook has exactly two standard tableaux. -/
theorem card_SYT_mu21 : Fintype.card (StandardYoungTableau mu21) = 2 := by
  have hkey := two_mul_card_rowClass_eq_card mu21_transpose card_ge_two
  rw [card_rowClass_mu21] at hkey; omega

end QOU.BraidKnot.SytSmallShapeCounts
