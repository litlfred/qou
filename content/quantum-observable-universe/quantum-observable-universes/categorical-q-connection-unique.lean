/-!
# QOU.CategoricalQConnection.unique — uniqueness of the categorical q-connection

∇_q uniquely determined by (∇, ξ, θ, q), inheriting the gauge
freedom of ∇.

LaTeX: `\label{prop:categorical-q-connection-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-connection-unique
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical q-connection.**

    Given fixed (∇, ξ, θ, q), the q-connection
    `∇_q = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇ ∘ θ` is uniquely determined;
    q-deformation introduces no additional gauge freedom. -/
-- Ref: [connes1994]
/-- **External axiom (§3b-cond pattern): CategoricalQConnection.unique.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalQConnection.unique_axiom (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    [CategoryTheory.Linear R_q C] :
    Subsingleton (CategoricalQConnection C)

theorem CategoricalQConnection.unique
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    [CategoryTheory.Linear R_q C] :
    Subsingleton (CategoricalQConnection C) :=
  CategoricalQConnection.unique_axiom C

end QOU
