/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Normed.Module.FiniteDimension
import Mathlib.Topology.UniformSpace.HeineCantor

set_option autoImplicit false

/-!
# Uniform constants for a C¹ family of diffeomorphisms (issue #8902, C¹ bridge)

A family `G : X → E ≃ₜ E` over a compact metric space `X`, with `E` finite-dimensional, is
**C¹** when each `G t` and each inverse is differentiable and both derivatives depend
continuously on `(t, x)`. On a compact `K ⊆ E` such a family has

* a uniform inverse-Lipschitz constant: `‖a - b‖ ≤ M ‖G t a - G t b‖` for `a, b ∈ K`, and the
  matching bound `‖u‖ ≤ M ‖D(G t)(x) u‖` for `x ∈ K`;
* uniformly continuous derivatives: `‖x - y‖ < η` gives `‖D(G t)(x) - D(G t)(y)‖ < ε`.

## What is a DEFINITION here

* `C1Family G` — the hypotheses above.

## What is a THEOREM here

* `C1Family.exists_inv_bound` — the uniform inverse bounds.
* `C1Family.uniform_fderiv` — uniform continuity of the derivative on `X × K`.
-/

namespace QOU.MathlibExt.PL

open Set Metric

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
variable {X : Type*} [MetricSpace X] [CompactSpace X]

/-- A family of homeomorphisms that are C¹ with C¹ inverses, jointly in time and space. -/
structure C1Family (G : X → E ≃ₜ E) : Prop where
  cont : Continuous fun p : X × E => G p.1 p.2
  diff : ∀ t x, DifferentiableAt ℝ (G t) x
  cont_fderiv : Continuous fun p : X × E => fderiv ℝ (G p.1) p.2
  diff_symm : ∀ t x, DifferentiableAt ℝ (G t).symm x
  cont_fderiv_symm : Continuous fun p : X × E => fderiv ℝ (G p.1).symm p.2

namespace C1Family

variable {G : X → E ≃ₜ E} (hG : C1Family G)
include hG

/-- **Uniform inverse bounds on a compact set.** -/
theorem exists_inv_bound {K : Set E} (hK : IsCompact K) :
    ∃ M, 0 ≤ M ∧ ∀ t, (∀ a ∈ K, ∀ b ∈ K, ‖a - b‖ ≤ M * ‖G t a - G t b‖) ∧
      (∀ x ∈ K, ∀ u, ‖u‖ ≤ M * ‖fderiv ℝ (G t) x u‖) := by
  have himg : IsCompact ((fun p : X × E => G p.1 p.2) '' (univ ×ˢ K)) :=
    (isCompact_univ.prod hK).image hG.cont
  obtain ⟨R, hR⟩ := (isBounded_iff_subset_closedBall (0 : E)).mp himg.isBounded
  have hGB : ∀ t, ∀ a ∈ K, G t a ∈ closedBall (0 : E) R := fun t a ha =>
    hR ⟨(t, a), ⟨mem_univ _, ha⟩, rfl⟩
  obtain ⟨C, hC⟩ := (isCompact_univ.prod (isCompact_closedBall (0 : E) R)).exists_bound_of_continuousOn
    hG.cont_fderiv_symm.continuousOn
  refine ⟨max C 0, le_max_right _ _, fun t => ⟨fun a ha b hb => ?_, fun x hx u => ?_⟩⟩
  · have h := Convex.norm_image_sub_le_of_norm_fderiv_le (𝕜 := ℝ) (f := (G t).symm)
      (fun y _ => hG.diff_symm t y) (fun y hy => hC (t, y) ⟨mem_univ _, hy⟩)
      (convex_closedBall 0 R) (hGB t b hb) (hGB t a ha)
    simp only [Homeomorph.symm_apply_apply] at h
    exact h.trans (mul_le_mul_of_nonneg_right (le_max_left _ _) (norm_nonneg _))
  · have hcomp : fderiv ℝ ((G t).symm ∘ G t) x =
        (fderiv ℝ (G t).symm (G t x)).comp (fderiv ℝ (G t) x) :=
      fderiv_comp x (hG.diff_symm t _) (hG.diff t x)
    have hid : (G t).symm ∘ G t = id := funext (G t).symm_apply_apply
    rw [hid, fderiv_id] at hcomp
    have hu : u = fderiv ℝ (G t).symm (G t x) (fderiv ℝ (G t) x u) := by
      have := congrArg (fun L : E →L[ℝ] E => L u) hcomp
      simpa using this
    calc ‖u‖ = ‖fderiv ℝ (G t).symm (G t x) (fderiv ℝ (G t) x u)‖ := by rw [← hu]
      _ ≤ ‖fderiv ℝ (G t).symm (G t x)‖ * ‖fderiv ℝ (G t) x u‖ := ContinuousLinearMap.le_opNorm _ _
      _ ≤ max C 0 * ‖fderiv ℝ (G t) x u‖ := by
          gcongr
          exact (hC (t, G t x) ⟨mem_univ _, hGB t x hx⟩).trans (le_max_left _ _)

omit [FiniteDimensional ℝ E] in
/-- **Uniform continuity of the derivative on a compact set.** -/
theorem uniform_fderiv {K : Set E} (hK : IsCompact K) {ε : ℝ} (hε : 0 < ε) :
    ∃ η > 0, ∀ t, ∀ x ∈ K, ∀ y ∈ K, ‖x - y‖ < η →
      ‖fderiv ℝ (G t) x - fderiv ℝ (G t) y‖ < ε := by
  have hu := (isCompact_univ.prod hK).uniformContinuousOn_of_continuous
    hG.cont_fderiv.continuousOn
  obtain ⟨η, hη, h⟩ := Metric.uniformContinuousOn_iff.mp hu ε hε
  refine ⟨η, hη, fun t x hx y hy hxy => ?_⟩
  have := h (t, x) ⟨mem_univ _, hx⟩ (t, y) ⟨mem_univ _, hy⟩
    (by rw [Prod.dist_eq, dist_self, dist_eq_norm]; exact max_lt hη hxy)
  rwa [dist_eq_norm] at this

end C1Family

end QOU.MathlibExt.PL
