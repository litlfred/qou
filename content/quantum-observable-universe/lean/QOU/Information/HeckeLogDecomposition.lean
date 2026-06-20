/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# Decomposition of log(1/h) into thermal + skein normalisation

Proves the algebraic identity

  log(1/h) = log(1/ℏ_q) - log(1 + q)

where h = q - q^{-1} is the Hecke skein deformation and
ℏ_q = (q - 1)/q is the QOU quantum Planck constant
(prop:boltzmann-constant : k_B · T_q = ℏ_q).

Proof: h = (q² - 1)/q = (q - 1)(q + 1)/q = ℏ_q · (q + 1).
Taking 1/h and log gives the decomposition.

Ref: [manuscript] prop:boltzmann-constant
Ref: probe_delta_coupling_q_edgeworth.py (numerical verification to 50 dps)
-/
import QOU.HeckeAlgebra.QSubstrate
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.Information

/-- The Hecke deformation h := q - q⁻¹ factors as ℏ_q · (q + 1) where
    ℏ_q = (q - 1)/q is the QOU quantum Planck constant. -/
theorem hecke_skein_factorization (q : ℝ) (hq : 0 < q) :
    q - q⁻¹ = ((q - 1) / q) * (q + 1) := by
  -- q - q⁻¹ = (q² - 1)/q = (q-1)(q+1)/q = ((q-1)/q)·(q+1)
  field_simp
  ring

/-- log(1/h) = log(1/ℏ_q) - log(1 + q) at every q > 1
    (so h > 0 and the log is well-defined). -/
theorem hecke_log_decomposition (q : ℝ) (hq : 1 < q) :
    Real.log (1 / (q - q⁻¹)) =
      Real.log (1 / ((q - 1) / q)) - Real.log (1 + q) := by
  -- Ref: [manuscript] prop:boltzmann-constant
  -- Strategy: use hecke_skein_factorization to rewrite the LHS, then
  -- 1/(a·b) = (1/a)·(1/b), then Real.log_mul + Real.log_one_div.
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have hq_minus_1_pos : 0 < q - 1 := by linarith
  have hq_plus_1_pos : 0 < q + 1 := by linarith
  have hhbar_pos : 0 < (q - 1) / q := div_pos hq_minus_1_pos hq_pos
  have hhbar_ne : ((q - 1) / q : ℝ) ≠ 0 := ne_of_gt hhbar_pos
  have hqp1_ne : (q + 1 : ℝ) ≠ 0 := ne_of_gt hq_plus_1_pos
  have h1p_q_eq : (1 + q : ℝ) = q + 1 := by ring
  -- Rewrite via the factorisation
  have heq : (1 / (q - q⁻¹) : ℝ) = (1 / ((q - 1) / q)) * (1 / (q + 1)) := by
    rw [hecke_skein_factorization q hq_pos]
    field_simp
  rw [heq, Real.log_mul (one_div_ne_zero hhbar_ne) (one_div_ne_zero hqp1_ne)]
  rw [Real.log_one_div, h1p_q_eq]
  ring

/-- Numerical equality at the QOU substrate parameter q_0:
    log(1/h(q_0)) = log(1/ℏ_q(q_0)) - log(1 + q_0) ≈ 1.56513...
    Verified to 50 dps in probe_delta_coupling_q_edgeworth.py. -/
noncomputable def hecke_log_decomposition_at_q0 :
    Real.log (1 / (HeckeAlgebra.q_0 - HeckeAlgebra.q_0⁻¹)) =
      Real.log (1 / ((HeckeAlgebra.q_0 - 1) / HeckeAlgebra.q_0)) - Real.log (1 + HeckeAlgebra.q_0) :=
  hecke_log_decomposition HeckeAlgebra.q_0 HeckeAlgebra.q_0_gt_one

end QOU.Information
