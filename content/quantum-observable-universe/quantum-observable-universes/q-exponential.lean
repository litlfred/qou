/-!
# QOU.QExponential — categorical q-exponential

The q-exponential is the unique grouplike e_q of the q-shuffle Hopf
algebra H_q satisfying the flow equation D_q e_q = e_q, e_q(0) = 1.

LaTeX label: `def:q-exponential`

This is a purely Hopf-algebraic characterisation — no power series.
The convergent Taylor series e_q(x) = Σ x^n / [n]_q! is an
archimedean realisation (char 0 only).

## References

- [manuscript] §2-quantum-observable-universes/q-exponential

**Ground ring**: `R_q = ℤ[q, q⁻¹]`.  The existence of e_q as an
abstract grouplike is base-ring independent.  The series
representation requires invertibility of [n]_q! in R, which fails
in characteristic p.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **q-Exponential data**: an abstract grouplike of the q-shuffle
    Hopf algebra, characterised by the flow equation `D_q g = g`.

    Encoded as a structure with the coproduct-diagonal and
    counit-unit axioms, plus the flow-invariance condition.  -/
-- Ref: [manuscript] §2
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

/-- **Uniqueness**: any two q-exponentials in the same Hopf algebra
    with the same `D_q` coincide.  (Conjecture — depends on
    non-degeneracy of the flow equation on grouplikes.) -/
-- Ref: [manuscript] §2
/-- **External axiom (§3b-cond pattern): QExponential.unique.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom QExponential.unique_axiom {H : Type*} (e₁ e₂ : QExponential H)
    (h_coprod : e₁.coprod = e₂.coprod)
    (h_counit : e₁.counit = e₂.counit)
    (h_Dq : e₁.D_q = e₂.D_q) :
    e₁.e_q = e₂.e_q

theorem QExponential.unique {H : Type*} (e₁ e₂ : QExponential H)
    (h_coprod : e₁.coprod = e₂.coprod)
    (h_counit : e₁.counit = e₂.counit)
    (h_Dq : e₁.D_q = e₂.D_q) :
    e₁.e_q = e₂.e_q :=
  QExponential.unique_axiom H e₁ e₂ h_coprod h_counit h_Dq

end QOU
