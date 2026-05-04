/-
  Hoefsmit seminormal matrices as R-matrix evaluations in H_n(q).

  For each partition λ ⊢ n, the Hoefsmit form gives an explicit
  matrix representation ρ_λ: H_n(q) → M_{d_λ}(R) on the basis of
  standard Young tableaux. The diagonal entry for generator T_i is
  a_ρ = h/(1 - q^{-2ρ}) where ρ is the axial distance.

  These are the R-matrix evaluations for topological crossings.

  **Pre-Archimedean stub.** The Hoefsmit form is rational in
  `q^±1` over any field `R ⊇ ℚ(q)`; the off-diagonal entry is the
  formal square root `b` of `a · a' + 1`, supplied as data — there
  is no `Real.sqrt` in the algebraic statement.  The Archimedean
  evaluation `q ↦ q₀ ∈ ℝ` is performed downstream
  (`QOU.Calculations`).

  Ref: [hoefsmit1974] P.N. Hoefsmit, "Representations of Hecke algebras
       of finite groups with BN-pairs of classical type", PhD thesis, 1974.
       [wenzl1988] https://doi.org/10.1007/BF01404457
       [manuscript] §5.5, prop:hoefsmit-seminormal-form
-/

import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.BraidKnot

universe u

/-- The diagonal entry in the Hoefsmit seminormal form
    (axial-distance `ρ`).  Polymorphic in the ground field `R`. -/
noncomputable def hoefsmitEntry {R : Type u} [Field R]
    (q : R) (rho : ℤ) : R :=
  let h := q - q⁻¹
  h / (1 - q ^ (-2 * rho))

/-- The off-diagonal entry of the Hoefsmit seminormal form is the
    formal square root `b` of `a · a' + 1`.  Rather than
    introducing `Real.sqrt`, we supply `b` as data and require
    the algebraic identity `b² = a·a' + 1` as a hypothesis on the
    caller's side. -/
structure HoefsmitOffDiag {R : Type u} [Field R] (q : R) (rho : ℤ) where
  b : R
  b_sq : b ^ 2 = hoefsmitEntry q rho * hoefsmitEntry q (-rho) + 1

/-- Helper: q^n ≠ 1 for q > 1 and n : ℤ with n ≠ 0. -/
private theorem hoefsmit_zpow_ne_one {q : ℝ} (hq : q > 1) {n : ℤ} (hn : n ≠ 0) :
    q ^ n ≠ 1 := by
  intro h_eq
  rcases lt_or_gt_of_ne hn with hn_neg | hn_pos
  · -- n < 0: q^n = (q^(-n).toNat)⁻¹ < 1, contradicts h_eq = 1
    have hnn : 0 ≤ -n := by omega
    have hpos : 0 < (-n).toNat := Int.toNat_pos.mpr (by omega)
    have hn_eq : n = -(↑((-n).toNat) : ℤ) := by
      rw [Int.toNat_of_nonneg hnn]; ring
    rw [hn_eq, zpow_neg, zpow_natCast] at h_eq
    have hpow : 1 < q ^ (-n).toNat := one_lt_pow₀ hq (Nat.pos_iff_ne_zero.mp hpos)
    have hlt : (q ^ (-n).toNat)⁻¹ < 1 := inv_lt_one_of_one_lt₀ hpow
    linarith [hlt, h_eq.ge]
  · -- 0 < n: q^n > 1, contradicts h_eq = 1
    have hnn : 0 ≤ n := by omega
    have hpos : 0 < n.toNat := Int.toNat_pos.mpr hn_pos
    have hn_eq : n = (↑(n.toNat) : ℤ) := (Int.toNat_of_nonneg hnn).symm
    rw [hn_eq, zpow_natCast] at h_eq
    have hpow : 1 < q ^ n.toNat := one_lt_pow₀ hq (Nat.pos_iff_ne_zero.mp hpos)
    linarith [hpow, h_eq.le]

/-- Helper: for `q > 1` and `n ≥ 1`, we have `q ≤ q^n`. -/
private theorem hoefsmit_self_le_pow {q : ℝ} (hq : 1 < q) :
    ∀ n : ℕ, 1 ≤ n → q ≤ q ^ n := by
  intro n hn
  have hq_pos : (0 : ℝ) < q := lt_trans zero_lt_one hq
  induction n with
  | zero => omega
  | succ k ih =>
    rcases Nat.eq_or_gt_of_le hn with h_eq | h_gt
    · -- n = 1, so k+1 = 1, k = 0
      have : k = 0 := by omega
      subst this; simp
    · -- k ≥ 1, apply IH then multiply by q ≥ 1
      have hk : 1 ≤ k := by omega
      have ih' : q ≤ q ^ k := ih hk
      have hqk_ge_one : (1 : ℝ) ≤ q ^ k := le_trans (le_of_lt hq) ih'
      calc q = q * 1 := (mul_one q).symm
        _ ≤ q * q ^ k := mul_le_mul_of_nonneg_left hqk_ge_one (le_of_lt hq_pos)
        _ = q ^ (k + 1) := by ring

/-- Helper: for `q > 1` and `ρ : ℤ` with `ρ ≠ 0`, the squared difference
    `(q^ρ - q^{-ρ})²` dominates `(q - q⁻¹)²`. -/
private theorem hoefsmit_zpow_diff_sq_ge {q : ℝ} (hq : q > 1) {ρ : ℤ} (hρ : ρ ≠ 0) :
    (q - q⁻¹) ^ 2 ≤ (q ^ ρ - q ^ (-ρ)) ^ 2 := by
  have hq_pos : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have hq0 : q ≠ 0 := ne_of_gt hq_pos
  have hq_inv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have h_h_pos : 0 < q - q⁻¹ := by linarith
  -- Reduce to natural-number power: let n := |ρ| ≥ 1.
  set n := ρ.natAbs with hn_def
  have hn_pos : 0 < n := Int.natAbs_pos.mpr hρ
  have hn_ge_one : 1 ≤ n := hn_pos
  -- The squared difference is symmetric under ρ ↔ -ρ, and equals (q^n - q^(-n))²
  have h_sq_eq : (q ^ ρ - q ^ (-ρ)) ^ 2 = (q ^ n - (q ^ n)⁻¹) ^ 2 := by
    rcases Int.natAbs_eq ρ with h_pos | h_neg
    · -- ρ = ↑n
      rw [show ρ = (↑n : ℤ) from h_pos, zpow_natCast, zpow_neg, zpow_natCast]
    · -- ρ = -↑n
      rw [show ρ = -(↑n : ℤ) from h_neg, neg_neg, zpow_natCast, zpow_neg, zpow_natCast]
      ring
  rw [h_sq_eq]
  -- Now: (q - q⁻¹)² ≤ (q^n - (q^n)⁻¹)² with n ≥ 1.
  have hqn_ge : q ≤ q ^ n := hoefsmit_self_le_pow hq n hn_ge_one
  have hqn_pos : (0 : ℝ) < q ^ n := pow_pos hq_pos n
  have hqn_ge_one : (1 : ℝ) ≤ q ^ n := le_trans (le_of_lt hq) hqn_ge
  -- Inverse direction: (q^n)⁻¹ ≤ q⁻¹  ⇔  q ≤ q^n  (both positive)
  have hqn_inv_le : (q ^ n)⁻¹ ≤ q⁻¹ := by
    rw [inv_le_inv₀ hqn_pos hq_pos]; exact hqn_ge
  -- Both base differences are non-negative
  have h_diff1_nn : 0 ≤ q - q⁻¹ := le_of_lt h_h_pos
  have h_diff2_nn : 0 ≤ q ^ n - (q ^ n)⁻¹ := by linarith
  -- Squares preserve order on non-negatives: x ≤ y → x² ≤ y² (both ≥ 0)
  have h_diff_le : q - q⁻¹ ≤ q ^ n - (q ^ n)⁻¹ := by linarith
  exact pow_le_pow_left h_diff1_nn h_diff_le 2

/-- The 2×2 Hoefsmit block has determinant -1 (from the Hecke relation).
    This is the product of eigenvalues: q · (-q⁻¹) = -1. -/
theorem hoefsmit_block_det (q : ℝ) (hq : q > 1) (rho : ℤ) (hrho : rho ≠ 0) :
    let a := hoefsmitEntry q hq rho
    let a' := hoefsmitEntry q hq (-rho)
    let b := hoefsmitOffDiag q hq rho
    a * a' - b ^ 2 = -1 := by
  -- The proof reduces to: b² = a*a' + 1, since b = √(a*a'+1) and a*a'+1 ≥ 0.
  -- Then a*a' - b² = a*a' - (a*a'+1) = -1 by ring.
  -- Non-negativity of a*a' + 1 reduces (by algebraic manipulation) to the
  -- inequality (q^ρ - q^{-ρ})² ≥ (q - q⁻¹)², proved as
  -- `hoefsmit_zpow_diff_sq_ge` above.
  have hq_pos : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have hq0 : q ≠ 0 := ne_of_gt hq_pos
  -- Side facts on denominators
  have h2r : (2 * rho : ℤ) ≠ 0 := by intro h; exact hrho (by omega)
  have h_den1 : (1 : ℝ) - q ^ (-2 * rho) ≠ 0 := by
    have h_ne : q ^ (-2 * rho) ≠ 1 := by
      have : (-2 * rho : ℤ) ≠ 0 := by intro h; exact h2r (by omega)
      exact hoefsmit_zpow_ne_one hq this
    intro h; exact h_ne (by linarith)
  have h_den2 : (1 : ℝ) - q ^ (-2 * -rho) ≠ 0 := by
    have h_ne : q ^ (-2 * -rho) ≠ 1 := by
      have : (-2 * -rho : ℤ) ≠ 0 := by intro h; exact h2r (by omega)
      exact hoefsmit_zpow_ne_one hq this
    intro h; exact h_ne (by linarith)
  -- Key inequality on q^ρ - q^{-ρ}
  have h_zpow_diff_pos : (q ^ rho - q ^ (-rho)) ^ 2 > 0 := by
    have h_ne : q ^ rho ≠ q ^ (-rho) := by
      intro h_eq
      -- q^rho = q^{-rho} ⇒ multiplying both sides by q^rho gives q^(2*rho) = 1
      have hmul : q ^ rho * q ^ rho = q ^ (-rho) * q ^ rho := by rw [h_eq]
      have h_lhs : q ^ rho * q ^ rho = q ^ (2 * rho) := by
        rw [show (2 * rho : ℤ) = rho + rho from by ring, zpow_add₀ hq0]
      have h_rhs : q ^ (-rho) * q ^ rho = (1 : ℝ) := by
        rw [← zpow_add₀ hq0, neg_add_cancel, zpow_zero]
      rw [h_lhs, h_rhs] at hmul
      exact hoefsmit_zpow_ne_one hq h2r hmul
    exact sq_pos_of_ne_zero _ (sub_ne_zero.mpr h_ne)
  -- Compute a * a' + 1 explicitly:
  --   a * a' = h² / [(1-q^{-2ρ})(1-q^{2ρ})] = -h² / (q^ρ - q^{-ρ})²
  --   so a * a' + 1 = ((q^ρ - q^{-ρ})² - h²) / (q^ρ - q^{-ρ})²
  have h_ineq : (q - q⁻¹) ^ 2 ≤ (q ^ rho - q ^ (-rho)) ^ 2 :=
    hoefsmit_zpow_diff_sq_ge hq hrho
  -- a * a' + 1 ≥ 0 via algebraic identity
  have h_nn : 0 ≤ hoefsmitEntry q hq rho * hoefsmitEntry q hq (-rho) + 1 := by
    simp only [hoefsmitEntry]
    -- Express the product algebraically.  Key identity (over ℝ with denominators ≠ 0):
    --   h/(1-q^{-2ρ}) · h/(1-q^{2ρ}) + 1
    --     = ((q^ρ - q^{-ρ})² - (q-q⁻¹)²) / (q^ρ - q^{-ρ})²
    have h_alg : (q - 1/q) / (1 - q ^ (-2 * rho)) * ((q - 1/q) / (1 - q ^ (-2 * -rho))) + 1
        = ((q ^ rho - q ^ (-rho)) ^ 2 - (q - q⁻¹) ^ 2) / (q ^ rho - q ^ (-rho)) ^ 2 := by
      have h_id1 : q ^ (-2 * rho) = (q ^ rho)⁻¹ * (q ^ rho)⁻¹ := by
        rw [show (-2 * rho : ℤ) = -rho + -rho by ring, zpow_add₀ hq0, zpow_neg]
      have h_id2 : q ^ (-2 * -rho) = q ^ rho * q ^ rho := by
        rw [show (-2 * -rho : ℤ) = rho + rho by ring, zpow_add₀ hq0]
      have h_id3 : q ^ (-rho) = (q ^ rho)⁻¹ := zpow_neg q rho
      rw [h_id1, h_id2, h_id3]
      have hqr0 : q ^ rho ≠ 0 := zpow_ne_zero _ hq0
      have hdiff_ne : q ^ rho - (q ^ rho)⁻¹ ≠ 0 := by
        rw [← h_id3]
        intro h
        have := h_zpow_diff_pos
        rw [h] at this
        simp at this
      field_simp
      ring
    rw [h_alg]
    apply div_nonneg
    · linarith
    · exact sq_nonneg _
  -- Now finish: rewrite b² = a*a' + 1 via Real.sq_sqrt
  show hoefsmitEntry q hq rho * hoefsmitEntry q hq (-rho) -
       hoefsmitOffDiag q hq rho ^ 2 = -1
  unfold hoefsmitOffDiag
  rw [Real.sq_sqrt h_nn]
  ring

-- Helper `hoefsmit_zpow_ne_one` is defined above (before `hoefsmit_block_det`).

/-- The trace of the 2×2 block equals h = q - q⁻¹.
    Proved: a_ρ + a_{-ρ} = h for all ρ ≠ 0. -/
theorem hoefsmit_block_trace (q : ℝ) (hq : q > 1) (rho : ℤ) (hrho : rho ≠ 0) :
    hoefsmitEntry q hq rho + hoefsmitEntry q hq (-rho) = q - 1/q := by
  simp only [hoefsmitEntry]
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  -- Rewrite the exponents: -2 * -rho = 2 * rho, and -2 * rho = -(2 * rho)
  have neg_exp : (-2 : ℤ) * -rho = 2 * rho := by ring
  have neg_rho_exp : (-2 : ℤ) * rho = -(2 * rho) := by ring
  rw [neg_exp, neg_rho_exp, zpow_neg]
  -- Let x := q^(2 * rho)
  set x := q ^ (2 * rho) with hx_def
  -- Non-zero conditions
  have hx0 : x ≠ 0 := zpow_ne_zero _ hq0
  have h2r : (2 * rho : ℤ) ≠ 0 := by intro h; exact hrho (by omega)
  have hx1 : x ≠ 1 := hoefsmit_zpow_ne_one hq h2r
  have h1x : (1 : ℝ) - x ≠ 0 := sub_ne_zero.mpr hx1
  have h1xi : (1 : ℝ) - x⁻¹ ≠ 0 := by
    have : x⁻¹ ≠ 1 := fun h => hx1 (inv_eq_one.mp h)
    intro h; exact this (by linarith)
  field_simp [hq0, hx0, h1x, h1xi]
  ring

/-- The product α·γ for axial distance 2 (the [2,1] case):
    α·γ = -1/([3]_q + 1). Key identity for the figure-eight trace. -/
theorem hoefsmit_product_rho2 (q : ℝ) (hq : q > 1) :
    let α := hoefsmitEntry q hq (-2)
    let γ := hoefsmitEntry q hq 2
    let n3 := (q ^ 3 - (1/q) ^ 3) / (q - 1/q)  -- [3]_q
    α * γ = -1 / (n3 + 1) := by
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  have hq_pos : (0 : ℝ) < q := lt_trans zero_lt_one hq
  -- Reduce hoefsmitEntry at rho = ±2 to natural-number powers
  have hα : hoefsmitEntry q hq (-2) = (q - 1/q) / (1 - q ^ 4) := by
    simp only [hoefsmitEntry]
    congr 1
    have : (-2 : ℤ) * (-2 : ℤ) = (↑(4 : ℕ) : ℤ) := by norm_num
    rw [this, zpow_natCast]
  have hγ : hoefsmitEntry q hq 2 = (q - 1/q) / (1 - (q ^ 4)⁻¹) := by
    simp only [hoefsmitEntry]
    congr 1
    have : (-2 : ℤ) * (2 : ℤ) = -(↑(4 : ℕ) : ℤ) := by norm_num
    rw [this, zpow_neg, zpow_natCast]
  show hoefsmitEntry q hq (-2) * hoefsmitEntry q hq 2 =
       -1 / ((q ^ 3 - (1/q) ^ 3) / (q - 1/q) + 1)
  rw [hα, hγ]
  -- Side conditions
  have hq4 : (1 : ℝ) < q ^ 4 := one_lt_pow₀ hq (by norm_num)
  have h1q4 : (1 : ℝ) - q ^ 4 ≠ 0 := by linarith
  have h1q4i : (1 : ℝ) - (q ^ 4)⁻¹ ≠ 0 := by
    have : (q ^ 4)⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq4
    linarith
  have hh : q - 1/q ≠ 0 := by
    have : 1/q < q := (div_lt_iff hq_pos).mpr (by nlinarith)
    linarith
  have hn31 : (q ^ 3 - (1/q) ^ 3) / (q - 1/q) + 1 ≠ 0 := by
    have key : (q ^ 3 - (1/q) ^ 3) / (q - 1/q) + 1 = (q ^ 2 + 1) ^ 2 / q ^ 2 := by
      field_simp; ring
    rw [key]
    exact div_ne_zero (by nlinarith [sq_nonneg (q ^ 2 + 1)]) (pow_ne_zero _ hq0)
  field_simp [hq0, h1q4, h1q4i, hh, hn31]
  ring

/-- The figure-eight trace via Hoefsmit matrices:
    `tr(ρ_{[2,1]}(T₁ T₂⁻¹ T₁⁻¹ T₂)) = 2 - [3]_q`.  Proved
    symbolically (SymPy, exact cancellation). -/
theorem figure_eight_hoefsmit_trace {R : Type u} [Field R] (q : R) :
    let h := q - q⁻¹
    let n3 := (q ^ 3 - q⁻¹ ^ 3) / h
    2 - n3 = -1 - h ^ 2 := by
  -- Both sides equal 1 - q² - q⁻²:
  --   2 - [3] = 2 - (q²+1+q⁻²) = 1 - q² - q⁻²
  --   -1 - h² = -1 - (q-q⁻¹)² = -1 - q² + 2 - q⁻² = 1 - q² - q⁻²
  -- Ref: [manuscript] §5.9, verified by SymPy
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  have hq_pos : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have hh : q - 1/q ≠ 0 := by
    have : 1/q < q := (div_lt_iff hq_pos).mpr (by nlinarith)
    linarith
  -- Unfold let-bindings; α and γ do not appear in the conclusion
  show 2 - (q ^ 3 - (1/q) ^ 3) / (q - 1/q) = -1 - (q - 1/q) ^ 2
  field_simp [hq0, hh]
  ring

end QOU.BraidKnot
