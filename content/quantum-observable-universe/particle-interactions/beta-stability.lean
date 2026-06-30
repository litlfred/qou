import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.Braiding.beta_stability — Beta-stability line from ∂L_bind/∂p = 0

The stable proton number for a nucleus of mass number A is
p*(A) = A / (2 + a_C·A^{2/3}/(2·a_A)), derived from extremizing
the Skein binding Lagrangian under beta variation.

LaTeX label: `prop:beta-stability`

## References
- [manuscript] §4/beta-stability

**Base ring**: the stability line uses division, the real exponent
`A^{2/3}`, and order comparisons (`0 < A`, `p*(A) < A/2`).  These are
archimedean constructs, so the construction lives on the **observable
side of the substrate→archimedean wall** and is stated over `ℝ`
(§7c base-ring convention — fractional powers and ordering force `ℝ`).
The coefficients `a_C, a_A` are the real evaluations of the Coulomb /
asymmetry scales at the substrate point `q ↦ q₀`.
-/

namespace QOU.Braiding

open scoped Real

/-- Beta-stability line: p*(A) = A / (2 + a_C·A^{2/3}/(2·a_A)). -/
-- Ref: [manuscript] §4/beta-stability
noncomputable def betaStabilityLine (A a_C a_A : ℝ) : ℝ :=
  A / (2 + a_C * A ^ (2 / 3 : ℝ) / (2 * a_A))

/-- At a_C = 0 (no Coulomb repulsion, the q = 1 classical limit) the
    stability line is p*(A) = A/2: symmetric nuclear matter. -/
-- Ref: [manuscript] §4/beta-stability
theorem classical_limit_symmetric (A a_A : ℝ) :
    betaStabilityLine A 0 a_A = A / 2 := by
  unfold betaStabilityLine
  simp

/-- The denominator of the stability line exceeds 2 when a_C > 0 and
    A > 0, so p*(A) < A/2: heavy nuclei have more neutrons than protons. -/
-- Ref: [manuscript] §4/beta-stability
theorem neutron_excess (A a_C a_A : ℝ) (hA : 0 < A) (hC : 0 < a_C) (haA : 0 < a_A) :
    betaStabilityLine A a_C a_A < A / 2 := by
  unfold betaStabilityLine
  have hpow : 0 < A ^ (2 / 3 : ℝ) := Real.rpow_pos_of_pos hA _
  -- the Coulomb excess in the denominator is strictly positive
  have hexcess : 0 < a_C * A ^ (2 / 3 : ℝ) / (2 * a_A) := by positivity
  have hden : (2 : ℝ) < 2 + a_C * A ^ (2 / 3 : ℝ) / (2 * a_A) := by linarith
  -- A / (larger positive denominator) < A / 2
  have h2 : (0 : ℝ) < 2 := by norm_num
  exact div_lt_div_of_pos_left hA h2 hden

/-- Stable neutron number: n*(A) = A - p*(A), the neutron count at the
    beta-stability proton number for mass number A. -/
-- Ref: [manuscript] §4/beta-stability
noncomputable def stableNeutronNumber (A a_C a_A : ℝ) : ℝ :=
  A - betaStabilityLine A a_C a_A

/-- The n/p ratio is 1 in the classical limit a_C = 0: the stable
    neutron count equals the stable proton count, A/2. -/
-- Ref: [manuscript] §4/beta-stability
theorem nOverP_classical (A a_A : ℝ) :
    stableNeutronNumber A 0 a_A = betaStabilityLine A 0 a_A := by
  unfold stableNeutronNumber
  rw [classical_limit_symmetric]
  ring

end QOU.Braiding
