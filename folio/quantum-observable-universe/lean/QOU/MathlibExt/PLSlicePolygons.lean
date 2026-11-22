/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLCyclePolygon
import QOU.MathlibExt.PLPlaneTransport

set_option autoImplicit false

/-!
# A generic slice of a closed surface is a union of planar simple polygons (issue #8902, part B)

This puts together the slicing step of Alexander's proof of the PL Schoenflies theorem in a
three-dimensional space:

* the slice of a closed triangulated surface by a generic level `{ψ = c}` is 2-regular
  (`slice_vertex_degree`);
* a finite 2-regular 1-complex is a disjoint union of simple polygons
  (`exists_polygons_of_twoRegular`);
* a polygon in a plane is the image of a simple polygon of `R2` under an injective affine map
  onto that plane (`Polygon.exists_planar_model`).

## What is a THEOREM here

* `exists_point_of_ne_zero` — a nonzero linear form takes every value.
* `slice_eq_union_planarPolygons` — **the slice of a finite closed surface in a
  three-dimensional space by a generic level `{ψ = c}` is the union of finitely many polygons with
  pairwise disjoint carriers, each the image of a simple polygon of `R2` under an injective affine
  map onto the level plane.**

## What is NOT proved here

* That each planar polygon bounds a disk (planar Schoenflies), and the induction across critical
  levels that finishes the three-dimensional theorem.
-/

namespace QOU.MathlibExt.PL

open Set Geometry

universe u

variable {E : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E]

lemma exists_point_of_ne_zero {ψ : E →L[ℝ] ℝ} (hψ : ψ ≠ 0) (c : ℝ) : ∃ p : E, ψ p = c := by
  obtain ⟨x, hx⟩ : ∃ x, ψ x ≠ 0 := by
    by_contra hcon
    push_neg at hcon
    exact hψ (ContinuousLinearMap.ext hcon)
  exact ⟨(c / ψ x) • x, by rw [map_smul, smul_eq_mul, div_mul_cancel₀ _ hx]⟩

/-- **A generic slice of a closed surface is a disjoint union of planar simple polygons.** -/
theorem slice_eq_union_planarPolygons [DecidableEq E] [FiniteDimensional ℝ E]
    (hE : Module.finrank ℝ E = 3) {ψ : E →L[ℝ] ℝ} (hψ : ψ ≠ 0) {c : ℝ}
    {K : SimplicialComplex ℝ E} (hK : IsClosedSurface K) (hfin : K.faces.Finite)
    (hgen : ∀ s ∈ K.faces, ∀ v ∈ s, ψ v ≠ c) :
    ∃ (ι : Type u) (_ : Finite ι) (Q : ι → Polygon R2) (g : ι → R2 →ᵃ[ℝ] E),
      (∀ i, (Q i).IsSimple) ∧ (∀ i, Function.Injective (g i)) ∧
      (∀ i, range (g i) = {x | ψ x = c}) ∧
      Pairwise (fun i j => Disjoint ((Q i).mapAff (g i)).carrier ((Q j).mapAff (g j)).carrier) ∧
      ⋃ i, ((Q i).mapAff (g i)).carrier = K.space ∩ {x | ψ x = c} := by
  obtain ⟨ι, hι, P, hsimple, hdisj, hcover⟩ :=
    exists_polygons_of_twoRegular (S := sliceComplex K hK.1 hgen)
      (sliceComplex_faces_finite hfin) (fun _ h => sliceComplex_card_le_two h)
      (fun _ hx => slice_vertex_degree hK hgen hx)
  rw [sliceComplex_space] at hcover
  obtain ⟨p, hp⟩ := exists_point_of_ne_zero hψ c
  set H := levelPlane (ψ : E →ₗ[ℝ] ℝ) p with hH
  have hHset : (H : Set E) = {x | ψ x = c} := by
    ext x
    rw [SetLike.mem_coe, hH, mem_levelPlane]
    simp [hp]
  have hψ' : (ψ : E →ₗ[ℝ] ℝ) ≠ 0 := fun h => hψ (ContinuousLinearMap.coe_injective h)
  have hdimH : Module.finrank ℝ H.direction = 2 := finrank_levelPlane_direction hE hψ' p
  have hvH : ∀ i j, (P i).v j ∈ H := by
    intro i j
    have hmem : (P i).v j ∈ ⋃ k, (P k).carrier :=
      mem_iUnion.mpr ⟨i, (P i).edge_subset_carrier j (left_mem_segment ℝ _ _)⟩
    rw [hcover] at hmem
    rw [← SetLike.mem_coe, hHset]
    exact hmem.2
  have hmodel := fun i => Polygon.exists_planar_model (P i) H hdimH (hvH i)
  choose Q g hginj hgrange hQP hQs using hmodel
  refine ⟨ι, hι, Q, g, fun i => (hQs i).mpr (hsimple i), hginj, fun i => by rw [hgrange, hHset],
    ?_, ?_⟩
  · intro i j hij
    rw [hQP, hQP]
    exact hdisj hij
  · simp_rw [hQP]
    exact hcover

end QOU.MathlibExt.PL
