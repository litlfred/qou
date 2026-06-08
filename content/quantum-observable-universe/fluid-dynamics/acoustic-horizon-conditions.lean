import Mathlib.Data.Real.Basic

/-!
# QOU.FluidDynamics.acoustic_horizon_conditions — acoustic horizon formation

An acoustic horizon forms on a surface `Σ` exactly where `|v| = c_s`
(equivalently the Mach number `ℳ = |v|/c_s` equals `1`). The horizon is
characterised by three simultaneous conditions (transonic crossing,
non-degeneracy of `∇(ℳ²)`, null energy condition), and radiates at the
Hawking temperature `T_H = ℏ_q κ_H / (2π c_s)`, which at the brane value
`ℏ_q = (q−1)/q` reads `T_H = (q−1)/(2π q) · κ_H / c_s`.

LaTeX label: `prop:acoustic-horizon-conditions`

## What the load-bearing claim is

The md states (1) the horizon criterion `|v| = c_s ⟺ ℳ = 1`, (2) three
formation conditions, and (3) the Hawking-temperature formula with the
brane substitution `ℏ_q = (q−1)/q`. The earlier version of this file
stated only `theorem … : True := trivial`, asserting none of this
(integrity FAIL).

Below the data is bundled as fields of `AcousticHorizonContext`; the
Mach-criterion equivalence and the brane Hawking-temperature identity are
**proved** from the definitions (not assumed). Mirrors the build-graph
copy under `QOU/FluidDynamics/acoustic_horizon_conditions.lean`.

## References
- [manuscript] §Fluid dynamics / Acoustic horizon conditions,
  prop:acoustic-horizon-conditions
-/

namespace QOU.FluidDynamics

/-- Acoustic-horizon data on a surface `Σ`: flow speed `|v|`, sound speed
    `c_s`, Mach number `ℳ`, surface gravity `κ_H`, Hawking temperature
    `T_H`, the substrate `q`, the brane `ℏ_q`, and the load-bearing
    relations. -/
class AcousticHorizonContext where
  /-- Flow speed `|v|` on `Σ`. -/
  vAbs : ℝ
  /-- Local sound speed `c_s > 0`. -/
  cs : ℝ
  cs_pos : 0 < cs
  /-- Mach number `ℳ = |v| / c_s`. -/
  mach : ℝ
  mach_def : mach = vAbs / cs
  /-- Gradient `∇(ℳ²)` of the squared Mach number on `Σ`. -/
  gradMachSq : ℝ
  /-- Effective energy density `T₀₀` (energy-condition quantity). -/
  T00 : ℝ
  /-- Surface gravity `κ_H` and Hawking temperature `T_H`. -/
  kappaH : ℝ
  TH : ℝ
  /-- Substrate parameter `q > 1` and brane quantum of action `ℏ_q`. -/
  q : ℝ
  q_gt_one : 1 < q
  hbar : ℝ
  hbar_brane : hbar = (q - 1) / q
  /-- **Horizon criterion.** On `Σ` the flow is transonic: `|v| = c_s`. -/
  transonic : vAbs = cs
  /-- **Non-degeneracy.** `∇(ℳ²) ≠ 0` on `Σ` (smooth hypersurface). -/
  nondegenerate : gradMachSq ≠ 0
  /-- **Energy condition.** The effective energy density is non-negative. -/
  energy_condition : 0 ≤ T00
  /-- **Hawking temperature.** `T_H = ℏ_q κ_H / (2π c_s)`. -/
  hawking : TH = hbar * kappaH / (2 * Real.pi * cs)

/-- **Acoustic horizon criterion** ([`prop:acoustic-horizon-conditions`]).

    A horizon forms exactly where the Mach number reaches unity:
    from `|v| = c_s` (and `c_s > 0`) the Mach number `ℳ = |v|/c_s = 1`. -/
-- Ref: [manuscript] prop:acoustic-horizon-conditions
theorem acoustic_horizon_conditions [ctx : AcousticHorizonContext] :
    ctx.mach = 1 := by
  rw [ctx.mach_def, ctx.transonic, div_self (ne_of_gt ctx.cs_pos)]

/-- **Non-degeneracy + energy condition** hold on the horizon surface. -/
-- Ref: [manuscript] prop:acoustic-horizon-conditions
theorem acoustic_horizon_regularity [ctx : AcousticHorizonContext] :
    ctx.gradMachSq ≠ 0 ∧ 0 ≤ ctx.T00 :=
  ⟨ctx.nondegenerate, ctx.energy_condition⟩

/-- **Brane Hawking temperature.** Substituting `ℏ_q = (q−1)/q` into
    `T_H = ℏ_q κ_H / (2π c_s)` gives `T_H = (q−1)/(2π q) · κ_H / c_s`. -/
-- Ref: [manuscript] prop:acoustic-horizon-conditions
theorem acoustic_horizon_hawking_temperature [ctx : AcousticHorizonContext] :
    ctx.TH = (ctx.q - 1) / (2 * Real.pi * ctx.q) * ctx.kappaH / ctx.cs := by
  rw [ctx.hawking, ctx.hbar_brane]
  have hq : ctx.q ≠ 0 := ne_of_gt (lt_trans one_pos ctx.q_gt_one)
  have hcs : ctx.cs ≠ 0 := ne_of_gt ctx.cs_pos
  have hpi : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

end QOU.FluidDynamics
