import QOU.Shared.SobolevHkRegularity


/-!
# QOU.FluidDynamics.acoustic_horizon_conditions

**Canonical declaration** for content block
[`prop:acoustic-horizon-conditions`](../../../quantum-observable-universe/fluid-dynamics/acoustic-horizon-conditions.md): *Acoustic horizon formation and gravitational emergence*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.FluidDynamics


/-- Abstract context for the `acoustic_horizon_conditions` claim — manuscript-themed
    typed fields below; `holds` carries the residual `Prop` claim. -/
class AcousticHorizonConditionsContext extends QOU.Shared.SobolevHkRegularityContext where
  /-- Mach number `ℳ = |v|/c_s` on the brane. -/
  mach : ℝ
  /-- Squared gradient norm of `ℳ²` on the horizon. -/
  grad_mach_sq_norm : ℝ
  /-- Null-energy contraction `T_{μν} k^μ k^ν` for null `k`. -/
  null_energy : ℝ
  /-- Acoustic horizon formed. -/
  acoustic_horizon_formed : Prop
  /-- Hypothesis that the acoustic horizon forms. -/
  horizon_active : acoustic_horizon_formed
  /-- (i) Transonic flow: Mach number is 1 on the horizon. -/
  impl_transonic : acoustic_horizon_formed → mach = 1
  /-- (ii) Non-degeneracy: Mach gradient is non-zero. -/
  impl_non_degeneracy : acoustic_horizon_formed → 0 < grad_mach_sq_norm
  /-- (iii) Energy condition: Null-energy contraction is non-negative. -/
  impl_energy_condition : acoustic_horizon_formed → 0 ≤ null_energy

/-- **Content statement** (from manuscript):

The [acoustic metric](#rem:madelung-fluid) $g_{\mathrm{ac}}$ admits
horizons wherever $|v| = c_s$.

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/fluid-dynamics/acoustic-horizon-conditions.ts
theorem acoustic_horizon_conditions [ctx : AcousticHorizonConditionsContext] :
    ctx.mach = 1 ∧ 0 < ctx.grad_mach_sq_norm ∧ 0 ≤ ctx.null_energy :=
  ⟨ctx.impl_transonic ctx.horizon_active,
   ctx.impl_non_degeneracy ctx.horizon_active,
   ctx.impl_energy_condition ctx.horizon_active⟩


end QOU.FluidDynamics
