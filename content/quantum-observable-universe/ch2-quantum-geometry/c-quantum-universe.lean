/-!
# QOU.CRManifoldData

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/CRManifoldData.lean (monolithic)
-/

import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousFunction.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **CR manifold data** for the ℂ realisation.

    A 5-tuple `(M, θ, G, P, E)` as in Example 1.3.  `M` is a CR manifold
    of hypersurface type with non-degenerate Levi form; `θ` is the contact
    form (pseudo-Hermitian structure); `G = SU(2)`; `P → M` is a principal
    `G`-bundle; `E = P ×_G CP¹` is the state bundle.

    LaTeX: `\label{def:c-quantum-universe}` -/
structure CRManifoldData where
  /-- The underlying smooth manifold carrier. -/
  M : Type*
  [topM : TopologicalSpace M]
  /-- CR dimension `n ≥ 1`; real dimension of `M` is `2n + 1`. -/
  n : ℕ
  n_pos : 0 < n
  /-- Levi form signature `(r, s)` with `r + s = n`. -/
  r : ℕ
  s : ℕ
  rs_sum : r + s = n
  /-- The contact form `θ` as a continuous real-valued function.
      Full type: a section of `T*M` (1-form), here modelled as `C(M, ℝ)`.
      The contact condition `θ ∧ (dθ)^n ≠ 0` is a non-degeneracy axiom
      that requires differential forms; we record θ as a continuous function
      and state the non-degeneracy separately. -/
  contactForm : C(M, ℝ)
  /-- The contact form is non-degenerate: there exists a point where θ ≠ 0. -/
  contact_nondeg : ∃ p : M, contactForm p ≠ 0
  /-- The Reeb vector field `ξ`, characterised by `ι_ξ dθ = 0` and `θ(ξ) = 1`.
      Modelled as a continuous self-map `M → M` (the Reeb flow at time 1).
      Full type: a section of `TM`. -/
  reebField : C(M, M)
  /-- The Reeb field preserves the contact form: θ(ξ(p)) = θ(p) for all p. -/
  reeb_preserves_contact : ∀ p : M, contactForm (reebField p) = contactForm p

end QOU
