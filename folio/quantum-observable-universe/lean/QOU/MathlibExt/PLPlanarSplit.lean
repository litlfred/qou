/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarParity

set_option autoImplicit false

/-!
# Cutting a polygon along a chord (issue #8902, Moise part B, step 1)

Bookkeeping for the two-ears theorem. A chord `[w 0, w β]` of a simple polygon that meets the
polygon only at its endpoints cuts it into two simple polygons, and the crossing parity of the
polygon is the sum of the parities of the two pieces.

## What is a DEFINITION here

* `Polygon.w P k` — the vertex with index `k` read modulo `n + 1`.
* `Polygon.seg P k` — the edge `[w k, w (k + 1)]`.
* `Polygon.cut P β` — the polygon with vertices `w 0, …, w β`; its closing edge is the chord
  `[w β, w 0]`.

## What is a THEOREM here

* `Polygon.isSimple_iff_seg` — simplicity with natural-number indices.
* `Polygon.isSimple_cut` — **the piece cut off by a chord is simple**, if the chord meets the
  polygon only at its endpoints and `2 ≤ β ≤ n - 1`.
* `Polygon.w_rotateBy`, `Polygon.parity_rotateBy` — rotating the vertex list shifts `w` and keeps
  the parity.
* `Polygon.parity_split` — **the parity is additive over the two pieces**: the chord is an edge
  of both, and its two contributions cancel modulo `2`.
-/

namespace QOU.MathlibExt.PL

open Set

namespace Polygon

section general

variable {E : Type*} [AddCommGroup E] [Module ℝ E] (P : Polygon E)

/-- The vertex with index `k`, read modulo `n + 1`. -/
def w (k : ℕ) : E := P.v ⟨k % (P.n + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩

lemma w_coe (i : Fin (P.n + 1)) : P.w i = P.v i := by
  unfold w; congr 1; ext; simp [Nat.mod_eq_of_lt i.2]

lemma w_mod (k : ℕ) : P.w (k % (P.n + 1)) = P.w k := by
  unfold w; simp

lemma w_add_period (k : ℕ) : P.w (k + (P.n + 1)) = P.w k := by
  unfold w; simp [Nat.add_mod_right]

lemma w_period : P.w (P.n + 1) = P.w 0 := by simpa using P.w_add_period 0

lemma next_val (i : Fin (P.n + 1)) : (P.next i : ℕ) = ((i : ℕ) + 1) % (P.n + 1) := by
  unfold next
  rw [coe_finRotate]
  split_ifs with h
  · subst h; simp
  · rw [Nat.mod_eq_of_lt]
    have := Fin.val_lt_last h
    omega

lemma v_next (i : Fin (P.n + 1)) : P.v (P.next i) = P.w (i + 1) := by
  rw [← w_coe, next_val, w_mod]

/-- The edge `[w k, w (k + 1)]`, indices modulo `n + 1`. -/
def seg (k : ℕ) : Set E := segment ℝ (P.w k) (P.w (k + 1))

lemma edge_eq_seg (i : Fin (P.n + 1)) : P.edge i = P.seg i := by
  unfold edge seg; rw [w_coe, v_next]

lemma seg_subset_carrier {k : ℕ} (hk : k ≤ P.n) : P.seg k ⊆ P.carrier := by
  have := P.edge_eq_seg ⟨k, by omega⟩
  simp only at this
  rw [← this]
  exact P.edge_subset_carrier _

lemma carrier_eq_biUnion : P.carrier = ⋃ k ∈ Finset.range (P.n + 1), P.seg k := by
  ext x
  simp only [carrier, mem_iUnion, Finset.mem_range, edge_eq_seg]
  constructor
  · rintro ⟨i, hi⟩; exact ⟨i, i.2, hi⟩
  · rintro ⟨k, hk, hx⟩; exact ⟨⟨k, hk⟩, hx⟩

lemma w_mem_seg_left (k : ℕ) : P.w k ∈ P.seg k := left_mem_segment ℝ _ _

lemma w_mem_seg_right (k : ℕ) : P.w (k + 1) ∈ P.seg k := right_mem_segment ℝ _ _

/-- **Simplicity with natural-number indices.** -/
theorem isSimple_iff_seg : P.IsSimple ↔
    (∀ i j : ℕ, i ≤ P.n → j ≤ P.n → P.w i = P.w j → i = j) ∧
    ∀ i j : ℕ, i ≤ P.n → j ≤ P.n → i ≠ j → P.seg i ∩ P.seg j =
      if j = (i + 1) % (P.n + 1) then {P.w j}
      else if i = (j + 1) % (P.n + 1) then {P.w i} else ∅ := by
  constructor
  · rintro ⟨hinj, hint⟩
    refine ⟨fun i j hi hj he => ?_, fun i j hi hj hij => ?_⟩
    · have := @hinj ⟨i, by omega⟩ ⟨j, by omega⟩ (by
        have h1 := P.w_coe ⟨i, by omega⟩
        have h2 := P.w_coe ⟨j, by omega⟩
        simp only at h1 h2
        rw [← h1, ← h2, he])
      simpa [Fin.ext_iff] using this
    · have := hint ⟨i, by omega⟩ ⟨j, by omega⟩ (by simpa [Fin.ext_iff] using hij)
      rw [edge_eq_seg, edge_eq_seg] at this
      simp only at this
      rw [this]
      simp only [Fin.ext_iff, next_val]
      have h1 := P.w_coe ⟨i, by omega⟩
      have h2 := P.w_coe ⟨j, by omega⟩
      simp only at h1 h2
      rw [h1, h2]
  · rintro ⟨hinj, hint⟩
    refine ⟨fun a b hab => ?_, fun a b hab => ?_⟩
    · have := hinj a b (by omega) (by omega) (by rw [w_coe, w_coe, hab])
      exact Fin.ext this
    · rw [edge_eq_seg, edge_eq_seg, hint a b (by omega) (by omega) (fun h => hab (Fin.ext h))]
      simp only [Fin.ext_iff, next_val, w_coe]

variable {P}

lemma IsSimple.w_injOn (h : P.IsSimple) {i j : ℕ} (hi : i ≤ P.n) (hj : j ≤ P.n)
    (he : P.w i = P.w j) : i = j :=
  ((isSimple_iff_seg P).mp h).1 i j hi hj he

lemma IsSimple.seg_inter (h : P.IsSimple) {i j : ℕ} (hi : i ≤ P.n) (hj : j ≤ P.n) (hij : i ≠ j) :
    P.seg i ∩ P.seg j =
      if j = (i + 1) % (P.n + 1) then {P.w j}
      else if i = (j + 1) % (P.n + 1) then {P.w i} else ∅ :=
  ((isSimple_iff_seg P).mp h).2 i j hi hj hij

/-- A vertex lies only on its two incident edges. -/
lemma IsSimple.w_mem_seg (h : P.IsSimple) {j k : ℕ} (hj : j ≤ P.n) (hk : k ≤ P.n)
    (hm : P.w j ∈ P.seg k) : j = k ∨ j = (k + 1) % (P.n + 1) := by
  by_contra hc
  push_neg at hc
  have hin : P.w j ∈ P.seg j ∩ P.seg k := ⟨P.w_mem_seg_left j, hm⟩
  rw [h.seg_inter hj hk hc.1] at hin
  split_ifs at hin with h1 h2
  · exact hc.1 (h.w_injOn hj hk hin)
  · exact hc.2 h2
  · exact hin

variable (P)

/-! ### Cutting along a chord -/

/-- The polygon `w 0, w 1, …, w β`; its closing edge is the chord `[w β, w 0]`. -/
def cut (β : ℕ) (hβ : 2 ≤ β) : Polygon E := ⟨β, hβ, fun k => P.w k⟩

variable {β : ℕ} {hβ : 2 ≤ β}

lemma cut_n : (P.cut β hβ).n = β := rfl

lemma cut_w (k : ℕ) : (P.cut β hβ).w k = P.w (k % (β + 1)) := rfl

lemma cut_w_of_le {k : ℕ} (hk : k ≤ β) : (P.cut β hβ).w k = P.w k := by
  rw [cut_w, Nat.mod_eq_of_lt (by omega)]

lemma cut_seg_of_lt {k : ℕ} (hk : k < β) : (P.cut β hβ).seg k = P.seg k := by
  unfold seg; rw [cut_w_of_le P (by omega), cut_w_of_le P (by omega)]

lemma cut_seg_self : (P.cut β hβ).seg β = segment ℝ (P.w β) (P.w 0) := by
  unfold seg; rw [cut_w_of_le P le_rfl, cut_w, Nat.mod_self]

lemma carrier_cut : (P.cut β hβ).carrier =
    (⋃ k ∈ Finset.range β, P.seg k) ∪ segment ℝ (P.w 0) (P.w β) := by
  rw [carrier_eq_biUnion, cut_n, Finset.range_add_one, Finset.set_biUnion_insert, union_comm,
    cut_seg_self, segment_symm]
  congr 1
  refine iUnion₂_congr fun k hk => ?_
  exact P.cut_seg_of_lt (Finset.mem_range.mp hk)

variable {P}

/-- **The piece cut off by a chord is simple.** -/
theorem isSimple_cut (h : P.IsSimple) (hβ : 2 ≤ β) (hβn : β + 1 ≤ P.n)
    (hD : segment ℝ (P.w 0) (P.w β) ∩ P.carrier ⊆ {P.w 0, P.w β}) :
    (P.cut β hβ).IsSimple := by
  rw [isSimple_iff_seg]
  simp only [cut_n]
  refine ⟨fun i j hi hj he => ?_, fun i j hi hj hij => ?_⟩
  · rw [cut_w_of_le P hi, cut_w_of_le P hj] at he
    exact h.w_injOn (by omega) (by omega) he
  -- the chord meets edge `k < β` exactly in the shared endpoints
  have hchord : ∀ k, k < β → segment ℝ (P.w β) (P.w 0) ∩ P.seg k =
      (if k = 0 then {P.w 0} else ∅) ∪ (if β = k + 1 then {P.w β} else ∅) := by
    intro k hk
    ext x
    simp only [mem_inter_iff, mem_union]
    constructor
    · rintro ⟨hx1, hx2⟩
      have hxP : x ∈ P.carrier := P.seg_subset_carrier (by omega) hx2
      rw [segment_symm] at hx1
      rcases hD ⟨hx1, hxP⟩ with hx | hx
      · subst hx
        rcases h.w_mem_seg (by omega) (by omega) hx2 with h0 | h0
        · left; rw [if_pos h0.symm]; rfl
        · rw [Nat.mod_eq_of_lt (by omega)] at h0; omega
      · rw [mem_singleton_iff] at hx
        subst hx
        rcases h.w_mem_seg (by omega) (by omega) hx2 with h0 | h0
        · omega
        · rw [Nat.mod_eq_of_lt (by omega)] at h0
          right; rw [if_pos h0]; rfl
    · rintro (hx | hx)
      · split_ifs at hx with hk0
        · rw [mem_singleton_iff] at hx; subst hx; subst hk0
          exact ⟨right_mem_segment ℝ _ _, P.w_mem_seg_left 0⟩
        · exact absurd hx (notMem_empty x)
      · split_ifs at hx with hk0
        · rw [mem_singleton_iff] at hx; subst hx
          refine ⟨left_mem_segment ℝ _ _, ?_⟩
          rw [hk0]; exact P.w_mem_seg_right k
        · exact absurd hx (notMem_empty x)
  rcases Nat.lt_or_ge i β with hiβ | hiβ <;> rcases Nat.lt_or_ge j β with hjβ | hjβ
  · rw [cut_seg_of_lt P hiβ, cut_seg_of_lt P hjβ, h.seg_inter (by omega) (by omega) hij]
    simp only [Nat.mod_eq_of_lt (show i + 1 < P.n + 1 by omega),
      Nat.mod_eq_of_lt (show j + 1 < P.n + 1 by omega),
      Nat.mod_eq_of_lt (show i + 1 < β + 1 by omega),
      Nat.mod_eq_of_lt (show j + 1 < β + 1 by omega), cut_w_of_le P hi, cut_w_of_le P hj]
  · have hj' : j = β := by omega
    subst hj'
    rw [cut_seg_of_lt P hiβ, cut_seg_self, inter_comm, hchord i hiβ]
    simp only [Nat.mod_eq_of_lt (show i + 1 < j + 1 by omega), Nat.mod_self, cut_w_of_le P hi,
      cut_w_of_le P (le_refl j)]
    have hj1 : j ≠ 1 := by omega
    by_cases hi0 : i = 0 <;> by_cases hi1 : j = i + 1
    · omega
    all_goals simp [*]
  · have hi' : i = β := by omega
    subst hi'
    rw [cut_seg_of_lt P hjβ, cut_seg_self, hchord j hjβ]
    simp only [Nat.mod_eq_of_lt (show j + 1 < i + 1 by omega), Nat.mod_self, cut_w_of_le P hj,
      cut_w_of_le P (le_refl i)]
    have hi1' : i ≠ 1 := by omega
    by_cases hj0 : j = 0 <;> by_cases hj1 : i = j + 1
    · omega
    all_goals simp [*]
  · omega

/-! ### Rotation -/

variable (P)

@[simp] lemma rotateBy_n (r : ℕ) : (P.rotateBy r).n = P.n := by
  induction r with
  | zero => rfl
  | succ r ih => simp only [rotateBy, rotate_n, ih]

lemma rotate_w (k : ℕ) : P.rotate.w k = P.w (k + 1) := by
  have h1 : P.rotate.w k = P.rotate.v ⟨k % (P.n + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩ := rfl
  rw [h1, rotate_v, v_next]
  simp only
  rw [← w_mod P (k % (P.n + 1) + 1), ← w_mod P (k + 1), Nat.add_mod, Nat.mod_mod,
    ← Nat.add_mod]

lemma w_rotateBy (r k : ℕ) : (P.rotateBy r).w k = P.w (k + r) := by
  induction r generalizing k with
  | zero => rfl
  | succ r ih =>
    show (P.rotateBy r).rotate.w k = _
    rw [rotate_w, ih]
    congr 1
    omega

end general

/-! ### The parity of the pieces -/

variable (P : Polygon R2)

lemma parity_eq_sum_range (y : R2) :
    P.parity y = ∑ k ∈ Finset.range (P.n + 1), crossInd (P.w k) (P.w (k + 1)) y := by
  unfold parity
  rw [← Fin.sum_univ_eq_sum_range (fun k => crossInd (P.w k) (P.w (k + 1)) y)]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [w_coe, v_next]

lemma parity_rotate : P.rotate.parity = P.parity := by
  funext y
  unfold parity
  simp only [rotate_v, rotate_next]
  exact Equiv.sum_comp (finRotate (P.n + 1)) (fun i => crossInd (P.v i) (P.v (P.next i)) y)

lemma parity_rotateBy (r : ℕ) : (P.rotateBy r).parity = P.parity := by
  induction r with
  | zero => rfl
  | succ r ih => exact ((P.rotateBy r).parity_rotate).trans ih

lemma parity_cut {β : ℕ} (hβ : 2 ≤ β) (y : R2) :
    (P.cut β hβ).parity y = ∑ k ∈ Finset.range β, crossInd (P.w k) (P.w (k + 1)) y +
      crossInd (P.w β) (P.w 0) y := by
  rw [parity_eq_sum_range, cut_n, Finset.sum_range_succ]
  congr 1
  · refine Finset.sum_congr rfl fun k hk => ?_
    have hk := Finset.mem_range.mp hk
    rw [cut_w_of_le P (by omega), cut_w_of_le P (by omega)]
  · rw [cut_w_of_le P le_rfl, cut_w, Nat.mod_self]

/-- The complementary piece: `w β, …, w n, w 0`, re-indexed from `w β`. -/
def cocut (β : ℕ) (h : 2 ≤ P.n + 1 - β) : Polygon R2 :=
  (P.rotateBy β).cut (P.n + 1 - β) h

lemma cocut_w_of_le {β : ℕ} {h : 2 ≤ P.n + 1 - β} {k : ℕ} (hk : k ≤ P.n + 1 - β) :
    (P.cocut β h).w k = P.w (k + β) := by
  unfold cocut
  rw [cut_w_of_le _ hk, w_rotateBy]

/-- **The parity is additive over the two pieces cut by a chord.** -/
theorem parity_split {β : ℕ} (hβ : 2 ≤ β) (h : 2 ≤ P.n + 1 - β) (y : R2) :
    P.parity y = (P.cut β hβ).parity y + (P.cocut β h).parity y := by
  have hβn : β ≤ P.n + 1 := by omega
  rw [parity_cut, cocut, parity_cut, parity_eq_sum_range]
  simp only [w_rotateBy, zero_add]
  rw [show P.n + 1 - β + β = P.n + 1 by omega, w_period]
  rw [← Finset.sum_range_add_sum_Ico _ hβn, Finset.sum_Ico_eq_sum_range]
  have hc : crossInd (P.w β) (P.w 0) y + crossInd (P.w 0) (P.w β) y = 0 := by
    rw [crossInd_swap]; exact CharTwo.add_self_eq_zero _
  have hs : ∀ k ∈ Finset.range (P.n + 1 - β),
      crossInd (P.w (β + k)) (P.w (β + k + 1)) y = crossInd (P.w (k + β)) (P.w (k + 1 + β)) y := by
    intro k _
    rw [show β + k = k + β by omega, show k + β + 1 = k + 1 + β by omega]
  rw [Finset.sum_congr rfl hs]
  linear_combination (exp := 1) -hc

end Polygon

end QOU.MathlibExt.PL
