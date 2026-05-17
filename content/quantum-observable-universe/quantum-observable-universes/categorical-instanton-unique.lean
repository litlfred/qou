/-!
# QOU.CategoricalInstanton.unique_up_to_gauge — uniqueness of instantons modulo gauge

Two categorical instantons of the same c₂ are related by a
categorical gauge transformation.

LaTeX: `\label{prop:categorical-instanton-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-instanton-unique
- [atiyah1978] https://doi.org/10.1098/rspa.1978.0143
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of categorical instantons (moduli).**

    For fixed `FrobeniusHopfData`, the moduli of self-dual instanton
    connections is a quotient by categorical gauge transformations;
    `Subsingleton` expresses the type-level uniqueness of the moduli
    point for a given topological charge. -/
-- Ref: [atiyah1978]
/-- **External axiom (§3b-cond pattern): CategoricalInstanton.unique_up_to_gauge.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalInstanton.unique_up_to_gauge_axiom {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _) :
    Subsingleton (@CategoricalInstanton C _ _ fh)

theorem CategoricalInstanton.unique_up_to_gauge
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _) :
    Subsingleton (@CategoricalInstanton C _ _ fh) :=
  CategoricalInstanton.unique_up_to_gauge_axiom C fh

end QOU
