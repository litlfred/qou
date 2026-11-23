/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLMaps
import Mathlib.Analysis.Calculus.MeanValue

set_option autoImplicit false

/-!
# PL maps are Lipschitz, piecewise-affine route (issue #8902, Moise build part A)

Renamed from `PLLipschitz.lean` when it collided with the stage-2 file of that name on main.

## What is a THEOREM here

* `IsPolyhedron.convex` — a polyhedron is convex.
* `norm_sub_le_of_piecewise_affine` — a function on `[0, 1]`, continuous there, that is affine with
  slope of norm `≤ C` on each of finitely many closed intervals covering `[0, 1]`, moves by at most
  `C` between `0` and `1`. Each point of `[0, 1)` has a right neighbourhood inside one interval, so
  the function has a right derivative there; the mean value inequality finishes.
* `IsPL.exists_lipschitz` — **a PL map is Lipschitz**: `‖f b - f a‖ ≤ C * ‖b - a‖` with `C` the sum
  of the operator norms of its linear parts.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

variable {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F]

lemma IsPolyhedron.convex {K : Set E} (hK : IsPolyhedron K) : Convex ℝ K := by
  obtain ⟨ι, _, φ, r, rfl⟩ := hK
  simp only [setOf_forall]
  exact convex_iInter fun i => convex_halfSpace_le (φ i).isLinear (r i)

/-- **The one-dimensional core.** -/
theorem norm_sub_le_of_piecewise_affine {g : ℝ → F} {ι : Type} [Fintype ι] (I : ι → Set ℝ)
    (hIc : ∀ m, IsClosed (I m)) (hIv : ∀ m, Convex ℝ (I m)) (hcov : Icc (0 : ℝ) 1 ⊆ ⋃ m, I m)
    (c v : ι → F) (hg : ∀ m, ∀ s ∈ I m, g s = c m + s • v m) (hgc : ContinuousOn g (Icc 0 1))
    (C : ℝ) (hv : ∀ m, ‖v m‖ ≤ C) : ‖g 1 - g 0‖ ≤ C := by
  classical
  -- each point of `[0, 1)` has a right neighbourhood inside one piece
  have key : ∀ x ∈ Ico (0 : ℝ) 1, ∃ m, ∃ δ > 0, Icc x (x + δ) ⊆ I m := by
    intro x hx
    by_contra H
    push_neg at H
    have hfar : ∀ m, ∃ ε > 0, ∀ y ∈ Ioo x (x + ε), y ∉ I m := by
      intro m
      by_contra H'
      push_neg at H'
      obtain ⟨y₁, hy₁, hy₁m⟩ := H' 1 one_pos
      have hxm : x ∈ I m := by
        refine (hIc m).closure_subset (Metric.mem_closure_iff.mpr fun ε hε => ?_)
        obtain ⟨y, hy, hym⟩ := H' (min ε 1) (lt_min hε one_pos)
        refine ⟨y, hym, ?_⟩
        rw [Real.dist_eq, abs_lt]
        constructor <;> linarith [hy.1, hy.2, min_le_left ε 1]
      have : Icc x y₁ ⊆ I m := by
        rw [← segment_eq_Icc hy₁.1.le]
        exact (hIv m).segment_subset hxm hy₁m
      exact H m (y₁ - x) (by linarith [hy₁.1]) (by simpa using this)
    choose ε hε hεm using hfar
    obtain ⟨m₀, -⟩ := mem_iUnion.mp (hcov (Ico_subset_Icc_self hx))
    set δ := Finset.univ.inf' ⟨m₀, Finset.mem_univ _⟩ ε
    have hδ : 0 < δ := (Finset.lt_inf'_iff _).mpr fun m _ => hε m
    have hδm : ∀ m, δ ≤ ε m := fun m => Finset.inf'_le _ (Finset.mem_univ m)
    obtain ⟨y, hydef⟩ : ∃ y : ℝ, y = x + min δ (1 - x) / 2 := ⟨_, rfl⟩
    have hpos : 0 < min δ (1 - x) := lt_min hδ (by linarith [hx.2])
    have hy : y ∈ Icc (0 : ℝ) 1 := ⟨by rw [hydef]; linarith [hx.1], by rw [hydef]; linarith [min_le_right δ (1 - x)]⟩
    obtain ⟨m, hm⟩ := mem_iUnion.mp (hcov hy)
    refine hεm m y ⟨by rw [hydef]; linarith, ?_⟩ hm
    rw [hydef]; linarith [min_le_left δ (1 - x), hδm m]
  haveI : Nonempty ι := ⟨(mem_iUnion.mp (hcov ⟨le_rfl, zero_le_one⟩)).choose⟩
  choose! mx δx hδx hsub using key
  have hderiv : ∀ x ∈ Ico (0 : ℝ) 1, HasDerivWithinAt g (v (mx x)) (Ici x) x := by
    intro x hx
    have hl : HasDerivAt (fun s : ℝ => c (mx x) + s • v (mx x)) (v (mx x)) x := by
      simpa using ((hasDerivAt_id x).smul_const (v (mx x))).const_add (c (mx x))
    refine hl.hasDerivWithinAt.congr_of_eventuallyEq ?_ ?_
    · filter_upwards [Icc_mem_nhdsGE (by linarith [hδx x hx] : x < x + δx x)] with s hs
      exact hg _ s (hsub x hx hs)
    · exact hg _ x (hsub x hx ⟨le_rfl, by linarith [hδx x hx]⟩)
  have := norm_image_sub_le_of_norm_deriv_right_le_segment hgc hderiv
    (fun x _ => hv (mx x)) 1 ⟨zero_le_one, le_rfl⟩
  simpa using this

/-- **A PL map is Lipschitz.** -/
theorem IsPL.exists_lipschitz {f : E → F} (hf : IsPL f) :
    ∃ C, 0 ≤ C ∧ ∀ a b, ‖f b - f a‖ ≤ C * ‖b - a‖ := by
  obtain ⟨ι, _, K, A, hK, hKu, hfA⟩ := hf
  have hfc : Continuous f := IsPL.continuous ⟨ι, inferInstance, K, A, hK, hKu, hfA⟩
  refine ⟨∑ m, ‖(A m).contLinear‖, Finset.sum_nonneg fun m _ => norm_nonneg _, fun a b => ?_⟩
  set w := b - a
  have hline : Continuous fun s : ℝ => a + s • w := continuous_const.add (continuous_id.smul
    continuous_const)
  have := norm_sub_le_of_piecewise_affine (g := fun s : ℝ => f (a + s • w))
    (fun m => (fun s : ℝ => a + s • w) ⁻¹' K m)
    (fun m => (hK m).isClosed.preimage hline)
    (fun m => by
      have hc := (hK m).convex
      intro x hx y hy p q hp hq hpq
      simp only [mem_preimage] at hx hy ⊢
      have := hc hx hy hp hq hpq
      have e : p • (a + x • w) + q • (a + y • w) = a + (p * x + q * y) • w := by
        rw [smul_add, smul_add, smul_smul, smul_smul, add_add_add_comm, ← add_smul, hpq, one_smul,
          ← add_smul]
      rw [smul_eq_mul, smul_eq_mul, ← e]
      exact this)
    (fun s _ => by
      obtain ⟨m, hm⟩ := mem_iUnion.mp (hKu ▸ mem_univ (a + s • w))
      exact mem_iUnion.mpr ⟨m, hm⟩)
    (fun m => A m a) (fun m => (A m).contLinear w)
    (fun m s hs => by
      show f (a + s • w) = A m a + s • (A m).contLinear w
      rw [hfA m hs, affine_apply_eq (A m), affine_apply_eq (A m) a, map_add, map_smul]
      abel)
    (hfc.comp hline).continuousOn ((∑ m, ‖(A m).contLinear‖) * ‖w‖)
    (fun m => by
      refine ((A m).contLinear.le_opNorm w).trans (mul_le_mul_of_nonneg_right ?_ (norm_nonneg _))
      exact Finset.single_le_sum (f := fun m => ‖(A m).contLinear‖) (fun m _ => norm_nonneg _)
        (Finset.mem_univ m))
  simpa [w] using this

end QOU.MathlibExt.PL
