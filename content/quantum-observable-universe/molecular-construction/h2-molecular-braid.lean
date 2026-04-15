/-!
# H2Braid — Hydrogen molecule $H_2$ as a braid in $H_4(q)$

The hydrogen molecule $H_2$ is the molecular braid of two hydrogen
atoms sharing one electron pair, living in $H_4(q)$ with strand
ordering $[\mathfrak{p}_1, e_1, \mathfrak{p}_2, e_2]$.

LaTeX label: `def:h2-molecular-braid`

## References

- [manuscript] Ch 12 §3
-/

import Mathlib.Data.Nat.Basic

namespace QOU.Molecular

/-- The H2 molecular braid: two hydrogen atoms sharing one
    electron pair (single covalent bond) in H_4(q). -/
-- Ref: [manuscript] Ch 12 §3, def:h2-molecular-braid
structure H2Braid where
  /-- Number of strands: 2 protons + 2 electrons = 4. -/
  strand_count : ℕ := 4
  /-- Bond order: single bond (1 shared electron pair). -/
  bond_order : ℕ := 1
  /-- Number of attractive crossings from the bond: 2. -/
  bond_crossings : ℕ := 2 * bond_order

-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Molecular
