import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# The rounded water-fill: why the excess `M_n − A√(2n)` is bounded

This file carries the order-theoretic steps that turn the `O(n^{1/4})` error of
`HardWallProjection.lean` into `O(1)` (bean `qou-fxym`; probe
`computations/deltalambda/rev_bounded_excess_upper_bound_probe.py`).

The `n^{1/4}` had two sources, and each is removed by one discrete statement:

* **Integrality defect.** The continuous water-fill `p` is not on the half-integer grid, and
  rounding it cost an energy defect `l/4` that a loss linear in `‖t − p‖` could exploit for free.
  Comparing instead with the **rounded** water-fill `q` (flat values in `{a, a+1}`, wall values
  `≥ a`), `rounded_pythagoras` gives the exact discrete exchange inequality
  `Σ t² ≥ Σ q² + Σ (t − q)² − Σ |t − q|`: the energy is `≥ Σ (dᵢ² − |dᵢ|)` with `d = t − q`
  **integer**, separable per coordinate. `int_tradeoff` then bounds each coordinate's net gain
  by `ωᵢ + ωᵢ²/(2L)`, and `Σ ωᵢ` is a convergent constant — no `√l` survives.
* **Row-count slack.** #7185's `2(H_l^min − H_min) ≥ (l − k)² − r` lets `l` exceed `k` by `√r`
  rows for free. Writing the hook sum as the linear cell functional `H(λ) = Σ_{(i,j) ∈ λ} (i+j−1)`,
  `diagonal_exchange` gives `H(λ) − H_greedy ≥ Σ_{d ≥ k+2} aₐ (d − k − 1)`, and an `l`-row shape
  has one cell on every diagonal `d ≤ l` (its first column), so `H − H_min ≥ T_{l−k−1}` with no
  `r`. `extra_rows_tradeoff` then caps the gain of extra rows by `(A + L/2)²/(2L)`.

All statements are over an ordered commutative ring / field with no reference to `ε`, `q₀` or
partitions (§7c). The assembly into `M_n ≤ A k + K₂` is checked per shape by the probe and written
out in its docstring; it is not proved here.
-/

namespace QOU.BraidKnot.RoundedWaterfillExchange

open Finset

variable {ι R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Discrete (rounded water-fill) Pythagoras.** If every `q i ≥ a`, every coordinate where
`t` lies strictly below `q` has `q i ≤ a + 1`, and the sums agree, then
`Σ q² + Σ (t − q)² − Σ |t − q| ≤ Σ t²`. -/
theorem rounded_pythagoras (s : Finset ι) (t q : ι → R) (a : R)
    (hlow : ∀ i ∈ s, a ≤ q i) (hflat : ∀ i ∈ s, t i < q i → q i ≤ a + 1)
    (hsum : ∑ i ∈ s, t i = ∑ i ∈ s, q i) :
    ∑ i ∈ s, q i ^ 2 + ∑ i ∈ s, (t i - q i) ^ 2 - ∑ i ∈ s, |t i - q i| ≤ ∑ i ∈ s, t i ^ 2 := by
  -- termwise: (q − a)(t − q) ≥ min (t − q) 0
  have hterm : ∀ i ∈ s, min (t i - q i) 0 ≤ (q i - a) * (t i - q i) := by
    intro i hi
    rcases le_or_gt (q i) (t i) with h | h
    · have h1 : 0 ≤ q i - a := by linarith [hlow i hi]
      have h2 : 0 ≤ t i - q i := by linarith
      exact le_trans (min_le_right _ _) (mul_nonneg h1 h2)
    · have hq1 := hflat i hi h
      have h1 : 0 ≤ q i - a := by linarith [hlow i hi]
      have h3 : q i - a ≤ 1 := by linarith
      have hneg : t i - q i < 0 := by linarith
      have : (t i - q i) ≤ (q i - a) * (t i - q i) := by nlinarith
      exact le_trans (min_le_left _ _) this
  have hS : ∑ i ∈ s, min (t i - q i) 0 ≤ ∑ i ∈ s, (q i - a) * (t i - q i) := sum_le_sum hterm
  have hzero : ∑ i ∈ s, (t i - q i) = 0 := by rw [sum_sub_distrib, hsum, sub_self]
  -- |x| = x − 2 min x 0
  have habs : ∑ i ∈ s, |t i - q i| = ∑ i ∈ s, (t i - q i) - 2 * ∑ i ∈ s, min (t i - q i) 0 := by
    rw [mul_sum, ← sum_sub_distrib]
    refine sum_congr rfl (fun i _ => ?_)
    rcases le_or_gt 0 (t i - q i) with h | h
    · rw [abs_of_nonneg h, min_eq_right h]; ring
    · rw [abs_of_neg h, min_eq_left h.le]; ring
  -- Σ t² − Σ q² − Σ d² = 2 Σ (q − a) d + 2 a Σ d
  have hexp : ∑ i ∈ s, t i ^ 2 - (∑ i ∈ s, q i ^ 2 + ∑ i ∈ s, (t i - q i) ^ 2)
      = 2 * ∑ i ∈ s, (q i - a) * (t i - q i) + 2 * a * ∑ i ∈ s, (t i - q i) := by
    rw [mul_sum, mul_sum, ← sum_add_distrib, ← sum_add_distrib, ← sum_sub_distrib]
    refine sum_congr rfl (fun i _ => ?_)
    ring
  rw [hzero, mul_zero, add_zero] at hexp
  rw [hzero, zero_sub] at habs
  linarith

/-- **Per-coordinate trade-off on the integer grid.** For `x ∈ ℕ`, a gain `ω x` against the
discrete energy `(L/2)(x² − x)` is at most `ω + ω²/(2L)`. -/
theorem int_tradeoff {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (ω L : F) (x : ℕ) (hω : 0 ≤ ω) (hL : 0 < L) :
    ω * x - L / 2 * ((x : F) ^ 2 - x) ≤ ω + ω ^ 2 / (2 * L) := by
  have hL2 : 0 < 2 * L := by linarith
  have hq : 0 ≤ ω ^ 2 / (2 * L) := div_nonneg (sq_nonneg ω) hL2.le
  rcases Nat.eq_zero_or_pos x with h | h
  · subst h; simp; linarith
  · -- e = x − 1 ≥ 0
    obtain ⟨e, rfl⟩ : ∃ e, x = e + 1 := ⟨x - 1, by omega⟩
    push_cast
    have he : (0 : F) ≤ e := Nat.cast_nonneg e
    have key : ω * e - L / 2 * (e : F) ^ 2 ≤ ω ^ 2 / (2 * L) := by
      rw [le_div_iff₀ hL2]
      nlinarith [sq_nonneg (L * e - ω)]
    have : L / 2 * (e : F) * 1 ≥ 0 := by
      have : (0 : F) ≤ L / 2 := by linarith
      nlinarith
    nlinarith

/-- **Diagonal exchange.** Let `a d` (cells of a shape on anti-diagonal `d`) and `o d` (the greedy
fill: full diagonals up to `k`, partial at `k+1`, empty beyond) have the same total, with
`a d ≤ o d` for `d ≤ k` and `o d = 0` for `d ≥ k + 2`. Then the weighted excess is at least the
cost of the cells beyond diagonal `k + 1`:
`Σ (a d − o d)·d ≥ Σ_{d ≥ k+2} a d · (d − k − 1)`. -/
theorem diagonal_exchange (N k : ℕ) (a o : ℕ → R)
    (hsum : ∑ d ∈ range N, a d = ∑ d ∈ range N, o d)
    (hlow : ∀ d ∈ range N, d ≤ k → a d ≤ o d)
    (hhigh : ∀ d ∈ range N, k + 2 ≤ d → o d = 0) :
    ∑ d ∈ range N, (if k + 2 ≤ d then a d * ((d : R) - (k + 1)) else 0)
      ≤ ∑ d ∈ range N, (a d - o d) * (d : R) := by
  have hzero : ∑ d ∈ range N, (a d - o d) = 0 := by rw [sum_sub_distrib, hsum, sub_self]
  have hshift : ∑ d ∈ range N, (a d - o d) * (d : R)
      = ∑ d ∈ range N, (a d - o d) * ((d : R) - (k + 1)) := by
    have : ∑ d ∈ range N, (a d - o d) * ((d : R) - (k + 1))
        = ∑ d ∈ range N, (a d - o d) * (d : R) - (k + 1) * ∑ d ∈ range N, (a d - o d) := by
      rw [mul_sum, ← sum_sub_distrib]
      exact sum_congr rfl (fun d _ => by ring)
    rw [this, hzero, mul_zero, sub_zero]
  rw [hshift]
  apply sum_le_sum
  intro d hd
  by_cases h2 : k + 2 ≤ d
  · rw [if_pos h2, hhigh d hd h2, sub_zero]
  · rw [if_neg h2]
    by_cases h1 : d ≤ k
    · have ha := hlow d hd h1
      have hdk : (d : R) - (k + 1) ≤ 0 := by
        have : (d : R) ≤ k := by exact_mod_cast h1
        linarith
      have : a d - o d ≤ 0 := by linarith
      nlinarith
    · -- d = k + 1: the weight vanishes
      have hd1 : d = k + 1 := by omega
      subst hd1
      push_cast
      simp

/-- **Extra rows.** `j` rows beyond `k` gain `j A` and cost at least `(L/2) j (j − 1)` of hook
energy; the net is at most `(A + L/2)²/(2L)`. -/
theorem extra_rows_tradeoff {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (A L j : F) (hL : 0 < L) :
    j * A - L / 2 * (j * (j - 1)) ≤ (A + L / 2) ^ 2 / (2 * L) := by
  have hL2 : 0 < 2 * L := by linarith
  rw [le_div_iff₀ hL2]
  nlinarith [sq_nonneg (L * j - (A + L / 2))]

/-- Subtracting the net extra-row gain from the quadratic ceiling yields a non-negative difference. -/
theorem extra_rows_tradeoff_sub_nonneg {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (A L j : F) (hL : 0 < L) :
    0 ≤ (A + L / 2) ^ 2 / (2 * L) - (j * A - L / 2 * (j * (j - 1))) :=
  sub_nonneg.mpr (extra_rows_tradeoff A L j hL)

end QOU.BraidKnot.RoundedWaterfillExchange
