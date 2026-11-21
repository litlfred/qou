import QOU.Archimedean.ParticleKnots
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
- [leitner2026] Ch. 5, §down-quark

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Archimedean

/- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
   See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
/-- The down quark is an unknot (same underlying knot as neutrino). -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem down_quark_is_unknot :
    ({} : DownQuark).crossing_number = ({} : Neutrino).crossing_number ∧
    ({} : DownQuark).genus = ({} : Neutrino).genus := ⟨rfl, rfl⟩

/-- The down quark has negative crossing orientation. -/
-- Ref: [leitner2026] Ch. 5, §down-quark
theorem down_quark_negative_orientation :
    ({} : DownQuark).crossing_orientation = -1 := rfl

/-- Up and down quarks have opposite crossing orientations. -/
-- Ref: [leitner2026] Ch. 5, §down-quark
theorem quark_crossing_asymmetry :
    ({} : DownQuark).crossing_orientation = -({} : UpQuark).crossing_orientation := by
  decide

/-- The down quark is color-confined. -/
-- Ref: [leitner2026] Ch. 5, §down-quark
theorem down_quark_confined : ({} : DownQuark).confined = true := rfl

end

end QOU.Archimedean
