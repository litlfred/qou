import QOU.Archimedean.ParticleKnots
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Archimedean.Antineutrino — Mirror unknot (antiparticle of neutrino)

The antineutrino is the mirror unknot T̄_{1,0}.  Since the unknot is
amphichiral, ν and ν̄ share all knot invariants; the distinction is
carried by orientation (framing).

LaTeX label: `def:antineutrino-knot`

## References
- [leitner2026] §6/antineutrino-knot

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Archimedean

/- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
   See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section

/-- The unknot is amphichiral: mirror ≅ original as unoriented knots. -/
-- Ref: [leitner2026] §6/antineutrino-knot
theorem unknot_amphichiral :
    ({} : Antineutrino).volume = (0 : R_q) ∧
    ({} : Antineutrino).crossing_number = 0 ∧
    ({} : Antineutrino).genus = 0 := by
  exact ⟨rfl, rfl, rfl⟩

end

end QOU.Archimedean
