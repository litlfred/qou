/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarDiskComplex
import QOU.MathlibExt.PLSlicePolygons

set_option autoImplicit false

/-!
# Each slice polygon bounds a triangulated disk in its level plane (issue #8902, part B)

`slice_eq_union_planarPolygons` writes a generic slice of a closed surface in a three-dimensional
space as finitely many disjoint polygons, each carried from a simple polygon of `R2` by an
injective affine map onto the level plane. `Polygon.exists_triangulation_region` triangulates the
region of a simple polygon of `R2`. Pushing that triangulation forward gives, for each slice
polygon, a triangulated disk in the level plane whose edges include the polygon's edges. These
disks are the ones Alexander's proof caps the slices with.

## What is a DEFINITION here

* `mapAffComplex f hf K` — the image of a simplicial complex under an injective affine
  map.

## What is a THEOREM here

* `mapAffComplex_space` — the space of the image is the image of the space.
* `Polygon.exists_triangulation_mapAff` — the image of a simple polygon of `R2` under an injective
  affine map bounds a triangulated disk, the image of its region.
* `slice_polygons_bound_disks` — **in a generic slice of a finite closed surface in a
  three-dimensional space, every slice polygon is the boundary edge set of a finite triangulated
  disk lying in the level plane.**

## What is NOT proved here

* That the capping disks of different slice polygons are nested or disjoint, and the induction
  across critical levels that finishes Alexander's theorem.
-/

namespace QOU.MathlibExt.PL

open Set Geometry

universe u

section MapAff

variable {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [DecidableEq F]

/-- The image of a simplicial complex under an injective affine map. -/
def mapAffComplex (f : E →ᵃ[ℝ] F) (hf : Function.Injective f)
    (K : SimplicialComplex ℝ E) : SimplicialComplex ℝ F where
  faces := Finset.image f '' K.faces
  empty_notMem := by
    rintro ⟨s, hs, h⟩
    rw [Finset.image_eq_empty] at h
    exact K.empty_notMem (h ▸ hs)
  indep := by
    rintro _ ⟨s, hs, rfl⟩
    have h := ((K.indep hs).map' f hf).range
    have hr : Set.range (f ∘ ((↑) : s → E)) = ((s.image f : Finset F) : Set F) := by
      ext y; simp
    rw [hr] at h
    exact h
  down_closed := by
    rintro _ t ⟨s, hs, rfl⟩ hts ht
    obtain ⟨s', hs's, rfl⟩ := Finset.subset_image_iff.mp hts
    refine ⟨s', K.down_closed hs hs's ?_, rfl⟩
    rintro rfl
    exact ht (Finset.image_empty f)
  inter_subset_convexHull := by
    rintro _ _ ⟨s, hs, rfl⟩ ⟨t, ht, rfl⟩
    simp only [Finset.coe_image, ← AffineMap.image_convexHull]
    rw [← image_inter hf, ← image_inter hf, ← AffineMap.image_convexHull]
    exact image_mono (K.inter_subset_convexHull hs ht)

lemma mapAffComplex_space (f : E →ᵃ[ℝ] F) (hf : Function.Injective f)
    (K : SimplicialComplex ℝ E) : (mapAffComplex f hf K).space = f '' K.space := by
  ext y
  simp only [SimplicialComplex.mem_space_iff, mem_image]
  constructor
  · rintro ⟨_, ⟨s, hs, rfl⟩, hy⟩
    rw [Finset.coe_image, ← AffineMap.image_convexHull] at hy
    obtain ⟨x, hx, rfl⟩ := hy
    exact ⟨x, ⟨s, hs, hx⟩, rfl⟩
  · rintro ⟨x, ⟨s, hs, hx⟩, rfl⟩
    refine ⟨s.image f, ⟨s, hs, rfl⟩, ?_⟩
    rw [Finset.coe_image, ← AffineMap.image_convexHull]
    exact mem_image_of_mem f hx

lemma mapAffComplex_faces_finite (f : E →ᵃ[ℝ] F) (hf : Function.Injective f)
    {K : SimplicialComplex ℝ E} (hK : K.faces.Finite) : (mapAffComplex f hf K).faces.Finite :=
  hK.image _

end MapAff

variable {E : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- **The image of a simple polygon of `R2` bounds a triangulated disk.** -/
theorem Polygon.exists_triangulation_mapAff [DecidableEq R2] [DecidableEq E] (P : Polygon R2)
    (hP : P.IsSimple) (f : R2 →ᵃ[ℝ] E) (hf : Function.Injective f) :
    ∃ K : SimplicialComplex ℝ E, K.faces.Finite ∧ (∀ s ∈ K.faces, s.card ≤ 3) ∧
      (∀ s ∈ K.faces, ∀ x ∈ s, ∃ j, (P.mapAff f).w j = x) ∧
      (∀ j, ({(P.mapAff f).w j, (P.mapAff f).w (j + 1)} : Finset E) ∈ K.faces) ∧
      K.space = f '' P.region := by
  obtain ⟨K, hfin, hcard, hvert, hedge, hspace⟩ := P.exists_triangulation_region hP
  refine ⟨mapAffComplex f hf K, mapAffComplex_faces_finite f hf hfin, ?_, ?_, ?_, ?_⟩
  · rintro _ ⟨s, hs, rfl⟩
    exact Finset.card_image_le.trans (hcard s hs)
  · rintro _ ⟨s, hs, rfl⟩ x hx
    obtain ⟨y, hy, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨j, rfl⟩ := hvert s hs y hy
    exact ⟨j, rfl⟩
  · intro j
    refine ⟨{P.w j, P.w (j + 1)}, hedge j, ?_⟩
    rw [Finset.image_insert, Finset.image_singleton]
    rfl
  · rw [mapAffComplex_space, hspace]

/-- **Each slice polygon bounds a triangulated disk in the level plane.** -/
theorem slice_polygons_bound_disks [DecidableEq R2] [DecidableEq E] [FiniteDimensional ℝ E]
    (hE : Module.finrank ℝ E = 3) {ψ : E →L[ℝ] ℝ} (hψ : ψ ≠ 0) {c : ℝ}
    {K : SimplicialComplex ℝ E} (hK : IsClosedSurface K) (hfin : K.faces.Finite)
    (hgen : ∀ s ∈ K.faces, ∀ v ∈ s, ψ v ≠ c) :
    ∃ (ι : Type u) (_ : Finite ι) (Q : ι → Polygon R2) (g : ι → R2 →ᵃ[ℝ] E),
      (∀ i, (Q i).IsSimple) ∧ (∀ i, Function.Injective (g i)) ∧
      (∀ i, range (g i) = {x | ψ x = c}) ∧
      Pairwise (fun i j => Disjoint ((Q i).mapAff (g i)).carrier ((Q j).mapAff (g j)).carrier) ∧
      (⋃ i, ((Q i).mapAff (g i)).carrier = K.space ∩ {x | ψ x = c}) ∧
      ∀ i, ∃ D : SimplicialComplex ℝ E, D.faces.Finite ∧ (∀ s ∈ D.faces, s.card ≤ 3) ∧
        (∀ j, ({((Q i).mapAff (g i)).w j, ((Q i).mapAff (g i)).w (j + 1)} : Finset E) ∈
          D.faces) ∧
        D.space = g i '' (Q i).region ∧ D.space ⊆ {x | ψ x = c} := by
  obtain ⟨ι, hι, Q, g, hs, hinj, hrange, hdisj, hcover⟩ :=
    slice_eq_union_planarPolygons hE hψ hK hfin hgen
  refine ⟨ι, hι, Q, g, hs, hinj, hrange, hdisj, hcover, fun i => ?_⟩
  obtain ⟨D, hDfin, hDcard, -, hDedge, hDspace⟩ :=
    (Q i).exists_triangulation_mapAff (hs i) (g i) (hinj i)
  refine ⟨D, hDfin, hDcard, hDedge, hDspace, ?_⟩
  rw [hDspace, ← hrange i]
  exact image_subset_range _ _

end QOU.MathlibExt.PL
