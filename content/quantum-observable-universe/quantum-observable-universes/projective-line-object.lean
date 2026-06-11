import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
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


/-!
# QOU.ProjectiveLineObject

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/ProjectiveLineObject.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Projective line object** `P(V) = G_q / T` in a monoidal category.

    The coset object obtained by quotienting the quantum gauge group `G_q`
    by the maximal torus `T = Aut⊗(ω|_{C₀})`.  Its function algebra is
    the `T`-coinvariant subalgebra `O_q(P(V)) = A^{co T}`.

    In the archimedean realisation: `P(V) ≅ SU(2)/U(1) ≅ CP¹`.

    LaTeX: `\label{def:projective-line-object}`
    Ref: [kock2004] -/
structure ProjectiveLineObject (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The underlying object `P(V)` in `C` (the coset `G_q / T`). -/
  obj : C
  /-- The Frobenius–Hopf object `A` whose coset this is. -/
  hopfObj : C
  /-- Base-point morphism `∞ : 𝟙 → P(V)` (the identity coset). -/
  basePoint : (𝟙_ C) ⟶ obj
  /-- Action morphism `ρ : A ⊗ P(V) → P(V)` encoding the `G_q`-action
      on the coset space, compatible with the Hopf multiplication. -/
  action : (hopfObj ⊗ obj) ⟶ obj
  /-- The coinvariant inclusion `P(V) ↪ A`: the function algebra
      `O_q(P(V)) = A^{co T}` is a sub-object of `A`. -/
  coinvariant_incl : obj ⟶ hopfObj
  /-- The coinvariant inclusion is a monomorphism (abstractly:
      the coset embeds faithfully into the Hopf object). -/
  coinvariant_mono : ∀ (f g : (𝟙_ C) ⟶ obj),
    f ≫ coinvariant_incl = g ≫ coinvariant_incl → f = g

end QOU
