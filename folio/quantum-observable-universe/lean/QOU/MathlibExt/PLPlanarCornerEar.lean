/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarLexCorner

set_option autoImplicit false

/-!
# An empty corner at the lowest-leftmost vertex is an ear (issue #8902, Moise part B, step 1)

At the lowest-leftmost vertex `v = w 0` of a simple polygon with `n ≥ 3`, with neighbours
`a = w n` and `b = w 1`: if no other vertex lies in the closed triangle `a v b`, then the corner
at `v` is an ear.

## What is a THEOREM here

* `corner_inter_of_empty` — the closed triangle meets the polygon only in its two sides at `v`.
* `isEar_of_empty_corner` — the corner is an ear (`P.IsEar 0`).
-/

namespace QOU.MathlibExt.PL

open Set Polygon Filter Topology

lemma cross_eq_zero_of_mem_segment {p q x : R2} (hx : x ∈ segment ℝ p q) : cross p q x = 0 := by
  obtain ⟨s, t, -, -, hst, rfl⟩ := hx
  rw [cross_lineMap p q p q s t hst, cross_left, cross_right]; ring

/-- Two points with the same barycentric weights (with respect to a non-degenerate triangle)
are equal. -/
lemma eq_of_cross_eq {a v b x x' : R2} (hD : cross a v b ≠ 0)
    (h1 : cross b a x = cross b a x') (h2 : cross a v x = cross a v x') : x = x' := by
  have e : cross v b x = cross v b x' := by
    linarith [cross_cyclic_sum a v b x, cross_cyclic_sum a v b x']
  calc x = _ := bary_eq hD
    _ = _ := by rw [e, h1, h2]
    _ = x' := (bary_eq hD).symm

/-- On the line `a b` (weight of `v` zero), the `b`-weight orders points along a segment. -/
lemma mem_segment_of_line {a v b p q u : R2} (hD : cross a v b ≠ 0) (hp : cross b a p = 0)
    (hq : cross b a q = 0) (hu : cross b a u = 0)
    (h1 : cross a v p * cross a v b ≤ cross a v u * cross a v b)
    (h2 : cross a v u * cross a v b ≤ cross a v q * cross a v b) : u ∈ segment ℝ p q := by
  rcases h1.lt_or_eq with h1 | h1
  · have hpq : cross a v p * cross a v b < cross a v q * cross a v b := h1.trans_le h2
    set lam := (cross a v u * cross a v b - cross a v p * cross a v b) /
      (cross a v q * cross a v b - cross a v p * cross a v b) with hlam
    have hden : 0 < cross a v q * cross a v b - cross a v p * cross a v b := by linarith
    have hl0 : 0 ≤ lam := div_nonneg (by linarith) hden.le
    have hl1 : lam ≤ 1 := (div_le_one hden).mpr (by linarith)
    refine ⟨1 - lam, lam, by linarith, hl0, by ring, ?_⟩
    refine eq_of_cross_eq hD ?_ ?_
    · rw [cross_lineMap _ _ _ _ _ _ (by ring), hp, hq, hu]; ring
    · rw [cross_lineMap _ _ _ _ _ _ (by ring)]
      refine mul_right_cancel₀ hD ?_
      have : lam * (cross a v q * cross a v b - cross a v p * cross a v b) =
          cross a v u * cross a v b - cross a v p * cross a v b := by
        rw [hlam, div_mul_cancel₀ _ hden.ne']
      linear_combination this
  · have : u = p := eq_of_cross_eq hD (by rw [hu, hp]) (mul_right_cancel₀ hD h1.symm)
    rw [this]; exact left_mem_segment ℝ p q

lemma exists_small {A₁ A₂ B₁ B₂ : ℝ} (h₁ : 0 < A₁) (h₂ : 0 < A₂) :
    ∃ ε : ℝ, 0 < ε ∧ ε ≤ 1 ∧ 0 < (1 - ε) * A₁ + ε * B₁ ∧ 0 < (1 - ε) * A₂ + ε * B₂ := by
  set M := A₁ + A₂ + |B₁| + |B₂| with hM
  have hM0 : 0 < M := by positivity
  set m := min A₁ A₂
  have hm0 : 0 < m := lt_min h₁ h₂
  have hm1 : m ≤ A₁ := min_le_left _ _
  have hm2 : m ≤ A₂ := min_le_right _ _
  set ε := m / (2 * M) with hε
  have hε0 : 0 < ε := by positivity
  have hεM : ε * M = m / 2 := by rw [hε]; field_simp
  have hb1 := neg_abs_le B₁
  have hb2 := neg_abs_le B₂
  have ha1 := abs_nonneg B₁
  have ha2 := abs_nonneg B₂
  refine ⟨ε, hε0, ?_, ?_, ?_⟩
  · nlinarith
  · nlinarith [mul_le_mul_of_nonneg_left hb1 hε0.le]
  · nlinarith [mul_le_mul_of_nonneg_left hb2 hε0.le]

/-- **The local picture on one edge.** For a non-degenerate triangle `a v b` and an edge
`[p, q]`: suppose points of the edge in the triangle have `v`-weight at most `0`, an endpoint in
the triangle is `b` (for `p`) or `a` (for `q`), and the edge does not contain both `a` and `b`.
Then the edge meets the triangle only in its sides at `v`. -/
lemma edge_corner {a v b p q : R2} (hD : cross a v b ≠ 0)
    (hbound : ∀ y ∈ segment ℝ p q, y ∈ convexHull ℝ {a, v, b} →
      cross b a y * cross a v b ≤ 0)
    (hpT : p ∈ convexHull ℝ {a, v, b} → p = b) (hqT : q ∈ convexHull ℝ {a, v, b} → q = a)
    (hab : ¬ (a ∈ segment ℝ p q ∧ b ∈ segment ℝ p q)) {y : R2} (hy : y ∈ segment ℝ p q)
    (hyT : y ∈ convexHull ℝ {a, v, b}) : y ∈ segment ℝ a v ∪ segment ℝ v b := by
  obtain ⟨h1, h2, h3⟩ := (mem_convexHull_triple_iff hD).mp hyT
  have hle := hbound y hy hyT
  have hv0 : cross b a y * cross a v b = 0 := le_antisymm hle h2
  rcases h3.lt_or_eq with hB | hB
  swap
  · left
    exact mem_segment_of_mem_convexHull_of_cross hD hyT
      ((mul_eq_zero.mp hB.symm).resolve_right hD)
  rcases h1.lt_or_eq with hA | hA
  swap
  · right
    have hD' : cross v b a ≠ 0 := by rw [cross_rot]; exact hD
    have hT' : y ∈ convexHull ℝ {v, b, a} := by rwa [triple_rot]
    exact mem_segment_of_mem_convexHull_of_cross hD' hT' ((mul_eq_zero.mp hA.symm).resolve_right hD)
  exfalso
  have hsum : ∀ x, cross v b x * cross a v b + cross b a x * cross a v b +
      cross a v x * cross a v b = cross a v b * cross a v b := by
    intro x; rw [← add_mul, ← add_mul, cross_cyclic_sum]
  obtain ⟨s, t, hs, ht, hst, hyst⟩ := hy
  have lin : ∀ X Y : R2, cross X Y y * cross a v b =
      s * (cross X Y p * cross a v b) + t * (cross X Y q * cross a v b) := by
    intro X Y; rw [← hyst, cross_lineMap X Y p q s t hst]; ring
  have hy' : y ∈ segment ℝ p q := ⟨s, t, hs, ht, hst, hyst⟩
  -- raising the weight of `v` along the edge is impossible
  have raise : ∀ r ∈ segment ℝ p q, 0 < cross b a r * cross a v b → False := by
    intro r hr hrv
    obtain ⟨ε, hε, hε1, ha, hb⟩ := exists_small (B₁ := cross v b r * cross a v b)
      (B₂ := cross a v r * cross a v b) hA hB
    have lin' : ∀ X Y : R2, cross X Y ((1 - ε) • y + ε • r) * cross a v b =
        (1 - ε) * (cross X Y y * cross a v b) + ε * (cross X Y r * cross a v b) := by
      intro X Y; rw [cross_lineMap X Y y r (1 - ε) ε (by ring)]; ring
    have hmem : (1 - ε) • y + ε • r ∈ segment ℝ p q :=
      (convex_segment p q) hy' hr (by linarith) hε.le (by ring)
    have hT : (1 - ε) • y + ε • r ∈ convexHull ℝ {a, v, b} := by
      refine (mem_convexHull_triple_iff hD).mpr ⟨?_, ?_, ?_⟩
      · rw [lin']; exact ha.le
      · rw [lin', hv0]; nlinarith [mul_pos hε hrv]
      · rw [lin']; exact hb.le
    have := hbound _ hmem hT
    rw [lin', hv0] at this
    nlinarith
  rcases lt_or_ge 0 (cross b a p * cross a v b) with hp | hp
  · exact raise p (left_mem_segment ℝ p q) hp
  rcases lt_or_ge 0 (cross b a q * cross a v b) with hq | hq
  · exact raise q (right_mem_segment ℝ p q) hq
  have hlv := lin b a
  rw [hv0] at hlv
  have hsp : s * (cross b a p * cross a v b) = 0 := by
    nlinarith [mul_nonpos_of_nonneg_of_nonpos hs hp, mul_nonpos_of_nonneg_of_nonpos ht hq]
  have htq : t * (cross b a q * cross a v b) = 0 := by
    nlinarith [mul_nonpos_of_nonneg_of_nonpos hs hp, mul_nonpos_of_nonneg_of_nonpos ht hq]
  -- an endpoint of the edge equal to `y`
  rcases hs.lt_or_eq with hs0 | hs0
  swap
  · have : y = q := by rw [← hyst, ← hs0, show t = 1 by linarith]; simp
    have hq' := hqT (this ▸ hyT)
    rw [this, hq', cross_left, zero_mul] at hB
    exact lt_irrefl _ hB
  rcases ht.lt_or_eq with ht0 | ht0
  swap
  · have : y = p := by rw [← hyst, ← ht0, show s = 1 by linarith]; simp
    have hp' := hpT (this ▸ hyT)
    rw [this, hp', cross_right, zero_mul] at hA
    exact lt_irrefl _ hA
  have hp0 : cross b a p = 0 :=
    (mul_eq_zero.mp ((mul_eq_zero.mp hsp).resolve_left hs0.ne')).resolve_right hD
  have hq0 : cross b a q = 0 :=
    (mul_eq_zero.mp ((mul_eq_zero.mp htq).resolve_left ht0.ne')).resolve_right hD
  -- on the line `a b`: compare `b`-weights
  have hS : 0 < cross a v b * cross a v b := mul_self_pos.mpr hD
  have hfy := lin a v
  have hsy := hsum y
  have hsp' := hsum p
  have hsq' := hsum q
  rw [hp0, zero_mul] at hsp'
  rw [hq0, zero_mul] at hsq'
  have hpin : ¬ (0 < cross a v p * cross a v b ∧ cross a v p * cross a v b <
      cross a v b * cross a v b) := by
    rintro ⟨hp1, hp2⟩
    have hpT' : p ∈ convexHull ℝ {a, v, b} :=
      (mem_convexHull_triple_iff hD).mpr ⟨by linarith, by rw [hp0, zero_mul], hp1.le⟩
    rw [hpT hpT'] at hp2
    exact lt_irrefl _ hp2
  have hqin : ¬ (0 < cross a v q * cross a v b ∧ cross a v q * cross a v b <
      cross a v b * cross a v b) := by
    rintro ⟨hq1, hq2⟩
    have hqT' : q ∈ convexHull ℝ {a, v, b} :=
      (mem_convexHull_triple_iff hD).mpr ⟨by linarith, by rw [hq0, zero_mul], hq1.le⟩
    rw [hqT hqT', cross_left, zero_mul] at hq1
    exact lt_irrefl _ hq1
  have ha0 : cross b a a = 0 := cross_right b a
  have hb0 : cross b a b = 0 := cross_left b a
  have hav : cross a v a * cross a v b = 0 := by rw [cross_left, zero_mul]
  push_neg at hpin hqin
  rcases le_or_gt (cross a v p * cross a v b) 0 with hpl | hpl
  · rcases le_or_gt (cross a v q * cross a v b) 0 with hql | hql
    · nlinarith
    · have hqS := hqin hql
      exact hab ⟨mem_segment_of_line hD hp0 hq0 ha0 (by linarith) (by linarith),
        mem_segment_of_line hD hp0 hq0 hb0 (by linarith) hqS⟩
  · have hpS := hpin hpl
    rcases le_or_gt (cross a v q * cross a v b) 0 with hql | hql
    · rw [segment_symm] at hab
      exact hab ⟨mem_segment_of_line hD hq0 hp0 ha0 (by linarith) (by linarith),
        mem_segment_of_line hD hq0 hp0 hb0 (by linarith) hpS⟩
    · have hqS := hqin hql
      nlinarith

/-- **An empty corner meets the polygon only in its sides.** -/
theorem corner_inter_of_empty {P : Polygon R2} (hP : P.IsSimple) (hn : 3 ≤ P.n)
    (hD : cross (P.w P.n) (P.w 0) (P.w 1) ≠ 0)
    (hempty : ∀ j, 2 ≤ j → j ≤ P.n - 1 → P.w j ∉ convexHull ℝ {P.w P.n, P.w 0, P.w 1}) :
    convexHull ℝ {P.w P.n, P.w 0, P.w 1} ∩ P.carrier ⊆
      segment ℝ (P.w P.n) (P.w 0) ∪ segment ℝ (P.w 0) (P.w 1) := by
  rintro y ⟨hyT, hy⟩
  rw [carrier_eq_biUnion] at hy
  simp only [mem_iUnion, Finset.mem_range] at hy
  obtain ⟨k, hk, hyk⟩ := hy
  by_cases hk0 : k = 0
  · subst hk0; right; exact hyk
  by_cases hkn : k = P.n
  · subst hkn; left; unfold seg at hyk; rwa [P.w_period] at hyk
  refine edge_corner hD (fun y' hy' hT => edge_weight_le hP hn hD le_rfl
      (fun j hj2 hjn hjT => absurd hjT (hempty j hj2 hjn)) (k := k) (by omega) (by omega) hy' hT)
    (fun h => ?_) (fun h => ?_) ?_ hyk hyT
  · by_cases h1 : k = 1
    · subst h1; rfl
    · exact absurd h (hempty k (by omega) (by omega))
  · by_cases h1 : k + 1 = P.n
    · rw [h1]
    · exact absurd h (hempty (k + 1) (by omega) (by omega))
  · rintro ⟨ha, hb⟩
    rcases hP.w_mem_seg le_rfl (by omega) ha with h | h
    · omega
    rcases hP.w_mem_seg (j := 1) (by omega) (by omega) hb with h' | h'
    · rw [Nat.mod_eq_of_lt (by omega)] at h; omega
    · rw [Nat.mod_eq_of_lt (by omega)] at h h'; omega

lemma isEar_add_period (P : Polygon R2) (k : ℕ) : P.IsEar (k + (P.n + 1)) ↔ P.IsEar k := by
  unfold Polygon.IsEar
  rw [show k + (P.n + 1) + P.n = (k + P.n) + (P.n + 1) by omega,
    show k + (P.n + 1) + 1 = (k + 1) + (P.n + 1) by omega, w_add_period, w_add_period,
    w_add_period]

/-- **An empty corner at the lowest-leftmost vertex is an ear.** -/
theorem isEar_of_empty_corner {P : Polygon R2} (hP : P.IsSimple) (hn : 3 ≤ P.n)
    (hlex : ∀ i, P.w 0 0 ≤ P.v i 0) (hD : cross (P.w P.n) (P.w 0) (P.w 1) ≠ 0)
    (hempty : ∀ j, 2 ≤ j → j ≤ P.n - 1 → P.w j ∉ convexHull ℝ {P.w P.n, P.w 0, P.w 1}) :
    P.IsEar 0 := by
  have A1 := corner_inter_of_empty hP hn hD hempty
  set R := P.rotateBy 1 with hR
  have hRs : R.IsSimple := Polygon.isSimple_rotateBy P hP 1
  have hRn : R.n = P.n := rotateBy_n P 1
  have hw : ∀ k, R.w k = P.w (k + 1) := fun k => w_rotateBy P 1 k
  set β := P.n - 1 with hβdef
  have hβ : 2 ≤ β := by omega
  have hβn : β + 1 ≤ R.n := by omega
  have h2 : 2 ≤ R.n + 1 - β := by omega
  have hRb : R.w 0 = P.w 1 := by rw [hw]
  have hRa : R.w β = P.w P.n := by rw [hw, show β + 1 = P.n by omega]
  have hRv : R.w R.n = P.w 0 := by rw [hw, hRn, P.w_period]
  have hDba : cross (P.w 1) (P.w P.n) (P.w 0) ≠ 0 := by rw [cross_rot2]; exact hD
  have haT : P.w P.n ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1} := subset_convexHull ℝ _ (by simp)
  have hvT : P.w 0 ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1} := subset_convexHull ℝ _ (by simp)
  have hbT : P.w 1 ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1} := subset_convexHull ℝ _ (by simp)
  -- the chord `[b, a]`
  have hchord : segment ℝ (R.w 0) (R.w β) ∩ R.carrier ⊆ {R.w 0, R.w β} := by
    rw [hRb, hRa, carrier_rotateBy]
    rintro y ⟨hy1, hy2⟩
    have hyT : y ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1} :=
      (convex_convexHull ℝ _).segment_subset hbT haT hy1
    obtain ⟨s, t, hs, ht, hst, rfl⟩ := hy1
    rcases A1 ⟨hyT, hy2⟩ with h | h
    · have h0 := cross_eq_zero_of_mem_segment h
      rw [cross_lineMap _ _ _ _ s t hst, cross_left, mul_zero, add_zero] at h0
      have : s = 0 := (mul_eq_zero.mp h0).resolve_right hD
      right; rw [this, show t = 1 by linarith]; simp
    · have h0 := cross_eq_zero_of_mem_segment h
      rw [cross_lineMap _ _ _ _ s t hst, cross_right, mul_zero, zero_add, cross_rot] at h0
      have : t = 0 := (mul_eq_zero.mp h0).resolve_right hD
      left; rw [this, show s = 1 by linarith]; simp
  -- the big piece: witness `v`
  have S₁ := parity_cut_eq_zero_of_witness hRs hβ hβn hchord (y₀ := P.w 0) ?_ ?_
  rotate_left
  · refine ⟨R.n, by omega, le_rfl, ?_, ?_, ?_⟩
    · unfold seg; rw [hRv]; exact left_mem_segment ℝ _ _
    · rw [hRa]; exact hP.w_n_ne_zero.symm
    · rw [hRb]; exact hP.w_ne_succ (k := 0) (by omega)
  · set Q := R.cut β hβ
    have hvQ : P.w 0 ∉ Q.carrier := by
      rw [carrier_cut]
      rintro (h | h)
      · obtain ⟨k, hk, hvk⟩ := mem_iUnion₂.mp h
        rw [Finset.mem_range] at hk
        rw [seg_rotateBy] at hvk
        rcases hP.w_mem_seg (Nat.zero_le _) (by omega) hvk with h | h
        · omega
        · rw [Nat.mod_eq_of_lt (by omega)] at h; omega
      · rw [hRb, hRa] at h
        exact hDba (cross_eq_zero_of_mem_segment h)
    have hev := Q.parity_eventually_eq hvQ
    have hc : Continuous (fun δ : ℝ => P.w 0 - δ • e0) := by fun_prop
    have ht : Tendsto (fun δ : ℝ => P.w 0 - δ • e0) (𝓝[>] 0) (𝓝 (P.w 0)) := by
      have := (hc.tendsto 0).mono_left (nhdsWithin_le_nhds (s := Ioi 0))
      simpa using this
    obtain ⟨δ, hδ, hδ0⟩ := ((ht.eventually hev).and self_mem_nhdsWithin).exists
    rw [← hδ]
    refine Q.parity_eq_zero_of_forall_lt fun i => ?_
    rw [← w_coe, cut_w, hw]
    have := hlex ⟨((i : ℕ) % (β + 1) + 1) % (P.n + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩
    change P.w 0 0 ≤ P.w ((i : ℕ) % (β + 1) + 1) 0 at this
    simp only [e0, Pi.sub_apply, Pi.smul_apply, smul_eq_mul, Matrix.cons_val_zero, mul_one]
    have : (0 : ℝ) < δ := hδ0
    linarith
  -- the triangle piece
  have S₂ : ∀ y ∈ R.carrier, y ∉ (R.cocut β h2).carrier → (R.cocut β h2).parity y = 0 := by
    intro y hy hyc
    rw [carrier_rotateBy] at hy
    apply Polygon.parity_eq_zero_of_not_mem_convexHull
    intro hyH
    have hsub : range (R.cocut β h2).v ⊆ {P.w P.n, P.w 0, P.w 1} := by
      rintro x ⟨i, rfl⟩
      have hi : (i : ℕ) ≤ R.n + 1 - β := Nat.lt_succ_iff.mp i.2
      rw [← w_coe, cocut_w_of_le R hi, hw]
      have hi2 : (i : ℕ) ≤ 2 := by omega
      interval_cases h : (i : ℕ)
      · rw [show 0 + β + 1 = P.n by omega]; simp
      · rw [show 1 + β + 1 = P.n + 1 by omega, P.w_period]; simp
      · rw [show 2 + β + 1 = 1 + (P.n + 1) by omega, w_add_period]; simp
    have hyT := convexHull_mono hsub hyH
    apply hyc
    rw [carrier_cocut R (by omega) h2]
    left
    rcases A1 ⟨hyT, hy⟩ with h | h
    · refine mem_iUnion₂.mpr ⟨0, Finset.mem_range.mpr (by omega), ?_⟩
      rw [seg_rotateBy]; unfold seg
      rw [show 0 + β + 1 = P.n by omega, show P.n + 1 = P.n + 1 from rfl, P.w_period]; exact h
    · refine mem_iUnion₂.mpr ⟨1, Finset.mem_range.mpr (by omega), ?_⟩
      rw [seg_rotateBy]; unfold seg
      rw [show 1 + β + 1 = P.n + 1 by omega, P.w_period,
        show P.n + 1 + 1 = 1 + (P.n + 1) by omega, w_add_period]; exact h
  have hear := isEar_of_cocut hRs hβ h2 hchord S₁ S₂ (k := 1) le_rfl (by omega)
    (Or.inr (by omega))
  rw [isEar_rotateBy, show 1 + β + 1 = 0 + (P.n + 1) by omega, isEar_add_period] at hear
  exact hear

end QOU.MathlibExt.PL
