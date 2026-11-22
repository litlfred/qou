/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLAffineEquivariance
import QOU.MathlibExt.PLPlanarParity
import Mathlib.LinearAlgebra.AffineSpace.FiniteDimensional

set_option autoImplicit false

/-!
# Carrying a plane polygon to `R2` (issue #8902, part B, 3D Schoenflies)

Alexander's proof of the PL Schoenflies theorem in `ℝ³` slices a sphere by parallel planes. Each
slice polygon lies in a plane `H` of the ambient space. To apply the planar results proved for
`R2 = Fin 2 → ℝ` (two ears, ear clipping), the polygon has to be moved into `R2`. An affine
subspace of dimension two is the image of an injective affine map `R2 → E`, and the polygon is the
image of a simple polygon of `R2` under that map.

## What is a DEFINITION here

* `Polygon.mapAff f P` — the image of a polygon under an affine map (not necessarily invertible).
* `levelPlane ψ p` — the affine subspace through `p` with direction `ker ψ`.

## What is a THEOREM here

* `Polygon.carrier_mapAff`, `Polygon.isSimple_mapAff`, `Polygon.isSimple_of_mapAff` — an
  injective affine map carries simple polygons to simple polygons and back.
* `Polygon.exists_planar_model` — **a polygon whose vertices lie in a two-dimensional affine
  subspace `H` is the image of a polygon of `R2` under an injective affine map with range `H`;
  the planar polygon is simple exactly when the original one is.**
* `mem_levelPlane`, `finrank_levelPlane_direction` — `levelPlane ψ p` is the level set
  `{x | ψ x = ψ p}`, and it is two-dimensional when `E` is three-dimensional and `ψ ≠ 0`.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E F : Type*} [AddCommGroup E] [Module ℝ E] [AddCommGroup F] [Module ℝ F]

namespace Polygon

/-- The image of a polygon under an affine map. -/
def mapAff (f : E →ᵃ[ℝ] F) (P : Polygon E) : Polygon F where
  n := P.n
  two_le := P.two_le
  v := f ∘ P.v

variable (f : E →ᵃ[ℝ] F) (P : Polygon E)

lemma mapAff_v (i : Fin (P.n + 1)) : (P.mapAff f).v i = f (P.v i) := rfl

lemma mapAff_next (i : Fin (P.n + 1)) : (P.mapAff f).next i = P.next i := rfl

theorem edge_mapAff (i : Fin (P.n + 1)) : (P.mapAff f).edge i = f '' P.edge i := by
  simp only [edge, mapAff_v, mapAff_next]
  exact (image_segment ℝ f _ _).symm

theorem carrier_mapAff : (P.mapAff f).carrier = f '' P.carrier := by
  simp only [carrier, edge_mapAff, image_iUnion]
  rfl

theorem isSimple_mapAff {f : E →ᵃ[ℝ] F} (hf : Function.Injective f) {P : Polygon E}
    (h : P.IsSimple) : (P.mapAff f).IsSimple := by
  refine ⟨hf.comp h.1, fun i j hij => ?_⟩
  rw [edge_mapAff, edge_mapAff, ← image_inter hf, h.2 i j hij]
  simp only [mapAff_next, mapAff_v]
  split_ifs <;> simp

theorem isSimple_of_mapAff {f : E →ᵃ[ℝ] F} (hf : Function.Injective f) {P : Polygon E}
    (h : (P.mapAff f).IsSimple) : P.IsSimple := by
  refine ⟨Function.Injective.of_comp h.1, fun i j hij => ?_⟩
  have h2 := h.2 i j hij
  rw [edge_mapAff, edge_mapAff, ← image_inter hf] at h2
  rw [← preimage_image_eq (P.edge i ∩ P.edge j) hf, h2]
  simp only [mapAff_next, mapAff_v]
  split_ifs <;> ext z <;> simp [hf.eq_iff]

/-- **A polygon in a plane is the image of a polygon in `R2`.** -/
theorem exists_planar_model (P : Polygon E) (H : AffineSubspace ℝ E)
    (hH : Module.finrank ℝ H.direction = 2) (h : ∀ i, P.v i ∈ H) :
    ∃ (Q : Polygon R2) (g : R2 →ᵃ[ℝ] E), Function.Injective g ∧ range g = H ∧
      Q.mapAff g = P ∧ (Q.IsSimple ↔ P.IsSimple) := by
  set p := P.v 0 with hp
  have hpH : p ∈ H := h 0
  haveI : FiniteDimensional ℝ H.direction := Module.finite_of_finrank_eq_succ hH
  have hdim : Module.finrank ℝ H.direction = Module.finrank ℝ R2 := by
    rw [hH, Module.finrank_fin_fun]
  set e : H.direction ≃ₗ[ℝ] R2 := LinearEquiv.ofFinrankEq _ _ hdim with he
  set g : R2 →ᵃ[ℝ] E :=
    (AffineEquiv.vaddConst ℝ p).toAffineMap.comp
      (H.direction.subtype.comp e.symm.toLinearMap).toAffineMap with hg
  have hgx : ∀ x : R2, g x = (e.symm x : E) + p := fun x => rfl
  have hginj : Function.Injective g := by
    intro x y hxy
    rw [hgx, hgx, add_left_inj] at hxy
    exact e.symm.injective (Subtype.ext hxy)
  set Q : Polygon R2 :=
    { n := P.n, two_le := P.two_le,
      v := fun i => e ⟨P.v i - p, by
        have := H.vsub_mem_direction (h i) hpH
        rwa [vsub_eq_sub] at this⟩ } with hQ
  have hQP : Q.mapAff g = P := by
    have hv : (Q.mapAff g).v = P.v := by
      funext i
      rw [mapAff_v, hgx]
      change ((e.symm (e _) : H.direction) : E) + p = _
      rw [LinearEquiv.symm_apply_apply]
      exact sub_add_cancel _ _
    show Polygon.mk P.n P.two_le ((Q.mapAff g).v) = P
    rw [hv]
  refine ⟨Q, g, hginj, ?_, hQP, ⟨fun hs => hQP ▸ isSimple_mapAff hginj hs,
    fun hs => isSimple_of_mapAff hginj (hQP ▸ hs)⟩⟩
  ext y
  constructor
  · rintro ⟨x, rfl⟩
    rw [hgx]
    have := H.vadd_mem_of_mem_direction (e.symm x).2 hpH
    rwa [vadd_eq_add] at this
  · intro hy
    refine ⟨e ⟨y - p, ?_⟩, ?_⟩
    · have := H.vsub_mem_direction hy hpH
      rwa [vsub_eq_sub] at this
    · rw [hgx]; simp

end Polygon

/-- The plane through `p` parallel to `ker ψ`. -/
def levelPlane (ψ : E →ₗ[ℝ] ℝ) (p : E) : AffineSubspace ℝ E :=
  AffineSubspace.mk' p (LinearMap.ker ψ)

lemma mem_levelPlane {ψ : E →ₗ[ℝ] ℝ} {p x : E} : x ∈ levelPlane ψ p ↔ ψ x = ψ p := by
  rw [levelPlane, AffineSubspace.mem_mk', LinearMap.mem_ker, vsub_eq_sub, map_sub, sub_eq_zero]

/-- **A level set of a nonzero linear form on a three-dimensional space is a plane.** -/
theorem finrank_levelPlane_direction [FiniteDimensional ℝ E] (hE : Module.finrank ℝ E = 3)
    {ψ : E →ₗ[ℝ] ℝ} (hψ : ψ ≠ 0) (p : E) :
    Module.finrank ℝ (levelPlane ψ p).direction = 2 := by
  rw [levelPlane, AffineSubspace.direction_mk']
  have hr : Module.finrank ℝ (LinearMap.range ψ) = 1 := by
    have hrange : LinearMap.range ψ = ⊤ := by
      obtain ⟨x, hx⟩ : ∃ x, ψ x ≠ 0 := by
        by_contra hc
        push_neg at hc
        exact hψ (LinearMap.ext hc)
      rw [eq_top_iff]
      intro t _
      refine ⟨(t / ψ x) • x, ?_⟩
      rw [map_smul, smul_eq_mul, div_mul_cancel₀ _ hx]
    rw [hrange, finrank_top, Module.finrank_self]
  have := LinearMap.finrank_range_add_finrank_ker ψ
  omega

end QOU.MathlibExt.PL
