/-!
# QOU.Archimedean.mobiusLimitFromThimble — Steepest-descent derivation of `a = (4-q)/(4q+3)`

The integration limit `a(q) = (4 - q)/(4q + 3)` is the leading-order
asymptotic re-entry point on `ℝ` of the Picard–Lefschetz thimble
emanating from the complex critical point `z_c^+ ∈ ℂ` of the SW
action.

This is an **archimedean** statement: it requires the embedding
`R ↪ ℂ` and uses the modulus and argument of the Hessian
`H(z_c) ∈ ℂ`.  The categorical (`R`-side) statement is only the
existence of the Möbius transformation; the identification with the
steepest-descent re-entry point lives downstream of `τ`.

LaTeX label: `conj:mobius-limit-from-thimble`

## References

- [witten2011] https://doi.org/10.1090/conm/560 (Picard–Lefschetz)
- [manuscript] §6/mobius-limit-from-thimble

## Witness

- [mobius-limit-from-thimble.witness.json](../../../computations/mobius-limit-from-thimble.witness.json)
  — sympy closed-form `a(q) = (4 - q) / (4 q + 3)` evaluated at `q = q₀`.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
namespace QOU.Archimedean

/-- The Möbius transformation `q ↦ (4 - q)/(4q + 3)` defining the
    baryon integration limit.  Output is in the categorical base ring
    `R` (here represented by `ℝ`); the identification with the thimble
    re-entry point requires the archimedean embedding. -/
noncomputable def mobiusIntegrationLimit (q : ℝ) : ℝ :=
  (4 - q) / (4 * q + 3)

/-- For `q ≥ 0` the denominator `4q + 3 ≥ 3 > 0`, so the Möbius
    transformation is well-defined on the physical range. -/
-- Ref: [manuscript] §6/mobius-limit-from-thimble (denominator non-vanishing)
lemma mobius_denom_pos {q : ℝ} (hq : 0 ≤ q) : 0 < 4 * q + 3 := by
  linarith

/-- The denominator never vanishes on the physical range `q ≥ 0`. -/
-- Ref: [manuscript] §6/mobius-limit-from-thimble
lemma mobius_denom_ne_zero {q : ℝ} (hq : 0 ≤ q) : 4 * q + 3 ≠ 0 :=
  ne_of_gt (mobius_denom_pos hq)

/-- Numerical sanity check: at `q = 1`, the Möbius limit is `3/7`. -/
-- Ref: [manuscript] §6/mobius-limit-from-thimble (Table: limit values)
example : mobiusIntegrationLimit 1 = 3 / 7 := by
  unfold mobiusIntegrationLimit
  norm_num

/-- **Proposition: the Möbius integration limit is the steepest-descent
    re-entry point.**
    Under the archimedean embedding `R ↪ ℂ`, the points `±a(q) ∈ ℝ`
    at which the Picard–Lefschetz thimbles `𝒥_{z_c^±}` re-enter the
    real axis equal `±(4 - q)/(4q + 3)` to leading order in the
    Hessian-direction expansion at `z_c^±`.

    Statement-level only; the analytic proof (Hessian computation +
    asymptotic ODE solution) lives in `mobius-limit-from-thimble.md`
    and is verified numerically in
    `picard-lefschetz-thimble.witness.json`.  The current Lean payload
    asserts only the well-definedness of the Möbius limit on the
    physical range; the analytic identification with the steepest-
    descent re-entry abscissa requires complex-contour infrastructure
    not yet in Mathlib. -/
-- Ref: [witten2011] https://doi.org/10.1090/conm/560 (Picard–Lefschetz)
-- Ref: [manuscript] https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/archimedean-universe/mobius-limit-from-thimble.md
theorem mobiusLimitFromThimble :
    ∀ (q : ℝ), 0 ≤ q → 4 * q + 3 ≠ 0 := by
  intro q hq
  exact mobius_denom_ne_zero hq

end QOU.Archimedean
