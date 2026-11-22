/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarDisk
import Mathlib.Analysis.Convex.KreinMilman

set_option autoImplicit false

/-!
# Regions of disjoint simple plane polygons are nested or disjoint (issue #8902, part B)

Alexander's proof of the PL Schoenflies theorem in three dimensions caps the polygons of a slice
with planar disks. When a slice has several polygons, the capping disks have to be compared: two
disjoint simple polygons in a plane bound regions that are either nested or disjoint. This file
proves that from the crossing parity, using only that a polygon and its region are connected and
that the region lies in the convex hull of the vertices.

## What is a THEOREM here

* `Polygon.isPreconnected_carrier` — the point set of a polygon is connected.
* `Polygon.isPreconnected_region` — the region of a simple plane polygon is connected.
* `Polygon.region_subset_convexHull` — the region lies in the convex hull of the vertices.
* `Polygon.region_nested_or_disjoint` — **the regions of two simple plane polygons with disjoint
  carriers are nested or disjoint.**

The case in which each polygon lies inside the other is excluded by convex hulls: both hulls would
coincide, and an extreme point of that hull would be a vertex of both polygons.
-/

namespace QOU.MathlibExt.PL

open Set

namespace Polygon

lemma zmod2_cases (x : ZMod 2) : x = 0 ∨ x = 1 := by
  fin_cases x <;> simp

/-- **The point set of a plane polygon is connected.** -/
theorem isPreconnected_carrier (P : Polygon R2) : IsPreconnected P.carrier := by
  have h : P.carrier = ⋃ k ∈ Set.Iic P.n, P.seg k := by
    rw [carrier_eq_biUnion]
    ext x
    simp only [mem_iUnion, Finset.mem_range, mem_Iic, Nat.lt_succ_iff, exists_prop]
  rw [h]
  refine IsPreconnected.biUnion_of_chain Set.ordConnected_Iic
    (fun k _ => (convex_segment _ _).isPreconnected) ?_
  intro k _ _
  refine ⟨P.w (k + 1), right_mem_segment ℝ _ _, ?_⟩
  rw [Order.succ_eq_add_one]
  exact left_mem_segment ℝ _ _

lemma w_mem_carrier (P : Polygon R2) (j : ℕ) : P.w j ∈ P.carrier :=
  P.vertex_mem_carrier _

/-- **The region of a simple plane polygon is connected.** -/
theorem isPreconnected_region (P : Polygon R2) (hP : P.IsSimple) : IsPreconnected P.region := by
  obtain ⟨ts, hts, hreg⟩ := P.region_eq_iUnion_triangles hP
  have hreg' : P.region = P.carrier ∪ ⋃ t ∈ ts, convexHull ℝ {t.1, t.2.1, t.2.2} := by
    refine Subset.antisymm (fun y hy => Or.inr (hreg ▸ hy)) ?_
    rintro y (hy | hy)
    · exact Or.inl hy
    · rw [hreg]; exact hy
  rw [hreg']
  suffices H : ∀ l : List (R2 × R2 × R2), (∀ t ∈ l, ∃ j, P.w j = t.1) →
      IsPreconnected (P.carrier ∪ ⋃ t ∈ l, convexHull ℝ ({t.1, t.2.1, t.2.2} : Set R2)) from
    H ts (fun t ht => (hts t ht).2.1)
  intro l
  induction l with
  | nil =>
      intro _
      simpa using P.isPreconnected_carrier
  | cons t l ih =>
      intro hl
      have hsplit : P.carrier ∪ ⋃ t' ∈ t :: l, convexHull ℝ ({t'.1, t'.2.1, t'.2.2} : Set R2) =
          (P.carrier ∪ ⋃ t' ∈ l, convexHull ℝ ({t'.1, t'.2.1, t'.2.2} : Set R2)) ∪
            convexHull ℝ {t.1, t.2.1, t.2.2} := by
        ext y
        simp only [mem_union, mem_iUnion, List.mem_cons, exists_prop]
        constructor
        · rintro (h | ⟨t', rfl | ht', hy⟩)
          · exact Or.inl (Or.inl h)
          · exact Or.inr hy
          · exact Or.inl (Or.inr ⟨t', ht', hy⟩)
        · rintro ((h | ⟨t', ht', hy⟩) | h)
          · exact Or.inl h
          · exact Or.inr ⟨t', Or.inr ht', hy⟩
          · exact Or.inr ⟨t, Or.inl rfl, h⟩
      rw [hsplit]
      obtain ⟨j, hj⟩ := hl t (List.mem_cons_self ..)
      refine IsPreconnected.union' ⟨t.1, Or.inl (hj ▸ P.w_mem_carrier j), ?_⟩
        (ih fun t' ht' => hl t' (List.mem_cons_of_mem _ ht'))
        (convex_convexHull ℝ _).isPreconnected
      exact subset_convexHull ℝ _ (mem_insert _ _)

/-- **The region lies in the convex hull of the vertices.** -/
theorem region_subset_convexHull (P : Polygon R2) : P.region ⊆ convexHull ℝ (range P.v) := by
  rintro y (hy | hy)
  · exact P.carrier_subset_convexHull hy
  · by_contra h
    have h0 := P.parity_eq_zero_of_not_mem_convexHull h
    rw [mem_setOf_eq, h0] at hy
    exact absurd hy (by decide)

/-- If the second polygon lies outside the first, the first region misses the second polygon and
is either disjoint from, or contained in, the second region. -/
lemma nested_or_disjoint_of_outside {P Q : Polygon R2} (hP : P.IsSimple)
    (hPQ : Disjoint P.carrier Q.carrier) (hout : P.parity (Q.v 0) = 0) :
    Disjoint P.region Q.region ∨ P.region ⊆ Q.region := by
  have hQc : ∀ y ∈ Q.carrier, P.parity y = 0 := fun y hy =>
    (P.parity_const_of_isPreconnected Q.isPreconnected_carrier hPQ.symm hy
      (Q.vertex_mem_carrier 0)).trans hout
  have hmiss : Disjoint P.region Q.carrier := by
    rw [Set.disjoint_right]
    intro y hy hyP
    rcases hyP with hyP | hyP
    · exact Set.disjoint_left.mp hPQ hyP hy
    · rw [mem_setOf_eq, hQc y hy] at hyP
      exact absurd hyP (by decide)
  have hconst : ∀ y ∈ P.region, Q.parity y = Q.parity (P.v 0) := fun y hy =>
    Q.parity_const_of_isPreconnected (P.isPreconnected_region hP) hmiss hy
      (Or.inl (P.vertex_mem_carrier 0))
  rcases zmod2_cases (Q.parity (P.v 0)) with h0 | h1
  · left
    rw [Set.disjoint_left]
    intro y hyP hyQ
    rcases hyQ with hyQ | hyQ
    · exact Set.disjoint_left.mp hmiss hyP hyQ
    · rw [mem_setOf_eq, hconst y hyP, h0] at hyQ
      exact absurd hyQ (by decide)
  · right
    intro y hy
    exact Or.inr ((hconst y hy).trans h1)

/-- **The regions of two simple plane polygons with disjoint carriers are nested or disjoint.** -/
theorem region_nested_or_disjoint {P Q : Polygon R2} (hP : P.IsSimple) (hQ : Q.IsSimple)
    (hPQ : Disjoint P.carrier Q.carrier) :
    P.region ⊆ Q.region ∨ Q.region ⊆ P.region ∨ Disjoint P.region Q.region := by
  rcases zmod2_cases (P.parity (Q.v 0)) with hP0 | hP1
  · rcases nested_or_disjoint_of_outside hP hPQ hP0 with h | h
    · exact Or.inr (Or.inr h)
    · exact Or.inl h
  rcases zmod2_cases (Q.parity (P.v 0)) with hQ0 | hQ1
  · rcases nested_or_disjoint_of_outside hQ hPQ.symm hQ0 with h | h
    · exact Or.inr (Or.inr h.symm)
    · exact Or.inr (Or.inl h)
  -- Each polygon lies inside the other: impossible.
  exfalso
  have hin : ∀ {A B : Polygon R2}, Disjoint A.carrier B.carrier → A.parity (B.v 0) = 1 →
      convexHull ℝ (range B.v) ⊆ convexHull ℝ (range A.v) := by
    intro A B hAB h1
    refine convexHull_min ?_ (convex_convexHull ℝ _)
    rintro _ ⟨i, rfl⟩
    refine A.region_subset_convexHull (Or.inr ?_)
    rw [mem_setOf_eq, ← h1]
    exact A.parity_const_of_isPreconnected B.isPreconnected_carrier hAB.symm
      (B.vertex_mem_carrier i) (B.vertex_mem_carrier 0)
  have heq : convexHull ℝ (range Q.v) = convexHull ℝ (range P.v) :=
    Subset.antisymm (hin hPQ hP1) (hin hPQ.symm hQ1)
  have hcpt : IsCompact (convexHull ℝ (range P.v)) := (finite_range _).isCompact_convexHull
  obtain ⟨x, hx⟩ := hcpt.extremePoints_nonempty
    ⟨P.v 0, subset_convexHull ℝ _ (mem_range_self 0)⟩
  have hxP : x ∈ range P.v := extremePoints_convexHull_subset hx
  have hxQ : x ∈ range Q.v := by
    rw [← heq] at hx
    exact extremePoints_convexHull_subset hx
  obtain ⟨i, rfl⟩ := hxP
  obtain ⟨j, hj⟩ := hxQ
  exact Set.disjoint_left.mp hPQ (P.vertex_mem_carrier i) (hj ▸ Q.vertex_mem_carrier j)

end Polygon

end QOU.MathlibExt.PL
