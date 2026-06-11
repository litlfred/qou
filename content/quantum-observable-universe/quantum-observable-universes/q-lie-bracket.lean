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
# QOU.qLieBracket

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/qLieBracket.lean (monolithic)

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

/-- **q-Deformed Lie bracket**:
    `[V, W]_q = q⁻¹ [V, W] + (1 − q⁻¹)(θ(V) L_ξ W − θ(W) L_ξ V)`.

    LaTeX: `\label{def:q-lie-bracket}` -/
noncomputable def qLieBracket {M : Type*} (sp : SubstrateParameter M)
    (bracket_VW : M → R_q) (thetaV_LxiW : M → R_q) (thetaW_LxiV : M → R_q)
    (p : M) : R_q :=
  (sp.field p)⁻¹ * bracket_VW p +
    (1 - (sp.field p)⁻¹) * (thetaV_LxiW p - thetaW_LxiV p)

/-- The q-deformed Lie bracket recovers the classical bracket at `q = 1`. -/
theorem qLieBracket_classical {M : Type*} (sp : SubstrateParameter M)
    (bracket_VW thetaV_LxiW thetaW_LxiV : M → R_q) (p : M) (hq : sp.field p = 1) :
    qLieBracket sp bracket_VW thetaV_LxiW thetaW_LxiV p = bracket_VW p := by
  simp [qLieBracket, hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

end QOU
