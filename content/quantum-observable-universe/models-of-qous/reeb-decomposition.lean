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
# QOU.ReebDecomposition

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/ReebDecomposition.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

/- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

universe u v

/-- **Reeb decomposition** of a differential form on a CR manifold.

    Every `k`-form `α` decomposes as `α = α_H + θ ∧ ι_ξ α` where
    `α_H` is the horizontal component and `θ ∧ ι_ξ α` is the vertical
    component.

    LaTeX: `\label{def:reeb-decomposition}` -/
structure ReebDecomposition (M : Type*) where
  /-- The total form (abstract representative).

      Real-valued. This structure and the two components below were `M → R_q`
      where the library copy (`lean/QOU/QuantumObservableUniverse/Particles.lean:18`)
      has `ℝ`. The docstring above settles it: the decomposition
      `α = α_H + θ ∧ ι_ξ α` is written with the contact form `θ` and the
      interior product `ι_ξ`, which are real differential-geometric operations
      on a CR manifold — the same reason `CRManifoldData.contactForm` is `ℝ`.
      Bean `qou-u87j`. -/
  total : M → ℝ
  /-- Horizontal component `α_H` satisfying `ι_ξ α_H = 0`. -/
  horizontal : M → ℝ
  /-- Vertical component `α_V = θ ∧ ι_ξ α`. -/
  vertical : M → ℝ
  /-- Decomposition identity: `total = horizontal + vertical`. -/
  decomp : ∀ (p : M), total p = horizontal p + vertical p

/-- A form is **purely horizontal** iff its vertical component vanishes. -/
def ReebDecomposition.isPurelyHorizontal {M : Type*}
    (rd : ReebDecomposition M) : Prop :=
  ∀ (p : M), rd.vertical p = 0

end

end QOU
