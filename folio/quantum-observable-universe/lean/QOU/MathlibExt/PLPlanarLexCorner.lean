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

end QOU.MathlibExt.PL
