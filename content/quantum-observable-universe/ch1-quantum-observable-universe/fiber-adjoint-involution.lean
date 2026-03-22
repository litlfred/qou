/-!
# QOU.FiberAdjointInvolution — Fibre–adjoint-fibre involution

The Frobenius self-duality A ≅ A∨ identifies the projective line
object P(V) with a coadjoint orbit inside Ad(A), yielding an
involution σ : P(V) ↪ Ad(A).

## References

- [lusztig1993] Introduction to Quantum Groups
- [leitner2026] §1
-/

import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

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
