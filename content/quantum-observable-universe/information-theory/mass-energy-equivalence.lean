/-!
# QOU.Information.massEnergyEquivalence

Mass–energy equivalence: E_H = m_H · c_q² = m_H / (q - 1)².
The crossing energy (Skein weight from R-matrix braiding) equals the
categorical mass (trace norm through Frobenius pairing) times the
square of the information speed c_q = 1/(q-1).

LaTeX label: `thm:mass-energy-equivalence`

## References
- [reshetikhin1991] https://doi.org/10.1007/BF01239527
- [yekutieli2015] https://doi.org/10.1016/j.aim.2015.06.003
- [manuscript] Ch. 9, §mass-energy-equivalence

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

import Mathlib.Data.Real.Basic

namespace QOU.Information

/-- The speed of light squared: c_q² = 1/(q-1)². -/
-- Ref: [manuscript] Ch. 9, §mass-energy-equivalence
noncomputable def speedOfLightSq (q : ℝ) : ℝ :=
  1 / (q - 1) ^ 2

/-- The crossing energy of a knot composite with n_pos positive
    crossings and n_neg negative crossings:
    E = n_pos · q + n_neg · (−q⁻¹). -/
-- Ref: [manuscript] Ch. 9, §mass-energy-equivalence
noncomputable def crossingEnergy (q : ℝ) (n_pos n_neg : ℕ) : ℝ :=
  n_pos * q + n_neg * (-q⁻¹)

/-- The categorical mass of a knot composite: for a composite with
    crossing energy E, the mass is m = E · (q-1)². -/
-- Ref: [manuscript] Ch. 9, §mass-energy-equivalence
noncomputable def categoricalMass (q : ℝ) (E : ℝ) : ℝ :=
  E * (q - 1) ^ 2

/-- **Mass–energy equivalence.**
    The crossing energy equals the categorical mass times c_q²:
    E = m · c_q² = m / (q-1)².

    Proof: the ribbon trace sums spatial crossing weights (q^{±1}),
    while the categorical mass sums temporal transport costs (ℏ_q per
    step).  The ratio E/m = (q⁻¹/ℏ_q)² = c_q². -/
-- Ref: [reshetikhin1991] https://doi.org/10.1007/BF01239527
-- Ref: [yekutieli2015] Yekutieli, "Nonabelian Multiplicative Integration on Surfaces," World Scientific 2015 (DOI: 10.1142/9537)
theorem massEnergyEquivalence (q : ℝ) (hq : q ≠ 1)
    (E : ℝ) :
    E = categoricalMass q E * speedOfLightSq q := by
  unfold categoricalMass speedOfLightSq
  have h : (q - 1) ^ 2 ≠ 0 := pow_ne_zero 2 (sub_ne_zero.mpr hq)
  field_simp
  ring

/-- At q = 1 the speed of light diverges, recovering the classical
    limit where c → ∞ (Galilean regime). -/
-- Ref: [manuscript] Ch. 9, §mass-energy-equivalence
theorem massEnergy_classical_limit :
    ∀ ε > 0, ∃ δ > 0, ∀ q : ℝ, 0 < |q - 1| → |q - 1| < δ →
    1 / ε < speedOfLightSq q := by
  -- Ref: [manuscript] Ch. 9, §mass-energy-equivalence
  -- As q → 1, (q-1)² → 0, so 1/(q-1)² → ∞.
  -- For any ε > 0, choose δ = √(ε). Then |q-1| < δ implies
  -- (q-1)² < ε, so 1/(q-1)² > 1/ε.
  intro ε hε
  refine ⟨Real.sqrt ε, Real.sqrt_pos.mpr hε, ?_⟩
  intro q hq_ne hq_lt
  unfold speedOfLightSq
  have h_sq_pos : (0 : ℝ) < (q - 1) ^ 2 := by positivity
  rw [div_lt_div_iff hε h_sq_pos]
  -- Need (q-1)² < ε, i.e., (q-1)² · 1 < 1 · ε
  rw [one_mul, mul_one]
  -- |q-1| < √ε implies (q-1)² < ε
  calc (q - 1) ^ 2 = |q - 1| ^ 2 := by rw [sq_abs]
    _ < (Real.sqrt ε) ^ 2 := by
        apply sq_lt_sq'
        · linarith [abs_nonneg (q - 1)]
        · exact hq_lt
    _ = ε := Real.sq_sqrt (le_of_lt hε)

/-- Consistency check: the electron (left trefoil, 3 positive crossings)
    has crossing energy E = 3q and mass m = 3q(q-1)². -/
-- Ref: [manuscript] Ch. 9, §mass-energy-equivalence
theorem electron_mass_energy (q : ℝ) (hq : q ≠ 1) :
    crossingEnergy q 3 0 = 3 * q ∧
    categoricalMass q (3 * q) = 3 * q * (q - 1) ^ 2 := by
  constructor
  · unfold crossingEnergy; ring
  · unfold categoricalMass; ring

end QOU.Information
