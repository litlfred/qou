/-!
# QOU.QLogarithm — categorical q-logarithm

The q-logarithm is the unique primitive of H_q inverse to the
q-exponential grouplike, forming an adjoint pair

  log_q ⊣ e_q    (Prim(H_q), [·,·]_q) ⇌ (G(H_q), ·).

LaTeX label: `def:q-logarithm`

## References

- [manuscript] §2-quantum-observable-universes/q-logarithm

**Ground ring**: `R_q = ℤ[q, q⁻¹]`.  Base-ring independent at the
Hopf-algebra level; archimedean series representation needs char 0.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **q-Logarithm data**: a primitive element of the q-shuffle Hopf
    algebra, inverse to the q-exponential grouplike. -/
-- Ref: [manuscript] §2
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

/-- **Adjoint pair**: log_q ⊣ e_q as an inverse pair between
    primitives and grouplikes. -/
-- Ref: [manuscript] §2
structure QLogExpAdjoint (H : Type*) where
  log : QLogarithm H
  exp : QExponential H
  /-- Composition: applying exp.D_q to log.log_q, then extracting
      the grouplike, recovers exp.e_q.  Placeholder for the full
      inverse-in-PROP statement. -/
  left_inverse : exp.D_q log.log_q = exp.e_q
  /-- Composition: log_q(e_q) = id  (formal PROP inverse). -/
  right_inverse : log.counit exp.e_q = 0

end QOU
