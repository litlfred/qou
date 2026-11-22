/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLAmbientIsotopy
import QOU.MathlibExt.PLPush
import Mathlib.Topology.Order.Compact

set_option autoImplicit false

/-!
# A Δ-move is an ambient isotopy (issue #8902, stage 2, part 5)

Work in progress. This file builds the convex body around the Δ-triangle on which the push of
`PLPush.lean` is applied.

## What is a THEOREM here

* `cone_stable` — if `w` is outside the cone spanned by `u₁, u₂` and `0 ∉ [u₁, u₂]`, then for
  some `ρ > 0` it stays outside the cone spanned by the closed `ρ`-balls around `u₁` and `u₂`.
  This is what keeps the edges at the apexes `a`, `b` of the triangle out of the body.

## What is NOT proved here (yet)

* The choice of the body and the assembly of the isotopy for `Move.delta`.
-/

namespace QOU.MathlibExt.PL

open Set Metric

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- **Cones are stable under small perturbation of their generators**, away from `0`. -/
theorem cone_stable {u₁ u₂ w : E} (hseg : ∀ θ ∈ Icc (0 : ℝ) 1, (1 - θ) • u₁ + θ • u₂ ≠ 0)
    (hw : ∀ l₁ l₂ : ℝ, 0 ≤ l₁ → 0 ≤ l₂ → w ≠ l₁ • u₁ + l₂ • u₂) :
    ∃ ρ > 0, ∀ l₁ l₂ : ℝ, 0 ≤ l₁ → 0 ≤ l₂ → ∀ q₁ ∈ closedBall u₁ ρ, ∀ q₂ ∈ closedBall u₂ ρ,
      w ≠ l₁ • q₁ + l₂ • q₂ := by
  set p : ℝ → E := fun θ => (1 - θ) • u₁ + θ • u₂ with hp
  have hpc : Continuous p := ((continuous_const.sub continuous_id).smul continuous_const).add
    (continuous_id.smul continuous_const)
  -- `γ`: the least norm on the segment
  obtain ⟨θ₀, hθ₀, hγmin⟩ := isCompact_Icc.exists_isMinOn (nonempty_Icc.mpr zero_le_one)
    (continuous_norm.comp hpc).continuousOn
  set γ := ‖p θ₀‖
  have hγ : 0 < γ := norm_pos_iff.mpr (hseg θ₀ hθ₀)
  have hγle : ∀ θ ∈ Icc (0 : ℝ) 1, γ ≤ ‖p θ‖ := fun θ hθ => hγmin hθ
  have hw0 : w ≠ 0 := fun h => hw 0 0 le_rfl le_rfl (by simp [h])
  set M := 2 * ‖w‖ / γ
  have hM : 0 ≤ M := by positivity
  -- `δ`: the least distance from `w` to the truncated cone
  set f : ℝ × ℝ → ℝ := fun x => ‖w - x.1 • p x.2‖
  have hfc : Continuous f :=
    continuous_norm.comp (continuous_const.sub (continuous_fst.smul (hpc.comp continuous_snd)))
  have hK : IsCompact (Icc (0 : ℝ) M ×ˢ Icc (0 : ℝ) 1) := isCompact_Icc.prod isCompact_Icc
  obtain ⟨x₀, hx₀, hδmin⟩ := hK.exists_isMinOn
    ((nonempty_Icc.mpr hM).prod (nonempty_Icc.mpr zero_le_one)) hfc.continuousOn
  set δ := f x₀
  have hδ : 0 < δ := by
    apply norm_pos_iff.mpr
    intro h
    obtain ⟨⟨h1, -⟩, ⟨h3, h4⟩⟩ := hx₀
    apply hw (x₀.1 * (1 - x₀.2)) (x₀.1 * x₀.2) (mul_nonneg h1 (by linarith)) (mul_nonneg h1 h3)
    rw [sub_eq_zero] at h
    rw [h]
    simp only [p, smul_add, smul_smul]
  refine ⟨min (γ / 2) (δ / (M + 1)), by positivity, ?_⟩
  intro l₁ l₂ hl₁ hl₂ q₁ hq₁ q₂ hq₂ heq
  set ρ := min (γ / 2) (δ / (M + 1))
  have hργ : ρ ≤ γ / 2 := min_le_left _ _
  have hρδ : ρ ≤ δ / (M + 1) := min_le_right _ _
  set Λ := l₁ + l₂
  have hΛ : 0 < Λ := by
    rcases (add_nonneg hl₁ hl₂).lt_or_eq with h | h
    · exact h
    · exfalso
      have e1 : l₁ = 0 := by linarith
      have e2 : l₂ = 0 := by linarith
      exact hw0 (by rw [heq, e1, e2]; simp)
  set θ := l₂ / Λ
  have hθ : θ ∈ Icc (0 : ℝ) 1 :=
    ⟨div_nonneg hl₂ hΛ.le, (div_le_one hΛ).mpr (by linarith)⟩
  have hsplit : l₁ • q₁ + l₂ • q₂ = Λ • p θ + (l₁ • (q₁ - u₁) + l₂ • (q₂ - u₂)) := by
    have h2 : Λ * θ = l₂ := mul_div_cancel₀ l₂ hΛ.ne'
    have h1 : Λ * (1 - θ) = l₁ := by rw [mul_sub, mul_one, h2]; simp only [Λ]; ring
    simp only [p, smul_add, smul_smul, h1, h2, smul_sub]
    abel
  have herr : ‖l₁ • (q₁ - u₁) + l₂ • (q₂ - u₂)‖ ≤ Λ * ρ := by
    refine (norm_add_le _ _).trans ?_
    rw [norm_smul, norm_smul, Real.norm_of_nonneg hl₁, Real.norm_of_nonneg hl₂,
      ← dist_eq_norm, ← dist_eq_norm]
    have := mul_le_mul_of_nonneg_left (mem_closedBall.mp hq₁) hl₁
    have := mul_le_mul_of_nonneg_left (mem_closedBall.mp hq₂) hl₂
    simp only [Λ]; nlinarith
  have hfar : ‖w - Λ • p θ‖ ≤ Λ * ρ := by
    rw [heq, hsplit, add_sub_cancel_left]; exact herr
  -- `Λ ≤ M`
  have hΛM : Λ ≤ M := by
    have h1 : Λ * γ ≤ ‖Λ • p θ‖ := by
      rw [norm_smul, Real.norm_of_nonneg hΛ.le]
      exact mul_le_mul_of_nonneg_left (hγle θ hθ) hΛ.le
    have h2 : ‖Λ • p θ‖ ≤ ‖w‖ + Λ * ρ := by
      have := norm_sub_norm_le (Λ • p θ) w
      rw [norm_sub_rev] at this
      linarith
    have h3 : Λ * ρ ≤ Λ * (γ / 2) := mul_le_mul_of_nonneg_left hργ hΛ.le
    simp only [M]
    rw [le_div_iff₀ hγ]
    linarith
  have hmin : δ ≤ ‖w - Λ • p θ‖ := hδmin (show (Λ, θ) ∈ _ from ⟨⟨hΛ.le, hΛM⟩, hθ⟩)
  have : Λ * ρ < δ := by
    calc Λ * ρ ≤ M * (δ / (M + 1)) := mul_le_mul hΛM hρδ (by positivity) hM
      _ < δ := by
        rw [mul_div_assoc', div_lt_iff₀ (by linarith)]
        nlinarith
  linarith

end QOU.MathlibExt.PL
