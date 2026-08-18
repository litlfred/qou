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
import QOU.QuantumObservableUniverse.CategoricalFoundations


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

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
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
  /-- The deformation parameter `q`. -/
  q : R_q
  /-- A two-sided inverse for `q`, carried as **data**.

      The ground ring `R_q = ℤ[q, q⁻¹]` is a ring, not a field: it has no
      `Inv` instance, so `q⁻¹` cannot be *written* even though the
      indeterminate `q` is invertible in it. Carrying the inverse
      explicitly, with its defining relation below, is the same move the
      QOU existence statement makes (`(q qinv : R) (hq : q * qinv = 1)`),
      and it is strictly stronger than the `q ≠ 0` it replaces —
      over a ring, invertible is not implied by nonzero. -/
  qinv : R_q
  /-- `qinv` is the inverse of `q`. Replaces the former `q_ne_zero`. -/
  q_mul_qinv : q * qinv = 1
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
  -- d_q = q⁻¹ · d + (1 − q⁻¹) · (π_V ≫ d), with `q⁻¹` supplied by `qinv`
  cqd.qinv • cqd.d_classical + (1 - cqd.qinv) • (cqd.proj_V ≫ cqd.d_classical)

/-- When `q = 1`, `d_q` reduces to `d`. -/
theorem CategoricalQExtDeriv.dq_classical {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R_q C]
    (cqd : CategoricalQExtDeriv C) (hq : cqd.q = 1) :
    cqd.dq = cqd.d_classical := by
  -- `q = 1` forces `qinv = 1` through the defining relation, rather than
  -- through `inv_one` (which needs an `Inv` instance `R_q` does not have).
  have hqinv : cqd.qinv = 1 := by
    have h := cqd.q_mul_qinv
    rw [hq, one_mul] at h
    exact h
  simp [dq, hqinv, sub_self, zero_smul, one_smul, add_zero]

end

end QOU
