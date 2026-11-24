import Mathlib.Data.Real.Basic

/-!
# QOU.Shared.SobolevHkRegularity — shared context for FluidDynamics Sobolev claims

A *Sobolev-`H^k` regularity claim* is any proposition that bundles:
- A substrate parameter `q : ℝ` with `q > 1`
- A `q`-deformed kinematic viscosity `ν_q = ½(1 − q⁻¹) > 0`
- A solution `v : ℝ → Ω¹(A)` of the `q`-deformed Navier–Stokes equation
- Sobolev `H^k` norms `||v||_{H^k}` for various `k`

Per `local/lean-substantive-pass`, ~5 FluidDynamics blocks share
this shape (q-NS well-posedness / energy inequality / spectral
decay / Leray profile / vorticity lower bound).

**Usage**:

```lean
class MyFluidClaim extends QOU.Shared.SobolevHkRegularityContext where
  claim_smoothness : ∀ t ≥ 0, ContinuousV t  -- block-specific
```

-- Ref: [leitner2026] fluid-dynamics/q-ns-wellposedness.md (shared)
-/

namespace QOU.Shared

/-- Shared context for any FluidDynamics block whose claim involves
    Sobolev-`H^k` regularity of a `q`-deformed Navier–Stokes
    solution. -/
class SobolevHkRegularityContext where
  /-- The substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- `q > 1` (QOU regime). -/
  q_gt_one : 1 < q
  /-- The kinematic viscosity `ν_q = ½(1 − q⁻¹) > 0`. -/
  ν_q : ℝ
  /-- `ν_q = ½(1 − q⁻¹)`. -/
  ν_q_eq : ν_q = (1 - q⁻¹) / 2
  /-- `ν_q > 0`. -/
  ν_q_pos : 0 < ν_q
  /-- The Sobolev `H^k` regularity index `k`. -/
  k : ℕ
  /-- The `H^k`-norm of the solution at time `t`. -/
  H_k_norm : ℝ → ℝ

end QOU.Shared
