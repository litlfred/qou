/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarChord

set_option autoImplicit false

/-!
# The parity near a corner (issue #8902, Moise part B, step 1)

Near a vertex of a simple polygon only its two sides pass, so the crossing parity is constant on
the reflex side of the corner near the vertex. At a leftmost vertex that constant is `0`: just
left of the vertex is outside.

## What is a THEOREM here

* `parity_corner` — constancy on the reflex side near vertex `0`.
* `parity_corner_zero_at` — at a leftmost vertex (any index), the constant is `0`.
-/

namespace QOU.MathlibExt.PL

open Set Polygon

theorem parity_corner (Q : Polygon R2) (hQ : Q.IsSimple)
    (hD : cross (Q.w 0) (Q.w 1) (Q.w Q.n) ≠ 0) :
    ∃ ρ > 0, ∀ y ∈ Metric.ball (Q.w 0) ρ ∩ reflex (Q.w 0) (Q.w 1) (Q.w Q.n),
      ∀ y' ∈ Metric.ball (Q.w 0) ρ ∩ reflex (Q.w 0) (Q.w 1) (Q.w Q.n),
        Q.parity y = Q.parity y' := by
  set C : Set R2 := ⋃ k ∈ Finset.Icc 1 (Q.n - 1), Q.seg k with hC
  have hCc : IsClosed C :=
    isClosed_biUnion_finset fun k _ => (isCompact_segment_R2 _ _).isClosed
  have hvC : Q.w 0 ∉ C := by
    intro h
    obtain ⟨k, hk, hvk⟩ := mem_iUnion₂.mp h
    rw [Finset.mem_Icc] at hk
    rcases hQ.w_mem_seg (Nat.zero_le _) (by omega) hvk with h | h
    · omega
    · rw [Nat.mod_eq_of_lt (by omega)] at h; omega
  obtain ⟨ρ, hρ, hball⟩ := Metric.isOpen_iff.mp hCc.isOpen_compl _ hvC
  refine ⟨ρ, hρ, fun y hy y' hy' =>
    Q.parity_const_of_isPreconnected (isPreconnected_reflex hD hρ) ?_ hy hy'⟩
  rw [Set.disjoint_left]
  rintro x ⟨hxb, hxr⟩ hxc
  rw [carrier_eq_biUnion] at hxc
  obtain ⟨k, hk, hxk⟩ := mem_iUnion₂.mp hxc
  rw [Finset.mem_range] at hk
  by_cases h0 : k = 0
  · subst h0
    exact not_mem_reflex_of_mem_segment (Or.inl hxk) hxr
  by_cases hn : k = Q.n
  · subst hn
    have : x ∈ segment ℝ (Q.w 0) (Q.w Q.n) := by
      rw [segment_symm, ← Q.w_period]; exact hxk
    exact not_mem_reflex_of_mem_segment (Or.inr this) hxr
  · exact hball hxb (mem_iUnion₂.mpr ⟨k, Finset.mem_Icc.mpr ⟨by omega, by omega⟩, hxk⟩)

theorem parity_corner_zero (Q : Polygon R2) (hQ : Q.IsSimple)
    (hD : cross (Q.w 0) (Q.w 1) (Q.w Q.n) ≠ 0) (hlex : ∀ i, Q.w 0 0 ≤ Q.v i 0) :
    ∃ ρ > 0, ∀ y ∈ Metric.ball (Q.w 0) ρ ∩ reflex (Q.w 0) (Q.w 1) (Q.w Q.n), Q.parity y = 0 := by
  obtain ⟨ρ, hρ, hc⟩ := parity_corner Q hQ hD
  refine ⟨ρ, hρ, fun y hy => ?_⟩
  set v := Q.w 0
  set δ := ρ / (2 * (‖e0‖ + 1)) with hδ
  have hδ0 : 0 < δ := by positivity
  have hy0 : v - δ • e0 ∈ Metric.ball v ρ ∩ reflex v (Q.w 1) (Q.w Q.n) := by
    refine ⟨?_, mem_reflex_of_not_cone hD fun s t hs ht h => ?_⟩
    · rw [Metric.mem_ball, dist_eq_norm, sub_sub_cancel_left, norm_neg, norm_smul,
        Real.norm_eq_abs, abs_of_pos hδ0]
      calc δ * ‖e0‖ < δ * (2 * (‖e0‖ + 1)) := by gcongr; linarith [norm_nonneg e0]
        _ = ρ := by simp only [δ]; field_simp
    · have h0 := congrFun h 0
      have hb := hlex ⟨1 % (Q.n + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩
      have hz := hlex ⟨Q.n % (Q.n + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩
      change v 0 ≤ Q.w 1 0 at hb
      change v 0 ≤ Q.w Q.n 0 at hz
      simp [e0] at h0
      nlinarith [mul_nonneg hs (sub_nonneg.mpr hb), mul_nonneg ht (sub_nonneg.mpr hz)]
  rw [hc y hy _ hy0]
  refine Q.parity_eq_zero_of_forall_lt fun i => ?_
  simp [e0]
  linarith [hlex i]

/-- At a leftmost vertex `j`, the parity just off the corner, on the reflex side, is `0`. -/
theorem parity_corner_zero_at (Q : Polygon R2) (hQ : Q.IsSimple) (j : ℕ)
    (hD : cross (Q.w j) (Q.w (j + 1)) (Q.w (j + Q.n)) ≠ 0) (hlex : ∀ i, Q.w j 0 ≤ Q.v i 0) :
    ∃ ρ > 0, ∀ y ∈ Metric.ball (Q.w j) ρ ∩ reflex (Q.w j) (Q.w (j + 1)) (Q.w (j + Q.n)),
      Q.parity y = 0 := by
  have e0' : (Q.rotateBy j).w 0 = Q.w j := by rw [w_rotateBy, zero_add]
  have e1' : (Q.rotateBy j).w 1 = Q.w (j + 1) := by rw [w_rotateBy, add_comm]
  have en' : (Q.rotateBy j).w (Q.rotateBy j).n = Q.w (j + Q.n) := by
    rw [w_rotateBy, rotateBy_n, add_comm]
  have hR := parity_corner_zero (Q.rotateBy j) (Q.isSimple_rotateBy hQ j)
    (by rw [e0', e1', en']; exact hD) (fun i => by
      rw [e0', ← w_coe, w_rotateBy]
      exact hlex ⟨(i + j) % (Q.n + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩)
  rw [e0', e1', en', parity_rotateBy] at hR
  exact hR

end QOU.MathlibExt.PL
