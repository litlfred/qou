import QOU.MathlibExt.GaussianTailBound
import Mathlib.Analysis.SpecialFunctions.Gaussian.PoissonSummation

/-!
# QOU.MathlibExt.ComplexGaussianSumNonCancellation — a chirped Gaussian sum cannot cancel

Bean `qou-epy2` (L4-5), complex case; epic `qou-u1b5` (vdV Lemma 4).

The corpus Gaussian infrastructure (`GaussianThetaSum`, `GaussianThetaBound`,
`GaussianTailBound`, …) is **real**: `∑ exp(−a(n−c)²)` with `a > 0`.  The
non-cancellation step of van der Veen's Lemma 4 needs the **complex** (chirped)
version: the Whitehead-link outer sum is, after the Gaussian shape of its
positive weights is substituted, the lattice sum of

    G(n) = exp(−π a (n − c)² + 2π i ξ n),   Re a > 0,

with `a = (1+i)/(2N)` — the real part from the weights, the imaginary part from
the Fresnel phase `χ_{N,n}^{-1}`.  This file proves, from Mathlib's Poisson
summation for complex Gaussians (`Complex.tsum_exp_neg_quadratic`), the
**lower bound**

    ‖∑_{n∈ℤ} G(n)‖ ≥ ‖a^{1/2}‖⁻¹ · (e^{−π R ξ²} − 2q/(1−q)),
    R = Re(a⁻¹),  q = e^{−πR/4},  |ξ| ≤ 1/2,

uniformly in the real centre `c` (the centre only contributes a unimodular
factor on the dual side).  For `R` large the bracket is close to `1`, so a
chirped Gaussian of width `√N` keeps `≈ |a|^{-1/2}` of mass: no cancellation.

Pure complex analysis; no knots.  Upstreamable.  Archimedean (ℂ).
-/

namespace QOU.MathlibExt

open Complex

/-- The chirped Gaussian lattice term `exp(−π a (n−c)² + 2π i ξ n)`. -/
noncomputable def cgaussTerm (a : ℂ) (c ξ : ℝ) (n : ℤ) : ℂ :=
  cexp (-(Real.pi : ℂ) * a * ((n : ℂ) - c) ^ 2 + 2 * Real.pi * I * ξ * n)

/-- Its modulus is the real Gaussian `exp(−π Re a (n−c)²)` — the chirp is unimodular. -/
theorem norm_cgaussTerm (a : ℂ) (c ξ : ℝ) (n : ℤ) :
    ‖cgaussTerm a c ξ n‖ = Real.exp (-(Real.pi * a.re) * ((n : ℝ) - c) ^ 2) := by
  unfold cgaussTerm
  rw [Complex.norm_exp]
  congr 1
  have h : (-(Real.pi : ℂ) * a * ((n : ℂ) - c) ^ 2 + 2 * Real.pi * I * ξ * n)
      = ((-(Real.pi * ((n : ℝ) - c) ^ 2) : ℝ) : ℂ) * a
        + ((2 * Real.pi * ξ * n : ℝ) : ℂ) * I := by
    push_cast; ring
  rw [h, Complex.add_re, Complex.re_ofReal_mul, Complex.re_ofReal_mul, Complex.I_re]
  ring

/-- Summability of the chirped Gaussian, by comparison with the real one. -/
theorem summable_cgaussTerm {a : ℂ} (ha : 0 < a.re) (c ξ : ℝ) :
    Summable (cgaussTerm a c ξ) := by
  refine Summable.of_norm ?_
  have h := (hasSum_gaussian_theta_real (Real.pi * a.re) c
    (mul_pos Real.pi_pos ha)).summable
  refine h.congr (fun n => ?_)
  rw [norm_cgaussTerm]

/-- The dual-side term after Poisson summation. -/
noncomputable def cgaussDual (a : ℂ) (c ξ : ℝ) (m : ℤ) : ℂ :=
  cexp (-(Real.pi : ℂ) / a * ((m : ℂ) - ξ) ^ 2 - 2 * Real.pi * I * c * ((m : ℂ) - ξ))

theorem norm_cgaussDual (a : ℂ) (c ξ : ℝ) (m : ℤ) :
    ‖cgaussDual a c ξ m‖ = Real.exp (-(Real.pi * (a⁻¹).re) * ((m : ℝ) - ξ) ^ 2) := by
  unfold cgaussDual
  rw [Complex.norm_exp]
  congr 1
  have h : (-(Real.pi : ℂ) / a * ((m : ℂ) - ξ) ^ 2 - 2 * Real.pi * I * c * ((m : ℂ) - ξ))
      = ((-(Real.pi * ((m : ℝ) - ξ) ^ 2) : ℝ) : ℂ) * a⁻¹
        + ((-(2 * Real.pi * c * ((m : ℝ) - ξ)) : ℝ) : ℂ) * I := by
    push_cast; ring
  rw [h, Complex.add_re, Complex.re_ofReal_mul, Complex.re_ofReal_mul, Complex.I_re]
  ring

theorem inv_re_pos {a : ℂ} (ha : 0 < a.re) : 0 < (a⁻¹).re := by
  rw [Complex.inv_re]
  have : a ≠ 0 := by
    intro h; rw [h] at ha; simp at ha
  exact div_pos ha (Complex.normSq_pos.mpr this)

/-- **Poisson summation for the chirped Gaussian**, with the centre `c` pulled to
the dual side as a unimodular twist. -/
theorem tsum_cgaussTerm_eq {a : ℂ} (ha : 0 < a.re) (c ξ : ℝ) :
    ∑' n : ℤ, cgaussTerm a c ξ n
      = 1 / a ^ (1 / 2 : ℂ) * ∑' m : ℤ, cgaussDual a c ξ m := by
  have ha0 : a ≠ 0 := by
    intro h; rw [h] at ha; simp at ha
  set b : ℂ := a * c + I * ξ with hb
  have hfun : ∀ n : ℤ, cgaussTerm a c ξ n
      = cexp (-(Real.pi : ℂ) * a * c ^ 2)
        * cexp (-(Real.pi : ℂ) * a * (n : ℂ) ^ 2 + 2 * Real.pi * b * n) := by
    intro n
    unfold cgaussTerm
    rw [← Complex.exp_add]
    congr 1
    rw [hb]; ring
  have hP := Complex.tsum_exp_neg_quadratic ha b
  simp_rw [hfun]
  rw [tsum_mul_left, hP, ← mul_assoc, mul_comm (cexp _) (1 / _), mul_assoc,
    ← tsum_mul_left]
  congr 1
  congr 1
  funext m
  unfold cgaussDual
  rw [← Complex.exp_add]
  congr 1
  have hI : I * I = -1 := Complex.I_mul_I
  have h1 : (m : ℂ) + I * b = ((m : ℂ) - ξ) + I * a * c := by
    rw [hb]; linear_combination (ξ : ℂ) * hI
  rw [h1]
  have h2 : -(Real.pi : ℂ) / a * (((m : ℂ) - ξ) + I * a * c) ^ 2
      = -(Real.pi : ℂ) / a * ((m : ℂ) - ξ) ^ 2 - 2 * Real.pi * I * c * ((m : ℂ) - ξ)
        - Real.pi * (I * I) * a * c ^ 2 := by
    field_simp; ring
  rw [h2]
  linear_combination (-(Real.pi : ℂ) * a * c ^ 2) * hI

/-- **Non-cancellation of a chirped Gaussian lattice sum (sorry-free).**

For `Re a > 0`, any real centre `c`, and a linear chirp `|ξ| ≤ 1/2`,

    ‖a^{1/2}‖⁻¹ · (e^{−π R ξ²} − 2q/(1−q)) ≤ ‖∑_{n∈ℤ} e^{−π a (n−c)² + 2π i ξ n}‖,

`R = Re(a⁻¹)`, `q = e^{−πR/4}`.  The dual `m = 0` term dominates; the others are
bounded by a geometric series because `(m − ξ)² ≥ |m|/4` for `m ≠ 0`. -/
theorem norm_tsum_cgaussTerm_ge {a : ℂ} (ha : 0 < a.re) (c ξ : ℝ)
    (hξ : |ξ| ≤ 1 / 2) :
    ‖a ^ (1 / 2 : ℂ)‖⁻¹
        * (Real.exp (-(Real.pi * (a⁻¹).re) * ξ ^ 2)
          - 2 * Real.exp (-(Real.pi * (a⁻¹).re) / 4)
              / (1 - Real.exp (-(Real.pi * (a⁻¹).re) / 4)))
      ≤ ‖∑' n : ℤ, cgaussTerm a c ξ n‖ := by
  have hR := inv_re_pos ha
  set R := (a⁻¹).re with hRdef
  set q := Real.exp (-(Real.pi * R) / 4) with hq
  have hpiR : 0 < Real.pi * R := mul_pos Real.pi_pos hR
  have hq0 : 0 ≤ q := (Real.exp_pos _).le
  have hq1 : q < 1 := by
    rw [hq]
    calc Real.exp (-(Real.pi * R) / 4) < Real.exp 0 := Real.exp_lt_exp.mpr (by linarith)
      _ = 1 := Real.exp_zero
  -- summability of the dual series
  have hsumD : Summable (cgaussDual a c ξ) := by
    refine Summable.of_norm ?_
    have h := (hasSum_gaussian_theta_real (Real.pi * R) ξ hpiR).summable
    refine h.congr (fun m => ?_)
    rw [norm_cgaussDual]
  -- split off the `m = 0` term
  have hsplit := hsumD.tsum_eq_add_tsum_ite 0
  have hrest : ‖∑' m : ℤ, (if m = 0 then 0 else cgaussDual a c ξ m)‖
      ≤ 2 * q / (1 - q) := by
    refine tsum_of_norm_bounded (hasSum_int_geometric_ne_zero hq0 hq1) (fun m => ?_)
    by_cases hm : m = 0
    · simp [hm]
    · simp only [hm, if_false]
      rw [norm_cgaussDual, hq, ← Real.exp_nat_mul]
      apply Real.exp_le_exp.mpr
      have hM : (1 : ℝ) ≤ |(m : ℝ)| := by
        have : (1 : ℤ) ≤ |m| := Int.one_le_abs hm
        exact_mod_cast this
      have hcast : ((m.natAbs : ℕ) : ℝ) = |(m : ℝ)| := by
        rw [Nat.cast_natAbs]; push_cast; rfl
      rw [hcast]
      have hdist : |(m : ℝ)| - 1 / 2 ≤ |(m : ℝ) - ξ| := by
        have := abs_sub_abs_le_abs_sub (m : ℝ) ξ
        linarith
      have hsq : (|(m : ℝ)| - 1 / 2) ^ 2 ≤ ((m : ℝ) - ξ) ^ 2 := by
        rw [← sq_abs ((m : ℝ) - ξ)]
        exact pow_le_pow_left₀ (by linarith) hdist 2
      have hkey : |(m : ℝ)| / 4 ≤ ((m : ℝ) - ξ) ^ 2 := by
        nlinarith [mul_nonneg (by linarith : (0:ℝ) ≤ |(m : ℝ)| - 1)
          (by linarith : (0:ℝ) ≤ |(m : ℝ)| - 1 / 4)]
      nlinarith [mul_le_mul_of_nonneg_left hkey hpiR.le]
  have h0 : ‖cgaussDual a c ξ 0‖ = Real.exp (-(Real.pi * R) * ξ ^ 2) := by
    rw [norm_cgaussDual, hRdef]; congr 1; push_cast; ring
  have hlow : Real.exp (-(Real.pi * R) * ξ ^ 2) - 2 * q / (1 - q)
      ≤ ‖∑' m : ℤ, cgaussDual a c ξ m‖ := by
    rw [hsplit, ← h0]
    have := norm_sub_le (cgaussDual a c ξ 0 + ∑' m : ℤ,
      (if m = 0 then 0 else cgaussDual a c ξ m))
      (∑' m : ℤ, (if m = 0 then 0 else cgaussDual a c ξ m))
    rw [add_sub_cancel_right] at this
    linarith
  rw [tsum_cgaussTerm_eq ha c ξ, norm_mul, norm_div, norm_one, one_div (‖a ^ (1 / 2 : ℂ)‖)]
  exact mul_le_mul_of_nonneg_left hlow (inv_nonneg.mpr (norm_nonneg _))

/-- **Finite windows.**  If outside a finite set `s` the terms of a summable
`f` are dominated by a summable `g` with sum `B`, then the window sum is within `B`
of the full sum. -/
theorem norm_tsum_sub_finset_sum_le {f : ℤ → ℂ} (hf : Summable f) (s : Finset ℤ)
    {g : ℤ → ℝ} {B : ℝ} (hg : HasSum g B) (hg0 : ∀ n, 0 ≤ g n)
    (h : ∀ n, n ∉ s → ‖f n‖ ≤ g n) :
    ‖(∑' n, f n) - ∑ n ∈ s, f n‖ ≤ B := by
  have hF : HasSum (fun n => if n ∈ s then f n else 0) (∑ n ∈ s, f n) := by
    have hsum : (∑ n ∈ s, if n ∈ s then f n else 0) = ∑ n ∈ s, f n :=
      Finset.sum_congr rfl fun b hb => by simp [hb]
    rw [← hsum]
    exact hasSum_sum_of_ne_finset_zero fun b hb => by simp [hb]
  have hdiff := hf.hasSum.sub hF
  rw [hdiff.tsum_eq.symm]
  refine tsum_of_norm_bounded hg (fun n => ?_)
  by_cases hn : n ∈ s
  · simp [hn, hg0 n]
  · simp [hn, h n hn]

/-- `‖a^{1/2}‖² = ‖a‖`. -/
theorem norm_cpow_half_sq (a : ℂ) : ‖a ^ (1 / 2 : ℂ)‖ ^ 2 = ‖a‖ := by
  have h : (1 / 2 : ℂ) = ((1 / 2 : ℝ) : ℂ) := by push_cast; rfl
  rw [h, Complex.norm_cpow_real, ← Real.rpow_natCast, ← Real.rpow_mul (norm_nonneg _)]
  norm_num

end QOU.MathlibExt
