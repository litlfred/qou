/-!
# BenzeneBraid — Benzene $C_6H_6$ as a molecular braid

Benzene $C_6H_6$ is the molecular braid of six carbon atoms and
six hydrogen atoms, assembled iteratively from pre-computed atomic
braids, with delocalized $\pi$ electrons modeled as threading links
around the ring, living in $H_{120}(q)$.

LaTeX label: `def:benzene-molecular-braid`

## References

- [manuscript] Ch 12 §7
-/

import Mathlib.Data.Nat.Basic

namespace QOU.Molecular

/-- The benzene molecular braid: six carbons + six hydrogens with
    6 C-C sigma bonds, 6 C-H sigma bonds, and 6 delocalized pi
    electrons in H_120(q). -/
-- Ref: [manuscript] Ch 12 §7, def:benzene-molecular-braid
structure BenzeneBraid where
  /-- Carbon strands (each): A_C + Z_C = 12 + 6 = 18. -/
  carbon_strands : ℕ := 18
  /-- Hydrogen strands (each): A_H + Z_H = 1 + 1 = 2. -/
  hydrogen_strands : ℕ := 2
  /-- Number of carbon atoms. -/
  num_carbons : ℕ := 6
  /-- Number of hydrogen atoms. -/
  num_hydrogens : ℕ := 6
  /-- Total strands: 6 * 18 + 6 * 2 = 120. -/
  total_strands : ℕ := num_carbons * carbon_strands + num_hydrogens * hydrogen_strands
  /-- Number of C-C sigma bonds. -/
  num_cc_bonds : ℕ := 6
  /-- Number of C-H sigma bonds. -/
  num_ch_bonds : ℕ := 6
  /-- Number of delocalized pi electrons. -/
  num_pi_electrons : ℕ := 6

-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Molecular
