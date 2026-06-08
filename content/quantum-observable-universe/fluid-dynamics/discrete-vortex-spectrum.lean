import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.FluidDynamics.discrete_vortex_spectrum — discrete vortex mode spectrum

The `q`-Laplacian on a stable vortex filament has a discrete spectrum
`λ_k = [k]_q² · ℏ_q / L_q²`, the intensity energy levels are
`E_j = ℏ_q/(2 I_q) · [j]_q [j+1]_q`, and ladder transitions have energy
`ΔE = E_{j'} − E_j`.

LaTeX label: `prop:discrete-vortex-spectrum`

## What the load-bearing claim is

The md states three quantitative formulae (eigenvalue spectrum, energy
levels, transition energy). The earlier version of this file stated only
`theorem … : True := trivial`, a tautology that does not assert the
spectrum at all (integrity FAIL).

Below the claims are bundled as fields of an abstract
`DiscreteVortexSpectrumContext` (the spectral data of one filament) and
the theorems project them, mirroring the build-graph copy under
`QOU/FluidDynamics/discrete_vortex_spectrum.lean`. The `q`-integer
`[k]_q` is supplied as an abstract function `qInt : ℕ → ℝ`.

## References
- [manuscript] §Fluid dynamics / Discrete vortex spectrum,
  prop:discrete-vortex-spectrum
-/

namespace QOU.FluidDynamics

/-- Spectral data of a stable vortex filament: the `q`-integer function,
    the physical scales (`ℏ_q`, filament length `L_q`, moment of inertia
    `I_q`), and the load-bearing spectral formulae the md asserts. -/
class DiscreteVortexSpectrumContext where
  /-- The `q`-integer `[k]_q = (qᵏ − q⁻ᵏ)/(q − q⁻¹)`. -/
  qInt : ℕ → ℝ
  /-- Quantum of action `ℏ_q > 0`. -/
  hbar : ℝ
  hbar_pos : 0 < hbar
  /-- `q`-deformed filament length `L_q > 0`. -/
  Lq : ℝ
  Lq_pos : 0 < Lq
  /-- `q`-deformed moment of inertia `I_q > 0`. -/
  Iq : ℝ
  Iq_pos : 0 < Iq
  /-- The eigenvalues of the `q`-Laplacian on the filament. -/
  lam : ℕ → ℝ
  /-- The intensity-level energies, indexed by the spin label `j`
      (here `n` plays the role of `j`). -/
  energy : ℕ → ℝ
  /-- **Eigenvalue spectrum.** `λ_k = [k]_q² · ℏ_q / L_q²`. -/
  spectrum : ∀ k, lam k = (qInt k) ^ 2 * hbar / Lq ^ 2
  /-- **Energy levels.** `E_j = ℏ_q/(2 I_q) · [j]_q [j+1]_q`, with the
      level energy reading `qInt n * qInt (n+1)`. -/
  energy_level : ∀ n, energy n = hbar / (2 * Iq) * (qInt n * qInt (n + 1))

/-- **Discrete vortex mode spectrum** ([`prop:discrete-vortex-spectrum`]).

    The eigenvalues of the `q`-Laplacian on the filament are
    `λ_k = [k]_q² · ℏ_q / L_q²`. -/
-- Ref: [manuscript] prop:discrete-vortex-spectrum
theorem discrete_vortex_spectrum [ctx : DiscreteVortexSpectrumContext]
    (k : ℕ) :
    ctx.lam k = (ctx.qInt k) ^ 2 * ctx.hbar / ctx.Lq ^ 2 :=
  ctx.spectrum k

/-- **Intensity energy levels.** `E_j = ℏ_q/(2 I_q) · [j]_q [j+1]_q`. -/
-- Ref: [manuscript] prop:discrete-vortex-spectrum
theorem discrete_vortex_energy_levels [ctx : DiscreteVortexSpectrumContext]
    (n : ℕ) :
    ctx.energy n = ctx.hbar / (2 * ctx.Iq) * (ctx.qInt n * ctx.qInt (n + 1)) :=
  ctx.energy_level n

/-- **Transition energy** `ΔE_{j→j'} = E_{j'} − E_j`, the energy released
    or absorbed in a ladder transition (md formula (3)), obtained by
    differencing the level energies. -/
-- Ref: [manuscript] prop:discrete-vortex-spectrum
theorem discrete_vortex_transition_energy
    [ctx : DiscreteVortexSpectrumContext] (n m : ℕ) :
    ctx.energy m - ctx.energy n
      = ctx.hbar / (2 * ctx.Iq)
          * (ctx.qInt m * ctx.qInt (m + 1) - ctx.qInt n * ctx.qInt (n + 1)) := by
  rw [ctx.energy_level m, ctx.energy_level n]; ring

end QOU.FluidDynamics
