import QOU.KZ.Drinfeld.Legs

/-!
# The flip as an `sl₂` Casimir on two legs

Stage S2 of bean `qou-zoyv`. With `e = E₀₁`, `f = E₁₀`, `h = E₀₀ − E₁₁` and `i ≠ j`:

  `P_{ij} = e^{(i)} f^{(j)} + f^{(i)} e^{(j)} + ½ h^{(i)} h^{(j)} + ½`   (`flip_eq_casimir`).

So the `sl₂` block Casimir `t^{sl}_{S,T} = E^S F^T + F^S E^T + ½ H^S H^T` equals
`t_{S,T} − ½ |S||T|`, where `E^S = ∑_{i ∈ S} e^{(i)}`. This form is what equivariant maps
intertwine.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues

/-- The `sl₂` generators. -/
def eS : Matrix (Fin 2) (Fin 2) ℂ := !![0, 1; 0, 0]
def fS : Matrix (Fin 2) (Fin 2) ℂ := !![0, 0; 1, 0]
def hS : Matrix (Fin 2) (Fin 2) ℂ := !![1, 0; 0, -1]

theorem trace_eS : eS.trace = 0 := by simp [eS, Matrix.trace, Fin.sum_univ_two]
theorem trace_fS : fS.trace = 0 := by simp [fS, Matrix.trace, Fin.sum_univ_two]
theorem trace_hS : hS.trace = 0 := by simp [hS, Matrix.trace, Fin.sum_univ_two]

variable {L : Type*} [Fintype L] [DecidableEq L]

/-- Entries of a product of operators on two distinct legs. -/
theorem leafOp_mul_leafOp_apply {i j : L} (hij : i ≠ j) (a b : Matrix (Fin 2) (Fin 2) ℂ)
    (y x : L → Fin 2) :
    (leafOp i a * leafOp j b) y x =
      a (y i) (x i) * b (y j) (x j) * if ∀ k, k ≠ i → k ≠ j → y k = x k then 1 else 0 := by
  rw [Matrix.mul_apply]
  rw [Finset.sum_eq_single (Function.update y i (x i))]
  · simp only [leafOp, Matrix.of_apply, Function.update_self, Function.update_of_ne hij.symm]
    by_cases h : ∀ k, k ≠ i → k ≠ j → y k = x k
    · rw [if_pos h, if_pos, if_pos, mul_one, mul_one, mul_one]
      · intro k hk
        by_cases hki : k = i
        · subst hki; simp
        · rw [Function.update_of_ne hki]; exact h k hki hk
      · intro k hk; rw [Function.update_of_ne hk]
    · rw [if_neg h, mul_zero]
      by_cases h2 : ∀ k, k ≠ j → Function.update y i (x i) k = x k
      · exfalso; apply h; intro k hki hkj
        have := h2 k hkj; rwa [Function.update_of_ne hki] at this
      · rw [if_neg h2]; simp
  · intro z _ hz
    simp only [leafOp, Matrix.of_apply]
    by_cases h1 : ∀ k, k ≠ i → y k = z k
    · by_cases h2 : ∀ k, k ≠ j → z k = x k
      · exfalso; apply hz; funext k
        by_cases hki : k = i
        · subst hki; rw [Function.update_self]; exact h2 k hij
        · rw [Function.update_of_ne hki]; exact (h1 k hki).symm
      · rw [if_neg h2]; simp
    · rw [if_neg h1]; simp
  · simp

/-- **The flip as a two-leg `sl₂` Casimir.** -/
theorem flip_eq_casimir {i j : L} (hij : i ≠ j) :
    flipL ℂ 2 i j = leafOp i eS * leafOp j fS + leafOp i fS * leafOp j eS +
      (1 / 2 : ℂ) • (leafOp i hS * leafOp j hS) + (1 / 2 : ℂ) • 1 := by
  ext y x
  simp only [Matrix.add_apply, Matrix.smul_apply, smul_eq_mul, leafOp_mul_leafOp_apply hij,
    Matrix.one_apply, flipL, permL, permMat, Matrix.of_apply]
  by_cases h : ∀ k, k ≠ i → k ≠ j → y k = x k
  · simp only [if_pos h, mul_one]
    have hyx : (x ∘ Equiv.swap i j = y) ↔ (x j = y i ∧ x i = y j) := by
      constructor
      · intro e; exact ⟨by rw [← e]; simp, by rw [← e]; simp [Equiv.swap_apply_right]⟩
      · rintro ⟨h1, h2⟩; funext k
        by_cases hki : k = i
        · subst hki; simpa using h1
        · by_cases hkj : k = j
          · subst hkj; simpa [Equiv.swap_apply_right] using h2
          · simp [Equiv.swap_apply_of_ne_of_ne hki hkj, h k hki hkj]
    have hyx' : (y = x) ↔ (y i = x i ∧ y j = x j) := by
      constructor
      · rintro rfl; exact ⟨rfl, rfl⟩
      · rintro ⟨h1, h2⟩; funext k
        by_cases hki : k = i
        · subst hki; exact h1
        · by_cases hkj : k = j
          · subst hkj; exact h2
          · exact h k hki hkj
    rw [if_congr hyx rfl rfl, if_congr hyx' rfl rfl]
    generalize y i = a, x i = b, y j = c', x j = d
    fin_cases a <;> fin_cases b <;> fin_cases c' <;> fin_cases d <;> norm_num [eS, fS, hS]
  · simp only [if_neg h, mul_zero, zero_add]
    have h1 : ¬ (x ∘ Equiv.swap i j = y) := by
      intro e; apply h; intro k hki hkj; rw [← e]
      simp [Equiv.swap_apply_of_ne_of_ne hki hkj]
    have h2 : ¬ (y = x) := by rintro rfl; exact h (fun _ _ _ => rfl)
    rw [if_neg h1, if_neg h2]; ring

end QOU.KZ.Drinfeld
