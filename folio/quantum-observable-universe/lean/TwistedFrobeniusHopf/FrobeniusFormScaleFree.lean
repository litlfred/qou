import Mathlib.CategoryTheory.Monoidal.Linear

/-!
# The snake identities do not fix the scale of the Frobenius form

In `FrobeniusHopfData` the Frobenius form `λ : A ⟶ 𝟙` is constrained only by the two snake
identities with the coevaluation `coev : 𝟙 ⟶ A ⊗ A`. Both are unchanged under
`λ ↦ s • λ`, `coev ↦ s⁻¹ • coev` for any unit `s : Fˣ` of the base ring. So the axioms do not fix the scale of the
pairing `ψ* ψ = λ(S(ψ) ψ)`, and with it the normalisation of the nucleon state that enters the
matter term `ψ* 𝒟 ψ` of the two-term Lagrangian.
-/

namespace QOU.MassTheory.FrobeniusFormScaleFree

open CategoryTheory MonoidalCategory

universe u v

variable {F : Type*} [CommRing F]
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C] [Linear F C]
  [MonoidalPreadditive C] [MonoidalLinear F C]

/-- Left snake identity survives `λ ↦ s • λ`, `coev ↦ s⁻¹ • coev`. -/
theorem snake_left_rescale (A : C) (mul : A ⊗ A ⟶ A) (lam : A ⟶ 𝟙_ C)
    (coev : 𝟙_ C ⟶ A ⊗ A) (s : Fˣ)
    (h : (ρ_ A).inv ≫ (A ◁ coev) ≫ (α_ A A A).inv ≫ ((mul ≫ lam) ▷ A) ≫ (λ_ A).hom = 𝟙 A) :
    (ρ_ A).inv ≫ (A ◁ (((s⁻¹ : Fˣ) : F) • coev)) ≫ (α_ A A A).inv ≫ ((mul ≫ ((s : F) • lam)) ▷ A) ≫
      (λ_ A).hom = 𝟙 A := by
  rw [MonoidalLinear.whiskerLeft_smul, Linear.comp_smul, MonoidalLinear.smul_whiskerRight]
  simp only [Linear.smul_comp, Linear.comp_smul, smul_smul, Units.mul_inv, one_smul]
  exact h

/-- Right snake identity survives the same rescaling. -/
theorem snake_right_rescale (A : C) (mul : A ⊗ A ⟶ A) (lam : A ⟶ 𝟙_ C)
    (coev : 𝟙_ C ⟶ A ⊗ A) (s : Fˣ)
    (h : (λ_ A).inv ≫ (coev ▷ A) ≫ (α_ A A A).hom ≫ (A ◁ (mul ≫ lam)) ≫ (ρ_ A).hom = 𝟙 A) :
    (λ_ A).inv ≫ ((((s⁻¹ : Fˣ) : F) • coev) ▷ A) ≫ (α_ A A A).hom ≫ (A ◁ (mul ≫ ((s : F) • lam))) ≫
      (ρ_ A).hom = 𝟙 A := by
  rw [MonoidalLinear.smul_whiskerRight, Linear.comp_smul, MonoidalLinear.whiskerLeft_smul]
  simp only [Linear.smul_comp, Linear.comp_smul, smul_smul, Units.mul_inv, one_smul]
  exact h

omit [MonoidalPreadditive C] [MonoidalLinear F C] in
/-- The pairing value scales: `(s • λ)(x) = s · λ(x)` for any `x : 𝟙 ⟶ A`. So the size of
`ψ* ψ` is not fixed by the snake identities. -/
theorem pairing_rescale (A : C) (lam : A ⟶ 𝟙_ C) (x : 𝟙_ C ⟶ A) (s : F) :
    x ≫ (s • lam) = s • (x ≫ lam) := Linear.comp_smul _ _ _ _ _ _

omit [MonoidalPreadditive C] [MonoidalLinear F C] in
/-- **The categorical trace is scale-free.** `leftTrace f = coev ≫ (f ▷ A) ≫ μ ≫ λ` is unchanged
by `λ ↦ s • λ`, `coev ↦ s⁻¹ • coev`. So the closed-loop trace, unlike the open pairing `ψ* ψ`, is
fixed by the axioms. -/
theorem leftTrace_rescale (A : C) (mul : A ⊗ A ⟶ A) (lam : A ⟶ 𝟙_ C)
    (coev : 𝟙_ C ⟶ A ⊗ A) (f : A ⟶ A) (s : Fˣ) :
    (((s⁻¹ : Fˣ) : F) • coev) ≫ (f ▷ A) ≫ mul ≫ ((s : F) • lam) = coev ≫ (f ▷ A) ≫ mul ≫ lam := by
  simp only [Linear.smul_comp, Linear.comp_smul, smul_smul, Units.mul_inv, one_smul]

end QOU.MassTheory.FrobeniusFormScaleFree
