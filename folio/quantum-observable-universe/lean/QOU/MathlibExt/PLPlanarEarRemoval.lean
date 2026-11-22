/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarTwoEars
import QOU.MathlibExt.PLDropVertex
import QOU.MathlibExt.PLDeltaPoly

set_option autoImplicit false

/-!
# Clipping ears: a simple plane polygon is PL ambient isotopic to a triangle (issue #8902)

Removing an ear is the reverse of a Δ-move: the ear triangle meets the polygon only in its two
sides at the ear vertex (`Polygon.IsEar`), which is the triangle condition of
`PolygonalLink.dropLast`. By the two-ears theorem (`exists_ear`) an ear exists whenever there are
at least four vertices, so clipping ears one at a time ends at a triangle.

## What is a THEOREM here

* `Polygon.exists_eq_subdivideLast` — a polygon with at least four vertices is its last vertex
  inserted on the closing edge of the polygon with that vertex deleted.
* `PolygonalLink.deltaEquiv_triangle` — **a one-component plane link is Δ-equivalent to a
  one-component link whose component is a triangle.**
* `PolygonalLink.plAmbientIsotopic_triangle` — the same, as a **PL ambient isotopy** of the plane.

## What is NOT proved here

* That any two triangles are PL ambient isotopic (and so any two simple plane polygons).
-/

namespace QOU.MathlibExt.PL

open Set Polygon

/-- **Splitting off the last vertex.** -/
lemma Polygon.exists_eq_subdivideLast {E : Type*} [AddCommGroup E] [Module ℝ E] (P : Polygon E)
    (h : 3 ≤ P.n) : ∃ M : Polygon E, P = M.subdivideLast (P.v (Fin.last P.n)) := by
  obtain ⟨n, h2, v⟩ := P
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by simp only at h; omega⟩
  refine ⟨⟨m, by simp only at h; omega, fun i => v i.castSucc⟩, ?_⟩
  simp only [subdivideLast, mk.injEq, heq_eq_eq, true_and]
  funext i
  refine Fin.lastCases ?_ (fun j => ?_) i <;> simp

/-- The three corners of the last-vertex ear of `M.subdivideLast c`. -/
lemma Polygon.subdivideLast_w_ear (M : Polygon R2) (c : R2) :
    (M.subdivideLast c).w ((M.subdivideLast c).n + (M.subdivideLast c).n) = M.v (Fin.last M.n) ∧
      (M.subdivideLast c).w (M.subdivideLast c).n = c ∧
      (M.subdivideLast c).w ((M.subdivideLast c).n + 1) = M.v 0 := by
  set Q := M.subdivideLast c with hQ
  have hn : Q.n = M.n + 1 := rfl
  refine ⟨?_, ?_, ?_⟩
  · rw [← w_mod, show (Q.n + Q.n) % (Q.n + 1) = ((Fin.last M.n).castSucc : Fin (Q.n + 1)).val by
      simp only [Fin.coe_castSucc, Fin.val_last, hn]
      rw [show M.n + 1 + (M.n + 1) = M.n + (M.n + 1 + 1) by omega, Nat.add_mod_right,
        Nat.mod_eq_of_lt (by omega)], w_coe]
    exact M.subdivideLast_v_castSucc c _
  · rw [show Q.n = (Fin.last (M.n + 1) : Fin (Q.n + 1)).val from rfl, w_coe]
    exact M.subdivideLast_v_last c
  · rw [w_period]
    show Q.w (((0 : Fin (M.n + 1)).castSucc : Fin (Q.n + 1)) : ℕ) = _
    rw [w_coe]
    exact M.subdivideLast_v_castSucc c _

namespace PolygonalLink

/-- Rotate every component of a link by `r` steps. -/
def rotateAll {E : Type*} [AddCommGroup E] [Module ℝ E] (L : PolygonalLink E) (r : ℕ) :
    PolygonalLink E where
  k := L.k
  comp := fun i => (L.comp i).rotateBy r
  simple := fun i => (L.comp i).isSimple_rotateBy (L.simple i) r
  disjoint := fun i j hij => by
    simp only [carrier_rotateBy]; exact L.disjoint hij

lemma deltaEquiv_rotateAll {E : Type*} [AddCommGroup E] [Module ℝ E] (L : PolygonalLink E)
    (r : ℕ) : DeltaEquiv L (L.rotateAll r) :=
  Relation.EqvGen.rel _ _ (Move.relabel L (L.rotateAll r) (Equiv.refl _) (fun _ => r)
    (fun _ => rfl))

/-- **One-component plane links clip down to a triangle.** -/
theorem deltaEquiv_triangle (L : PolygonalLink R2) (hk : L.k = 1) :
    ∃ L' : PolygonalLink R2, DeltaEquiv L L' ∧ L'.k = 1 ∧ ∀ i, (L'.comp i).n = 2 := by
  suffices H : ∀ N, ∀ L : PolygonalLink R2, L.k = 1 → ∀ i, (L.comp i).n = N →
      ∃ L' : PolygonalLink R2, DeltaEquiv L L' ∧ L'.k = 1 ∧ ∀ i, (L'.comp i).n = 2 from
    H _ L hk ⟨0, by omega⟩ rfl
  intro N
  induction N using Nat.strong_induction_on with
  | _ N ih =>
  intro L hk i hN
  have hall : ∀ j : Fin L.k, j = i := fun j => Fin.ext (by have := j.2; have := i.2; omega)
  by_cases h2 : N = 2
  · refine ⟨L, Relation.EqvGen.refl _, hk, fun j => ?_⟩
    rw [hall j, hN, h2]
  have hn3 : 3 ≤ (L.comp i).n := by have := (L.comp i).two_le; omega
  set P := L.comp i with hP
  obtain ⟨k, hear, -, -⟩ := exists_ear P (L.simple i) hn3 0
  set r := k + 1 with hr
  set L₁ := L.rotateAll r with hL₁
  set R := L₁.comp i with hR
  have hRn : R.n = P.n := rotateBy_n P r
  have hRear : R.IsEar R.n := by
    rw [hR, show L₁.comp i = P.rotateBy r from rfl, isEar_rotateBy, rotateBy_n,
      show P.n + r = k + (P.n + 1) by omega, isEar_add_period]
    exact hear
  obtain ⟨M, hM⟩ := R.exists_eq_subdivideLast (by omega)
  set c := R.v (Fin.last R.n) with hc
  have hcomp : L₁.comp i = M.subdivideLast c := hM
  have hL₁carrier : L₁.carrier = R.carrier := by
    apply Subset.antisymm
    · intro z hz
      obtain ⟨j, hj⟩ := mem_iUnion.mp hz
      rw [show j = i from hall j] at hj
      exact hj
    · exact L₁.comp_carrier_subset i
  have hT : convexHull ℝ {M.v (Fin.last M.n), M.v 0, c} ∩ L₁.carrier ⊆
      segment ℝ (M.v (Fin.last M.n)) c ∪ segment ℝ c (M.v 0) := by
    rw [hL₁carrier, hM]
    obtain ⟨e1, e2, e3⟩ := M.subdivideLast_w_ear c
    have h := hRear.2.1
    rw [hM, e1, e2, e3] at h
    rwa [Set.pair_comm c (M.v 0)] at h
  set L₂ := L₁.dropLast i M c hcomp hT with hL₂
  have hL₂i : L₂.comp i = M := Function.update_self _ _ _
  have hMn : M.n < N := by
    have h1 : R.n = M.n + 1 := by rw [hM]; rfl
    rw [← hN]
    show M.n < P.n
    omega
  obtain ⟨L', hL', hk', h2'⟩ := ih M.n hMn L₂ hk i (by rw [hL₂i])
  refine ⟨L', ?_, hk', h2'⟩
  exact (L.deltaEquiv_rotateAll r).trans _ _ _
    ((L₁.deltaEquiv_dropLast i M c hcomp hT).trans _ _ _ hL')

/-- **Every simple plane polygon is PL ambient isotopic to a triangle.** -/
theorem plAmbientIsotopic_triangle (L : PolygonalLink R2) (hk : L.k = 1) :
    ∃ L' : PolygonalLink R2, PLAmbientIsotopic L L' ∧ L'.k = 1 ∧ ∀ i, (L'.comp i).n = 2 := by
  obtain ⟨L', h, hk', h2⟩ := deltaEquiv_triangle L hk
  exact ⟨L', h.plAmbientIsotopic, hk', h2⟩

end PolygonalLink

end QOU.MathlibExt.PL
