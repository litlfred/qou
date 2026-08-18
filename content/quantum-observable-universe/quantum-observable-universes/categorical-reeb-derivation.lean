import Mathlib.CategoryTheory.Endomorphism
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic

/-!
# QOU.AlgebraicSubstrate.CategoricalReebDerivation

The categorical Reeb derivation on a Frobenius–Hopf substrate,
encoding observer drift via the contact structure.

LaTeX label: `def:categorical-reeb-derivation`

This file is verified standalone.  The upstream substrate structure
`FrobeniusHopfSubstrate` lives in the sibling content block
`frobenius-hopf-substrate.lean` (`def:frobenius-hopf-substrate`); a
minimal copy is inlined here so the derivation block elaborates without
an inter-sibling import.  Keep the two in sync.
-/

set_option autoImplicit false


open CategoryTheory MonoidalCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **Frobenius–Hopf substrate** (inlined from
    `def:frobenius-hopf-substrate`): a self-dual Frobenius–Hopf algebra
    object `A` in a rigid monoidal category `C`.

    Only the fields consumed by the Reeb derivation are retained here
    (object, multiplication, unit); the full Frobenius/snake data is in
    the canonical sibling block.

    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
structure FrobeniusHopfSubstrate (C : Type u) [Category.{v} C]
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
    [MonoidalCategory C] extends FrobeniusHopfSubstrate C where
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
