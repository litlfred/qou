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
# QOU.CategoricalQExtDeriv

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/CategoricalQExtDeriv.lean (monolithic)

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

/-- **Categorical q-deformed exterior derivative**.

    On a quantum observable universe with weight decomposition `π_H, π_V`
    and substrate parameter `q`, the q-deformed exterior derivative is
    `d_q = q⁻¹ d + (1 − q⁻¹) π_V ∘ d`.  It acts as `q⁻¹ d` on horizontal
    forms and as `d` on vertical forms.

    LaTeX: `\label{def:categorical-q-ext-deriv}` -/
structure CategoricalQExtDeriv (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C _ _
  /-- The classical differential `d : Ωᵏ(A) → Ωᵏ⁺¹(A)`. -/
  d_classical : frobHopf.obj ⟶ frobHopf.obj
  /-- The vertical projection `π_V`. -/
  proj_V : frobHopf.obj ⟶ frobHopf.obj
  /-- The deformation parameter `q` (non-zero). -/
  q : R_q
  q_ne_zero : q ≠ 0
  /-- Idempotency of the vertical projection: `π_V ∘ π_V = π_V`. -/
  proj_V_idem : proj_V ≫ proj_V = proj_V

/-- The horizontal projection `π_H = id − π_V`. -/
def CategoricalQExtDeriv.proj_H {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cqd : CategoricalQExtDeriv C) : cqd.frobHopf.obj ⟶ cqd.frobHopf.obj :=
  𝟙 _ - cqd.proj_V

/-- The q-deformed derivative `d_q` as a morphism: `q⁻¹ d + (1 − q⁻¹) π_V ≫ d`.
    In a preadditive ℝ-linear category, this is the explicit linear combination.
    This is the categorical analogue of `qExtDeriv`. -/
noncomputable def CategoricalQExtDeriv.dq {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R_q C]
    (cqd : CategoricalQExtDeriv C) : cqd.frobHopf.obj ⟶ cqd.frobHopf.obj :=
  -- d_q = q⁻¹ · d + (1 − q⁻¹) · (π_V ≫ d)
  (cqd.q⁻¹) • cqd.d_classical + (1 - cqd.q⁻¹) • (cqd.proj_V ≫ cqd.d_classical)

/-- When `q = 1`, `d_q` reduces to `d`. -/
theorem CategoricalQExtDeriv.dq_classical {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R_q C]
    (cqd : CategoricalQExtDeriv C) (hq : cqd.q = 1) :
    cqd.dq = cqd.d_classical := by
  simp [dq, hq, inv_one, sub_self, zero_smul, one_smul, add_zero]

end QOU
