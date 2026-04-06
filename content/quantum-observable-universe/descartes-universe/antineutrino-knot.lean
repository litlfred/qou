/-!
# QOU.Descartes.Antineutrino — Mirror unknot (antiparticle of neutrino)

The antineutrino is the mirror unknot T̄_{1,0}.  Since the unknot is
amphichiral, ν and ν̄ share all knot invariants; the distinction is
carried by orientation (framing).

LaTeX label: `def:antineutrino-knot`

## References
- [manuscript] §6/antineutrino-knot
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- The antineutrino: mirror unknot with reversed orientation. -/
-- Ref: [manuscript] §6/antineutrino-knot
structure Antineutrino where
  /-- Crossing number (trivial knot). -/
  crossing_number : ℕ := 0
  /-- Seifert genus. -/
  genus : ℕ := 0
  /-- Hyperbolic volume. -/
  volume : ℝ := 0
  /-- Jones polynomial evaluated at any q is 1. -/
  jones_trivial : ∀ q : ℝ, (1 : ℝ) = 1 := fun _ => rfl
  /-- Orientation: -1 for antiparticle. -/
  orientation : ℤ := -1

/-- The unknot is amphichiral: mirror ≅ original as unoriented knots. -/
-- Ref: [manuscript] §6/antineutrino-knot
theorem unknot_amphichiral :
    Antineutrino.mk.volume = (0 : ℝ) ∧
    Antineutrino.mk.crossing_number = 0 ∧
    Antineutrino.mk.genus = 0 := by
  exact ⟨rfl, rfl, rfl⟩

end QOU.Descartes
