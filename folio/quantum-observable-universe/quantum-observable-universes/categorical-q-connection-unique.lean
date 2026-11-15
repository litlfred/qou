import QOU.Basic
import QOU.QuantumObservableUniverses.QDifferentialGeometry


/-!
# QOU.CategoricalQConnection.unique — uniqueness of the categorical q-connection

`∇_q` is uniquely determined by `(∇, ξ⌟∇, θ, q)`: the `nabla_q_formula`
field forces the q-deformed connection, so two q-connections sharing the
classical data coincide — q-deformation introduces no additional gauge
freedom.

LaTeX: `\label{prop:categorical-q-connection-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted
`axiom : Subsingleton (CategoricalQConnection C)`, which is **false**:
the structure bundles its objects (`A`, `Omega1` are fields), so any
category with two objects carrying connection data gives distinct
instances.

This file imports the relocated, **strengthened** `CategoricalQConnection`
structure (`QOU.QuantumObservableUniverses.QDifferentialGeometry`,
following the `proof-integrity` law-field pattern): `nabla_q` is pinned
by `nabla_q_formula`, so the proof below is a genuine *determination* —
given the same objects and classical data `(∇, ξ⌟∇, θ, q, q⁻¹)`, the
derived q-connection (and hence the whole structure) is forced.  Since
the morphism fields live over the bundled objects, the data comparisons
use `HEq` transported along the object equalities.

## References

- [leitner2026] §2-quantum-observable-universes/categorical-q-connection-unique
- [connes1994] Noncommutative Geometry
-/

namespace QOU

open CategoryTheory
open MonoidalCategory

universe u v

/-- **Uniqueness of the categorical q-connection (proved
    determination).**

    Two `CategoricalQConnection C` instances with the same underlying
    objects and the same classical data `(∇, ξ⌟∇, θ, q, q⁻¹)` are
    equal: the `nabla_q` morphism is forced by `nabla_q_formula`, and
    `q_unit` is proof-irrelevant.  This replaces a false
    `Subsingleton (CategoricalQConnection C)` axiom (the structure
    bundles its objects) with the determination the narrative actually
    claims — q-deformation introduces no additional gauge freedom. -/
-- Ref: [connes1994] Noncommutative Geometry
theorem CategoricalQConnection.unique
    (C : Type u) [Category.{v} C] [MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [Preadditive C] [Linear Archimedean.R_q C]
    (c₁ c₂ : CategoricalQConnection C)
    (hA : c₁.A = c₂.A)
    (hΩ : c₁.Omega1 = c₂.Omega1)
    (hnabla : HEq c₁.nabla c₂.nabla)
    (hxi : HEq c₁.xi_contract_nabla c₂.xi_contract_nabla)
    (htheta : HEq c₁.theta_nabla c₂.theta_nabla)
    (hq : c₁.q = c₂.q)
    (hqinv : c₁.qinv = c₂.qinv) : c₁ = c₂ := by
  obtain ⟨A₁, Ω₁, n₁, x₁, t₁, q₁, qi₁, hu₁, nq₁, hf₁⟩ := c₁
  obtain ⟨A₂, Ω₂, n₂, x₂, t₂, q₂, qi₂, hu₂, nq₂, hf₂⟩ := c₂
  simp only at hA hΩ hnabla hxi htheta hq hqinv
  subst hA
  subst hΩ
  rw [heq_iff_eq] at hnabla hxi htheta
  subst hnabla
  subst hxi
  subst htheta
  subst hq
  subst hqinv
  -- `nabla_q` is forced by the formula from the (now shared) data;
  -- `q_unit` is proof-irrelevant.
  have hnq : nq₁ = nq₂ := hf₁.trans hf₂.symm
  subst hnq
  rfl

end QOU
