import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.qReebVectorField

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/qReebVectorField.lean (monolithic).
That file no longer exists — the library was split, and `qReebVectorField` now lives at
  folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Particles.lean

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
/-- The canonical indeterminate `q = T¹` of `R_q`. -/
def q_param : R_q := LaurentPolynomial.T 1
/-- The inverse indeterminate `q⁻¹ = T⁻¹` of `R_q`. -/
def q_inv_param : R_q := LaurentPolynomial.T (-1)

universe u v

/-- **q-Deformed Reeb vector field**: defined by its action on smooth functions
    `ξ_q(f) = q⁻¹ ξ(f) + (1 − q⁻¹) [ξ, X_f]_q`.

    Here `xi_f p = ξ(f)(p)` and `bracket_q_xi_Xf p = [ξ, X_f]_q(p)` are the
    pointwise values over the ground ring `R_q`, and `q_inv` is the local
    value of `q⁻¹` (the image of `q_inv_param` under the substrate
    specialisation `ι : R_q → R_q`).

    LaTeX: `\label{def:q-reeb-vector-field}` -/
def qReebVectorField {M : Type*}
    (q_inv : M → R_q) (xi_f : M → R_q) (bracket_q_xi_Xf : M → R_q) (p : M) : R_q :=
  (q_inv p) * xi_f p +
    (1 - q_inv p) * bracket_q_xi_Xf p

end

end QOU
