/-!
# CO2Braid — Carbon dioxide $CO_2$ as a molecular braid

Carbon dioxide $CO_2$ is the molecular braid of one carbon atom
$C(6, 6)$ and two oxygen atoms $O_1(8, 8)$, $O_2(8, 8)$, with
two double bonds (O=C=O), living in $H_{66}(q)$.

LaTeX label: `def:co2-molecular-braid`

## References

- [manuscript] Ch 12 §5
-/

import Mathlib.Data.Nat.Basic

namespace QOU.Molecular

/-- The CO2 molecular braid: carbon + two oxygens with two double
    bonds (each 1 sigma + 1 pi pair) in H_66(q). -/
-- Ref: [manuscript] Ch 12 §5, def:co2-molecular-braid
structure CO2Braid where
  /-- Carbon strands: 18. -/
  carbon_strands : ℕ := 18
  /-- Oxygen strands (each): 24. -/
  oxygen_strands : ℕ := 24
  /-- Total strands: 18 + 24 + 24 = 66. -/
  total_strands : ℕ := carbon_strands + 2 * oxygen_strands
  /-- Number of bonds: 2 double bonds. -/
  num_bonds : ℕ := 2
  /-- Each bond has order 2 (double bond). -/
  bond_order : ℕ := 2

-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Molecular
