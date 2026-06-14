import QOU.Basic


/-!
# QOU.CategoricalQConnection.exists — existence of the categorical q-connection

∇_q = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇ ∘ θ is compositional.

LaTeX: `\label{prop:categorical-q-connection-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-connection-exists
- [connes1994] Noncommutative Geometry
-/

namespace QOU

/-- **Existence of the categorical q-connection.**

    For every category `C` with the required enrichments, a
    `CategoricalQConnection C` term exists via the formula
    `∇_q = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇ ∘ θ`. -/
-- Ref: [connes1994]
theorem CategoricalQConnection.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    [CategoryTheory.Linear R_q C]
    (cqc : CategoricalQConnection C) :
    ∃ (nabla_q : cqc.A ⟶ (cqc.A ⊗ cqc.Omega1)),
      nabla_q = cqc.q⁻¹ • cqc.nabla + (1 - cqc.q⁻¹) • (cqc.xi_contract_nabla ≫ cqc.theta_nabla) :=
  ⟨cqc.nabla_q, rfl⟩

end QOU
