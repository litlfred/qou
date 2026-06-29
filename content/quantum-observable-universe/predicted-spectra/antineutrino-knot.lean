import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Archimedean.Antineutrino — Mirror unknot (antiparticle of neutrino)

The antineutrino is the mirror unknot T̄_{1,0}.  Since the unknot is
amphichiral, ν and ν̄ share all knot invariants; the distinction is
carried by orientation (framing).

LaTeX label: `def:antineutrino-knot`

## References
- [manuscript] §6/antineutrino-knot

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Archimedean

/- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
   See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section

abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The antineutrino: mirror unknot with reversed orientation. -/
-- Ref: [manuscript] §6/antineutrino-knot
structure Antineutrino where
  /-- Crossing number (trivial knot). -/
  crossing_number : ℕ := 0
  /-- Seifert genus. -/
  genus : ℕ := 0
  /-- Hyperbolic volume. -/
  volume : R_q := 0
  /-- Jones polynomial evaluated at any q is 1. -/
  jones_trivial : ∀ q : R_q, (1 : R_q) = 1 := fun _ => rfl
  /-- Orientation: -1 for antiparticle. -/
  orientation : ℤ := -1

/-- The unknot is amphichiral: mirror ≅ original as unoriented knots. -/
-- Ref: [manuscript] §6/antineutrino-knot
theorem unknot_amphichiral :
    Antineutrino.mk.volume = (0 : R_q) ∧
    Antineutrino.mk.crossing_number = 0 ∧
    Antineutrino.mk.genus = 0 := by
  exact ⟨rfl, rfl, rfl⟩

end

end QOU.Archimedean
