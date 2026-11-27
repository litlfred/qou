import QOU.Transcendental.BraidKnotOctonion.FigureEightVolume

/-!
# QOU.Transcendental.BraidKnotOctonion.FigureEightKashaevHabiroReading

Bean `qou-28qh`, phase 3. Since phase 3 step 2, `QOU.Knot.FigureEightVolume.kashaev`
is *defined* as the archimedean reading of the Habiro element
`QCalculus.HabiroSeries.figureEight`, and the comparison lemmas live next to that
definition. This file keeps the names it published in step 1 (#9592) as thin
aliases, so citers do not break.

No empirical value enters this file.
-/

namespace QOU.Transcendental.FigureEightKashaevHabiroReading

open Polynomial QCalculus.HabiroSeries QOU.Knot.FigureEightVolume

/-- `ζ_N = exp(2πi/N)` (alias of `kashaevRoot`). -/
noncomputable abbrev zeta (N : ℕ) : ℂ := kashaevRoot N

theorem aeval_zeta_cyclotomic {N : ℕ} (hN : N ≠ 0) :
    aeval (zeta N) (cyclotomic N ℤ) = 0 :=
  aeval_kashaevRoot_cyclotomic hN

/-- One factor: `(1 - ζ^{-j})(1 - ζ^j) = 2 - 2 cos(2πj/N)`. -/
theorem factor_eq (N j : ℕ) :
    (1 - (zeta N)⁻¹ ^ j) * (1 - zeta N ^ j) =
      ((2 - 2 * Real.cos (2 * Real.pi * j / N) : ℝ) : ℂ) :=
  kashaev_factor_eq N j

/-- **The archimedean reading.** -/
theorem kashaev_eq_evalRoot_figureEight {N : ℕ} (hN : N ≠ 0) :
    ((kashaev N : ℝ) : ℂ) =
      evalRoot hN (zeta N) (aeval_zeta_cyclotomic hN) (figureEight (R := ℤ)) :=
  kashaev_eq_evalRoot hN

end QOU.Transcendental.FigureEightKashaevHabiroReading
