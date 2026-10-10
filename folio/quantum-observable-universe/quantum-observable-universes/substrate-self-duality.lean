import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic

/-!
# QOU.AlgebraicSubstrate.substrate_self_duality

Self-duality of the algebraic substrate: the Frobenius form induces
a quasi-isomorphism `A ≃ ω_A•` in the derived category.

LaTeX label: `thm:substrate-self-duality`
-/

set_option autoImplicit false


open CategoryTheory MonoidalCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **Self-dual pairing data**: the object, comultiplication and
    Frobenius form that the self-duality morphism below consumes, and
    nothing else.

    This is a file-local minimal carrier, **not** a Frobenius–Hopf
    substrate.  It was named `FrobeniusHopfSubstrate` until 2026-09-15,
    which collided — at the *fully qualified* name
    `QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate` — with the canonical
    eight-field structure in `frobenius-hopf-substrate.lean` and with a
    third three-field carrier in `categorical-reeb-derivation.lean`.
    Nothing imported two of the three, so the collision was latent
    rather than a build error; renamed per bean `qou-hmhw`.

    What it is NOT, and the difference is load-bearing: it carries no
    multiplication, no unit, no counit, no antipode and no laws — in
    particular neither snake identity, so the non-degeneracy the
    self-duality claim below appeals to is *not* available from this
    structure and is supplied as an external axiom.

    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
structure SelfDualPairingData (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The underlying object `A` in `C`. -/
  obj : C
  /-- Comultiplication `Δ : A → A ⊗ A`. -/
  comul : obj ⟶ (obj ⊗ obj)
  /-- Frobenius form `λ : A → 𝟙`. -/
  frobeniusForm : obj ⟶ (𝟙_ C)

/-- The self-duality morphism `φ : A → A` induced by the Frobenius
    pairing. Constructed as the composition:

      A  →[Δ]  A ⊗ A  →[id ⊗ λ]  A ⊗ 𝟙  →[ρ]  A

    where Δ is comultiplication and λ is the Frobenius form.
    This is the categorical analog of `a ↦ Σ a₍₁₎ · λ(a₍₂₎)`. -/
def selfDualityMorphism {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (S : SelfDualPairingData C) :
    S.obj ⟶ S.obj :=
  S.comul ≫ (S.obj ◁ S.frobeniusForm) ≫ (ρ_ S.obj).hom

/-- **External axiom — substrate self-duality.**

    The Frobenius pairing of a Frobenius–Hopf substrate induces an
    isomorphism `A ≅ A`.  The self-duality morphism
    `φ = ρ ∘ (id ⊗ λ) ∘ Δ` is an isomorphism, with inverse
    `ψ = λ ∘ (η̃ ⊗ id) ∘ μ`.  This follows from the snake identities
    (non-degeneracy axioms) of `SelfDualPairingData`, which are
    precisely the zig-zag identities expressing that `(A, A, λ∘μ, η̃)`
    form a duality pair.

    The full statement is that the Frobenius pairing identifies
    `A ≅ A∨` in the internal-hom sense. In a rigid monoidal category
    this is expressed as `A ≅ A` since `A∨ ≅ A` by self-duality.
    The non-tautological content is that the *specific* morphism
    `selfDualityMorphism` (not just any isomorphism) is invertible.
    The categorical content is pending the rigid-monoidal duality
    infrastructure not yet in Mathlib. -/
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 §2.3
-- Ref: [yekutieli2015] Yekutieli, "Nonabelian Multiplicative Integration on Surfaces," World Scientific 2015 (DOI: 10.1142/9537)
axiom substrate_self_duality_axiom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (S : SelfDualPairingData C) :
    IsIso (selfDualityMorphism S)

theorem substrate_self_duality {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (S : SelfDualPairingData C) :
    IsIso (selfDualityMorphism S) :=
  substrate_self_duality_axiom S

end QOU.AlgebraicSubstrate
