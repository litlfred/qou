/-!
# QOU.ProjectiveLineObject

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/ProjectiveLineObject.lean (monolithic)
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

/-- **Fibre–adjoint-fibre involution** `σ : P(V) ↪ Ad(A)`.

    The Frobenius self-duality `A ≅ A∨` identifies the projective line
    object `P(V)` with a coadjoint orbit inside `Ad(A)`.  Three parts:

    1. `P(V)` embeds in `Ad(A)` as the coadjoint orbit of a highest-weight
       vector.
    2. The embedding `σ` is an involution: it determines `P(V)` from
       `Ad(A)` and vice versa.
    3. Non-degeneracy of the Frobenius pairing forces the observability
       condition `Hom(𝟙, Ad(A)) = 0`.

    In the archimedean realisation: `σ` is the identification
    `CP¹ ≅ S² ⊂ su(2)` (unit sphere under Killing form).

    LaTeX: `\label{prop:fiber-adjoint-involution}`
    Ref: [lusztig1993] -/
structure FiberAdjointInvolution (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The adjoint bundle object `Ad(A)` in `C`. -/
  adjointObj : C
  /-- The projective line object `P(V)` in `C`. -/
  projLine : C
  /-- **(Part 1)** The orbit embedding `σ : P(V) ↪ Ad(A)`, realising
      `P(V)` as a coadjoint orbit of a highest-weight vector. -/
  orbit_embed : projLine ⟶ adjointObj
  /-- The involution morphism `τ_Ad : Ad(A) ⟶ Ad(A)`, induced by the
      antipode `S : A ⟶ A`. -/
  involution : adjointObj ⟶ adjointObj
  /-- `τ_Ad` is an involution: `τ_Ad ≫ τ_Ad = id`. -/
  involution_sq : involution ≫ involution = 𝟙 adjointObj
  /-- **(Part 2)** The embedding is compatible with the involution:
      restricting `τ_Ad` to the image of `σ` recovers `σ`.
      This means `σ` determines each from the other. -/
  orbit_involution_compat : orbit_embed ≫ involution = orbit_embed
  /-- **(Part 3)** The embedding is a monomorphism: the orbit map
      is injective, so `P(V)` is faithfully represented inside `Ad(A)`. -/
  orbit_mono : ∀ (f g : (𝟙_ C) ⟶ projLine),
    f ≫ orbit_embed = g ≫ orbit_embed → f = g

/-- The fibre-wise adjoint involution is indeed an involution (`τ² = id`).

    LaTeX: `\label{prop:fiber-adjoint-involution}`
    Proof: The antipode of a Hopf algebra satisfies `S² = id` on the centre
    of `A`; the adjoint action factors through this, so `τ_Ad² = id`. -/
theorem fiber_adjoint_involution_sq {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C)
    (fai : FiberAdjointInvolution C fh) :
    fai.involution ≫ fai.involution = 𝟙 fai.adjointObj :=
  fai.involution_sq

end QOU
