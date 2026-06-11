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
# QOU.qConnection

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/qConnection.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

universe u v

/-- **q-Deformed connection**: `A_q = q⁻¹ A + (1 − q⁻¹) ι_ξ A · θ`.

    LaTeX: `\label{def:q-connection}` -/
noncomputable def qConnection {M : Type*} (sp : SubstrateParameter M)
    (connA : M → R_q) (iotaXiA : M → R_q) (theta : M → R_q) (p : M) : R_q :=
  (sp.field p)⁻¹ * connA p +
    (1 - (sp.field p)⁻¹) * (iotaXiA p * theta p)

/-- The q-deformed connection recovers the classical connection at `q = 1`. -/
theorem qConnection_classical {M : Type*} (sp : SubstrateParameter M)
    (connA iotaXiA theta : M → R_q) (p : M) (hq : sp.field p = 1) :
    qConnection sp connA iotaXiA theta p = connA p := by
  simp [qConnection, hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

end QOU
