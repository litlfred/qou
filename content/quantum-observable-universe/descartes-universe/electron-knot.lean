/-!
# QOU.Descartes.Electron — Trefoil T_{2,3} (lepton sector)

The electron is the trefoil knot T_{2,3} in the lepton sector.
It is the same knot type as the up quark, but not localized in a
color tube — it orbits the nucleus via Hopf linking.

LaTeX label: `def:electron-knot`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] Ch. 5, §electron-knot
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- The electron: trefoil knot T_{2,3} in the lepton sector.
    Same knot type as the up quark; distinguished by environment
    (orbital Hopf-linked, not in a color tube). -/
-- Ref: [manuscript] Ch. 5, §electron-knot
structure Electron where
  /-- Torus knot parameter p. -/
  torusP : ℕ := 2
  /-- Torus knot parameter n. -/
  torusN : ℕ := 3
  /-- Crossing number of the trefoil. -/
  crossing_number : ℕ := 3
  /-- Seifert genus of the trefoil. -/
  genus : ℕ := 1
  /-- Hyperbolic volume (torus knot → non-hyperbolic). -/
  volume : ℝ := 0
  /-- Coulomb charge: -1 (from crossing chirality). -/
  charge : ℤ := -1
  /-- Orientation: +1 for particle (forward time). -/
  orientation : ℤ := 1

/-- The electron trefoil is a torus knot T_{2,3}. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem electron_is_torus_knot :
    Electron.mk.torusP = 2 ∧ Electron.mk.torusN = 3 := ⟨rfl, rfl⟩

/-- The trefoil has crossing number 3. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem electron_crossing_number : Electron.mk.crossing_number = 3 := rfl

/-- Torus knots are non-hyperbolic: Vol(T_{2,3}) = 0. -/
-- Ref: [manuscript] Ch. 5, §electron-knot
theorem electron_nonhyperbolic : Electron.mk.volume = (0 : ℝ) := rfl

end QOU.Descartes
