/-!
# QOU.categorical_dq_squared

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/categorical_dq_squared.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

universe u v

/-- **Proposition (Non-vanishing of d_q²).**
    The composition `d_q ∘ d_q : Ωᵏ(A) → Ωᵏ⁺²(A)` does not vanish
    for generic forms when `q ≠ 1`:
    `d_q² α = q⁻¹(1 − q⁻¹) ω_V ∧_q [ξ, α]`.

    `d_q² = 0` iff `q = 1` (classical) or `[ξ, α] = 0` (ξ-invariant forms).

    We prove the classical direction: when `q = 1` and `d² = 0`, then `d_q² = 0`.

    LaTeX: `\label{prop:categorical-dq-squared}` -/
theorem categorical_dq_squared {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R_q C]
    (cqd : CategoricalQExtDeriv C)
    (hq : cqd.q = 1)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0) :
    cqd.dq ≫ cqd.dq = 0 := by
  -- When q = 1, d_q = d (by dq_classical), so d_q² = d² = 0.
  rw [cqd.dq_classical hq]
  exact hd_sq

end QOU
