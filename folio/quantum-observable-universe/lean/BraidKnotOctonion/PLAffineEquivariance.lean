/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLPolygonalLink

set_option autoImplicit false

/-!
# Affine equivariance of Δ-equivalence (issue #8902, stage 2, part 1)

Stage 2 of #8902 relates Δ-equivalence (`QOU.MathlibExt.PL.DeltaEquiv`) to ambient
piecewise-linear isotopy. This file proves the first, purely affine, ingredient: **an affine
equivalence `f : E ≃ᵃ[ℝ] F` carries polygons, polygonal links, Δ-moves and Δ-equivalence to
polygons, polygonal links, Δ-moves and Δ-equivalence.**

## What is a DEFINITION here

* `Polygon.map f P` — the polygon with vertices `f ∘ P.v`.
* `PolygonalLink.map f L` — the link with components `(L.comp i).map f`.

## What is a THEOREM here

* `Polygon.edge_map`, `Polygon.carrier_map` — the edges and the point set of `P.map f` are the
  images under `f` of those of `P`.
* `Polygon.isSimple_map` — simplicity is preserved.
* `Polygon.map_rotateBy`, `Polygon.map_subdivideLast` — `map` commutes with re-indexing and
  with inserting a vertex.
* `PolygonalLink.carrier_map`, `Move.map`, `DeltaEquiv.map` — **Δ-equivalence is equivariant
  under affine equivalences**: if `L ~ L'` then `L.map f ~ L'.map f`.
* `DeltaEquiv.map_iff` — and conversely, since `f.symm` undoes `f`.

## What is NOT proved here

* That `L.map f` is Δ-equivalent to `L` itself, even for a translation or a rotation of `ℝ³`.
  That is an isotopy statement and needs moving the link in small steps; it is not claimed.
  For an orientation-reversing `f` it is false in general (the mirror image of a chiral knot).
* Anything about piecewise-linear homeomorphisms that are not affine, and the comparison of
  Δ-equivalence with ambient PL isotopy, which remain the rest of stage 2.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E F : Type*} [AddCommGroup E] [Module ℝ E] [AddCommGroup F] [Module ℝ F]

namespace Polygon

variable (f : E ≃ᵃ[ℝ] F) (P : Polygon E)

/-- **The image of a polygon** under an affine equivalence. -/
def map : Polygon F where
  n := P.n
  two_le := P.two_le
  v := f ∘ P.v

@[simp] lemma map_n : (P.map f).n = P.n := rfl

lemma map_v (i : Fin (P.n + 1)) : (P.map f).v i = f (P.v i) := rfl

lemma map_next (i : Fin (P.n + 1)) : (P.map f).next i = P.next i := rfl

theorem edge_map (i : Fin (P.n + 1)) : (P.map f).edge i = f '' P.edge i := by
  simp only [edge, map_v, map_next]
  exact (image_segment ℝ f.toAffineMap _ _).symm

theorem carrier_map : (P.map f).carrier = f '' P.carrier := by
  simp only [carrier, edge_map, image_iUnion]
  rfl

theorem isSimple_map (h : P.IsSimple) : (P.map f).IsSimple := by
  refine ⟨f.injective.comp h.1, fun i j hij => ?_⟩
  rw [edge_map, edge_map, ← image_inter f.injective, h.2 i j hij]
  simp only [map_next, map_v]
  split_ifs <;> simp

theorem map_rotate : P.rotate.map f = (P.map f).rotate := rfl

theorem map_rotateBy (r : ℕ) : (P.rotateBy r).map f = (P.map f).rotateBy r := by
  induction r with
  | zero => rfl
  | succ r ih => simp only [rotateBy, ← ih, map_rotate]

theorem map_subdivideLast (c : E) : (P.subdivideLast c).map f = (P.map f).subdivideLast (f c) := by
  cases P
  simp only [map, subdivideLast, Fin.comp_snoc]

end Polygon

namespace PolygonalLink

variable (f : E ≃ᵃ[ℝ] F) (L : PolygonalLink E)

/-- **The image of a polygonal link** under an affine equivalence. -/
def map : PolygonalLink F where
  k := L.k
  comp i := (L.comp i).map f
  simple i := (L.comp i).isSimple_map f (L.simple i)
  disjoint i j hij := by
    show Disjoint ((L.comp i).map f).carrier ((L.comp j).map f).carrier
    rw [Polygon.carrier_map, Polygon.carrier_map]
    exact (L.disjoint hij).image f.injective.injOn (subset_univ _) (subset_univ _)

lemma map_comp (i : Fin L.k) : (L.map f).comp i = (L.comp i).map f := rfl

theorem carrier_map : (L.map f).carrier = f '' L.carrier := by
  simp only [carrier, map_comp, Polygon.carrier_map, image_iUnion]
  rfl

end PolygonalLink

/-- **A move is carried to a move** by an affine equivalence. -/
theorem Move.map (f : E ≃ᵃ[ℝ] F) {L L' : PolygonalLink E} (h : Move L L') :
    Move (L.map f) (L'.map f) := by
  cases h with
  | relabel e r h =>
    refine Move.relabel (L.map f) (L'.map f) e r fun i => ?_
    show (L'.comp (e i)).map f = ((L.comp i).map f).rotateBy (r i)
    rw [h i, Polygon.map_rotateBy]
  | delta e m c hother hm htri =>
    refine Move.delta (L.map f) (L'.map f) e m (f c) (fun i hi => ?_) ?_ ?_
    · show (L'.comp (e i)).map f = (L.comp i).map f
      rw [hother i hi]
    · show (L'.comp (e m)).map f = ((L.comp m).map f).subdivideLast (f c)
      rw [hm, Polygon.map_subdivideLast]
    · have hT : convexHull ℝ {((L.map f).comp m).v (Fin.last _), ((L.map f).comp m).v 0, f c} =
          f '' convexHull ℝ {(L.comp m).v (Fin.last _), (L.comp m).v 0, c} := by
        have := AffineMap.image_convexHull f.toAffineMap
          {(L.comp m).v (Fin.last _), (L.comp m).v 0, c}
        simp only [AffineEquiv.coe_toAffineMap, image_insert_eq, image_singleton] at this
        rw [this]
        rfl
      rw [hT, PolygonalLink.carrier_map, ← image_inter f.injective, htri]
      exact (image_segment ℝ f.toAffineMap _ _)

/-- **Δ-equivalence is equivariant under affine equivalences.** -/
theorem DeltaEquiv.map (f : E ≃ᵃ[ℝ] F) {L L' : PolygonalLink E} (h : DeltaEquiv L L') :
    DeltaEquiv (L.map f) (L'.map f) := by
  induction h with
  | rel _ _ h => exact Relation.EqvGen.rel _ _ (h.map f)
  | refl => exact Relation.EqvGen.refl _
  | symm _ _ _ ih => exact Relation.EqvGen.symm _ _ ih
  | trans _ _ _ _ _ ih₁ ih₂ => exact Relation.EqvGen.trans _ _ _ ih₁ ih₂

lemma Polygon.map_symm_map (f : E ≃ᵃ[ℝ] F) (P : Polygon E) : (P.map f).map f.symm = P := by
  cases P
  simp only [Polygon.map, Polygon.mk.injEq, heq_eq_eq, true_and]
  funext i
  simp

lemma PolygonalLink.map_symm_map (f : E ≃ᵃ[ℝ] F) (L : PolygonalLink E) :
    (L.map f).map f.symm = L := by
  cases L
  simp only [PolygonalLink.map, PolygonalLink.mk.injEq, heq_eq_eq, true_and]
  funext i
  exact Polygon.map_symm_map f _

/-- **Δ-equivalence is reflected by affine equivalences.** -/
theorem DeltaEquiv.map_iff (f : E ≃ᵃ[ℝ] F) {L L' : PolygonalLink E} :
    DeltaEquiv (L.map f) (L'.map f) ↔ DeltaEquiv L L' := by
  refine ⟨fun h => ?_, DeltaEquiv.map f⟩
  have := h.map f.symm
  rwa [PolygonalLink.map_symm_map, PolygonalLink.map_symm_map] at this

end QOU.MathlibExt.PL
