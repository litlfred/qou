import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-!
# The hard-wall reference: why the pair-term loss is paid by the energy

This file carries the three non-trivial order-theoretic steps of the sharp-coefficient upper bound
`M_n ≤ A √(2n) + O(n^{1/4})` (bean `qou-fxym`; probe
`computations/deltalambda/rev_sharp_coefficient_upper_bound_probe.py`).

In the completed-square coordinates of `HookSumCompletedSquare.lean`, an `l`-row partition is a
vector `t` with `t i ≥ w i` (the hard wall `β_l ≥ 1`) and fixed sum, and `2H = Σ t² − Σ m²`. The
pair term loses at most `Σ_k |ε'(2k)| Δ_k(t)` against the staircase, with
`Δ_k(v) = Σ_{i<l-k} (v i − v (i+k))`. The argument compares `t` with the **water-filling**
reference `p i = max τ (w i)`:

* `waterfill_pythagoras` — `Σ p² + Σ (t − p)² ≤ Σ t²` for every `t` above the wall with the same
  sum. (`p` is the Euclidean projection of `0` onto that convex set; the proof is the variational
  inequality written out, with no appeal to projections.)
* `shiftDiff_nonpos_of_monotone` — `p` is monotone, so `Δ_k(p) ≤ 0`: the reference itself never
  widens a mean neighbour distance, hence carries no pair-term loss.
* `linear_sub_excess_le` — the scalar trade-off: a loss linear in `y = ‖t − p‖` against an energy
  `(L/2)·max(0, y² − y₀²)` is at most `c·y₀ + c²/(2L)`. With `y₀² = l/4` (the integrality defect
  of rounding `p` to the half-integer grid) this is `O(√l) = O(n^{1/4})`, which is where the
  error term of the bound comes from and why it is not `O(1)`.

All three are stated over an ordered commutative ring / field with no reference to `ε`, `q₀` or
partitions (§7c); the archimedean content enters only at the probe. Nothing here proves the
composition into the bound on `M_n` — that assembly is checked numerically, per shape, by S6 of the
probe, and is written out in the probe's docstring.
-/

namespace QOU.BraidKnot.HardWallProjection

open Finset

variable {ι R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Water-filling Pythagoras.** If `p i = max τ (w i)` on `s`, `t` lies above the wall `w`, and
`t`, `p` have the same sum, then `Σ p² + Σ (t − p)² ≤ Σ t²`. -/
theorem waterfill_pythagoras (s : Finset ι) (t p w : ι → R) (τ : R)
    (hp : ∀ i ∈ s, p i = max τ (w i)) (ht : ∀ i ∈ s, w i ≤ t i)
    (hsum : ∑ i ∈ s, t i = ∑ i ∈ s, p i) :
    ∑ i ∈ s, p i ^ 2 + ∑ i ∈ s, (t i - p i) ^ 2 ≤ ∑ i ∈ s, t i ^ 2 := by
  -- Σ t² − Σ p² − Σ (t−p)² = 2 Σ (p − τ)(t − p) + 2 τ Σ (t − p), and the last sum is 0.
  have hkey : ∀ i ∈ s, 0 ≤ (p i - τ) * (t i - p i) := by
    intro i hi
    rcases le_total (w i) τ with h | h
    · have : p i = τ := by rw [hp i hi]; exact max_eq_left h
      rw [this]; simp
    · have hpw : p i = w i := by rw [hp i hi]; exact max_eq_right h
      have h1 : 0 ≤ p i - τ := by rw [hpw]; linarith
      have h2 : 0 ≤ t i - p i := by rw [hpw]; linarith [ht i hi]
      exact mul_nonneg h1 h2
  have hS : 0 ≤ ∑ i ∈ s, (p i - τ) * (t i - p i) := sum_nonneg hkey
  have hzero : ∑ i ∈ s, (t i - p i) = 0 := by rw [sum_sub_distrib, hsum, sub_self]
  have hexp : ∑ i ∈ s, t i ^ 2 - (∑ i ∈ s, p i ^ 2 + ∑ i ∈ s, (t i - p i) ^ 2)
      = 2 * ∑ i ∈ s, (p i - τ) * (t i - p i) + 2 * τ * ∑ i ∈ s, (t i - p i) := by
    rw [mul_sum, mul_sum, ← sum_add_distrib, ← sum_add_distrib, ← sum_sub_distrib]
    refine sum_congr rfl (fun i _ => ?_)
    ring
  rw [hzero, mul_zero, add_zero] at hexp
  linarith

/-- The neighbour-order-`k` difference `Δ_k(v) = Σ_{i < m} (v i − v (i+k))` of a monotone sequence
is non-positive: the water-filling reference never widens a mean `k`-th neighbour distance. -/
theorem shiftDiff_nonpos_of_monotone (v : ℕ → R) (hv : Monotone v) (m k : ℕ) :
    ∑ i ∈ range m, (v i - v (i + k)) ≤ 0 := by
  apply sum_nonpos
  intro i _
  have : v i ≤ v (i + k) := hv (Nat.le_add_right i k)
  linarith

/-- Linearity of `Δ_k`: `Δ_k(t) = Δ_k(p) + Δ_k(t − p)`. Combined with
`shiftDiff_nonpos_of_monotone`, `Δ_k(t) ≤ Δ_k(t − p)`, which Cauchy–Schwarz bounds by
`√(2 min(k, l−k))·‖t − p‖`. -/
theorem shiftDiff_le_of_reference (t p : ℕ → R) (hp : Monotone p) (m k : ℕ) :
    ∑ i ∈ range m, (t i - t (i + k)) ≤
      ∑ i ∈ range m, ((t i - p i) - (t (i + k) - p (i + k))) := by
  have h := shiftDiff_nonpos_of_monotone p hp m k
  have hsplit : ∑ i ∈ range m, (t i - t (i + k)) =
      ∑ i ∈ range m, (p i - p (i + k)) +
        ∑ i ∈ range m, ((t i - p i) - (t (i + k) - p (i + k))) := by
    rw [← sum_add_distrib]; exact sum_congr rfl (fun i _ => by ring)
  linarith

/-- **The scalar trade-off.** A loss `c·y` linear in the distance to the reference, against an
energy `(L/2)·max(0, y² − y₀²)`, is bounded by `c·y₀ + c²/(2L)` uniformly in `y ≥ 0`. -/
theorem linear_sub_excess_le {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (c L y y0 : F) (hc : 0 ≤ c) (hL : 0 < L) (hy : 0 ≤ y) (hy0 : 0 ≤ y0) :
    c * y - L / 2 * max 0 (y ^ 2 - y0 ^ 2) ≤ c * y0 + c ^ 2 / (2 * L) := by
  have hL2 : 0 < 2 * L := by linarith
  have hq : 0 ≤ c ^ 2 / (2 * L) := div_nonneg (sq_nonneg c) hL2.le
  have hLh : 0 ≤ L / 2 := by linarith
  rcases le_total y y0 with h | h
  · have hmax : 0 ≤ L / 2 * max 0 (y ^ 2 - y0 ^ 2) :=
      mul_nonneg hLh (le_max_left _ _)
    nlinarith [mul_le_mul_of_nonneg_left h hc]
  · have hmax : max 0 (y ^ 2 - y0 ^ 2) = y ^ 2 - y0 ^ 2 := by
      apply max_eq_right; nlinarith
    rw [hmax]
    -- c(y−y₀) − (L/2)(y−y₀)(y+y₀) ≤ c(y−y₀) − (L/2)(y−y₀)² ≤ c²/(2L)
    have hd : 0 ≤ y - y0 := by linarith
    have h1 : L / 2 * (y ^ 2 - y0 ^ 2) ≥ L / 2 * (y - y0) ^ 2 := by
      have : (y ^ 2 - y0 ^ 2) - (y - y0) ^ 2 = 2 * y0 * (y - y0) := by ring
      have h2 : 0 ≤ 2 * y0 * (y - y0) := mul_nonneg (by linarith) hd
      nlinarith [mul_nonneg hLh h2]
    have h4 : c * (y - y0) - L / 2 * (y - y0) ^ 2 ≤ c ^ 2 / (2 * L) := by
      rw [le_div_iff₀ hL2]
      nlinarith [sq_nonneg (L * (y - y0) - c)]
    nlinarith

/-- Rearranging the linear-versus-excess bound yields a nonnegative slack (`qou-kt8o`). -/
theorem linear_sub_excess_slack_nonneg {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (c L y y0 : F) (hc : 0 ≤ c) (hL : 0 < L) (hy : 0 ≤ y) (hy0 : 0 ≤ y0) :
    0 ≤ (c * y0 + c ^ 2 / (2 * L)) - (c * y - L / 2 * max 0 (y ^ 2 - y0 ^ 2)) :=
  sub_nonneg.mpr (linear_sub_excess_le c L y y0 hc hL hy hy0)

end QOU.BraidKnot.HardWallProjection
