/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLMoveVertex
import QOU.MathlibExt.PLStability

set_option autoImplicit false

/-!
# Moving one vertex a little (issue #8902, isotopy-to-Δ bridge, local stability)

`PLMoveVertex.reaches_moveLast` moves the last vertex `v` of a component to `w` under pointwise
conditions on two buffer points `p ∈ (v, b)`, `q ∈ (a, v)`. This file shows those conditions hold
for every configuration near a simple one when `w` is near `v`: fix `p = v + r (b - v)`,
`q = v + r (a - v)` with a small fixed ratio `r`, and every condition becomes one of the
robust ones of `PLStability`.

## What is a THEOREM here

* `eq_zero_of_smul_eq_smul_of_not_sameRay` — the one piece of planar algebra used: two
  non-negative multiples of non-parallel vectors agree only when both are zero.
* `not_sameRay_of_isSimple` — at a vertex of a simple polygon the two edges are not parallel.
* `eventually_moveConds` — the conditions hold near a simple configuration.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

section Algebra

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- **Non-parallel vectors.** If `c • u = d • w` with `c, d ≥ 0`, `u, w ≠ 0` and `u, w` not on a
common ray, then `c = d = 0`. -/
theorem eq_zero_of_smul_eq_smul_of_not_sameRay {u w : E} (hu : u ≠ 0) (hw : w ≠ 0)
    (hns : ¬ SameRay ℝ u w) {c d : ℝ} (hc : 0 ≤ c) (hd : 0 ≤ d) (h : c • u = d • w) :
    c = 0 ∧ d = 0 := by
  rcases hc.eq_or_lt with rfl | hc
  · refine ⟨rfl, ?_⟩
    rw [zero_smul, eq_comm, smul_eq_zero] at h
    exact h.resolve_right hw
  · exfalso
    rcases hd.eq_or_lt with rfl | hd
    · rw [zero_smul, smul_eq_zero] at h
      exact hu (h.resolve_left hc.ne')
    · apply hns
      have : u = (d / c) • w := by
        rw [div_eq_inv_mul, mul_smul, ← h, smul_smul, inv_mul_cancel₀ hc.ne', one_smul]
      rw [this]
      exact SameRay.sameRay_nonneg_smul_left w (div_nonneg hd.le hc.le)

/-- The point at ratio `r` from `x` towards `y`. -/
def ratioPt (r : ℝ) (x y : E) : E := x + r • (y - x)

lemma ratioPt_mem_openSegment {r : ℝ} (hr0 : 0 < r) (hr1 : r < 1) (x y : E) :
    ratioPt r x y ∈ openSegment ℝ x y :=
  ⟨1 - r, r, by linarith, hr0, by ring, by simp only [ratioPt]; module⟩

lemma ratioPt_mem_segment {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1) (x y : E) :
    ratioPt r x y ∈ segment ℝ x y := by
  rw [segment_eq_image']; exact ⟨r, ⟨hr0, hr1⟩, rfl⟩

lemma ratioPt_ne_left {r : ℝ} (hr0 : 0 < r) {x y : E} (hxy : x ≠ y) : ratioPt r x y ≠ x := by
  intro h
  have : r • (y - x) = 0 := by simpa [ratioPt] using h
  rw [smul_eq_zero] at this
  rcases this with h | h
  · exact hr0.ne' h
  · exact hxy (sub_eq_zero.mp h).symm

/-- `x` is not on `[ratioPt r x y, y]` for `r > 0`. -/
lemma left_notMem_segment_ratioPt {r : ℝ} (hr0 : 0 < r) (hr1 : r ≤ 1) {x y : E}
    (hxy : x ≠ y) : x ∉ segment ℝ (ratioPt r x y) y := by
  rw [segment_eq_image']
  rintro ⟨θ, ⟨h0, h1⟩, h⟩
  simp only at h
  have e : (r + θ * (1 - r)) • (y - x) = 0 := by
    have : ratioPt r x y + θ • (y - ratioPt r x y) - x = 0 := by rw [h, sub_self]
    rw [← this]; simp only [ratioPt]; module
  rw [smul_eq_zero] at e
  rcases e with e | e
  · nlinarith
  · exact hxy (sub_eq_zero.mp e).symm

/-- `y` is not on `[x, ratioPt r x y]` for `r < 1`. -/
lemma right_notMem_segment_ratioPt {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r < 1) {x y : E}
    (hxy : x ≠ y) : y ∉ segment ℝ x (ratioPt r x y) := by
  rw [segment_eq_image']
  rintro ⟨θ, ⟨h0, h1⟩, h⟩
  simp only at h
  have e : (1 - θ * r) • (y - x) = 0 := by
    have : y - (x + θ • (ratioPt r x y - x)) = 0 := by rw [h, sub_self]
    rw [← this]; simp only [ratioPt]; module
  rw [smul_eq_zero] at e
  rcases e with e | e
  · nlinarith [mul_le_mul_of_nonneg_right h1 hr0]
  · exact hxy (sub_eq_zero.mp e).symm

lemma segment_ratioPt_subset {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1) (x y : E) :
    segment ℝ x (ratioPt r x y) ⊆ segment ℝ x y :=
  (convex_segment x y).segment_subset (left_mem_segment ℝ x y) (ratioPt_mem_segment hr0 hr1 x y)

lemma segment_ratioPt_subset' {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1) (x y : E) :
    segment ℝ (ratioPt r x y) y ⊆ segment ℝ x y :=
  (convex_segment x y).segment_subset (ratioPt_mem_segment hr0 hr1 x y) (right_mem_segment ℝ x y)

/-- **The corner triangle meets the edge `[q, a]` only at `q`.** Here `q`, `p` are at ratio
`r` from `v` towards `a`, `b`. -/
theorem segment_inter_cornerTriangle {r : ℝ} (hr0 : 0 < r) (hr1 : r < 1) {v a b : E}
    (ha : a - v ≠ 0) (hb : b - v ≠ 0) (hns : ¬ SameRay ℝ (a - v) (b - v)) :
    segment ℝ (ratioPt r v a) a ∩ convexHull ℝ {ratioPt r v a, ratioPt r v b, v} ⊆
      {ratioPt r v a} := by
  rintro z ⟨hz1, hz2⟩
  rw [segment_eq_image'] at hz1
  obtain ⟨θ, ⟨h0, h1⟩, rfl⟩ := hz1
  simp only at hz2 ⊢
  rw [show ({ratioPt r v a, ratioPt r v b, v} : Set E) = {v, ratioPt r v a, ratioPt r v b} by
    ext; simp only [mem_insert_iff, mem_singleton_iff]; tauto, convexHull_triple_eq_image] at hz2
  obtain ⟨⟨α, β⟩, ⟨hα, hβ, hαβ⟩, he⟩ := hz2
  simp only [triPt, ratioPt] at he
  have key : (r + θ * (1 - r) - α * r) • (a - v) = (β * r) • (b - v) := by
    have : v + α • (v + r • (a - v) - v) + β • (v + r • (b - v) - v) -
        (v + r • (a - v) + θ • (a - (v + r • (a - v)))) = 0 := by rw [he, sub_self]
    rw [← sub_eq_zero, ← neg_eq_zero, ← this]; module
  obtain ⟨e1, e2⟩ := eq_zero_of_smul_eq_smul_of_not_sameRay ha hb hns
    (by nlinarith) (by positivity) key
  have hθ : θ = 0 := by nlinarith
  subst hθ
  simp [ratioPt]

/-- **The buffer `q` is not on `[p, v]`.** -/
theorem ratioPt_notMem_segment {r : ℝ} (hr0 : 0 < r) {v a b : E}
    (ha : a - v ≠ 0) (hb : b - v ≠ 0) (hns : ¬ SameRay ℝ (a - v) (b - v)) :
    ratioPt r v a ∉ segment ℝ (ratioPt r v b) v := by
  rw [segment_eq_image']
  rintro ⟨θ, ⟨h0, h1⟩, h⟩
  simp only at h
  have key : r • (a - v) = ((1 - θ) * r) • (b - v) := by
    have : ratioPt r v b + θ • (v - ratioPt r v b) - ratioPt r v a = 0 := by rw [h, sub_self]
    rw [← sub_eq_zero, ← neg_eq_zero, ← this]; simp only [ratioPt]; module
  have := eq_zero_of_smul_eq_smul_of_not_sameRay ha hb hns hr0.le
    (mul_nonneg (by linarith) hr0.le) key
  exact hr0.ne' this.1

lemma ratioPt_ne_right {r : ℝ} (hr1 : r < 1) {x y : E} (hxy : x ≠ y) : ratioPt r x y ≠ y := by
  intro h
  have : (1 - r) • (y - x) = 0 := by
    rw [← neg_eq_zero, ← sub_eq_zero.mpr h]; simp only [ratioPt]; module
  rw [smul_eq_zero] at this
  rcases this with h | h
  · linarith
  · exact hxy (sub_eq_zero.mp h).symm

end Algebra

/-! ## The polygon around the moving vertex -/

section Corner

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- The polygon with `N + 3` vertices `V`. -/
def polyOf {N : ℕ} (V : Fin (N + 3) → E) : Polygon E := ⟨N + 2, by omega, V⟩

variable {N : ℕ} (V : Fin (N + 3) → E)

/-- Index of the vertex before the last, `a`. -/
def iA (N : ℕ) : Fin (N + 3) := (Fin.last (N + 1)).castSucc

lemma polyOf_next_iA : (polyOf V).next (iA N) = Fin.last (N + 2) := by
  have := (polyOf V).next_castSucc_lt (Fin.last (N + 1))
  simpa [iA] using this

lemma polyOf_next_last : (polyOf V).next (Fin.last (N + 2)) = 0 := (polyOf V).next_last

lemma polyOf_next_core (k : Fin (N + 1)) :
    (polyOf V).next k.castSucc.castSucc = k.succ.castSucc := by
  have := (polyOf V).next_castSucc_lt k.castSucc
  rw [this, Fin.succ_castSucc]

lemma polyOf_edge_iA : (polyOf V).edge (iA N) = segment ℝ (V (iA N)) (V (Fin.last (N + 2))) := by
  simp only [Polygon.edge, polyOf_next_iA]; rfl

lemma polyOf_edge_last : (polyOf V).edge (Fin.last (N + 2)) = segment ℝ (V (Fin.last (N + 2))) (V 0) := by
  simp only [Polygon.edge, polyOf_next_last]; rfl

lemma polyOf_edge_core (k : Fin (N + 1)) :
    (polyOf V).edge k.castSucc.castSucc = segment ℝ (V k.castSucc.castSucc) (V k.succ.castSucc) := by
  simp only [Polygon.edge, polyOf_next_core]; rfl

variable {V}

lemma iA_ne_last : iA N ≠ Fin.last (N + 2) := by
  simp [iA, Fin.ext_iff]

lemma last_ne_zero' : Fin.last (N + 2) ≠ 0 := by
  simp [Fin.ext_iff]

lemma iA_ne_zero : iA N ≠ 0 := by
  simp [iA, Fin.ext_iff]

lemma core_ne_last (k : Fin (N + 1)) : k.castSucc.castSucc ≠ Fin.last (N + 2) := by
  simp [Fin.ext_iff]; omega

lemma core_ne_iA (k : Fin (N + 1)) : k.castSucc.castSucc ≠ iA N := by
  simp [iA, Fin.ext_iff]; omega

/-- The two edges at the moving vertex meet only there. -/
lemma corner_adj (hP : (polyOf V).IsSimple) :
    segment ℝ (V (iA N)) (V (Fin.last (N + 2))) ∩ segment ℝ (V (Fin.last (N + 2))) (V 0) =
      {V (Fin.last (N + 2))} := by
  have := hP.adj (iA N)
  rwa [polyOf_next_iA, polyOf_edge_iA, polyOf_edge_last] at this

/-- The closing edge meets the first core edge only at `V 0`. -/
lemma corner_adj_zero (hP : (polyOf V).IsSimple) :
    segment ℝ (V (Fin.last (N + 2))) (V 0) ∩ segment ℝ (V 0) (V 1) = {V 0} := by
  have := hP.adj (Fin.last (N + 2))
  rw [polyOf_next_last, polyOf_edge_last] at this
  have h0 := polyOf_edge_core V 0
  simp only [Fin.castSucc_zero, Fin.succ_zero_eq_one, Fin.castSucc_one] at h0
  rwa [h0] at this

/-- The last core edge meets `[a, v]` only at `a`. -/
lemma corner_adj_core (hP : (polyOf V).IsSimple) :
    segment ℝ (V (Fin.last N).castSucc.castSucc) (V (iA N)) ∩
      segment ℝ (V (iA N)) (V (Fin.last (N + 2))) = {V (iA N)} := by
  have := hP.adj (Fin.last N).castSucc.castSucc
  have e : (Fin.last N).succ.castSucc = iA N := by simp [iA]
  rwa [polyOf_next_core, polyOf_edge_core, e, polyOf_edge_iA] at this

lemma corner_disj_iA (hP : (polyOf V).IsSimple) {k : Fin (N + 1)} (hk : k ≠ Fin.last N) :
    Disjoint (segment ℝ (V k.castSucc.castSucc) (V k.succ.castSucc))
      (segment ℝ (V (iA N)) (V (Fin.last (N + 2)))) := by
  rw [← polyOf_edge_core, ← polyOf_edge_iA]
  refine hP.disj (core_ne_iA k) ?_ ?_
  · rw [polyOf_next_core]
    simp [iA, Fin.ext_iff]
    intro h; exact hk (Fin.ext (by simp; omega))
  · rw [polyOf_next_iA]; exact core_ne_last k

lemma corner_disj_last (hP : (polyOf V).IsSimple) {k : Fin (N + 1)} (hk : k ≠ 0) :
    Disjoint (segment ℝ (V k.castSucc.castSucc) (V k.succ.castSucc))
      (segment ℝ (V (Fin.last (N + 2))) (V 0)) := by
  rw [← polyOf_edge_core, ← polyOf_edge_last]
  refine hP.disj (core_ne_last k) ?_ ?_
  · rw [polyOf_next_core]; simp [Fin.ext_iff]; omega
  · rw [polyOf_next_last]
    intro h; exact hk (Fin.ext (by have := congrArg Fin.val h; simpa using this))

lemma corner_v_notMem_core (hP : (polyOf V).IsSimple) (k : Fin (N + 1)) :
    V (Fin.last (N + 2)) ∉ segment ℝ (V k.castSucc.castSucc) (V k.succ.castSucc) := by
  rw [← polyOf_edge_core]
  intro h
  rcases hP.eq_or_next_eq_of_v_mem_edge (P := polyOf V) h with h | h
  · exact core_ne_last k h
  · rw [polyOf_next_core] at h; simp [Fin.ext_iff] at h; omega

lemma corner_ne (hP : (polyOf V).IsSimple) {i j : Fin (N + 3)} (h : i ≠ j) : V i ≠ V j :=
  fun e => h (hP.1 e)

/-- **The edges at the moving vertex are not parallel.** -/
theorem corner_not_sameRay (hP : (polyOf V).IsSimple) :
    ¬ SameRay ℝ (V (iA N) - V (Fin.last (N + 2))) (V 0 - V (Fin.last (N + 2))) := by
  set a := V (iA N); set v := V (Fin.last (N + 2)); set b := V 0
  have hav : a ≠ v := corner_ne hP iA_ne_last
  have hbv : b ≠ v := corner_ne hP last_ne_zero'.symm
  have hab : a ≠ b := corner_ne hP iA_ne_zero
  intro hs
  obtain ⟨r₁, r₂, h1, h2, he⟩ := hs.exists_pos (sub_ne_zero.mpr hav) (sub_ne_zero.mpr hbv)
  have hadj := corner_adj hP
  rcases le_total r₂ r₁ with h | h
  · -- `a` lies on `[v, b]`
    have ha : a ∈ segment ℝ v b := by
      rw [segment_eq_image']
      refine ⟨r₂ / r₁, ⟨by positivity, (div_le_one h1).mpr h⟩, ?_⟩
      have : a - v = (r₂ / r₁) • (b - v) := by
        rw [div_eq_inv_mul, mul_smul, ← he, smul_smul, inv_mul_cancel₀ h1.ne', one_smul]
      simp only; rw [← this]; abel
    have : a ∈ ({v} : Set E) := hadj ▸ ⟨left_mem_segment ℝ _ _, ha⟩
    exact hav this
  · -- `b` lies on `[a, v]`
    have hb : b ∈ segment ℝ a v := by
      rw [segment_symm, segment_eq_image']
      refine ⟨r₁ / r₂, ⟨by positivity, (div_le_one h2).mpr h⟩, ?_⟩
      have : b - v = (r₁ / r₂) • (a - v) := by
        rw [div_eq_inv_mul, mul_smul, he, smul_smul, inv_mul_cancel₀ h2.ne', one_smul]
      simp only; rw [← this]; abel
    have : b ∈ ({v} : Set E) := hadj ▸ ⟨hb, right_mem_segment ℝ _ _⟩
    exact hbv this

end Corner

end QOU.MathlibExt.PL
