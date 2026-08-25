import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# QOU.FluidDynamics.low_mode_block_global

**Large-data global persistence at the fixed low-mode block — and the
precise localization of the millennium difficulty** (epic `qou-a3n3`
remainder; opening brick).

The GP arc (`surreal_enstrophy_finite_modes.lean`) left one gap: data
with `c·Ω₀ > νμ` (large data) past the bootstrap horizon.  This file
proves that **for the fixed finite block the gap closes**, with no
smallness hypothesis, from two structural facts of a Galerkin low-mode
block:

1. **Energy monotonicity** (`E (n+1) ≤ E n`): the quadratic transfer
   term of a truncated Leray system is energy-conserving (it
   redistributes, never creates), so unforced dissipative dynamics can
   only lower the block energy.
2. **Spectral norm equivalence** (`Ω n ≤ kmax²·E n`): on a finite block
   the enstrophy is controlled by the energy through the top wavenumber
   — all norms are equivalent in finite dimension.

Consequences, all sorry-free and **valid for arbitrarily large data**:

- `energy_le_initial` — `E n ≤ E 0` for all `n`.
- `block_global_enstrophy_bound` — `Ω n ≤ kmax²·E 0` for all `n`: the
  block's enstrophy is globally bounded forever.  This is large-data
  global persistence *at the fixed block*.
- `cumulative_enstrophy_bound` — the discrete **Leray energy
  inequality**: with quantitative dissipation
  `E (n+1) ≤ E n − δν·Ω n`, the cumulative enstrophy satisfies
  `δν·∑_{i<n} Ω i ≤ E 0` — enstrophy is not just bounded but
  summable-in-time against the dissipation rate.

**Where the millennium difficulty actually lives (honest
localization).**  Every constant above is uniform in the data but NOT
in the block size: on the q-ladder the top wavenumber of the active
block is `kmax = [m]_{1+ε}` and the damping threshold pushes
`m ~ ε⁻¹`, so the global bound `kmax²·E 0` diverges as `q → 1⁺`.  The
open millennium content is therefore *not* "does the finite block
persist for large data" (it does — this file), but "are the bounds
uniform as the block widens into the classical limit" — equivalently,
whether the energy flux through the receding damping threshold keeps
the low-mode enstrophy bounded independently of `ε`.  That uniformity
question is the honest remainder of epic `qou-a3n3`; nothing in this
file (or the corpus) resolves it.

Hypothesis-carrying discrete style as in the GP bricks (§7c: generic
linearly ordered field; sequences with step inequalities as explicit
hypotheses — the derivation of those inequalities from a concrete ODE
discretization is the consumer's obligation, not smuggled in here).
-/

namespace QOU.FluidDynamics.LowModeBlock

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

omit [Field K] [IsStrictOrderedRing K] in
/-- Monotone energy stays below its initial value. -/
theorem energy_le_initial (E : ℕ → K) (hmono : ∀ n, E (n + 1) ≤ E n) :
    ∀ n, E n ≤ E 0 := by
  intro n
  induction n with
  | zero => exact le_refl _
  | succ m ih => exact le_trans (hmono m) ih

/-- **Large-data global enstrophy bound at the fixed block**: energy
    monotonicity + finite-block norm equivalence give
    `Ω n ≤ kmax²·E 0` for every `n` — no smallness hypothesis on the
    data.  (The bound is uniform in time and in the data scale `E 0`,
    but grows with the block's top wavenumber — see the module
    docstring for the `ε`-non-uniformity localization.) -/
theorem block_global_enstrophy_bound (E Ω : ℕ → K) (kmax2 : K)
    (hk : 0 ≤ kmax2)
    (hmono : ∀ n, E (n + 1) ≤ E n)
    (hspec : ∀ n, Ω n ≤ kmax2 * E n) :
    ∀ n, Ω n ≤ kmax2 * E 0 := by
  intro n
  calc Ω n ≤ kmax2 * E n := hspec n
    _ ≤ kmax2 * E 0 :=
        mul_le_mul_of_nonneg_left (energy_le_initial E hmono n) hk

/-- **The discrete Leray energy inequality**: with quantitative
    dissipation `E (n+1) ≤ E n − δν·Ω n` and nonnegative energy, the
    cumulative enstrophy is bounded by the initial energy:
    `δν·∑_{i<n} Ω i ≤ E 0` for every `n`.  Enstrophy is
    summable-in-time against the dissipation rate — the discrete
    counterpart of the classical Leray a-priori bound, again with no
    smallness hypothesis. -/
theorem cumulative_enstrophy_bound (E Ω : ℕ → K) (δν : K)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δν * Ω n)
    (hEnonneg : ∀ n, 0 ≤ E n) :
    ∀ n, δν * ∑ i ∈ Finset.range n, Ω i ≤ E 0 := by
  have key : ∀ n, E n + δν * ∑ i ∈ Finset.range n, Ω i ≤ E 0 := by
    intro n
    induction n with
    | zero => simp
    | succ m ih =>
        have hstep := hdiss m
        calc E (m + 1) + δν * ∑ i ∈ Finset.range (m + 1), Ω i
            = E (m + 1) + δν * (∑ i ∈ Finset.range m, Ω i + Ω m) := by
              rw [Finset.sum_range_succ]
          _ = E (m + 1) + δν * Ω m + δν * ∑ i ∈ Finset.range m, Ω i := by
              ring
          _ ≤ E m + δν * ∑ i ∈ Finset.range m, Ω i := by linarith
          _ ≤ E 0 := ih
  intro n
  have := key n
  have := hEnonneg n
  linarith

end QOU.FluidDynamics.LowModeBlock
