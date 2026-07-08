import QOU.Molecular.ShellCapacitySelfSquare

namespace QOU.Molecular

/--
The maximum number of bonding sites at shell level `n` is `2n^2`.
This is the open shell-capacity derivation: the photon-electron transfer matrix
is 2x2, so its n-th power fixes the shell energies (the Chebyshev/Rydberg ladder)
but supplies only a 2-fold degeneracy. The full count requires an SO(4)-type
accidental degeneracy bundling angular-momentum levels.
-/
theorem electron_shell_capacity_2n2 (n : ℕ) :
    (2 * n^2) = 2 * (Finset.range n).sum (fun ℓ => 2 * ℓ + 1) := by
  sorry

end QOU.Molecular
