import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.BraidsAndKnots.CSMarginCorrelationConstant — the exact (CS) correlation `ρ_P = 2√6/5`

The leading-order Cauchy–Schwarz margin for `M₁ > 0` (gap `qou-k5r5`, machinery task `qou-po72`,
epic `qou-h315`) is `m∞ = ρ_P − √(V_D/V_A)`, where `ρ_P = Corr(Σ|c|, ω₃)` is the limiting
Plancherel correlation of the content charge and the cubic content power. Via the Ivanov–Olshanski
Kerov CLT and the elementary closed-form modified-Chebyshev coefficients
(`wlambda_covariance_epic_M1_po72_leading_constants.py`, audit
`docs/audits/2026-08-29-covariance-kernel-M1-po72-leading-constants.md`),

    ρ_P = Â₃ / √(3 V_A),   Â₃ = 8/(5π),   V_A = 8/(9π²)   (de-poissonized, k=1 frozen).

The remarkable fact is that **π cancels entirely in the square**:

    ρ_P² = Â₃²/(3 V_A) = (64/(25π²)) / (8/(3π²)) = 192/200 = 24/25,

a purely *rational* value, whence `ρ_P = √(24/25) = 2√6/5`.

This file formalizes both halves:
* `csMargin_rhoSq_eq` — the rational identity `Â₃²/(3 V_A) = 24/25`, a sorry-free `field_simp; ring`
  fact over any characteristic-zero field with the scale `p := π ≠ 0`. **The π-cancellation is the
  content** — the statement is false if either constant is perturbed, so it is genuinely falsifiable,
  not a tautology.
* `csMargin_rho_eq` (in the Transcendental companion `CSMarginCorrelationConstantReal`) — the real specialization `Â₃/√(3 V_A) = 2√6/5`, proved from the rational square
  plus nonnegativity.

Scope (§7c): the square is generic-field algebra (no `ℝ`); the `√` step is archimedean and lives over
`ℝ`. Nothing here is fitted — the constants are derived closed forms; only the cited IO CLT is assumed.
-/

namespace QOU.BraidsAndKnots.CSMarginCorrelationConstant

/-- **The (CS) correlation squared is rational: `Â₃²/(3 V_A) = 24/25` (sorry-free).**

With the de-poissonized leading constants `Â₃ = 8/(5p)` and `V_A = 8/(9p²)` (`p := π`), the ratio
`Â₃²/(3 V_A)` is `24/25` — the factors of `p` cancel exactly. Stated over any characteristic-zero
field with `p ≠ 0` (§7c: purely algebraic; `CharZero` supplies `5,8,9,25 ≠ 0`). Perturbing either
constant breaks the equality, so this is a falsifiable identity. -/
theorem csMargin_rhoSq_eq {K : Type*} [Field K] [CharZero K] (p : K) (hp : p ≠ 0) :
    (8 / (5 * p)) ^ 2 / (3 * (8 / (9 * p ^ 2))) = 24 / 25 := by
  field_simp
  ring

/-! The `Real.sqrt` form `csMargin_rho_eq` (`ρ = 2√6/5`) is in
`QOU.Transcendental.BraidKnotOctonion.CSMarginCorrelationConstantReal`; this module keeps
the `ρ² = 24/25` identity over any characteristic-zero field (bean `qou-dk7p`). -/

end QOU.BraidsAndKnots.CSMarginCorrelationConstant
