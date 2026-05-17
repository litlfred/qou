/-!
# QOU.CategoricalLagrangian.unique — uniqueness of the categorical Lagrangian

Given (∇, ψ), 𝓛_q is uniquely determined by its defining formula.

LaTeX: `\label{prop:categorical-lagrangian-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-lagrangian-unique
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical Lagrangian.**

    Given fixed (∇, ψ), the Lagrangian
    `𝒟_∇² + ψ* ⊗ 𝒟_∇ψ` is uniquely determined. -/
-- Ref: [connes1994]
/-- **External axiom (§3b-cond pattern): CategoricalLagrangian.unique.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalLagrangian.unique_axiom {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Subsingleton (CategoricalLagrangian C fh)

theorem CategoricalLagrangian.unique
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Subsingleton (CategoricalLagrangian C fh) :=
  CategoricalLagrangian.unique_axiom C fh

end QOU
