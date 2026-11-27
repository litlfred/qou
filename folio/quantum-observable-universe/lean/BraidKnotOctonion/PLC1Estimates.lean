/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.Normed.Module.Ray

set_option autoImplicit false

/-!
# Elementary estimates for the C¹ bridge (issue #8902)

Two scale-free inequalities used to show that fine inscribed polygons of a C¹ image of a
polygonal link are simple.

## What is a THEOREM here

* `exists_pos_mul_le_norm_smul_sub` — **angle bound.** For nonzero `u, w` not on the same ray,
  some `κ > 0` has `κ (α ‖u‖ + β ‖w‖) ≤ ‖α u - β w‖` for all `α, β ≥ 0` (inner product spaces).
* `norm_chord_sub_le` — **chord deviation.** If `‖Df - φ‖ ≤ ε` on `[x, y]`, the chord of `f`
  over `[x, y]` stays within `2 ε ‖y - x‖` of the image of the segment.
* `norm_sub_sub_le` — the first-order estimate `‖f y - f x - φ (y - x)‖ ≤ ε ‖y - x‖`.
-/

namespace QOU.MathlibExt.PL

open Set

section Angle

variable {F : Type*} [NormedAddCommGroup F] [InnerProductSpace ℝ F]

/-- **Angle bound.** Two directions that are not on the same ray stay apart in a scale-free
way. -/
theorem exists_pos_mul_le_norm_smul_sub {u w : F} (hu : u ≠ 0) (hw : w ≠ 0)
    (h : ¬ SameRay ℝ u w) :
    ∃ κ > 0, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β → κ * (α * ‖u‖ + β * ‖w‖) ≤ ‖α • u - β • w‖ := by
  set a := ‖u‖
  set b := ‖w‖
  set p := inner ℝ u w
  have ha : 0 < a := norm_pos_iff.mpr hu
  have hb : 0 < b := norm_pos_iff.mpr hw
  have hp : p < a * b := by
    refine lt_of_le_of_ne (real_inner_le_norm u w) fun he => h ?_
    rw [sameRay_iff_norm_smul_eq]
    exact (inner_eq_norm_mul_iff_real.mp he).symm
  set c := p / (a * b)
  have hc : c < 1 := by rw [div_lt_one (by positivity)]; exact hp
  have hc' : -1 ≤ c := by
    rw [le_div_iff₀ (by positivity)]
    have := abs_real_inner_le_norm u w
    linarith [neg_abs_le p]
  refine ⟨Real.sqrt ((1 - c) / 2), Real.sqrt_pos.mpr (by linarith), fun α β hα hβ => ?_⟩
  set X := α * a
  set Y := β * b
  have hX : 0 ≤ X := by positivity
  have hY : 0 ≤ Y := by positivity
  have hsq : ‖α • u - β • w‖ ^ 2 = X ^ 2 + Y ^ 2 - 2 * c * X * Y := by
    rw [norm_sub_sq_real, norm_smul, norm_smul, real_inner_smul_left, real_inner_smul_right,
      Real.norm_of_nonneg hα, Real.norm_of_nonneg hβ]
    simp only [c, X, Y]
    field_simp
    ring
  have key : (1 - c) / 2 * (X + Y) ^ 2 ≤ ‖α • u - β • w‖ ^ 2 := by
    rw [hsq]; nlinarith [sq_nonneg (X - Y)]
  have := Real.sqrt_le_sqrt key
  rwa [Real.sqrt_mul (by linarith), Real.sqrt_sq (by positivity),
    Real.sqrt_sq (norm_nonneg _)] at this

end Angle

section Chord

variable {E G : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup G] [NormedSpace ℝ G]

/-- **First-order estimate** on a segment. -/
theorem norm_sub_sub_le {f : E → G} {φ : E →L[ℝ] G} {ε : ℝ} {x y : E}
    (hd : ∀ z ∈ segment ℝ x y, DifferentiableAt ℝ f z)
    (hε : ∀ z ∈ segment ℝ x y, ‖fderiv ℝ f z - φ‖ ≤ ε) :
    ‖f y - f x - φ (y - x)‖ ≤ ε * ‖y - x‖ :=
  (convex_segment x y).norm_image_sub_le_of_norm_fderiv_le' hd hε
    (left_mem_segment ℝ x y) (right_mem_segment ℝ x y)

/-- **Chord deviation.** The chord of `f` over `[x, y]` stays within `2 ε ‖y - x‖` of the image
of the segment. -/
theorem norm_chord_sub_le {f : E → G} {φ : E →L[ℝ] G} {ε : ℝ} {x y : E}
    (hd : ∀ z ∈ segment ℝ x y, DifferentiableAt ℝ f z)
    (hε : ∀ z ∈ segment ℝ x y, ‖fderiv ℝ f z - φ‖ ≤ ε) {s : ℝ} (hs0 : 0 ≤ s) (hs1 : s ≤ 1) :
    ‖f (x + s • (y - x)) - (f x + s • (f y - f x))‖ ≤ 2 * ε * ‖y - x‖ := by
  have hε0 : 0 ≤ ε := (norm_nonneg _).trans (hε x (left_mem_segment ℝ x y))
  set z := x + s • (y - x)
  have hz : segment ℝ x z ⊆ segment ℝ x y := by
    apply (convex_segment x y).segment_subset (left_mem_segment ℝ x y)
    rw [segment_eq_image']; exact ⟨s, ⟨hs0, hs1⟩, rfl⟩
  have h1 := norm_sub_sub_le (f := f) (φ := φ) (fun w hw => hd w (hz hw)) fun w hw => hε w (hz hw)
  have h2 := norm_sub_sub_le (f := f) (φ := φ) hd hε
  have e : f z - (f x + s • (f y - f x)) =
      (f z - f x - φ (z - x)) - s • (f y - f x - φ (y - x)) := by
    have : φ (z - x) = s • φ (y - x) := by simp only [z, add_sub_cancel_left, map_smul]
    rw [this]; module
  rw [e]
  have hzx : ‖z - x‖ = s * ‖y - x‖ := by
    simp only [z, add_sub_cancel_left, norm_smul, Real.norm_of_nonneg hs0]
  calc _ ≤ ‖f z - f x - φ (z - x)‖ + ‖s • (f y - f x - φ (y - x))‖ := norm_sub_le _ _
    _ ≤ ε * (s * ‖y - x‖) + s * (ε * ‖y - x‖) := by
        rw [norm_smul, Real.norm_of_nonneg hs0, ← hzx]
        exact add_le_add h1 (mul_le_mul_of_nonneg_left h2 hs0)
    _ ≤ 2 * ε * ‖y - x‖ := by
        have := mul_le_mul_of_nonneg_left hs1 (mul_nonneg hε0 (norm_nonneg (y - x)))
        nlinarith

end Chord

end QOU.MathlibExt.PL
