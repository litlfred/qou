/-!
# COBraid — Carbon monoxide $CO$ as a molecular braid

Carbon monoxide $CO$ is the molecular braid of a carbon atom
$C(6, 6)$ and an oxygen atom $O(8, 8)$ sharing three electron
pairs (triple bond), living in $H_{42}(q)$.

LaTeX label: `def:co-molecular-braid`

## References

- [manuscript] Ch 12 §4
-/

import Mathlib.Data.Nat.Basic

namespace QOU.Molecular

/-- The CO molecular braid: carbon + oxygen with a triple bond
    (1 sigma + 2 pi shared pairs) in H_42(q). -/
-- Ref: [manuscript] Ch 12 §4, def:co-molecular-braid
structure COBraid where
  /-- Carbon strands: A_C + Z_C = 12 + 6 = 18. -/
  carbon_strands : ℕ := 18
  /-- Oxygen strands: A_O + Z_O = 16 + 8 = 24. -/
  oxygen_strands : ℕ := 24
  /-- Total strands: 18 + 24 = 42. -/
  total_strands : ℕ := carbon_strands + oxygen_strands
  /-- Bond order: triple bond (3 shared electron pairs). -/
  bond_order : ℕ := 3

-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Molecular
