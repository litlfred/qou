import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Module.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Finset.Basic

abbrev Monomial (G : Type u) := List G

structure AlgElement (G : Type u) (k : Type v) [Ring k] where
  coeff : Monomial G → k
  support : Finset (Monomial G)
  support_spec : ∀ m, m ∉ support → coeff m = 0

def AlgElement.add {G} {k} [Ring k] (f g : AlgElement G k) : AlgElement G k where
  coeff := fun m => f.coeff m + g.coeff m
  support := f.support ∪ g.support
  support_spec := sorry

def AlgElement.smul {G} {k} [Ring k] (c : k) (f : AlgElement G k) : AlgElement G k where
  coeff := fun m => c * f.coeff m
  support := f.support
  support_spec := sorry

def AlgElement.neg {G} {k} [Ring k] (f : AlgElement G k) : AlgElement G k where
  coeff := fun m => -(f.coeff m)
  support := f.support
  support_spec := sorry

def AlgElement.sub {G} {k} [Ring k] (f g : AlgElement G k) : AlgElement G k :=
  AlgElement.add f (AlgElement.neg g)

def sPolynomial {G} {k} [Field k] (a₁ a₂ : k) (f₁ f₂ : AlgElement G k) : AlgElement G k :=
  AlgElement.sub (AlgElement.smul a₁⁻¹ f₁) (AlgElement.smul a₂⁻¹ f₂)

theorem s_polynomial_decomposition {G} {k} [Field k] [DecidableEq G]
    (a₁ a₂ c₁ c₂ : k) (f₁ f₂ : AlgElement G k)
    (ha₁ : a₁ ≠ 0) (ha₂ : a₂ ≠ 0)
    (hcancel : c₁ * a₁ + c₂ * a₂ = 0) :
    ∃ d : k,
      AlgElement.add (AlgElement.smul c₁ f₁) (AlgElement.smul c₂ f₂)
        = AlgElement.smul d (sPolynomial a₁ a₂ f₁ f₂) := by
  refine ⟨c₁ * a₁, ?_⟩
  ext m
  dsimp [AlgElement.add, AlgElement.smul, AlgElement.sub, AlgElement.neg, sPolynomial]
  -- c₁ * f₁.coeff m + c₂ * f₂.coeff m = (c₁ * a₁) * (a₁⁻¹ * f₁.coeff m - a₂⁻¹ * f₂.coeff m)
  sorry
