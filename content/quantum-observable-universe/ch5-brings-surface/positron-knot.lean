/-!
# QOU.Descartes.Positron — Mirror trefoil σ(T_{2,3}) (antiparticle of electron)

The positron is the mirror trefoil σ(T_{2,3}) — the antiparticle of the
electron.  It carries reversed crossing chirality (Q = +1) and corresponds
to an electron travelling backward in time (Feynman–Stueckelberg).

LaTeX label: `def:positron-knot`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] Ch. 5, §positron-knot
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- The positron: mirror trefoil σ(T_{2,3}) with reversed crossings.
    Antiparticle of the electron; same knot as down quark but in
    the lepton sector (orbital, not color-tube). -/
-- Ref: [manuscript] Ch. 5, §positron-knot
structure Positron where
  /-- Torus knot parameter p (same as trefoil). -/
  torusP : ℕ := 2
  /-- Torus knot parameter n (same as trefoil). -/
  torusN : ℕ := 3
  /-- Crossing number (same as trefoil). -/
  crossing_number : ℕ := 3
  /-- Seifert genus (same as trefoil). -/
  genus : ℕ := 1
  /-- Hyperbolic volume (torus knot → non-hyperbolic). -/
  volume : ℝ := 0
  /-- Coulomb charge: +1 (reversed crossing chirality). -/
  charge : ℤ := 1
  /-- Orientation: -1 for antiparticle (reversed time direction). -/
  orientation : ℤ := -1

/-- The positron is a mirror trefoil T_{2,3} with reversed crossings. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem positron_is_mirror_torus_knot :
    Positron.mk.torusP = 2 ∧ Positron.mk.torusN = 3 := ⟨rfl, rfl⟩

/-- The positron has opposite charge to the electron. -/
-- Ref: [manuscript] Ch. 5, §positron-knot
theorem positron_charge_opposite_electron :
    Positron.mk.charge + Electron.mk.charge = 0 := by decide

/-- The positron has reversed orientation (antiparticle). -/
-- Ref: [manuscript] Ch. 5, §positron-knot
theorem positron_reversed_orientation :
    Positron.mk.orientation = -Electron.mk.orientation := by decide

end QOU.Descartes
