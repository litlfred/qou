/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.QuantumGLCommutant

/-!
# `dim HW_μ = f^μ`: the equality half of G3.4c

Bean `qou-gl343`. `finrank_hwSpace_le_numSYT` gives `dim HW_μ ≤ f^μ` for every dominant `μ`.
This file proves equality, over a linearly ordered field at `q` not a root of unity.

The argument is a squeeze. `range_jimbo_eq_commutant` (G3.4) and `finrank_range_jimbo` give
`Σ_λ (f^λ)² = dim ρ(H) = dim B' ≤ Σ_μ (dim HW_μ)²`, where `λ` runs over partitions of `m+1`
with at most `d` rows. `hstar_occWeights` gives the reverse inequality. Each term is bounded
termwise, and the map `μ ↦ λ(μ)` from dominant occurring weights to such partitions is injective,
so equality of the sums forces equality of every term.

* `sum_sq_finrank_hwSpace_eq`: `Σ_μ (dim HW_μ)² = Σ_λ (f^λ)²`.
* `finrank_hwSpace_eq_numSYT`: `dim HW_μ = f^μ` for every dominant `μ` of total weight `m+1`.

The isomorphism `HW_λ ≅ S_λ` of `H`-modules is not proved here.

## Base ring (§7c)

A linearly ordered field `L` (strict ordered ring), inherited from `range_jimbo_eq_commutant`,
whose complete-reducibility step uses an anisotropic dot product. The any-field case is #7874.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.SchurWeyl.JimboGL QOU.Mathlib YoungDiagram

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] {d : ℕ} [NeZero d]

/-- **`Σ_μ (dim HW_μ)² = Σ_{λ ⊢ m+1, ℓ(λ) ≤ d} (f^λ)²`.** -/
theorem sum_sq_finrank_hwSpace_eq (q : L) (hq : q ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    ∑ μ ∈ occWeights d m, Module.finrank L (hwSpace q m μ) ^ 2
      = ∑ lam : RowCapIdx d m,
          Fintype.card (StandardYoungTableau (partitionShape lam.1)) ^ 2 := by
  have hq2 := sub_inv_ne_zero_of_notRootOfUnity hq hgen
  refine le_antisymm (hstar_occWeights q hq hq2 hgen m) ?_
  rw [← finrank_range_jimbo q hq hgen m, range_jimbo_eq_commutant q hq hgen m]
  exact finrank_commutant_le q m

omit [LinearOrder L] [IsStrictOrderedRing L] [NeZero d] in
/-- A highest-weight space of a non-occurring weight is zero. -/
theorem hwSpace_eq_bot_of_not_mem (q : L) (m : ℕ) {μ : Fin d → ℕ} (hμ : μ ∉ occWeights d m) :
    hwSpace q m μ = ⊥ := by
  rw [Submodule.eq_bot_iff]
  rintro v ⟨hv, -⟩
  rw [← hv, weightProj_eq_zero_of_not_mem hμ, Matrix.zero_mulVec]

/-- **`dim HW_μ = f^μ`** for every dominant weight `μ` of total weight `m + 1`. -/
theorem finrank_hwSpace_eq_numSYT (q : L) (hq : q ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) (μ₀ : Fin d → ℕ) (hμ₀ : IsDom μ₀)
    (hs₀ : ∑ y, μ₀ y = m + 1) :
    Module.finrank L (hwSpace q m μ₀) = numStandardYoungTableaux (rowDiagram μ₀ hμ₀) := by
  classical
  have hq2 := sub_inv_ne_zero_of_notRootOfUnity hq hgen
  set S := occWeights d m
  set S' := insert μ₀ S
  let P : (Fin d → ℕ) → Prop := fun μ => IsDom μ ∧ ∑ y, μ y = m + 1
  let a : (Fin d → ℕ) → ℕ := fun μ => Module.finrank L (hwSpace q m μ) ^ 2
  let b : (Fin d → ℕ) → ℕ := fun μ =>
    if h : P μ then numStandardYoungTableaux (rowDiagram μ h.1) ^ 2 else 0
  -- termwise bound
  have hab : ∀ μ, a μ ≤ b μ := by
    intro μ
    by_cases h : P μ
    · simp only [a, b, dif_pos h]
      exact Nat.pow_le_pow_left (finrank_hwSpace_le_numSYT q hq hq2 hgen m μ h.1) 2
    · simp only [b, dif_neg h]
      have : hwSpace q m μ = ⊥ := by
        by_contra hne
        apply h
        refine ⟨isDom_of_ne_bot q hq hq2 hgen m μ hne, ?_⟩
        by_contra hs
        exact hne (hwSpace_eq_bot_of_sum_ne q m μ hs)
      simp [a, this]
  -- the extra point contributes nothing to `a`
  have haS : ∑ μ ∈ S', a μ = ∑ μ ∈ S, a μ := by
    show ∑ μ ∈ insert μ₀ S, a μ = _
    by_cases h : μ₀ ∈ S
    · rw [Finset.insert_eq_of_mem h]
    · rw [Finset.sum_insert h]
      simp [a, hwSpace_eq_bot_of_not_mem q m h]
  -- `Σ_{S'} b ≤ Σ_λ (f^λ)²` by injectivity of `μ ↦ λ(μ)`
  have hbS : ∑ μ ∈ S', b μ ≤ ∑ lam : RowCapIdx d m,
      Fintype.card (StandardYoungTableau (partitionShape lam.1)) ^ 2 := by
    rw [← Finset.sum_filter_add_sum_filter_not S' P]
    have hzero : ∑ μ ∈ S'.filter (fun μ => ¬ P μ), b μ = 0 :=
      Finset.sum_eq_zero fun μ hμ => by simp only [b, dif_neg (Finset.mem_filter.mp hμ).2]
    rw [hzero, add_zero]
    set T := S'.filter P
    let φ : T → RowCapIdx d m := fun μ =>
      toRowCap m μ.1 (Finset.mem_filter.mp μ.2).2.1 (Finset.mem_filter.mp μ.2).2.2
    have hφ : Function.Injective φ := by
      intro μ ν h
      have := congrArg (fun l : RowCapIdx d m => partitionShape l.1) h
      simp only [φ, partitionShape_toRowCap] at this
      exact Subtype.ext (rowDiagram_injective _ _ this)
    rw [← Finset.sum_attach T]
    have hg : ∀ μ ∈ T.attach,
        b μ.1 = Fintype.card (StandardYoungTableau (partitionShape (φ μ).1)) ^ 2 := by
      intro μ _
      simp only [b, φ, dif_pos (Finset.mem_filter.mp μ.2).2, partitionShape_toRowCap,
        ← Nat.card_eq_fintype_card]
      rfl
    rw [Finset.sum_congr rfl hg,
      ← Finset.sum_image (f := fun lam : RowCapIdx d m =>
        Fintype.card (StandardYoungTableau (partitionShape lam.1)) ^ 2)
        (fun x _ y _ h => hφ h)]
    exact Finset.sum_le_sum_of_subset (Finset.subset_univ _)
  -- the squeeze
  have hsum : ∑ μ ∈ S', a μ = ∑ μ ∈ S', b μ := by
    refine le_antisymm (Finset.sum_le_sum fun μ _ => hab μ) ?_
    rw [haS]
    exact hbS.trans (sum_sq_finrank_hwSpace_eq q hq hgen m).ge
  have h0 := (Finset.sum_eq_sum_iff_of_le fun μ _ => hab μ).mp hsum μ₀ (Finset.mem_insert_self _ _)
  simp only [a, b, dif_pos (show P μ₀ from ⟨hμ₀, hs₀⟩)] at h0
  exact Nat.pow_left_injective two_ne_zero h0

end QOU.SchurWeyl.QuantumGL
