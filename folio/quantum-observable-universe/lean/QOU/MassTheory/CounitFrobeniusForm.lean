import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Linear

/-!
# The counit as Frobenius form, and why the matter constant is not a closed trace

Two checks on how the Frobenius form `λ` could be normalised.

**1. `λ = ε` against the snake identities.** `counit_snake_right`: with evaluation `μ ≫ ε` and
coevaluation `η ≫ Δ`, the right snake identity holds, from the Frobenius relation, the left unit
law and the right counit law alone. So taking the counit as Frobenius form is compatible with the
right snake identity in every `FrobeniusHopfData`, with coevaluation `η ≫ Δ`. The left snake
identity would need the mirror Frobenius relation `μ ≫ Δ = (A ◁ Δ) ≫ α⁻¹ ≫ (μ ▷ A)`, which is not
an axiom of `FrobeniusHopfData`; it is not checked here.

**2. The matter constant as a closed trace.** `matter_leftTrace_rescale`: if the costate is
`ψ* = h ≫ λ` (as in `categorical-lagrangian.md`, `ψ* = λ ∘ S(ψ)`), then any closed trace of the
matter term `ψ* ≫ ψ ≫ 𝒟` scales by `s` under `λ ↦ sλ`, `coev ↦ s⁻¹coev`. The closed loop cancels
one `λ` against `coev`, but the costate carries a second `λ`. So the matter constant is not
scale-free, closed trace or not: its normalisation is the normalisation of `λ`.
-/

namespace QOU.MassTheory.CounitFrobeniusForm

open CategoryTheory MonoidalCategory

universe u v

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]

/-- Right snake identity for the counit as Frobenius form, with coevaluation `η ≫ Δ`. -/
theorem counit_snake_right (F : QOU.FrobeniusHopfData C) :
    (λ_ F.obj).inv ≫ ((F.unit ≫ F.comul) ▷ F.obj) ≫ (α_ F.obj F.obj F.obj).hom ≫
      (F.obj ◁ (F.mul ≫ F.counit)) ≫ (ρ_ F.obj).hom = 𝟙 F.obj := by
  have hF := F.frobenius_relation
  have h1 : ((F.unit ≫ F.comul) ▷ F.obj) ≫ (α_ F.obj F.obj F.obj).hom ≫
      (F.obj ◁ (F.mul ≫ F.counit)) =
      (F.unit ▷ F.obj) ≫ (F.mul ≫ F.comul) ≫ (F.obj ◁ F.counit) := by
    rw [hF, comp_whiskerRight, whiskerLeft_comp]
    simp only [Category.assoc]
  rw [reassoc_of% h1, ← Category.assoc (F.unit ▷ F.obj) F.mul, F.one_mul]
  simp only [Iso.inv_hom_id_assoc]
  rw [← Category.assoc F.comul, F.comul_counit, Iso.inv_hom_id]

variable {K : Type*} [Field K] [Preadditive C] [Linear K C]
  [MonoidalPreadditive C] [MonoidalLinear K C]

omit [BraidedCategory C] in
/-- A closed trace of the matter term `(h ≫ λ) ≫ g` scales by `s` under the rescaling
`λ ↦ s • λ`, `coev ↦ s⁻¹ • coev`. -/
theorem matter_leftTrace_rescale (A : C) (mul : A ⊗ A ⟶ A) (lam : A ⟶ 𝟙_ C)
    (coev : 𝟙_ C ⟶ A ⊗ A) (h : A ⟶ A) (g : 𝟙_ C ⟶ A) (s : K) (hs : s ≠ 0) :
    (s⁻¹ • coev) ≫ ((h ≫ (s • lam) ≫ g) ▷ A) ≫ mul ≫ (s • lam) =
      s • (coev ≫ ((h ≫ lam ≫ g) ▷ A) ≫ mul ≫ lam) := by
  simp only [Linear.smul_comp, Linear.comp_smul, MonoidalLinear.smul_whiskerRight, smul_smul]
  congr 1
  field_simp

end QOU.MassTheory.CounitFrobeniusForm
