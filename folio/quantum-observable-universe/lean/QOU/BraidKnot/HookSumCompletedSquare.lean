import QOU.BraidKnot.HookSumBetaCoordinates
import Mathlib.Algebra.Order.Chebyshev

/-!
# The hook sum is a positive-definite quadratic in the β-numbers

`HookSumBetaCoordinates` puts the hook sum in β-coordinates.  Completing the square there turns
it into a sum of squares, which is what makes the `REV_n` energy term *rigid*:

    8 · Σ_{c∈μ} h(c)  =  Σ_{i<L} (2β_i − a_i)²  −  Σ_{i<L} a_i²,      a_i := 2L − 3 − 4i

The `a_i` depend only on `L`, so the whole `μ`-dependence sits in one sum of squares.  Two
consequences follow immediately and are the point of this file:

| | |
|---|---|
| `eight_mul_sum_hookZ_completedSquare` | the identity above |
| `hookDev_sub_succ` | `d_i − d_{i+1} = 2(β_i − β_{i+1}) − 4` for `d_i := 2β_i − a_i` |
| `eight_mul_card_mul_sum_hookZ_ge` | Cauchy–Schwarz: `(Σ d_i)² − L·Σ a_i² ≤ 8L·Σ_c h(c)` |

**`hookDev_sub_succ` is the rigidity, exactly.** The deviations `d_i` are constant precisely when
every β-gap is `2` — the staircase — and Cauchy–Schwarz says `Σ d_i²` is minimised, at fixed
`Σ d_i`, exactly when the `d_i` are all equal.  Since `Σ d_i` is determined by `(n, L)` alone
(identity (III)), the hook sum's floor at fixed `(n, L)` is attained at gap 2 and the cost of
deviating is *quadratic* in the gap's departure from 2.  No asymptotics enter.

## Why this matters for `qou-hok7`

The `Θ(√n)` coefficient's open item is a **lower** bound on the pair term
`P = Σ_{i<j} ε(β_i − β_j)`.  `P` is small exactly when the β-numbers are widely separated, and
this file is the exact statement of what that costs: separation is deviation of `d` from
constant, and the energy `E = (H − H_min)·ln q₀` pays for it as a sum of squares.  A numerical
version of this was measured in PR #7286
(`computations/deltalambda/rev_energy_gap_rigidity_probe.py`), where it appeared only as the
asymptotic `E ≈ ln q₀ (2n)^{3/2}(ḡ−2)²/24`; the identity below is that statement without the
asymptotics, and it is where a proof should start rather than the fit.

The Cauchy–Schwarz floor is **tight**, not merely valid: measured against `H_min(n)` at every
triangular `n` tested with `L = k`, the gap is exactly `0`.

## Base ring (§7c)

All sums over `ℤ`, matching `HookSumBetaCoordinates` and `PieceAGeneral`.  No `ℝ`, no
archimedean input — the `ln q₀` that turns `H` into an energy lives strictly downstream.

-- Ref: [leitner2026] computations/deltalambda/rev_energy_gap_rigidity_probe.py
-/

namespace QOU.BraidKnot.HookSum

open Finset QOU.BraidKnot.PieceA

/-- The centre of the hook sum's quadratic in row `i` at `L` rows: `a_i = 2L − 3 − 4i`. -/
def hookCentre (L i : ℕ) : ℤ := 2 * (L : ℤ) - 3 - 4 * (i : ℤ)

/-- The row-`i` deviation `d_i = 2β_i − a_i`.  Constant exactly on the staircase. -/
def hookDev (μ : YoungDiagram) (L i : ℕ) : ℤ :=
  2 * ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) - hookCentre L i

/-- **The rigidity, exactly.** `d_i − d_{i+1} = 2(β_i − β_{i+1}) − 4`: the deviations are
constant iff every β-gap is `2`, and each unit of gap-deviation moves `d` by `2`. -/
theorem hookDev_sub_succ (μ : YoungDiagram) (L i : ℕ) :
    hookDev μ L i - hookDev μ L (i + 1)
      = 2 * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
          - ((QOU.SchurWeyl.betaR L μ (i + 1) : ℕ) : ℤ)) - 4 := by
  simp only [hookDev, hookCentre]
  push_cast
  ring

/-- **The hook sum is a positive-definite quadratic in the β-numbers.**

`8 Σ_c h(c) = Σ_{i<L} (2β_i − a_i)² − Σ_{i<L} a_i²` for any padding `L ≥ ℓ(μ)`.  The second sum
depends only on `L`, so all of the diagram-dependence is the sum of squares. -/
theorem eight_mul_sum_hookZ_completedSquare (μ : YoungDiagram) {L : ℕ} (hL : μ.colLen 0 ≤ L) :
    8 * ∑ c ∈ μ.cells, hookZ μ c
      = (∑ i ∈ range L, hookDev μ L i ^ 2) - ∑ i ∈ range L, hookCentre L i ^ 2 := by
  have h := sum_hookZ_betaForm_of_hookMultiset μ hL
  rw [sum_pair_betaR_sub μ L] at h
  have hterm : ∀ i ∈ range L, hookDev μ L i ^ 2 - hookCentre L i ^ 2
      = 4 * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
            * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) + 1))
        - 8 * (((L : ℤ) - 1 - 2 * (i : ℤ)) * ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)) := by
    intro i _
    simp only [hookDev, hookCentre]
    ring
  have hrhs : (∑ i ∈ range L, hookDev μ L i ^ 2) - ∑ i ∈ range L, hookCentre L i ^ 2
      = 4 * (∑ i ∈ range L, ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
              * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) + 1))
        - 8 * (∑ i ∈ range L,
              ((L : ℤ) - 1 - 2 * (i : ℤ)) * ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)) := by
    rw [← Finset.sum_sub_distrib, Finset.sum_congr rfl hterm, Finset.sum_sub_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum]
  rw [hrhs]
  linarith [h]

/-- **Cauchy–Schwarz floor on the hook sum.**

`(Σ_i d_i)² − L·Σ_i a_i² ≤ 8L·Σ_c h(c)`.  Since `Σ_i d_i = 2 Σ_i β_i − Σ_i a_i` is fixed by
`(n, L)` alone (identity (III), `two_mul_sum_betaR`), the left-hand side is a constant of
`(n, L)` — so this is a parameter-free lower bound on the hook sum, hence on the energy.

Measured tight: against `H_min(n)` at `L = k` the gap is exactly `0` at every triangular `n`
tested (`rev_energy_gap_rigidity_probe.py`). -/
theorem eight_mul_card_mul_sum_hookZ_ge (μ : YoungDiagram) {L : ℕ} (hL : μ.colLen 0 ≤ L) :
    (∑ i ∈ range L, hookDev μ L i) ^ 2 - (L : ℤ) * ∑ i ∈ range L, hookCentre L i ^ 2
      ≤ 8 * (L : ℤ) * ∑ c ∈ μ.cells, hookZ μ c := by
  have hid := eight_mul_sum_hookZ_completedSquare μ hL
  have hcs : (∑ i ∈ range L, hookDev μ L i) ^ 2
      ≤ (L : ℤ) * ∑ i ∈ range L, hookDev μ L i ^ 2 := by
    -- Mathlib declares this at the ROOT, not under `Finset`, despite taking a `Finset`:
    -- `Mathlib/Algebra/Order/Chebyshev.lean` opens `Finset` and opens no namespace of its own.
    have h := _root_.sq_sum_le_card_mul_sum_sq (s := range L) (f := fun i => hookDev μ L i)
    simpa [Finset.card_range] using h
  have hmul : (L : ℤ) * ∑ i ∈ range L, hookDev μ L i ^ 2
      = (L : ℤ) * (8 * ∑ c ∈ μ.cells, hookZ μ c)
        + (L : ℤ) * ∑ i ∈ range L, hookCentre L i ^ 2 := by
    have : (∑ i ∈ range L, hookDev μ L i ^ 2)
        = 8 * (∑ c ∈ μ.cells, hookZ μ c) + ∑ i ∈ range L, hookCentre L i ^ 2 := by
      linarith [hid]
    rw [this]
    ring
  linarith [hcs, hmul]

/-- Subtracting the Cauchy-Schwarz floor from eight times the frame-scaled hook sum yields a nonnegative excess (`qou-n4r9`). -/
theorem eight_mul_card_mul_sum_hookZ_sub_nonneg (μ : YoungDiagram) {L : ℕ} (hL : μ.colLen 0 ≤ L) :
    0 ≤ 8 * (L : ℤ) * (∑ c ∈ μ.cells, hookZ μ c)
      - ((∑ i ∈ range L, hookDev μ L i) ^ 2 - (L : ℤ) * ∑ i ∈ range L, hookCentre L i ^ 2) :=
  sub_nonneg.mpr (eight_mul_card_mul_sum_hookZ_ge μ hL)

end QOU.BraidKnot.HookSum
