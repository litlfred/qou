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

/-! ## 🛑 RESOLVED 2026-09-12: the hypothesis of `towerSum_of_const` is FALSE

`qou-y3bm` left one gap — is `Δ^{(n)}` level-independent?  It is **not**, and the
corpus already said so.  `prop:brane-tower-q-laplacian-decay`'s Step 3 states an
**equality**, not a bound:

    |⟨e_k, Δ^{(n)} e_k⟩| = (λ_k^{(q)})^n ,      λ_k^{(q)} = [k]_q² ℏ_q / L_q²

so `Δ^{(n)}` is the **n-th iterate of the q-Laplacian** and its eigenvalue grows
(or decays) geometrically in `n`.  `towerSum_of_const` is a true theorem whose
hypothesis this object does not satisfy.

The true sum is therefore geometric in `ℏ_q² · λ_k`, not in `ℏ_q²`
(`towerSum_iterated` below), and it **coincides with `1/(1 - ℏ_q²)` exactly when
`λ_k = 1`** (`towerSum_iterated_eq_simple_iff`).  At the leading mode `k = 1`,
`[1]_q = 1`, so `λ_1 = ℏ_q / L_q²` and `λ_1 = 1` iff

    L_q = √ℏ_q .

**So `qbeta_e0.tower_summed` does carry a hidden parameter after all, and it is
now named: it fixes the q-deformed filament length to `√ℏ_q`.**  That is a choice,
not a derivation — `L_q` is a free geometric scale (`fluid-dynamics/discrete-vortex-spectrum`
calls it "the q-deformed filament length"; the Kelvin-dispersion derivation takes
`L_q = L`, the period).  The honest statement is that the tower factor is a
one-parameter family in `L_q` and the implemented value selects one member.
-/

/-- **The tower of an ITERATED residual.**  With `Δ^{(n)}` the `n`-th iterate,
eigenvalue `lam ^ n`, the tower is geometric in `ℏ_q² · lam`. -/
-- `1 < q` is deliberately ABSENT: the linter flagged it unused, and it is -- the
-- geometric sum needs only `0 ≤ ℏ_q² · lam < 1`, so the theorem is STRONGER
-- without it and holds wherever the ratio is admissible, not only above the
-- substrate. Keeping an unused hypothesis would understate it.
theorem towerSum_iterated {q : ℝ} (lam : ℝ) (hlam : 0 ≤ lam)
    (h : hbarQ q ^ 2 * lam < 1) :
    ∑' n : ℕ, hbarQ q ^ (2 * n) * lam ^ n = (1 - hbarQ q ^ 2 * lam)⁻¹ := by
  have hr0 : (0:ℝ) ≤ hbarQ q ^ 2 * lam := mul_nonneg (sq_nonneg _) hlam
  have hpow : ∀ n : ℕ, hbarQ q ^ (2 * n) * lam ^ n = (hbarQ q ^ 2 * lam) ^ n := by
    intro n
    rw [mul_pow, ← pow_mul, Nat.mul_comm]
  calc ∑' n : ℕ, hbarQ q ^ (2 * n) * lam ^ n
      = ∑' n : ℕ, (hbarQ q ^ 2 * lam) ^ n := tsum_congr hpow
    _ = (1 - hbarQ q ^ 2 * lam)⁻¹ := tsum_geometric_of_lt_one hr0 h

/-- **The implemented factor `1/(1 - ℏ_q²)` is the `lam = 1` member of that
family, and only that one.**  So adopting it is adopting `λ_k = 1`. -/
theorem towerSum_iterated_eq_simple_iff {q : ℝ} (lam : ℝ)
    (hne : hbarQ q ^ 2 ≠ 0) :
    (1 - hbarQ q ^ 2 * lam)⁻¹ = (1 - hbarQ q ^ 2)⁻¹ ↔ lam = 1 := by
  constructor
  · intro h
    have h' := inv_inj.mp h
    have hstep : hbarQ q ^ 2 * lam = hbarQ q ^ 2 * 1 := by
      rw [mul_one]; linarith
    exact mul_left_cancel₀ hne hstep
  · intro h; rw [h, mul_one]

/-- At the leading mode `[1]_q = 1`, so `λ_1 = ℏ_q / L_q²`, and `λ_1 = 1` pins
`L_q² = ℏ_q`.  Stated on `L_q²` so no square root is needed. -/
theorem leadingMode_lam_eq_one_iff {q Lq : ℝ} (hL : Lq ≠ 0) :
    hbarQ q / Lq ^ 2 = 1 ↔ Lq ^ 2 = hbarQ q := by
  have hL2 : Lq ^ 2 ≠ 0 := pow_ne_zero 2 hL
  rw [div_eq_one_iff_eq hL2]
  exact ⟨fun h => h.symm, fun h => h.symm⟩

/-- The gap between the two results above, as a statement rather than a comment:
a uniform bound does NOT give level-independence.  Witnessed by an alternating
residual, which is uniformly bounded by `1` and not constant.

(Still true and still the right statement — but note the ACTUAL residual is not
merely non-constant, it is `lam ^ n`; see `towerSum_iterated`.) -/
theorem uniform_bound_not_const :
    ∃ Δ : ℕ → ℝ, (∀ n, |Δ n| ≤ 1) ∧ ¬ (∀ n, Δ n = Δ 0) := by
  refine ⟨fun n => (-1 : ℝ) ^ n, fun n => ?_, ?_⟩
  · rw [abs_pow, abs_neg, abs_one, one_pow]
  · intro h
    have h1 := h 1
    norm_num at h1

end QOU.QBeta
