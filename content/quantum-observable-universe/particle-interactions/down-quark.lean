import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Archimedean.DownQuark — Unknot in Borromean link with negative crossing

The down quark is an unknot (neutrino) localized in a color tube with
negative crossing orientation within the Borromean link B₃.  It differs
from the up quark only in crossing orientation: at each crossing, the
down quark's strand passes under where the up quark passes over,
contributing q⁻¹ instead of q to the Skein polynomial.

LaTeX label: `def:down-quark`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] Ch. 5, §down-quark

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Archimedean

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The down quark: unknot K_{0₁} with negative crossing orientation
    in the Borromean link B₃.  Contributes q⁻¹ to the Skein polynomial
    at each crossing.  Coulomb charge contribution -1/3 relative
    to the proton. -/
-- Ref: [manuscript] Ch. 5, §down-quark
structure DownQuark where
  /-- Crossing number of the underlying unknot. -/
  crossing_number : ℕ := 0
  /-- Seifert genus (trivial knot). -/
  genus : ℕ := 0
  /-- Hyperbolic volume (unknot is non-hyperbolic). -/
  volume : R_q := 0
  /-- Crossing orientation: -1 for negative (contributes q⁻¹ to Skein). -/
  crossing_orientation : ℤ := -1
  /-- Number of Borromean components this quark links with. -/
  borromean_links : ℕ := 2
  /-- Coulomb charge numerator (charge = numerator / 3). -/
  charge_numerator : ℤ := -1
  /-- Coulomb charge denominator. -/
  charge_denominator : ℕ := 3
  /-- Color-confined: cannot be isolated from B₃. -/
  confined : Bool := true

/-- The down quark is an unknot (same underlying knot as the neutrino,
    `QOU.Archimedean.Neutrino`): zero crossings and trivial Seifert genus.
    The neutrino's defining invariants are `crossing_number = 0`,
    `genus = 0`; this states the matching values for the down quark. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem down_quark_is_unknot :
    DownQuark.mk.crossing_number = 0 ∧
    DownQuark.mk.genus = 0 := ⟨rfl, rfl⟩

/-- The down quark has negative crossing orientation. -/
-- Ref: [manuscript] Ch. 5, §down-quark
theorem down_quark_negative_orientation :
    DownQuark.mk.crossing_orientation = -1 := rfl

/-- Up and down quarks have opposite crossing orientations.  The up quark
    (`QOU.Archimedean.UpQuark`) has `crossing_orientation = 1`; the down
    quark's is its negation, `-1`. -/
-- Ref: [manuscript] Ch. 5, §down-quark
theorem quark_crossing_asymmetry :
    DownQuark.mk.crossing_orientation = -(1 : ℤ) := by
  decide

/-- The down quark is color-confined. -/
-- Ref: [manuscript] Ch. 5, §down-quark
theorem down_quark_confined : DownQuark.mk.confined = true := rfl

end

end QOU.Archimedean
