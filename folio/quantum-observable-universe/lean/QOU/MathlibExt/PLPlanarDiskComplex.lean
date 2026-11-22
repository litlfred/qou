/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarDisk
import QOU.MathlibExt.PLSurfaceSlice
import Mathlib.LinearAlgebra.AffineSpace.FiniteDimensional

set_option autoImplicit false

/-!
# The region of a simple plane polygon is triangulated (issue #8902, part B)

`Polygon.region_eq_iUnion_triangles` writes the region of a simple plane polygon as a union of ear
triangles. Here the ear triangles are shown to fit together: the region is the space of a finite
simplicial complex of triangles whose vertices are vertices of the polygon and in which every edge
of the polygon is a face. This is the planar PL Schoenflies theorem in triangulated form.

The key geometric fact is `Polygon.ear_inter_region`: a clipped ear meets the region of the clipped
polygon only in the chord. Since the chord is an edge of the clipped polygon, and so a face of its
triangulation, the ear triangle can be glued on along it (`unionComplex`).

## What is a DEFINITION here

* `simplexComplex s hs` — the complex of all nonempty faces of one affinely independent set.
* `unionComplex K L h` — the union of two complexes whose faces meet in common faces.

## What is a THEOREM here

* `affineIndependent_triangle` — three points with nonzero `cross` are affinely independent.
* `Polygon.ear_inter_region` — **an ear triangle meets the region of the clipped polygon only in the
  chord.**
* `Polygon.exists_triangulation_region` — **the region of a simple plane polygon is the space of a
  finite simplicial complex of dimension at most two, whose vertices are vertices of the polygon
  and in which every edge of the polygon is a face.**
-/

namespace QOU.MathlibExt.PL

open Set Geometry

section Complexes

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- The simplicial complex of all nonempty faces of one simplex. -/
def simplexComplex (s : Finset E) (hs : AffineIndependent ℝ ((↑) : s → E)) :
    SimplicialComplex ℝ E where
  faces := {t | t.Nonempty ∧ t ⊆ s}
  empty_notMem := fun h => Finset.not_nonempty_empty h.1
  indep := fun ht => AffineIndependent.mono hs (Finset.coe_subset.mpr ht.2)
  down_closed := fun ht hut hu => ⟨Finset.nonempty_iff_ne_empty.mpr hu, hut.trans ht.2⟩
  inter_subset_convexHull := fun ht hu => (hs.convexHull_inter ht.2 hu.2).ge

lemma simplexComplex_space (s : Finset E) (hs : AffineIndependent ℝ ((↑) : s → E))
    (hne : s.Nonempty) : (simplexComplex s hs).space = convexHull ℝ (s : Set E) := by
  ext x
  rw [SimplicialComplex.mem_space_iff]
  constructor
  · rintro ⟨t, ht, hx⟩
    exact convexHull_mono (Finset.coe_subset.mpr ht.2) hx
  · intro hx
    exact ⟨s, ⟨hne, Finset.Subset.refl s⟩, hx⟩

/-- The union of two complexes whose faces meet in common faces. -/
def unionComplex (K L : SimplicialComplex ℝ E)
    (h : ∀ s ∈ K.faces, ∀ t ∈ L.faces,
      convexHull ℝ (s : Set E) ∩ convexHull ℝ ↑t ⊆ convexHull ℝ (s ∩ t : Set E)) :
    SimplicialComplex ℝ E where
  faces := K.faces ∪ L.faces
  empty_notMem := fun h' => h'.elim K.empty_notMem L.empty_notMem
  indep := fun hs => hs.elim K.indep L.indep
  down_closed := fun hs hts ht =>
    hs.imp (fun h' => K.down_closed h' hts ht) (fun h' => L.down_closed h' hts ht)
  inter_subset_convexHull := by
    rintro s t (hs | hs) (ht | ht)
    · exact K.inter_subset_convexHull hs ht
    · exact h s hs t ht
    · rw [Set.inter_comm (convexHull ℝ (s : Set E)), Set.inter_comm (s : Set E)]
      exact h t ht s hs
    · exact L.inter_subset_convexHull hs ht

lemma unionComplex_space (K L : SimplicialComplex ℝ E) (h) :
    (unionComplex K L h).space = K.space ∪ L.space := by
  ext x
  simp only [SimplicialComplex.mem_space_iff, mem_union]
  constructor
  · rintro ⟨s, hs | hs, hx⟩
    · exact Or.inl ⟨s, hs, hx⟩
    · exact Or.inr ⟨s, hs, hx⟩
  · rintro (⟨s, hs, hx⟩ | ⟨s, hs, hx⟩)
    · exact ⟨s, Or.inl hs, hx⟩
    · exact ⟨s, Or.inr hs, hx⟩

end Complexes

/-- **Three points with nonzero `cross` are affinely independent.** -/
lemma affineIndependent_triangle [DecidableEq R2] {a c b : R2} (hD : cross a c b ≠ 0) :
    AffineIndependent ℝ ((↑) : ({a, c, b} : Finset R2) → R2) := by
  have hnc : ¬ Collinear ℝ ({a, c, b} : Set R2) := by
    intro hcol
    obtain ⟨v, hv⟩ := (collinear_iff_of_mem (by simp : a ∈ ({a, c, b} : Set R2))).mp hcol
    obtain ⟨r1, h1⟩ := hv c (by simp)
    obtain ⟨r2, h2⟩ := hv b (by simp)
    apply hD
    unfold cross
    rw [h1, h2]
    simp only [vadd_eq_add, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    ring
  have hi := affineIndependent_iff_not_collinear_set.mpr hnc
  refine hi.range.mono ?_
  intro x hx
  have hx' : x ∈ ({a, c, b} : Finset R2) := hx
  simp only [Finset.mem_insert, Finset.mem_singleton] at hx'
  rcases hx' with rfl | rfl | rfl
  · exact ⟨0, rfl⟩
  · exact ⟨1, rfl⟩
  · exact ⟨2, rfl⟩

namespace Polygon

/-- **An ear meets the region of the clipped polygon only in the chord.** -/
theorem ear_inter_region (M : Polygon R2) (c : R2) (hQ : (M.subdivideLast c).IsSimple)
    (hD : cross (M.v (Fin.last M.n)) c (M.v 0) ≠ 0)
    (hT : convexHull ℝ {M.v (Fin.last M.n), c, M.v 0} ∩ (M.subdivideLast c).carrier ⊆
      segment ℝ (M.v (Fin.last M.n)) c ∪ segment ℝ c (M.v 0))
    (hpar : ∀ y ∈ openTri (M.v (Fin.last M.n)) c (M.v 0), (M.subdivideLast c).parity y = 1) :
    convexHull ℝ {M.v (Fin.last M.n), c, M.v 0} ∩ M.region ⊆
      segment ℝ (M.v (Fin.last M.n)) (M.v 0) := by
  set a := M.v (Fin.last M.n) with ha
  set b := M.v 0 with hb
  set P := M.subdivideLast c with hP
  -- `M` has parity `0` in the open ear
  have hM0 : ∀ z ∈ openTri a c b, M.parity z = 0 := by
    intro z hz
    have h1 := hpar z hz
    have h2 := triPoly_parity_eq_one hD (openTri_subset_hull hD hz)
      (Set.disjoint_left.mp (disjoint_openTri a c b) hz)
    have := parity_subdivideLast M c z
    rw [← hP, h1, h2] at this
    linear_combination this.symm
  rintro y ⟨hyT, hyR⟩
  have hyM : y ∈ M.carrier := by
    rcases hyR with hyR | hyR
    · exact hyR
    · by_contra hn
      have h0 := parity_eq_of_mem_convexHull M hD 0 hM0 hyT hn
      rw [mem_setOf_eq, h0] at hyR
      exact zero_ne_one hyR
  obtain ⟨k, hk⟩ := mem_iUnion.mp hyM
  by_cases hkl : k = Fin.last M.n
  · rw [hkl, M.edge_last] at hk
    exact hk
  · have hyP : y ∈ P.carrier := by
      have := hk
      rw [← M.subdivideLast_edge_castSucc c hkl] at this
      exact P.edge_subset_carrier _ this
    rcases mem_new_edges M c hQ hkl hk (hT ⟨hyT, hyP⟩) with h | h
    · rw [h]; exact left_mem_segment ℝ _ _
    · rw [h]; exact right_mem_segment ℝ _ _

lemma w_rotateBy_back (P : Polygon R2) (r j : ℕ) : (P.rotateBy r).w (j + P.n * r) = P.w j := by
  rw [w_rotateBy, ← w_mod, show j + P.n * r + r = j + (P.n + 1) * r by ring,
    Nat.add_mul_mod_self_left, w_mod]

lemma w_last_eq (M : Polygon R2) : M.w M.n = M.v (Fin.last M.n) := by rw [← w_coe]; rfl

lemma w_succ_last_eq (M : Polygon R2) : M.w (M.n + 1) = M.v 0 := by rw [w_period, ← w_coe]; rfl

/-- **The planar PL Schoenflies theorem, triangulated form.** The region of a simple plane polygon
is the space of a finite simplicial complex of dimension at most two whose vertices are vertices of
the polygon and in which every edge of the polygon is a face. -/
theorem exists_triangulation_region [DecidableEq R2] (P : Polygon R2) (hP : P.IsSimple) :
    ∃ K : SimplicialComplex ℝ R2, K.faces.Finite ∧ (∀ s ∈ K.faces, s.card ≤ 3) ∧
      (∀ s ∈ K.faces, ∀ x ∈ s, ∃ j, P.w j = x) ∧
      (∀ j, ({P.w j, P.w (j + 1)} : Finset R2) ∈ K.faces) ∧ K.space = P.region := by
  suffices H : ∀ N, ∀ P : Polygon R2, P.n = N → P.IsSimple →
      ∃ K : SimplicialComplex ℝ R2, K.faces.Finite ∧ (∀ s ∈ K.faces, s.card ≤ 3) ∧
        (∀ s ∈ K.faces, ∀ x ∈ s, ∃ j, P.w j = x) ∧
        (∀ j, ({P.w j, P.w (j + 1)} : Finset R2) ∈ K.faces) ∧ K.space = P.region from
    H _ P rfl hP
  intro N
  induction N using Nat.strong_induction_on with
  | _ N ih =>
  intro P hN hP
  -- faces of a single simplex
  have hsimplex : ∀ (s0 : Finset R2) (hs : AffineIndependent ℝ ((↑) : s0 → R2)),
      (simplexComplex s0 hs).faces.Finite ∧
        ∀ t ∈ (simplexComplex s0 hs).faces, t ⊆ s0 := fun s0 hs =>
    ⟨(s0.powerset.finite_toSet).subset fun t ht =>
      Finset.mem_coe.mpr (Finset.mem_powerset.mpr ht.2), fun t ht => ht.2⟩
  by_cases h2 : P.n = 2
  · have hD := cross_ne_zero_of_isSimple hP h2
    set s0 : Finset R2 := {P.w 0, P.w 1, P.w 2} with hs0
    have hw : ∀ j, P.w j ∈ s0 := by
      intro j
      rw [← w_mod, h2]
      have : j % 3 < 3 := Nat.mod_lt _ (by norm_num)
      interval_cases (j % 3) <;> simp [hs0]
    obtain ⟨hfin, hsub⟩ := hsimplex s0 (affineIndependent_triangle hD)
    refine ⟨simplexComplex s0 (affineIndependent_triangle hD), hfin, fun t ht => ?_,
      fun t ht x hx => ?_, fun j => ?_, ?_⟩
    · exact (Finset.card_le_card (hsub t ht)).trans Finset.card_le_three
    · have := hsub t ht hx
      simp only [hs0, Finset.mem_insert, Finset.mem_singleton] at this
      rcases this with rfl | rfl | rfl
      · exact ⟨0, rfl⟩
      · exact ⟨1, rfl⟩
      · exact ⟨2, rfl⟩
    · refine ⟨⟨P.w j, by simp⟩, ?_⟩
      intro x hx
      simp only [Finset.mem_insert, Finset.mem_singleton] at hx
      rcases hx with rfl | rfl
      · exact hw _
      · exact hw _
    · rw [simplexComplex_space _ _ ⟨P.w 0, by simp [hs0]⟩, region_eq_triPoly P h2,
        region_triPoly hD, hs0]
      push_cast
      rfl
  have hn3 : 3 ≤ P.n := by have := P.two_le; omega
  obtain ⟨k, hear, -, -⟩ := exists_ear P hP hn3 0
  set r := k + 1 with hr
  set R := P.rotateBy r with hR
  have hRn : R.n = P.n := rotateBy_n P r
  have hRs : R.IsSimple := P.isSimple_rotateBy hP r
  have hRear : R.IsEar R.n := by
    rw [hR, isEar_rotateBy, rotateBy_n, show P.n + r = k + (P.n + 1) by omega, isEar_add_period]
    exact hear
  have hRreg : R.region = P.region := by
    unfold region; rw [hR, carrier_rotateBy, parity_rotateBy]
  have hRw : ∀ j, ∃ j', P.w j' = R.w j := fun j => ⟨j + r, (w_rotateBy P r j).symm⟩
  have hPR : ∀ j, P.w j = R.w (j + P.n * r) := fun j => (w_rotateBy_back P r j).symm
  obtain ⟨M, hM⟩ := R.exists_eq_subdivideLast (by omega)
  set c := R.v (Fin.last R.n) with hc
  obtain ⟨e1, e2, e3⟩ := M.subdivideLast_w_ear c
  have hMR : R.n = M.n + 1 := by rw [hM]; rfl
  have hear' := hRear
  unfold IsEar at hear'
  rw [hM, e1, e2, e3] at hear'
  obtain ⟨hD, hT, hpar⟩ := hear'
  have hQs : (M.subdivideLast c).IsSimple := hM ▸ hRs
  have hMs : M.IsSimple := by
    refine isSimple_of_isSimple_subdivideLast M c hQs fun k hk z ⟨hzT, hzk⟩ => ?_
    have hz1 : z ∈ convexHull ℝ {M.v (Fin.last M.n), c, M.v 0} := by
      rwa [Set.pair_comm c (M.v 0)]
    have hz2 : z ∈ (M.subdivideLast c).carrier := by
      have := hzk
      rw [← M.subdivideLast_edge_castSucc c hk] at this
      exact (M.subdivideLast c).edge_subset_carrier _ this
    rcases mem_new_edges M c hQs hk hzk (hT ⟨hz1, hz2⟩) with h | h
    · rw [h]; exact Or.inl rfl
    · rw [h]; exact Or.inr rfl
  obtain ⟨KM, hKfin, hKcard, hKv, hKe, hKsp⟩ := ih M.n (by omega) M rfl hMs
  set a := M.v (Fin.last M.n) with ha
  set b := M.v 0 with hb
  have hRM : ∀ j, R.w j = (M.subdivideLast c).w j := fun j => by rw [hM]
  have hvM : ∀ j, ∃ j', P.w j' = M.w j := by
    intro j
    obtain ⟨j', hj'⟩ := hRw (j % (M.n + 1))
    exact ⟨j', by rw [hj', w_eq_subdivideLast_w M c j, hRM]⟩
  have hvR : ∀ x, (∃ j, R.w j = x) → ∃ j, P.w j = x := by
    rintro x ⟨j, rfl⟩; exact hRw j
  have hRa : R.w M.n = a := by
    rw [hRM, subdivideLast_w_of_le M c le_rfl, w_last_eq]
  have hRc : R.w (M.n + 1) = c := by rw [hRM]; exact e2
  have hRb : R.w (M.n + 1 + 1) = b := by rw [hRM]; exact e3
  -- the ear simplex
  set se : Finset R2 := {a, c, b} with hse
  have hind := affineIndependent_triangle hD
  set T := simplexComplex se hind with hTdef
  obtain ⟨hTfin, hTsub⟩ := hsimplex se hind
  have hab : ({a, b} : Finset R2) ∈ KM.faces := by
    have := hKe M.n
    rwa [w_last_eq, w_succ_last_eq] at this
  have hglue : ∀ s ∈ KM.faces, ∀ t ∈ T.faces,
      convexHull ℝ (s : Set R2) ∩ convexHull ℝ ↑t ⊆ convexHull ℝ (s ∩ t : Set R2) := by
    rintro s hs t ht z ⟨hzs, hzt⟩
    have hzR : z ∈ M.region := by
      rw [← hKsp, SimplicialComplex.mem_space_iff]; exact ⟨s, hs, hzs⟩
    have hzT : z ∈ convexHull ℝ {a, c, b} := by
      have := convexHull_mono (Finset.coe_subset.mpr (hTsub t ht)) hzt
      rwa [hse, Finset.coe_insert, Finset.coe_insert, Finset.coe_singleton] at this
    have hzc := ear_inter_region M c hQs hD hT hpar ⟨hzT, hzR⟩
    have hzab : z ∈ convexHull ℝ ((({a, b} : Finset R2)) : Set R2) := by
      rw [coe_pair_convexHull]; exact hzc
    have hz1 := KM.inter_subset_convexHull hs hab ⟨hzs, hzab⟩
    rw [← Finset.coe_inter] at hz1
    have hu : s ∩ {a, b} ⊆ se := fun x hx => by
      have := (Finset.mem_inter.mp hx).2
      simp only [Finset.mem_insert, Finset.mem_singleton] at this
      rcases this with rfl | rfl <;> simp [hse]
    have hz2 := (hind.convexHull_inter hu (hTsub t ht)).ge ⟨hz1, hzt⟩
    refine convexHull_mono ?_ hz2
    intro x hx
    exact ⟨(Finset.mem_inter.mp hx.1).1, hx.2⟩
  refine ⟨unionComplex KM T hglue, hKfin.union hTfin, ?_, ?_, ?_, ?_⟩
  · rintro s (hs | hs)
    · exact hKcard s hs
    · exact (Finset.card_le_card (hTsub s hs)).trans Finset.card_le_three
  · rintro s (hs | hs) x hx
    · obtain ⟨j, hj⟩ := hKv s hs x hx
      obtain ⟨j', hj'⟩ := hvM j
      exact ⟨j', hj'.trans hj⟩
    · have := hTsub s hs hx
      simp only [hse, Finset.mem_insert, Finset.mem_singleton] at this
      rcases this with rfl | rfl | rfl
      · exact hvR _ ⟨M.n, hRa⟩
      · exact hvR _ ⟨M.n + 1, hRc⟩
      · exact hvR _ ⟨M.n + 1 + 1, hRb⟩
  · intro j
    rw [hPR j, hPR (j + 1), show j + 1 + P.n * r = j + P.n * r + 1 by ring, ← R.w_mod (j + P.n * r),
      ← w_succ_mod R (j + P.n * r)]
    set i := (j + P.n * r) % (R.n + 1) with hi
    have hilt : i < M.n + 2 := by rw [hi, hMR]; exact Nat.mod_lt _ (by omega)
    by_cases hi1 : i < M.n
    · left
      rw [hRM, hRM, subdivideLast_w_of_le M c (by omega), subdivideLast_w_of_le M c (by omega)]
      exact hKe i
    right
    refine ⟨⟨R.w i, by simp⟩, fun x hx => ?_⟩
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    by_cases hi2 : i = M.n
    · rw [hi2] at hx
      rcases hx with rfl | rfl
      · rw [hRa]; simp [hse]
      · rw [hRc]; simp [hse]
    · have hi3 : i = M.n + 1 := by omega
      rw [hi3] at hx
      rcases hx with rfl | rfl
      · rw [hRc]; simp [hse]
      · rw [hRb]; simp [hse]
  · rw [unionComplex_space, hKsp, simplexComplex_space _ _ ⟨a, by simp [hse]⟩, ← hRreg, hM,
      region_subdivideLast M c hD hpar, hse]
    push_cast
    rfl

end Polygon

end QOU.MathlibExt.PL
