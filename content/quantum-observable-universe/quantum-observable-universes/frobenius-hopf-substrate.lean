import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic

/-!
# QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate

The quantum vacuum as a self-dual Frobenius–Hopf algebra in a rigid
monoidal category.

LaTeX label: `def:frobenius-hopf-substrate`
-/

set_option autoImplicit false


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
  /-- Frobenius relation: `Δ ∘ μ = (μ ⊗ id) ∘ α⁻¹ ∘ (id ⊗ Δ)` as a
      morphism `A ⊗ A → A ⊗ A`. -/
  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  frobenius_relation :
    mul ≫ comul =
    (obj ◁ comul) ≫ (α_ obj obj obj).inv ≫ (mul ▷ obj)
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
  /-- Left unit law — the "unital" of axiom 1. -/
  one_mul : unit ▷ obj ≫ mul = (λ_ obj).hom
  /-- Right unit law. -/
  mul_one : obj ◁ unit ≫ mul = (ρ_ obj).hom
  /-- Left counit law — the "counital" of axiom 2. -/
  counit_comul : comul ≫ counit ▷ obj = (λ_ obj).inv
  /-- Right counit law. -/
  comul_counit : comul ≫ obj ◁ counit = (ρ_ obj).inv
  /-- Coassociativity — the "coassociative" of axiom 2. -/
  comul_assoc :
    comul ≫ obj ◁ comul = comul ≫ (comul ▷ obj) ≫ (α_ obj obj obj).hom
  /-- **Antipode axiom (left)** — `Δ ≫ S ▷ A ≫ μ = ε ≫ η`.

      `S` is the convolution inverse of `id_A`, hence unique: the antipode is
      *determined* by `(μ, η, Δ, ε)` and is not free data.

      Added 2026-09-14 on owner decision (beans `qou-c64q`, `qou-qjhc`).  Until
      then this structure named `antipode` and constrained it with nothing, so
      every question about `S` — `S² = id` included — was independent of the
      definition rather than open.  Record of that state:
      `QOU.AntipodeIndependence`; the uniqueness proof lives in
      `QOU.QuantumObservableUniverse.AntipodeDetermined`. -/
  antipode_left : comul ≫ antipode ▷ obj ≫ mul = counit ≫ unit
  /-- **Antipode axiom (right)** — `Δ ≫ A ◁ S ≫ μ = ε ≫ η`. -/
  antipode_right : comul ≫ obj ◁ antipode ≫ mul = counit ≫ unit

end QOU.AlgebraicSubstrate
