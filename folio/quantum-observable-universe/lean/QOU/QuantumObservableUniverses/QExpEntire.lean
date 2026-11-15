import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Analysis.Complex.Basic

/-!
# QOU.QExpEntire — the q-exponential is entire (the Wick-rotation licence)

The categorical Wick rotation identifies the q-Laplace pairing
`s ↦ exp_q(s ·)` with the q-Fourier pairing `ξ ↦ exp_q(i ξ ·)` as a
single grouplike element evaluated on the real vs. imaginary axis
(`def:categorical-fourier`, `intro-q-resolvent-wick`,
`i-as-braiding-orientation`).  The identity `F(ξ) = L(iξ)` is
*definitional* once a single grouplike function is used; its
**falsifiable** content is that this function is defined on all of `ℂ`,
i.e. the q-exponential series converges everywhere (is entire).

This file proves exactly that, in the substrate regime `q > 1`
(`q₀ ≈ 1.11`): the series `∑ xⁿ / [n]_q!` is summable for every
`x : ℂ`.  If it had a finite radius of convergence the Wick rotation
would not be globally valid, so summability-everywhere — not the
tautological `F = L ∘ (i·)` — is the honest mathematical core.

Base ring: genuinely archimedean (`ℝ` growth bounds, `ℂ` series,
`tendsto_pow_atTop`), so `ℝ`/`ℂ` is correct here per §7c, not gratuitous.

LaTeX label: `prop:q-exp-entire`
-/

namespace QOU.QExp

open Filter Topology

noncomputable section

variable {q : ℝ}

/-- Balanced q-integer `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`. -/
def qNat (q : ℝ) (n : ℕ) : ℝ := (q ^ n - (q⁻¹) ^ n) / (q - q⁻¹)

/-- q-factorial `[n]_q! = ∏_{k=1}^{n} [k]_q`. -/
def qFact (q : ℝ) : ℕ → ℝ
  | 0 => 1
  | (n + 1) => qNat q (n + 1) * qFact q n

/-- `n`-th term of the q-exponential `∑ xⁿ / [n]_q!`. -/
def qExpTerm (q : ℝ) (x : ℂ) (n : ℕ) : ℂ := x ^ n / (qFact q n : ℂ)

@[simp] theorem qFact_zero : qFact q 0 = 1 := rfl

theorem qFact_succ (n : ℕ) : qFact q (n + 1) = qNat q (n + 1) * qFact q n := rfl

/-- For `q > 1` the denominator `q − q⁻¹` is positive. -/
theorem sub_inv_pos (hq : 1 < q) : 0 < q - q⁻¹ := by
  have hinv : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have : q⁻¹ < q := lt_trans hinv hq
  linarith

/-- The balanced q-integer of `n+1` dominates `qⁿ` (drop the positive tail). -/
theorem qNat_succ_ge (hq : 1 < q) (n : ℕ) : q ^ n ≤ qNat q (n + 1) := by
  have hqpos : 0 < q := lt_trans one_pos hq
  have hden : 0 < q - q⁻¹ := sub_inv_pos hq
  have hinv_pos : 0 < q⁻¹ := inv_pos.mpr hqpos
  have hinv_le : q⁻¹ ≤ q := le_trans (inv_le_one_of_one_le₀ hq.le) hq.le
  have hpow : (q⁻¹) ^ n ≤ q ^ n := pow_le_pow_left₀ hinv_pos.le hinv_le n
  rw [qNat, le_div_iff₀ hden]
  have h1 : (q⁻¹) ^ (n + 1) ≤ q ^ n * q⁻¹ := by
    rw [pow_succ]
    exact mul_le_mul_of_nonneg_right hpow hinv_pos.le
  have e1 : q ^ n * (q - q⁻¹) = q ^ (n + 1) - q ^ n * q⁻¹ := by
    rw [pow_succ]; ring
  rw [e1]; linarith

/-- The balanced q-integer of `n+1` is positive for `q > 1`. -/
theorem qNat_succ_pos (hq : 1 < q) (n : ℕ) : 0 < qNat q (n + 1) :=
  lt_of_lt_of_le (pow_pos (lt_trans one_pos hq) n) (qNat_succ_ge hq n)

/-- The q-factorial is positive for `q > 1`. -/
theorem qFact_pos (hq : 1 < q) : ∀ n, 0 < qFact q n
  | 0 => by simp
  | (n + 1) => by
    rw [qFact_succ]
    exact mul_pos (qNat_succ_pos hq n) (qFact_pos hq n)

/-- Norm of the `n`-th q-exponential term. -/
theorem norm_qExpTerm (hq : 1 < q) (x : ℂ) (n : ℕ) :
    ‖qExpTerm q x n‖ = ‖x‖ ^ n / qFact q n := by
  simp only [qExpTerm, norm_div, norm_pow, Complex.norm_real]
  rw [Real.norm_of_nonneg (qFact_pos hq n).le]

/-- **The q-exponential is entire.**  For `q > 1` the series
`∑ xⁿ / [n]_q!` is summable for every `x : ℂ` — the analytic fact that
licenses the categorical Wick rotation `F(ξ) = L(iξ)`. -/
theorem qExpTerm_summable (hq : 1 < q) (x : ℂ) : Summable (qExpTerm q x) := by
  have hx : (0 : ℝ) ≤ ‖x‖ := norm_nonneg x
  have htend : Tendsto (fun n : ℕ => q ^ n) atTop atTop :=
    tendsto_pow_atTop_atTop_of_one_lt hq
  have hev : ∀ᶠ n in atTop, 2 * ‖x‖ ≤ q ^ n :=
    htend.eventually_ge_atTop (2 * ‖x‖)
  refine summable_of_ratio_norm_eventually_le (r := 1 / 2) (by norm_num) ?_
  filter_upwards [hev] with n hn
  have hfn : 0 < qFact q n := qFact_pos hq n
  have hqnat : 0 < qNat q (n + 1) := qNat_succ_pos hq n
  -- `q ^ n ≤ qNat q (n+1)` gives `2‖x‖ ≤ qNat q (n+1)`.
  have h2x : 2 * ‖x‖ ≤ qNat q (n + 1) := le_trans hn (qNat_succ_ge hq n)
  rw [norm_qExpTerm hq, norm_qExpTerm hq, qFact_succ, pow_succ]
  have hFne : qFact q n ≠ 0 := (qFact_pos hq n).ne'
  rw [div_le_iff₀ (by positivity)]
  have hEq : (1 : ℝ) / 2 * (‖x‖ ^ n / qFact q n) * (qNat q (n + 1) * qFact q n)
      = ‖x‖ ^ n * qNat q (n + 1) / 2 := by
    field_simp
  rw [hEq, le_div_iff₀ (by norm_num : (0 : ℝ) < 2)]
  nlinarith [mul_nonneg (pow_nonneg hx n) (sub_nonneg.mpr h2x)]

end

end QOU.QExp
