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

open Pointwise

/-- The cone over `B`: the nonnegative multiples of points of `B`. -/
def rayHull (B : Set E) : Set E := {y | ∃ l : ℝ, 0 ≤ l ∧ ∃ q ∈ B, y = l • q}

lemma convex_rayHull {B : Set E} (hB : Convex ℝ B) : Convex ℝ (rayHull B) := by
  rintro _ ⟨l, hl, q, hq, rfl⟩ _ ⟨l', hl', q', hq', rfl⟩ s t hs ht hst
  by_cases hL : s * l + t * l' = 0
  · have e1 : s * l = 0 := by nlinarith [mul_nonneg hs hl, mul_nonneg ht hl']
    have e2 : t * l' = 0 := by nlinarith [mul_nonneg hs hl, mul_nonneg ht hl']
    exact ⟨0, le_rfl, q, hq, by rw [smul_smul, smul_smul, e1, e2]; simp⟩
  · have hLpos : 0 < s * l + t * l' :=
      lt_of_le_of_ne (add_nonneg (mul_nonneg hs hl) (mul_nonneg ht hl')) (Ne.symm hL)
    refine ⟨s * l + t * l', hLpos.le,
      (s * l / (s * l + t * l')) • q + (t * l' / (s * l + t * l')) • q',
      hB hq hq' (div_nonneg (mul_nonneg hs hl) hLpos.le)
        (div_nonneg (mul_nonneg ht hl') hLpos.le) (by rw [← add_div, div_self hL]), ?_⟩
    have h1 : (s * l + t * l') * (s * l / (s * l + t * l')) = s * l := by field_simp
    have h2 : (s * l + t * l') * (t * l' / (s * l + t * l')) = t * l' := by field_simp
    simp only [smul_add, smul_smul, h1, h2]

lemma zero_mem_rayHull {B : Set E} {q : E} (hq : q ∈ B) : (0 : E) ∈ rayHull B :=
  ⟨0, le_rfl, q, hq, by simp⟩

/-- **The body around the Δ-triangle**: the convex hull of `a`, `b`, and the closed `ρ`-balls
around the midpoint `m` of `[a, b]` and around `c`. -/
def deltaBody (a b c : E) (ρ : ℝ) : Set E :=
  convexHull ℝ (({a, b} ∪ closedBall (midpoint ℝ a b) ρ) ∪ closedBall c ρ)

variable {a b c : E} {ρ : ℝ}

lemma deltaBody_comm : deltaBody a b c ρ = deltaBody b a c ρ := by
  unfold deltaBody
  rw [pair_comm, midpoint_comm]

lemma deltaBody_mono {ρ' : ℝ} (h : ρ ≤ ρ') : deltaBody a b c ρ ⊆ deltaBody a b c ρ' :=
  convexHull_mono (union_subset_union (union_subset_union_right _ (closedBall_subset_closedBall h))
    (closedBall_subset_closedBall h))

/-- **Seen from the apex `a`**, the body lies in the cone over the two balls. -/
lemma deltaBody_apex (hρ : 0 ≤ ρ) {x : E} (hx : x ∈ deltaBody a b c ρ) :
    x - a ∈ rayHull (closedBall (midpoint ℝ a b - a) ρ) + rayHull (closedBall (c - a) ρ) := by
  set C := rayHull (closedBall (midpoint ℝ a b - a) ρ) + rayHull (closedBall (c - a) ρ)
  have hC : Convex ℝ C :=
    (convex_rayHull (convex_closedBall _ _)).add (convex_rayHull (convex_closedBall _ _))
  have h01 := zero_mem_rayHull (mem_closedBall_self hρ : midpoint ℝ a b - a ∈ _)
  have h02 := zero_mem_rayHull (mem_closedBall_self hρ : c - a ∈ closedBall (c - a) ρ)
  have hsub : (({a, b} ∪ closedBall (midpoint ℝ a b) ρ) ∪ closedBall c ρ) ⊆
      (fun x => -a + x) ⁻¹' C := by
    intro y hy
    simp only [mem_preimage, neg_add_eq_sub]
    rcases hy with (hy | hy) | hy
    · rcases hy with rfl | hy
      · exact ⟨0, h01, 0, h02, by simp⟩
      · rw [mem_singleton_iff] at hy
        subst hy
        refine ⟨(2 : ℝ) • (midpoint ℝ a y - a), ⟨2, by norm_num, _, mem_closedBall_self hρ, rfl⟩,
          0, h02, ?_⟩
        show (2 : ℝ) • (midpoint ℝ a y - a) + 0 = y - a
        rw [add_zero, midpoint_sub_left, smul_smul]
        norm_num
    · refine ⟨y - a, ⟨1, zero_le_one, y - a, ?_, (one_smul _ _).symm⟩, 0, h02, add_zero _⟩
      rw [mem_closedBall, dist_sub_right]; exact hy
    · refine ⟨0, h01, y - a, ⟨1, zero_le_one, y - a, ?_, (one_smul _ _).symm⟩, zero_add _⟩
      rw [mem_closedBall, dist_sub_right]; exact hy
  have := convexHull_min hsub (hC.translate_preimage_right (-a)) hx
  simpa [neg_add_eq_sub] using this

/-- **Points outside the perturbed cone at `a` are outside the body.** -/
lemma not_mem_deltaBody_of_cone (hρ : 0 ≤ ρ) {w : E}
    (hcone : ∀ l₁ l₂ : ℝ, 0 ≤ l₁ → 0 ≤ l₂ → ∀ q₁ ∈ closedBall (midpoint ℝ a b - a) ρ,
      ∀ q₂ ∈ closedBall (c - a) ρ, w ≠ l₁ • q₁ + l₂ • q₂) {t : ℝ} (ht : 0 < t) :
    a + t • w ∉ deltaBody a b c ρ := by
  intro h
  obtain ⟨y₁, ⟨l₁, hl₁, q₁, hq₁, rfl⟩, y₂, ⟨l₂, hl₂, q₂, hq₂, rfl⟩, he⟩ :=
    Set.mem_add.mp (deltaBody_apex hρ h)
  apply hcone (l₁ / t) (l₂ / t) (div_nonneg hl₁ ht.le) (div_nonneg hl₂ ht.le) q₁ hq₁ q₂ hq₂
  have htw : t • w = l₁ • q₁ + l₂ • q₂ := by rw [he]; abel
  calc w = t⁻¹ • (t • w) := by rw [smul_smul, inv_mul_cancel₀ ht.ne', one_smul]
    _ = _ := by rw [htw, smul_add, smul_smul, smul_smul, div_eq_inv_mul, div_eq_inv_mul]

/-- **The body lies within `ρ` of the triangle.** -/
lemma deltaBody_subset_cthickening :
    deltaBody a b c ρ ⊆ cthickening ρ (convexHull ℝ {a, b, c}) := by
  refine convexHull_min ?_ ((convex_convexHull ℝ _).cthickening ρ)
  have ha : a ∈ convexHull ℝ {a, b, c} := subset_convexHull ℝ _ (by simp)
  have hb : b ∈ convexHull ℝ {a, b, c} := subset_convexHull ℝ _ (by simp)
  have hc : c ∈ convexHull ℝ {a, b, c} := subset_convexHull ℝ _ (by simp)
  have hm : midpoint ℝ a b ∈ convexHull ℝ {a, b, c} :=
    segment_subset_convexHull (by simp) (by simp) (midpoint_mem_segment a b)
  rintro y ((hy | hy) | hy)
  · rcases hy with rfl | hy
    · exact self_subset_cthickening _ ha
    · rw [mem_singleton_iff] at hy; subst hy; exact self_subset_cthickening _ hb
  · exact closedBall_subset_cthickening hm ρ hy
  · exact closedBall_subset_cthickening hc ρ hy

lemma convex_deltaBody : Convex ℝ (deltaBody a b c ρ) := convex_convexHull ℝ _

lemma midpoint_mem_interior_deltaBody (hρ : 0 < ρ) :
    midpoint ℝ a b ∈ interior (deltaBody a b c ρ) :=
  mem_interior.mpr ⟨ball (midpoint ℝ a b) ρ, fun _ hy => subset_convexHull ℝ _
    (Or.inl (Or.inr (ball_subset_closedBall hy))), isOpen_ball, mem_ball_self hρ⟩

lemma mem_interior_deltaBody (hρ : 0 < ρ) : c ∈ interior (deltaBody a b c ρ) :=
  mem_interior.mpr ⟨ball c ρ, fun _ hy => subset_convexHull ℝ _
    (Or.inr (ball_subset_closedBall hy)), isOpen_ball, mem_ball_self hρ⟩

lemma left_mem_deltaBody : a ∈ deltaBody a b c ρ := subset_convexHull ℝ _ (by simp)

end QOU.MathlibExt.PL
