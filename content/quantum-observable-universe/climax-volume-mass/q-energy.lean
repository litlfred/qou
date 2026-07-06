import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Real.Basic


/-!
# QOU.Archimedean.QEnergy — q-Energy from angular momentum + momentum + action

The q-energy of a particle knot is the sum of three terms:
  E_q = J_q² · ℏ_q + p_q² · ℏ_q/(2[n]_q) + S_q
where S_q is the categorical action (rest mass energy).

LaTeX label: `def:q-energy`

## References
- [manuscript] §6/q-energy

**Ground ring**: archimedean specialisation over `ℝ` (AGENTS.md §7c).
The q-number formula uses real exponents `q^n` (`Real.rpow`), division
and ordering, all of which require the archimedean structure of `ℝ`.
The underlying combinatorial content stays generic to any commutative
ring carrying the same q-data.
-/

namespace QOU.Archimedean

/-- Ground ring: the archimedean specialisation `R_q = ℝ`. -/
abbrev R_q := ℝ

/-- The substrate indeterminate, specialised to the numerical anchor. -/
noncomputable def q_param : R_q := 1.1097

/-- ℏ_q = 1 - q⁻¹, the quantum Planck constant. -/
-- Ref: [manuscript] §6/q-energy
noncomputable def hbar_q (q : R_q) : R_q := 1 - 1 / q

/-- [n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹), the q-number (real exponents). -/
-- Ref: [manuscript] §6/q-energy
noncomputable def q_number (q n : R_q) : R_q :=
  (q ^ n - q ^ (-n)) / (q - q ^ (-(1 : R_q)))

/-- The q-energy of a particle knot.
    Three terms: rotational + translational + rest mass (action). -/
-- Ref: [manuscript] §6/q-energy
structure QEnergy where
  /-- Substrate parameter. -/
  q : R_q
  /-- Spin quantum number j. -/
  j : R_q
  /-- q-momentum (writhe-derived). -/
  p_q : R_q
  /-- Number of strands in braid representative. -/
  n_strands : R_q
  /-- Categorical action S_q (rest mass energy). -/
  S_q : R_q

/-- The total q-energy. -/
-- Ref: [manuscript] §6/q-energy
noncomputable def QEnergy.total (E : QEnergy) : R_q :=
  -- Rotational: [j]_q · [j+1]_q · ℏ_q
  q_number E.q E.j * q_number E.q (E.j + 1) * hbar_q E.q
  -- Translational: p_q² · ℏ_q / (2 · [n]_q)
  + E.p_q ^ 2 * hbar_q E.q / (2 * q_number E.q E.n_strands)
  -- Action (rest mass): S_q
  + E.S_q

/-- At rest (p_q = 0, j = 0), q-energy equals the action (rest mass).
    With `j = 0` the rotational term carries `[0]_q = 0` and with
    `p_q = 0` the translational term vanishes, leaving `S_q`. -/
-- Ref: [manuscript] §6/q-energy
theorem q_energy_rest (q S : R_q) :
    (QEnergy.mk q 0 0 1 S).total = S := by
  unfold QEnergy.total q_number
  simp

/-- The crossing energy at a single positive crossing. -/
-- Ref: [manuscript] §6/q-energy
noncomputable def crossingEnergy_pos (q : R_q) : R_q := q

/-- The crossing energy at a single negative crossing. -/
-- Ref: [manuscript] §6/q-energy
noncomputable def crossingEnergy_neg (q : R_q) : R_q := 1 / q

/-- Positive crossings carry more energy than negative at q > 1. -/
-- Ref: [manuscript] §6/q-energy
theorem crossing_energy_asymmetry {q : R_q} (hq : 1 < q) :
    crossingEnergy_neg q < crossingEnergy_pos q := by
  unfold crossingEnergy_pos crossingEnergy_neg
  rw [div_lt_iff₀ (by linarith : (0 : R_q) < q)]
  nlinarith

/-- Q-Deformed Energy: a rest-mass-nonnegative configuration exists. -/
-- Ref: [manuscript] def:q-energy
theorem q_energy_def :
    ∃ (E : QEnergy), E.S_q ≥ 0 :=
  ⟨QEnergy.mk 1.1097 0 0 1 0, le_refl 0⟩

end QOU.Archimedean
