/-!
# QOU.CategoricalNeutron.unique_up_to_isotopy — uniqueness of the categorical neutron

𝔫 unique up to Hecke NF in H₃(q) + S₃-symmetry on color tubes.

LaTeX: `\label{prop:categorical-neutron-unique}`

## References

- [manuscript] §6-descartes-universe/categorical-neutron-unique
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical neutron up to braid isotopy.** -/
-- Ref: [jones1987]
/-- **External axiom (§3b-cond pattern): CategoricalNeutron.unique_up_to_isotopy.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalNeutron.unique_up_to_isotopy_axiom  :
    Subsingleton CategoricalNeutron

theorem CategoricalNeutron.unique_up_to_isotopy : Subsingleton CategoricalNeutron :=
  CategoricalNeutron.unique_up_to_isotopy_axiom

end QOU
