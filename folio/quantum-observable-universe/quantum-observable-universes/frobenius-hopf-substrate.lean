import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
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
    [MonoidalCategory C] [BraidedCategory C] where
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
  /-- The right unit law is the mirror condition on the other tensor factor. -/
  mul_one : obj ◁ unit ≫ mul = (ρ_ obj).hom
  /-- Left counit law — the "counital" of axiom 2. -/
  counit_comul : comul ≫ counit ▷ obj = (λ_ obj).inv
  /-- The right counit law is the mirror condition on the other tensor
      factor. -/
  comul_counit : comul ≫ obj ◁ counit = (ρ_ obj).inv
  /-- Coassociativity — the "coassociative" of axiom 2. -/
  comul_assoc :
    comul ≫ obj ◁ comul = comul ≫ (comul ▷ obj) ≫ (α_ obj obj obj).hom
  /-- **Antipode axiom 1 — `S` reverses multiplication.**
      `μ ≫ S = (S ⊗ S) ≫ β ≫ μ`, in elements `S(ab) = S(b)S(a)`.

      The braiding is why this structure requires `[BraidedCategory C]`.  That
      is no new demand: the narrative already places the substrate at the level
      of a *quantum universe*, which is braided monoidal. -/
  antipode_anti_mul :
    mul ≫ antipode = (antipode ⊗ₘ antipode) ≫ (BraidedCategory.braiding obj obj).hom ≫ mul
  /-- **Antipode axiom 2 — `S` reverses comultiplication.**
      `S ≫ Δ = Δ ≫ β ≫ (S ⊗ S)`. -/
  antipode_anti_comul :
    antipode ≫ comul = comul ≫ (BraidedCategory.braiding obj obj).hom ≫ (antipode ⊗ₘ antipode)
  /-- **Antipode axiom 3 — `S` fixes the unit.** -/
  antipode_unit : unit ≫ antipode = unit
  /-- **Antipode axiom 4 — `S` preserves the counit.** -/
  antipode_counit : antipode ≫ counit = counit
  /-- **Antipode axiom 5 — `S` is involutive (unimodular / `q = 1` specialization).**
      `S ≫ S = 𝟙_A`.

      On its own this pins nothing: `S = 𝟙_A` satisfies it on every group
      tested (`computations/probes/frobenius_hopf_intermediate_axioms_probe.py`).
      It earns its place only alongside `antipode_anti_mul`, which `𝟙_A`
      fails whenever `A` is non-commutative. Away from `q = 1` (`O_q(SU(2))`
      where `S²(β) = q⁻² β`, or Taft `H_4` where `S²(X) = -X`), `S²` equals a
      pivotal automorphism `γ_A` (`TwistedPivotalFrobeniusHopfSubstrate` below). -/
  antipode_involutive : antipode ≫ antipode = 𝟙 obj
  /-- **Antipode axiom 6 — `S` preserves the Frobenius form (unimodular specialization).**
      `S ≫ λ = λ`, so the pairing `⟨a, b⟩ = λ(ab)` is `S`-invariant; on
      non-unimodular Hopf algebras (`H_4`), `S ≫ λ = modulusShift ≫ λ`. -/
  antipode_frobeniusForm : antipode ≫ frobeniusForm = frobeniusForm

/-- **Pivotal & modular-twisted Frobenius–Hopf substrate** (`TN-1`), replacing
    `S² = id` and `S ≫ λ = λ` with `S ≫ S = pivotalAut.hom` and
    `S ≫ λ = modulusShift ≫ λ` for `q ≠ 1` quantum groups and non-unimodular
    Hopf algebras. -/
structure TwistedPivotalFrobeniusHopfSubstrate (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] where
  obj : C
  mul : (obj ⊗ obj) ⟶ obj
  unit : (𝟙_ C) ⟶ obj
  comul : obj ⟶ (obj ⊗ obj)
  counit : obj ⟶ (𝟙_ C)
  antipode : obj ⟶ obj
  frobeniusForm : obj ⟶ (𝟙_ C)
  coevaluation : (𝟙_ C) ⟶ (obj ⊗ obj)
  pivotalAut : obj ≅ obj
  modulusShift : obj ⟶ obj
  mul_assoc :
    (α_ obj obj obj).hom ≫ (obj ◁ mul) ≫ mul = (mul ▷ obj) ≫ mul
  frobenius_relation :
    mul ≫ comul = (obj ◁ comul) ≫ (α_ obj obj obj).inv ≫ (mul ▷ obj)
  snake_left :
    (ρ_ obj).inv ≫ (obj ◁ coevaluation) ≫ (α_ obj obj obj).inv ≫
      ((mul ≫ frobeniusForm) ▷ obj) ≫ (λ_ obj).hom = 𝟙 obj
  snake_right :
    (λ_ obj).inv ≫ (coevaluation ▷ obj) ≫ (α_ obj obj obj).hom ≫
      (obj ◁ (mul ≫ frobeniusForm)) ≫ (ρ_ obj).hom = 𝟙 obj
  one_mul : unit ▷ obj ≫ mul = (λ_ obj).hom
  mul_one : obj ◁ unit ≫ mul = (ρ_ obj).hom
  counit_comul : comul ≫ counit ▷ obj = (λ_ obj).inv
  comul_counit : comul ≫ obj ◁ counit = (ρ_ obj).inv
  comul_assoc :
    comul ≫ obj ◁ comul = comul ≫ (comul ▷ obj) ≫ (α_ obj obj obj).hom
  antipode_anti_mul :
    mul ≫ antipode = (antipode ⊗ₘ antipode) ≫ (BraidedCategory.braiding obj obj).hom ≫ mul
  antipode_anti_comul :
    antipode ≫ comul = comul ≫ (BraidedCategory.braiding obj obj).hom ≫ (antipode ⊗ₘ antipode)
  antipode_unit : unit ≫ antipode = unit
  antipode_counit : antipode ≫ counit = counit
  antipode_sq_eq_pivotal : antipode ≫ antipode = pivotalAut.hom
  antipode_frobeniusForm_twisted : antipode ≫ frobeniusForm = modulusShift ≫ frobeniusForm

/-- Every classical `FrobeniusHopfSubstrate` embeds into `TwistedPivotalFrobeniusHopfSubstrate`. -/
def FrobeniusHopfSubstrate.toTwistedPivotal {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C]
    (S : FrobeniusHopfSubstrate C) : TwistedPivotalFrobeniusHopfSubstrate C where
  obj := S.obj
  mul := S.mul
  unit := S.unit
  comul := S.comul
  counit := S.counit
  antipode := S.antipode
  frobeniusForm := S.frobeniusForm
  coevaluation := S.coevaluation
  pivotalAut := Iso.refl S.obj
  modulusShift := 𝟙 S.obj
  mul_assoc := S.mul_assoc
  frobenius_relation := S.frobenius_relation
  snake_left := S.snake_left
  snake_right := S.snake_right
  one_mul := S.one_mul
  mul_one := S.mul_one
  counit_comul := S.counit_comul
  comul_counit := S.comul_counit
  comul_assoc := S.comul_assoc
  antipode_anti_mul := S.antipode_anti_mul
  antipode_anti_comul := S.antipode_anti_comul
  antipode_unit := S.antipode_unit
  antipode_counit := S.antipode_counit
  antipode_sq_eq_pivotal := S.antipode_involutive
  antipode_frobeniusForm_twisted := by simp [S.antipode_frobeniusForm]

end QOU.AlgebraicSubstrate
