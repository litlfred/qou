import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category


/-!
# QOU.FrobeniusHopfData.frobeniusForm

Frobenius pairing: the composite A ⊗ A → A → 𝟙 of multiplication and
a Frobenius form.  Non-degeneracy is characterized by snake identities
and induces an isomorphism A ≅ A∨.

LaTeX label: `def:frobenius-pairing`
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Frobenius pairing**: the composite `λ ∘ μ : A ⊗ A → 𝟙`.

    Given a Frobenius–Hopf object `(A, μ, λ)` in a monoidal category `C`,
    the Frobenius pairing is `⟨a, b⟩_F = λ(μ(a ⊗ b))`, i.e. the composite
    `A ⊗ A →[μ] A →[λ] 𝟙`.

    Non-degeneracy means this pairing induces an isomorphism `A ≅ A∨`.
    Equivalently, the snake identities hold with respect to a coevaluation
    `η̃ : 𝟙 → A ⊗ A`.

    LaTeX: `\label{def:frobenius-pairing}`
    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
structure FrobeniusPairing (C : Type u) [Category.{v} C]
    [MonoidalCategory C] (fh : FrobeniusHopfData C) where
  /-- The Frobenius pairing morphism `⟨-,-⟩_F : A ⊗ A → 𝟙`,
      defined as the composite `λ ∘ μ`. -/
  pairing : (fh.obj ⊗ fh.obj) ⟶ (𝟙_ C)
  /-- The pairing factors through multiplication then the Frobenius form. -/
  pairing_eq : pairing = fh.mul ≫ fh.frobeniusForm

/-- Construct the canonical Frobenius pairing from a Frobenius–Hopf datum. -/
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
def FrobeniusHopfData.canonicalPairing {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (fh : FrobeniusHopfData C) :
    FrobeniusPairing C fh where
  pairing := fh.mul ≫ fh.frobeniusForm
  pairing_eq := rfl

/-- The Frobenius pairing is symmetric when the multiplication is
    commutative (i.e., `μ ∘ β = μ` where `β` is the braiding).
    In this case `⟨a, b⟩_F = ⟨b, a⟩_F`. -/
theorem FrobeniusPairing.symmetric_of_comm {C : Type u} [Category.{v} C]
    [MonoidalCategory C] {fh : FrobeniusHopfData C}
    (fp : FrobeniusPairing C fh)
    (β : fh.obj ⊗ fh.obj ⟶ fh.obj ⊗ fh.obj)
    (h_comm : β ≫ fh.mul = fh.mul) :
    β ≫ fp.pairing = fp.pairing := by
  rw [fp.pairing_eq]
  rw [← Category.assoc, h_comm]

/-- Non-degeneracy of the Frobenius pairing: the induced map
    `A → A∨` (currying one argument of the pairing) is an isomorphism.
    Stated as: the snake identities hold. -/
structure FrobeniusPairing.NonDegenerate {C : Type u} [Category.{v} C]
    [MonoidalCategory C] {fh : FrobeniusHopfData C}
    (fp : FrobeniusPairing C fh) where
  /-- The coevaluation morphism `η̃ : 𝟙 → A ⊗ A` dual to the pairing. -/
  coevaluation : (𝟙_ C) ⟶ (fh.obj ⊗ fh.obj)
  /-- Snake identity (left): the composite
      `A →[ρ⁻¹] A ⊗ 𝟙 →[id ⊗ η̃] A ⊗ A ⊗ A →[α⁻¹] (A ⊗ A) ⊗ A
       →[⟨-,-⟩_F ⊗ id] 𝟙 ⊗ A →[λ] A`
      equals `𝟙_A`. -/
  snake_left :
    (ρ_ fh.obj).inv ≫ (fh.obj ◁ coevaluation) ≫
    (α_ fh.obj fh.obj fh.obj).inv ≫
    (fp.pairing ▷ fh.obj) ≫ (λ_ fh.obj).hom = 𝟙 fh.obj
  /-- Snake identity (right): the mirror composite equals `𝟙_A`. -/
  snake_right :
    (λ_ fh.obj).inv ≫ (coevaluation ▷ fh.obj) ≫
    (α_ fh.obj fh.obj fh.obj).hom ≫
    (fh.obj ◁ fp.pairing) ≫ (ρ_ fh.obj).hom = 𝟙 fh.obj

/-- A Frobenius–Hopf datum with snake identities already has a
    non-degenerate canonical pairing. -/
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
def FrobeniusHopfData.hasNonDegeneratePairing {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (fh : FrobeniusHopfData C) :
    FrobeniusPairing.NonDegenerate (fh.canonicalPairing) where
  coevaluation := fh.coevaluation
  snake_left := by
    simp only [FrobeniusPairing.pairing, canonicalPairing]
    exact fh.pairing_snake_left
  snake_right := by
    simp only [FrobeniusPairing.pairing, canonicalPairing]
    exact fh.pairing_snake_right

end QOU
