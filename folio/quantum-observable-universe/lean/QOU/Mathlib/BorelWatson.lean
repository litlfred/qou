/-
  Watson-uniqueness brick 2 — Gevrey-1 remainder ⇒ exp(−1/x) decay
  (bean el8w tranche 5), split across the substrate→archimedean wall (§7c).

  Watson / Nevanlinna–Sokal uniqueness reduces to: a Gevrey-1 remainder bound
  `∀N, a ≤ C·N!·xᴺ` forces `a` to be exponentially small, `a ≲ e^{−1/x}`. That
  exponential smallness (beating every polynomial) is what a >π-sector
  Phragmén–Lindelöf argument (brick 3) turns into uniqueness.

  The brick splits cleanly at the §7c wall — answering "what of this is
  pre-archimedean":

    * PRE-ARCHIMEDEAN (order-theoretic, generic `LinearOrderedField`, no `exp`,
      no completeness): WHERE the least term sits. The truncation sequence
      `t_N = N!·xᴺ` has ratio `t_{N+1}/t_N = (N+1)x`, so it stops decreasing
      exactly when `(N+1)x > 1` — the least term is at `N ≈ 1/x`. This index
      selection is `factorialPow_succ_le_iff`, valid over any ordered field.
    * ARCHIMEDEAN (ℝ — genuinely needs `Real.exp`, Stirling, completeness): the
      VALUE of that least term is `e^{−1/x}`. This is `gevrey1_remainder_expDecay`,
      built on brick 1 (`factorial_le_stirling_upper`).

  This is exactly the two-layer convention: the fibre carries the formal
  truncation combinatorics; the archimedean functor turns the least term into
  the number `e^{−1/x}`.

  -- Ref: [sokal1980] https://doi.org/10.1063/1.524408
  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness brick 2
-/

import QOU.Mathlib.StirlingUpperBound

namespace QOU.Mathlib.Borel

open scoped Nat
open Real

/-! ### Pre-archimedean: the least-term index (generic ordered field) -/

/-- **Least-term index (pre-archimedean).** For `0 < x` in any linearly
    ordered field, the truncation term `t_N = N!·xᴺ` stops decreasing exactly
    when `(N+1)·x > 1`: `t_{N+1} ≤ t_N ↔ (N+1)·x ≤ 1`. No `exp`, no
    completeness — pure order theory; the least term therefore sits at
    `N ≈ 1/x`. -/
theorem factorialPow_succ_le_iff {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {x : K} (hx : 0 < x) (N : ℕ) :
    ((N + 1)! : K) * x ^ (N + 1) ≤ (N ! : K) * x ^ N ↔ ((N : K) + 1) * x ≤ 1 := by
  have hpos : (0 : K) < (N ! : K) * x ^ N := by positivity
  have hstep : ((N + 1)! : K) * x ^ (N + 1)
      = (((N : K) + 1) * x) * ((N ! : K) * x ^ N) := by
    rw [Nat.factorial_succ, pow_succ]
    push_cast
    ring
  rw [hstep]
  constructor
  · intro h
    have := (mul_le_iff_le_one_left hpos).mp (by rwa [mul_comm] at h)
    exact this
  · intro h
    calc (((N : K) + 1) * x) * ((N ! : K) * x ^ N)
        ≤ 1 * ((N ! : K) * x ^ N) := by gcongr
      _ = (N ! : K) * x ^ N := one_mul _

/-! ### Archimedean: the least-term value is `e^{−1/x}` (ℝ, Stirling) -/

/-- **Gevrey-1 remainder ⇒ exponential decay (archimedean).** If a nonnegative
    real `a` is dominated by the Gevrey-1 truncation bound `a ≤ C·N!·xᴺ` for
    *every* `N`, then `a` is exponentially small:
    `a ≤ C·e²·x^{-1/2}·e^{−1/x}` for `0 < x ≤ 1`. Evaluating the bound at the
    least-term index `N = ⌊1/x⌋` and applying brick 1
    (`factorial_le_stirling_upper`, `N! ≤ e√N(N/e)ᴺ`) collapses `(Nx/e)ᴺ` to
    `e^{−N} ≤ e·e^{−1/x}`. This is the analytic heart of Watson uniqueness —
    exponential (super-polynomial) smallness that a >π-sector
    Phragmén–Lindelöf argument (brick 3) turns into `a = 0`. -/
theorem gevrey1_remainder_expDecay {C x a : ℝ}
    (hC : 0 ≤ C) (hx0 : 0 < x) (hx1 : x ≤ 1) (_ha : 0 ≤ a)
    (hbound : ∀ N : ℕ, a ≤ C * (N ! : ℝ) * x ^ N) :
    a ≤ C * Real.exp 2 / Real.sqrt x * Real.exp (-1 / x) := by
  set N : ℕ := ⌊x⁻¹⌋₊ with hNdef
  have hxinv0 : 0 < x⁻¹ := inv_pos.mpr hx0
  have hxinv1 : 1 ≤ x⁻¹ := (one_le_inv₀ hx0).mpr hx1
  have hN1 : 1 ≤ N := Nat.le_floor (by exact_mod_cast hxinv1)
  have hNle : (N : ℝ) ≤ x⁻¹ := Nat.floor_le hxinv0.le
  have hNgt : x⁻¹ - 1 < (N : ℝ) := by
    have := Nat.lt_floor_add_one (x⁻¹); push_cast at this ⊢; linarith
  have hNx : (N : ℝ) * x ≤ 1 := by
    have := mul_le_mul_of_nonneg_right hNle hx0.le
    rwa [inv_mul_cancel₀ hx0.ne'] at this
  -- sub-bound A: (Nx/e)^N ≤ (1/e)^N
  have hbase : (0 : ℝ) ≤ (N : ℝ) * x / Real.exp 1 := by positivity
  have hbase_le : (N : ℝ) * x / Real.exp 1 ≤ 1 / Real.exp 1 := by gcongr
  have hpowA : ((N : ℝ) * x / Real.exp 1) ^ N ≤ (1 / Real.exp 1) ^ N :=
    pow_le_pow_left₀ hbase hbase_le N
  -- sub-bound B: (1/e)^N = exp(-N)
  have hpowB : (1 / Real.exp 1) ^ N = Real.exp (-(N : ℝ)) := by
    rw [one_div, ← Real.exp_neg, ← Real.exp_nat_mul, mul_neg_one]
  -- sub-bound C: exp(-N) ≤ e · exp(-1/x)
  have hexpC : Real.exp (-(N : ℝ)) ≤ Real.exp 1 * Real.exp (-1 / x) := by
    rw [← Real.exp_add]
    apply Real.exp_le_exp.mpr
    rw [neg_div]
    have : (x⁻¹ : ℝ) = 1 / x := by rw [one_div]
    linarith [hNgt, this ▸ hNgt]
  -- sub-bound D: √N ≤ 1/√x
  have hsqrtD : Real.sqrt N ≤ 1 / Real.sqrt x := by
    rw [one_div, ← Real.sqrt_inv]
    exact Real.sqrt_le_sqrt hNle
  -- assemble
  calc a ≤ C * (N ! : ℝ) * x ^ N := hbound N
    _ ≤ C * (Real.exp 1 * Real.sqrt N * ((N : ℝ) / Real.exp 1) ^ N) * x ^ N := by
        gcongr; exact factorial_le_stirling_upper hN1
    _ = C * Real.exp 1 * Real.sqrt N * (((N : ℝ) * x / Real.exp 1) ^ N) := by ring
    _ ≤ C * Real.exp 1 * Real.sqrt N * (1 / Real.exp 1) ^ N := by gcongr
    _ = C * Real.exp 1 * Real.sqrt N * Real.exp (-(N : ℝ)) := by rw [hpowB]
    _ ≤ C * Real.exp 1 * (1 / Real.sqrt x) * (Real.exp 1 * Real.exp (-1 / x)) := by
        gcongr
    _ = C * Real.exp 2 / Real.sqrt x * Real.exp (-1 / x) := by
        rw [show (2 : ℝ) = 1 + 1 by norm_num, Real.exp_add]; ring

end QOU.Mathlib.Borel
