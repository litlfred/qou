/-!
# QOU.Descartes.QEnergy — q-Energy from angular momentum + momentum + action

The q-energy of a particle knot is the sum of three terms:
  E_q = J_q² · ℏ_q + p_q² · ℏ_q/(2[n]_q) + S_q
where S_q is the categorical action (rest mass energy).

LaTeX label: `def:q-energy`

## References
- [manuscript] §6/q-energy
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- ℏ_q = 1 - q⁻¹, the quantum Planck constant. -/
-- Ref: [manuscript] §6/q-energy
noncomputable def hbar_q (q : ℝ) : ℝ := 1 - 1 / q

/-- [n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹), the q-number. -/
-- Ref: [manuscript] §6/q-energy
noncomputable def q_number (q n : ℝ) : ℝ :=
  (q ^ n - q ^ (-n)) / (q - q ^ (-(1 : ℝ)))

/-- The q-energy of a particle knot.
    Three terms: rotational + translational + rest mass (action). -/
-- Ref: [manuscript] §6/q-energy
structure QEnergy where
  /-- Substrate parameter. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Spin quantum number j. -/
  j : ℝ
  j_nonneg : 0 ≤ j
  /-- q-momentum (writhe-derived). -/
  p_q : ℝ
  /-- Number of strands in braid representative. -/
  n_strands : ℝ
  n_pos : 0 < n_strands
  /-- Categorical action S_q (rest mass energy). -/
  S_q : ℝ
  S_q_nonneg : 0 ≤ S_q

/-- The total q-energy. -/
-- Ref: [manuscript] §6/q-energy
noncomputable def QEnergy.total (E : QEnergy) : ℝ :=
  -- Rotational: [j]_q · [j+1]_q · ℏ_q
  q_number E.q E.j * q_number E.q (E.j + 1) * hbar_q E.q
  -- Translational: p_q² · ℏ_q / (2 · [n]_q)
  + E.p_q ^ 2 * hbar_q E.q / (2 * q_number E.q E.n_strands)
  -- Action (rest mass): S_q
  + E.S_q

/-- At rest (p_q = 0, j = 0), q-energy equals the action (rest mass). -/
-- Ref: [manuscript] §6/q-energy
theorem q_energy_rest (q S : ℝ) (hq : 1 < q) (hS : 0 ≤ S) :
    (QEnergy.mk q hq 0 (le_refl 0) 0 1 one_pos S hS).total = S := by
  unfold QEnergy.total q_number hbar_q
  simp
  ring

/-- The crossing energy at a single positive crossing. -/
-- Ref: [manuscript] §6/q-energy
noncomputable def crossingEnergy_pos (q : ℝ) : ℝ := q

/-- The crossing energy at a single negative crossing. -/
-- Ref: [manuscript] §6/q-energy
noncomputable def crossingEnergy_neg (q : ℝ) : ℝ := 1 / q

/-- Positive crossings carry more energy than negative at q > 1. -/
-- Ref: [manuscript] §6/q-energy
theorem crossing_energy_asymmetry {q : ℝ} (hq : 1 < q) :
    crossingEnergy_neg q < crossingEnergy_pos q := by
  unfold crossingEnergy_pos crossingEnergy_neg
  rw [div_lt_iff (by linarith : (0 : ℝ) < q)]
  nlinarith

end QOU.Descartes
