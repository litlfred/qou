/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarTri

set_option autoImplicit false

/-!
# Ears of plane polygons: tools (issue #8902, Moise part B, step 1)

Three tools for the two-ears theorem.

## What is a THEOREM here

* `exit_right`, `exit_left` — **leaving a polytope along a line.** Finitely many affine
  constraints on `[0, 1]`, all `≥ 0` at `t₀`: moving in one direction, the first time a
  constraint that is decreasing reaches `0` (or the end of the interval) is still feasible.
* `isPreconnected_reflex`, `not_mem_reflex_of_mem_segment` — **the reflex side of a corner.**
  Near a corner `v` with sides towards `b` and `z`, the complement of the closed cone is the
  union of two open half-planes; inside a ball it is connected and misses both sides.
* `exists_lexMin` — every polygon has a lowest-leftmost vertex.
-/

namespace QOU.MathlibExt.PL

open Set Polygon

/-! ### Leaving a polytope along a line -/

/-- **Exit to the right.** -/
theorem exit_right {ι : Type*} [Finite ι] (u w : ι → ℝ) {t₀ : ℝ} (_h0 : 0 ≤ t₀) (h1 : t₀ ≤ 1)
    (hh : ∀ i, 0 ≤ (1 - t₀) * u i + t₀ * w i) :
    ∃ t, t₀ ≤ t ∧ t ≤ 1 ∧ (∀ i, 0 ≤ (1 - t) * u i + t * w i) ∧
      (t = 1 ∨ ∃ i, w i < u i ∧ (1 - t) * u i + t * w i = 0) ∧
      ((∀ i, 0 < (1 - t₀) * u i + t₀ * w i) → t₀ < 1 → t₀ < t) := by
  classical
  let c : ι → ℝ := fun i => if w i < u i then u i / (u i - w i) else 1
  have hc : ∀ i, t₀ ≤ c i := by
    intro i
    simp only [c]
    split_ifs with h
    · rw [le_div_iff₀ (by linarith)]; nlinarith [hh i]
    · exact h1
  let S : Set ℝ := insert 1 (range c)
  have hS : S.Finite := (finite_range c).insert 1
  obtain ⟨t, htS, hle⟩ := Set.exists_min_image S id hS ⟨1, mem_insert _ _⟩
  have ht1 : t ≤ 1 := hle 1 (mem_insert _ _)
  have htc : ∀ i, t ≤ c i := fun i => hle _ (mem_insert_of_mem _ ⟨i, rfl⟩)
  have ht0 : t₀ ≤ t := by
    rcases htS with h | ⟨i, rfl⟩
    · rw [h]; exact h1
    · exact hc i
  refine ⟨t, ht0, ht1, ?_, ?_, ?_⟩
  · intro i
    by_cases h : w i < u i
    · have hci : c i = u i / (u i - w i) := if_pos h
      have := htc i
      rw [hci, le_div_iff₀ (by linarith)] at this
      nlinarith
    · push_neg at h
      nlinarith [hh i]
  · rcases htS with h | ⟨i, rfl⟩
    · exact Or.inl h
    · by_cases h : w i < u i
      · right; refine ⟨i, h, ?_⟩
        have hci : c i = u i / (u i - w i) := if_pos h
        have hne : u i - w i ≠ 0 := (sub_pos.mpr h).ne'
        rw [hci]; field_simp; ring
      · left; exact if_neg h
  · intro hpos ht01
    rcases htS with h | ⟨i, rfl⟩
    · rw [h]; exact ht01
    · by_cases h : w i < u i
      · have hci : c i = u i / (u i - w i) := if_pos h
        rw [hci, lt_div_iff₀ (by linarith)]; nlinarith [hpos i]
      · have hci : c i = 1 := if_neg h
        rw [hci]; exact ht01

/-- **Exit to the left.** -/
theorem exit_left {ι : Type*} [Finite ι] (u w : ι → ℝ) {t₀ : ℝ} (h0 : 0 ≤ t₀) (h1 : t₀ ≤ 1)
    (hh : ∀ i, 0 ≤ (1 - t₀) * u i + t₀ * w i) :
    ∃ t, 0 ≤ t ∧ t ≤ t₀ ∧ (∀ i, 0 ≤ (1 - t) * u i + t * w i) ∧
      (t = 0 ∨ ∃ i, u i < w i ∧ (1 - t) * u i + t * w i = 0) ∧
      ((∀ i, 0 < (1 - t₀) * u i + t₀ * w i) → 0 < t₀ → t < t₀) := by
  obtain ⟨s, hs0, hs1, hfeas, hend, hstrict⟩ := exit_right w u (t₀ := 1 - t₀) (by linarith)
    (by linarith) (fun i => by have := hh i; linarith)
  refine ⟨1 - s, by linarith, by linarith, fun i => by have := hfeas i; linarith, ?_, ?_⟩
  · rcases hend with h | ⟨i, hi, hz⟩
    · left; linarith
    · right; exact ⟨i, hi, by linarith⟩
  · intro hpos ht
    have := hstrict (fun i => by have := hpos i; linarith) (by linarith)
    linarith

/-! ### The reflex side of a corner -/

lemma cross_vertex_add (v b d : R2) : cross v b (v + d) = (b 0 - v 0) * d 1 - (b 1 - v 1) * d 0 := by
  unfold cross; simp

lemma convex_cross_neg (a b : R2) (k : ℝ) : Convex ℝ {y | cross a b y * k < 0} := by
  intro y hy z hz s t hs ht hst
  simp only [mem_setOf_eq] at hy hz ⊢
  rw [cross_lineMap a b y z s t hst]
  rcases eq_or_lt_of_le hs with h | h
  · subst h; simp at hst; subst hst; simpa using hz
  · nlinarith [mul_nonneg ht (le_of_lt (neg_pos.mpr hz))]

/-- The open reflex side of the corner `v` with sides towards `b` and `z`. -/
def reflex (v b z : R2) : Set R2 :=
  {y | cross v b y * cross v b z < 0} ∪ {y | cross v z y * cross v z b < 0}

lemma not_mem_reflex_of_mem_segment {v b z y : R2}
    (hy : y ∈ segment ℝ v b ∪ segment ℝ v z) : y ∉ reflex v b z := by
  have key : ∀ p q y : R2, y ∈ segment ℝ v p → ¬ cross v p y * cross v p q < 0 ∧
      ¬ cross v q y * cross v q p < 0 := by
    intro p q y hy
    obtain ⟨s, t, hs, ht, hst, rfl⟩ := hy
    rw [cross_lineMap _ _ _ _ _ _ hst, cross_lineMap _ _ _ _ _ _ hst]
    simp only [cross_left, cross_right]
    constructor
    · simp
    · nlinarith [sq_nonneg (cross v q p)]
  rintro (h | h)
  · rcases hy with hy | hy
    · exact (key b z y hy).1 h
    · exact (key z b y hy).2 h
  · rcases hy with hy | hy
    · exact (key b z y hy).2 h
    · exact (key z b y hy).1 h

theorem isPreconnected_reflex {v b z : R2} (hD : cross v b z ≠ 0) {ρ : ℝ} (hρ : 0 < ρ) :
    IsPreconnected (Metric.ball v ρ ∩ reflex v b z) := by
  rw [reflex, inter_union_distrib_left]
  have hc1 := (convex_ball v ρ).inter (convex_cross_neg v b (cross v b z))
  have hc2 := (convex_ball v ρ).inter (convex_cross_neg v z (cross v z b))
  refine hc1.isPreconnected.union' ?_ hc2.isPreconnected
  -- a common point `v - s (b - v) - s (z - v)`
  set N := ‖b - v‖ + ‖z - v‖ + 1
  have hN : 0 < N := by positivity
  set s := ρ / (2 * N)
  have hs : 0 < s := by positivity
  refine ⟨v + (-s) • ((b - v) + (z - v)), ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
  · rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_left, norm_smul, Real.norm_eq_abs,
      abs_neg, abs_of_pos hs]
    calc s * ‖(b - v) + (z - v)‖ ≤ s * (‖b - v‖ + ‖z - v‖) := by gcongr; exact norm_add_le _ _
      _ < s * (2 * N) := by gcongr; linarith
      _ = ρ := by simp only [s]; field_simp
  · show cross v b _ * cross v b z < 0
    have : cross v b (v + (-s) • ((b - v) + (z - v))) = -s * cross v b z := by
      rw [cross_vertex_add]; unfold cross; simp; ring
    rw [this]; nlinarith [mul_self_pos.mpr hD]
  · rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_left, norm_smul, Real.norm_eq_abs,
      abs_neg, abs_of_pos hs]
    calc s * ‖(b - v) + (z - v)‖ ≤ s * (‖b - v‖ + ‖z - v‖) := by gcongr; exact norm_add_le _ _
      _ < s * (2 * N) := by gcongr; linarith
      _ = ρ := by simp only [s]; field_simp
  · show cross v z _ * cross v z b < 0
    have hD' : cross v z b ≠ 0 := by
      rw [show cross v z b = -cross v b z by unfold cross; ring]; exact neg_ne_zero.mpr hD
    have : cross v z (v + (-s) • ((b - v) + (z - v))) = -s * cross v z b := by
      rw [cross_vertex_add]; unfold cross; simp; ring
    rw [this]; nlinarith [mul_self_pos.mpr hD']

/-- A point outside the closed cone at `v` spanned by `b - v` and `z - v` is on the reflex side. -/
lemma mem_reflex_of_not_cone {v b z y : R2} (hD : cross v b z ≠ 0)
    (h : ∀ s t : ℝ, 0 ≤ s → 0 ≤ t → y ≠ v + s • (b - v) + t • (z - v)) : y ∈ reflex v b z := by
  by_contra hy
  simp only [reflex, mem_union, mem_setOf_eq, not_or, not_lt] at hy
  obtain ⟨h1, h2⟩ := hy
  have hD' : cross v z b = -cross v b z := by unfold cross; ring
  rw [hD'] at h2
  have hD2 : 0 < cross v b z * cross v b z := mul_self_pos.mpr hD
  refine h (-cross v z y / cross v b z) (cross v b y / cross v b z) ?_ ?_ ?_
  · rw [div_nonneg_iff]
    rcases lt_or_gt_of_ne hD with hn | hp
    · right; constructor <;> nlinarith
    · left; constructor <;> nlinarith
  · rw [div_nonneg_iff]
    rcases lt_or_gt_of_ne hD with hn | hp
    · right; constructor <;> nlinarith
    · left; constructor <;> nlinarith
  · funext k
    simp only [Pi.add_apply, Pi.smul_apply, Pi.sub_apply, smul_eq_mul]
    field_simp
    fin_cases k <;> (simp; unfold cross; ring)

/-! ### The lowest-leftmost vertex -/

/-- `x` is lexicographically below `y`: smaller abscissa, or equal abscissa and smaller
ordinate. -/
def LexLt (x y : R2) : Prop := x 0 < y 0 ∨ (x 0 = y 0 ∧ x 1 < y 1)

theorem exists_lexMin (P : Polygon R2) (hP : P.IsSimple) :
    ∃ i : Fin (P.n + 1), ∀ j, j ≠ i → LexLt (P.v i) (P.v j) := by
  classical
  let f : Fin (P.n + 1) → Lex (ℝ × ℝ) := fun i => toLex (P.v i 0, P.v i 1)
  obtain ⟨i, -, hi⟩ := Finset.exists_min_image Finset.univ f ⟨0, Finset.mem_univ _⟩
  refine ⟨i, fun j hj => ?_⟩
  have hle := hi j (Finset.mem_univ _)
  have hne : P.v i ≠ P.v j := fun h => hj (hP.1 h).symm
  have hlt : f i < f j := by
    refine lt_of_le_of_ne hle fun h => hne ?_
    have h' := congrArg ofLex h
    simp only [f, ofLex_toLex, Prod.mk.injEq] at h'
    funext k; fin_cases k
    · exact h'.1
    · exact h'.2
  simp only [f, Prod.Lex.toLex_lt_toLex] at hlt
  exact hlt

end QOU.MathlibExt.PL
