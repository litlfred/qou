/-
  Euclidean patches as a small-label regime, with q setting the curvature scale.

  Model (issue #7895).  Take the representation labels of `U_q(sl₂)` as the
  "points", and measure the size of the ball of radius `n` by the Plancherel
  volume `V(n) = Σ_{m=1}^{n} [m]_q²` (sum of squared quantum dimensions).  At
  `q = 1` this is the Kirillov picture: `[m]_1 = m`, coadjoint orbits are spheres
  in `su(2)* ≅ ℝ³`, and `V(n) = n(n+1)(2n+1)/6` grows like `n³` — growth
  dimension 3.  For `q > 1` the growth turns exponential.

  The balanced quantum integer is `[n]_q = Σ_{k<n} q^{n−1−2k}`.  This file proves

  * `qint_ge_n`        : `n ≤ [n]_q`               (for `q > 0`),
  * `qint_le`          : `[n]_q ≤ n · q^{n−1}`     (for `q ≥ 1`),
  * `qint_ge_pow`      : `q^{n−1} ≤ [n]_q`         (for `q > 0`),

  so on labels with `q^{n−1}` close to `1` — i.e. `(n−1) log q` small — the
  quantum dimension is `n` up to a factor `q^{n−1}`: a flat (cubic-growth)
  patch, with relative error controlled by `n log q`.  Beyond the scale
  `n ~ 1 / log q` the growth is at least `q^{2(n−1)}`: exponential, the
  hallmark of negative curvature.  So `1 / log q` is the curvature length.

  This is a statement about the label space, not about physical space; reading
  it as the latter is the open conjecture of the analysis doc.
-/
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Push
import Mathlib.Algebra.Order.Field.Power
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace QOU.Optimization.QIntGrowth

open Finset

/-- The balanced quantum integer `[n]_q = Σ_{k<n} q^{(n−1−2k)}`. -/
noncomputable def qint (n : ℕ) (q : ℝ) : ℝ :=
  ∑ k ∈ range n, q ^ ((n : ℤ) - 1 - 2 * k)

/-- Reflection `k ↦ n−1−k` negates the exponent. -/
theorem qint_reflect (n : ℕ) (q : ℝ) :
    qint n q = ∑ k ∈ range n, q ^ (-((n : ℤ) - 1 - 2 * k)) := by
  unfold qint
  rw [← sum_range_reflect]
  refine sum_congr rfl (fun k hk => ?_)
  have hk' : k < n := mem_range.mp hk
  congr 1
  rw [show ((n - 1 - k : ℕ) : ℤ) = (n : ℤ) - 1 - k by omega]
  ring

/-- `x + x⁻¹ ≥ 2` for `x > 0`. -/
theorem add_inv_ge_two {x : ℝ} (hx : 0 < x) : 2 ≤ x + x⁻¹ := by
  have h : 0 ≤ (x - 1) ^ 2 / x := by positivity
  have e : (x - 1) ^ 2 / x = x + x⁻¹ - 2 := by
    field_simp
    ring
  linarith

/-- **`n ≤ [n]_q`** for `q > 0`. -/
theorem qint_ge_n (n : ℕ) {q : ℝ} (hq : 0 < q) : (n : ℝ) ≤ qint n q := by
  have h2 : 2 * qint n q = ∑ k ∈ range n,
      (q ^ ((n : ℤ) - 1 - 2 * k) + q ^ (-((n : ℤ) - 1 - 2 * k))) := by
    rw [sum_add_distrib, ← qint_reflect]
    unfold qint
    ring
  have hterm : ∀ k ∈ range n,
      (2 : ℝ) ≤ q ^ ((n : ℤ) - 1 - 2 * k) + q ^ (-((n : ℤ) - 1 - 2 * k)) := by
    intro k _
    rw [zpow_neg]
    exact add_inv_ge_two (zpow_pos hq _)
  have hsum : ∑ _k ∈ range n, (2 : ℝ) ≤ ∑ k ∈ range n,
      (q ^ ((n : ℤ) - 1 - 2 * k) + q ^ (-((n : ℤ) - 1 - 2 * k))) :=
    sum_le_sum hterm
  simp only [sum_const, card_range, nsmul_eq_mul] at hsum
  linarith

/-- **`[n]_q ≤ n · q^{n−1}`** for `q ≥ 1`. -/
theorem qint_le (n : ℕ) {q : ℝ} (hq : 1 ≤ q) :
    qint n q ≤ n * q ^ ((n : ℤ) - 1) := by
  unfold qint
  have hterm : ∀ k ∈ range n, q ^ ((n : ℤ) - 1 - 2 * k) ≤ q ^ ((n : ℤ) - 1) := by
    intro k _
    exact zpow_le_zpow_right₀ hq (by omega)
  calc ∑ k ∈ range n, q ^ ((n : ℤ) - 1 - 2 * k)
      ≤ ∑ _k ∈ range n, q ^ ((n : ℤ) - 1) := sum_le_sum hterm
    _ = n * q ^ ((n : ℤ) - 1) := by simp [sum_const, card_range, nsmul_eq_mul]

/-- **`q^{n−1} ≤ [n]_q`** for `q > 0` and `n ≥ 1` (the `k = 0` term). -/
theorem qint_ge_pow {n : ℕ} (hn : 1 ≤ n) {q : ℝ} (hq : 0 < q) :
    q ^ ((n : ℤ) - 1) ≤ qint n q := by
  unfold qint
  have h0 : (0 : ℕ) ∈ range n := mem_range.mpr (by omega)
  have := single_le_sum (f := fun k : ℕ => q ^ ((n : ℤ) - 1 - 2 * k))
    (fun k _ => (zpow_pos hq _).le) h0
  simpa using this

/-- The Plancherel volume of the label ball of radius `n`. -/
noncomputable def vol (n : ℕ) (q : ℝ) : ℝ := ∑ m ∈ range n, qint (m + 1) q ^ 2

/-- **Cubic floor**: `V(n) ≥ Σ_{m ≤ n} m²`, the `q = 1` (Euclidean, Kirillov)
volume, which grows like `n³/3`. -/
theorem vol_ge_classical (n : ℕ) {q : ℝ} (hq : 0 < q) :
    ∑ m ∈ range n, ((m : ℝ) + 1) ^ 2 ≤ vol n q := by
  unfold vol
  refine sum_le_sum (fun m _ => ?_)
  have h := qint_ge_n (m + 1) hq
  push_cast at h
  have h0 : (0 : ℝ) ≤ (m : ℝ) + 1 := by positivity
  exact pow_le_pow_left₀ h0 h 2

/-- **Exponential floor** for `q > 1`: `V(n) ≥ q^{2(n−1)}`. -/
theorem vol_ge_exp {n : ℕ} (hn : 1 ≤ n) {q : ℝ} (hq : 0 < q) :
    (q ^ ((n : ℤ) - 1)) ^ 2 ≤ vol n q := by
  unfold vol
  have hmem : n - 1 ∈ range n := mem_range.mpr (by omega)
  have hle := single_le_sum (f := fun m : ℕ => qint (m + 1) q ^ 2)
    (fun m _ => sq_nonneg _) hmem
  have hq1 := qint_ge_pow (n := n - 1 + 1) (by omega) hq
  have hcast : ((n - 1 + 1 : ℕ) : ℤ) - 1 = (n : ℤ) - 1 := by omega
  rw [hcast] at hq1
  have hpos : 0 ≤ q ^ ((n : ℤ) - 1) := (zpow_pos hq _).le
  calc (q ^ ((n : ℤ) - 1)) ^ 2 ≤ qint (n - 1 + 1) q ^ 2 := pow_le_pow_left₀ hpos hq1 2
    _ ≤ _ := hle

end QOU.Optimization.QIntGrowth
