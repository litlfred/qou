/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLSlice

set_option autoImplicit false

/-!
# Slicing a closed surface (issue #8902, Moise build part B, 3D Schoenflies)

Alexander's proof of the PL Schoenflies theorem in `ℝ³` slices the sphere by planes in general
position. Each slice is a finite graph; this file shows that it is **2-regular** when the
triangulated surface is closed (every edge lies on exactly two triangles). A finite 2-regular
graph is a disjoint union of cycles, which are then simple polygons in the plane of the slice.

## What is a THEOREM here

* `crossPt_edge_unique` — two edges of a complex that cross the hyperplane at the same point are
  the same edge (with the same orientation across the hyperplane).
* `crossSet_triangle` — a triangle through a crossing edge `{u, v}` slices to a segment through
  `crossPt u v`, i.e. its crossing set has two points and contains `crossPt u v`.
* `slice_vertex_degree` — **every vertex of the slice of a closed surface lies on exactly two
  slice edges.**
-/

namespace QOU.MathlibExt.PL

open Set Geometry

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] {ψ : E →L[ℝ] ℝ} {c : ℝ}

lemma coe_pair_convexHull (u v : E) [DecidableEq E] :
    convexHull ℝ ((({u, v} : Finset E)) : Set E) = segment ℝ u v := by
  rw [Finset.coe_insert, Finset.coe_singleton, convexHull_pair]

/-- **A crossing point determines its edge.** -/
theorem crossPt_edge_unique [DecidableEq E] {K : SimplicialComplex ℝ E} {u v u' v' : E}
    (he : ({u, v} : Finset E) ∈ K.faces) (he' : ({u', v'} : Finset E) ∈ K.faces)
    (hu : ψ u < c) (hv : c < ψ v) (hu' : ψ u' < c) (hv' : c < ψ v')
    (h : crossPt ψ c u v = crossPt ψ c u' v') : u = u' ∧ v = v' := by
  set p := crossPt ψ c u v with hpdef
  have hp : ψ p = c := map_crossPt (by intro h; linarith)
  have hmem : p ∈ convexHull ℝ ((({u, v} : Finset E) : Set E) ∩ (({u', v'} : Finset E) : Set E)) := by
    rw [← K.convexHull_inter_convexHull he he']
    refine ⟨?_, ?_⟩
    · rw [coe_pair_convexHull]; exact crossPt_mem_segment hu hv
    · rw [coe_pair_convexHull, h]; exact crossPt_mem_segment hu' hv'
  have hcol : ∀ z : E, ((({u, v} : Finset E) : Set E) ∩ (({u', v'} : Finset E) : Set E)) ⊆ {z} →
      p = z := fun z hz => by
    have := convexHull_mono hz hmem
    rwa [convexHull_singleton, mem_singleton_iff] at this
  have hut : u ∈ ({u', v'} : Finset E) := by
    by_contra hn
    have := hcol v (by
      rintro z ⟨hz, hz'⟩
      simp only [Finset.coe_insert, Finset.coe_singleton, mem_insert_iff,
        mem_singleton_iff] at hz ⊢
      rcases hz with rfl | rfl
      · exact absurd (by simpa using hz') hn
      · rfl)
    rw [this] at hp; linarith
  have hvt : v ∈ ({u', v'} : Finset E) := by
    by_contra hn
    have := hcol u (by
      rintro z ⟨hz, hz'⟩
      simp only [Finset.coe_insert, Finset.coe_singleton, mem_insert_iff,
        mem_singleton_iff] at hz ⊢
      rcases hz with rfl | rfl
      · rfl
      · exact absurd (by simpa using hz') hn)
    rw [this] at hp; linarith
  simp only [Finset.mem_insert, Finset.mem_singleton] at hut hvt
  refine ⟨hut.resolve_right (by rintro rfl; linarith), hvt.resolve_left (by rintro rfl; linarith)⟩

lemma pair_mem_faces [DecidableEq E] {K : SimplicialComplex ℝ E} {τ : Finset E}
    (hτ : τ ∈ K.faces) {a b : E} (ha : a ∈ τ) (hb : b ∈ τ) : ({a, b} : Finset E) ∈ K.faces :=
  K.down_closed hτ (Finset.insert_subset ha (Finset.singleton_subset_iff.mpr hb)) (by simp)

/-- **A triangle through a crossing edge slices to a segment through its crossing point.** -/
theorem crossSet_triangle [DecidableEq E] {K : SimplicialComplex ℝ E}
    (hgen : ∀ s ∈ K.faces, ∀ v ∈ s, ψ v ≠ c) {τ : Finset E} (hτ : τ ∈ K.faces)
    (h3 : τ.card = 3) {u v : E} (hu : u ∈ τ) (hv : v ∈ τ) (hu' : ψ u < c) (hv' : c < ψ v) :
    crossPt ψ c u v ∈ crossSet ψ c τ ∧ (crossSet ψ c τ).card = 2 := by
  have hx : crossPt ψ c u v ∈ crossSet ψ c τ := mem_crossSet.mpr ⟨u, hu, v, hv, hu', hv', rfl⟩
  refine ⟨hx, le_antisymm (card_crossSet_le_two h3.le) ?_⟩
  have huv : u ≠ v := by rintro rfl; linarith
  obtain ⟨w, hw, hwu, hwv⟩ : ∃ w ∈ τ, w ≠ u ∧ w ≠ v := by
    by_contra hcon
    push_neg at hcon
    have : τ ⊆ {u, v} := fun w hw => by
      by_cases h : w = u
      · simp [h]
      · simp [hcon w hw h]
    have := Finset.card_le_card this
    rw [Finset.card_pair huv] at this
    omega
  rcases lt_or_gt_of_ne (hgen τ hτ w hw) with hwc | hwc
  · have hy : crossPt ψ c w v ∈ crossSet ψ c τ := mem_crossSet.mpr ⟨w, hw, v, hv, hwc, hv', rfl⟩
    refine Finset.one_lt_card.mpr ⟨_, hx, _, hy, fun h => hwu ?_⟩
    exact ((crossPt_edge_unique (pair_mem_faces hτ hu hv) (pair_mem_faces hτ hw hv) hu' hv' hwc
      hv' h).1).symm
  · have hy : crossPt ψ c u w ∈ crossSet ψ c τ := mem_crossSet.mpr ⟨u, hu, w, hw, hu', hwc, rfl⟩
    refine Finset.one_lt_card.mpr ⟨_, hx, _, hy, fun h => hwv ?_⟩
    exact ((crossPt_edge_unique (pair_mem_faces hτ hu hv) (pair_mem_faces hτ hu hw) hu' hv' hu'
      hwc h).2).symm

/-- The triangles of `K` on an edge `e`. -/
def trianglesOn (K : SimplicialComplex ℝ E) (e : Finset E) : Set (Finset E) :=
  {t | t ∈ K.faces ∧ e ⊆ t ∧ t.card = 3}

/-- **A closed surface**: dimension at most two, and every edge lies on exactly two triangles. -/
def IsClosedSurface (K : SimplicialComplex ℝ E) : Prop :=
  (∀ s ∈ K.faces, s.card ≤ 3) ∧ ∀ e ∈ K.faces, e.card = 2 → (trianglesOn K e).ncard = 2

/-- **The slice of a closed surface is 2-regular**: each slice vertex lies on exactly two slice
edges. -/
theorem slice_vertex_degree [DecidableEq E] {K : SimplicialComplex ℝ E} (hK : IsClosedSurface K)
    (hgen : ∀ s ∈ K.faces, ∀ v ∈ s, ψ v ≠ c) {x : E}
    (hx : {x} ∈ (sliceComplex K hK.1 hgen).faces) :
    {σ | σ ∈ (sliceComplex K hK.1 hgen).faces ∧ x ∈ σ ∧ σ.card = 2}.ncard = 2 := by
  obtain ⟨u, v, he, hu', hv', rfl⟩ := sliceComplex_vertex hx
  have huv : u ≠ v := by rintro rfl; linarith
  have hu : u ∈ ({u, v} : Finset E) := by simp
  have hv : v ∈ ({u, v} : Finset E) := by simp
  have himage : {σ | σ ∈ (sliceComplex K hK.1 hgen).faces ∧ crossPt ψ c u v ∈ σ ∧ σ.card = 2} =
      crossSet ψ c '' trianglesOn K {u, v} := by
    ext σ
    constructor
    · rintro ⟨hσ, hxσ, h2⟩
      obtain ⟨τ, hτ, h3, rfl, -⟩ := sliceComplex_edge hσ h2
      refine ⟨τ, ⟨hτ, ?_, h3⟩, rfl⟩
      obtain ⟨a, ha, b, hb, ha', hb', hab⟩ := mem_crossSet.mp hxσ
      obtain ⟨rfl, rfl⟩ := crossPt_edge_unique (pair_mem_faces hτ ha hb) he ha' hb' hu' hv' hab
      exact Finset.insert_subset ha (Finset.singleton_subset_iff.mpr hb)
    · rintro ⟨τ, ⟨hτ, hsub, h3⟩, rfl⟩
      obtain ⟨hxτ, h2⟩ := crossSet_triangle hgen hτ h3 (hsub hu) (hsub hv) hu' hv'
      exact ⟨⟨τ, hτ, rfl, ⟨_, hxτ⟩⟩, hxτ, h2⟩
  rw [himage, Set.ncard_image_of_injOn, hK.2 _ he (Finset.card_pair huv)]
  -- injectivity
  rintro τ ⟨hτ, hsub, h3⟩ τ' ⟨hτ', hsub', h3'⟩ heq
  obtain ⟨hxτ, h2⟩ := crossSet_triangle hgen hτ h3 (hsub hu) (hsub hv) hu' hv'
  obtain ⟨y, hy, hyx⟩ := Finset.exists_mem_ne (by omega : 1 < (crossSet ψ c τ).card)
    (crossPt ψ c u v)
  have hy' : y ∈ crossSet ψ c τ' := heq ▸ hy
  obtain ⟨a, ha, b, hb, ha', hb', rfl⟩ := mem_crossSet.mp hy
  obtain ⟨a', ha2, b', hb2, ha2', hb2', hab⟩ := mem_crossSet.mp hy'
  obtain ⟨rfl, rfl⟩ := crossPt_edge_unique (pair_mem_faces hτ' ha2 hb2) (pair_mem_faces hτ ha hb)
    ha2' hb2' ha' hb' hab
  -- some vertex of `{a, b}` lies off `{u, v}`
  obtain ⟨z, hzτ, hzτ', hzu, hzv⟩ : ∃ z, z ∈ τ ∧ z ∈ τ' ∧ z ≠ u ∧ z ≠ v := by
    by_cases hau : a' = u
    · subst hau
      refine ⟨b', hb, hb2, fun h => by subst h; linarith, fun h => hyx (by rw [h])⟩
    · exact ⟨a', ha, ha2, hau, fun h => by subst h; linarith⟩
  have key : ∀ t : Finset E, t.card = 3 → {u, v} ⊆ t → z ∈ t → t = {z, u, v} := by
    intro t ht hs hz
    have hsub3 : ({z, u, v} : Finset E) ⊆ t :=
      Finset.insert_subset hz hs
    have hc : ({z, u, v} : Finset E).card = 3 := by
      rw [Finset.card_insert_of_notMem (by simp [hzu, hzv]), Finset.card_pair huv]
    exact (Finset.eq_of_subset_of_card_le hsub3 (by omega)).symm
  rw [key τ h3 hsub hzτ, key τ' h3' hsub' hzτ']

end QOU.MathlibExt.PL
