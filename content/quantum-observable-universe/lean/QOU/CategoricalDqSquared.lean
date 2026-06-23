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
import QOU.QuantumObservableUniverse.Instanton

/-!
# QOU.categorical_dq_squared

Canonical Lake-built source for `prop:categorical-dq-squared` /
`prf:categorical-dq-squared`.  Sibling stubs at
`content/.../quantum-observable-universes/categorical-dq-squared.lean`
and `categorical-dq-squared-proof.lean` re-export this module via
`import QOU.CategoricalDqSquared`.

**Open authoring task** (`AUDIT-REPORT.md §P3` item 10): the theorem
below proves the *classical-limit direction* `d_q² = 0` at `q = 1`.
The narrative also claims the *non-vanishing direction* `d_q² ≠ 0` for
`q ≠ 1`; that direction remains open.  In `QOU/QuantumObservableUniverse/Instanton.lean`
the same statement under the new name `categorical_dq_squared_classical_limit`
makes the directional asymmetry explicit; the original name is
preserved here to keep the content-block URI
`qou:QOU.categorical_dq_squared` resolvable.

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

/-- **Proposition (Non-vanishing of d_q²).**
    The composition `d_q ∘ d_q : Ωᵏ(A) → Ωᵏ⁺²(A)` does not vanish
    for generic forms when `q ≠ 1`:
    `d_q² α = q⁻¹(1 − q⁻¹) ω_V ∧_q [ξ, α]`.

    `d_q² = 0` iff `q = 1` (classical) or `[ξ, α] = 0` (ξ-invariant forms).

    We prove the classical direction: when `q = 1` and `d² = 0`, then `d_q² = 0`.

    LaTeX: `\label{prop:categorical-dq-squared}` -/
theorem categorical_dq_squared {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear ℝ C]
    (cqd : CategoricalQExtDeriv C)
    (hq : cqd.q = 1)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0) :
    cqd.dq ≫ cqd.dq = 0 := by
  -- When q = 1, d_q = d (by dq_classical), so d_q² = d² = 0.
  rw [cqd.dq_classical hq]
  exact hd_sq

end  -- noncomputable section

end QOU
