import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Monoidal.Types.Basic

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

/-- **The former axiom `substrate_self_duality_axiom` was false** (removed
    2026-11-15, with its wrapper `substrate_self_duality`). It claimed that
    `selfDualityMorphism S` is an isomorphism for *every*
    `SelfDualPairingData`, but that structure carries no counit or snake
    laws: `comul` and `frobeniusForm` are arbitrary morphisms. In `Type`, with
    `A = Bool` and `Δ b = (true, b)`, the morphism `φ` is constant at `true`,
    hence not injective. The true statement needs the Frobenius (snake)
    identities as fields; recorded as open in bean `qou-n2un`. -/
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 §2.3
theorem not_selfDualityMorphism_isIso_unconstrained :
    ¬ ∀ S : SelfDualPairingData (Type), IsIso (selfDualityMorphism S) := by
  intro h
  let S : SelfDualPairingData (Type) := ⟨Bool, fun b => (true, b), fun _ => PUnit.unit⟩
  have hb : Function.Bijective (selfDualityMorphism S) := (isIso_iff_bijective _).mp (h S)
  exact Bool.noConfusion (hb.1 (a₁ := true) (a₂ := false) rfl)

end QOU.AlgebraicSubstrate
