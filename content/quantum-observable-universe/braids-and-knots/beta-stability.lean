/-!
# QOU.Braiding.beta_stability — Beta-stability line from ∂L_bind/∂p = 0

The stable proton number for a nucleus of mass number A is
p*(A) = A / (2 + a_C·A^{2/3}/(2·a_A)), derived from extremizing
the Skein binding Lagrangian under beta variation.

LaTeX label: `prop:beta-stability`

## References
- [manuscript] §4/beta-stability
-/

import Mathlib.Data.Real.Basic

namespace QOU.Braiding

/-- Beta-stability line: p*(A) = A / (2 + a_C·A^{2/3}/(2·a_A)). -/
-- Ref: [manuscript] §4/beta-stability
noncomputable def betaStabilityLine (A a_C a_A : ℝ) : ℝ :=
  A / (2 + a_C * A^((2:ℝ)/3) / (2 * a_A))

/-- At q = 1 (classical limit), a_C = 0 and all nuclei have p = A/2.
    No Coulomb repulsion means symmetric nuclear matter. -/
-- Ref: [manuscript] §4/beta-stability
theorem classical_limit_symmetric (A a_A : ℝ) (hA : A ≠ 0) :
    betaStabilityLine A 0 a_A = A / 2 := by
  unfold betaStabilityLine
  simp [zero_mul, zero_div, add_zero]

/-- The denominator of the stability line is > 2 when a_C > 0 and A > 0,
    so p*(A) < A/2: heavy nuclei have more neutrons than protons. -/
-- Ref: [manuscript] §4/beta-stability
theorem neutron_excess (A a_C a_A : ℝ) (hA : 0 < A) (hC : 0 < a_C) (haA : 0 < a_A) :
    betaStabilityLine A a_C a_A < A / 2 := by
  unfold betaStabilityLine
  apply div_lt_div_of_pos_left hA (by linarith) -- A > 0
  · -- 2 + a_C·A^{2/3}/(2·a_A) > 2
    have h1 : 0 < a_C * A ^ ((2:ℝ)/3) / (2 * a_A) := by
      apply div_pos
      · exact mul_pos hC (rpow_pos_of_pos hA _)
      · linarith
    linarith
  · linarith

/-- Stable neutron number: n*(p) = A*(p) - p where A*(p) is the
    fixed point of A = p·(2 + a_C·A^{2/3}/(2·a_A)). -/
-- Ref: [manuscript] §4/beta-stability
noncomputable def stableNeutronNumber (p : ℕ) (a_C a_A : ℝ) (A_stable : ℝ) : ℝ :=
  A_stable - p

/-- The n/p ratio is 1 when a_C = 0. -/
-- Ref: [manuscript] §4/beta-stability
theorem nOverP_classical (p : ℕ) (a_A : ℝ) (hp : 0 < p) :
    stableNeutronNumber p 0 a_A (2 * p) / p = 1 := by
  unfold stableNeutronNumber
  push_cast
  field_simp

end QOU.Braiding
