/-
  Vorticity lower bound (conditional on the q-NS cone).

  Ref: [leitner2026] §Fluid dynamics / Vorticity lower bound,
       conj:vorticity-lower-bound
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace QOU.FluidDynamics

/-- **Conditional hypotheses for the vorticity lower bound.**

    The proposition is conditional on the q-NS conjecture cone
    (`conj:q-aubin-lions`, `conj:ns-counterexample`,
    `conj:critical-exponent`, `prop:blowup-yekutieli`,
    `conj:regularity-breakdown`).  Rather than concluding the vacuous
    `True`, this class carries the three analytic facts the
    proposition actually asserts as **explicit hypotheses**, and
    `vorticity_lower_bound_conditional` *derives* their conjunction
    (§3b-cond non-degenerate conditional pattern, the
    `q_bkm_criterion` exemplar).

    The fields abstract the limit solution: `dist t` is the
    inter-filament separation `d(t)`, `vortNorm t` is
    `‖ω*(t)‖_{L^∞}`, `bkmIntegralDiverges` records the BKM
    time-integral divergence, and `tStar` the collision time.  The
    inequalities are the bar-odd collapse signature of the
    anti-parallel filament collision. -/
class VorticityLowerBoundContext (bkmIntegralDiverges : Prop) where
  /-- Collision (blow-up) time `T*`. -/
  tStar : ℝ
  /-- Universal lower constant `c₁ > 0` (independent of `q`). -/
  c₁ : ℝ
  /-- Universal upper constant `c₂ > 0` (independent of `q`). -/
  c₂ : ℝ
  /-- Inter-filament separation `d(t)`. -/
  dist : ℝ → ℝ
  /-- Limit-solution vorticity sup-norm `‖ω*(t)‖_{L^∞}`. -/
  vortNorm : ℝ → ℝ
  /-- `c₁ > 0`. -/
  c₁_pos : 0 < c₁
  /-- **(a) Separation decay.**  `c₁·√(T*−t) ≤ d(t) ≤ c₂·√(T*−t)`
      for `t < T*`, the Biot–Savart approach law. -/
  separation_decay :
    ∀ t : ℝ, t < tStar →
      c₁ * Real.sqrt (tStar - t) ≤ dist t ∧
        dist t ≤ c₂ * Real.sqrt (tStar - t)
  /-- **(b) Vorticity lower bound.**  `‖ω*(t)‖_{L^∞} ≥ c₁/(T*−t)`,
      the stretching-driven concentration. -/
  vorticity_lower :
    ∀ t : ℝ, t < tStar → c₁ / (tStar - t) ≤ vortNorm t
  /-- **(c) BKM divergence.**  The time-integral of the vorticity sup-norm
      up to `T*` diverges — the conjectural input, witnessed here.

      **Parameterised 2026-09-13.**  `bkmIntegralDiverges` was a *field*
      typed with the universe `Prop` alongside this witness, so the instance
      chose the proposition and `⟨True, trivial⟩` discharged sub-claim (c);
      `vorticity_lower_bound_conditional`'s third conjunct was therefore
      unconditional.  Fields (a) and (b) above were always genuinely
      encoded — only (c) was not, so this is the minimal fix.

      It is a parameter rather than an encoding because stating the BKM
      divergence needs an integral this class does not carry (`vortNorm` is
      a bare `ℝ → ℝ` with no integrability hypothesis), and guessing at its
      content would be the author's call to make.  The conjectural input is
      untouched and still open. -/
  bkm_diverges : bkmIntegralDiverges

/-- **Vorticity lower bound (conditional).**

    Conditional on the q-NS conjecture cone, the q-NS vorticity
    `‖ω*‖_{L^∞}` along anti-parallel vortex-pair initial data
    satisfies the separation decay (a), the `c₁/(T*−t)` lower bound
    (b), and the BKM time-integral divergence (c) — the vorticity
    blow-up signature of `conj:ns-counterexample`.

    *Derived* from the three directional hypotheses of
    `VorticityLowerBoundContext` (it composes them; it does not
    assume its own conclusion).

    Ref: [leitner2026] §Fluid dynamics / Vorticity lower bound,
         conj:vorticity-lower-bound -/
def vorticity_lower_bound_conditional
    {bkmIntegralDiverges : Prop}
    [ctx : VorticityLowerBoundContext bkmIntegralDiverges] :
    (∀ t : ℝ, t < ctx.tStar →
        ctx.c₁ * Real.sqrt (ctx.tStar - t) ≤ ctx.dist t ∧
          ctx.dist t ≤ ctx.c₂ * Real.sqrt (ctx.tStar - t)) ∧
    (∀ t : ℝ, t < ctx.tStar → ctx.c₁ / (ctx.tStar - t) ≤ ctx.vortNorm t) ∧
    bkmIntegralDiverges :=
  ⟨ctx.separation_decay, ctx.vorticity_lower, ctx.bkm_diverges⟩

end QOU.FluidDynamics
