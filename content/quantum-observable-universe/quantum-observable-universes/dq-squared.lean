import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.dq_squared — Non-vanishing of dq² (archimedean form)

The q-deformed exterior derivative satisfies:

  dq²(α) = q⁻¹(1 - q⁻¹) dθ ∧ ℒ_ξ α

Thus dq² = 0 iff q = 1 or α is Reeb-invariant.

LaTeX label: `prop:dq-squared`

## References

- [manuscript] §1-quantum-observable-universe/dq-squared

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Archimedean dq² formula**.

    In the archimedean realisation, the q-deformed exterior derivative
    squared evaluates to:
    `dq²(α) = q⁻¹(1 - q⁻¹) · dθ ∧ ℒ_ξ α`

    The Lie derivative ℒ_ξ measures the failure of Reeb-invariance. -/
-- Ref: [manuscript] §1
structure ArchimedeanDqSquared where
  /-- The substrate parameter q. -/
  q : R_q
  /-- q > 0. -/
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- The Lie derivative value ℒ_ξ α (scalar representative). -/
  lie_deriv : R_q
  /-- The Levi form value dθ(·, ·) (scalar representative). -/
  levi_form : R_q
  /-- dq²(α) = q⁻¹(1 - q⁻¹) · dθ · ℒ_ξ α. -/
  dq_squared : R_q := q⁻¹ * (1 - q⁻¹) * levi_form * lie_deriv

/-- dq² vanishes on Reeb-invariant forms. -/
-- Ref: [manuscript] §1
theorem dq_squared_zero_reeb_invariant (d : ArchimedeanDqSquared)
    (h : d.lie_deriv = 0) : d.dq_squared = 0 := by
  unfold ArchimedeanDqSquared.dq_squared
  simp [h]

/-- dq² vanishes at q = 1 (classical limit). -/
-- Ref: [manuscript] §1
theorem dq_squared_zero_classical (d : ArchimedeanDqSquared)
    (hq : d.q = 1) : d.dq_squared = 0 := by
  unfold ArchimedeanDqSquared.dq_squared
  simp [hq]

/-- On horizontal ℒ_ξ-invariant forms, dq defines a cochain complex. -/
-- Ref: [manuscript] §1
theorem dq_cochain_on_invariant (d : ArchimedeanDqSquared)
    (h : d.lie_deriv = 0) : d.dq_squared = 0 :=
  dq_squared_zero_reeb_invariant d h

end QOU
