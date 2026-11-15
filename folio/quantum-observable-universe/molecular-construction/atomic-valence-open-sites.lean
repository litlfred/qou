-- Ref: [leitner2026] Ch. 12, §atomic-valence-open-sites
-- Valence and lone pairs as open bonding sites

namespace QOU.Molecular

/-- The **valence** of an atom: the number of open bonding sites available
    for covalent bonds, `v(Z) = min(Z_val, 2·n_val² − Z_val)`, where `Z_val`
    is the number of valence electrons and `n_val` the outermost shell level. -/

def atomicValence (zVal nVal : Nat) : Nat :=
  min zVal (2 * nVal * nVal - zVal)

/-- Hydrogen (Z_val = 1, n_val = 1): valence 1. -/
theorem valence_hydrogen : atomicValence 1 1 = 1 := by
  unfold atomicValence; decide

/-- Carbon (Z_val = 4, n_val = 2): valence 4 — the half-filled L shell. -/
theorem valence_carbon : atomicValence 4 2 = 4 := by
  unfold atomicValence; decide

/-- Nitrogen (Z_val = 5, n_val = 2): valence 3 (plus one lone pair). -/
theorem valence_nitrogen : atomicValence 5 2 = 3 := by
  unfold atomicValence; decide

/-- Oxygen (Z_val = 6, n_val = 2): valence 2 (plus two lone pairs). -/
theorem valence_oxygen : atomicValence 6 2 = 2 := by
  unfold atomicValence; decide

/-- The valence never exceeds the count of valence electrons. -/
theorem valence_le_zVal (zVal nVal : Nat) : atomicValence zVal nVal ≤ zVal := by
  unfold atomicValence
  omega

end QOU.Molecular
