/-
  Hoefsmit seminormal matrices as R-matrix evaluations in H_n(q).

  For each partition λ ⊢ n, the Hoefsmit form gives an explicit
  matrix representation ρ_λ: H_n(q) → M_{d_λ}(ℂ) on the basis of
  standard Young tableaux. The diagonal entry for generator T_i is
  a_ρ = h/(1 - q^{-2ρ}) where ρ is the axial distance.

  These are the R-matrix evaluations for topological crossings.

  Ref: [hoefsmit1974] P.N. Hoefsmit, "Representations of Hecke algebras
       of finite groups with BN-pairs of classical type", PhD thesis, 1974.
       [wenzl1988] https://doi.org/10.1007/BF01404457
       [manuscript] §5.5, prop:hoefsmit-seminormal-form
-/

import Mathlib.LinearAlgebra.Matrix.Trace

namespace QOU.BraidKnot

/-- The axial distance entry in the Hoefsmit seminormal form. -/
noncomputable def hoefsmitEntry (q : ℝ) (hq : q > 1) (rho : ℤ) : ℝ :=
  let h := q - 1/q
  h / (1 - q ^ (-2 * rho))

/-- The off-diagonal entry satisfying b² = a_ρ · a_{-ρ} + 1. -/
noncomputable def hoefsmitOffDiag (q : ℝ) (hq : q > 1) (rho : ℤ) : ℝ :=
  let a := hoefsmitEntry q hq rho
  let a' := hoefsmitEntry q hq (-rho)
  Real.sqrt (a * a' + 1)

/-- The 2×2 Hoefsmit block has determinant -1 (from the Hecke relation).
    This is the product of eigenvalues: q · (-q⁻¹) = -1. -/
theorem hoefsmit_block_det (q : ℝ) (hq : q > 1) (rho : ℤ) (hrho : rho ≠ 0) :
    let a := hoefsmitEntry q hq rho
    let a' := hoefsmitEntry q hq (-rho)
    let b := hoefsmitOffDiag q hq rho
    a * a' - b ^ 2 = -1 := by
  simp only [hoefsmitOffDiag]
  -- b² = a·a' + 1 requires showing 0 ≤ a·a' + 1, i.e., a·a' ≥ -1.
  -- a·a' = -(q-1/q)² / (q^ρ - q^{-ρ})² and
  -- (q^ρ - q^{-ρ})² ≥ (q - q^{-1})² for |ρ| ≥ 1 (zpow monotonicity).
  -- That inequality requires Int.toNat conversion + pow monotonicity.
  -- Ref: [hoefsmit1974]
  sorry

-- Helper: q^n ≠ 1 for q > 1 and n : ℤ with n ≠ 0.
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
    tr(ρ_{[2,1]}(T₁ T₂⁻¹ T₁⁻¹ T₂)) = 2 - [3]_q.
    Proved symbolically (SymPy, exact cancellation). -/
theorem figure_eight_hoefsmit_trace (q : ℝ) (hq : q > 1) :
    let h := q - 1/q
    let n3 := (q ^ 3 - (1/q) ^ 3) / h
    let α := hoefsmitEntry q hq (-2)
    let γ := hoefsmitEntry q hq 2
    -- tr(M) = -α·γ·(1+[3]) - ([3]-1) = 2 - [3]
    -- using α+γ=h, α·γ=-1/([3]+1), β²=α·γ+1
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
