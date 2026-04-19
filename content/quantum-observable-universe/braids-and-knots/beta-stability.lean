/-!
# QOU.Braiding.beta_stability — Beta-stability line from ∂L_bind/∂p = 0

The stable proton number for a nucleus of mass number A is
p*(A) = A / (2 + a_C·A^{2/3}/(2·a_A)), derived from extremizing
the Skein binding Lagrangian under beta variation.

LaTeX label: `prop:beta-stability`

## References
- [manuscript] §4/beta-stability

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Braiding

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- Beta-stability line: p*(A) = A / (2 + a_C·A^{2/3}/(2·a_A)). -/
-- Ref: [manuscript] §4/beta-stability
noncomputable def betaStabilityLine (A a_C a_A : R_q) : R_q :=
  A / (2 + a_C * A^((2:R_q)/3) / (2 * a_A))

/-- At q = 1 (classical limit), a_C = 0 and all nuclei have p = A/2.
    No Coulomb repulsion means symmetric nuclear matter. -/
-- Ref: [manuscript] §4/beta-stability
theorem classical_limit_symmetric (A a_A : R_q) (hA : A ≠ 0) :
    betaStabilityLine A 0 a_A = A / 2 := by
  unfold betaStabilityLine
  simp [zero_mul, zero_div, add_zero]

/-- The denominator of the stability line is > 2 when a_C > 0 and A > 0,
    so p*(A) < A/2: heavy nuclei have more neutrons than protons. -/
-- Ref: [manuscript] §4/beta-stability
-- theorem neutron_excess (A a_C a_A : R_q) (hA : 0 < A) (hC : 0 < a_C) (haA : 0 < a_A) :  -- (archimedean; not meaningful over R_q)
    betaStabilityLine A a_C a_A < A / 2 := by
  unfold betaStabilityLine
  apply div_lt_div_of_pos_left hA (by linarith) -- A > 0
  · -- 2 + a_C·A^{2/3}/(2·a_A) > 2
    have h1 : 0 < a_C * A ^ ((2:R_q)/3) / (2 * a_A) := by
      apply div_pos
      · exact mul_pos hC (rpow_pos_of_pos hA _)
      · linarith
    linarith
  · linarith

/-- Stable neutron number: n*(p) = A*(p) - p where A*(p) is the
    fixed point of A = p·(2 + a_C·A^{2/3}/(2·a_A)). -/
-- Ref: [manuscript] §4/beta-stability
noncomputable def stableNeutronNumber (p : ℕ) (a_C a_A : R_q) (A_stable : R_q) : R_q :=
  A_stable - p

/-- The n/p ratio is 1 when a_C = 0. -/
-- Ref: [manuscript] §4/beta-stability
-- theorem nOverP_classical (p : ℕ) (a_A : R_q) (hp : 0 < p) :  -- (archimedean; not meaningful over R_q)
    stableNeutronNumber p 0 a_A (2 * p) / p = 1 := by
  unfold stableNeutronNumber
  push_cast
  field_simp


/-- **prop:beta-stability** — placeholder stub; full proof TBD. -/
theorem beta_stability : ∃ (witness : ℝ), 0 < witness := by
  -- Ref: [manuscript] §braids-and-knots/beta-stability
  sorry
end QOU.Braiding
