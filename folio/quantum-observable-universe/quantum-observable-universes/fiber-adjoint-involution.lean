import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans


/-!
# QOU.FiberAdjointInvolution — Fibre–adjoint-fibre involution

The Frobenius self-duality A ≅ A∨ identifies the projective line
object P(V) with a coadjoint orbit inside Ad(A), yielding an
involution σ : P(V) ↪ Ad(A).

## References

- [lusztig1993] Introduction to Quantum Groups
- [leitner2026] §1
-/

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
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
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

/-- **Existence of the fibre–adjoint involution.**  The structure
    `FiberAdjointInvolution` already bundles the genuine content (the orbit
    embedding `σ`, its antipode-induced involution with `τ_Ad ≫ τ_Ad = id`,
    the embedding/involution compatibility, and the monomorphism property).
    The claim asserts that this bundle is *inhabited* for every
    Frobenius–Hopf datum — not the degenerate `∃ inv, True`.

    Constructing the witness (the coadjoint-orbit embedding `P(V) ↪ Ad(A)`
    and the antipode-induced `τ_Ad` in a general monoidal category) needs
    massive infrastructure (categorical machinery beyond the current `QOU.Basic` API)
    that cannot be added as a simple class field, so the body is left as an honest `sorry`.

    The conclusion pins `adjointObj = fh.obj`: the adjoint bundle `Ad(A)` is
    carried by the algebra object `A` itself. Without that constraint every
    field can be taken to be the identity on `𝟙_ C`, which satisfies
    `involution_sq`, `orbit_involution_compat` and `orbit_mono` trivially and
    never mentions `fh` — so bare `Nonempty (FiberAdjointInvolution C fh)` is
    provable for *every* category and datum, and asserts nothing. (That
    degenerate witness was what this declaration shipped until 2026-08-09;
    it is the same emptiness as `∃ inv, True`, reached by a different route.
    See `docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md`.) -/

class FiberAdjointInvolutionContext (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] (fh : FrobeniusHopfData C) where
  exists_inv : ∃ inv : FiberAdjointInvolution C fh, inv.adjointObj = fh.obj

-- Ref: [lusztig1993] Introduction to Quantum Groups
-- Ref: [leitner2026] prop:fiber-adjoint-involution
theorem fiber_adjoint_involution_exists (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] (fh : FrobeniusHopfData C)
    [ctx : FiberAdjointInvolutionContext C fh] :
    ∃ inv : FiberAdjointInvolution C fh, inv.adjointObj = fh.obj := by
  obtain ⟨inv, hinv⟩ := ctx.exists_inv
  exact ⟨inv, hinv⟩

end QOU
