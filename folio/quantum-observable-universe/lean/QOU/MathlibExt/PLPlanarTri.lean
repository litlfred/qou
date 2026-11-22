/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarSplit

set_option autoImplicit false

/-!
# Plane triangles (issue #8902, Moise part B, step 1)

Barycentric coordinates by cross products, and the Jordan curve theorem for a triangle.

## What is a DEFINITION here

* `triPoly p q r` — the triangle `p, q, r` as a polygon.
* `openTri p q r` — the open triangle: all three cross products have the sign of `cross p q r`.

## What is a THEOREM here

* `cross_cyclic_sum`, `cross_bary` — `cross q r x`, `cross r p x`, `cross p q x` are the
  barycentric coordinates of `x` times `cross p q r`.
* `mem_convexHull_triple_iff` — for `cross p q r ≠ 0`, membership in the closed triangle is the
  sign condition on the three cross products.
* `mem_segment_of_mem_convexHull_of_cross` — a point of the triangle with `cross p q x = 0` is on
  `[p, q]`.
* `cross_ne_zero_of_isSimple` — a simple triangle is not degenerate.
* `triPoly_parity` — the parity of a triangle is the sum of its three edge indicators.
* `crossInd_add_sub_e1` — moving vertically by less than the distance to a line keeps `crossInd`.
* `convex_openTri`, `disjoint_openTri`, `mem_openTri` — the open triangle is convex, misses the
  boundary, and holds every point of the closed triangle off the boundary.
* `triPoly_parity_eq_one` — **the inside of a non-degenerate triangle has crossing parity `1`.**
-/

namespace QOU.MathlibExt.PL

open Set Polygon

lemma cross_cyclic_sum (p q r x : R2) :
    cross q r x + cross r p x + cross p q x = cross p q r := by
  unfold cross; ring

lemma cross_bary (p q r x : R2) (k : Fin 2) :
    cross p q r * x k = cross q r x * p k + cross r p x * q k + cross p q x * r k := by
  fin_cases k <;> (unfold cross; simp; ring)

lemma cross_rot (p q r : R2) : cross q r p = cross p q r := by unfold cross; ring

lemma cross_self_left (p x : R2) : cross p p x = 0 := by unfold cross; ring

lemma cross_left (p q : R2) : cross p q p = 0 := by unfold cross; ring

lemma cross_right (p q : R2) : cross p q q = 0 := by unfold cross; ring

lemma cross_swap (p q x : R2) : cross q p x = -cross p q x := by unfold cross; ring

/-- `cross a b` is affine. -/
lemma cross_lineMap (a b x y : R2) (s t : ℝ) (h : s + t = 1) :
    cross a b (s • x + t • y) = s * cross a b x + t * cross a b y := by
  have : s = 1 - t := by linarith
  subst this
  unfold cross; simp; ring

lemma cross_combo (a b p q r : R2) (α β γ : ℝ) (h : α + β + γ = 1) :
    cross a b (α • p + β • q + γ • r) = α * cross a b p + β * cross a b q + γ * cross a b r := by
  have : γ = 1 - α - β := by linarith
  subst this
  unfold cross; simp; ring

/-- The barycentric representation. -/
lemma bary_eq {p q r x : R2} (hD : cross p q r ≠ 0) :
    x = (cross q r x / cross p q r) • p + (cross r p x / cross p q r) • q +
      (cross p q x / cross p q r) • r := by
  funext k
  have := cross_bary p q r x k
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  field_simp
  linarith

/-- **The closed triangle by signs of cross products.** -/
theorem mem_convexHull_triple_iff {p q r x : R2} (hD : cross p q r ≠ 0) :
    x ∈ convexHull ℝ {p, q, r} ↔ 0 ≤ cross q r x * cross p q r ∧
      0 ≤ cross r p x * cross p q r ∧ 0 ≤ cross p q x * cross p q r := by
  constructor
  · intro hx
    set S := {x : R2 | 0 ≤ cross q r x * cross p q r ∧ 0 ≤ cross r p x * cross p q r ∧
      0 ≤ cross p q x * cross p q r}
    have hS : Convex ℝ S := by
      intro x hx y hy s t hs ht hst
      simp only [S, mem_setOf_eq, cross_lineMap _ _ _ _ _ _ hst] at hx hy ⊢
      refine ⟨?_, ?_, ?_⟩ <;> nlinarith [hx.1, hx.2.1, hx.2.2, hy.1, hy.2.1, hy.2.2]
    have hsub : ({p, q, r} : Set R2) ⊆ S := by
      intro y hy
      simp only [mem_insert_iff, mem_singleton_iff] at hy
      have hD2 : 0 ≤ cross p q r * cross p q r := mul_self_nonneg _
      rcases hy with rfl | rfl | rfl
      · refine ⟨by rw [cross_rot]; exact hD2, by rw [cross_right]; simp,
          by rw [cross_left]; simp⟩
      · refine ⟨by rw [cross_left]; simp, by rw [cross_rot, cross_rot]; exact hD2,
          by rw [cross_right]; simp⟩
      · exact ⟨by rw [cross_right]; simp, by rw [cross_left]; simp, hD2⟩
    exact convexHull_min hsub hS hx
  · rintro ⟨h1, h2, h3⟩
    set D := cross p q r
    have hD2 : 0 < D * D := mul_self_pos.mpr hD
    set α := cross q r x / D
    set β := cross r p x / D
    set γ := cross p q x / D
    have hα : 0 ≤ α := by
      have : α = cross q r x * D / (D * D) := by simp only [α]; field_simp
      rw [this]; exact div_nonneg h1 hD2.le
    have hβ : 0 ≤ β := by
      have : β = cross r p x * D / (D * D) := by simp only [β]; field_simp
      rw [this]; exact div_nonneg h2 hD2.le
    have hγ : 0 ≤ γ := by
      have : γ = cross p q x * D / (D * D) := by simp only [γ]; field_simp
      rw [this]; exact div_nonneg h3 hD2.le
    have hsum : α + β + γ = 1 := by
      simp only [α, β, γ]
      field_simp
      linarith [cross_cyclic_sum p q r x]
    have hx : x = α • p + β • q + γ • r := bary_eq hD
    have hP : p ∈ convexHull ℝ ({p, q, r} : Set R2) := subset_convexHull ℝ _ (by simp)
    by_cases hα1 : α = 1
    · have hβ0 : β = 0 := by linarith
      have hγ0 : γ = 0 := by linarith
      rw [hx, hα1, hβ0, hγ0]
      simpa using hP
    · have hbg : 0 < β + γ := by
        rcases lt_or_eq_of_le (show α ≤ 1 by linarith) with h | h
        · linarith
        · exact absurd h hα1
      have hy : (β / (β + γ)) • q + (γ / (β + γ)) • r ∈ convexHull ℝ ({p, q, r} : Set R2) :=
        segment_subset_convexHull (by simp) (by simp)
          ⟨β / (β + γ), γ / (β + γ), div_nonneg hβ hbg.le, div_nonneg hγ hbg.le,
            by field_simp, rfl⟩
      have := convex_convexHull ℝ ({p, q, r} : Set R2) hP hy hα hbg.le (by linarith)
      convert this using 1
      rw [hx, smul_add, smul_smul, smul_smul, mul_div_cancel₀ _ hbg.ne',
        mul_div_cancel₀ _ hbg.ne', add_assoc]

/-- A point of the triangle with `cross p q x = 0` lies on the side `[p, q]`. -/
theorem mem_segment_of_mem_convexHull_of_cross {p q r x : R2} (hD : cross p q r ≠ 0)
    (hx : x ∈ convexHull ℝ {p, q, r}) (h0 : cross p q x = 0) : x ∈ segment ℝ p q := by
  obtain ⟨h1, h2, -⟩ := (mem_convexHull_triple_iff hD).mp hx
  set D := cross p q r
  have hD2 : 0 < D * D := mul_self_pos.mpr hD
  have hsum := cross_cyclic_sum p q r x
  rw [h0, add_zero] at hsum
  refine ⟨cross q r x / D, cross r p x / D, ?_, ?_, ?_, ?_⟩
  · have : cross q r x / D = cross q r x * D / (D * D) := by field_simp
    rw [this]; exact div_nonneg h1 hD2.le
  · have : cross r p x / D = cross r p x * D / (D * D) := by field_simp
    rw [this]; exact div_nonneg h2 hD2.le
  · rw [← add_div, hsum, div_self hD]
  · have := bary_eq (x := x) hD
    rw [h0, zero_div, zero_smul, add_zero] at this
    exact this.symm

/-! ### Triangles as polygons -/

/-- The triangle `p, q, r` as a polygon. -/
def triPoly (p q r : R2) : Polygon R2 := ⟨2, le_rfl, ![p, q, r]⟩

lemma triPoly_range (p q r : R2) : range (triPoly p q r).v = {p, q, r} := by
  simp only [triPoly, Matrix.range_cons, Matrix.range_empty, union_empty, singleton_union]

lemma triPoly_carrier (p q r : R2) :
    (triPoly p q r).carrier = segment ℝ p q ∪ segment ℝ q r ∪ segment ℝ r p := by
  rw [Polygon.carrier_eq_biUnion]
  simp only [triPoly, Finset.range_add_one, Finset.range_zero, insert_empty_eq,
    Finset.set_biUnion_insert, Finset.set_biUnion_singleton]
  simp only [Polygon.seg, Polygon.w]
  ext x
  simp [union_comm, union_left_comm]

/-- **A simple triangle is not degenerate.** -/
theorem cross_ne_zero_of_isSimple {Q : Polygon R2} (hQ : Q.IsSimple) (h2 : Q.n = 2) :
    cross (Q.w 0) (Q.w 1) (Q.w 2) ≠ 0 := by
  intro hc
  set p := Q.w 0
  set q := Q.w 1
  set r := Q.w 2
  have hpq : p ≠ q := fun h => by have := hQ.w_injOn (by omega) (by omega) h; omega
  -- `r` is on the line through `p` and `q`
  obtain ⟨t, ht⟩ : ∃ t : ℝ, r = p + t • (q - p) := by
    by_cases hd0 : q 0 - p 0 = 0
    · have hd1 : q 1 - p 1 ≠ 0 := by
        intro h1; apply hpq; funext k; fin_cases k
        · show p 0 = q 0; linarith
        · show p 1 = q 1; linarith
      refine ⟨(r 1 - p 1) / (q 1 - p 1), ?_⟩
      unfold cross at hc
      rw [hd0, zero_mul, zero_sub, neg_eq_zero] at hc
      have hr0 : r 0 = p 0 := by
        rcases mul_eq_zero.mp hc with h | h
        · exact absurd h hd1
        · linarith
      funext k; fin_cases k
      · simp; rw [hd0]; simp [hr0]
      · simp; field_simp; ring
    · refine ⟨(r 0 - p 0) / (q 0 - p 0), ?_⟩
      unfold cross at hc
      funext k; fin_cases k
      · simp; field_simp; ring
      · simp; field_simp; linarith
  have hw3 : Q.w 3 = p := by
    have h := Q.w_period
    have h3 : Q.n + 1 = 3 := by omega
    rwa [h3] at h
  have hseg := fun k (hk : k ≤ 2) j (hj : j ≤ 2) => @Polygon.IsSimple.w_mem_seg _ _ _ Q hQ j k
    (by omega) (by omega)
  rcases le_or_gt t 0 with ht0 | ht0
  · -- `p` lies on `[q, r]` (edge 1)
    have hmem : p ∈ Q.seg 1 := by
      show p ∈ segment ℝ q r
      by_cases ht1 : t = 0
      · subst ht1; simp at ht; rw [ht]; exact right_mem_segment ℝ q p
      have h1t : (1 - t) ≠ 0 := (show (0 : ℝ) < 1 - t by linarith).ne'
      refine ⟨-t / (1 - t), 1 / (1 - t), div_nonneg (by linarith) (by linarith),
        div_nonneg zero_le_one (by linarith), by field_simp; ring, ?_⟩
      rw [ht]; funext k; simp; field_simp; ring
    rcases hseg 1 (by omega) 0 (by omega) hmem with h | h <;> simp [h2] at h
  · rcases le_or_gt t 1 with ht1 | ht1
    · -- `r` lies on `[p, q]` (edge 0)
      have hmem : r ∈ Q.seg 0 := by
        show r ∈ segment ℝ p q
        refine ⟨1 - t, t, by linarith, ht0.le, by ring, ?_⟩
        rw [ht]; funext k; simp; ring
      rcases hseg 0 (by omega) 2 (by omega) hmem with h | h <;> simp [h2] at h
    · -- `q` lies on `[r, p]` (edge 2)
      have hmem : q ∈ Q.seg 2 := by
        show q ∈ segment ℝ r (Q.w 3)
        rw [hw3]
        refine ⟨1 / t, 1 - 1 / t, by positivity, ?_, by ring, ?_⟩
        · rw [sub_nonneg, div_le_one ht0]; exact ht1.le
        · rw [ht]; funext k; simp; field_simp; ring
      rcases hseg 2 (by omega) 1 (by omega) hmem with h | h <;> simp [h2] at h

lemma triPoly_parity (p q r x : R2) :
    (triPoly p q r).parity x = crossInd p q x + crossInd q r x + crossInd r p x := by
  unfold Polygon.parity
  change (∑ i : Fin 3, crossInd ((triPoly p q r).v i)
    ((triPoly p q r).v ((triPoly p q r).next i)) x) = _
  rw [Fin.sum_univ_three]
  rfl

lemma triPoly_parity_rot (p q r x : R2) :
    (triPoly q r p).parity x = (triPoly p q r).parity x := by
  rw [triPoly_parity, triPoly_parity]; abel

lemma triPoly_carrier_rot (p q r : R2) :
    (triPoly q r p).carrier = (triPoly p q r).carrier := by
  rw [triPoly_carrier, triPoly_carrier, union_comm, union_assoc]

lemma cross_rot2 (p q r : R2) : cross r p q = cross p q r := by unfold cross; ring

lemma triple_rot (p q r : R2) : ({q, r, p} : Set R2) = {p, q, r} := by
  ext y; simp only [mem_insert_iff, mem_singleton_iff]; tauto

/-- Moving vertically by less than the distance to the line does not change `crossInd`. -/
lemma crossInd_add_sub_e1 {a b m : R2} (hc : cross a b m ≠ 0) {s : ℝ} (hs : 0 ≤ s)
    (hsm : |b 0 - a 0| * s < |cross a b m|) :
    crossInd a b (m + s • e1) = crossInd a b (m - s • e1) := by
  have h1 : (m + s • e1) 0 = m 0 := by simp
  have h2 : (m - s • e1) 0 = m 0 := by simp
  have h3 : cross a b (m - s • e1) = cross a b m + (b 0 - a 0) * (-s) := by
    rw [sub_eq_add_neg, ← neg_smul]; exact cross_add_smul_e1 a b m (-s)
  unfold crossInd
  rw [h1, h2, cross_add_smul_e1, h3]
  congr 1
  apply propext
  set c := cross a b m
  set d := b 0 - a 0
  by_cases hd : d = 0
  · simp [hd]
  have hdpos : 0 < |d| := abs_pos.mpr hd
  have key : d ^ 2 * s < |c * d| := by
    rw [abs_mul, show d ^ 2 = |d| * |d| by rw [abs_mul_abs_self, sq]]
    have := mul_lt_mul_of_pos_right hsm hdpos
    nlinarith [abs_nonneg d]
  have hs2 : 0 ≤ d ^ 2 * s := by positivity
  rcases lt_trichotomy (c * d) 0 with hn | hz | hp
  · rw [abs_of_neg hn] at key
    constructor <;> rintro ⟨hx, -⟩ <;> refine ⟨hx, ?_⟩ <;> nlinarith
  · exact absurd hz (mul_ne_zero hc hd)
  · rw [abs_of_pos hp] at key
    constructor <;> rintro ⟨-, h⟩ <;> nlinarith

lemma pos_combo {X Y a b : ℝ} (hX : 0 < X) (hY : 0 < Y) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hab : a + b = 1) : 0 < a * X + b * Y := by
  rcases eq_or_lt_of_le ha with h | h
  · subst h; simp at hab; subst hab; simpa using hY
  · nlinarith [mul_nonneg hb hY.le]

/-- The open triangle. -/
def openTri (p q r : R2) : Set R2 :=
  {y | 0 < cross q r y * cross p q r ∧ 0 < cross r p y * cross p q r ∧
    0 < cross p q y * cross p q r}

lemma convex_openTri (p q r : R2) : Convex ℝ (openTri p q r) := by
  intro y hy z hz a b ha hb hab
  have e : ∀ u v : R2, cross u v (a • y + b • z) * cross p q r =
      a * (cross u v y * cross p q r) + b * (cross u v z * cross p q r) := by
    intro u v; rw [cross_lineMap u v y z a b hab]; ring
  exact ⟨by rw [e]; exact pos_combo hy.1 hz.1 ha hb hab,
    by rw [e]; exact pos_combo hy.2.1 hz.2.1 ha hb hab,
    by rw [e]; exact pos_combo hy.2.2 hz.2.2 ha hb hab⟩

lemma openTri_rot (p q r : R2) : openTri q r p = openTri p q r := by
  ext y; simp only [openTri, mem_setOf_eq, cross_rot p q r]; tauto

lemma disjoint_openTri (p q r : R2) : Disjoint (openTri p q r) (triPoly p q r).carrier := by
  rw [Set.disjoint_left, triPoly_carrier]
  rintro y ⟨h1, h2, h3⟩ ((hy | hy) | hy)
  · rw [cross_of_mem_segment hy] at h3; simp at h3
  · rw [cross_of_mem_segment hy] at h1; simp at h1
  · rw [cross_of_mem_segment hy] at h2; simp at h2

lemma mem_openTri {p q r : R2} (hD : cross p q r ≠ 0) {x : R2}
    (hx : x ∈ convexHull ℝ {p, q, r}) (hxc : x ∉ (triPoly p q r).carrier) :
    x ∈ openTri p q r := by
  obtain ⟨h1, h2, h3⟩ := (mem_convexHull_triple_iff hD).mp hx
  rw [triPoly_carrier] at hxc
  have hD1 : cross q r p ≠ 0 := by rwa [cross_rot]
  have hD2 : cross r p q ≠ 0 := by rw [cross_rot2]; exact hD
  refine ⟨lt_of_le_of_ne h1 fun h => ?_, lt_of_le_of_ne h2 fun h => ?_,
    lt_of_le_of_ne h3 fun h => ?_⟩
  · have h0 : cross q r x = 0 := by
      rcases mul_eq_zero.mp h.symm with h | h
      · exact h
      · exact absurd h hD
    exact hxc (Or.inl (Or.inr (mem_segment_of_mem_convexHull_of_cross hD1
      (by rw [triple_rot]; exact hx) h0)))
  · have h0 : cross r p x = 0 := by
      rcases mul_eq_zero.mp h.symm with h | h
      · exact h
      · exact absurd h hD
    exact hxc (Or.inr (mem_segment_of_mem_convexHull_of_cross hD2
      (by rw [← triple_rot r p q]; exact hx) h0))
  · have h0 : cross p q x = 0 := by
      rcases mul_eq_zero.mp h.symm with h | h
      · exact h
      · exact absurd h hD
    exact hxc (Or.inl (Or.inl (mem_segment_of_mem_convexHull_of_cross hD hx h0)))

/-- The interior case when the side `[p, q]` is not vertical. -/
lemma triPoly_parity_eq_one_aux {p q r : R2} (hD : cross p q r ≠ 0) (hpq : p 0 ≠ q 0)
    {x : R2} (hx : x ∈ openTri p q r) : (triPoly p q r).parity x = 1 := by
  obtain ⟨m, hm⟩ : ∃ m : R2, m = (1 / 2 : ℝ) • p + (1 / 2 : ℝ) • q := ⟨_, rfl⟩
  have hm1 : cross q r m = cross p q r / 2 := by
    rw [hm, cross_lineMap q r p q _ _ (by norm_num), cross_left, cross_rot p q r]; ring
  have hm2 : cross r p m = cross p q r / 2 := by
    rw [hm, cross_lineMap r p p q _ _ (by norm_num), cross_right, cross_rot2]; ring
  have hm3 : cross p q m = 0 := by
    rw [hm, cross_lineMap p q p q _ _ (by norm_num), cross_left, cross_right]; ring
  have hm0 : m 0 = (p 0 + q 0) / 2 := by rw [hm]; simp; ring
  have hDa : 0 < |cross p q r| := abs_pos.mpr hD
  have hK : 0 < |r 0 - q 0| + |p 0 - r 0| + 1 := by positivity
  obtain ⟨s, hsdef⟩ : ∃ s : ℝ, s = |cross p q r| / (4 * (|r 0 - q 0| + |p 0 - r 0| + 1)) :=
    ⟨_, rfl⟩
  have hs : 0 < s := by rw [hsdef]; positivity
  have hKs : |r 0 - q 0| * s + |p 0 - r 0| * s + s = |cross p q r| / 4 := by
    rw [hsdef]; field_simp
  have ha1 := mul_nonneg (abs_nonneg (r 0 - q 0)) hs.le
  have ha2 := mul_nonneg (abs_nonneg (p 0 - r 0)) hs.le
  have hb1 : |r 0 - q 0| * s < |cross q r m| := by
    rw [hm1, abs_div, abs_two]; linarith
  have hb2 : |p 0 - r 0| * s < |cross r p m| := by
    rw [hm2, abs_div, abs_two]; linarith
  have hc1 : cross q r m ≠ 0 := by rw [hm1]; exact div_ne_zero hD two_ne_zero
  have hc2 : cross r p m ≠ 0 := by rw [hm2]; exact div_ne_zero hD two_ne_zero
  -- crossing the side `[p, q]` from `m - s e1` to `m + s e1`
  have hpq' : q 0 - p 0 ≠ 0 := sub_ne_zero.mpr (Ne.symm hpq)
  have hxor : Xor' (p 0 ≤ m 0) (q 0 ≤ m 0) := by
    rw [hm0]
    rcases lt_or_gt_of_ne hpq with h | h
    · left; exact ⟨by linarith, fun h' => by linarith⟩
    · right; exact ⟨by linarith, fun h' => by linarith⟩
  have h2e : (m - s • e1) 0 = m 0 := by simp
  have hcp : cross p q (m + s • e1) = (q 0 - p 0) * s := by
    rw [cross_add_smul_e1, hm3, zero_add]
  have hcm : cross p q (m - s • e1) = -((q 0 - p 0) * s) := by
    rw [sub_eq_add_neg, ← neg_smul, cross_add_smul_e1, hm3]; ring
  have hsq : 0 < (q 0 - p 0) * s * (q 0 - p 0) := by
    rw [show (q 0 - p 0) * s * (q 0 - p 0) = (q 0 - p 0) * (q 0 - p 0) * s by ring]
    exact mul_pos (mul_self_pos.mpr hpq') hs
  have hip : crossInd p q (m + s • e1) = 0 := by
    unfold crossInd; rw [if_neg]; rintro ⟨-, h⟩; rw [hcp] at h; linarith
  have him : crossInd p q (m - s • e1) = 1 := by
    unfold crossInd; rw [if_pos]; refine ⟨by rw [h2e]; exact hxor, ?_⟩
    rw [hcm]; linarith
  have hflip : (triPoly p q r).parity (m - s • e1) =
      (triPoly p q r).parity (m + s • e1) + 1 := by
    rw [triPoly_parity, triPoly_parity, hip, him,
      crossInd_add_sub_e1 hc1 hs.le hb1, crossInd_add_sub_e1 hc2 hs.le hb2]
    ring
  -- the two points `m ± s e1`: the other two signs are those of `cross p q r`
  have hsgn : ∀ X : ℝ, |X| < |cross p q r| / 2 → 0 < (cross p q r / 2 + X) * cross p q r := by
    intro X hX
    have h := abs_lt.mp hX
    rcases lt_or_gt_of_ne hD with hn | hp
    · rw [abs_of_neg hn] at h; exact mul_pos_of_neg_of_neg (by linarith) hn
    · rw [abs_of_pos hp] at h; exact mul_pos (by linarith) hp
  have hq1 : ∀ u : ℝ, |u| ≤ s → 0 < cross q r (m + u • e1) * cross p q r := by
    intro u hu
    rw [cross_add_smul_e1, hm1]
    apply hsgn
    rw [abs_mul]
    calc |r 0 - q 0| * |u| ≤ |r 0 - q 0| * s := by gcongr
      _ < _ := by linarith
  have hq2 : ∀ u : ℝ, |u| ≤ s → 0 < cross r p (m + u • e1) * cross p q r := by
    intro u hu
    rw [cross_add_smul_e1, hm2]
    apply hsgn
    rw [abs_mul]
    calc |p 0 - r 0| * |u| ≤ |p 0 - r 0| * s := by gcongr
      _ < _ := by linarith
  have hsabs : |s| ≤ s := (abs_of_pos hs).le
  have hnsabs : |-s| ≤ s := by rw [abs_neg]; exact hsabs
  have hms : m - s • e1 = m + (-s) • e1 := by rw [neg_smul, ← sub_eq_add_neg]
  have hconst : ∀ y ∈ openTri p q r, (triPoly p q r).parity x = (triPoly p q r).parity y :=
    fun y hy => (triPoly p q r).parity_const_of_isPreconnected
      (convex_openTri p q r).isPreconnected (disjoint_openTri p q r) hx hy
  have hout : ∀ y, cross p q y * cross p q r < 0 → (triPoly p q r).parity y = 0 := by
    intro y hy
    apply Polygon.parity_eq_zero_of_not_mem_convexHull
    rw [triPoly_range, mem_convexHull_triple_iff hD]
    rintro ⟨-, -, h⟩; linarith
  rcases lt_or_gt_of_ne (mul_ne_zero (mul_ne_zero hpq' hs.ne') hD) with hneg | hpos
  · -- `m - s e1` is inside, `m + s e1` is outside
    have hin : m - s • e1 ∈ openTri p q r := by
      refine ⟨?_, ?_, ?_⟩
      · rw [hms]; exact hq1 _ hnsabs
      · rw [hms]; exact hq2 _ hnsabs
      · rw [hcm]; linarith
    rw [hconst _ hin, hflip, hout _ (by rw [hcp]; exact hneg), zero_add]
  · -- `m + s e1` is inside, `m - s e1` is outside
    have hin : m + s • e1 ∈ openTri p q r :=
      ⟨hq1 _ hsabs, hq2 _ hsabs, by rw [hcp]; exact hpos⟩
    have h0 := hout _ (by rw [hcm]; linarith)
    rw [hflip] at h0
    rw [hconst _ hin]
    calc (triPoly p q r).parity (m + s • e1)
        = (triPoly p q r).parity (m + s • e1) + 1 + 1 := by
          rw [add_assoc, CharTwo.add_self_eq_zero, add_zero]
      _ = 1 := by rw [h0, zero_add]

/-- **The inside of a non-degenerate triangle has crossing parity `1`.** -/
theorem triPoly_parity_eq_one {p q r : R2} (hD : cross p q r ≠ 0) {x : R2}
    (hx : x ∈ convexHull ℝ {p, q, r}) (hxc : x ∉ (triPoly p q r).carrier) :
    (triPoly p q r).parity x = 1 := by
  have hI := mem_openTri hD hx hxc
  by_cases h1 : p 0 = q 0
  · by_cases h2 : q 0 = r 0
    · have h3 : r 0 ≠ p 0 := by
        intro h3; apply hD; unfold cross; rw [h1, h2]; ring
      have hD' : cross r p q ≠ 0 := by rw [cross_rot2]; exact hD
      have hI' : x ∈ openTri r p q := by rw [openTri_rot q r p, openTri_rot p q r]; exact hI
      rw [← triPoly_parity_rot p q r, ← triPoly_parity_rot q r p]
      exact triPoly_parity_eq_one_aux hD' h3 hI'
    · have hD' : cross q r p ≠ 0 := by rw [cross_rot]; exact hD
      have hI' : x ∈ openTri q r p := by rw [openTri_rot p q r]; exact hI
      rw [← triPoly_parity_rot p q r]
      exact triPoly_parity_eq_one_aux hD' h2 hI'
  · exact triPoly_parity_eq_one_aux hD h1 hI

end QOU.MathlibExt.PL
