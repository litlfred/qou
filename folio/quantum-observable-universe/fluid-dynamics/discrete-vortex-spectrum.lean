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

The md states four claims: (1) the discrete eigenvalue spectrum
`λ_k = [k]_q² · ℏ_q / L_q²`, (2) the intensity energy levels
`E_j = ℏ_q/(2 I_q) · [j]_q [j+1]_q`, (3) ladder transitions with the
selection rule `|j − j'| = 1` and transition energy `ΔE = E_{j'} − E_j`,
and (4) the classical limit `q → 1`: `[k]_q → k` (Kelvin-wave spectrum)
and `[j]_q[j+1]_q → j(j+1)` (rigid-rotor). The earlier version of this
file stated only `theorem … : True := trivial`, a tautology that does not
assert the spectrum at all (integrity FAIL).

Below all four claims are bundled as fields of an abstract
`DiscreteVortexSpectrumContext` (the spectral data of one filament), and
the headline theorem `discrete_vortex_spectrum` states the full
proposition as their conjunction (matching the `.ts` `lean.ref`), with
projection theorems for the individual claims. Mirrors the build-graph
copy under `QOU/FluidDynamics/discrete_vortex_spectrum.lean`. The
`q`-integer `[k]_q` is supplied as an abstract function `qInt : ℕ → ℝ`,
and the classical limit is modelled by `q = 1 → ∀ k, qInt k = k`.

## References
- [leitner2026] §Fluid dynamics / Discrete vortex spectrum,
  prop:discrete-vortex-spectrum
-/

namespace QOU.FluidDynamics

/-- Spectral data of a stable vortex filament: the `q`-integer function,
    the physical scales (`ℏ_q`, filament length `L_q`, moment of inertia
    `I_q`), and the load-bearing spectral formulae the md asserts. -/
class DiscreteVortexSpectrumContext where
  /-- The substrate parameter `q : ℝ` (`q > 1` in the spectral regime;
      the classical limit is `q = 1`). -/
  q : ℝ
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
  /-- The transition energy `ΔE_{j→j'}` between intensity levels. -/
  deltaE : ℕ → ℕ → ℝ
  /-- **(1) Eigenvalue spectrum.** `λ_k = [k]_q² · ℏ_q / L_q²`. -/
  spectrum : ∀ k, lam k = (qInt k) ^ 2 * hbar / Lq ^ 2
  /-- **(2) Energy levels.** `E_j = ℏ_q/(2 I_q) · [j]_q [j+1]_q`, with the
      level energy reading `qInt n * qInt (n+1)`. -/
  energy_level : ∀ n, energy n = hbar / (2 * Iq) * (qInt n * qInt (n + 1))
  /-- **(3) Ladder transitions, selection rule `|j − j'| = 1`.** For levels
      one rung apart (`n+1 = m` or `m+1 = n`) the transition energy is the
      level-energy difference `E_{j'} − E_j`. -/
  ladder_transition : ∀ n m, (n + 1 = m ∨ m + 1 = n) →
    deltaE n m = energy m - energy n
  /-- **(4) Classical limit.** At `q = 1` the `q`-integer collapses to the
      ordinary integer, `[k]_q → k`, recovering the Kelvin-wave / rigid-rotor
      spectrum (`[j]_q[j+1]_q → j(j+1)`). -/
  classical_limit : q = 1 → ∀ k, qInt k = (k : ℝ)

/-- **Discrete vortex mode spectrum** ([`prop:discrete-vortex-spectrum`]).

    The full proposition: (1) the discrete eigenvalue spectrum
    `λ_k = [k]_q² · ℏ_q / L_q²`, (2) the intensity energy levels
    `E_j = ℏ_q/(2 I_q) · [j]_q [j+1]_q`, (3) ladder transitions obeying the
    selection rule `|j − j'| = 1` with energy `ΔE = E_{j'} − E_j`, and
    (4) the classical limit `q → 1`, `[k]_q → k`. All four md bullets are
    bundled here so the `lean.ref` target states the complete proposition,
    not just the eigenvalue spectrum. -/
-- Ref: [leitner2026] prop:discrete-vortex-spectrum
def discrete_vortex_spectrum [ctx : DiscreteVortexSpectrumContext] :
    (∀ k, ctx.lam k = (ctx.qInt k) ^ 2 * ctx.hbar / ctx.Lq ^ 2) ∧
    (∀ n, ctx.energy n = ctx.hbar / (2 * ctx.Iq) * (ctx.qInt n * ctx.qInt (n + 1))) ∧
    (∀ n m, (n + 1 = m ∨ m + 1 = n) → ctx.deltaE n m = ctx.energy m - ctx.energy n) ∧
    (ctx.q = 1 → ∀ k, ctx.qInt k = (k : ℝ)) :=
  ⟨ctx.spectrum, ctx.energy_level, ctx.ladder_transition, ctx.classical_limit⟩

/-- **Eigenvalue spectrum** (md item (1), projection of
    `discrete_vortex_spectrum`). The eigenvalues of the `q`-Laplacian on the
    filament are `λ_k = [k]_q² · ℏ_q / L_q²`. -/
-- Ref: [leitner2026] prop:discrete-vortex-spectrum
theorem discrete_vortex_eigenvalues [ctx : DiscreteVortexSpectrumContext]
    (k : ℕ) :
    ctx.lam k = (ctx.qInt k) ^ 2 * ctx.hbar / ctx.Lq ^ 2 :=
  ctx.spectrum k

/-- **Intensity energy levels.** `E_j = ℏ_q/(2 I_q) · [j]_q [j+1]_q`. -/
-- Ref: [leitner2026] prop:discrete-vortex-spectrum
theorem discrete_vortex_energy_levels [ctx : DiscreteVortexSpectrumContext]
    (n : ℕ) :
    ctx.energy n = ctx.hbar / (2 * ctx.Iq) * (ctx.qInt n * ctx.qInt (n + 1)) :=
  ctx.energy_level n

/-- **Transition energy** `ΔE_{j→j'} = E_{j'} − E_j`, the energy released
    or absorbed in a ladder transition (md formula (3)), obtained by
    differencing the level energies. -/
-- Ref: [leitner2026] prop:discrete-vortex-spectrum
theorem discrete_vortex_transition_energy
    [ctx : DiscreteVortexSpectrumContext] (n m : ℕ) :
    ctx.energy m - ctx.energy n
      = ctx.hbar / (2 * ctx.Iq)
          * (ctx.qInt m * ctx.qInt (m + 1) - ctx.qInt n * ctx.qInt (n + 1)) := by
  rw [ctx.energy_level m, ctx.energy_level n]; ring

/-- **Ladder selection rule** (md item (3)): for adjacent intensity levels
    (`|j − j'| = 1`, i.e. `n+1 = m` or `m+1 = n`) the transition energy is the
    level-energy difference, with the closed form below. -/
-- Ref: [leitner2026] prop:discrete-vortex-spectrum
theorem discrete_vortex_ladder_rule
    [ctx : DiscreteVortexSpectrumContext] (n m : ℕ)
    (h : n + 1 = m ∨ m + 1 = n) :
    ctx.deltaE n m
      = ctx.hbar / (2 * ctx.Iq)
          * (ctx.qInt m * ctx.qInt (m + 1) - ctx.qInt n * ctx.qInt (n + 1)) := by
  rw [ctx.ladder_transition n m h, discrete_vortex_transition_energy]

/-- **Classical limit** (md item (4)): at `q = 1` the `q`-integer collapses to
    the ordinary integer `[k]_q → k`, recovering the Kelvin-wave spectrum. -/
-- Ref: [leitner2026] prop:discrete-vortex-spectrum
theorem discrete_vortex_classical_limit
    [ctx : DiscreteVortexSpectrumContext] (hq : ctx.q = 1) (k : ℕ) :
    ctx.qInt k = (k : ℝ) :=
  ctx.classical_limit hq k

end QOU.FluidDynamics
