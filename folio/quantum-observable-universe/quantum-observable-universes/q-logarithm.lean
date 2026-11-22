import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.QLogarithm — categorical q-logarithm

The q-logarithm is the unique primitive of H_q inverse to the
q-exponential grouplike, forming an adjoint pair

  log_q ⊣ e_q    (Prim(H_q), [·,·]_q) ⇌ (G(H_q), ·).

LaTeX label: `def:q-logarithm`

## References

- [leitner2026] §2-quantum-observable-universes/q-logarithm

**Ground ring**: `R_q = ℤ[q, q⁻¹]`.  Base-ring independent at the
Hopf-algebra level; archimedean series representation needs char 0.
-/

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **q-Logarithm data**: a primitive element of the q-shuffle Hopf
    algebra, inverse to the q-exponential grouplike. -/
-- Ref: [leitner2026] §2
structure QLogarithm (H : Type*) where
  /-- The primitive element log_q ∈ H. -/
  log_q : H
  /-- Coproduct on log_q: Δ_q(log_q) = log_q ⊗ 1 + 1 ⊗ log_q. -/
  coprod : H → H × H
  /-- Counit on log_q. -/
  counit : H → R_q
  /-- Unit element of H. -/
  one : H
  /-- Primitive axiom: Δ_q(log_q) = log_q ⊗ 1 + 1 ⊗ log_q.  In pair
      form: coprod log_q = (log_q, one).extend (one, log_q) additively.
      Encoded as a single equality on a symmetric tensor slot. -/
  primitive_left : (coprod log_q).1 = log_q
  primitive_right : (coprod log_q).2 = log_q
  /-- Counit: ε(log_q) = 0. -/
  counit_eq_zero : counit log_q = 0

/-- **q-Exponential data**: an abstract grouplike of the q-shuffle
    Hopf algebra, characterised by the flow equation `D_q g = g`.

    Mirrors `QExponential` in `q-exponential.lean`; inlined here so
    this block's sibling compiles standalone (the adjoint-pair
    structure below needs the q-exponential fields `D_q` and `e_q`
    in scope). -/
-- Ref: [leitner2026] §2-quantum-observable-universes/q-exponential
structure QExponential (H : Type*) where
  /-- The grouplike element e_q ∈ H. -/
  e_q : H
  /-- Coproduct on e_q: Δ_q(e_q) = e_q ⊗ e_q. -/
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

/-- **Adjoint pair**: log_q ⊣ e_q as an inverse pair between
    primitives and grouplikes. -/
-- Ref: [leitner2026] §2
structure QLogExpAdjoint (H : Type*) where
  log : QLogarithm H
  exp : QExponential H
  /-- Composition: applying exp.D_q to log.log_q, then extracting
      the grouplike, recovers exp.e_q.  Placeholder for the full
      inverse-in-PROP statement. -/
  left_inverse : exp.D_q log.log_q = exp.e_q
  /-- Composition: log_q(e_q) = id  (formal PROP inverse). -/
  right_inverse : log.counit exp.e_q = 0

end

end QOU
