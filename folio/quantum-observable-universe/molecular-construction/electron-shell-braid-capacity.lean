-- Ref: [leitner2026] Ch. 10, §electron-shell-braid-capacity
-- Electron shell as braid bonding capacity

namespace QOU.Molecular

/-- An **electron shell** at level n has:
    - Maximum capacity: 2n² electrons
    - Bonding capacity: number of open sites available for covalent bonds
    - Valence: determines which electrons participate in bonding vs lone pairs -/

structure ElectronShell where
  /-- Shell level (1, 2, 3, ...). -/
  level : Nat
  level_pos : 0 < level
  /-- Maximum electron capacity = 2n². -/
  capacity : Nat := 2 * level * level
  /-- Number of electrons currently in this shell. -/
  occupancy : Nat
  occupancy_le : occupancy ≤ 2 * level * level

/-- Shell 1 (K shell) holds at most 2 electrons. -/
theorem shell1_capacity : 2 * 1 * 1 = 2 := by decide

/-- Shell 2 (L shell) holds at most 8 electrons. -/
theorem shell2_capacity : 2 * 2 * 2 = 8 := by decide

/-- Shell 3 (M shell) holds at most 18 electrons. -/
theorem shell3_capacity : 2 * 3 * 3 = 18 := by decide

end QOU.Molecular
