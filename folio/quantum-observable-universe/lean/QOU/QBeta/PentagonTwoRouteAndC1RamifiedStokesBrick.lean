/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Pentagon Two-Route Rigidity, V1 Bar-Even Tauberian Reflection, and C1 Ramified Stokes Bricks
(Beans: qou-524t, qou-7xvy, qou-f7g2, qou-l6fz, qou-odh5)

This module establishes the self-contained algebraic bricks for:
1. `v1_bar_even_tauberian_dilog_reflection_synthesis` (`qou-524t`):
   Given Euler's dilogarithm reflection functional equation
   `L_z + L_one_minus_z = pi_sq_over_6 - P_z` and the Tauberian partial-sum error
   bounds `|S_z - L_z| ≤ C1 * eps + C2 * delta_N` and
   `|S_one_minus_z - L_one_minus_z| ≤ C1 * eps + C2 * delta_N`, the paired
   bar-even Archimedean sum `S_z + S_one_minus_z + P_z` approximates `pi_sq_over_6`
   within `2 * (C1 * eps + C2 * delta_N)`, and at the self-dual point `L_half`
   where `L_one_minus_z = L_z`, one has `2 * L_z = pi_sq_over_6 - P_z`.
2. `phi_b_prod_divisor_rigidity_exponential_elimination` (`qou-7xvy`):
   For a doubly-periodic entire ratio parameterized on the logarithmic scale by a
   quadratic polynomial `ln_R(z) = alpha * z ^ 2 + beta * z + gamma`, periodicity
   at `z = 0` (`ln_R(w1) = ln_R(0)`) and `z = w1` (`ln_R(2 * w1) = ln_R(w1)`)
   for any nonzero period `w1 ≠ 0` forces `alpha = 0` and `beta = 0`, eliminating
   all exponential freedom (`ln_R(z) = gamma`).
3. `pentagon_two_route_a_omega_rigidity_lock` (`qou-f7g2`):
   When Faddeev-Volkov uniqueness identifies the Route-2 state-integral log-shift
   second difference `d2_route2 = A_omega * step ^ 2` with the Route-1 pentagon
   functional equation second difference `d2_route1 = c_pent * step ^ 2` where
   `c_pent = 3` and `step ≠ 0`, the shift coefficient is locked to `A_omega = 3`
   with zero residual `A_omega - 3 = 0`.
4. `watson_gevrey1_optimal_truncation_quadratic_completion` (`qou-l6fz`):
   At the optimal Gevrey-1 truncation order `N_star = 1 / (sigma * r)` (`sigma > 0`,
   `r > 0`), the normalized product `sigma * r * N_star = 1` yields the exact
   Watson exponential decay exponent `E_star = -N_star = -1 / (sigma * r) < 0`,
   and the quadratic Stirling-Gevrey envelope
   `E_quad(N) = -N_star + (sigma * r / 2) * (N - N_star) ^ 2` satisfies
   `E_quad(N) ≥ -1 / (sigma * r)` for all `N`.
5. `c1_ramified_edge_polynomial_and_stokes_connection_determinant` (`qou-odh5`):
   For the ramified `d = 2` C1 operator edge polynomial `p ^ 4 * T ^ 2 - (p ^ 2 - 1)`
   with `q = p ^ 2` (`p ≠ 0`) and `s ^ 2 = q - 1 > 0`, the two leading-block
   eigenvalues `B1 = s / q` and `B2 = -s / q` satisfy `p ^ 4 * B1 ^ 2 - (p ^ 2 - 1) = 0`
   and `p ^ 4 * B2 ^ 2 - (p ^ 2 - 1) = 0`, with spectral gap
   `(B1 - B2) ^ 2 = 4 * (q - 1) / q ^ 2 > 0`, while the `2 × 2` Stokes connection
   product has unit determinant `(1 + u_plus * u_minus) * 1 - u_plus * u_minus = 1`
   and trace defect `(2 + u_plus * u_minus) - 2 = u_plus * u_minus`.
-/

import Mathlib.Tactic

namespace QOU.QBeta.PentagonTwoRouteAndC1RamifiedStokesBrick

/-- Logarithmic quadratic ansatz `alpha * z ^ 2 + beta * z + gamma` for an entire
unit ratio of order at most 2 (`qou-7xvy`). -/
def entireLogQuadraticAnsatz (alpha beta gamma z : ℝ) : ℝ :=
  alpha * z ^ 2 + beta * z + gamma

/-- Quadratic Stirling-Gevrey truncation envelope around the optimal truncation
order `N_star = 1 / (sigma * r)` (`qou-l6fz`). -/
noncomputable def watsonGevreyQuadraticEnvelope (sigma r N : ℝ) : ℝ :=
  -(1 / (sigma * r)) + (sigma * r / 2) * (N - 1 / (sigma * r)) ^ 2

/-- **Theorem 1 (`qou-524t`)**: Bar-even Tauberian partial-sum exchange and Euler
dilog reflection synthesis, plus self-dual midpoint identity when `L_one_minus_z = L_z`. -/
theorem v1_bar_even_tauberian_dilog_reflection_synthesis
    (S_z S_one_minus_z L_z L_one_minus_z P_z pi_sq_over_6 C1 C2 eps delta_N : ℝ)
    (h_refl : L_z + L_one_minus_z = pi_sq_over_6 - P_z)
    (h_err1 : |S_z - L_z| ≤ C1 * eps + C2 * delta_N)
    (h_err2 : |S_one_minus_z - L_one_minus_z| ≤ C1 * eps + C2 * delta_N) :
    |(S_z + S_one_minus_z + P_z) - pi_sq_over_6| ≤ 2 * (C1 * eps + C2 * delta_N) ∧
      (L_one_minus_z = L_z → 2 * L_z = pi_sq_over_6 - P_z) := by
  have h_decomp :
      (S_z + S_one_minus_z + P_z) - pi_sq_over_6 =
        (S_z - L_z) + (S_one_minus_z - L_one_minus_z) := by
    linarith [h_refl]
  have h_tri :
      |(S_z - L_z) + (S_one_minus_z - L_one_minus_z)| ≤
        |S_z - L_z| + |S_one_minus_z - L_one_minus_z| :=
    abs_add_le (S_z - L_z) (S_one_minus_z - L_one_minus_z)
  have h_bound :
      |(S_z + S_one_minus_z + P_z) - pi_sq_over_6| ≤
        2 * (C1 * eps + C2 * delta_N) := by
    rw [h_decomp]
    linarith [h_tri, h_err1, h_err2]
  have h_mid : L_one_minus_z = L_z → 2 * L_z = pi_sq_over_6 - P_z := by
    intro h_sym
    linarith [h_refl, h_sym]
  exact ⟨h_bound, h_mid⟩

/-- **Theorem 2 (`qou-7xvy`)**: Periodicity of `entireLogQuadraticAnsatz alpha beta gamma`
along two consecutive lattice steps `0 → w1 → 2 * w1` (`w1 ≠ 0`) eliminates both
quadratic and linear exponential parameters (`alpha = 0` and `beta = 0`), reducing
the ansatz to the constant `gamma`. -/
theorem phi_b_prod_divisor_rigidity_exponential_elimination
    (alpha beta gamma w1 z : ℝ)
    (hw1 : w1 ≠ 0)
    (h_per1 : entireLogQuadraticAnsatz alpha beta gamma w1 =
              entireLogQuadraticAnsatz alpha beta gamma 0)
    (h_per2 : entireLogQuadraticAnsatz alpha beta gamma (2 * w1) =
              entireLogQuadraticAnsatz alpha beta gamma w1) :
    alpha = 0 ∧ beta = 0 ∧ entireLogQuadraticAnsatz alpha beta gamma z = gamma := by
  unfold entireLogQuadraticAnsatz at h_per1 h_per2 ⊢
  have h_diff2 : 2 * alpha * w1 ^ 2 = 0 := by
    linarith [h_per1, h_per2]
  have hw1_sq : w1 ^ 2 ≠ 0 := pow_ne_zero 2 hw1
  have h_alpha : alpha = 0 := by
    have h1 : alpha * w1 ^ 2 = 0 := by linarith [h_diff2]
    exact (mul_eq_zero.mp h1).resolve_right hw1_sq
  have h_beta_w1 : beta * w1 = 0 := by
    nlinarith [h_per1, h_alpha]
  have h_beta : beta = 0 := (mul_eq_zero.mp h_beta_w1).resolve_right hw1
  have h_const : alpha * z ^ 2 + beta * z + gamma = gamma := by
    rw [h_alpha, h_beta]
    ring
  exact ⟨h_alpha, h_beta, h_const⟩

/-- **Theorem 3 (`qou-f7g2`)**: Two-route `A_ω` rigidity lock: when Faddeev-Volkov
uniqueness equates the Route-2 state-integral logarithmic second difference
`d2_route2 = A_omega * step ^ 2` with the Route-1 pentagon second difference
`d2_route1 = c_pent * step ^ 2` (`c_pent = 3`, `step ≠ 0`), one obtains `A_omega = 3`. -/
theorem pentagon_two_route_a_omega_rigidity_lock
    (d2_route1 d2_route2 c_pent A_omega step : ℝ)
    (h_r1 : d2_route1 = c_pent * step ^ 2)
    (h_r2 : d2_route2 = A_omega * step ^ 2)
    (h_fv_uniq : d2_route2 = d2_route1)
    (h_cpent : c_pent = 3)
    (h_step : step ≠ 0) :
    A_omega = 3 ∧ A_omega - 3 = 0 := by
  have h_step_sq : step ^ 2 ≠ 0 := pow_ne_zero 2 h_step
  have h_eq_sq : A_omega * step ^ 2 = 3 * step ^ 2 := by
    linarith [h_r1, h_r2, h_fv_uniq, h_cpent]
  have h_a : A_omega = 3 := mul_right_cancel₀ h_step_sq h_eq_sq
  exact ⟨h_a, by linarith [h_a]⟩

/-- **Theorem 4 (`qou-l6fz`)**: At the optimal Gevrey-1 truncation `N_star = 1 / (sigma * r)`
(`sigma > 0`, `r > 0`), the normalized scale `sigma * r * N_star = 1`, the quadratic
Stirling-Gevrey decay exponent attains `-1 / (sigma * r) < 0`, and every truncation
order `N` satisfies `watsonGevreyQuadraticEnvelope sigma r N ≥ -1 / (sigma * r)`. -/
theorem watson_gevrey1_optimal_truncation_quadratic_completion
    (sigma r N_star N : ℝ)
    (hsigma : 0 < sigma)
    (hr : 0 < r)
    (hN_star : N_star = 1 / (sigma * r)) :
    sigma * r * N_star = 1 ∧
      watsonGevreyQuadraticEnvelope sigma r N_star = -(1 / (sigma * r)) ∧
      watsonGevreyQuadraticEnvelope sigma r N_star < 0 ∧
      -(1 / (sigma * r)) ≤ watsonGevreyQuadraticEnvelope sigma r N := by
  have hsr_pos : 0 < sigma * r := mul_pos hsigma hr
  have hsr_ne : sigma * r ≠ 0 := ne_of_gt hsr_pos
  have h_prod : sigma * r * N_star = 1 := by
    rw [hN_star]
    field_simp [hsr_ne]
  have h_at_star :
      watsonGevreyQuadraticEnvelope sigma r N_star = -(1 / (sigma * r)) := by
    unfold watsonGevreyQuadraticEnvelope
    rw [hN_star]
    ring
  have h_neg : watsonGevreyQuadraticEnvelope sigma r N_star < 0 := by
    rw [h_at_star]
    have h_inv_pos : 0 < 1 / (sigma * r) := one_div_pos.mpr hsr_pos
    linarith
  have h_nonneg :
      0 ≤ (sigma * r / 2) * (N - 1 / (sigma * r)) ^ 2 := by
    exact mul_nonneg (by positivity) (sq_nonneg _)
  have h_lower :
      -(1 / (sigma * r)) ≤ watsonGevreyQuadraticEnvelope sigma r N := by
    unfold watsonGevreyQuadraticEnvelope
    linarith [h_nonneg]
  exact ⟨h_prod, h_at_star, h_neg, h_lower⟩

/-- **Theorem 5 (`qou-odh5`)**: Ramified `d = 2` C1 edge polynomial root verification
for `B1 = s / q` and `B2 = -s / q` (`q = p ^ 2`, `s ^ 2 = q - 1 > 0`), positive
spectral separation `(B1 - B2) ^ 2 = 4 * (q - 1) / q ^ 2 > 0`, and unit determinant
plus trace-defect identity for the `2 × 2` Stokes connection matrix product. -/
theorem c1_ramified_edge_polynomial_and_stokes_connection_determinant
    (p q s B1 B2 u_plus u_minus : ℝ)
    (hp : p ≠ 0)
    (hq : q = p ^ 2)
    (hs_sq : s ^ 2 = q - 1)
    (hq1_pos : 0 < q - 1)
    (hB1 : B1 = s / q)
    (hB2 : B2 = -s / q) :
    p ^ 4 * B1 ^ 2 - (p ^ 2 - 1) = 0 ∧
      p ^ 4 * B2 ^ 2 - (p ^ 2 - 1) = 0 ∧
      B1 + B2 = 0 ∧
      (B1 - B2) ^ 2 = 4 * (q - 1) / q ^ 2 ∧
      0 < (B1 - B2) ^ 2 ∧
      (1 + u_plus * u_minus) * 1 - u_plus * u_minus = 1 ∧
      (2 + u_plus * u_minus) - 2 = u_plus * u_minus := by
  have hq_ne : q ≠ 0 := by
    rw [hq]
    exact pow_ne_zero 2 hp
  have h_edge1 : p ^ 4 * B1 ^ 2 - (p ^ 2 - 1) = 0 := by
    rw [hB1]
    have h_p4 : p ^ 4 = q ^ 2 := by
      rw [hq]
      ring
    have h_p2 : p ^ 2 = q := hq.symm
    rw [h_p4, h_p2]
    field_simp [hq_ne]
    linarith [hs_sq]
  have h_edge2 : p ^ 4 * B2 ^ 2 - (p ^ 2 - 1) = 0 := by
    rw [hB2]
    have h_p4 : p ^ 4 = q ^ 2 := by
      rw [hq]
      ring
    have h_p2 : p ^ 2 = q := hq.symm
    rw [h_p4, h_p2]
    field_simp [hq_ne]
    linarith [hs_sq]
  have h_tr : B1 + B2 = 0 := by
    rw [hB1, hB2]
    ring
  have h_gap : (B1 - B2) ^ 2 = 4 * (q - 1) / q ^ 2 := by
    rw [hB1, hB2]
    field_simp [hq_ne]
    linarith [hs_sq]
  have h_gap_pos : 0 < (B1 - B2) ^ 2 := by
    rw [h_gap]
    have hq2_pos : 0 < q ^ 2 := sq_pos_of_ne_zero hq_ne
    exact div_pos (by linarith [hq1_pos]) hq2_pos
  have h_det : (1 + u_plus * u_minus) * 1 - u_plus * u_minus = 1 := by ring
  have h_tr_def : (2 + u_plus * u_minus) - 2 = u_plus * u_minus := by ring
  exact ⟨h_edge1, h_edge2, h_tr, h_gap, h_gap_pos, h_det, h_tr_def⟩

end QOU.QBeta.PentagonTwoRouteAndC1RamifiedStokesBrick
