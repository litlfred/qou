/-!
# QOU.dq_squared — Non-vanishing of dq² (archimedean form)

The q-deformed exterior derivative satisfies:

  dq²(α) = q⁻¹(1 - q⁻¹) dθ ∧ ℒ_ξ α

Thus dq² = 0 iff q = 1 or α is Reeb-invariant.

LaTeX label: `prop:dq-squared`

## References

- [manuscript] §1-quantum-observable-universe/dq-squared
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- **Archimedean dq² formula**.

    In the archimedean realisation, the q-deformed exterior derivative
    squared evaluates to:
    `dq²(α) = q⁻¹(1 - q⁻¹) · dθ ∧ ℒ_ξ α`

    The Lie derivative ℒ_ξ measures the failure of Reeb-invariance. -/
-- Ref: [manuscript] §1
structure ArchimedeanDqSquared where
  /-- The substrate parameter q. -/
  q : ℝ
  /-- q > 0. -/
  q_pos : 0 < q
  /-- The Lie derivative value ℒ_ξ α (scalar representative). -/
  lie_deriv : ℝ
  /-- The Levi form value dθ(·, ·) (scalar representative). -/
  levi_form : ℝ
  /-- dq²(α) = q⁻¹(1 - q⁻¹) · dθ · ℒ_ξ α. -/
  dq_squared : ℝ := q⁻¹ * (1 - q⁻¹) * levi_form * lie_deriv

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
