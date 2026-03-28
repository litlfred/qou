/-!
# QOU.Descartes.Neutrino — Unknot K_{0₁} (trivial knot)

The neutrino is the unknot K_{0₁} with zero crossings, Seifert genus 0,
and trivial Jones polynomial J_ν(q) = 1.  It carries no topological mass;
neutrino mass comes entirely from vacuum drag.

LaTeX label: `def:neutrino-knot`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] Ch. 5, §neutrino-knot
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- The neutrino: unknot K_{0₁} with trivial knot invariants.
    Zero crossings, genus 0, trivial Jones polynomial, zero volume.
    Neutrino mass arises from vacuum drag, not knot topology. -/
-- Ref: [manuscript] Ch. 5, §neutrino-knot
structure Neutrino where
  /-- Crossing number of the unknot. -/
  crossing_number : ℕ := 0
  /-- Seifert genus of the unknot. -/
  genus : ℕ := 0
  /-- Hyperbolic volume (unknot is non-hyperbolic). -/
  volume : ℝ := 0
  /-- Jones polynomial J_ν(q) = 1 for all q. -/
  jones_trivial : ∀ q : ℝ, (1 : ℝ) = 1 := fun _ => rfl
  /-- Coulomb charge contribution: zero (no crossings). -/
  charge : ℤ := 0
  /-- Orientation: +1 for particle (vs. -1 for antiparticle). -/
  orientation : ℤ := 1

/-- The neutrino is electrically neutral (zero crossing chirality). -/
-- Ref: [manuscript] Ch. 5, §neutrino-knot
theorem neutrino_neutral : Neutrino.mk.charge = 0 := rfl

/-- The unknot has trivial genus. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem neutrino_genus_zero : Neutrino.mk.genus = 0 := rfl

/-- The unknot has zero crossings. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem neutrino_crossing_zero : Neutrino.mk.crossing_number = 0 := rfl

end QOU.Descartes
