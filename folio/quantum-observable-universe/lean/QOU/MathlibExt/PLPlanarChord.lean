/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarEarTransfer

set_option autoImplicit false

/-!
# The far side of a chord is connected (issue #8902, Moise part B, step 1)

Cut a simple polygon `P` along a chord `[w 0, w β]`. The rest of `P`, the open path
`w β, w (β+1), …, w n, w 0` without its two ends, is connected and misses the cut piece. So the
cut piece's crossing parity is constant on it: one point decides it.

## What is a THEOREM here

* `isPreconnected_farPath` — the open far path is connected.
* `disjoint_farPath_cut` — it misses the cut piece.
* `parity_cut_eq_zero_of_witness` — if the cut piece's parity is `0` at one point of the far
  path, it is `0` on all of `P` off the cut piece.
-/

namespace QOU.MathlibExt.PL

open Set Polygon

lemma lineMap_eq_left_iff {a b : R2} (hab : a ≠ b) {t : ℝ} :
    AffineMap.lineMap a b t = a ↔ t = 0 := by
  rw [AffineMap.lineMap_apply, vsub_eq_sub, vadd_eq_add, add_eq_right, smul_eq_zero,
    sub_eq_zero]
  exact ⟨fun h => h.resolve_right (Ne.symm hab), fun h => Or.inl h⟩

lemma lineMap_eq_right_iff {a b : R2} (hab : a ≠ b) {t : ℝ} :
    AffineMap.lineMap a b t = b ↔ t = 1 := by
  rw [← AffineMap.lineMap_apply_one_sub, lineMap_eq_left_iff (Ne.symm hab), sub_eq_zero, eq_comm]

variable {P : Polygon R2}

/-- The open far path of the chord `[w 0, w β]`. -/
def Polygon.farPath (P : Polygon R2) (β : ℕ) : Set R2 :=
  {y | ∃ k, β ≤ k ∧ k ≤ P.n ∧ y ∈ P.seg k ∧ y ≠ P.w β ∧ y ≠ P.w 0}

lemma Polygon.IsSimple.w_ne_succ (hP : P.IsSimple) {k : ℕ} (hk : k + 1 ≤ P.n) : P.w k ≠ P.w (k + 1) :=
  fun h => by have := hP.w_injOn (by omega) hk h; omega

lemma Polygon.IsSimple.w_n_ne_zero (hP : P.IsSimple) : P.w P.n ≠ P.w 0 :=
  fun h => by have := hP.w_injOn le_rfl (Nat.zero_le _) h; have := P.two_le; omega

variable {β : ℕ}

theorem disjoint_farPath_cut (hP : P.IsSimple) (hβ : 2 ≤ β) (hβn : β + 1 ≤ P.n)
    (hchord : segment ℝ (P.w 0) (P.w β) ∩ P.carrier ⊆ {P.w 0, P.w β}) :
    Disjoint (P.farPath β) (P.cut β hβ).carrier := by
  rw [Set.disjoint_left, carrier_cut]
  rintro y ⟨k, hk1, hk2, hyk, hyβ, hy0⟩ (h | h)
  · simp only [mem_iUnion, Finset.mem_range] at h
    obtain ⟨i, hi, hyi⟩ := h
    have hin : y ∈ P.seg k ∩ P.seg i := ⟨hyk, hyi⟩
    rw [hP.seg_inter hk2 (by omega) (by omega)] at hin
    split_ifs at hin with c1 c2
    · rcases Nat.lt_or_ge (k + 1) (P.n + 1) with h | h
      · rw [Nat.mod_eq_of_lt h] at c1; omega
      · obtain rfl : k = P.n := by omega
        rw [Nat.mod_self] at c1; subst c1; exact hy0 hin
    · rw [Nat.mod_eq_of_lt (by omega)] at c2
      obtain rfl : k = β := by omega
      exact hyβ hin
    · exact hin
  · rcases hchord ⟨h, P.seg_subset_carrier hk2 hyk⟩ with h | h
    · exact hy0 h
    · exact hyβ h

theorem diff_subset_farPath (hβ : 2 ≤ β) :
    P.carrier \ (P.cut β hβ).carrier ⊆ P.farPath β := by
  rintro y ⟨hy, hyc⟩
  rw [carrier_eq_biUnion] at hy
  simp only [mem_iUnion, Finset.mem_range] at hy
  obtain ⟨k, hk, hyk⟩ := hy
  refine ⟨k, ?_, by omega, hyk, ?_, ?_⟩
  · by_contra hkb
    apply hyc
    rw [carrier_cut]
    left
    exact mem_iUnion₂.mpr ⟨k, Finset.mem_range.mpr (by omega), hyk⟩
  · rintro rfl; apply hyc; rw [carrier_cut]; right; exact right_mem_segment _ _ _
  · rintro rfl; apply hyc; rw [carrier_cut]; right; exact left_mem_segment _ _ _

/-- The first edge of the far path, without its start. -/
def Polygon.farFirst (P : Polygon R2) (β : ℕ) : Set R2 :=
  AffineMap.lineMap (P.w β) (P.w (β + 1)) '' Ioc (0 : ℝ) 1

/-- The last edge of the far path, without its end. -/
def Polygon.farLast (P : Polygon R2) : Set R2 :=
  AffineMap.lineMap (P.w P.n) (P.w 0) '' Ico (0 : ℝ) 1

/-- The far path, assembled edge by edge. -/
def Polygon.farChain (P : Polygon R2) (β m : ℕ) : Set R2 :=
  P.farFirst β ∪ ⋃ i ∈ Finset.range m, P.seg (β + 1 + i)

lemma isPreconnected_farChain (m : ℕ) :
    IsPreconnected (P.farChain β m) ∧ P.w (β + m + 1) ∈ P.farChain β m := by
  induction m with
  | zero =>
    simp only [Polygon.farChain, Finset.range_zero, Finset.notMem_empty, iUnion_of_empty, iUnion_empty,
      union_empty, add_zero]
    refine ⟨isPreconnected_Ioc.image _ (AffineMap.lineMap_continuous).continuousOn, ?_⟩
    exact ⟨1, ⟨by norm_num, le_rfl⟩, AffineMap.lineMap_apply_one _ _⟩
  | succ m ih =>
    have heq : P.farChain β (m + 1) = P.farChain β m ∪ P.seg (β + 1 + m) := by
      simp only [Polygon.farChain, Finset.range_add_one, Finset.set_biUnion_insert]
      rw [union_comm (P.seg _), union_assoc]
    rw [heq]
    refine ⟨ih.1.union (P.w (β + m + 1)) ih.2 ?_ (convex_segment _ _).isPreconnected, ?_⟩
    · rw [show β + m + 1 = β + 1 + m by omega]; exact P.w_mem_seg_left _
    · right
      rw [show β + (m + 1) + 1 = β + 1 + m + 1 by omega]
      exact P.w_mem_seg_right _

theorem farPath_eq (hP : P.IsSimple) (hβ : 2 ≤ β) (hβn : β + 1 ≤ P.n) :
    P.farPath β = P.farChain β (P.n - 1 - β) ∪ P.farLast := by
  have hseg : ∀ k, P.seg k = AffineMap.lineMap (P.w k) (P.w (k + 1)) '' Icc (0 : ℝ) 1 :=
    fun k => segment_eq_image_lineMap ℝ _ _
  have hwn : P.w (P.n + 1) = P.w 0 := P.w_period
  have hne1 := hP.w_ne_succ (k := β) hβn
  have hne2 := hP.w_n_ne_zero
  ext y
  constructor
  · rintro ⟨k, hk1, hk2, hyk, hyβ, hy0⟩
    rcases eq_or_lt_of_le hk1 with rfl | hk1
    · left; left
      rw [hseg] at hyk
      obtain ⟨t, ht, rfl⟩ := hyk
      refine ⟨t, ⟨lt_of_le_of_ne ht.1 fun h => hyβ ?_, ht.2⟩, rfl⟩
      rw [← h, AffineMap.lineMap_apply_zero]
    rcases eq_or_lt_of_le hk2 with rfl | hk2
    · right
      rw [hseg, hwn] at hyk
      obtain ⟨t, ht, rfl⟩ := hyk
      refine ⟨t, ⟨ht.1, lt_of_le_of_ne ht.2 fun h => hy0 ?_⟩, rfl⟩
      rw [h, AffineMap.lineMap_apply_one]
    · left; right
      refine mem_iUnion₂.mpr ⟨k - β - 1, Finset.mem_range.mpr (by omega), ?_⟩
      rwa [show β + 1 + (k - β - 1) = k by omega]
  · rintro ((h | h) | h)
    · obtain ⟨t, ht, rfl⟩ := h
      refine ⟨β, le_rfl, by omega, ?_, ?_, ?_⟩
      · rw [hseg]; exact ⟨t, ⟨ht.1.le, ht.2⟩, rfl⟩
      · rw [Ne, lineMap_eq_left_iff hne1]; exact ht.1.ne'
      · intro h
        have hm : P.w 0 ∈ P.seg β := by
          rw [← h, hseg]; exact ⟨t, ⟨ht.1.le, ht.2⟩, rfl⟩
        rcases hP.w_mem_seg (Nat.zero_le _) (by omega) hm with h | h
        · omega
        · rw [Nat.mod_eq_of_lt (by omega)] at h; omega
    · obtain ⟨i, hi, hy⟩ := mem_iUnion₂.mp h
      have hi := Finset.mem_range.mp hi
      refine ⟨β + 1 + i, by omega, by omega, hy, ?_, ?_⟩
      · rintro rfl
        rcases hP.w_mem_seg (by omega) (by omega) hy with h | h
        · omega
        · rw [Nat.mod_eq_of_lt (by omega)] at h; omega
      · rintro rfl
        rcases hP.w_mem_seg (Nat.zero_le _) (by omega) hy with h | h
        · omega
        · rw [Nat.mod_eq_of_lt (by omega)] at h; omega
    · obtain ⟨t, ht, rfl⟩ := h
      refine ⟨P.n, by omega, le_rfl, ?_, ?_, ?_⟩
      · rw [hseg, hwn]; exact ⟨t, ⟨ht.1, ht.2.le⟩, rfl⟩
      · intro h
        have hm : P.w β ∈ P.seg P.n := by
          rw [← h, hseg, hwn]; exact ⟨t, ⟨ht.1, ht.2.le⟩, rfl⟩
        rcases hP.w_mem_seg (by omega) le_rfl hm with h | h
        · omega
        · rw [Nat.mod_self] at h; omega
      · rw [Ne, lineMap_eq_right_iff hne2]; exact ht.2.ne

theorem isPreconnected_farPath (hP : P.IsSimple) (hβ : 2 ≤ β) (hβn : β + 1 ≤ P.n) :
    IsPreconnected (P.farPath β) := by
  rw [farPath_eq hP hβ hβn]
  have h := isPreconnected_farChain (P := P) (β := β) (P.n - 1 - β)
  rw [show β + (P.n - 1 - β) + 1 = P.n by omega] at h
  refine h.1.union (P.w P.n) h.2 ⟨0, ⟨le_rfl, by norm_num⟩, AffineMap.lineMap_apply_zero _ _⟩ ?_
  exact isPreconnected_Ico.image _ (AffineMap.lineMap_continuous).continuousOn

lemma farFirst_subset (hP : P.IsSimple) (hβ : 2 ≤ β) (hβn : β + 1 ≤ P.n) :
    P.farFirst β ⊆ P.farPath β := by
  rw [farPath_eq hP hβ hβn]; intro y hy; left; left; exact hy

lemma farLast_subset (hP : P.IsSimple) (hβ : 2 ≤ β) (hβn : β + 1 ≤ P.n) :
    P.farLast ⊆ P.farPath β := by
  rw [farPath_eq hP hβ hβn]; intro y hy; right; exact hy

/-- **One point decides.** If the cut piece has parity `0` at one point of the far path, it has
parity `0` on all of `P` off the cut piece. -/
theorem parity_cut_eq_zero_of_witness (hP : P.IsSimple) (hβ : 2 ≤ β) (hβn : β + 1 ≤ P.n)
    (hchord : segment ℝ (P.w 0) (P.w β) ∩ P.carrier ⊆ {P.w 0, P.w β}) {y₀ : R2}
    (hy₀ : y₀ ∈ P.farPath β) (hpar : (P.cut β hβ).parity y₀ = 0) :
    ∀ y ∈ P.carrier, y ∉ (P.cut β hβ).carrier → (P.cut β hβ).parity y = 0 := by
  intro y hy hyc
  rw [← hpar]
  exact (P.cut β hβ).parity_const_of_isPreconnected (isPreconnected_farPath hP hβ hβn)
    (disjoint_farPath_cut hP hβ hβn hchord) (diff_subset_farPath hβ ⟨hy, hyc⟩) hy₀

end QOU.MathlibExt.PL
