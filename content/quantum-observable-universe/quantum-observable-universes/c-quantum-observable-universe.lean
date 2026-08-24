import QOU.Basic
import QOU.Glossary
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousMap.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.CQuantumObservableUniverse

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/CQuantumObservableUniverse.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    Mirrors the sibling block `c-quantum-universe.lean`; see
    `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ

/-- **CR manifold data** for the ℂ realisation (local prerequisite).

    Re-declared from the sibling block `c-quantum-universe.lean`
    (`def:c-quantum-universe`) so this sibling is a self-contained
    compilation unit — importing the library `CRRealisation` module
    would collide with its own `CQuantumObservableUniverse`
    declaration.  Keep field-for-field in sync with the sibling. -/
structure CRManifoldData where
  /-- The underlying smooth manifold carrier. -/
  M : Type*
  [topM : TopologicalSpace M]
  /-- CR dimension `n ≥ 1`; real dimension of `M` is `2n + 1`. -/
  n : ℕ
  /-- `n ≥ 1`, as the docstring above already claimed. Taken from the library
      copy, which had it where this one did not (bean `qou-u87j`). -/
  n_pos : 0 < n
  /-- Levi form signature `(r, s)` with `r + s = n`. -/
  r : ℕ
  s : ℕ
  rs_sum : r + s = n
  /-- The contact form `θ` as a real-valued function on `M`.

      Was `M → R_q`. A contact form is a real 1-form: this structure's own
      `reebField` docstring characterises `ξ` by `ι_ξ dθ = 0` and `θ(ξ) = 1`,
      and neither the exterior derivative nor the normalisation `= 1` means
      anything over `R_q = ℤ[q, q⁻¹]`. §7c reserves `ℝ` for archimedean
      constructs and this is one; the library copy always had `ℝ`
      (bean `qou-u87j`). -/
  contactForm : M → ℝ
  /-- The contact form is non-degenerate: there exists a point where θ ≠ 0. -/
  contact_nondeg : ∃ p : M, contactForm p ≠ 0
  /-- The Reeb vector field `ξ`, characterised by `ι_ξ dθ = 0` and `θ(ξ) = 1`. -/
  reebField : C(M, M)
  /-- The Reeb field preserves the contact form: θ(ξ(p)) = θ(p) for all p. -/
  reeb_preserves_contact : ∀ p : M, contactForm (reebField p) = contactForm p

/-- **ℂ quantum observable universe**: CR manifold data satisfying the
    vanishing conditions `H⁰(M, Ad(P)) = 0` and `Γ_c(M, S) = 0`.

    LaTeX: `\label{def:c-quantum-observable-universe}` -/
structure CQuantumObservableUniverse extends CRManifoldData where
  /-- The type of global sections of the adjoint bundle `Ad(P)`. -/
  adjointSections : Type*
  /-- `H⁰(M, Ad(P))` is trivial: all global adjoint sections are equal.
      In a vector space this means `H⁰(M, Ad(P)) = 0`. -/
  adjoint_cohomology_vanishes : Subsingleton adjointSections
  /-- The type of compactly supported sections of the state bundle `S`. -/
  compactStateSections : Type*
  /-- `Γ_c(M, S)` is trivial: all compactly supported state sections are equal. -/
  state_sections_vanish : Subsingleton compactStateSections

end

end QOU
