/-!
# QOU.CategoricalProton.unique_up_to_isotopy — uniqueness of the categorical proton

𝔭 unique up to Hecke NF in H₃(q), with S₃-symmetry on color tubes.

LaTeX: `\label{prop:categorical-proton-unique}`

## References

- [manuscript] §6-descartes-universe/categorical-proton-unique
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical proton up to braid isotopy.**

    Two `CategoricalProton` terms with the same Hecke NF in H₃(q)
    (and the same S₃-color assignment) coincide. -/
-- Ref: [jones1987]
theorem CategoricalProton.unique_up_to_isotopy : Subsingleton CategoricalProton := by
  -- Hecke NF is unique; S₃ color permutations act by inner autos.
  -- Ref: [jones1987]
  sorry

end QOU
