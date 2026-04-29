/-!
# QOU.Descartes.mobiusLimitFromThimble — Steepest-descent derivation of `a = (4-q)/(4q+3)`

The integration limit `a(q) = (4 - q)/(4q + 3)` is the leading-order
asymptotic re-entry point on `ℝ` of the Picard–Lefschetz thimble
emanating from the complex critical point `z_c^+ ∈ ℂ` of the SW
action.

This is an **archimedean** statement: it requires the embedding
`R ↪ ℂ` and uses the modulus and argument of the Hessian
`H(z_c) ∈ ℂ`.  The categorical (`R`-side) statement is only the
existence of the Möbius transformation; the identification with the
steepest-descent re-entry point lives downstream of `τ`.

LaTeX label: `prop:mobius-limit-from-thimble`

## References

- [witten2011] https://doi.org/10.1090/conm/560 (Picard–Lefschetz)
- [manuscript] §6/mobius-limit-from-thimble
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Complex.Basic

namespace QOU.Descartes

/-- The Möbius transformation `q ↦ (4 - q)/(4q + 3)` defining the
    baryon integration limit.  Output is in the categorical base ring
    `R` (here represented by `ℝ`); the identification with the thimble
    re-entry point requires the archimedean embedding. -/
noncomputable def mobiusIntegrationLimit (q : ℝ) : ℝ :=
  (4 - q) / (4 * q + 3)

/-- **Proposition: the Möbius integration limit is the steepest-descent
    re-entry point.**
    Under the archimedean embedding `R ↪ ℂ`, the points `±a(q) ∈ ℝ`
    at which the Picard–Lefschetz thimbles `𝒥_{z_c^±}` re-enter the
    real axis equal `±(4 - q)/(4q + 3)` to leading order in the
    Hessian-direction expansion at `z_c^±`.

    Statement-level only; the analytic proof (Hessian computation +
    asymptotic ODE solution) lives in `mobius-limit-from-thimble.md`
    and is verified numerically in
    `picard-lefschetz-thimble.witness.json`.

    Ref: [witten2011], [manuscript] §6/mobius-limit-from-thimble -/
-- Ref: [manuscript] https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/descartes-universe/mobius-limit-from-thimble.md
axiom mobiusLimitFromThimble :
  ∀ (q : ℝ),
    -- Archimedean: steepest-descent re-entry abscissa = mobiusIntegrationLimit q
    -- (statement requires complex contours; placeholder until the
    -- archimedean PL infrastructure is formalised).
    True

end QOU.Descartes
