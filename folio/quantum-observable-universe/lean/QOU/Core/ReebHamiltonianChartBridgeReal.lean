import QOU.Core.ReebHamiltonianChartBridge

/-!
# Archimedean half of the Reeb ↔ Legendre Hamiltonian bridge

`worldlineEnergy` (`QOU.Core.CategoricalHamiltonianLegendre`) is defined over `ℝ` with a square
root, so its comparison with the generic `categoricalEnergy` sits after the
substrate → archimedean wall (AGENTS.md §7c), in this separate file.
-/

namespace QOU.Core.ReebHamiltonianChartBridge

open QOU.GravitySpacetime.ReebLengthTimeAndLightConeEntropy
open QOU.Core.CategoricalHamiltonianLegendre

/-- For `1 < q`, the Legendre worldline energy at rest equals the Reeb module's
`categoricalEnergy`: `worldlineEnergy m q 0 = categoricalEnergy q m`. -/
theorem worldlineEnergy_rest_eq_categoricalEnergy (m q : ℝ) (hq : 1 < q) :
    worldlineEnergy m q 0 = categoricalEnergy q m := by
  rw [(worldlineEnergy_rest m q hq).1, categoricalEnergy_eq_mul_lightconeSpeed_sq]

end QOU.Core.ReebHamiltonianChartBridge
