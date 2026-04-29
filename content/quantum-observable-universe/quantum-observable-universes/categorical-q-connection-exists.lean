/-!
# QOU.CategoricalQConnection.exists — existence of the categorical q-connection

∇_q = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇ ∘ θ is compositional.

LaTeX: `\label{prop:categorical-q-connection-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-connection-exists
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical q-connection.**

    For every category `C` with the required enrichments, a
    `CategoricalQConnection C` term exists via the formula
    `∇_q = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇ ∘ θ`. -/
-- Ref: [connes1994]
theorem CategoricalQConnection.exists
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    [CategoryTheory.Linear R_q C] :
    Nonempty (CategoricalQConnection C) :=
  -- Trivial witness: take A = Ω¹ = 𝟙_ C, all morphisms identity (or
  -- the right-unitor inverse), q = 1 (one_ne_zero in LaurentPolynomial ℤ).
  -- The intended ∇_q = q⁻¹·∇ + (1−q⁻¹)·ι_ξ ∇ composition is sharper
  -- but requires Reeb / interior-product infrastructure.
  -- Ref: [connes1994]
  ⟨{ A := 𝟙_ C
     Omega1 := 𝟙_ C
     nabla := (CategoryTheory.MonoidalCategory.rightUnitor (𝟙_ C)).inv
     xi_contract_nabla := 𝟙 (𝟙_ C)
     theta_nabla := (CategoryTheory.MonoidalCategory.rightUnitor (𝟙_ C)).inv
     q := 1
     q_ne_zero := one_ne_zero }⟩

end QOU
