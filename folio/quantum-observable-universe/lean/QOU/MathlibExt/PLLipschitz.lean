/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLIsotopy
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Topology.EMetricSpace.Lipschitz

set_option autoImplicit false

/-!
# PL maps are Lipschitz (issue #8902, stage 2: towards PL isotopy ⇒ Δ-equivalence)

## What is a THEOREM here

* `IsPL.norm_sub_le` — if `f` agrees with the affine map `A i` on the polyhedron `K i`, the
  `K i` cover the space, and every linear part has norm `≤ C`, then `‖f y - f x‖ ≤ C ‖y - x‖`.
  Proof by real induction along the segment `[x, y]`: near any point of the segment, some piece
  contains points of the segment arbitrarily close on the right, and (being closed) the point
  itself.
* `IsPL.lipschitz` — **a PL map is Lipschitz.**
* `AmbientIsotopy.exists_lipschitz_H` — the homeomorphisms `H t` of a PL ambient isotopy are
  Lipschitz with **one constant for all `t`**.
* `AmbientIsotopy.exists_lipschitz_H_symm` — the same for their inverses, in finite dimension.

## What is NOT proved here

* The converse of `DeltaEquiv.plAmbientIsotopic` (PL ambient isotopy ⇒ Δ-equivalence). These
  uniform bounds are the input that keeps inscribed polygons of the moving link simple.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

variable {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F]

namespace IsPL

/-- **The segment bound for a PL decomposition.** -/
theorem norm_sub_le {f : E → F} {ι : Type} [Fintype ι] (K : ι → Set E) (A : ι → E →ᴬ[ℝ] F)
    (hK : ∀ i, IsPolyhedron (K i)) (hKu : (⋃ i, K i) = univ) (hfA : ∀ i, EqOn f (A i) (K i))
    {C : ℝ} (hC : ∀ i, ‖(A i).contLinear‖ ≤ C) (x y : E) :
    ‖f y - f x‖ ≤ C * ‖y - x‖ := by
  have hcont : Continuous f := IsPL.continuous ⟨ι, inferInstance, K, A, hK, hKu, hfA⟩
  set g : ℝ → E := fun s => x + s • (y - x) with hg
  have hgc : Continuous g := by fun_prop
  set S : Set ℝ := {s | ‖f (g s) - f x‖ ≤ C * s * ‖y - x‖} with hSdef
  have hS : IsClosed (S ∩ Icc 0 1) :=
    (isClosed_le (by fun_prop) (by fun_prop)).inter isClosed_Icc
  have h0 : (0 : ℝ) ∈ S := by simp [S, g]
  have key : Icc (0 : ℝ) 1 ⊆ S := by
    refine IsClosed.Icc_subset_of_forall_exists_gt hS h0 ?_
    intro s0 hs0 u hu
    have hfreq : ∃ i, ∃ᶠ s in 𝓝[>] s0, g s ∈ K i := by
      by_contra hne
      push_neg at hne
      have hall : ∀ᶠ s in 𝓝[>] s0, ∀ i, g s ∉ K i :=
        eventually_all.2 fun i => by simpa [Filter.not_frequently] using hne i
      obtain ⟨s, hs⟩ := hall.exists
      have hmem : g s ∈ ⋃ i, K i := hKu ▸ mem_univ _
      obtain ⟨i, hi⟩ := mem_iUnion.1 hmem
      exact hs i hi
    obtain ⟨i, hi⟩ := hfreq
    have hTc : IsClosed (g ⁻¹' K i) := (hK i).isClosed.preimage hgc
    have hs0K : g s0 ∈ K i := by
      have hcl : s0 ∈ closure (g ⁻¹' K i) :=
        mem_closure_iff_frequently.2 (hi.filter_mono nhdsWithin_le_nhds)
      rw [hTc.closure_eq] at hcl
      exact hcl
    have hev : ∀ᶠ s in 𝓝[>] s0, s ∈ Ioo s0 (min u 1) :=
      Ioo_mem_nhdsGT (lt_min hu hs0.2.2)
    obtain ⟨s1, hs1K, hs1⟩ := (hi.and_eventually hev).exists
    refine ⟨s1, ?_, hs1.1, (hs1.2.trans_le (min_le_left _ _)).le⟩
    have hdiff : f (g s1) - f (g s0) = (A i).contLinear ((s1 - s0) • (y - x)) := by
      rw [hfA i hs1K, hfA i hs0K, ← vsub_eq_sub, ← (A i).contLinear_map_vsub, vsub_eq_sub]
      congr 1
      simp only [g]
      module
    have hC0 : 0 ≤ C := (norm_nonneg _).trans (hC i)
    have hstep : ‖f (g s1) - f (g s0)‖ ≤ C * (s1 - s0) * ‖y - x‖ := by
      rw [hdiff]
      calc ‖(A i).contLinear ((s1 - s0) • (y - x))‖
          ≤ ‖(A i).contLinear‖ * ‖(s1 - s0) • (y - x)‖ := (A i).contLinear.le_opNorm _
        _ ≤ C * ‖(s1 - s0) • (y - x)‖ := by gcongr; exact hC i
        _ = C * (s1 - s0) * ‖y - x‖ := by
          rw [norm_smul, Real.norm_of_nonneg (by linarith [hs1.1]), mul_assoc]
    have hprev : ‖f (g s0) - f x‖ ≤ C * s0 * ‖y - x‖ := hs0.1
    show ‖f (g s1) - f x‖ ≤ C * s1 * ‖y - x‖
    calc ‖f (g s1) - f x‖ = ‖(f (g s1) - f (g s0)) + (f (g s0) - f x)‖ := by
          congr 1; abel
      _ ≤ ‖f (g s1) - f (g s0)‖ + ‖f (g s0) - f x‖ := norm_add_le _ _
      _ ≤ C * (s1 - s0) * ‖y - x‖ + C * s0 * ‖y - x‖ := add_le_add hstep hprev
      _ = C * s1 * ‖y - x‖ := by ring
  have h1 := key ⟨zero_le_one, le_rfl⟩
  simpa [S, g] using h1

/-- **A PL map is Lipschitz.** -/
theorem lipschitz {f : E → F} (hf : IsPL f) : ∃ K, LipschitzWith K f := by
  obtain ⟨ι, _, K, A, hK, hKu, hfA⟩ := hf
  set C : ℝ := ∑ i, ‖(A i).contLinear‖
  have hC : ∀ i, ‖(A i).contLinear‖ ≤ C := fun i =>
    Finset.single_le_sum (f := fun i => ‖(A i).contLinear‖) (fun _ _ => norm_nonneg _)
      (Finset.mem_univ i)
  have hC0 : 0 ≤ C := Finset.sum_nonneg fun _ _ => norm_nonneg _
  refine ⟨C.toNNReal, LipschitzWith.of_dist_le_mul fun x y => ?_⟩
  rw [Real.coe_toNNReal _ hC0, dist_eq_norm, dist_eq_norm]
  exact norm_sub_le K A hK hKu hfA hC y x

end IsPL

variable {L L' : PolygonalLink E}

namespace AmbientIsotopy

/-- **The homeomorphisms of a PL ambient isotopy are uniformly Lipschitz.** -/
theorem exists_lipschitz_H (I : AmbientIsotopy L L') (h : IsPL I.track) :
    ∃ K, ∀ t, LipschitzWith K (I.H t) := by
  obtain ⟨K, hK⟩ := h.lipschitz
  refine ⟨K, fun t => LipschitzWith.of_dist_le_mul fun x y => ?_⟩
  have := hK.dist_le_mul ((t : ℝ), x) ((t : ℝ), y)
  simpa [track, Prod.dist_eq, clamp01, Set.projIcc_val] using this

/-- **The inverses of a PL ambient isotopy are uniformly Lipschitz** (finite dimension). -/
theorem exists_lipschitz_H_symm [FiniteDimensional ℝ E] (I : AmbientIsotopy L L')
    (h : IsPL I.track) : ∃ K, ∀ t, LipschitzWith K (I.H t).symm := by
  obtain ⟨K, hK⟩ := (I.isPL_trackInv h).lipschitz
  refine ⟨K, fun t => LipschitzWith.of_dist_le_mul fun x y => ?_⟩
  have := hK.dist_le_mul ((t : ℝ), x) ((t : ℝ), y)
  simpa [trackInv, Prod.dist_eq, clamp01, Set.projIcc_val] using this

end AmbientIsotopy

end QOU.MathlibExt.PL
