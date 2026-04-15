/-!
# CovalentBond — Covalent bond as shared electron trefoil

A covalent bond of order $k$ between atoms $i$ and $j$ is the
Hopf linking of $k$ electron trefoils across the two nuclei.
Each shared electron contributes two attractive $\sigma^{-1}$
crossings -- one to each nucleus.

LaTeX label: `def:covalent-bond-shared-trefoil`

## References

- [manuscript] Ch 12 §1
-/

import Mathlib.Algebra.Order.Ring.Defs

namespace QOU.Molecular

/-- A covalent bond of order k between two atoms, representing
    k shared electron trefoils Hopf-linked across both nuclei. -/
-- Ref: [manuscript] Ch 12 §1, def:covalent-bond-shared-trefoil
structure CovalentBond where
  /-- Index of the first atom. -/
  atom_i : ℕ
  /-- Index of the second atom. -/
  atom_j : ℕ
  /-- Bond order (number of shared electron pairs). -/
  order : ℕ
  /-- Each shared electron contributes 2 attractive crossings. -/
  crossing_count : ℕ := 2 * order

-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Molecular
