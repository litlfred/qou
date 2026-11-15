import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.QDilogarithm — categorical q-dilogarithm

The q-dilogarithm is the unique level-2 iterated primitive of H_q
satisfying the pentagon identity.  It is the categorical avatar
of the Drinfeld associator / logarithm of the universal R-matrix.

LaTeX label: `def:q-dilogarithm`

## References

- [leitner2026] §2-quantum-observable-universes/q-dilogarithm

**Ground ring**: `R_q = ℤ[q, q⁻¹]`.  The iterated-primitive
characterisation and pentagon identity are Hopf-algebraic and
base-ring independent.  The Kirillov series `Σ x^n / (n · [n]_q)`
is the archimedean realisation.
-/

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **q-Dilogarithm data**: a level-2 iterated primitive of H_q
    characterised by the pentagon identity.  `Li2_q ∈ H ⊗ H`.  -/
-- Ref: [leitner2026] §2
structure QDilogarithm (H : Type*) [Add H] where
  /-- The level-2 primitive Li₂_q ∈ H ⊗ H. -/
  Li2 : H × H
  /-- The level-1 primitive log_q ∈ H (needed for pentagon). -/
  log_q : H
  /-- Evaluation map: Li₂_q applied to an element of H. -/
  Li2_eval : H → H
  /-- Binary composition for pentagon arguments: (x,y) ↦ xy. -/
  mul : H → H → H
  /-- Complement: x ↦ 1 - x. -/
  compl : H → H
  /-- Division: (x,y) ↦ x/y (requires y invertible). -/
  div : H → H → H
  /-- **Pentagon identity** (5-term relation):
      Li₂_q(y) + Li₂_q(x) = Li₂_q(xy) +
        Li₂_q(x(1-y)/(1-xy)) + Li₂_q(y(1-x)/(1-xy)). -/
  pentagon : ∀ (x y : H),
    Li2_eval y + Li2_eval x =
      Li2_eval (mul x y) +
      Li2_eval (div (mul x (compl y)) (compl (mul x y))) +
      Li2_eval (div (mul y (compl x)) (compl (mul x y)))

/-! ## Uniqueness

The uniqueness statement that stood here as
`QDilogarithm.unique_up_to_shift_axiom` was **false** and is deleted
(2026-09-06).  It concluded `L₁.Li2.1 = L₂.Li2.1` from agreement of
`log_q`, `mul`, `compl` and `div` -- but `Li2` is not mentioned by the
`pentagon` field at all (the pentagon constrains `Li2_eval`, a different
field), so `Li2` is free data and two such records can differ in it.

Refutation: `QOU.QAnalysisCounterexamples.not_qDilogarithm_unique`.
Live conditional statement, about `Li2_eval`:
`QOU.QDilogarithm.eval_unique_of_pentagon_rigid`.  Both live under
`QOU/QuantumObservableUniverses/`; see `prop:q-dilogarithm-unique`.

The axiom was declared twice, verbatim, here and in
`q-dilogarithm-unique.lean`. -/

end

end QOU
