/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLMoveVertex
import BraidKnotOctonion.PLStability

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

/-! ## The conditions near a simple configuration -/

section Near

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- The pointwise conditions of `PolygonalLink.reaches_moveLast`, with `RR` the path `b … a`
together with the other components. -/
structure MoveConds (RR : Set E) (a b v w p q : E) : Prop where
  hp : p ∈ openSegment ℝ v b
  hq : q ∈ openSegment ℝ a v
  hcut : convexHull ℝ {q, p, v} ∩ (RR ∪ segment ℝ a q ∪ segment ℝ p b) ⊆ {q, p}
  hwq : w ≠ q
  hwp : w ≠ p
  hwseg : segment ℝ q w ∩ segment ℝ w p ⊆ {w}
  hins : convexHull ℝ {q, p, w} ∩ (RR ∪ segment ℝ a q ∪ segment ℝ p b) ⊆ {q, p}
  hdq : convexHull ℝ {a, w, q} ∩ (RR ∪ segment ℝ w p ∪ segment ℝ p b) ⊆ {a, w}
  hdp : convexHull ℝ {w, b, p} ∩ (RR ∪ segment ℝ a w) ⊆ {w, b}

variable {X : Type*} [TopologicalSpace X] {x₀ : X}

lemma continuous_ratioPt (r : ℝ) {f g : X → E} (hf : Continuous f) (hg : Continuous g) :
    Continuous fun x => ratioPt r (f x) (g x) := by
  simp only [ratioPt]; fun_prop

/-- The edges `[V k, V (k+1)]`, `k ≤ N`, of the path from `b = V 0` to `a = V (N + 1)`. -/
def coreSet {N : ℕ} (V : Fin (N + 3) → E) : Set E :=
  ⋃ k : Fin (N + 1), segment ℝ (V k.castSucc.castSucc) (V k.succ.castSucc)

/-- **Choosing the buffer ratio.** For small `r` the corner triangle at `v` misses the path
`b … a` and any compact family of segments avoiding `v`. -/
theorem exists_ratio {N : ℕ} {V : Fin (N + 3) → E} (hP : (polyOf V).IsSimple)
    {J : Type*} [Finite J] (s t : J → E) (hR : ∀ j, V (Fin.last (N + 2)) ∉ segment ℝ (s j) (t j)) :
    ∃ r, 0 < r ∧ r < 1 ∧
      (∀ k : Fin (N + 1), segment ℝ (V k.castSucc.castSucc) (V k.succ.castSucc) ∩
        convexHull ℝ {ratioPt r (V (Fin.last (N + 2))) (V (iA N)),
          ratioPt r (V (Fin.last (N + 2))) (V 0), V (Fin.last (N + 2))} = ∅) ∧
      (∀ j, segment ℝ (s j) (t j) ∩
        convexHull ℝ {ratioPt r (V (Fin.last (N + 2))) (V (iA N)),
          ratioPt r (V (Fin.last (N + 2))) (V 0), V (Fin.last (N + 2))} = ∅) := by
  set v := V (Fin.last (N + 2))
  have hq : Continuous fun r : ℝ => ratioPt r v (V (iA N)) := by simp only [ratioPt]; fun_prop
  have hp : Continuous fun r : ℝ => ratioPt r v (V 0) := by simp only [ratioPt]; fun_prop
  have base : ∀ S : Set E, v ∉ S → S ∩ convexHull ℝ {ratioPt 0 v (V (iA N)),
      ratioPt 0 v (V 0), v} = ∅ := by
    intro S hS
    simp only [ratioPt, zero_smul, add_zero, mem_singleton_iff, insert_eq_of_mem,
      convexHull_singleton]
    exact eq_empty_iff_forall_notMem.mpr fun z ⟨hz, hz'⟩ => hS (hz' ▸ hz)
  have e1 : ∀ k : Fin (N + 1), ∀ᶠ r in 𝓝 (0 : ℝ), segment ℝ (V k.castSucc.castSucc)
      (V k.succ.castSucc) ∩ convexHull ℝ {ratioPt r v (V (iA N)), ratioPt r v (V 0), v} = ∅ :=
    fun k => eventually_segment_inter_convexHull_eq_empty (x₀ := (0 : ℝ))
      continuous_const continuous_const hq hp continuous_const
      (base _ (corner_v_notMem_core hP k))
  have e2 : ∀ j, ∀ᶠ r in 𝓝 (0 : ℝ), segment ℝ (s j) (t j) ∩
      convexHull ℝ {ratioPt r v (V (iA N)), ratioPt r v (V 0), v} = ∅ :=
    fun j => eventually_segment_inter_convexHull_eq_empty (x₀ := (0 : ℝ))
      continuous_const continuous_const hq hp continuous_const (base _ (hR j))
  obtain ⟨ε, hε, hεP⟩ := Metric.eventually_nhds_iff.mp
    ((Filter.eventually_all.mpr e1).and (Filter.eventually_all.mpr e2))
  refine ⟨min (ε / 2) (1 / 2), by positivity, by
    have := min_le_right (ε / 2) (1 / 2); linarith, hεP ?_⟩
  rw [Real.dist_eq, sub_zero, abs_of_pos (by positivity)]
  have := min_le_left (ε / 2) (1 / 2); linarith

/-- **The conditions of `reaches_moveLast` hold near a simple configuration.** Let the vertices
`V x` of a polygon and segments `[s j x, t j x]` depend continuously on `x`, with the polygon
simple and the segments clear of it at `x₀`, and let `w x → V x₀ (last)`. For a fixed small
ratio `r` the buffers `p = v + r (b - v)`, `q = v + r (a - v)` satisfy every condition for all
`x` near `x₀`. -/
theorem eventually_moveConds {N : ℕ} {V : X → Fin (N + 3) → E} (hV : Continuous V)
    (hP : (polyOf (V x₀)).IsSimple) {w : X → E} (hw : Continuous w)
    (hw0 : w x₀ = V x₀ (Fin.last (N + 2)))
    {J : Type*} [Finite J] {s t : J → X → E} (hs : ∀ j, Continuous (s j))
    (ht : ∀ j, Continuous (t j))
    (hR : ∀ j, Disjoint (segment ℝ (s j x₀) (t j x₀)) (polyOf (V x₀)).carrier) :
    ∃ r, 0 < r ∧ r < 1 ∧ ∀ᶠ x in 𝓝 x₀,
      MoveConds (coreSet (V x) ∪ ⋃ j, segment ℝ (s j x) (t j x))
        (V x (iA N)) (V x 0) (V x (Fin.last (N + 2))) (w x)
        (ratioPt r (V x (Fin.last (N + 2))) (V x 0))
        (ratioPt r (V x (Fin.last (N + 2))) (V x (iA N))) := by
  have hVi : ∀ i, Continuous fun x => V x i := fun i => (continuous_apply i).comp hV
  have hRv : ∀ j, V x₀ (Fin.last (N + 2)) ∉ segment ℝ (s j x₀) (t j x₀) := fun j h =>
    disjoint_left.mp (hR j) h ((polyOf (V x₀)).vertex_mem_carrier (Fin.last _))
  obtain ⟨r, hr0, hr1, hcore, hRr⟩ :=
    exists_ratio hP (fun j => s j x₀) (fun j => t j x₀) hRv
  refine ⟨r, hr0, hr1, ?_⟩
  -- names for the moving points
  set a : X → E := fun x => V x (iA N) with ha_def
  set b : X → E := fun x => V x 0 with hb_def
  set v : X → E := fun x => V x (Fin.last (N + 2)) with hv_def
  set p : X → E := fun x => ratioPt r (v x) (b x) with hp_def
  set q : X → E := fun x => ratioPt r (v x) (a x) with hq_def
  have ha : Continuous a := hVi _
  have hb : Continuous b := hVi _
  have hv : Continuous v := hVi _
  have hp : Continuous p := continuous_ratioPt r hv hb
  have hq : Continuous q := continuous_ratioPt r hv ha
  have hav : a x₀ ≠ v x₀ := corner_ne hP iA_ne_last
  have hbv : b x₀ ≠ v x₀ := corner_ne hP last_ne_zero'.symm
  have hns : ¬ SameRay ℝ (a x₀ - v x₀) (b x₀ - v x₀) := corner_not_sameRay hP
  have hns' : ¬ SameRay ℝ (b x₀ - v x₀) (a x₀ - v x₀) := fun h => hns h.symm
  have hau : a x₀ - v x₀ ≠ 0 := sub_ne_zero.mpr hav
  have hbu : b x₀ - v x₀ ≠ 0 := sub_ne_zero.mpr hbv
  have hadj : segment ℝ (a x₀) (v x₀) ∩ segment ℝ (v x₀) (b x₀) = {v x₀} := corner_adj hP
  have hw0' : w x₀ = v x₀ := hw0
  have hcarA : segment ℝ (a x₀) (v x₀) ⊆ (polyOf (V x₀)).carrier := by
    have := (polyOf (V x₀)).edge_subset_carrier (iA N)
    rwa [polyOf_edge_iA] at this
  have hcarV : segment ℝ (v x₀) (b x₀) ⊆ (polyOf (V x₀)).carrier := by
    have := (polyOf (V x₀)).edge_subset_carrier (Fin.last (N + 2))
    rwa [polyOf_edge_last] at this
  have hqa : q x₀ ∈ segment ℝ (v x₀) (a x₀) := ratioPt_mem_segment hr0.le hr1.le _ _
  have hpb : p x₀ ∈ segment ℝ (v x₀) (b x₀) := ratioPt_mem_segment hr0.le hr1.le _ _
  have hvq : segment ℝ (v x₀) (q x₀) ⊆ segment ℝ (v x₀) (a x₀) :=
    segment_ratioPt_subset hr0.le hr1.le _ _
  have hvp : segment ℝ (v x₀) (p x₀) ⊆ segment ℝ (v x₀) (b x₀) :=
    segment_ratioPt_subset hr0.le hr1.le _ _
  have hpb' : segment ℝ (p x₀) (b x₀) ⊆ segment ℝ (v x₀) (b x₀) :=
    segment_ratioPt_subset' hr0.le hr1.le _ _
  have hv_pb : v x₀ ∉ segment ℝ (p x₀) (b x₀) :=
    left_notMem_segment_ratioPt hr0 hr1.le hbv.symm
  have hv_qa : v x₀ ∉ segment ℝ (q x₀) (a x₀) :=
    left_notMem_segment_ratioPt hr0 hr1.le hav.symm
  -- the two `x₀`-intersections at `v` that every case reduces to
  have hva_vb : ∀ y, y ∈ segment ℝ (v x₀) (a x₀) → y ∈ segment ℝ (v x₀) (b x₀) → y = v x₀ :=
    fun y h1 h2 => by
      have : y ∈ segment ℝ (a x₀) (v x₀) ∩ segment ℝ (v x₀) (b x₀) :=
        ⟨by rwa [segment_symm], h2⟩
      rw [hadj] at this; exact this
  -- the corner triangle conditions (`hcut` with `z = v`, `hins` with `z = w`)
  have corner : ∀ z : X → E, Continuous z → z x₀ = v x₀ → ∀ᶠ x in 𝓝 x₀,
      convexHull ℝ {q x, p x, z x} ∩ ((coreSet (V x) ∪ ⋃ j, segment ℝ (s j x) (t j x)) ∪
        segment ℝ (a x) (q x) ∪ segment ℝ (p x) (b x)) ⊆ {q x, p x} := by
    intro z hz hz0
    have hT0 : convexHull ℝ {q x₀, p x₀, z x₀} = convexHull ℝ {q x₀, p x₀, v x₀} := by rw [hz0]
    have ecore : ∀ k : Fin (N + 1), ∀ᶠ x in 𝓝 x₀, segment ℝ (V x k.castSucc.castSucc)
        (V x k.succ.castSucc) ∩ convexHull ℝ {q x, p x, z x} = ∅ := fun k =>
      eventually_segment_inter_convexHull_eq_empty (hVi _) (hVi _) hq hp hz
        (by rw [hT0]; exact hcore k)
    have eR : ∀ j, ∀ᶠ x in 𝓝 x₀, segment ℝ (s j x) (t j x) ∩
        convexHull ℝ {q x, p x, z x} = ∅ := fun j =>
      eventually_segment_inter_convexHull_eq_empty (hs j) (ht j) hq hp hz
        (by rw [hT0]; exact hRr j)
    have eaq := eventually_segment_inter_convexHull_subset hq ha hp hz
      (by rw [hT0]; exact segment_inter_cornerTriangle hr0 hr1 hau hbu hns)
      (by rw [hz0]; exact ratioPt_notMem_segment hr0 hau hbu hns)
      (ratioPt_ne_right hr1 hav.symm).symm
    have epb := eventually_segment_inter_convexHull_subset hp hb hq hz
      (by rw [hz0]; exact segment_inter_cornerTriangle hr0 hr1 hbu hau hns')
      (by rw [hz0]; exact ratioPt_notMem_segment hr0 hbu hau hns')
      (ratioPt_ne_right hr1 hbv.symm).symm
    filter_upwards [Filter.eventually_all.mpr ecore, Filter.eventually_all.mpr eR, eaq, epb]
      with x h1 h2 h3 h4
    rintro y ⟨hyT, hy⟩
    rcases hy with ((hy | hy) | hy) | hy
    · obtain ⟨k, hk⟩ := mem_iUnion.mp hy
      exact ((h1 k).subset ⟨hk, hyT⟩).elim
    · obtain ⟨j, hj⟩ := mem_iUnion.mp hy
      exact ((h2 j).subset ⟨hj, hyT⟩).elim
    · rw [segment_symm] at hy
      exact Or.inl (h3 ⟨hy, hyT⟩)
    · have : y ∈ convexHull ℝ {p x, q x, z x} := by rwa [insert_comm]
      exact Or.inr (h4 ⟨hy, this⟩)
  -- deleting `q`: the triangle `{a, w, q}` is the edge `[a, v]` at `x₀`
  have hdq : ∀ᶠ x in 𝓝 x₀, convexHull ℝ {a x, w x, q x} ∩
      ((coreSet (V x) ∪ ⋃ j, segment ℝ (s j x) (t j x)) ∪ segment ℝ (w x) (p x) ∪
        segment ℝ (p x) (b x)) ⊆ {a x, w x} := by
    have hT0 : convexHull ℝ {a x₀, w x₀, q x₀} = segment ℝ (a x₀) (v x₀) := by
      rw [hw0']; exact convexHull_triple_of_mem_segment (by rw [segment_symm]; exact hqa)
    have hno : a x₀ ∉ segment ℝ (w x₀) (q x₀) := by
      rw [hw0']; exact right_notMem_segment_ratioPt hr0.le hr1 hav.symm
    have ecore : ∀ k : Fin (N + 1), ∀ᶠ x in 𝓝 x₀, segment ℝ (V x k.castSucc.castSucc)
        (V x k.succ.castSucc) ∩ convexHull ℝ {a x, w x, q x} ⊆ {a x, w x} := by
      intro k
      by_cases hk : k = Fin.last N
      · subst hk
        have e : (Fin.last N).succ.castSucc = iA N := by simp [iA]
        have := eventually_segment_inter_convexHull_subset ha (hVi (Fin.last N).castSucc.castSucc)
          hw hq (x₀ := x₀) (by
            rw [hT0]
            intro y hy
            have := corner_adj_core hP
            rw [← this]
            exact ⟨by rw [segment_symm]; exact hy.1, hy.2⟩) hno
          (corner_ne hP (core_ne_iA _))
        filter_upwards [this] with x hx
        rw [e, segment_symm]
        exact hx.trans (by simp)
      · have := eventually_segment_inter_convexHull_eq_empty (hVi k.castSucc.castSucc)
          (hVi k.succ.castSucc) ha hw hq (x₀ := x₀) (by
            rw [hT0]; exact disjoint_iff_inter_eq_empty.mp (corner_disj_iA hP hk))
        filter_upwards [this] with x hx
        rw [hx]; exact empty_subset _
    have eR : ∀ j, ∀ᶠ x in 𝓝 x₀, segment ℝ (s j x) (t j x) ∩
        convexHull ℝ {a x, w x, q x} = ∅ := fun j =>
      eventually_segment_inter_convexHull_eq_empty (hs j) (ht j) ha hw hq (by
        rw [hT0]
        exact disjoint_iff_inter_eq_empty.mp ((hR j).mono_right hcarA))
    have ewp := eventually_segment_inter_convexHull_subset hw hp ha hq (x₀ := x₀)
      (by
        rw [hw0', convexHull_triple_of_mem_segment hqa]
        rintro y ⟨hy1, hy2⟩
        exact hva_vb y hy2 (hvp hy1))
      (by rw [hw0', segment_symm]; exact hv_qa)
      (by rw [hw0']; exact ratioPt_ne_left hr0 hbv.symm)
    have epb := eventually_segment_inter_convexHull_eq_empty hp hb ha hw hq (x₀ := x₀) (by
      rw [hT0]
      refine eq_empty_iff_forall_notMem.mpr fun y ⟨hy1, hy2⟩ => hv_pb ?_
      have := hva_vb y (by rw [segment_symm]; exact hy2) (hpb' hy1)
      exact this ▸ hy1)
    filter_upwards [Filter.eventually_all.mpr ecore, Filter.eventually_all.mpr eR, ewp, epb]
      with x h1 h2 h3 h4
    rintro y ⟨hyT, hy⟩
    rcases hy with ((hy | hy) | hy) | hy
    · obtain ⟨k, hk⟩ := mem_iUnion.mp hy
      exact h1 k ⟨hk, hyT⟩
    · obtain ⟨j, hj⟩ := mem_iUnion.mp hy
      exact ((h2 j).subset ⟨hj, hyT⟩).elim
    · have : y ∈ convexHull ℝ {w x, a x, q x} := by rwa [insert_comm]
      exact Or.inr (h3 ⟨hy, this⟩)
    · exact ((h4).subset ⟨hy, hyT⟩).elim
  -- deleting `p`: the triangle `{w, b, p}` is the edge `[v, b]` at `x₀`
  have hdp : ∀ᶠ x in 𝓝 x₀, convexHull ℝ {w x, b x, p x} ∩
      ((coreSet (V x) ∪ ⋃ j, segment ℝ (s j x) (t j x)) ∪ segment ℝ (a x) (w x)) ⊆
        {w x, b x} := by
    have hT0 : convexHull ℝ {w x₀, b x₀, p x₀} = segment ℝ (v x₀) (b x₀) := by
      rw [hw0']; exact convexHull_triple_of_mem_segment hpb
    have hT0' : convexHull ℝ {b x₀, w x₀, p x₀} = segment ℝ (v x₀) (b x₀) := by
      rw [insert_comm]; exact hT0
    have ecore : ∀ k : Fin (N + 1), ∀ᶠ x in 𝓝 x₀, segment ℝ (V x k.castSucc.castSucc)
        (V x k.succ.castSucc) ∩ convexHull ℝ {w x, b x, p x} ⊆ {w x, b x} := by
      intro k
      by_cases hk : k = 0
      · subst hk
        have e0 : (0 : Fin (N + 1)).castSucc.castSucc = (0 : Fin (N + 3)) := rfl
        have e1 : (0 : Fin (N + 1)).succ.castSucc = (1 : Fin (N + 3)) := by
          simp
        have := eventually_segment_inter_convexHull_subset hb (hVi 1) hw hp (x₀ := x₀)
          (by
            rw [hT0']
            intro y hy
            have := corner_adj_zero hP
            rw [← this]
            exact ⟨hy.2, hy.1⟩)
          (by rw [hw0']; exact right_notMem_segment_ratioPt hr0.le hr1 hbv.symm)
          (corner_ne hP (by simp))
        filter_upwards [this] with x hx
        rw [e0, e1]
        intro y hy
        have : y ∈ segment ℝ (b x) (V x 1) ∩ convexHull ℝ {b x, w x, p x} :=
          ⟨hy.1, by rw [insert_comm]; exact hy.2⟩
        exact Or.inr (hx this)
      · have := eventually_segment_inter_convexHull_eq_empty (hVi k.castSucc.castSucc)
          (hVi k.succ.castSucc) hw hb hp (x₀ := x₀) (by
            rw [hT0]; exact disjoint_iff_inter_eq_empty.mp (corner_disj_last hP hk))
        filter_upwards [this] with x hx
        rw [hx]; exact empty_subset _
    have eR : ∀ j, ∀ᶠ x in 𝓝 x₀, segment ℝ (s j x) (t j x) ∩
        convexHull ℝ {w x, b x, p x} = ∅ := fun j =>
      eventually_segment_inter_convexHull_eq_empty (hs j) (ht j) hw hb hp (by
        rw [hT0]
        exact disjoint_iff_inter_eq_empty.mp ((hR j).mono_right hcarV))
    have eaw := eventually_segment_inter_convexHull_subset hw ha hb hp (x₀ := x₀)
      (by
        rw [hT0, hw0']
        rintro y ⟨hy1, hy2⟩
        exact hva_vb y hy1 hy2)
      (by rw [hw0', segment_symm]; exact hv_pb)
      (by rw [hw0']; exact hav)
    filter_upwards [Filter.eventually_all.mpr ecore, Filter.eventually_all.mpr eR, eaw]
      with x h1 h2 h3
    rintro y ⟨hyT, hy⟩
    rcases hy with (hy | hy) | hy
    · obtain ⟨k, hk⟩ := mem_iUnion.mp hy
      exact h1 k ⟨hk, hyT⟩
    · obtain ⟨j, hj⟩ := mem_iUnion.mp hy
      exact ((h2 j).subset ⟨hj, hyT⟩).elim
    · rw [segment_symm] at hy
      exact Or.inl (h3 ⟨hy, hyT⟩)
  -- `[q, w] ∩ [w, p] ⊆ {w}`
  have hseg := eventually_segment_inter_segment_subset hw hq hp (x₀ := x₀)
    (by
      rw [hw0']
      rintro y ⟨hy1, hy2⟩
      exact hva_vb y (hvq hy1) (hvp hy2))
    (by rw [hw0']; exact ratioPt_ne_left hr0 hbv.symm)
    (by rw [hw0']; exact ratioPt_ne_left hr0 hav.symm)
  have hwq : ∀ᶠ x in 𝓝 x₀, w x ≠ q x := by
    have h0 : w x₀ - q x₀ ≠ 0 := sub_ne_zero.mpr (by
      rw [hw0']; exact (ratioPt_ne_left hr0 hav.symm).symm)
    filter_upwards [(hw.sub hq).continuousAt.eventually_ne h0] with x hx
    exact sub_ne_zero.mp hx
  have hwp : ∀ᶠ x in 𝓝 x₀, w x ≠ p x := by
    have h0 : w x₀ - p x₀ ≠ 0 := sub_ne_zero.mpr (by
      rw [hw0']; exact (ratioPt_ne_left hr0 hbv.symm).symm)
    filter_upwards [(hw.sub hp).continuousAt.eventually_ne h0] with x hx
    exact sub_ne_zero.mp hx
  filter_upwards [corner v hv rfl, corner w hw hw0', hdq, hdp, hseg, hwq, hwp]
    with x hcut hins hdq hdp hseg hwq hwp
  exact
    { hp := ratioPt_mem_openSegment hr0 hr1 _ _
      hq := by rw [openSegment_symm]; exact ratioPt_mem_openSegment hr0 hr1 _ _
      hcut := hcut
      hwq := hwq
      hwp := hwp
      hwseg := fun y hy => hseg ⟨by rw [segment_symm]; exact hy.1, hy.2⟩
      hins := hins
      hdq := hdq
      hdp := hdp }

end Near

end QOU.MathlibExt.PL
