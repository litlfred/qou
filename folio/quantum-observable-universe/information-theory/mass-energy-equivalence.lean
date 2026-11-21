import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity


/-!
# QOU.Information.energy

Energy of a braid class: 𝔈 = 𝔪 · c_q² = 𝔪 / (q - 1)², where 𝔪 is the mass
of `def:mass-identity` and c_q = 1/(q-1) is the information speed.

LaTeX label: `def:mass-energy`

This block was `thm:mass-energy-equivalence` until 2026-11-15. That theorem
claimed the crossing energy equals 𝔪 · c_q², and was proved only by defining
mass as `E * (q - 1)^2`. With the mass of `def:mass-identity` the claim is
false (trivial braid: crossing energy 0, mass nonzero), so energy is now a
definition and the crossing energy is a separate quantity. Open question:
bean `qou-078y`.

## References
- [leitner2026] Ch. 9, §mass-energy

**Ground ring**: `ℝ` (archimedean realisation; the speed of light needs
`q ≠ 1` and the classical limit uses the real order).
-/

namespace QOU.Information

/-- The speed of light squared: c_q² = 1/(q-1)². -/
-- Ref: [leitner2026] Ch. 9, §mass-energy-equivalence
noncomputable def speedOfLightSq (q : ℝ) : ℝ :=
  1 / (q - 1) ^ 2

/-- **Energy** of a braid class with mass `m`: 𝔈 = m · c_q². -/
-- Ref: [leitner2026] Ch. 9, §mass-energy
noncomputable def energy (q m : ℝ) : ℝ :=
  m * speedOfLightSq q

/-- At q = 1 the speed of light diverges, recovering the classical
    limit where c → ∞ (Galilean regime). -/
-- Ref: [leitner2026] Ch. 9, §mass-energy-equivalence
theorem massEnergy_classical_limit :
    ∀ ε > 0, ∃ δ > 0, ∀ q : ℝ, 0 < |q - 1| → |q - 1| < δ →
    1 / ε < speedOfLightSq q := by
  -- Ref: [leitner2026] Ch. 9, §mass-energy-equivalence
  -- As q → 1, (q-1)² → 0, so 1/(q-1)² → ∞.
  -- For any ε > 0, choose δ = √(ε). Then |q-1| < δ implies
  -- (q-1)² < ε, so 1/(q-1)² > 1/ε.
  intro ε hε
  refine ⟨Real.sqrt ε, Real.sqrt_pos.mpr hε, ?_⟩
  intro q hq_ne hq_lt
  unfold speedOfLightSq
  have h_sq_pos : (0 : ℝ) < (q - 1) ^ 2 := by
    rw [← sq_abs]
    exact pow_pos hq_ne 2
  -- |q-1| < √ε implies (q-1)² < ε
  have hlt : (q - 1) ^ 2 < ε :=
    calc (q - 1) ^ 2 = |q - 1| ^ 2 := by rw [sq_abs]
      _ < (Real.sqrt ε) ^ 2 := by
          apply sq_lt_sq'
          · linarith [abs_nonneg (q - 1)]
          · exact hq_lt
      _ = ε := Real.sq_sqrt (le_of_lt hε)
  exact one_div_lt_one_div_of_lt h_sq_pos hlt

end QOU.Information
