/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarCorner

set_option autoImplicit false

/-!
# The corner at the lowest-leftmost vertex (issue #8902, Moise part B, step 1)

At the lowest-leftmost vertex `v` of a simple polygon, with neighbours `a` and `b`, the corner
`a v b` is non-degenerate. Either no other vertex lies in the triangle `a v b`, or the vertex
`z` in it nearest to `v` (largest barycentric weight of `v`) gives an interior chord `[v, z]`.

## What is a THEOREM here

* `cross_ne_zero_of_lex` — the corner at a lowest-leftmost vertex is non-degenerate.
* `exit_triangle` — moving along a segment in the direction that raises the weight of `v`,
  one leaves the triangle through the side opposite... or reaches the segment's end.
* `edge_weight_le` — an edge away from `v` meets the triangle only where the weight of `v` is at
  most that of some vertex in the triangle (or `0`).
-/

namespace QOU.MathlibExt.PL

open Set Polygon

/-- Two lexicographically-positive directions from `v` that are parallel: one point lies on the
segment to the other. -/
lemma mem_segment_of_lex_parallel {v a b : R2} (ha : LexLt v a) (hb : LexLt v b)
    (hc : cross a v b = 0) : b ∈ segment ℝ v a ∨ a ∈ segment ℝ v b := by
  have hc1 : cross v a b = 0 := by rw [cross_swap]; simp [hc]
  have hc2 : cross v b a = 0 := by rw [cross_rot]; exact hc
  have hb0 : v 0 ≤ b 0 := by rcases hb with h | h <;> [linarith; linarith [h.1]]
  rcases ha with ha | ⟨ha0, ha1⟩
  · rcases le_or_gt (b 0) (a 0) with h | h
    · exact Or.inl (mem_segment_of_cross_eq_zero ha.ne (Or.inl ⟨hb0, h⟩) hc1)
    · exact Or.inr (mem_segment_of_cross_eq_zero (by linarith) (Or.inl ⟨ha.le, h.le⟩) hc2)
  · have hb0' : b 0 = v 0 := by
      unfold cross at hc
      rw [ha0] at hc
      have : (v 1 - a 1) * (b 0 - a 0) = 0 := by linarith
      rcases mul_eq_zero.mp this with h | h
      · linarith
      · linarith
    have hb1 : v 1 < b 1 := by
      rcases hb with h | h
      · linarith
      · exact h.2
    rcases le_or_gt (b 1) (a 1) with h | h
    · exact Or.inl (segment_vertical hb0'.symm (by rw [← ha0, hb0']) hb1.le h)
    · exact Or.inr (segment_vertical ha0 (by rw [hb0', ha0]) ha1.le h.le)

/-- **The corner at a lowest-leftmost vertex is non-degenerate.** -/
theorem cross_ne_zero_of_lex {P : Polygon R2} (hP : P.IsSimple) (ha : LexLt (P.w 0) (P.w P.n))
    (hb : LexLt (P.w 0) (P.w 1)) : cross (P.w P.n) (P.w 0) (P.w 1) ≠ 0 := by
  have h2 := P.two_le
  intro hc
  rcases mem_segment_of_lex_parallel ha hb hc with h | h
  · have hm : P.w 1 ∈ P.seg P.n := by unfold seg; rw [P.w_period, segment_symm]; exact h
    rcases hP.w_mem_seg (j := 1) (by omega) le_rfl hm with h | h
    · omega
    · rw [Nat.mod_self] at h; omega
  · have hm : P.w P.n ∈ P.seg 0 := h
    rcases hP.w_mem_seg le_rfl (Nat.zero_le _) hm with h | h
    · omega
    · rw [Nat.mod_eq_of_lt (by omega)] at h; omega

/-- **Leaving the triangle along a segment.** Moving from `y` towards `q`, where the weight of
`v` does not decrease, one stays in the triangle `a v b` up to a point that is `q` itself or lies
on one of the two sides at `v`, with the weight of `v` still above `c`. -/
lemma exit_triangle {a v b p q y : R2} (hD : cross a v b ≠ 0) (hy : y ∈ segment ℝ p q)
    (hyT : y ∈ convexHull ℝ {a, v, b})
    (hmono : cross b a p * cross a v b ≤ cross b a q * cross a v b) {c : ℝ}
    (hc : c < cross b a y * cross a v b) :
    ∃ y' ∈ segment ℝ p q, y' ∈ convexHull ℝ {a, v, b} ∧ c < cross b a y' * cross a v b ∧
      (y' = q ∨ cross v b y' = 0 ∨ cross a v y' = 0) := by
  obtain ⟨s, t₀, hs, ht₀, hst, rfl⟩ := hy
  obtain rfl : s = 1 - t₀ := by linarith
  have e : ∀ (X Y : R2) (t : ℝ), cross X Y ((1 - t) • p + t • q) * cross a v b =
      (1 - t) * (cross X Y p * cross a v b) + t * (cross X Y q * cross a v b) := by
    intro X Y t; rw [cross_lineMap X Y p q (1 - t) t (by ring)]; ring
  obtain ⟨h1, h2, h3⟩ := (mem_convexHull_triple_iff hD).mp hyT
  rw [e] at h1 h2 h3 hc
  let u : Fin 3 → ℝ :=
    ![cross v b p * cross a v b, cross b a p * cross a v b, cross a v p * cross a v b]
  let w : Fin 3 → ℝ :=
    ![cross v b q * cross a v b, cross b a q * cross a v b, cross a v q * cross a v b]
  have hh : ∀ i, 0 ≤ (1 - t₀) * u i + t₀ * w i := by
    intro i; fin_cases i
    · exact h1
    · exact h2
    · exact h3
  obtain ⟨t, htt, ht1, hall, hend, -⟩ := exit_right u w ht₀ (by linarith) hh
  refine ⟨(1 - t) • p + t • q, ⟨1 - t, t, by linarith, by linarith, by ring, rfl⟩, ?_, ?_, ?_⟩
  · refine (mem_convexHull_triple_iff hD).mpr ⟨?_, ?_, ?_⟩
    · rw [e]; exact hall 0
    · rw [e]; exact hall 1
    · rw [e]; exact hall 2
  · rw [e]
    nlinarith [mul_nonneg (sub_nonneg.mpr htt) (sub_nonneg.mpr hmono)]
  · rcases hend with rfl | ⟨i, hi, hz⟩
    · left; simp
    · fin_cases i
      · right; left
        have hz' : cross v b ((1 - t) • p + t • q) * cross a v b = 0 := by rw [e]; exact hz
        exact (mul_eq_zero.mp hz').resolve_right hD
      · exact absurd hi (not_lt.mpr hmono)
      · right; right
        have hz' : cross a v ((1 - t) • p + t • q) * cross a v b = 0 := by rw [e]; exact hz
        exact (mul_eq_zero.mp hz').resolve_right hD

/-- **An edge away from `v` stays low in the triangle.** If every vertex of `P` other than
`a, v, b` that lies in the triangle `a v b` has `v`-weight at most `c ≥ 0`, so does every point
of an edge not incident to `v` that lies in the triangle. -/
theorem edge_weight_le {P : Polygon R2} (hP : P.IsSimple) (hn : 3 ≤ P.n)
    (hD : cross (P.w P.n) (P.w 0) (P.w 1) ≠ 0) {c : ℝ} (hc0 : 0 ≤ c)
    (hin : ∀ j, 2 ≤ j → j ≤ P.n - 1 → P.w j ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1} →
      cross (P.w 1) (P.w P.n) (P.w j) * cross (P.w P.n) (P.w 0) (P.w 1) ≤ c)
    {k : ℕ} (hk1 : 1 ≤ k) (hk2 : k ≤ P.n - 1) {y : R2} (hy : y ∈ P.seg k)
    (hyT : y ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1}) :
    cross (P.w 1) (P.w P.n) y * cross (P.w P.n) (P.w 0) (P.w 1) ≤ c := by
  by_contra hlt
  push_neg at hlt
  -- a vertex of the edge in the triangle cannot have weight above `c`
  have hvert : ∀ m, (m = k ∨ m = k + 1) → P.w m ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1} →
      c < cross (P.w 1) (P.w P.n) (P.w m) * cross (P.w P.n) (P.w 0) (P.w 1) → False := by
    intro m hm hT hc
    by_cases h1 : m = 1
    · subst h1; rw [cross_left, zero_mul] at hc; linarith
    by_cases h2 : m = P.n
    · subst h2; rw [cross_right, zero_mul] at hc; linarith
    exact absurd (hin m (by omega) (by omega) hT) (not_le.mpr hc)
  have hside : ∀ y', y' ∈ P.seg k → y' ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1} →
      c < cross (P.w 1) (P.w P.n) y' * cross (P.w P.n) (P.w 0) (P.w 1) →
      (y' = P.w k ∨ y' = P.w (k + 1) ∨ cross (P.w 0) (P.w 1) y' = 0 ∨
        cross (P.w P.n) (P.w 0) y' = 0) → False := by
    intro y' hy' hT hc hcase
    rcases hcase with h | h | h | h
    · exact hvert k (Or.inl rfl) (h ▸ hT) (h ▸ hc)
    · exact hvert (k + 1) (Or.inr rfl) (h ▸ hT) (h ▸ hc)
    · have hD' : cross (P.w 0) (P.w 1) (P.w P.n) ≠ 0 := by rw [cross_rot]; exact hD
      have hT' : y' ∈ convexHull ℝ {P.w 0, P.w 1, P.w P.n} := by rwa [triple_rot]
      have h0 : y' ∈ P.seg 0 := mem_segment_of_mem_convexHull_of_cross hD' hT' h
      have hin2 : y' ∈ P.seg k ∩ P.seg 0 := ⟨hy', h0⟩
      rw [hP.seg_inter (by omega) (by omega) (by omega)] at hin2
      split_ifs at hin2 with c1 c2
      · rw [Nat.mod_eq_of_lt (by omega)] at c1; omega
      · rw [hin2] at hT hc; exact hvert k (Or.inl rfl) hT hc
      · exact hin2
    · have hn' : y' ∈ P.seg P.n := by
        have := mem_segment_of_mem_convexHull_of_cross hD hT h
        unfold seg; rwa [P.w_period]
      have hin2 : y' ∈ P.seg k ∩ P.seg P.n := ⟨hy', hn'⟩
      rw [hP.seg_inter (by omega) le_rfl (by omega)] at hin2
      split_ifs at hin2 with c1 c2
      · rw [Nat.mod_eq_of_lt (by omega)] at c1
        rw [hin2] at hT hc; exact hvert (k + 1) (Or.inr rfl) (c1 ▸ hT) (c1 ▸ hc)
      · rw [Nat.mod_self] at c2; omega
      · exact hin2
  rcases le_total (cross (P.w 1) (P.w P.n) (P.w k) * cross (P.w P.n) (P.w 0) (P.w 1))
    (cross (P.w 1) (P.w P.n) (P.w (k + 1)) * cross (P.w P.n) (P.w 0) (P.w 1)) with hm | hm
  · obtain ⟨y', hy', hT, hc, hcase⟩ := exit_triangle hD hy hyT hm hlt
    exact hside y' hy' hT hc (by tauto)
  · have hy2 : y ∈ segment ℝ (P.w (k + 1)) (P.w k) := by rw [segment_symm]; exact hy
    obtain ⟨y', hy', hT, hc, hcase⟩ := exit_triangle hD hy2 hyT hm hlt
    rw [segment_symm] at hy'
    exact hside y' hy' hT hc (by tauto)

/-- **A point strictly inside the angle at `v`** (positive weights of `a` and `b`): neither
neighbour lies in the closed cone spanned by the other neighbour and the point. -/
lemma cone_facts {a v b z : R2} (hD : cross a v b ≠ 0) (hMa : 0 < cross v b z * cross a v b)
    (hMb : 0 < cross a v z * cross a v b) :
    (∀ s t : ℝ, 0 ≤ s → 0 ≤ t → a - v ≠ s • (b - v) + t • (z - v)) ∧
    (∀ s t : ℝ, 0 ≤ s → 0 ≤ t → b - v ≠ s • (z - v) + t • (a - v)) ∧
    cross v b z ≠ 0 ∧ cross v z a ≠ 0 := by
  have hD2 : 0 < cross a v b * cross a v b := mul_self_pos.mpr hD
  refine ⟨fun s t hs ht h => ?_, fun s t hs ht h => ?_, fun h => ?_, fun h => ?_⟩
  · have E0 := congrFun h 0
    have E1 := congrFun h 1
    simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul] at E0 E1
    have c1 : cross a v b = t * cross v b z := by
      unfold cross; linear_combination (b 0 - v 0) * E1 - (b 1 - v 1) * E0
    have c2 : 0 = s * cross a v b + t * cross a v z := by
      unfold cross; linear_combination (a 1 - v 1) * E0 - (a 0 - v 0) * E1
    have k1 : cross a v b * cross a v b = t * (cross v b z * cross a v b) := by rw [c1]; ring
    have k2 : 0 = s * (cross a v b * cross a v b) + t * (cross a v z * cross a v b) := by
      linear_combination (cross a v b) * c2
    have ht0 : t * (cross a v z * cross a v b) = 0 := by nlinarith [mul_nonneg hs hD2.le]
    have : t = 0 := by
      rcases mul_eq_zero.mp ht0 with h | h
      · exact h
      · linarith
    rw [this, zero_mul] at k1; linarith
  · have E0 := congrFun h 0
    have E1 := congrFun h 1
    simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul] at E0 E1
    have c1 : cross a v b = s * cross a v z := by
      unfold cross; linear_combination (v 0 - a 0) * E1 - (v 1 - a 1) * E0
    have c2 : 0 = s * cross v b z + t * cross a v b := by
      unfold cross; linear_combination (b 0 - v 0) * E1 - (b 1 - v 1) * E0
    have k1 : cross a v b * cross a v b = s * (cross a v z * cross a v b) := by rw [c1]; ring
    have k2 : 0 = s * (cross v b z * cross a v b) + t * (cross a v b * cross a v b) := by
      linear_combination (cross a v b) * c2
    have hs0 : s * (cross v b z * cross a v b) = 0 := by nlinarith [mul_nonneg ht hD2.le]
    have : s = 0 := by
      rcases mul_eq_zero.mp hs0 with h | h
      · exact h
      · linarith
    rw [this, zero_mul] at k1; linarith
  · rw [h, zero_mul] at hMa; exact lt_irrefl _ hMa
  · rw [cross_rot] at h; rw [h, zero_mul] at hMb; exact lt_irrefl _ hMb

/-- **The deepest inner vertex gives an interior chord.** If some vertex other than the three
corner vertices lies in the triangle `w n, w 0, w 1`, take the one with the largest weight of
`w 0`. The segment from `w 0` to it meets `P` only at its ends, and it lies strictly inside the
angle at `w 0`. -/
theorem exists_chord {P : Polygon R2} (hP : P.IsSimple) (hn : 3 ≤ P.n)
    (hD : cross (P.w P.n) (P.w 0) (P.w 1) ≠ 0)
    (hz : ∃ j, 2 ≤ j ∧ j ≤ P.n - 1 ∧ P.w j ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1}) :
    ∃ β, 2 ≤ β ∧ β ≤ P.n - 1 ∧
      segment ℝ (P.w 0) (P.w β) ∩ P.carrier ⊆ {P.w 0, P.w β} ∧
      cross (P.w 0) (P.w 1) (P.w β) ≠ 0 ∧
      (∀ s t : ℝ, 0 ≤ s → 0 ≤ t →
        P.w P.n - P.w 0 ≠ s • (P.w 1 - P.w 0) + t • (P.w β - P.w 0)) ∧
      cross (P.w 0) (P.w β) (P.w P.n) ≠ 0 ∧
      (∀ s t : ℝ, 0 ≤ s → 0 ≤ t →
        P.w 1 - P.w 0 ≠ s • (P.w β - P.w 0) + t • (P.w P.n - P.w 0)) := by
  classical
  have hD2 : 0 < cross (P.w P.n) (P.w 0) (P.w 1) * cross (P.w P.n) (P.w 0) (P.w 1) :=
    mul_self_pos.mpr hD
  let S := (Finset.Icc 2 (P.n - 1)).filter
    (fun j => P.w j ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1})
  obtain ⟨j0, hj0a, hj0b, hj0T⟩ := hz
  have hSne : S.Nonempty := ⟨j0, by simp [S, hj0a, hj0b, hj0T]⟩
  obtain ⟨β, hβS, hmax⟩ := Finset.exists_max_image S
    (fun j => cross (P.w 1) (P.w P.n) (P.w j) * cross (P.w P.n) (P.w 0) (P.w 1)) hSne
  simp only [S, Finset.mem_filter, Finset.mem_Icc] at hβS
  obtain ⟨⟨hβ2, hβn⟩, hzT⟩ := hβS
  obtain ⟨hza, hzv, hzb⟩ := (mem_convexHull_triple_iff hD).mp hzT
  -- the weights of `w n` and `w 1` at the chosen vertex are positive
  have hMa : 0 < cross (P.w 0) (P.w 1) (P.w β) * cross (P.w P.n) (P.w 0) (P.w 1) := by
    rcases hza.lt_or_eq with h | h
    · exact h
    exfalso
    have h0 : cross (P.w 0) (P.w 1) (P.w β) = 0 := (mul_eq_zero.mp h.symm).resolve_right hD
    have hD' : cross (P.w 0) (P.w 1) (P.w P.n) ≠ 0 := by rw [cross_rot]; exact hD
    have hT' : P.w β ∈ convexHull ℝ {P.w 0, P.w 1, P.w P.n} := by rwa [triple_rot]
    have hm : P.w β ∈ P.seg 0 := mem_segment_of_mem_convexHull_of_cross hD' hT' h0
    rcases hP.w_mem_seg (by omega) (Nat.zero_le _) hm with h | h
    · omega
    · rw [Nat.mod_eq_of_lt (by omega)] at h; omega
  have hMb : 0 < cross (P.w P.n) (P.w 0) (P.w β) * cross (P.w P.n) (P.w 0) (P.w 1) := by
    rcases hzb.lt_or_eq with h | h
    · exact h
    exfalso
    have h0 : cross (P.w P.n) (P.w 0) (P.w β) = 0 := (mul_eq_zero.mp h.symm).resolve_right hD
    have hm : P.w β ∈ P.seg P.n := by
      have := mem_segment_of_mem_convexHull_of_cross hD hzT h0
      unfold seg; rwa [P.w_period]
    rcases hP.w_mem_seg (by omega) le_rfl hm with h | h
    · omega
    · rw [Nat.mod_self] at h; omega
  obtain ⟨hA, hB, hD1, hD3⟩ := cone_facts hD hMa hMb
  refine ⟨β, hβ2, hβn, ?_, hD1, hA, hD3, hB⟩
  -- the chord meets `P` only at its ends
  rintro y ⟨⟨s, t, hs, ht, hst, rfl⟩, hycar⟩
  by_contra hy
  simp only [mem_insert_iff, mem_singleton_iff, not_or] at hy
  obtain ⟨hy0, hyβ⟩ := hy
  have hs0 : 0 < s := by
    rcases hs.lt_or_eq with h | h
    · exact h
    · exfalso; apply hyβ; rw [← h, show t = 1 by linarith]; simp
  have ht0 : 0 < t := by
    rcases ht.lt_or_eq with h | h
    · exact h
    · exfalso; apply hy0; rw [← h, show s = 1 by linarith]; simp
  have lin : ∀ X Y : R2, cross X Y (s • P.w 0 + t • P.w β) =
      s * cross X Y (P.w 0) + t * cross X Y (P.w β) :=
    fun X Y => cross_lineMap X Y _ _ s t hst
  rw [carrier_eq_biUnion] at hycar
  simp only [mem_iUnion, Finset.mem_range] at hycar
  obtain ⟨k, hk, hyk⟩ := hycar
  have hseg0 : ∀ {p q x : R2}, x ∈ segment ℝ p q → cross p q x = 0 := by
    rintro p q x ⟨s', t', -, -, hst', rfl⟩
    rw [cross_lineMap p q p q s' t' hst', cross_left, cross_right]; ring
  by_cases hk0 : k = 0
  · subst hk0
    have hyk' : s • P.w 0 + t • P.w β ∈ segment ℝ (P.w 0) (P.w 1) := hyk
    have h0 := hseg0 hyk'
    rw [lin, cross_left, mul_zero, zero_add] at h0
    rw [(mul_eq_zero.mp h0).resolve_left ht0.ne', zero_mul] at hMa
    exact lt_irrefl _ hMa
  by_cases hkn : k = P.n
  · subst hkn
    have hyk' : s • P.w 0 + t • P.w β ∈ segment ℝ (P.w P.n) (P.w 0) := by
      have := hyk; unfold seg at this; rwa [P.w_period] at this
    have h0 := hseg0 hyk'
    rw [lin, cross_right, mul_zero, zero_add] at h0
    rw [(mul_eq_zero.mp h0).resolve_left ht0.ne', zero_mul] at hMb
    exact lt_irrefl _ hMb
  -- an edge away from `w 0`: compare weights of `w 0`
  have hvT : P.w 0 ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1} :=
    subset_convexHull ℝ _ (by simp)
  have hyT : s • P.w 0 + t • P.w β ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1} :=
    (convex_convexHull ℝ _) hvT hzT hs ht hst
  have hle := edge_weight_le hP hn hD hzv (fun j hj2 hjn hjT => hmax j (by
      simp only [S, Finset.mem_filter, Finset.mem_Icc]; exact ⟨⟨hj2, hjn⟩, hjT⟩))
    (k := k) (by omega) (by omega) hyk hyT
  rw [lin, cross_rot2] at hle
  have hsum := cross_cyclic_sum (P.w P.n) (P.w 0) (P.w 1) (P.w β)
  have hsumD : cross (P.w 0) (P.w 1) (P.w β) * cross (P.w P.n) (P.w 0) (P.w 1) +
      cross (P.w 1) (P.w P.n) (P.w β) * cross (P.w P.n) (P.w 0) (P.w 1) +
      cross (P.w P.n) (P.w 0) (P.w β) * cross (P.w P.n) (P.w 0) (P.w 1) =
      cross (P.w P.n) (P.w 0) (P.w 1) * cross (P.w P.n) (P.w 0) (P.w 1) := by
    rw [← hsum]; ring
  have ht1 : t = 1 - s := by linarith
  subst ht1
  nlinarith [mul_pos hs0 (show 0 < cross (P.w P.n) (P.w 0) (P.w 1) * cross (P.w P.n) (P.w 0) (P.w 1)
    - cross (P.w 1) (P.w P.n) (P.w β) * cross (P.w P.n) (P.w 0) (P.w 1) by linarith)]

end QOU.MathlibExt.PL
