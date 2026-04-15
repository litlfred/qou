/-!
# CH4Braid — Methane $CH_4$ as a molecular braid

Methane $CH_4$ is the molecular braid of one carbon atom $C(6,6)$
and four hydrogen atoms, each sharing one electron pair (four single
bonds), living in $H_{26}(q)$.

LaTeX label: `def:ch4-molecular-braid`

## References

- [manuscript] Ch 12 §6
-/

import Mathlib.Data.Nat.Basic

namespace QOU.Molecular

/-- The CH4 molecular braid: one carbon + four hydrogens with four
    single bonds (one shared electron pair each) in H_26(q). -/
-- Ref: [manuscript] Ch 12 §6, def:ch4-molecular-braid
structure CH4Braid where
  /-- Carbon strands: A_C + Z_C = 12 + 6 = 18. -/
  carbon_strands : ℕ := 18
  /-- Hydrogen strands (each): A_H + Z_H = 1 + 1 = 2. -/
  hydrogen_strands : ℕ := 2
  /-- Number of hydrogen atoms. -/
  num_hydrogens : ℕ := 4
  /-- Total strands: 18 + 4 * 2 = 26. -/
  total_strands : ℕ := carbon_strands + num_hydrogens * hydrogen_strands
  /-- Bond order per C-H bond: single bond (1 shared electron pair). -/
  bond_order : ℕ := 1
  /-- Number of C-H bonds. -/
  num_bonds : ℕ := 4

-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Molecular
