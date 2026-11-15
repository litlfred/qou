import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.QExponential — categorical q-exponential

The q-exponential is the unique grouplike e_q of the q-shuffle Hopf
algebra H_q satisfying the flow equation D_q e_q = e_q, e_q(0) = 1.

LaTeX label: `def:q-exponential`

This is a purely Hopf-algebraic characterisation — no power series.
The convergent Taylor series e_q(x) = Σ x^n / [n]_q! is an
archimedean realisation (char 0 only).

## References

- [leitner2026] §2-quantum-observable-universes/q-exponential

**Ground ring**: `R_q = ℤ[q, q⁻¹]`.  The existence of e_q as an
abstract grouplike is base-ring independent.  The series
representation requires invertibility of [n]_q! in R, which fails
in characteristic p.
-/

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **q-Exponential data**: an abstract grouplike of the q-shuffle
    Hopf algebra, characterised by the flow equation `D_q g = g`.

    Encoded as a structure with the coproduct-diagonal and
    counit-unit axioms, plus the flow-invariance condition.  -/
-- Ref: [leitner2026] §2
structure QExponential (H : Type*) where
  /-- The grouplike element e_q ∈ H. -/
  e_q : H
  /-- Coproduct on e_q: Δ_q(e_q) = e_q ⊗ e_q.  Encoded via a
      prescribed coproduct function `coprod : H → H × H`. -/
  coprod : H → H × H
  /-- Counit on e_q. -/
  counit : H → R_q
  /-- q-Jackson derivative on H. -/
  D_q : H → H
  /-- Grouplike axiom: Δ_q(e_q) = (e_q, e_q). -/
  grouplike : coprod e_q = (e_q, e_q)
  /-- Counit: ε(e_q) = 1. -/
  counit_eq_one : counit e_q = 1
  /-- Flow equation: D_q e_q = e_q. -/
  flow_invariant : D_q e_q = e_q

/-! ## Uniqueness

The uniqueness statement that stood here as `QExponential.unique_axiom`
was **false** and is deleted (2026-09-06).  `coprod := fun x => (x, x)`,
a constant counit and `D_q := id` satisfy `grouplike`, `counit_eq_one`
and `flow_invariant` for *every* `e_q`, so two records agree on all
three hypothesised fields and differ in the concluded one.

Refutation: `QOU.QAnalysisCounterexamples.not_qExponential_unique`.
Live conditional statement:
`QOU.QExponential.unique_of_flow_rigid`.  See `prop:q-exponential-unique`.

The axiom was declared twice, verbatim, here and in
`q-exponential-unique.lean`. -/

end

end QOU
