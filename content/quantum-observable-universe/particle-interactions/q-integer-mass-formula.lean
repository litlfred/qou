/-
  Atomic mass formula with q-integer Bethe-Weizsäcker coefficients.

  All BW coefficients are products of quantum integers [n]_q × m_e:
    λ_V = 2[2]_q[7]_q · m_e
    λ_S = 2[4]_q² · m_e
    λ_C = (q-q⁻¹)[6]_q · m_e
    a_asym = 3[2]_q[7]_q · m_e
    δ_P = [3]_q[7]_q · m_e

  Ref: [manuscript] Ch 11 §8, prop:q-integer-mass-formula
-/

import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.Interactions

/-- Quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}). -/
noncomputable def q_int (q : ℝ) (n : ℤ) : ℝ :=
  (q ^ n - q ^ (-n)) / (q - q⁻¹)

/-- Volume coefficient λ_V = 2[2]_q[7]_q · m_e. -/
-- Ref: [manuscript] Ch 11 §8
noncomputable def lambda_V (q m_e : ℝ) : ℝ :=
  2 * q_int q 2 * q_int q 7 * m_e

/-- Surface coefficient λ_S = 2[4]_q² · m_e. -/
noncomputable def lambda_S (q m_e : ℝ) : ℝ :=
  2 * (q_int q 4) ^ 2 * m_e

/-- Coulomb coefficient λ_C = (q - q⁻¹)[6]_q · m_e. -/
noncomputable def lambda_C (q m_e : ℝ) : ℝ :=
  (q - q⁻¹) * q_int q 6 * m_e

/-- Asymmetry coefficient a_asym = 3[2]_q[7]_q · m_e. -/
noncomputable def a_asym (q m_e : ℝ) : ℝ :=
  3 * q_int q 2 * q_int q 7 * m_e

/-- Pairing coefficient δ_P = [3]_q[7]_q · m_e. -/
noncomputable def delta_P (q m_e : ℝ) : ℝ :=
  q_int q 3 * q_int q 7 * m_e

/-- The relation a_asym = (3/2) × λ_V holds exactly. -/
-- Ref: [manuscript] Ch 11 §8
theorem asym_volume_relation (q m_e : ℝ) :
    a_asym q m_e = (3 / 2) * lambda_V q m_e := by
  unfold a_asym lambda_V
  ring

/-- Bethe-Weizsäcker binding energy with q-integer coefficients. -/
-- Ref: [manuscript] Ch 11 §8
noncomputable def binding_energy_bw (q m_e : ℝ) (Z N : ℕ) : ℝ :=
  let A := (Z + N : ℝ)
  lambda_V q m_e * A
  - lambda_S q m_e * A ^ (2/3 : ℝ)
  - lambda_C q m_e * Z * (Z - 1) / A ^ (1/3 : ℝ)
  - a_asym q m_e * (N - Z) ^ 2 / (4 * A)

end QOU.Interactions
