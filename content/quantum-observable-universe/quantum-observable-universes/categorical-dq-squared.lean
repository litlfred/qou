/-!
# QOU.categorical_dq_squared — Non-vanishing of dq²

The categorical q-deformed exterior derivative satisfies:

  dq²(α) = q⁻¹(1 - q⁻¹) ω_V ∧_q [ξ, α]

So dq² = 0 iff q = 1 or [ξ, α] = 0. On ξ-invariant forms,
dq reduces to q⁻¹ d with dq² = 0.

LaTeX label: `prop:categorical-dq-squared`

## References

- [manuscript] §1-quantum-observable-universe/categorical-dq-squared

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **dq² obstruction data**: the non-vanishing of dq² for generic q ≠ 1.

    The obstruction is `q⁻¹(1 - q⁻¹) · ω_V ∧_q [ξ, α]`, which vanishes
    iff `q = 1` or `α` is Reeb-invariant (`[ξ, α] = 0`). -/
-- Ref: [manuscript] §1
structure DqSquaredObstruction where
  /-- The substrate parameter q. -/
  q : R_q
  /-- q > 0 (invertibility). -/
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- The Reeb-bracket value [ξ, α] (scalar representative). -/
  reeb_bracket : R_q
  /-- The obstruction: dq²(α) = q⁻¹(1 - q⁻¹) · [ξ, α]. -/
  obstruction : R_q := q⁻¹ * (1 - q⁻¹) * reeb_bracket

/-- dq² vanishes iff q = 1 or the form is Reeb-invariant. -/
-- Ref: [manuscript] §1
theorem dq_squared_vanishes_iff (obs : DqSquaredObstruction) :
    obs.obstruction = 0 ↔ (obs.q = 1 ∨ obs.reeb_bracket = 0) := by
  unfold DqSquaredObstruction.obstruction
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h3
    · rcases mul_eq_zero.mp h1 with h2 | h4
      · left
        rwa [inv_eq_zero] at h2
        exact absurd h2 (ne_of_gt obs.q_pos)
      · left
        have : q⁻¹ = 1 := by linarith [sub_eq_zero.mp h4]
        rwa [inv_eq_one] at this
    · right; exact h3
  · intro h
    rcases h with rfl | rfl
    · simp
    · simp

/-- On Reeb-invariant forms, dq is a cochain differential (dq² = 0). -/
-- Ref: [manuscript] §1
theorem dq_squared_zero_on_invariant (obs : DqSquaredObstruction)
    (h_inv : obs.reeb_bracket = 0) : obs.obstruction = 0 := by
  unfold DqSquaredObstruction.obstruction
  simp [h_inv]

/-- For q ≠ 1, dq² ≠ 0 on generic (non-Reeb-invariant) forms. -/
-- Ref: [manuscript] §1
theorem dq_squared_nonzero_generic (obs : DqSquaredObstruction)
    (hq : obs.q ≠ 1) (h_gen : obs.reeb_bracket ≠ 0) :
    obs.obstruction ≠ 0 := by
  unfold DqSquaredObstruction.obstruction
  apply mul_ne_zero
  apply mul_ne_zero
  · exact inv_ne_zero.mpr (ne_of_gt obs.q_pos)
  · intro h
    apply hq
    have : obs.q⁻¹ = 1 := by linarith [sub_eq_zero.mp h]
    rwa [inv_eq_one] at this
  · exact h_gen

end QOU
