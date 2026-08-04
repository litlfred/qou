import UGB.GrobnerShirshov.AlgOps

namespace UGB.UnitalGroebner
open UGB.GrobnerShirshov
universe u v
variable {G : Type u} {k : Type v} [Field k] [DecidableEq G]

def sPolynomial (a₁ a₂ : k) (f₁ f₂ : AlgElement G k) : AlgElement G k :=
  AlgElement.sub (AlgElement.smul a₁⁻¹ f₁) (AlgElement.smul a₂⁻¹ f₂)

theorem s_polynomial_decomposition
    (a₁ a₂ c₁ c₂ : k) (f₁ f₂ : AlgElement G k)
    (ha₁ : a₁ ≠ 0) (ha₂ : a₂ ≠ 0)
    (hcancel : c₁ * a₁ + c₂ * a₂ = 0) :
    ∃ d : k,
      AlgElement.add (AlgElement.smul c₁ f₁) (AlgElement.smul c₂ f₂)
        = AlgElement.smul d (sPolynomial a₁ a₂ f₁ f₂) := by
  refine ⟨c₁ * a₁, ?_⟩
  rcases f₁ with ⟨coeff₁, supp₁, spec₁⟩
  rcases f₂ with ⟨coeff₂, supp₂, spec₂⟩
  dsimp [AlgElement.add, AlgElement.smul, sPolynomial, AlgElement.sub, AlgElement.neg]
  congr 1
  funext m
  have h3 : c₂ * a₂ = - (c₁ * a₁) := by
    calc c₂ * a₂ = (c₁ * a₁ + c₂ * a₂) - c₁ * a₁ := by ring
         _       = 0 - c₁ * a₁ := by rw [hcancel]
         _       = - (c₁ * a₁) := by ring
  have h2 : c₂ = - (c₁ * a₁) * a₂⁻¹ := by
    calc c₂ = c₂ * (a₂ * a₂⁻¹) := by rw [mul_inv_cancel₀ ha₂, mul_one]
         _  = (c₂ * a₂) * a₂⁻¹ := by ring
         _  = - (c₁ * a₁) * a₂⁻¹ := by rw [h3]
  rw [h2]
  calc c₁ * coeff₁ m + - (c₁ * a₁) * a₂⁻¹ * coeff₂ m
    _ = c₁ * (a₁ * a₁⁻¹) * coeff₁ m - c₁ * a₁ * a₂⁻¹ * coeff₂ m := by rw [mul_inv_cancel₀ ha₁, mul_one]; ring
    _ = (c₁ * a₁) * (a₁⁻¹ * coeff₁ m + - (a₂⁻¹ * coeff₂ m)) := by ring
