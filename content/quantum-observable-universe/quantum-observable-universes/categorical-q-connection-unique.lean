import QOU.Basic
import QOU.QuantumObservableUniverses.QDifferentialGeometry


/-!
# QOU.CategoricalQConnection.unique — uniqueness of the categorical q-connection

∇_q uniquely determined by (∇, ξ, θ, q), inheriting the gauge
freedom of ∇.

LaTeX: `\label{prop:categorical-q-connection-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted
`axiom : Subsingleton (CategoricalQConnection C)`, which is **false**:
the structure bundles its objects (`A`, `Omega1` are fields), so any
category with two objects carrying connection data gives distinct
instances.

This file now imports the relocated `CategoricalQConnection` structure
(`QOU.QuantumObservableUniverses.QDifferentialGeometry`) and **proves**
— with no axiom — exactly the narrative claim: given the same
classical data `(A, Ω¹, ∇, ξ⌟∇, θ, q)`, the structure is uniquely
determined; q-deformation introduces no additional freedom.  Since
`nabla`, `xi_contract_nabla`, `theta_nabla` live over the bundled
objects, the data comparisons use `HEq` transported along the object
equalities.

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-connection-unique
- [connes1994] Noncommutative Geometry
-/

namespace QOU

open CategoryTheory
open MonoidalCategory

universe u v

/-- **Uniqueness of the categorical q-connection (proved
    extensionality).**

    Two `CategoricalQConnection C` instances with the same underlying
    objects and the same classical data `(∇, ξ⌟∇, θ, q)` are equal:
    `q_ne_zero` is propositional.  Replaces a false
    `Subsingleton (CategoricalQConnection C)` axiom (the structure
    bundles its objects). -/
-- Ref: [connes1994] Noncommutative Geometry
theorem CategoricalQConnection.unique
    (C : Type u) [Category.{v} C] [MonoidalCategory C]
    [Preadditive C] [Linear Archimedean.R_q C]
    (c₁ c₂ : CategoricalQConnection C)
    (hA : c₁.A = c₂.A)
    (hΩ : c₁.Omega1 = c₂.Omega1)
    (hnabla : HEq c₁.nabla c₂.nabla)
    (hxi : HEq c₁.xi_contract_nabla c₂.xi_contract_nabla)
    (htheta : HEq c₁.theta_nabla c₂.theta_nabla)
    (hq : c₁.q = c₂.q) : c₁ = c₂ := by
  cases c₁
  cases c₂
  subst hA
  subst hΩ
  rw [heq_iff_eq] at hnabla hxi htheta
  subst hnabla
  subst hxi
  subst htheta
  subst hq
  rfl

end QOU
