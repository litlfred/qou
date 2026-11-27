import QOU.BraidsAndKnots.HiggsCategoricalMassFormula

/-!
# `catalanG = Cl₂(π/2)` — companion of `HiggsCategoricalMassFormula`

The one statement of `QOU.BraidsAndKnots.HiggsCategoricalMassFormula` that names
`Real.pi`, kept inside the transcendental boundary (bean `qou-dk7p`).
-/

namespace QOU.BraidKnot

/-- `catalanG` is definitionally `Cl_2 (π / 2)` (no decimal truncation). -/
theorem catalanG_eq_cl2_pi_div_two :
    catalanG = QOU.Archimedean.Cl_2 (Real.pi / 2) := rfl

end QOU.BraidKnot
