import QOU.Observations.CODATAChain
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.CODATAChain — `Real.sqrt` restatement of the substrate chain

Companion of `QOU.Observations.CODATAChain` inside the transcendental
boundary (bean `qou-dk7p`). The chain itself, and `end_to_end`, stay in the
main module; only the repackaging that names `Real.sqrt` lives here.
-/

open QOU.Torsion QOU.MassDerivation QOU.KnotRegistry
open QOU.Calculations QOU.HadronicMass

namespace QOU.CODATAChain

/-- **Full chain theorem**: Given an `ArchimedeanMassFormula` for
    the muon (knot volume = Vol(4₁)), and the CODATA mass ratio as
    input, the substrate parameter is determined to be q ≈ 1.1097.

    This repackages `Calculations.full_derivation_chain` to show
    it is a consequence of the `ArchimedeanMassFormula`. -/
theorem substrate_from_archimedean_formula :
    let vol := figureEightEntry.volume.value
    let ratio := experimental_mu_e_ratio
    let hq2 := vol / ratio
    let hq := Real.sqrt hq2
    let q := 1 / (1 - hq)
    |q - substrate_q| < 0.001 :=
  Calculations.full_derivation_chain

end QOU.CODATAChain
