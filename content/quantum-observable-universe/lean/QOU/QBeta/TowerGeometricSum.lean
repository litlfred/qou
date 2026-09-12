/-
# The E₀ tower factor `1/(1 - ℏ_q²)`: what is derived and what is assumed.

`qbeta_e0.tower_summed` multiplies the Q_β energy scale by `1/(1 - ℏ_q²)`.
Bean `qou-y3bm` asked whether that series is derived. It is — modulo ONE
hypothesis, which this file isolates so nobody has to take it on trust.

## The two corpus inputs

* `prop:brane-tower-q-laplacian-decay` (`QOU.Observations.brane_tower_q_laplacian_decay`)
  writes the tower as `Σ_{n} ℏ_q^{2n} · Δ^{(n)}(ρ)`.  The `ℏ_q^{2n}` is the
  tower's own **grading**, not a bound: the bound in that proof is the separate
  factor `Cⁿ q^{2nk}` on `Δ^{(n)}`.
* `prop:delta-max-uniform-bound` (`QOU.MassEndomorphism.delta_max_uniform_bound`)
  gives `|Δ^{(n)}(ρ)| ≤ Δ_max(ρ)` **independent of the jet level `n`**.

## What each buys, kept apart on purpose

`towerSum_of_const` — if the residual is **level-independent** (`Δ^{(n)} = Δ`
for all `n`), the tower is *exactly* `Δ / (1 - ℏ_q²)`.  This is the identity
`qbeta_e0.tower_summed` uses.

`towerSum_le_of_uniform_bound` — if the residual is merely **uniformly
bounded** (what the corpus actually proves), the same expression is an
**upper bound in magnitude**, not the value.

🛑 THE GAP, STATED PRECISELY.  `delta_max_uniform_bound` proves a bound uniform
in `n`; it does NOT prove `Δ^{(n)}` is constant in `n`.  So
`E₀ / (1 - ℏ_q²)` is the tower **at saturation** and a **magnitude bound**
otherwise.  Closing `qou-y3bm` means proving `Δ^{(n)}` is level-independent, or
computing its `n`-dependence and replacing the geometric sum.  Do not read
`tower_summed` as more than this.

A note on the free scale, because it is the trap here: the decay proof's ratio
is `ℏ_q² · C · q²` with `C = ℏ_q / ((q - q⁻¹)² L_q²)`, and `L_q` is the
*q-deformed filament length* — a free geometric scale.  That `C` belongs to the
BOUND on `Δ^{(n)}`, not to the grading, so it does not contaminate
`towerSum_of_const`.  It would contaminate any attempt to derive the ratio
itself as `ℏ_q² C q²`; such an attempt smuggles in a choice of `L_q`.
-/
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.Normed.Module.Basic

namespace QOU.QBeta

open scoped Topology

/-- `ℏ_q = 1 - 1/q`, the substrate deformation parameter. -/
noncomputable def hbarQ (q : ℝ) : ℝ := 1 - 1 / q

/-- At `q > 1` the tower ratio `ℏ_q²` is in `[0, 1)`, so the grading converges.
At the substrate pin `q₀ ≈ 1.11` this gives `ℏ_q² ≈ 0.0098`. -/
theorem hbarQ_sq_lt_one {q : ℝ} (hq : 1 < q) : hbarQ q ^ 2 < 1 := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have h1 : 0 < 1 / q := by positivity
  have h2 : 1 / q < 1 := by
    rw [div_lt_one hq0]; exact hq
  have hlb : (0:ℝ) ≤ hbarQ q := by
    unfold hbarQ; linarith
  have hub : hbarQ q < 1 := by
    unfold hbarQ; linarith
  calc hbarQ q ^ 2 = hbarQ q * hbarQ q := sq (hbarQ q)
    _ < 1 * 1 := by
        apply mul_lt_mul' (le_of_lt hub) hub hlb zero_lt_one
    _ = 1 := one_mul 1

/-- **The identity `tower_summed` uses.**  A tower `Σ_n ℏ_q^{2n} · Δ` whose
residual is LEVEL-INDEPENDENT sums to `Δ / (1 - ℏ_q²)`.

This is where the `1/(1 - ℏ_q²)` in `qbeta_e0.tower_summed` comes from: the
`ℏ_q^{2n}` is the brane tower's structural grading, and `Δ^{(n)} = Δ` is the
hypothesis. -/
theorem towerSum_of_const {q : ℝ} (hq : 1 < q) (Δ : ℝ) :
    ∑' _n : ℕ, hbarQ q ^ (2 * _n) * Δ = Δ / (1 - hbarQ q ^ 2) := by
  have hr : hbarQ q ^ 2 < 1 := hbarQ_sq_lt_one hq
  have hr0 : (0:ℝ) ≤ hbarQ q ^ 2 := sq_nonneg _
  have habs : |hbarQ q ^ 2| < 1 := by
    rw [abs_of_nonneg hr0]; exact hr
  have hpow : ∀ n : ℕ, hbarQ q ^ (2 * n) = (hbarQ q ^ 2) ^ n := by
    intro n; rw [← pow_mul, Nat.mul_comm]
  calc ∑' _n : ℕ, hbarQ q ^ (2 * _n) * Δ
      = ∑' n : ℕ, (hbarQ q ^ 2) ^ n * Δ := by
        exact tsum_congr fun n => by rw [hpow n]
    _ = (∑' n : ℕ, (hbarQ q ^ 2) ^ n) * Δ := by
        rw [tsum_mul_right]
    _ = (1 - hbarQ q ^ 2)⁻¹ * Δ := by
        rw [tsum_geometric_of_lt_one hr0 hr]
    _ = Δ / (1 - hbarQ q ^ 2) := by
        rw [inv_mul_eq_div]

/-- **What the corpus actually proves buys you: a bound, not the value.**
Given only `|Δ^{(n)}| ≤ M` uniformly in `n` — which is exactly
`delta_max_uniform_bound` — the geometric expression bounds the tower's
magnitude termwise.

Stated termwise rather than on the `tsum` so it carries no summability
hypothesis: each partial sum is dominated, which is the honest content. -/
theorem towerSum_le_of_uniform_bound {q : ℝ} (hq : 1 < q) (Δ : ℕ → ℝ) (M : ℝ)
    (hM : ∀ n, |Δ n| ≤ M) (N : ℕ) :
    |∑ n ∈ Finset.range N, hbarQ q ^ (2 * n) * Δ n|
      ≤ ∑ n ∈ Finset.range N, hbarQ q ^ (2 * n) * M := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have hlb : (0:ℝ) ≤ hbarQ q := by
    have h2 : 1 / q < 1 := by rw [div_lt_one hq0]; exact hq
    unfold hbarQ; linarith
  refine le_trans (Finset.abs_sum_le_sum_abs _ _) ?_
  refine Finset.sum_le_sum fun n _ => ?_
  rw [abs_mul, abs_of_nonneg (pow_nonneg hlb _)]
  exact mul_le_mul_of_nonneg_left (hM n) (pow_nonneg hlb _)

/-- The gap between the two results above, as a statement rather than a comment:
a uniform bound does NOT give level-independence.  Witnessed by an alternating
residual, which is uniformly bounded by `1` and not constant. -/
theorem uniform_bound_not_const :
    ∃ Δ : ℕ → ℝ, (∀ n, |Δ n| ≤ 1) ∧ ¬ (∀ n, Δ n = Δ 0) := by
  refine ⟨fun n => (-1 : ℝ) ^ n, fun n => ?_, ?_⟩
  · rw [abs_pow, abs_neg, abs_one, one_pow]
  · intro h
    have h1 := h 1
    norm_num at h1

end QOU.QBeta
