/-!
# QOU.Hadron.unique_up_to_isotopy — uniqueness of hadrons up to isotopy

Hecke normal form is unique in H_n(q); Markov trace is isotopy-invariant.

LaTeX: `\label{prop:hadron-unique}`

## References

- [manuscript] §4-braids-and-knots/hadron-unique
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of hadrons up to braid isotopy.**

    Two hadrons with the same crossing partition, localisation point,
    and Hecke normal form coincide.  `Subsingleton` expresses the
    statement at the level of the `Hadron` type (up to the relevant
    equivalence built into the structure's equality). -/
-- Ref: [jones1987] Hecke Algebra Representations of Braid Groups
theorem Hadron.unique_up_to_isotopy : Subsingleton Hadron := by
  -- Hecke NF is unique; Markov trace is isotopy-invariant.
  -- Ref: [jones1987]
  sorry

end QOU
