/-!
# ElectronShellCapacity — Electron shell as braid bonding capacity

In the atomic braid, each electron trefoil $T_{2,3}$ occupies a
bonding site. The maximum number of bonding sites at shell level
$n$ is $2n^2$. The valence is the number of open bonding sites
available for covalent bonds.

LaTeX label: `def:electron-shell-braid-capacity`

## References

- [manuscript] Ch 12 §2
-/

import Mathlib.Data.Nat.Basic

namespace QOU.Molecular

/-- Shell capacity at level n is 2n^2. -/
-- Ref: [manuscript] Ch 12 §2, def:electron-shell-braid-capacity
def shell_capacity (n : ℕ) : ℕ := 2 * n ^ 2

/-- The electron shell structure of an atom, determining
    bonding capacity and valence from the braid structure. -/
-- Ref: [manuscript] Ch 12 §2
structure ElectronShellCapacity where
  /-- Atomic number (number of electrons). -/
  Z : ℕ
  /-- Valence shell level. -/
  n_val : ℕ
  /-- Number of valence electrons. -/
  Z_val : ℕ
  /-- Valence: min(Z_val, 2*n_val^2 - Z_val). -/
  valence : ℕ := min Z_val (shell_capacity n_val - Z_val)

-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Molecular
