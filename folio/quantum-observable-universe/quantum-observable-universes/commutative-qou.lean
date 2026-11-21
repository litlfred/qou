import Mathlib.CategoryTheory.Monoidal.Braided.Basic


/-!
# QOU.CommutativeQOU

The strictly commutative specialisation of a QOU: the Frobenius-Hopf
object A is commutative (equivalently, by self-duality, cocommutative),
corresponding to the classical limit q → 1.

LaTeX label: `def:commutative-qou`

**Ground ring**: `ℤ` (structural).  Purely algebraic; no analysis.
-/

namespace QOU

open CategoryTheory MonoidalCategory BraidedCategory

/-- **Commutative QOU**: a QOU together with the structural
    witness that the Frobenius-Hopf object A is commutative as an
    algebra object inside the ambient braided category 𝐂.

    Concretely: if (A, μ, η) is the algebra structure on A and
    c_{A,A} : A ⊗ A → A ⊗ A is the braiding, then
      μ ∘ c_{A,A} = μ
    which, by self-duality of Frobenius-Hopf, also forces
      c_{A,A} ∘ Δ = Δ
    (cocommutativity of the coalgebra).

    LaTeX: `\label{def:commutative-qou}`
    Ref: [leitner2026] Chapter 3, §Varying Euler + mirror bundle -/
class CommutativeQOU
    (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C]
    (A : C) (μ : A ⊗ A ⟶ A) : Prop where
  /-- The multiplication is invariant under the braiding on A ⊗ A. -/
  -- Ref: [leitner2026] Chapter 3, §Varying Euler + mirror bundle
  mul_commutes : (β_ A A).hom ≫ μ = μ

end QOU
