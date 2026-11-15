/-
  THE DISCRETE GAUSSIAN SUM EQUALS ITS INTEGRAL, UP TO `e^{−π²/a}`.

      | ∑_{n∈ℤ} e^{−a(n−c)²}  −  √(π/a) |  ≤  √(π/a) · 2q/(1−q),
      q = e^{−π²/a},

  uniformly in the shift `c`.

  `GaussianSumBound` gives `∑ ≤ 1 + ½√(π/a)` — a BOUND, one-sided, and lossy in
  the constant.  That is enough to prove a Laplace sum is `Θ(1/√a)` and not
  enough to say what the constant is.  This file gives the constant, and it is
  exactly the integral `√(π/a) = ∫_ℝ e^{−a(x−c)²}dx`, with an error that is not
  polynomially small but EXPONENTIALLY small.

  For the Kashaev application `a = √3π/N`, so `π²/a = πN/√3` and the error is
  `e^{−πN/√3}` — utterly below every other error in the development.  In other
  words: for the constant `c_σ`, replacing the sum over `k` by a Gaussian
  integral is free.  Everything that is lost is lost elsewhere.

  `GaussianThetaSum` already has the exact identity
  `∑_{n∈ℤ} e^{−a(n−c)²} = √(π/a)·Re θ₂(−c, iπ/a)`.  What this file adds is the
  one estimate that makes it usable: `θ₂ = 1 + O(e^{−π²/a})`.  The proof is
  Mathlib's own `norm_jacobiTheta₂_term_le` at `S = 0` — the argument `−c` is
  real, so the theta series has no growth from the `z` direction — summed
  against a two-sided geometric series via `n² ≥ |n|`.

  -- Ref: [leitner2026] QOU/MathlibExt/GaussianThetaSum.lean
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianSumBound.lean
-/
import QOU.MathlibExt.GaussianThetaSum

namespace QOU.MathlibExt

open Complex Real

/-- `(iπ/a).im = π/a` — the modulus of the transformed lattice. -/
theorem im_I_mul_pi_div (a : ℝ) (ha : 0 < a) :
    (Complex.I * (π : ℂ) / (a : ℂ)).im = π / a := by
  simp [Complex.div_im, Complex.mul_im, Complex.mul_re, Complex.normSq_apply]
  field_simp

/-- The `n = 0` term of `θ₂` is `1`, whatever `z` and `τ`.

The lemma list is spelled out rather than left to `simp`/`norm_num`: with the
default simp set this one goal costs more than the 200000-heartbeat budget,
for no reason visible in the statement. -/
theorem jacobiTheta₂_term_zero (z τ : ℂ) : jacobiTheta₂_term 0 z τ = 1 := by
  simp only [jacobiTheta₂_term, Int.cast_zero, mul_zero, zero_mul, ne_eq,
    OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, add_zero, Complex.exp_zero]

/-- The two-sided geometric series over `ℤ` with the `n = 0` term removed:
`∑_{n≠0} q^{|n|} = 2q/(1−q)`. -/
theorem hasSum_int_geometric_ne_zero {q : ℝ} (hq0 : 0 ≤ q) (hq1 : q < 1) :
    HasSum (fun n : ℤ => if n = 0 then (0 : ℝ) else q ^ n.natAbs)
      (2 * q / (1 - q)) := by
  have hne : (1 : ℝ) - q ≠ 0 := by linarith
  have hnat : HasSum (fun n : ℕ => if n = 0 then (0 : ℝ) else q ^ n)
      ((1 - q)⁻¹ - 1) := by
    have h := (hasSum_geometric_of_lt_one hq0 hq1).sub (hasSum_ite_eq (0 : ℕ) (1 : ℝ))
    have heq : (fun n : ℕ => q ^ n - if n = 0 then (1 : ℝ) else 0)
        = fun n : ℕ => if n = 0 then (0 : ℝ) else q ^ n := by
      funext n; by_cases h : n = 0 <;> simp [h]
    rwa [heq] at h
  -- both directions restrict to the same ℕ-series
  have hpos : HasSum
      (fun n : ℕ => (fun m : ℤ => if m = 0 then (0 : ℝ) else q ^ m.natAbs) ((n : ℤ)))
      ((1 - q)⁻¹ - 1) := by
    have heq : (fun n : ℕ =>
          (fun m : ℤ => if m = 0 then (0 : ℝ) else q ^ m.natAbs) ((n : ℤ)))
        = fun n : ℕ => if n = 0 then (0 : ℝ) else q ^ n := by
      funext n; by_cases h : n = 0 <;> simp [h]
    rw [heq]; exact hnat
  have hneg : HasSum
      (fun n : ℕ => (fun m : ℤ => if m = 0 then (0 : ℝ) else q ^ m.natAbs) (-(n : ℤ)))
      ((1 - q)⁻¹ - 1) := by
    have heq : (fun n : ℕ =>
          (fun m : ℤ => if m = 0 then (0 : ℝ) else q ^ m.natAbs) (-(n : ℤ)))
        = fun n : ℕ => if n = 0 then (0 : ℝ) else q ^ n := by
      funext n; by_cases h : n = 0 <;> simp [h]
    rw [heq]; exact hnat
  -- `f` MUST be given explicitly.  Left to unification this one step costs
  -- more than a 1000000-heartbeat budget: `?f ↑n =?= (if ↑n = 0 then ...)` is
  -- a higher-order problem with many solutions, and Lean searches for them.
  have h := HasSum.of_nat_of_neg
    (f := fun m : ℤ => if m = 0 then (0 : ℝ) else q ^ m.natAbs) hpos hneg
  have hz : (fun m : ℤ => if m = 0 then (0 : ℝ) else q ^ m.natAbs) 0 = 0 := by simp
  rw [hz] at h
  have hval : ((1 - q)⁻¹ - 1) + ((1 - q)⁻¹ - 1) - (0 : ℝ) = 2 * q / (1 - q) := by
    field_simp
    ring
  rwa [hval] at h

/-- **`θ₂(−c, iπ/a) = 1 + O(e^{−π²/a})`, uniformly in the real shift `c`.**

`S = 0` in `norm_jacobiTheta₂_term_le` because `(-c : ℂ)` has zero imaginary
part — that is what makes the bound uniform in `c`.  `n² ≥ |n|` then converts
the Gaussian tail into a geometric one. -/
theorem norm_jacobiTheta₂_sub_one_le (c a : ℝ) (ha : 0 < a) :
    ‖jacobiTheta₂ (-(c : ℂ)) (Complex.I * π / a) - 1‖
      ≤ 2 * Real.exp (-(π ^ 2 / a)) / (1 - Real.exp (-(π ^ 2 / a))) := by
  have hpi := Real.pi_pos
  set q := Real.exp (-(π ^ 2 / a)) with hqdef
  have hq0 : 0 < q := Real.exp_pos _
  have hq1 : q < 1 := by
    rw [hqdef, Real.exp_lt_one_iff]
    have : 0 < π ^ 2 / a := by positivity
    linarith
  have hτ : (Complex.I * (π : ℂ) / (a : ℂ)).im = π / a := im_I_mul_pi_div a ha
  have hτpos : 0 < (Complex.I * (π : ℂ) / (a : ℂ)).im := by
    rw [hτ]; positivity
  have hmain := hasSum_jacobiTheta₂_term (-(c : ℂ)) hτpos
  have h0 : jacobiTheta₂_term 0 (-(c : ℂ)) (Complex.I * π / a) = 1 :=
    jacobiTheta₂_term_zero _ _
  have hsub := hmain.sub
    (hasSum_ite_eq (0 : ℤ) (jacobiTheta₂_term 0 (-(c : ℂ)) (Complex.I * π / a)))
  have heq : (fun n : ℤ => jacobiTheta₂_term n (-(c : ℂ)) (Complex.I * π / a)
        - if n = 0 then jacobiTheta₂_term 0 (-(c : ℂ)) (Complex.I * π / a) else 0)
      = fun n : ℤ => if n = 0 then 0
          else jacobiTheta₂_term n (-(c : ℂ)) (Complex.I * π / a) := by
    funext n; by_cases h : n = 0 <;> simp [h]
  rw [heq, h0] at hsub
  refine hsub.norm_le_of_bounded (hasSum_int_geometric_ne_zero hq0.le hq1) ?_
  intro n
  by_cases h : n = 0
  · simp [h]
  · simp only [h, if_false]
    have hzim : |(-(c : ℂ)).im| ≤ 0 := by simp
    have hb := norm_jacobiTheta₂_term_le (S := 0) (T := π / a)
      (by positivity) hzim (le_of_eq hτ.symm) n
    have hcast : ((n.natAbs : ℕ) : ℝ) = |(n : ℝ)| := by
      rw [Int.cast_natAbs]; push_cast; ring
    -- `|n| ≥ 1` because `n ≠ 0`, hence `|n| ≤ n²`
    have hone : (1 : ℝ) ≤ |(n : ℝ)| := by
      have h1 : 1 ≤ n.natAbs := Int.natAbs_pos.mpr h
      have h2 : (1 : ℝ) ≤ ((n.natAbs : ℕ) : ℝ) := by exact_mod_cast h1
      rwa [hcast] at h2
    have hsq : |(n : ℝ)| ≤ (n : ℝ) ^ 2 := by nlinarith [sq_abs (n : ℝ)]
    have hcoef : 0 < π ^ 2 / a := by positivity
    have hpow : q ^ n.natAbs = Real.exp (|(n : ℝ)| * (-(π ^ 2 / a))) := by
      rw [← hcast]; exact (Real.exp_nat_mul _ _).symm
    rw [hpow]
    refine le_trans hb (Real.exp_le_exp.mpr ?_)
    simp only [mul_zero, zero_mul, sub_zero]
    rw [show -π * (π / a * (n : ℝ) ^ 2) = -(π ^ 2 / a) * (n : ℝ) ^ 2 by
      field_simp]
    nlinarith [mul_nonneg hcoef.le (sub_nonneg.mpr hsq)]

/-- **The sharp Laplace sum.**  `∑_{n∈ℤ} e^{−a(n−c)²}` is `√(π/a)` — the
Gaussian integral — with a relative error that is exponentially small in `1/a`
and uniform in the shift `c`. -/
theorem abs_tsum_gaussian_sub_sqrt_le (a c : ℝ) (ha : 0 < a) :
    |(∑' n : ℤ, Real.exp (-a * ((n : ℝ) - c) ^ 2)) - Real.sqrt (π / a)|
      ≤ Real.sqrt (π / a)
        * (2 * Real.exp (-(π ^ 2 / a)) / (1 - Real.exp (-(π ^ 2 / a)))) := by
  have h := hasSum_gaussian_theta_real a c ha
  rw [h.tsum_eq]
  set T := jacobiTheta₂ (-(c : ℂ)) (Complex.I * π / a) with hTdef
  have hs : (0 : ℝ) ≤ Real.sqrt (π / a) := Real.sqrt_nonneg _
  have hre : |T.re - 1| ≤ ‖T - 1‖ := by
    have hr : (T - 1).re = T.re - 1 := by simp
    calc |T.re - 1| = |(T - 1).re| := by rw [hr]
      _ ≤ ‖T - 1‖ := Complex.abs_re_le_norm _
  have hb := norm_jacobiTheta₂_sub_one_le c a ha
  have hfac : Real.sqrt (π / a) * T.re - Real.sqrt (π / a)
      = Real.sqrt (π / a) * (T.re - 1) := by ring
  rw [hfac, abs_mul, abs_of_nonneg hs]
  exact mul_le_mul_of_nonneg_left (le_trans hre hb) hs

end QOU.MathlibExt
