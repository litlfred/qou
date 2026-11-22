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

/-! ### A chord at a leftmost vertex sees both sides as outside -/

lemma exists_near (v d : R2) {ρ : ℝ} (hρ : 0 < ρ) :
    ∃ ε : ℝ, 0 < ε ∧ ε ≤ 1 ∧ v + ε • d ∈ Metric.ball v ρ := by
  refine ⟨min 1 (ρ / (2 * (‖d‖ + 1))), by positivity, min_le_left _ _, ?_⟩
  rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_left, norm_smul, Real.norm_eq_abs,
    abs_of_pos (by positivity)]
  calc min 1 (ρ / (2 * (‖d‖ + 1))) * ‖d‖ ≤ ρ / (2 * (‖d‖ + 1)) * ‖d‖ := by
        gcongr; exact min_le_right _ _
    _ < ρ / (2 * (‖d‖ + 1)) * (2 * (‖d‖ + 1)) := by
        gcongr; linarith [norm_nonneg d]
    _ = ρ := by field_simp

lemma mem_reflex_smul {v b z d : R2} (hD : cross v b z ≠ 0)
    (hd : ∀ s t : ℝ, 0 ≤ s → 0 ≤ t → d ≠ s • (b - v) + t • (z - v)) {ε : ℝ} (hε : 0 < ε) :
    v + ε • d ∈ reflex v b z := by
  refine mem_reflex_of_not_cone hD fun s t hs ht h => hd (s / ε) (t / ε) (by positivity)
    (by positivity) ?_
  rw [add_assoc] at h
  have h' := add_left_cancel h
  have : d = ε⁻¹ • (ε • d) := by rw [smul_smul, inv_mul_cancel₀ hε.ne', one_smul]
  rw [this, h', smul_add, smul_smul, smul_smul, div_eq_inv_mul, div_eq_inv_mul]

lemma lineMap_one_sub (a v : R2) (ε : ℝ) :
    AffineMap.lineMap a v (1 - ε) = v + ε • (a - v) := by
  rw [AffineMap.lineMap_apply_module]; module

lemma lineMap_eq_add (v b : R2) (t : ℝ) : AffineMap.lineMap v b t = v + t • (b - v) := by
  rw [AffineMap.lineMap_apply_module]; module

/-- **A chord at a leftmost vertex is interior.** At the leftmost vertex `v = w 0` with
neighbours `a = w n` and `b = w 1`, a valid chord to `z = w β` such that neither neighbour lies
in the closed cone the other two directions span sees both pieces as outside each other. -/
theorem chord_sides_outside {P : Polygon R2} (hP : P.IsSimple) (hlex : ∀ i, P.w 0 0 ≤ P.v i 0)
    {β : ℕ} (hβ : 2 ≤ β) (h2 : 2 ≤ P.n + 1 - β)
    (hchord : segment ℝ (P.w 0) (P.w β) ∩ P.carrier ⊆ {P.w 0, P.w β})
    (hD1 : cross (P.w 0) (P.w 1) (P.w β) ≠ 0)
    (hA : ∀ s t : ℝ, 0 ≤ s → 0 ≤ t →
      P.w P.n - P.w 0 ≠ s • (P.w 1 - P.w 0) + t • (P.w β - P.w 0))
    (hD2 : cross (P.w 0) (P.w β) (P.w P.n) ≠ 0)
    (hB : ∀ s t : ℝ, 0 ≤ s → 0 ≤ t →
      P.w 1 - P.w 0 ≠ s • (P.w β - P.w 0) + t • (P.w P.n - P.w 0)) :
    (∀ y ∈ P.carrier, y ∉ (P.cut β hβ).carrier → (P.cut β hβ).parity y = 0) ∧
    (∀ y ∈ P.carrier, y ∉ (P.cocut β h2).carrier → (P.cocut β h2).parity y = 0) := by
  have hβn : β + 1 ≤ P.n := by omega
  constructor
  · -- the cut piece, corner at index `0`
    have hQ := isSimple_cut hP hβ hβn hchord
    have e0 : (P.cut β hβ).w 0 = P.w 0 := cut_w_of_le P (Nat.zero_le _)
    have e1 : (P.cut β hβ).w (0 + 1) = P.w 1 := cut_w_of_le P (by omega)
    have en : (P.cut β hβ).w (0 + (P.cut β hβ).n) = P.w β := by
      rw [cut_n, zero_add]; exact cut_w_of_le P le_rfl
    obtain ⟨ρ, hρ, hc⟩ := parity_corner_zero_at (P.cut β hβ) hQ 0
      (by rw [e0, e1, en]; exact hD1) (fun i => by
        rw [e0]; exact hlex ⟨i % (P.n + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩)
    rw [e0, e1, en] at hc
    obtain ⟨ε, hε, hε1, hball⟩ := exists_near (P.w 0) (P.w P.n - P.w 0) hρ
    refine parity_cut_eq_zero_of_witness hP hβ hβn hchord (y₀ := P.w 0 + ε • (P.w P.n - P.w 0))
      ?_ (hc _ ⟨hball, mem_reflex_smul hD1 hA hε⟩)
    refine farLast_subset hP hβ hβn ⟨1 - ε, ⟨by linarith, by linarith⟩, ?_⟩
    exact lineMap_one_sub _ _ _
  · -- the complementary piece: the cut piece of the rotation, corner at index `γ`
    set R := P.rotateBy β with hR
    set γ := P.n + 1 - β with hγ
    have hRn : R.n = P.n := rotateBy_n P β
    have hRs : R.IsSimple := P.isSimple_rotateBy hP β
    have hw : ∀ k, R.w k = P.w (k + β) := fun k => w_rotateBy P β k
    have hRγ : R.w γ = P.w 0 := by rw [hw, show γ + β = P.n + 1 by omega, w_period]
    have hR0 : R.w 0 = P.w β := by rw [hw, zero_add]
    have hR1 : R.w (γ + 1) = P.w 1 := by
      rw [hw, show γ + 1 + β = 1 + (P.n + 1) by omega, w_add_period]
    have hRγ' : R.w (γ - 1) = P.w P.n := by rw [hw, show γ - 1 + β = P.n by omega]
    have hRchord : segment ℝ (R.w 0) (R.w γ) ∩ R.carrier ⊆ {R.w 0, R.w γ} := by
      rw [hR0, hRγ, carrier_rotateBy, segment_symm]
      intro y hy
      rcases hchord hy with h | h
      · exact Or.inr h
      · exact Or.inl h
    have h2' : 2 ≤ γ := h2
    have hγn : γ + 1 ≤ R.n := by omega
    have hQ := isSimple_cut hRs h2' hγn hRchord
    have e0 : (R.cut γ h2').w γ = P.w 0 := by rw [cut_w_of_le R le_rfl, hRγ]
    have e1 : (R.cut γ h2').w (γ + 1) = P.w β := by rw [cut_w, Nat.mod_self, hR0]
    have en : (R.cut γ h2').w (γ + (R.cut γ h2').n) = P.w P.n := by
      rw [cut_n, cut_w, show γ + γ = (γ - 1) + (γ + 1) by omega, Nat.add_mod_right,
        Nat.mod_eq_of_lt (by omega), hRγ']
    obtain ⟨ρ, hρ, hc⟩ := parity_corner_zero_at (R.cut γ h2') hQ γ
      (by rw [e0, e1, en]; exact hD2) (fun i => by
        rw [e0]
        show P.w 0 0 ≤ R.w i 0
        rw [hw]; exact hlex ⟨(i + β) % (P.n + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩)
    rw [e0, e1, en] at hc
    obtain ⟨ε, hε, hε1, hball⟩ := exists_near (P.w 0) (P.w 1 - P.w 0) hρ
    have hres := parity_cut_eq_zero_of_witness hRs h2' hγn hRchord
      (y₀ := P.w 0 + ε • (P.w 1 - P.w 0)) ?_ (hc _ ⟨hball, mem_reflex_smul hD2 hB hε⟩)
    · rw [carrier_rotateBy] at hres
      exact hres
    · refine farFirst_subset hRs h2' hγn ⟨ε, ⟨hε, hε1⟩, ?_⟩
      rw [hRγ, hR1]; exact lineMap_eq_add _ _ _

end QOU.MathlibExt.PL
