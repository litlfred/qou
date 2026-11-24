import Mathlib.Algebra.Field.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Order.Filter.AtTopBot.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.BraidsAndKnots.ContentVarianceLeadingConstant — the partial-fraction step of `v_A = 8/π²`

The leading constant of the descent-DPP variance of `Σ|c|` is `v_A = 8/π²`
(`docs/audits/2026-08-29-covariance-kernel-M1-tvok-leading-constant-vA.md`, machinery task
`qou-tvok`, epic `qou-h315`). Its derivation reduces — via the IO Kerov CLT and the elementary
closed form `Â_{2m+1} = 8(−1)^{m+1}/(π((2m+1)²−4))` — to the rational-series identity

    Σ_{n odd ≥ 1} 1/[n(n²−4)²] = 1/8,

which is proved by **partial fractions + telescoping** (both the divergent `Σ1/odd` linear tail and
the `π²/8` quadratic tail cancel exactly, leaving `1/16 + 1/16`).

This file formalizes the **algebraic heart** of that step — the partial-fraction identity itself, a
sorry-free `field_simp; ring` fact over any field. It is deliberately scoped: it proves the *summand
decomposition*, **not** the infinite sum (`= 1/8`, a `tsum` telescoping) and **not** `v_A = 8/π²`
(which also invokes the cited IO CLT). Stated over a generic characteristic-zero field (§7c — no `ℝ`;
the identity is purely algebraic, needing only `char ≠ 2` so that `16, 32 ≠ 0`); the reals instantiate
it at use. -/

namespace QOU.BraidsAndKnots.ContentVarianceLeadingConstant

/-- **Partial-fraction decomposition of the `v_A` summand (sorry-free).**

For `x ≠ 0, 2, −2` in any field,

    1/(x(x²−4)²) = 1/(16x) − 1/(32(x−2)) − 1/(32(x+2)) + 1/(32(x−2)²) − 1/(32(x+2)²).

This is the elementary identity underlying `Σ_{n odd} 1/[n(n²−4)²] = 1/8`: summed over odd `n`, the
`1/(16x)`, `1/(x∓2)` linear parts telescope (the divergent tail cancels, coefficient
`1/16 − 1/32 − 1/32 = 0`) and the `1/(x∓2)²` quadratic parts telescope (the `π²/8` tail cancels),
leaving the rational value `1/8`. Here only the per-term algebra is asserted. -/
theorem vA_summand_partial_fractions {K : Type*} [Field K] [CharZero K] (x : K)
    (hx : x ≠ 0) (h2 : x - 2 ≠ 0) (h2' : x + 2 ≠ 0) :
    1 / (x * (x ^ 2 - 4) ^ 2)
      = 1 / (16 * x) - 1 / (32 * (x - 2)) - 1 / (32 * (x + 2))
        + 1 / (32 * (x - 2) ^ 2) - 1 / (32 * (x + 2) ^ 2) := by
  have hx2 : x ^ 2 - 4 = (x - 2) * (x + 2) := by ring
  rw [hx2]
  field_simp
  ring

/-! ## The infinite sum, which the header above scoped OUT

That scoping note says this file proves the summand decomposition "**not** the
infinite sum (`= 1/8`, a `tsum` telescoping)". It is proved here.

The telescoping is done exactly, as a closed form for EVERY partial sum rather
than as a limit argument: with `n = 2k+1`,

    ∑_{k < N} 1/(n(n²−4)²)
      = 1/8 + (1/32)( 1/(2N−1) − 1/(2N+1) − 1/(2N−1)² − 1/(2N+1)² ).

Both tails the header describes are visible in that one line: the linear parts
contribute `1/(2N∓1)` and the quadratic parts `1/(2N∓1)²`, and all four vanish
as `N → ∞`, leaving `1/8`. The formula holds at `N = 0` too — the four
correction terms sum to `−4/32 = −1/8` there, cancelling the `1/8` exactly — so
no positivity side condition is needed anywhere.

`2N − 1` is never zero for a natural `N` (it is `−1` at `N = 0` and odd
thereafter), which is what makes the single closed form legitimate across the
whole range. -/

/-- The `v_A` summand at the odd integer `n = 2k + 1`. -/
noncomputable def vaTerm (k : ℕ) : ℝ :=
  1 / ((2 * k + 1) * ((2 * k + 1) ^ 2 - 4) ^ 2)

private theorem two_mul_sub_one_ne (N : ℕ) : (2 * (N : ℝ) - 1) ≠ 0 := by
  rcases N with _ | M
  · norm_num
  · push_cast
    have : (0 : ℝ) ≤ (M : ℝ) := Nat.cast_nonneg M
    intro h
    linarith

private theorem two_mul_add_ne (N : ℕ) (c : ℝ) (hc : 0 < c) :
    (2 * (N : ℝ) + c) ≠ 0 := by
  have : (0 : ℝ) ≤ (N : ℝ) := Nat.cast_nonneg N
  intro h
  linarith

/-- **Closed form for every partial sum — the telescoping, exactly.** -/
theorem sum_range_vaTerm (N : ℕ) :
    ∑ k ∈ Finset.range N, vaTerm k
      = 1 / 8 + (1 / 32) * (1 / (2 * (N : ℝ) - 1) - 1 / (2 * (N : ℝ) + 1)
          - 1 / (2 * (N : ℝ) - 1) ^ 2 - 1 / (2 * (N : ℝ) + 1) ^ 2) := by
  induction N with
  | zero => norm_num
  | succ N ih =>
    rw [Finset.sum_range_succ, ih]
    have h1 : (2 * (N : ℝ) - 1) ≠ 0 := two_mul_sub_one_ne N
    have h2 : (2 * (N : ℝ) + 1) ≠ 0 := two_mul_add_ne N 1 one_pos
    have h3 : (2 * (N : ℝ) + 3) ≠ 0 := two_mul_add_ne N 3 (by norm_num)
    have hfac : ((2 * (N : ℝ) + 1) ^ 2 - 4) = (2 * (N : ℝ) - 1) * (2 * (N : ℝ) + 3) := by
      ring
    simp only [vaTerm, Nat.cast_succ]
    rw [show (2 * ((N : ℝ) + 1) - 1) = 2 * (N : ℝ) + 1 by ring,
      show (2 * ((N : ℝ) + 1) + 1) = 2 * (N : ℝ) + 3 by ring, hfac]
    field_simp
    ring

/-- Every partial sum is at most `1/8`. The four correction terms are
collectively non-positive, and the reason is AM-GM: writing `x = 1/(2M+1)`,
`y = 1/(2M+3)`, the linear part is exactly `x - y = 2xy` and the quadratic part
is `x² + y² ≥ 2xy`. -/
private theorem sum_range_vaTerm_le (N : ℕ) : ∑ k ∈ Finset.range N, vaTerm k ≤ 1 / 8 := by
  rw [sum_range_vaTerm]
  rcases N with _ | M
  · norm_num
  · have hM : (0 : ℝ) ≤ (M : ℝ) := Nat.cast_nonneg M
    push_cast
    rw [show (2 * ((M : ℝ) + 1) - 1) = 2 * (M : ℝ) + 1 by ring,
      show (2 * ((M : ℝ) + 1) + 1) = 2 * (M : ℝ) + 3 by ring]
    have hA : (0 : ℝ) < 2 * (M : ℝ) + 1 := by linarith
    have hB : (0 : ℝ) < 2 * (M : ℝ) + 3 := by linarith
    have hlin : 1 / (2 * (M : ℝ) + 1) - 1 / (2 * (M : ℝ) + 3)
        = 2 * ((1 / (2 * (M : ℝ) + 1)) * (1 / (2 * (M : ℝ) + 3))) := by
      field_simp
      ring
    have hsq : 2 * ((1 / (2 * (M : ℝ) + 1)) * (1 / (2 * (M : ℝ) + 3)))
        ≤ (1 / (2 * (M : ℝ) + 1)) ^ 2 + (1 / (2 * (M : ℝ) + 3)) ^ 2 := by
      nlinarith [sq_nonneg (1 / (2 * (M : ℝ) + 1) - 1 / (2 * (M : ℝ) + 3))]
    have e1 : 1 / (2 * (M : ℝ) + 1) ^ 2 = (1 / (2 * (M : ℝ) + 1)) ^ 2 := by
      rw [one_div, one_div, inv_pow]
    have e2 : 1 / (2 * (M : ℝ) + 3) ^ 2 = (1 / (2 * (M : ℝ) + 3)) ^ 2 := by
      rw [one_div, one_div, inv_pow]
    rw [e1, e2]
    linarith

/-- **`Σ_{n odd ≥ 1} 1/(n(n²−4)²) = 1/8`** — the identity the header scoped out,
and the one the `v_A = 8/π²` derivation reduces to. -/
theorem vaTerm_hasSum : HasSum vaTerm (1 / 8 : ℝ) := by
  have hnn : ∀ k, 0 ≤ vaTerm k := by
    intro k
    unfold vaTerm
    positivity
  have hsummable : Summable vaTerm :=
    summable_of_sum_range_le hnn sum_range_vaTerm_le
  refine (hsummable.hasSum_iff_tendsto_nat).mpr ?_
  simp only [sum_range_vaTerm]
  have hA : Filter.Tendsto (fun N : ℕ => 2 * (N : ℝ) - 1) Filter.atTop Filter.atTop := by
    apply Filter.tendsto_atTop_add_const_right
    exact Filter.Tendsto.const_mul_atTop (by norm_num) tendsto_natCast_atTop_atTop
  have hB : Filter.Tendsto (fun N : ℕ => 2 * (N : ℝ) + 1) Filter.atTop Filter.atTop := by
    apply Filter.tendsto_atTop_add_const_right
    exact Filter.Tendsto.const_mul_atTop (by norm_num) tendsto_natCast_atTop_atTop
  have zA := hA.inv_tendsto_atTop
  have zB := hB.inv_tendsto_atTop
  have zA2 := (hA.atTop_mul_atTop₀ hA).inv_tendsto_atTop
  have zB2 := (hB.atTop_mul_atTop₀ hB).inv_tendsto_atTop
  simp only [one_div, ← inv_pow]
  have : Filter.Tendsto
      (fun N : ℕ => (1:ℝ)/8 + (1/32) * ((2*(N:ℝ)-1)⁻¹ - (2*(N:ℝ)+1)⁻¹
        - ((2*(N:ℝ)-1)⁻¹)^2 - ((2*(N:ℝ)+1)⁻¹)^2)) Filter.atTop (nhds (1/8)) := by
    have h := (((zA.sub zB).sub (zA.pow 2)).sub (zB.pow 2)).const_mul (1/32 : ℝ)
    simpa using (h.const_add ((1:ℝ)/8))
  simpa using this

end QOU.BraidsAndKnots.ContentVarianceLeadingConstant
