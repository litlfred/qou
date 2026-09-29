import Mathlib.CategoryTheory.Endomorphism
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic

/-!
# QOU.AlgebraicSubstrate.CategoricalReebDerivation

The categorical Reeb derivation on a Frobenius–Hopf substrate,
encoding observer drift via the contact structure.

LaTeX label: `def:categorical-reeb-derivation`

This file is verified standalone.  `ReebAlgebraData` below is a
file-local three-field carrier — object, multiplication, unit — inlined
so the derivation block elaborates without an inter-sibling import.  It
is **not** the Frobenius–Hopf substrate, which is the eight-field
`FrobeniusHopfSubstrate` of `frobenius-hopf-substrate.lean`
(`def:frobenius-hopf-substrate`) and carries eleven laws this one does
not, the two antipode axioms among them.

"Keep the two in sync" is what this note used to say, and it is
withdrawn: they are different structures with different obligations, so
there is nothing to synchronise.  What the old wording produced was a
*fully qualified* name collision — this carrier, the canonical
structure, and a third in `substrate-self-duality.lean` all declared
`QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate` — latent only because
nothing imports two of them.  Bean `qou-hmhw`.
-/

set_option autoImplicit false


open CategoryTheory MonoidalCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **Reeb algebra data**: the object, multiplication and unit that the
    Reeb derivation below consumes, and nothing else.

    This is a file-local minimal carrier, **not** a Frobenius–Hopf
    substrate.  It was named `FrobeniusHopfSubstrate` until 2026-09-15,
    which collided — at the *fully qualified* name
    `QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate` — with the canonical
    eight-field structure in `frobenius-hopf-substrate.lean` and with a
    third three-field carrier in `substrate-self-duality.lean`.  Nothing
    imported two of the three, so the collision was latent rather than a
    build error; renamed per bean `qou-hmhw`.

    What it is NOT, and the difference is load-bearing: it carries no
    comultiplication, no counit, no antipode, no Frobenius form and no
    laws.  In particular the antipode axioms added to the canonical
    structure on 2026-09-14 (bean `qou-c64q`) do not apply here, so a
    reader must not transport results about that structure to this one.

    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
structure ReebAlgebraData (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The underlying object `A` in `C`. -/
  obj : C
  /-- Multiplication `μ : A ⊗ A → A`. -/
  mul : (obj ⊗ obj) ⟶ obj
  /-- Unit `η : 𝟙 → A`. -/
  unit : (𝟙_ C) ⟶ obj

/-- **CategoricalReebDerivation**: a derivation `ξ_q : A → A` on a
    Frobenius–Hopf substrate, equipped with a contact form `θ` and a
    period `Ω_q` such that the iterated composition `ξ_q^Ω_q = id_A`.

    Two of the narrative's (`def:categorical-reeb-derivation`)
    conditions are encoded as fields below:
    * **Normalization** `ξ_q ∘ θ = θ` (`reeb_normalizes`), and
    * **Periodicity** `ξ_q^{Ω_q} = id_A` (`reeb_periodic`).

    The narrative's **derivation / Leibniz rule**
    `ξ_q ∘ μ = μ ∘ (ξ_q ⊗ id + id ⊗ ξ_q)` is *not* encoded as a field
    here: its additive form `ξ_q ⊗ id + id ⊗ ξ_q` requires a
    preadditive ambient category, so it is recorded in the narrative
    only and deferred to the preadditive specialisation.

    LaTeX: `\label{def:categorical-reeb-derivation}` -/
structure CategoricalReebDerivation (C : Type u) [Category.{v} C]
    [MonoidalCategory C] extends ReebAlgebraData C where
  /-- The Reeb derivation `ξ_q : A → A`, carried as an element of the
      endomorphism monoid `End obj` so that the periodicity field below
      can use its monoid power.  `End obj` unfolds to `obj ⟶ obj`, so
      `reeb ≫ contact` still elaborates. -/
  reeb : End obj
  /-- The contact form `θ : A → 𝟙`. -/
  contact : obj ⟶ (𝟙_ C)
  /-- The period of the Reeb flow. -/
  period : ℕ
  /-- Normalization: `ξ_q ∘ θ = θ`, i.e. the derivation preserves the
      contact form (`reeb ≫ contact = contact`). -/
  reeb_normalizes : reeb ≫ contact = contact
  /-- Periodicity: `ξ_q^{Ω_q} = id_A`.  The power and identity are
      taken in the endomorphism monoid `End obj`, whose multiplication
      is composition and whose unit `1` is `𝟙 obj`. -/
  reeb_periodic : (reeb : End obj) ^ period = 1

end QOU.AlgebraicSubstrate
