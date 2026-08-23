import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse.Instanton
import QOU.GroundRingCore
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic

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

**Categorical layer, and where the `ℝ` actually sits (§7c).** The
vanishing argument is scalar-generic: it is `dq_sq_eq_zero_of_scalar_one`
below, stated over an arbitrary `R`-linear preadditive category with
`R` any ring — in particular over the Laurent ground ring
`R_q = ℤ[q, q⁻¹]` recorded here.  The `ℝ` that remains in
`categorical_dq_squared` is inherited from the *shared* structure
`CategoricalQExtDeriv` of `QOU.QuantumObservableUniverse.Instanton`,
whose deformation parameter is a field `q : ℝ` and whose `dq` is
therefore `ℝ`-linear (`[CategoryTheory.Linear ℝ C]`).  That `ℝ` is
carried by the structure, not by the mathematics: `categorical_dq_squared`
is now literally the generic lemma instantiated at `R := ℝ`.  Moving the
structure itself to a generic ground ring needs `q⁻¹` replaced by a
carried inverse field (`Ring` has no `⁻¹`), which is a change to
`Instanton.lean` and its four other consumers.  The substrate
specialisation `ι : R_q → ℝ, q ↦ q₀` is used for numerical evaluation
downstream.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

-- Ground ring from the canonical module rather than re-declared here.
-- This file used to declare `R_q`, `q_param` and `q_inv_param` directly in
-- `namespace QOU`, which collided with the SAME THREE NAMES in
-- `QOU/BraidKnot/CasimirShared.lean` — and there `R_q` is `RatFunc ℚ`, a
-- different ring. The two modules could never both be imported:
--
--     error: import QOU.CategoricalDqSquared failed, environment already
--            contains 'QOU.q_param' from QOU.BraidKnot.CasimirShared
--
-- Bean `qou-kfcl`.
open QOU.GroundRing

namespace QOU

noncomputable section

universe u v

/-- **Scalar-generic core of `d_q² = 0` at `q = 1`** (pre-archimedean, §7c).

    In the `.md` notation `a = q⁻¹`, `b = 1 - q⁻¹`, the q-exterior
    derivative is `d_q = a·d + b·(π_V ≫ d)`.  The classical-limit
    vanishing uses no property of the scalar ring beyond `1 - 1 = 0`:
    `a = 1` forces `b = 0`, hence `d_q = d` and `d_q ≫ d_q = d ≫ d = 0`.

    Stated over an arbitrary ring `R` and an `R`-linear preadditive
    category, so the argument is available over the Laurent ground ring
    `R_q = ℤ[q, q⁻¹]` above.  `Ring` is the weakest class that admits the
    construction: `CategoryTheory.Linear` needs a `Semiring`, and the
    coefficient `1 - a` needs subtraction; commutativity is never used. -/
theorem dq_sq_eq_zero_of_scalar_one {R : Type*} [Ring R] {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.Preadditive C]
    [CategoryTheory.Linear R C] {X : C} (d πV : X ⟶ X) (a : R) (ha : a = 1)
    (hd_sq : d ≫ d = 0) :
    (a • d + (1 - a) • (πV ≫ d)) ≫ (a • d + (1 - a) • (πV ≫ d)) = 0 := by
  subst ha
  simpa using hd_sq

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
  -- The `ℝ` realisation of `dq_sq_eq_zero_of_scalar_one` at `R := ℝ`:
  -- `dq`'s scalar is `a = q⁻¹`, which is `1` when `q = 1`.
  unfold CategoricalQExtDeriv.dq
  exact dq_sq_eq_zero_of_scalar_one cqd.d_classical cqd.proj_V cqd.q⁻¹
    (by rw [hq, inv_one]) hd_sq

end

end QOU
