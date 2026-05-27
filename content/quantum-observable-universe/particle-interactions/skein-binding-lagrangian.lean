import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Braiding.SkeinBindingLagrangian — Nuclear binding from canonical action

The Skein binding Lagrangian is S_q evaluated on the multi-nucleon
Hopf link: L_bind = L_vol - L_surf - L_Coul - L_Pauli + L_pair.

LaTeX label: `def:skein-binding-lagrangian`

## References
- [manuscript] §4/skein-binding-lagrangian

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Braiding

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The five-term Skein binding Lagrangian for a nucleus (p, n). -/
-- Ref: [manuscript] §4/skein-binding-lagrangian
structure SkeinBindingLagrangian where
  /-- Number of protons. -/
  p : ℕ
  /-- Number of neutrons. -/
  n : ℕ
  /-- Substrate parameter q. -/
  q : R_q
  /-- q > 1. -/
  -- q_gt_one : 1 < q  -- (archimedean; not meaningful over R_q)
  /-- Volume scale λ_V. -/
  lambda_V : R_q
  /-- Surface scale λ_S. -/
  lambda_S : R_q
  /-- Coulomb scale λ_C. -/
  lambda_C : R_q
  /-- Pauli asymmetry coefficient a_A. -/
  a_A : R_q
  /-- Mass number. -/
  A : ℕ := p + n

/-- Volume binding: (q + q⁻¹)/2 · λ_V · A. -/
noncomputable def SkeinBindingLagrangian.L_vol (L : SkeinBindingLagrangian) : R_q :=
  (L.q + 1/L.q) / 2 * L.lambda_V * L.A

/-- Coulomb repulsion: (q - q⁻¹) · λ_C · p(p-1)/A^{1/3}. -/
noncomputable def SkeinBindingLagrangian.L_Coul (L : SkeinBindingLagrangian) : R_q :=
  (L.q - 1/L.q) * L.lambda_C * (L.p * (L.p - 1)) / (L.A : R_q)^(1/3 : R_q)

/-- Pauli asymmetry: a_A · (n - p)²/(4A). -/
noncomputable def SkeinBindingLagrangian.L_Pauli (L : SkeinBindingLagrangian) : R_q :=
  L.a_A * ((L.n : R_q) - L.p)^2 / (4 * L.A)

end QOU.Braiding
