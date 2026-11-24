import QOU.Core.ReebLengthTimeAndLightConeEntropy
import QOU.Core.CategoricalHamiltonianLegendre

/-!
# Bridge: Reeb length/time charts ↔ the categorical Legendre Hamiltonian

Two modules in `QOU.Core` were written independently and each define the causal-cone speed,
the Planck tick and the rest energy `𝔈 = 𝔪 c_q²`:

* `QOU.Core.ReebLengthTimeAndLightConeEntropy` (bean `qou-slfm`): `causalSpeed`,
  `planckTick` (via `UnifiedClockScaleLayers`), `categoricalEnergy`;
* `QOU.Core.CategoricalHamiltonianLegendre` (commit `1e8db432857`): `lightconeSpeed`,
  `planckTickChart`, `hbarChart`, `hadronicScaleChart`, and the Legendre worldline energy
  `worldlineEnergy`.

This file proves that the two families agree, so the Reeb module's `categoricalEnergy` is the
rest value of the Legendre worldline Hamiltonian, and its share-scaled form is the hadronic
energy scale `E₀ = m_e / (q (q - 1))`. All statements are over a generic field `K`; the
comparison with the ℝ-valued Legendre worldline energy is in `ReebHamiltonianChartBridgeReal`.

Scope: these are identifications between existing definitions. They do not derive
`def:mass-energy`; the derivation in `CategoricalHamiltonianLegendre` remains conditional on the
zero-instance class `BraidBoostInertialEquivalence`.
-/

namespace QOU.Core.ReebHamiltonianChartBridge

open QOU.InformationTheory.UnifiedClockScaleLayers
open QOU.GravitySpacetime.ReebLengthTimeAndLightConeEntropy
open QOU.Core.CategoricalHamiltonianLegendre

section Generic

variable {K : Type*} [Field K]

/-- The Reeb module's causal speed `(q - 1)⁻¹` is the Hamiltonian module's `lightconeSpeed`. -/
theorem causalSpeed_eq_lightconeSpeed (q : K) : causalSpeed q = lightconeSpeed q := by
  unfold causalSpeed lightconeSpeed
  rw [one_div]

/-- The Reeb share `hbarQ` is the Hamiltonian module's `hbarChart`. -/
theorem hbarQ_eq_hbarChart (q : K) : hbarQ q = hbarChart q := rfl

/-- The clock-layer Planck tick `(hbarQ q)⁻¹` equals `planckTickChart q = q / (q - 1)`. -/
theorem planckTick_eq_planckTickChart {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    planckTick q = planckTickChart q := by
  rw [planckTick_eq_div hq0 hq1]
  rfl

/-- `categoricalEnergy q m = m · lightconeSpeed q ²`. -/
theorem categoricalEnergy_eq_mul_lightconeSpeed_sq (q m : K) :
    categoricalEnergy q m = m * lightconeSpeed q ^ 2 := by
  unfold categoricalEnergy
  rw [causalSpeed_eq_lightconeSpeed]

/-- Share-scaled categorical energy of the electron is the hadronic energy scale:
`categoricalEnergy q m_e · ℏ_q = m_e / (q (q - 1)) = E₀`. -/
theorem categoricalEnergy_mul_hbarQ_eq_hadronicScale {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1)
    (m_e : K) :
    categoricalEnergy q m_e * hbarQ q = hadronicScaleChart m_e q := by
  rw [categoricalEnergy_eq_mul_lightconeSpeed_sq, hbarQ_eq_hbarChart]
  exact (three_unit_chart_bridge m_e q hq0 hq1).2.1

end Generic

end QOU.Core.ReebHamiltonianChartBridge
