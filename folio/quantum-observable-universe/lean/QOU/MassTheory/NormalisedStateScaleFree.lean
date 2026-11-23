import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.NoZeroSMulDivisors.Basic


/-!
# A normalised state makes the matter term independent of the scale of `λ`

The matter term of `ℒ = 𝒟² + ψ* ⊗ 𝒟ψ` is `ψ* ≫ ψ ≫ 𝒟` (field `CategoricalLagrangian.lagrangian_formula`).
It is bilinear in `(ψ*, ψ)`: `matter_rescale`. The pairing `ψ ≫ ψ*` scales by the same factor:
`norm_rescale`. Since `ψ* = λ ∘ S(ψ)` is linear in `λ`, rescaling `λ ↦ sλ` is a rescaling of the
costate, so the matter term carries the scale of `λ` (`CounitFrobeniusForm.matter_leftTrace_rescale`).

`matter_invariant_of_normalised`: if the state is normalised before and after a rescaling,
`ψ ≫ ψ* = 𝟙`, then the matter term does not change. So under the normalisation `ψ ≫ ψ* = 𝟙`
the scale of `λ` drops out of `ℒ` entirely: the bosonic term never carried it.

Scope. The normalisation `ψ ≫ ψ* = 𝟙` is a hypothesis. It is **not** a field of
`CategoricalLagrangian`, where `costate` and `state` are independent, and it is not stated in
`categorical-lagrangian.md`. Adopting it changes the definition, so it is the owner's call.
The hypothesis `𝟙 (𝟙_ C) ≠ 0` only excludes the zero category.
-/

namespace QOU.MassTheory.NormalisedStateScaleFree

open CategoryTheory MonoidalCategory

universe u v
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]
variable {K : Type*} [Field K] [Linear K C]

/-- The matter term is bilinear in `(ψ*, ψ)`. -/
theorem matter_rescale {A : C} (cs : A ⟶ 𝟙_ C) (st : 𝟙_ C ⟶ A) (D : A ⟶ A) (a b : K) :
    (a • cs) ≫ (b • st) ≫ D = (a * b) • (cs ≫ st ≫ D) := by
  simp only [Linear.smul_comp, Linear.comp_smul, smul_smul, mul_comm]

/-- The pairing `ψ ≫ ψ*` scales by the same factor. -/
theorem norm_rescale {A : C} (cs : A ⟶ 𝟙_ C) (st : 𝟙_ C ⟶ A) (a b : K) :
    (b • st) ≫ (a • cs) = (a * b) • (st ≫ cs) := by
  simp only [Linear.smul_comp, Linear.comp_smul, smul_smul]

/-- Normalised before and after, the matter term is unchanged. -/
theorem matter_invariant_of_normalised {A : C} (cs : A ⟶ 𝟙_ C) (st : 𝟙_ C ⟶ A) (D : A ⟶ A)
    (a b : K) (h1 : (𝟙 (𝟙_ C)) ≠ 0) (hn : st ≫ cs = 𝟙 (𝟙_ C))
    (hn' : (b • st) ≫ (a • cs) = 𝟙 (𝟙_ C)) :
    (a • cs) ≫ (b • st) ≫ D = cs ≫ st ≫ D := by
  have hab : a * b = 1 := by
    rw [norm_rescale, hn] at hn'
    have h0 : (a * b - 1) • (𝟙 (𝟙_ C)) = 0 := by rw [sub_smul, hn', one_smul, sub_self]
    rcases smul_eq_zero.mp h0 with h | h
    · exact sub_eq_zero.mp h
    · exact absurd h h1
  rw [matter_rescale, hab, one_smul]

end QOU.MassTheory.NormalisedStateScaleFree
