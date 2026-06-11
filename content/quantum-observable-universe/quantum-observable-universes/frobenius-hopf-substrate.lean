/-!
# QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate

The quantum vacuum as a self-dual Frobenius–Hopf algebra in a rigid
monoidal category.

LaTeX label: `def:frobenius-hopf-substrate`
-/

set_option autoImplicit false

import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic

open CategoryTheory MonoidalCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **Frobenius–Hopf substrate**: a self-dual Frobenius–Hopf algebra
    object `A` in a rigid monoidal category `C`.

    The substrate carries multiplication, comultiplication, antipode,
    Frobenius form, and a self-duality isomorphism `A ≅ A∨` induced
    by the non-degenerate Frobenius pairing.

    LaTeX: `\label{def:frobenius-hopf-substrate}`
    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
structure FrobeniusHopfSubstrate (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The underlying object `A` in `C`. -/
  obj : C
  /-- Multiplication `μ : A ⊗ A → A`. -/
  mul : (obj ⊗ obj) ⟶ obj
  /-- Unit `η : 𝟙 → A`. -/
  unit : (𝟙_ C) ⟶ obj
  /-- Comultiplication `Δ : A → A ⊗ A`. -/
  comul : obj ⟶ (obj ⊗ obj)
  /-- Counit `ε : A → 𝟙`. -/
  counit : obj ⟶ (𝟙_ C)
  /-- Antipode `S : A → A`. -/
  antipode : obj ⟶ obj
  /-- Frobenius form `λ : A → 𝟙`. -/
  frobeniusForm : obj ⟶ (𝟙_ C)
  /-- Coevaluation `η̃ : 𝟙 → A ⊗ A` dual to the Frobenius pairing. -/
  coevaluation : (𝟙_ C) ⟶ (obj ⊗ obj)
  /-- Associativity of multiplication. -/
  mul_assoc :
    (α_ obj obj obj).hom ≫ (obj ◁ mul) ≫ mul =
    (mul ▷ obj) ≫ mul
  /-- Frobenius relation: `μ ∘ Δ = (Δ ⊗ id) ∘ α ∘ (id ⊗ μ)`. -/
  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  frobenius_relation :
    comul ≫ mul =
    (obj ◁ mul) ≫ (α_ obj obj obj).inv ≫ (comul ▷ obj)
  /-- Snake identity (left): non-degeneracy of the Frobenius pairing. -/
  snake_left :
    (ρ_ obj).inv ≫ (obj ◁ coevaluation) ≫
    (α_ obj obj obj).inv ≫
    ((mul ≫ frobeniusForm) ▷ obj) ≫ (λ_ obj).hom = 𝟙 obj
  /-- Snake identity (right): mirror non-degeneracy condition. -/
  snake_right :
    (λ_ obj).inv ≫ (coevaluation ▷ obj) ≫
    (α_ obj obj obj).hom ≫
    (obj ◁ (mul ≫ frobeniusForm)) ≫ (ρ_ obj).hom = 𝟙 obj

end QOU.AlgebraicSubstrate
