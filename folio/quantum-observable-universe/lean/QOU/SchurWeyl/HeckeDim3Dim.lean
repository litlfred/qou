import QOU.SchurWeyl.HeckeDim3
import QOU.SchurWeyl.HeckeDim3Indep
import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# QOU.SchurWeyl.HeckeDim3Dim — `finrank_ℝ H_3(q) = 6` (SW-7 capstone, dimension)

Packages the two bounds of the Iwahori–Hecke basis theorem at `n = 3` into the
single dimension statement.  The six reduced words
`{1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}` form a **basis** of `H_3(q) = Hecke ℝ q q⁻¹ 2`
for `q ≠ 0`:

* **span** `⊤` — `HeckeDim3.span_sixWords_eq_top` (dim ≤ 6, on `main`),
* **linear independence** — `HeckeDim3Indep.sixWords_indep` (dim ≥ 6, on `main`),

so `Module.finrank ℝ (H_3(q)) = 6 = 3!`.  This is the dimension half of R2-inst at
`n = 3`; the matching Wedderburn *isomorphism* `H_3(q) ≅ ℝ × ℝ × M₂(ℝ)` is
assembled separately from the same three irreps.

Base ring `ℝ` (the seminormal rep used for independence is archimedean, §7c).

LaTeX label: `prop:hecke3-dim-six`
-/

namespace QOU.SchurWeyl

open Hecke Matrix

section Dim

variable (q : ℝ)

local notation3 "t₀" => σ ℝ q q⁻¹ 2 0
local notation3 "t₁" => σ ℝ q q⁻¹ 2 1

/-- The six reduced words `{T_w : w ∈ S_3}` as an indexed family `Fin 6 → H_3(q)`. -/
noncomputable def sixFamily : Fin 6 → Hecke ℝ q q⁻¹ 2 :=
  ![1, t₀, t₁, t₀ * t₁, t₁ * t₀, t₀ * t₁ * t₀]

/-- The six words are linearly independent over `ℝ` (`q ≠ 0`) — index-family form
of `sixWords_indep`. -/
theorem sixFamily_indep (hq : q ≠ 0) : LinearIndependent ℝ (sixFamily q) := by
  rw [Fintype.linearIndependent_iff]
  intro g hg
  simp only [sixFamily, Fin.sum_univ_six, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val] at hg
  obtain ⟨h1, h2, h3, h4, h5, h6⟩ :=
    sixWords_indep q hq (g 0) (g 1) (g 2) (g 3) (g 4) (g 5) hg
  intro i
  fin_cases i <;> assumption

/-- The six reduced words form a **basis** of `H_3(q)` (`q ≠ 0`). -/
noncomputable def sixBasis (hq : q ≠ 0) : Module.Basis (Fin 6) ℝ (Hecke ℝ q q⁻¹ 2) :=
  Module.Basis.mk (sixFamily_indep q hq) (by
    have hsub : HeckeDim3.sixWords (q := q) (qi := q⁻¹) ⊆ Set.range (sixFamily q) := by
      intro x hx
      simp only [HeckeDim3.sixWords, Set.mem_insert_iff, Set.mem_singleton_iff] at hx
      rcases hx with rfl | rfl | rfl | rfl | rfl | rfl
      · exact ⟨0, by simp [sixFamily]⟩
      · exact ⟨1, by simp [sixFamily]⟩
      · exact ⟨2, by simp [sixFamily]⟩
      · exact ⟨3, by simp [sixFamily]⟩
      · exact ⟨4, by simp [sixFamily]⟩
      · exact ⟨5, by simp [sixFamily]⟩
    calc (⊤ : Submodule ℝ (Hecke ℝ q q⁻¹ 2))
        = Submodule.span ℝ (HeckeDim3.sixWords (q := q) (qi := q⁻¹)) :=
          (HeckeDim3.span_sixWords_eq_top).symm
      _ ≤ Submodule.span ℝ (Set.range (sixFamily q)) := Submodule.span_mono hsub)

/-- **`dim_ℝ H_3(q) = 6`** (`q ≠ 0`) — the Iwahori–Hecke basis theorem `dim H_n(q) = n!`
at `n = 3`. -/
theorem finrank_hecke3 (hq : q ≠ 0) :
    Module.finrank ℝ (Hecke ℝ q q⁻¹ 2) = 6 := by
  rw [Module.finrank_eq_card_basis (sixBasis q hq), Fintype.card_fin]

end Dim

end QOU.SchurWeyl
