import QOU.Core.ReebHamiltonianChartBridge
import QOU.Core.AffineCausalityCone

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

/-- The corpus worldline Lagrangian is the square root of the affine-causality cone form:
`L(v) = -m c_q √(coneForm c_q 1 v)`, with `coneForm c ω u = c² ω² - u²` the form fixed by the
cone's null points `±c_q` (`QOU.Core.AffineCausalityCone.quadratic_with_cone_roots`). -/
theorem worldlineLagrangian_eq_sqrt_coneForm (m q v : ℝ) :
    worldlineLagrangian m q v =
      -m * lightconeSpeed q *
        Real.sqrt (QOU.Core.AffineCausalityCone.coneForm (lightconeSpeed q) 1 v) := by
  unfold worldlineLagrangian QOU.Core.AffineCausalityCone.coneForm
  rw [one_pow, mul_one]

end QOU.Core.ReebHamiltonianChartBridge
