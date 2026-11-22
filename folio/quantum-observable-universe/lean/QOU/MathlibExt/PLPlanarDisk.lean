/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarEarRemoval

set_option autoImplicit false

/-!
# The region of a simple plane polygon is a union of triangles (issue #8902, part B)

The region of a plane polygon `P` is its carrier together with the points of crossing parity `1`
(`Polygon.parity`). Clipping an ear `a, c, b` (`Polygon.IsEar`) splits the region into the region
of the clipped polygon and the closed ear triangle. By the two-ears theorem the region of a simple
polygon is therefore a finite union of non-degenerate closed triangles with vertices among the
vertices of the polygon: the first, set-level half of the planar Schoenflies theorem.

## What is a DEFINITION here

* `Polygon.region P` — `P.carrier ∪ {y | P.parity y = 1}`.

## What is a THEOREM here

* `Polygon.parity_subdivideLast` — the parity of `M.subdivideLast c` is the parity of `M` plus the
  parity of the triangle `M.v last, c, M.v 0`.
* `parity_eq_of_mem_convexHull` — a polygon of constant parity on an open triangle has that parity
  at every point of the closed triangle off the polygon.
* `region_triPoly` — the region of a non-degenerate triangle is its convex hull.
* `Polygon.region_subdivideLast` — **clipping an ear**: the region of `M.subdivideLast c` is the
  region of `M` together with the closed ear triangle.
* `Polygon.region_eq_iUnion_triangles` — **the region of a simple plane polygon is a finite union
  of non-degenerate closed triangles whose vertices are vertices of the polygon.**

## What is NOT proved here

* That these triangles form a simplicial complex (they meet in common faces), i.e. that the region
  is a PL disk.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

namespace Polygon

/-- The closed region bounded by a plane polygon: its carrier and the points of parity `1`. -/
def region (P : Polygon R2) : Set R2 := P.carrier ∪ {y | P.parity y = 1}

lemma subdivideLast_w_of_le (M : Polygon R2) (c : R2) {k : ℕ} (hk : k ≤ M.n) :
    (M.subdivideLast c).w k = M.w k := by
  have h1 : (M.subdivideLast c).w (((⟨k, by omega⟩ : Fin (M.n + 1)).castSucc : Fin (M.n + 2)) : ℕ)
      = M.v ⟨k, by omega⟩ := by
    rw [w_coe]; exact M.subdivideLast_v_castSucc c _
  rw [show (((⟨k, by omega⟩ : Fin (M.n + 1)).castSucc : Fin (M.n + 2)) : ℕ) = k from rfl] at h1
  rw [h1, ← w_coe]

/-- **The parity of a subdivided polygon.** -/
theorem parity_subdivideLast (M : Polygon R2) (c y : R2) :
    (M.subdivideLast c).parity y =
      M.parity y + (triPoly (M.v (Fin.last M.n)) c (M.v 0)).parity y := by
  obtain ⟨e1, e2, e3⟩ := M.subdivideLast_w_ear c
  have hn : (M.subdivideLast c).n = M.n + 1 := rfl
  rw [hn] at e1 e2 e3
  rw [parity_eq_sum_range, parity_eq_sum_range, triPoly_parity, hn, Finset.sum_range_succ,
    Finset.sum_range_succ, Finset.sum_range_succ]
  have hs : ∀ k ∈ Finset.range M.n, crossInd ((M.subdivideLast c).w k)
      ((M.subdivideLast c).w (k + 1)) y = crossInd (M.w k) (M.w (k + 1)) y := by
    intro k hk
    have := Finset.mem_range.mp hk
    rw [subdivideLast_w_of_le M c (by omega), subdivideLast_w_of_le M c (by omega)]
  rw [Finset.sum_congr rfl hs, subdivideLast_w_of_le M c le_rfl,
    show M.n + 1 + 1 = M.n + 1 + 1 from rfl]
  have ha : M.w M.n = M.v (Fin.last M.n) := by rw [← w_coe]; rfl
  have hb : M.w (M.n + 1) = M.v 0 := by rw [w_period, ← w_coe]; rfl
  have e2' : (M.subdivideLast c).w (M.n + 1) = c := e2
  have e3' : (M.subdivideLast c).w (M.n + 1 + 1) = M.v 0 := e3
  rw [e2', e3', ha, hb]
  have hc : crossInd (M.v 0) (M.v (Fin.last M.n)) y + crossInd (M.v (Fin.last M.n)) (M.v 0) y
      = 0 := by
    rw [crossInd_swap]; exact CharTwo.add_self_eq_zero _
  have h2 : (2 : ZMod 2) = 0 := rfl
  linear_combination hc + (-crossInd (M.v (Fin.last M.n)) (M.v 0) y -
    crossInd (M.v 0) (M.v (Fin.last M.n)) y) * h2

end Polygon

/-- The centroid of a non-degenerate triangle is in its open triangle. -/
lemma centroid_mem_openTri {p q r : R2} (hD : cross p q r ≠ 0) :
    ((1 / 3 : ℝ) • p + (1 / 3 : ℝ) • q + (1 / 3 : ℝ) • r) ∈ openTri p q r := by
  have hD2 : 0 < cross p q r * cross p q r := mul_self_pos.mpr hD
  refine ⟨?_, ?_, ?_⟩
  · rw [cross_combo _ _ _ _ _ _ _ _ (by norm_num), cross_rot, cross_left, cross_right]
    nlinarith
  · rw [cross_combo _ _ _ _ _ _ _ _ (by norm_num), cross_right, cross_rot2, cross_left]
    nlinarith
  · rw [cross_combo _ _ _ _ _ _ _ _ (by norm_num), cross_left, cross_right]
    nlinarith

/-- **Parity extends from the open triangle to the closed one**, off the polygon. -/
theorem parity_eq_of_mem_convexHull (Q : Polygon R2) {p q r : R2} (hD : cross p q r ≠ 0)
    (e : ZMod 2) (hpar : ∀ z ∈ openTri p q r, Q.parity z = e) {y : R2}
    (hy : y ∈ convexHull ℝ {p, q, r}) (hyQ : y ∉ Q.carrier) : Q.parity y = e := by
  set m := (1 / 3 : ℝ) • p + (1 / 3 : ℝ) • q + (1 / 3 : ℝ) • r with hm
  have hmT := centroid_mem_openTri hD
  obtain ⟨h1, h2, h3⟩ := (mem_convexHull_triple_iff hD).mp hy
  obtain ⟨m1, m2, m3⟩ := hmT
  set f : ℝ → R2 := fun t => (1 - t) • y + t • m with hf
  have hcont : Continuous f := by
    rw [hf]; fun_prop
  have hf0 : f 0 = y := by simp [hf]
  have hlim : Tendsto f (𝓝[>] 0) (𝓝 y) := by
    rw [← hf0]; exact (hcont.tendsto 0).mono_left nhdsWithin_le_nhds
  have hev := hlim.eventually (Q.parity_eventually_eq hyQ)
  have hpos : ∀ᶠ t in 𝓝[>] (0 : ℝ), t ∈ Ioo (0 : ℝ) 1 :=
    Ioo_mem_nhdsGT (by norm_num : (0 : ℝ) < 1)
  obtain ⟨t, ht, ht0, ht1⟩ := (hev.and hpos).exists
  have hfT : f t ∈ openTri p q r := by
    have key : ∀ a b : R2, 0 ≤ cross a b y * cross p q r → 0 < cross a b m * cross p q r →
        0 < cross a b (f t) * cross p q r := by
      intro a b hya hma
      rw [hf]
      simp only
      rw [cross_lineMap a b y m (1 - t) t (by ring)]
      nlinarith
    exact ⟨key _ _ h1 m1, key _ _ h2 m2, key _ _ h3 m3⟩
  rw [← ht]; exact hpar _ hfT

theorem parity_eq_one_of_mem_convexHull (Q : Polygon R2) {p q r : R2} (hD : cross p q r ≠ 0)
    (hpar : ∀ z ∈ openTri p q r, Q.parity z = 1) {y : R2} (hy : y ∈ convexHull ℝ {p, q, r})
    (hyQ : y ∉ Q.carrier) : Q.parity y = 1 :=
  parity_eq_of_mem_convexHull Q hD 1 hpar hy hyQ

/-- **The region of a non-degenerate triangle is its convex hull.** -/
theorem region_triPoly {p q r : R2} (hD : cross p q r ≠ 0) :
    (triPoly p q r).region = convexHull ℝ {p, q, r} := by
  apply Subset.antisymm
  · rintro y (hy | hy)
    · rw [triPoly_carrier] at hy
      rcases hy with (hy | hy) | hy
      · exact segment_subset_convexHull (by simp) (by simp) hy
      · exact segment_subset_convexHull (by simp) (by simp) hy
      · exact segment_subset_convexHull (by simp) (by simp) hy
    · by_contra hn
      have h0 := (triPoly p q r).parity_eq_zero_of_not_mem_convexHull
        (by rwa [triPoly_range] : y ∉ convexHull ℝ (range (triPoly p q r).v))
      rw [mem_setOf_eq, h0] at hy
      exact zero_ne_one hy
  · intro y hy
    by_cases hc : y ∈ (triPoly p q r).carrier
    · exact Or.inl hc
    · exact Or.inr (triPoly_parity_eq_one hD hy hc)

namespace Polygon

/-- **Clipping an ear.** -/
theorem region_subdivideLast (M : Polygon R2) (c : R2)
    (hD : cross (M.v (Fin.last M.n)) c (M.v 0) ≠ 0)
    (hpar : ∀ y ∈ openTri (M.v (Fin.last M.n)) c (M.v 0), (M.subdivideLast c).parity y = 1) :
    (M.subdivideLast c).region =
      M.region ∪ convexHull ℝ {M.v (Fin.last M.n), c, M.v 0} := by
  set a := M.v (Fin.last M.n) with ha
  set b := M.v 0 with hb
  set P := M.subdivideLast c with hP
  set T := convexHull ℝ {a, c, b} with hTdef
  have hac : segment ℝ a c ⊆ T := segment_subset_convexHull (by simp) (by simp)
  have hcb : segment ℝ c b ⊆ T := segment_subset_convexHull (by simp) (by simp)
  have hab : segment ℝ a b ⊆ T := segment_subset_convexHull (by simp) (by simp)
  -- the parity splits
  have hsplit := parity_subdivideLast M c
  -- outside the ear the triangle contributes nothing
  have hout : ∀ y, y ∉ T → (triPoly a c b).parity y = 0 := fun y hy =>
    (triPoly a c b).parity_eq_zero_of_not_mem_convexHull (by rwa [triPoly_range])
  -- carriers
  have hPM : P.carrier ⊆ M.carrier ∪ T := by
    intro z hz
    rw [hP, carrier_subdivideLast] at hz
    rcases hz with (hz | hz) | hz
    · obtain ⟨k, hk⟩ := mem_iUnion.mp hz
      exact Or.inl (M.edge_subset_carrier _ hk)
    · exact Or.inr (hac hz)
    · exact Or.inr (hcb hz)
  have hMP : M.carrier ⊆ P.carrier ∪ T := fun z hz =>
    (M.carrier_subset_subdivideLast_union c hz).imp id (fun h => hab h)
  -- inside the ear, off the polygon, the parity is `1`
  have hin : ∀ y ∈ T, y ∉ P.carrier → P.parity y = 1 := fun y hy hyP =>
    parity_eq_one_of_mem_convexHull P hD hpar hy hyP
  apply Subset.antisymm
  · rintro y hy
    by_cases hyT : y ∈ T
    · exact Or.inr hyT
    refine Or.inl ?_
    rcases hy with hy | hy
    · exact Or.inl ((hPM hy).resolve_right hyT)
    · by_cases hyM : y ∈ M.carrier
      · exact Or.inl hyM
      · right
        have := hsplit y
        rw [hy, hout y hyT, add_zero] at this
        exact this.symm
  · rintro y (hy | hy)
    · by_cases hyT : y ∈ T
      · by_cases hyP : y ∈ P.carrier
        · exact Or.inl hyP
        · exact Or.inr (hin y hyT hyP)
      rcases hy with hy | hy
      · exact Or.inl ((hMP hy).resolve_right hyT)
      · right
        show P.parity y = 1
        rw [hsplit, hout y hyT, add_zero]
        exact hy
    · by_cases hyP : y ∈ P.carrier
      · exact Or.inl hyP
      · exact Or.inr (hin y hy hyP)

/-- A polygon with three vertices has the region of its triangle. -/
lemma region_eq_triPoly (Q : Polygon R2) (h2 : Q.n = 2) :
    Q.region = (triPoly (Q.w 0) (Q.w 1) (Q.w 2)).region := by
  obtain ⟨n, hn, v⟩ := Q
  simp only at h2
  subst h2
  have : (⟨2, hn, v⟩ : Polygon R2) = triPoly (v 0) (v 1) (v 2) := by
    unfold triPoly
    congr 1
    funext i
    fin_cases i <;> rfl
  rw [this]
  rfl

lemma w_eq_subdivideLast_w (M : Polygon R2) (c : R2) (j : ℕ) :
    M.w j = (M.subdivideLast c).w (j % (M.n + 1)) := by
  rw [subdivideLast_w_of_le M c (Nat.le_of_lt_succ (Nat.mod_lt _ (Nat.succ_pos _))), w_mod]

/-- **The region of a simple plane polygon is a finite union of non-degenerate closed triangles
whose vertices are vertices of the polygon.** -/
theorem region_eq_iUnion_triangles (P : Polygon R2) (hP : P.IsSimple) :
    ∃ ts : List (R2 × R2 × R2), (∀ t ∈ ts, cross t.1 t.2.1 t.2.2 ≠ 0 ∧
      (∃ j, P.w j = t.1) ∧ (∃ j, P.w j = t.2.1) ∧ (∃ j, P.w j = t.2.2)) ∧
      P.region = ⋃ t ∈ ts, convexHull ℝ {t.1, t.2.1, t.2.2} := by
  suffices H : ∀ N, ∀ P : Polygon R2, P.n = N → P.IsSimple →
      ∃ ts : List (R2 × R2 × R2), (∀ t ∈ ts, cross t.1 t.2.1 t.2.2 ≠ 0 ∧
        (∃ j, P.w j = t.1) ∧ (∃ j, P.w j = t.2.1) ∧ (∃ j, P.w j = t.2.2)) ∧
        P.region = ⋃ t ∈ ts, convexHull ℝ {t.1, t.2.1, t.2.2} from H _ P rfl hP
  intro N
  induction N using Nat.strong_induction_on with
  | _ N ih =>
  intro P hN hP
  by_cases h2 : P.n = 2
  · have hD := cross_ne_zero_of_isSimple hP h2
    refine ⟨[(P.w 0, P.w 1, P.w 2)], ?_, ?_⟩
    · intro t ht
      rw [List.mem_singleton] at ht
      subst ht
      exact ⟨hD, ⟨0, rfl⟩, ⟨1, rfl⟩, ⟨2, rfl⟩⟩
    · rw [region_eq_triPoly P h2, region_triPoly hD]
      simp
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
  obtain ⟨ts, hts, hreg⟩ := ih M.n (by omega) M rfl hMs
  -- vertices of `M` and of the ear are vertices of `P`
  have hvM : ∀ j, ∃ j', P.w j' = M.w j := by
    intro j
    obtain ⟨j', hj'⟩ := hRw (j % (M.n + 1))
    exact ⟨j', by rw [hj', w_eq_subdivideLast_w M c j, hM]⟩
  have hvR : ∀ x, (∃ j, R.w j = x) → ∃ j, P.w j = x := by
    rintro x ⟨j, rfl⟩; exact hRw j
  have hRM : ∀ j, R.w j = (M.subdivideLast c).w j := fun j => by rw [hM]
  refine ⟨(M.v (Fin.last M.n), c, M.v 0) :: ts, ?_, ?_⟩
  · intro t ht
    rcases List.mem_cons.mp ht with rfl | ht
    · refine ⟨hD, hvR _ ⟨R.n + R.n, ?_⟩, hvR _ ⟨R.n, ?_⟩, hvR _ ⟨R.n + 1, ?_⟩⟩
      · rw [hRM, hMR]; exact e1
      · rw [hRM, hMR]; exact e2
      · rw [hRM, hMR]; exact e3
    · obtain ⟨hD', ⟨j1, h1⟩, ⟨j2, h2⟩, ⟨j3, h3⟩⟩ := hts t ht
      obtain ⟨i1, g1⟩ := hvM j1
      obtain ⟨i2, g2⟩ := hvM j2
      obtain ⟨i3, g3⟩ := hvM j3
      exact ⟨hD', ⟨i1, g1.trans h1⟩, ⟨i2, g2.trans h2⟩, ⟨i3, g3.trans h3⟩⟩
  · rw [← hRreg, hM, region_subdivideLast M c hD hpar, hreg]
    simp only [List.mem_cons, iUnion_iUnion_eq_or_left]
    exact union_comm _ _

end Polygon

end QOU.MathlibExt.PL
