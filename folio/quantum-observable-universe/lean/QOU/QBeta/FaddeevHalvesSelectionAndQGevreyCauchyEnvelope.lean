/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Faddeev Halves Selection, Divisor Cancellation, and q-Gevrey Cauchy Envelope
(Beans: qou-cons, qou-jplv, qou-lv34, qou-q95i, qou-uvqk)

This module establishes the self-contained algebraic bricks for:
1. `faddeev_halves_divisor_cancellation_and_scalar_rigidity` (`qou-cons`):
   When two meromorphic Faddeev solutions split into entire numerator/denominator
   products `Φ = N_Φ / D_Φ` and `Ψ = N_Ψ / D_Ψ` sharing divisors up to
   nonvanishing entire factors `N_Ψ = e_N * N_Φ` and `D_Ψ = e_D * D_Φ`
   (`N_Φ ≠ 0`, `D_Φ ≠ 0`, `e_D ≠ 0`), the ratio `Ψ / Φ` cancels the shared
   divisor factors identically to `e_N / e_D`, and if `e_N / e_D = c` is a scalar
   constant, then `Ψ = c * Φ`.
2. `branch_point_scaling_gap_and_quadratic_power_bound` (`qou-jplv`):
   Along the explicit branch-point approach `x * q_pow_n = 1 - 1 / m` (`m > 0`),
   the gap to the branch cut is `1 - x * q_pow_n = 1 / m`, and under the linear
   scaling bound `q - 1 ≤ L / m` (`L > 0`) one has `(1 / L) * (q - 1) ≤ 1 - x * q_pow_n`;
   moreover, in the quadratic badly-approximable regime `q - 1 ≤ 1 / j` (`j > 0`,
   `q - 1 ≥ 0`) with `1 - x * q_pow_n ≥ c0 / j ^ 2` (`c0 ≥ 0`), one obtains the
   power-law lower bound `c0 * (q - 1) ^ 2 ≤ 1 - x * q_pow_n`.
3. `faddeev_rigidity_normalization_pin_and_a_omega_three` (`qou-lv34`):
   Under the Liouville scalar proportionality `Ψ(z) = c * Φ(z)` (`h_prop : psi_z = c * phi_z`,
   `h_prop0 : psi_0 = c * phi_0`) together with the origin normalization pin
   `psi_0 = phi_0` and `phi_0 ≠ 0`, the proportionality constant is forced to
   `c = 1`, yielding `psi_z = phi_z` and locking the logarithmic shift coefficient
   `A_ω(Ψ) = A_ω(Φ) = 3`.
4. `faddeev_dual_shift_ratio_invariance` (`qou-q95i`):
   For any pair of meromorphic functions satisfying the dual shift equation
   `Φ_shift = s * Φ` and `Ψ_shift = s * Ψ` with common nonvanishing multiplier
   `s ≠ 0` and `Φ ≠ 0`, the ratio `R = Ψ / Φ` is strictly shift-invariant:
   `Ψ_shift / Φ_shift = Ψ / Φ` and `Ψ_shift / Φ_shift - Ψ / Φ = 0`.
5. `q_gevrey_cauchy_mul_quadratic_envelope_identity` (`qou-uvqk`):
   For positive q-Gevrey orders `s + t > 0`, the Cauchy-product quadratic
   convolution exponent `s * i ^ 2 + t * (n - i) ^ 2` satisfies the exact
   completion-of-the-square identity
   `s * i ^ 2 + t * (n - i) ^ 2 = (s * t / (s + t)) * n ^ 2 + (s + t) * (i - (t / (s + t)) * n) ^ 2`,
   proving that the harmonic-mean order `cauchyEnvelope(s, t) = s * t / (s + t)`
   is the exact quadratic lower envelope (`(s * t / (s + t)) * n ^ 2 ≤ s * i ^ 2 + t * (n - i) ^ 2`).
-/

import Mathlib.Tactic

namespace QOU.QBeta.FaddeevHalvesSelectionAndQGevreyCauchyEnvelope

/-- Harmonic-mean q-Gevrey Cauchy convolution order `s * t / (s + t)` (`qou-uvqk`). -/
noncomputable def qGevreyCauchyEnvelopeOrder (s t : ℝ) : ℝ :=
  (s * t) / (s + t)

/-- Optimal continuous index share `t / (s + t) * n` where the quadratic Cauchy
convolution exponent attains its harmonic-mean minimum (`qou-uvqk`). -/
noncomputable def qGevreyCauchySaddleIndex (s t n : ℝ) : ℝ :=
  (t / (s + t)) * n

/-- **Theorem 1 (`qou-cons`)**: Divisor cancellation for two Faddeev solutions
sharing zero and pole lattices (`N_Ψ = e_N * N_Φ`, `D_Ψ = e_D * D_Φ`), and scalar
rigidity when the entire unit ratio `e_N / e_D = c` is constant. -/
theorem faddeev_halves_divisor_cancellation_and_scalar_rigidity
    (phi psi n_phi d_phi n_psi d_psi e_n e_d c : ℝ)
    (h_phi : phi = n_phi / d_phi)
    (h_psi : psi = n_psi / d_psi)
    (h_n : n_psi = e_n * n_phi)
    (h_d : d_psi = e_d * d_phi)
    (hn0 : n_phi ≠ 0)
    (hd0 : d_phi ≠ 0)
    (hed0 : e_d ≠ 0)
    (h_const : e_n / e_d = c) :
    psi / phi = e_n / e_d ∧ psi = c * phi := by
  have h_ratio : psi / phi = e_n / e_d := by
    rw [h_psi, h_phi, h_n, h_d]
    field_simp [hn0, hd0, hed0]
  have h_phi_ne : phi ≠ 0 := by
    rw [h_phi]
    exact div_ne_zero hn0 hd0
  have h_scalar : psi = c * phi := by
    have h1 : psi / phi = c := h_ratio.trans h_const
    exact (div_eq_iff h_phi_ne).mp h1
  exact ⟨h_ratio, h_scalar⟩

/-- **Theorem 2 (`qou-jplv`)**: Branch-point scaling gap identity along
`x * q_pow_n = 1 - 1 / m` and quadratic power-law lower bound in the
badly-approximable regime `q - 1 ≤ 1 / j` with `1 - x * q_pow_n ≥ c0 / j ^ 2`. -/
theorem branch_point_scaling_gap_and_quadratic_power_bound
    (x q_pow_n m q L j c0 : ℝ)
    (hm : 0 < m)
    (h_seq : x * q_pow_n = 1 - 1 / m)
    (hL : 0 < L)
    (h_lin : q - 1 ≤ L / m)
    (hj : 0 < j)
    (hq1 : 0 ≤ q - 1)
    (hc0 : 0 ≤ c0)
    (h_j_bound : q - 1 ≤ 1 / j)
    (h_quad_gap : c0 / j ^ 2 ≤ 1 - x * q_pow_n) :
    1 - x * q_pow_n = 1 / m ∧
      (1 / L) * (q - 1) ≤ 1 - x * q_pow_n ∧
      c0 * (q - 1) ^ 2 ≤ 1 - x * q_pow_n := by
  have h_gap : 1 - x * q_pow_n = 1 / m := by linarith [h_seq]
  have hL_ne : L ≠ 0 := ne_of_gt hL
  have h_lin_gap : (1 / L) * (q - 1) ≤ 1 - x * q_pow_n := by
    rw [h_gap]
    have h1 : (1 / L) * (q - 1) ≤ (1 / L) * (L / m) :=
      mul_le_mul_of_nonneg_left h_lin (by positivity)
    have h2 : (1 / L) * (L / m) = 1 / m := by
      field_simp [hL_ne]
    linarith [h1, h2]
  have h_sq : (q - 1) ^ 2 ≤ (1 / j) ^ 2 := by
    nlinarith [h_j_bound, hq1, one_div_pos.mpr hj]
  have hj_ne : j ≠ 0 := ne_of_gt hj
  have h_sq_eq : (1 / j) ^ 2 = 1 / j ^ 2 := by ring
  have h_c0_sq : c0 * (q - 1) ^ 2 ≤ c0 / j ^ 2 := by
    have h3 : c0 * (q - 1) ^ 2 ≤ c0 * (1 / j) ^ 2 :=
      mul_le_mul_of_nonneg_left h_sq hc0
    have h4 : c0 * (1 / j) ^ 2 = c0 / j ^ 2 := by
      rw [h_sq_eq]
      ring
    linarith [h3, h4]
  exact ⟨h_gap, h_lin_gap, le_trans h_c0_sq h_quad_gap⟩

/-- **Theorem 3 (`qou-lv34`)**: Normalization pin `Ψ(0) = Φ(0) ≠ 0` under
Liouville scalar proportionality `Ψ = c * Φ` forces `c = 1`, `Ψ(z) = Φ(z)`,
and locks the logarithmic shift coefficient `A_ω(Ψ) = 3`. -/
theorem faddeev_rigidity_normalization_pin_and_a_omega_three
    (phi_0 psi_0 phi_z psi_z c a_omega_phi a_omega_psi : ℝ)
    (h_prop0 : psi_0 = c * phi_0)
    (h_propz : psi_z = c * phi_z)
    (h_pin0 : psi_0 = phi_0)
    (h_phi0_ne : phi_0 ≠ 0)
    (h_a_phi : a_omega_phi = 3)
    (h_a_transfer : psi_z = phi_z → a_omega_psi = a_omega_phi) :
    c = 1 ∧ psi_z = phi_z ∧ a_omega_psi = 3 := by
  have hc : c = 1 := by
    have h1 : c * phi_0 = 1 * phi_0 := by linarith [h_prop0, h_pin0]
    exact mul_right_cancel₀ h_phi0_ne h1
  have h_eq_z : psi_z = phi_z := by
    rw [h_propz, hc, one_mul]
  have h_a_psi : a_omega_psi = 3 := by
    rw [h_a_transfer h_eq_z, h_a_phi]
  exact ⟨hc, h_eq_z, h_a_psi⟩

/-- **Theorem 4 (`qou-q95i`)**: Dual shift ratio invariance (`hibinv` algebraic
core): when `Φ` and `Ψ` share the same nonvanishing shift multiplier `s`
(`Φ_shift = s * Φ`, `Ψ_shift = s * Ψ`), their ratio `Ψ / Φ` is strictly
shift-invariant (`Ψ_shift / Φ_shift = Ψ / Φ`). -/
theorem faddeev_dual_shift_ratio_invariance
    (phi psi phi_shift psi_shift s : ℝ)
    (h_phi_shift : phi_shift = s * phi)
    (h_psi_shift : psi_shift = s * psi)
    (hs : s ≠ 0)
    (hphi : phi ≠ 0) :
    psi_shift / phi_shift = psi / phi ∧
      psi_shift / phi_shift - psi / phi = 0 := by
  have h_inv : psi_shift / phi_shift = psi / phi := by
    rw [h_psi_shift, h_phi_shift]
    exact mul_div_mul_left psi phi hs
  exact ⟨h_inv, sub_eq_zero.mpr h_inv⟩

/-- **Theorem 5 (`qou-uvqk`)**: Exact completion of the square for the q-Gevrey
Cauchy product quadratic exponent `s * i ^ 2 + t * (n - i) ^ 2`, showing that
`qGevreyCauchyEnvelopeOrder s t * n ^ 2 = (s * t / (s + t)) * n ^ 2` is the
exact minimum over all convolution indices `i`. -/
theorem q_gevrey_cauchy_mul_quadratic_envelope_identity
    (s t n i : ℝ)
    (hst : 0 < s + t) :
    s * i ^ 2 + t * (n - i) ^ 2 =
      qGevreyCauchyEnvelopeOrder s t * n ^ 2 +
        (s + t) * (i - qGevreyCauchySaddleIndex s t n) ^ 2 ∧
    qGevreyCauchyEnvelopeOrder s t * n ^ 2 ≤ s * i ^ 2 + t * (n - i) ^ 2 := by
  have hst_ne : s + t ≠ 0 := ne_of_gt hst
  have h_ident :
      s * i ^ 2 + t * (n - i) ^ 2 =
        qGevreyCauchyEnvelopeOrder s t * n ^ 2 +
          (s + t) * (i - qGevreyCauchySaddleIndex s t n) ^ 2 := by
    unfold qGevreyCauchyEnvelopeOrder qGevreyCauchySaddleIndex
    field_simp [hst_ne]
    ring
  have h_nonneg :
      0 ≤ (s + t) * (i - qGevreyCauchySaddleIndex s t n) ^ 2 :=
    mul_nonneg (le_of_lt hst) (sq_nonneg _)
  have h_bound :
      qGevreyCauchyEnvelopeOrder s t * n ^ 2 ≤ s * i ^ 2 + t * (n - i) ^ 2 := by
    linarith [h_ident, h_nonneg]
  exact ⟨h_ident, h_bound⟩

end QOU.QBeta.FaddeevHalvesSelectionAndQGevreyCauchyEnvelope
