/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Dilog Cusp Cancellation, Half-Binomial Newton Slope, and Borel Proper-Time Bricks
(Beans: qou-03lh, qou-7b7v, qou-gkco, qou-icx5, qou-q04o)

This module establishes the self-contained algebraic bricks for:
1. `dilog_part_b_kashaev_conjugate_pairing_cancellation` (`qou-03lh`):
   When conjugate Kashaev state-sum cusps `V_plus = (L_x - pi_sq_over_6, +Phi_cusp)`
   and `V_minus = (L_x - pi_sq_over_6, -Phi_cusp)` are paired across mirror sectors,
   their imaginary cusp phases cancel identically (`Phi_cusp + (-Phi_cusp) = 0`)
   and their real parts sum to `2 * L_x - 2 * pi_sq_over_6`.
2. `newton_polygon_half_binomial_theta_second_difference` (`qou-7b7v`):
   For the Tier-2 #4 quadratic q-Gevrey exponent `theta(m) = (1/2) * C(m, 2) = m * (m - 1) / 4`,
   the first forward difference is `theta(m + 1) - theta(m) = m / 2`, the two-step
   C1 recurrence shift is `theta(m + 2) - theta(m) = m + 1 / 2`, and the second
   forward difference is identically the Newton slope
   `theta(m + 2) - 2 * theta(m + 1) + theta(m) = 1 / 2`.
3. `complex_dilog_reflection_and_inversion_compatibility` (`qou-gkco`):
   Combining Euler's dilogarithm reflection identity
   `L_z + L_one_minus_z = pi_sq_over_6 - P_refl` and inversion identity
   `L_z + L_inv_z = -pi_sq_over_6 - P_inv` eliminates `L_z` to yield the exact
   compatibility relation `L_one_minus_z - L_inv_z = 2 * pi_sq_over_6 - P_refl + P_inv`,
   and at the self-inverse point `z = -1` (`L_inv_z = L_z` with `P_inv = 0`) locks
   `L_z = -pi_sq_over_6 / 2` (`= -π² / 12`).
4. `dilog_part_b_cusp_linear_pole_and_pi_sq_third_cancellation` (`qou-icx5`):
   When the unregularized Part-B sum decomposes into the dilog core `L_x - pi_sq_over_6`,
   the `iπ`-tower cusp contribution `-pi_sq_over_6`, the singular linear pole
   `c_pole / (q - 1)` (`q - 1 ≠ 0`), and remainder `R_n`, subtracting the counterterm
   `c_pole / (q - 1)` yields `reg_n = L_x - 2 * pi_sq_over_6 + R_n` (`= Li₂(x) - π²/3 + R_n`)
   with exact error `|reg_n - (L_x - 2 * pi_sq_over_6)| = |R_n|`.
5. `borel_variable_loop_proper_time_laplace_scaling_bijection` (`qou-q04o`):
   Under the linear proper-time rescaling `tau = alpha * zeta` (`alpha > 0`, `hbar > 0`),
   the Borel Laplace exponent `zeta / hbar` equals `(1 / (alpha * hbar)) * tau`,
   the inverse map recovers `tau / alpha = zeta`, and matching a nonzero Borel
   singularity location `zeta_star ≠ 0` to the physical Schwinger proper-time
   threshold `tau_star = zeta_star` uniquely pins `alpha = 1`.
-/

import Mathlib.Tactic

namespace QOU.QBeta.DilogCuspCancellationAndBorelProperTimeBrick

/-- Half-binomial quadratic q-Gevrey exponent `theta(m) = (1/2) * C(m, 2) = m * (m - 1) / 4`
for the C1 recurrence (`qou-7b7v`). -/
noncomputable def halfBinomialTheta (m : ℝ) : ℝ :=
  m * (m - 1) / 4

/-- **Theorem 1 (`qou-03lh`)**: Conjugate Kashaev cusp pairing cancels the
oscillatory imaginary cusp phase `Phi_cusp` identically and doubles the Part-A/B
dilogarithm core `L_x - pi_sq_over_6`. -/
theorem dilog_part_b_kashaev_conjugate_pairing_cancellation
    (L_x pi_sq_over_6 Phi_cusp V_re_plus V_re_minus V_im_plus V_im_minus : ℝ)
    (h_re_p : V_re_plus = L_x - pi_sq_over_6)
    (h_re_m : V_re_minus = L_x - pi_sq_over_6)
    (h_im_p : V_im_plus = Phi_cusp)
    (h_im_m : V_im_minus = -Phi_cusp) :
    V_im_plus + V_im_minus = 0 ∧
      V_re_plus + V_re_minus = 2 * L_x - 2 * pi_sq_over_6 ∧
      (V_re_plus + V_re_minus) + 2 * pi_sq_over_6 = 2 * L_x := by
  have h_im : V_im_plus + V_im_minus = 0 := by
    linarith [h_im_p, h_im_m]
  have h_re : V_re_plus + V_re_minus = 2 * L_x - 2 * pi_sq_over_6 := by
    linarith [h_re_p, h_re_m]
  have h_core : (V_re_plus + V_re_minus) + 2 * pi_sq_over_6 = 2 * L_x := by
    linarith [h_re]
  exact ⟨h_im, h_re, h_core⟩

/-- **Theorem 2 (`qou-7b7v`)**: Exact finite-difference identities for the
half-binomial q-Gevrey exponent `halfBinomialTheta m = m * (m - 1) / 4`, locking
the two-step C1 shift `m + 1 / 2` and the Newton-polygon second difference `1 / 2`. -/
theorem newton_polygon_half_binomial_theta_second_difference
    (m : ℝ) :
    halfBinomialTheta (m + 1) - halfBinomialTheta m = m / 2 ∧
      halfBinomialTheta (m + 2) - halfBinomialTheta m = m + 1 / 2 ∧
      halfBinomialTheta (m + 2) - 2 * halfBinomialTheta (m + 1) + halfBinomialTheta m = 1 / 2 := by
  unfold halfBinomialTheta
  refine ⟨by ring, by ring, by ring⟩

/-- **Theorem 3 (`qou-gkco`)**: Compatibility of the dilogarithm reflection and
inversion functional equations, plus the `z = -1` self-inverse evaluation
`L(-1) = -π² / 12` (`= -pi_sq_over_6 / 2`). -/
theorem complex_dilog_reflection_and_inversion_compatibility
    (L_z L_one_minus_z L_inv_z pi_sq_over_6 P_refl P_inv : ℝ)
    (h_refl : L_z + L_one_minus_z = pi_sq_over_6 - P_refl)
    (h_inv : L_z + L_inv_z = -pi_sq_over_6 - P_inv) :
    L_one_minus_z - L_inv_z = 2 * pi_sq_over_6 - P_refl + P_inv ∧
      (L_inv_z = L_z ∧ P_inv = 0 → L_z = -pi_sq_over_6 / 2) := by
  have h_compat : L_one_minus_z - L_inv_z = 2 * pi_sq_over_6 - P_refl + P_inv := by
    linarith [h_refl, h_inv]
  have h_neg_one : L_inv_z = L_z ∧ P_inv = 0 → L_z = -pi_sq_over_6 / 2 := by
    rintro ⟨h_eq, h_p0⟩
    linarith [h_inv, h_eq, h_p0]
  exact ⟨h_compat, h_neg_one⟩

/-- **Theorem 4 (`qou-icx5`)**: Part-B cusp linear-pole counterterm cancellation
and `π² / 3` (`= 2 * pi_sq_over_6`) assembly from the Part-A `-π² / 6` core and
the `iπ`-tower `-π² / 6` cusp shift. -/
theorem dilog_part_b_cusp_linear_pole_and_pi_sq_third_cancellation
    (unreg_n reg_n L_x pi_sq_over_6 c_pole q R_n : ℝ)
    (hq1 : q - 1 ≠ 0)
    (h_unreg : unreg_n = (L_x - pi_sq_over_6) - pi_sq_over_6 + c_pole / (q - 1) + R_n)
    (h_reg : reg_n = unreg_n - c_pole / (q - 1)) :
    reg_n = L_x - 2 * pi_sq_over_6 + R_n ∧
      |reg_n - (L_x - 2 * pi_sq_over_6)| = |R_n| := by
  have h_pole_cancel : reg_n = L_x - 2 * pi_sq_over_6 + R_n := by
    linarith [h_unreg, h_reg]
  have h_diff : reg_n - (L_x - 2 * pi_sq_over_6) = R_n := by
    linarith [h_pole_cancel]
  exact ⟨h_pole_cancel, by rw [h_diff]⟩

/-- **Theorem 5 (`qou-q04o`)**: Borel-variable to loop-proper-time Laplace scaling
bijection `tau = alpha * zeta` (`alpha > 0`, `hbar > 0`) and unique unit-scale pin
`alpha = 1` when a nonzero Borel singularity `zeta_star ≠ 0` matches the physical
proper-time threshold `tau_star = zeta_star`. -/
theorem borel_variable_loop_proper_time_laplace_scaling_bijection
    (zeta tau alpha hbar zeta_star tau_star : ℝ)
    (halpha : 0 < alpha)
    (hhbar : 0 < hbar)
    (htau : tau = alpha * zeta)
    (htau_star : tau_star = alpha * zeta_star)
    (hzeta_star : zeta_star ≠ 0) :
    zeta / hbar = (1 / (alpha * hbar)) * tau ∧
      tau / alpha = zeta ∧
      (tau_star = zeta_star → alpha = 1) := by
  have halpha_ne : alpha ≠ 0 := ne_of_gt halpha
  have hhbar_ne : hbar ≠ 0 := ne_of_gt hhbar
  have h_laplace : zeta / hbar = (1 / (alpha * hbar)) * tau := by
    rw [htau]
    field_simp [halpha_ne, hhbar_ne]
  have h_inv : tau / alpha = zeta := by
    rw [htau]
    exact mul_div_cancel_left₀ zeta halpha_ne
  have h_pin : tau_star = zeta_star → alpha = 1 := by
    intro h_match
    have h1 : alpha * zeta_star = 1 * zeta_star := by
      linarith [htau_star, h_match]
    exact mul_right_cancel₀ hzeta_star h1
  exact ⟨h_laplace, h_inv, h_pin⟩

end QOU.QBeta.DilogCuspCancellationAndBorelProperTimeBrick
