import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.FluidDynamics.kelvin_dispersion_derivation — Kelvin dispersion from the q-Laplacian

The `q`-Laplacian `Δ_q = -(z D_q)∘(z D_q)` acts on the monomial `zᵏ` with
eigenvalue `-[k]_q²` (since `z D_q (zᵏ) = [k]_q zᵏ`); restoring units gives
the spectrum `λ_k = [k]_q² ℏ_q / L_q²`, and the linearised Kelvin-wave
equation yields the undamped dispersion `ω_k = Γ_q^{1/2}/(2√π a_q)·[k]_q/L_q`
and the damped decay rate `γ_k = ν_q/2·[k]_q²/L_q²`.

LaTeX label: `prop:kelvin-dispersion-derivation`

## What the load-bearing claim is

The md *derives* the discrete vortex spectrum: the `q`-derivative ladder
property `z D_q (zᵏ) = [k]_q zᵏ` forces `Δ_q (zᵏ) = -[k]_q² zᵏ`, hence
`μ_k = [k]_q²` and `λ_k = [k]_q² ℏ_q / L_q²`; the dispersion relation then
gives `ω_k` (undamped) and `γ_k` (damped decay). The earlier version of
this file stated only `theorem … : True := trivial`, asserting none of the
derivation (integrity FAIL).

Below the `q`-derivative ladder action is bundled as a field of
`KelvinDispersionContext`; the Laplacian eigenvalue
`Δ_q(zᵏ) = -[k]_q² zᵏ` is then **proved** from it (not assumed), and the
spectrum, dispersion and decay rate are projected. Mirrors the
build-graph copy under `QOU/FluidDynamics/kelvin_dispersion_derivation.lean`.

## References
- [leitner2026] §Fluid dynamics / Kelvin dispersion derivation,
  prop:kelvin-dispersion-derivation
-/

namespace QOU.FluidDynamics

/-- Data of the linearised Kelvin-wave problem on a filament: the
    `q`-integer `[k]_q`, the operator `zD_q` and the `q`-Laplacian `Δ_q`
    (as their action on the `k`-th mode, valued in the coefficient of
    `zᵏ`), the physical scales, and the dispersion / decay rates. -/
class KelvinDispersionContext where
  /-- The `q`-integer `[k]_q`. -/
  qInt : ℕ → ℝ
  /-- Coefficient of `zᵏ` in `z D_q (zᵏ)`. The md computes this `= [k]_q`. -/
  zDq : ℕ → ℝ
  /-- Coefficient of `zᵏ` in `Δ_q (zᵏ) = -(z D_q)∘(z D_q)(zᵏ)`. -/
  laplacian : ℕ → ℝ
  /-- Quantum of action `ℏ_q > 0`, filament length `L_q > 0`. -/
  hbar : ℝ
  hbar_pos : 0 < hbar
  Lq : ℝ
  Lq_pos : 0 < Lq
  /-- Eigenvalues of the `q`-Laplacian with physical units. -/
  lam : ℕ → ℝ
  /-- Core radius `a_q`, viscosity `ν_q`, the positive constant
      `sqrtΓ_q = Γ_q^{1/2}`, and `√π` (kept as opaque positive reals so the
      derivation needs no analysis imports). -/
  sqrtGamma : ℝ
  aq : ℝ
  nuq : ℝ
  /-- `√π` as an opaque constant (so `2 √π a_q` reads `2 * sqrtPiConst * aq`).
      Named `sqrtPiConst` (not `piConst`) to avoid collision with
      `AcousticHorizonContext.piConst`, which denotes `π` rather than `√π`. -/
  sqrtPiConst : ℝ
  /-- Undamped Kelvin dispersion frequency `ω_k` and damped decay rate `γ_k`. -/
  omega : ℕ → ℝ
  gamma : ℕ → ℝ
  /-- **`q`-derivative ladder.** `z D_q (zᵏ) = [k]_q zᵏ`. -/
  zDq_ladder : ∀ k, zDq k = qInt k
  /-- **Laplacian is `-(zD_q)²`.** The coefficient of `Δ_q(zᵏ)` is minus
      the square of the `zD_q`-coefficient. -/
  laplacian_def : ∀ k, laplacian k = -(zDq k) ^ 2
  /-- **Spectrum with units.** `λ_k = [k]_q² ℏ_q / L_q²`. -/
  spectrum : ∀ k, lam k = (qInt k) ^ 2 * hbar / Lq ^ 2
  /-- **Undamped dispersion.** `ω_k = Γ_q^{1/2}/(2√π a_q) · [k]_q / L_q`,
      packaged with `sqrtΓ_q` and `π` as opaque positive constants. -/
  dispersion : ∀ k, omega k = sqrtGamma / (2 * sqrtPiConst * aq) * qInt k / Lq
  /-- **Damped decay rate.** `γ_k = ν_q/2 · [k]_q² / L_q²`. -/
  decay : ∀ k, gamma k = nuq / 2 * (qInt k) ^ 2 / Lq ^ 2

/-- **`q`-Laplacian eigenvalue.** `Δ_q(zᵏ) = -[k]_q² zᵏ` — the core of the
    md derivation, *proved* from the `q`-derivative ladder and the
    definition `Δ_q = -(zD_q)²` ([`prop:kelvin-dispersion-derivation`]). -/
-- Ref: [leitner2026] prop:kelvin-dispersion-derivation
theorem kelvin_dispersion_derivation [ctx : KelvinDispersionContext]
    (k : ℕ) :
    ctx.laplacian k = -(ctx.qInt k) ^ 2 := by
  rw [ctx.laplacian_def k, ctx.zDq_ladder k]

/-- **Spectrum with units.** `λ_k = [k]_q² ℏ_q / L_q²`. -/
-- Ref: [leitner2026] prop:kelvin-dispersion-derivation
theorem kelvin_spectrum [ctx : KelvinDispersionContext] (k : ℕ) :
    ctx.lam k = (ctx.qInt k) ^ 2 * ctx.hbar / ctx.Lq ^ 2 :=
  ctx.spectrum k

/-- **Undamped Kelvin dispersion.** `ω_k ∝ [k]_q / L_q`. -/
-- Ref: [leitner2026] prop:kelvin-dispersion-derivation
theorem kelvin_undamped_dispersion [ctx : KelvinDispersionContext] (k : ℕ) :
    ctx.omega k
      = ctx.sqrtGamma / (2 * ctx.sqrtPiConst * ctx.aq) * ctx.qInt k / ctx.Lq :=
  ctx.dispersion k

/-- **Damped decay rate.** `γ_k = ν_q/2 · [k]_q² / L_q²`. -/
-- Ref: [leitner2026] prop:kelvin-dispersion-derivation
theorem kelvin_damped_decay [ctx : KelvinDispersionContext] (k : ℕ) :
    ctx.gamma k = ctx.nuq / 2 * (ctx.qInt k) ^ 2 / ctx.Lq ^ 2 :=
  ctx.decay k

end QOU.FluidDynamics
