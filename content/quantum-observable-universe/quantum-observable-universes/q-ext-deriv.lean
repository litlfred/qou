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
# QOU.qExtDeriv

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/qExtDeriv.lean (monolithic)

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

/-- **q-Deformed exterior derivative**: `d_q α = q⁻¹ dα + (1 − q⁻¹) θ ∧ L_ξ α`.

    LaTeX: `\label{def:q-ext-deriv}` -/
noncomputable def qExtDeriv {M : Type*} (sp : SubstrateParameter M)
    (d_alpha : M → R_q) (lieDerivReeb : M → R_q) (theta : M → R_q) (p : M) : R_q :=
  (sp.field p)⁻¹ * d_alpha p +
    (1 - (sp.field p)⁻¹) * (theta p * lieDerivReeb p)

/-- The q-deformed exterior derivative recovers the classical `d` at `q = 1`. -/
theorem qExtDeriv_classical {M : Type*} (sp : SubstrateParameter M)
    (d_alpha lieDerivReeb theta : M → R_q) (p : M) (hq : sp.field p = 1) :
    qExtDeriv sp d_alpha lieDerivReeb theta p = d_alpha p := by
  simp [qExtDeriv, hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

end QOU
