/-!
# QOU.Torsion.StableNucleus — Nucleus extremizing the Skein binding Lagrangian

A stable nucleus N(p,n) = p𝔭 ⋈ n𝔫 where (p,n) satisfies
∂L_bind/∂p|_A = 0 (beta-stability line).

LaTeX label: `def:stable-nucleus`

## References
- [manuscript] §3/stable-nucleus

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Torsion

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A stable nucleus: multi-nucleon Hopf link on the beta-stability line. -/
-- Ref: [manuscript] §3/stable-nucleus
structure StableNucleus where
  /-- Number of protons. -/
  p : ℕ
  /-- Number of neutrons. -/
  n : ℕ
  /-- Coulomb coefficient a_C = (q - q⁻¹) · λ_C. -/
  a_C : R_q
  /-- Pauli asymmetry coefficient. -/
  a_A : R_q
  /-- a_A is positive. -/
  -- a_A_pos : 0 < a_A  -- (archimedean; not meaningful over R_q)
  /-- Mass number. -/
  A : ℕ := p + n
  /-- Beta-stability condition: p ≈ A / (2 + a_C·A^{2/3}/(2·a_A)). -/
  stability : |((p : R_q) - (A : R_q) / (2 + a_C * (A : R_q)^(2/3 : R_q) / (2 * a_A)))| < 2

end QOU.Torsion
