/-!
# QOU.AlgebraicSubstrate.CategoricalReebDerivation

The categorical Reeb derivation on a Frobenius–Hopf substrate,
encoding observer drift via the contact structure.

LaTeX label: `def:categorical-reeb-derivation`
-/

set_option autoImplicit false

import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic

open CategoryTheory MonoidalCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **CategoricalReebDerivation**: a derivation `ξ_q : A → A` on a
    Frobenius–Hopf substrate, equipped with a period `Ω_q` such that
    the iterated composition `ξ_q^Ω_q = id_A`.

    LaTeX: `\label{def:categorical-reeb-derivation}` -/
structure CategoricalReebDerivation (C : Type u) [Category.{v} C]
    [MonoidalCategory C] extends FrobeniusHopfSubstrate C where
  /-- The Reeb derivation `ξ_q : A → A`. -/
  reeb : obj ⟶ obj
  /-- The contact form `θ : 𝟙 → A`. -/
  contact : (𝟙_ C) ⟶ obj
  /-- The period of the Reeb flow. -/
  period : ℕ
  /-- Normalization: `ξ_q ∘ θ = θ`. -/
  reeb_normalizes : contact ≫ reeb = contact
  /-- Periodicity: `ξ_q^Ω_q = id_A`. -/
  reeb_periodic : reeb ^ period = 𝟙 obj

end QOU.AlgebraicSubstrate
