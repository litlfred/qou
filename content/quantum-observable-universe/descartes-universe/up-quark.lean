/-!
# QOU.Descartes.UpQuark — Unknot in Borromean link with positive crossing

The up quark is an unknot (neutrino) localized in a color tube of the
Bring surface with positive crossing orientation within the Borromean
link B₃.  It is not a distinct knot type — it is the unknot K_{0₁}
distinguished by its environment (color-tube, Borromean-linked).

LaTeX label: `def:up-quark`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] Ch. 5, §up-quark
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- The up quark: unknot K_{0₁} with positive crossing orientation
    in the Borromean link B₃.  Threaded through a color tube;
    contributes +q to the Skein polynomial at each crossing.
    Coulomb charge contribution +2/3 relative to the proton. -/
-- Ref: [manuscript] Ch. 5, §up-quark
structure UpQuark where
  /-- Crossing number of the underlying unknot. -/
  crossing_number : ℕ := 0
  /-- Seifert genus (trivial knot). -/
  genus : ℕ := 0
  /-- Hyperbolic volume (unknot is non-hyperbolic). -/
  volume : ℝ := 0
  /-- Crossing orientation: +1 for positive (contributes +q to Skein). -/
  crossing_orientation : ℤ := 1
  /-- Number of Borromean components this quark links with. -/
  borromean_links : ℕ := 2
  /-- Coulomb charge numerator (charge = numerator / 3). -/
  charge_numerator : ℤ := 2
  /-- Coulomb charge denominator. -/
  charge_denominator : ℕ := 3
  /-- Color-confined: cannot be isolated from B₃. -/
  confined : Bool := true

/-- The up quark is an unknot (same underlying knot as neutrino). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem up_quark_is_unknot :
    UpQuark.mk.crossing_number = Neutrino.mk.crossing_number ∧
    UpQuark.mk.genus = Neutrino.mk.genus := ⟨rfl, rfl⟩

/-- The up quark has positive crossing orientation. -/
-- Ref: [manuscript] Ch. 5, §up-quark
theorem up_quark_positive_orientation :
    UpQuark.mk.crossing_orientation = 1 := rfl

/-- The up quark is color-confined. -/
-- Ref: [manuscript] Ch. 5, §up-quark
theorem up_quark_confined : UpQuark.mk.confined = true := rfl

end QOU.Descartes
