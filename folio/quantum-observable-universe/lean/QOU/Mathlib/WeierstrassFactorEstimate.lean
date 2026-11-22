/-
  Weierstrass primary-factor estimate — the Mathlib-level infrastructure.

  GOAL.  `‖1 - Eₚ(z)‖ ≤ ‖z‖^{p+1}` for `‖z‖ ≤ 1`, where
  `Eₚ(z) = (1 - z)·exp(∑_{k=1}^{p} z^k/k)`.  This is the convergence-critical
  bound behind the Weierstrass canonical product; Mathlib v4.24.0 has no
  Weierstrass/Hadamard/Jensen theory at all (verified: zero declarations
  matching `eierstrass`/`adamard`/`ensen` in the reachable environment).

  ROUTE — and why it is NOT the textbook one.  Ahlfors/Conway prove this from
  the power series `1 - Eₚ(z) = ∑_{k>p} a_k z^k` with `a_k ≥ 0`, deducing
  `|1-Eₚ(z)| ≤ 1-Eₚ(|z|)`.  Formalizing "exp of a nonneg-coefficient
  polynomial has nonneg coefficients, hence so does the antiderivative"
  requires real power-series machinery.

  This file takes an equivalent route that needs none of it, and gets the
  SHARP constant:

    1. `Eₚ'(z) = -z^p·exp(Sₚ(z))`, where the `(1-z)·∑_{k<p} z^k = 1 - z^p`
       telescoping is what kills the `-1` (`deriv_weierstrassFactor`).
    2. Hence `g(z) := 1 - Eₚ(z)` satisfies `g(0) = 0`, `g'(z) = z^p·exp(Sₚ(z))`,
       so along the segment `t ↦ tz`,
       `g(z) = z^{p+1}·∫₀¹ t^p·exp(Sₚ(tz)) dt`.
    3. `‖exp(Sₚ(tz))‖ = exp(Re Sₚ(tz)) ≤ exp(Sₚ(t‖z‖))` because
       `Re(w^k) ≤ ‖w‖^k` termwise (`re_sum_le`).
    4. For `‖z‖ ≤ 1` the real integral is monotone in `‖z‖`, and at `‖z‖ = 1`
       it equals `g(1) = 1 - Eₚ(1) = 1` EXACTLY — because `Eₚ(1) = 0`, the
       single fact that makes the constant sharp rather than `e^{H_p}/(p+1)`.

  The naive integral bound `‖exp(Sₚ(tz))‖ ≤ exp(H_p)` gives
  `e^{H_p}/(p+1) > 1` for `p ≥ 1` and is NOT good enough; step 4 is what
  recovers the exact `1`.

  §7c: the estimate is archimedean (a genuine `ℝ`-valued growth bound), so
  `Real.exp` / `‖·‖` are the honest carriers.

  -- Ref: [leitner2026] Ahlfors, "Complex Analysis" §5.3 Lemma; Conway,
  --      "Functions of One Complex Variable" XI.§2 Lemma 2.6.
-/

import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Algebra.Order.Ring.GeomSum
import Mathlib.Algebra.Ring.Regular

namespace QOU.Mathlib.WeierstrassFactorEstimate

open scoped BigOperators
open intervalIntegral

/-- The exponent polynomial `Sₚ(z) = ∑_{k=1}^{p} z^k/k`, reindexed over
    `Finset.range p` so the summand is `z^{k+1}/(k+1)`. -/
noncomputable def expSum (p : ℕ) (z : ℂ) : ℂ :=
  ∑ k ∈ Finset.range p, z ^ (k + 1) / ((k : ℂ) + 1)

/-- The **Weierstrass primary factor** `Eₚ(z) = (1 - z)·exp(Sₚ(z))`. -/
noncomputable def weierstrassFactor (p : ℕ) (z : ℂ) : ℂ :=
  (1 - z) * Complex.exp (expSum p z)

@[simp]
theorem expSum_zero (p : ℕ) : expSum p 0 = 0 := by
  unfold expSum
  exact Finset.sum_eq_zero fun k _ => by simp [pow_succ]

@[simp]
theorem weierstrassFactor_apply_zero (p : ℕ) : weierstrassFactor p 0 = 1 := by
  simp [weierstrassFactor]

/-- **`Eₚ(1) = 0`.**  The linear factor vanishes at `1`; this is what makes the
    constant in the main estimate exactly `1`. -/
@[simp]
theorem weierstrassFactor_one (p : ℕ) : weierstrassFactor p 1 = 0 := by
  simp [weierstrassFactor]

/-! ### Step 1 — the derivative identity -/

/-- `Sₚ` is differentiable, with `Sₚ'(z) = ∑_{k<p} z^k`. -/
theorem hasDerivAt_expSum (p : ℕ) (z : ℂ) :
    HasDerivAt (expSum p) (∑ k ∈ Finset.range p, z ^ k) z := by
  have h : ∀ k ∈ Finset.range p,
      HasDerivAt (fun w : ℂ => w ^ (k + 1) / ((k : ℂ) + 1)) (z ^ k) z := by
    intro k _
    have hk : ((k : ℂ) + 1) ≠ 0 := by
      have hkc : ((k : ℂ) + 1) = ((k + 1 : ℕ) : ℂ) := by push_cast; ring
      rw [hkc]
      exact_mod_cast Nat.succ_ne_zero k
    have hd := (hasDerivAt_pow (k + 1) z).div_const ((k : ℂ) + 1)
    convert hd using 1
    push_cast
    field_simp
  have hs := HasDerivAt.sum h
  -- `HasDerivAt.sum` lands on the POINTWISE (Pi-type) sum of functions;
  -- transport it to the function-of-sums shape `expSum` actually has.
  have hfun : (∑ i ∈ Finset.range p, fun w : ℂ => w ^ (i + 1) / ((i : ℂ) + 1))
      = fun w : ℂ => ∑ k ∈ Finset.range p, w ^ (k + 1) / ((k : ℂ) + 1) := by
    funext w
    simp
  rw [hfun] at hs
  exact hs

/-- **`Eₚ'(z) = -z^p · exp(Sₚ(z))`.**

    The telescoping `(1 - z)·∑_{k<p} z^k = 1 - z^p` is the whole content: it
    cancels the `-1` coming from differentiating the linear factor, leaving a
    single monomial `-z^p`.  This is why `Eₚ` is "flat to order `p`" at the
    origin and hence why the canonical product converges. -/
theorem hasDerivAt_weierstrassFactor (p : ℕ) (z : ℂ) :
    HasDerivAt (weierstrassFactor p) (-z ^ p * Complex.exp (expSum p z)) z := by
  unfold weierstrassFactor
  have hlin : HasDerivAt (fun w : ℂ => 1 - w) (-1) z := by
    simpa using (hasDerivAt_id z).const_sub 1
  have hexp : HasDerivAt (fun w : ℂ => Complex.exp (expSum p w))
      (Complex.exp (expSum p z) * ∑ k ∈ Finset.range p, z ^ k) z := by
    have := (hasDerivAt_expSum p z).cexp
    simpa [mul_comm] using this
  have h := hlin.mul hexp
  -- (1-z)·exp(S)·∑ z^k + (-1)·exp(S)  =  exp(S)·((1-z)·∑ z^k - 1) = -z^p·exp(S)
  have htel : (1 - z) * (∑ k ∈ Finset.range p, z ^ k) = 1 - z ^ p := by
    -- geom_sum_mul : (∑ i ∈ range p, z^i) * (z - 1) = z^p - 1.
    -- ℂ is not ordered, so this is ring arithmetic, not `nlinarith`.
    have hg := geom_sum_mul z p
    linear_combination -hg
  convert h using 1
  linear_combination (-(Complex.exp (expSum p z))) * htel

/-! ### Step 2 — the real companion, and why its value at `1` is the whole point -/

/-- Real exponent polynomial `Sₚ(t) = ∑_{k=1}^{p} t^k/k`. -/
noncomputable def expSumR (p : ℕ) (t : ℝ) : ℝ :=
  ∑ k ∈ Finset.range p, t ^ (k + 1) / ((k : ℝ) + 1)

/-- Real primary factor `Eₚ(t) = (1-t)·exp(Sₚ(t))`. -/
noncomputable def weierstrassFactorR (p : ℕ) (t : ℝ) : ℝ :=
  (1 - t) * Real.exp (expSumR p t)

theorem hasDerivAt_expSumR (p : ℕ) (t : ℝ) :
    HasDerivAt (expSumR p) (∑ k ∈ Finset.range p, t ^ k) t := by
  have h : ∀ k ∈ Finset.range p,
      HasDerivAt (fun x : ℝ => x ^ (k + 1) / ((k : ℝ) + 1)) (t ^ k) t := by
    intro k _
    have hk : ((k : ℝ) + 1) ≠ 0 := by positivity
    have hd := (hasDerivAt_pow (k + 1) t).div_const ((k : ℝ) + 1)
    convert hd using 1
    push_cast
    field_simp
  have hs := HasDerivAt.sum h
  have hfun : (∑ i ∈ Finset.range p, fun x : ℝ => x ^ (i + 1) / ((i : ℝ) + 1))
      = fun x : ℝ => ∑ k ∈ Finset.range p, x ^ (k + 1) / ((k : ℝ) + 1) := by
    funext x; simp
  rw [hfun] at hs
  exact hs

/-- Real analogue of the derivative identity. -/
theorem hasDerivAt_weierstrassFactorR (p : ℕ) (t : ℝ) :
    HasDerivAt (weierstrassFactorR p) (-t ^ p * Real.exp (expSumR p t)) t := by
  unfold weierstrassFactorR
  have hlin : HasDerivAt (fun x : ℝ => 1 - x) (-1) t := by
    simpa using (hasDerivAt_id t).const_sub 1
  have hexp : HasDerivAt (fun x : ℝ => Real.exp (expSumR p x))
      (Real.exp (expSumR p t) * ∑ k ∈ Finset.range p, t ^ k) t := by
    have := (hasDerivAt_expSumR p t).exp
    simpa [mul_comm] using this
  have h := hlin.mul hexp
  have htel : (1 - t) * (∑ k ∈ Finset.range p, t ^ k) = 1 - t ^ p := by
    have hg := geom_sum_mul t p
    linear_combination -hg
  convert h using 1
  linear_combination (-(Real.exp (expSumR p t))) * htel

@[simp] theorem expSumR_zero (p : ℕ) : expSumR p 0 = 0 := by
  unfold expSumR; exact Finset.sum_eq_zero fun k _ => by simp [pow_succ]

@[simp] theorem weierstrassFactorR_zero (p : ℕ) : weierstrassFactorR p 0 = 1 := by
  simp [weierstrassFactorR]

/-- **`Eₚ(1) = 0` on ℝ.**  This single value is what makes the main constant
    exactly `1`: the total mass of the integral below is `1 - Eₚ(1) = 1`. -/
@[simp] theorem weierstrassFactorR_one (p : ℕ) : weierstrassFactorR p 1 = 0 := by
  simp [weierstrassFactorR]

/-- **The total mass is exactly `1`.**  `∫₀¹ t^p·exp(Sₚ(t)) dt = 1`.

    This is the sharp step.  Bounding the integrand crudely by `exp(H_p)`
    would give `e^{H_p}/(p+1) > 1` for `p ≥ 1` — too weak.  Here the integral
    is evaluated EXACTLY by the fundamental theorem of calculus applied to
    `1 - Eₚ`, whose endpoint values are `0` and `1 - Eₚ(1) = 1`. -/
theorem integral_pow_mul_exp_expSumR (p : ℕ) :
    ∫ t in (0:ℝ)..1, t ^ p * Real.exp (expSumR p t) = 1 := by
  have hderiv : ∀ t ∈ Set.uIcc (0:ℝ) 1,
      HasDerivAt (fun x => 1 - weierstrassFactorR p x)
        (t ^ p * Real.exp (expSumR p t)) t := by
    intro t _
    have := (hasDerivAt_weierstrassFactorR p t).const_sub 1
    simpa using this
  have hint : IntervalIntegrable (fun t : ℝ => t ^ p * Real.exp (expSumR p t))
      MeasureTheory.volume 0 1 := by
    apply Continuous.intervalIntegrable
    unfold expSumR
    fun_prop
  have := intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint
  simpa using this

/-! ### Step 3 — the termwise real bound on the complex exponent -/

/-- `Re Sₚ(w) ≤ Sₚ(‖w‖)`: termwise, `Re(w^k) ≤ ‖w‖^k`. -/
theorem re_expSum_le (p : ℕ) (w : ℂ) : (expSum p w).re ≤ expSumR p ‖w‖ := by
  unfold expSum expSumR
  rw [Complex.re_sum]
  refine Finset.sum_le_sum fun k _ => ?_
  have hk : (0:ℝ) < (k : ℝ) + 1 := by positivity
  have hkc : ((k : ℂ) + 1) = ((((k : ℝ) + 1 : ℝ)) : ℂ) := by push_cast; ring
  rw [hkc, Complex.div_ofReal_re]
  have hre : (w ^ (k + 1)).re ≤ ‖w ^ (k + 1)‖ := Complex.re_le_norm _
  have hnorm : ‖w ^ (k + 1)‖ = ‖w‖ ^ (k + 1) := by rw [norm_pow]
  rw [hnorm] at hre
  gcongr

/-- `Sₚ` is monotone in its (nonnegative) real argument, so shrinking `‖z‖`
    below `1` only shrinks the exponent. -/
theorem expSumR_mono {p : ℕ} {a b : ℝ} (ha : 0 ≤ a) (hab : a ≤ b) :
    expSumR p a ≤ expSumR p b := by
  unfold expSumR
  refine Finset.sum_le_sum fun k _ => ?_
  have hk : (0:ℝ) < (k : ℝ) + 1 := by positivity
  gcongr

/-! ### Step 4 — integral representation and the estimate -/

private theorem hasDerivAt_seg (p : ℕ) (z : ℂ) (t : ℝ) :
    HasDerivAt (fun r : ℝ => 1 - weierstrassFactor p ((r : ℂ) * z))
      (z ^ (p + 1) * (t : ℂ) ^ p * Complex.exp (expSum p ((t : ℂ) * z))) t := by
  have h1 : HasDerivAt (fun r : ℝ => (r : ℂ)) 1 t := by
    simpa using (Complex.ofRealCLM.hasDerivAt (x := t))
  have hinner : HasDerivAt (fun r : ℝ => (r : ℂ) * z) z t := by
    simpa using h1.mul_const z
  have h := (hasDerivAt_weierstrassFactor p ((t : ℂ) * z)).scomp t hinner
  have h2 := h.const_sub 1
  convert h2 using 1
  simp only [smul_eq_mul, mul_pow]
  ring

/-- **Integral representation.**  `1 - Eₚ(z) = ∫₀¹ z^{p+1}·t^p·exp(Sₚ(tz)) dt`.
    Immediate from `hasDerivAt_weierstrassFactor` along the segment `t ↦ tz`,
    using `Eₚ(0) = 1` at the lower endpoint. -/
theorem oneSub_weierstrassFactor_eq_integral (p : ℕ) (z : ℂ) :
    1 - weierstrassFactor p z
      = ∫ t in (0:ℝ)..1,
          z ^ (p + 1) * (t : ℂ) ^ p * Complex.exp (expSum p ((t : ℂ) * z)) := by
  have hint : IntervalIntegrable
      (fun t : ℝ => z ^ (p + 1) * (t : ℂ) ^ p * Complex.exp (expSum p ((t : ℂ) * z)))
      MeasureTheory.volume 0 1 := by
    apply Continuous.intervalIntegrable
    unfold expSum
    fun_prop
  have := intervalIntegral.integral_eq_sub_of_hasDerivAt
    (fun t _ => hasDerivAt_seg p z t) hint
  simpa using this.symm

/-- **Weierstrass estimate.**  For `‖z‖ ≤ 1`, `‖1 - Eₚ(z)‖ ≤ ‖z‖^{p+1}`.

    The constant is exactly `1` because the total mass
    `∫₀¹ t^p exp(Sₚ(t)) dt` equals `1 - Eₚ(1) = 1` on the nose. -/
theorem norm_one_sub_weierstrassFactor_le (p : ℕ) {z : ℂ} (hz : ‖z‖ ≤ 1) :
    ‖1 - weierstrassFactor p z‖ ≤ ‖z‖ ^ (p + 1) := by
  rw [oneSub_weierstrassFactor_eq_integral p z]
  have hbound : ∀ t ∈ Set.Icc (0:ℝ) 1,
      ‖z ^ (p + 1) * (t : ℂ) ^ p * Complex.exp (expSum p ((t : ℂ) * z))‖
        ≤ ‖z‖ ^ (p + 1) * (t ^ p * Real.exp (expSumR p t)) := by
    intro t ht
    obtain ⟨ht0, ht1⟩ := ht
    have hnormt : ‖((t : ℝ) : ℂ)‖ = t := by
      rw [Complex.norm_real]
      exact Real.norm_of_nonneg ht0
    -- ‖exp(Sₚ(tz))‖ = exp(Re Sₚ(tz)) ≤ exp(Sₚ(‖tz‖)) ≤ exp(Sₚ(t))
    have hre := re_expSum_le p ((t : ℂ) * z)
    have hnz : ‖(t : ℂ) * z‖ ≤ t := by
      rw [norm_mul, hnormt]
      calc t * ‖z‖ ≤ t * 1 := by gcongr
        _ = t := by ring
    have hmono : expSumR p ‖(t : ℂ) * z‖ ≤ expSumR p t :=
      expSumR_mono (norm_nonneg _) hnz
    have hexp : ‖Complex.exp (expSum p ((t : ℂ) * z))‖ ≤ Real.exp (expSumR p t) := by
      rw [Complex.norm_exp]
      exact Real.exp_le_exp.mpr (hre.trans hmono)
    rw [norm_mul, norm_mul, norm_pow, norm_pow, hnormt]
    have hzp : (0:ℝ) ≤ ‖z‖ ^ (p + 1) := by positivity
    have htp : (0:ℝ) ≤ t ^ p := by positivity
    calc ‖z‖ ^ (p + 1) * t ^ p * ‖Complex.exp (expSum p ((t : ℂ) * z))‖
        ≤ ‖z‖ ^ (p + 1) * t ^ p * Real.exp (expSumR p t) := by gcongr
      _ = ‖z‖ ^ (p + 1) * (t ^ p * Real.exp (expSumR p t)) := by ring
  have hintg : IntervalIntegrable
      (fun t : ℝ => ‖z‖ ^ (p + 1) * (t ^ p * Real.exp (expSumR p t)))
      MeasureTheory.volume 0 1 := by
    apply Continuous.intervalIntegrable
    unfold expSumR
    fun_prop
  have hintf : IntervalIntegrable
      (fun t : ℝ => z ^ (p + 1) * (t : ℂ) ^ p * Complex.exp (expSum p ((t : ℂ) * z)))
      MeasureTheory.volume 0 1 := by
    apply Continuous.intervalIntegrable
    unfold expSum
    fun_prop
  calc ‖∫ t in (0:ℝ)..1,
            z ^ (p + 1) * (t : ℂ) ^ p * Complex.exp (expSum p ((t : ℂ) * z))‖
      ≤ ∫ t in (0:ℝ)..1,
            ‖z ^ (p + 1) * (t : ℂ) ^ p * Complex.exp (expSum p ((t : ℂ) * z))‖ :=
        intervalIntegral.norm_integral_le_integral_norm (by norm_num)
    _ ≤ ∫ t in (0:ℝ)..1, ‖z‖ ^ (p + 1) * (t ^ p * Real.exp (expSumR p t)) :=
        intervalIntegral.integral_mono_on (by norm_num) hintf.norm hintg hbound
    _ = ‖z‖ ^ (p + 1) := by
        rw [intervalIntegral.integral_const_mul, integral_pow_mul_exp_expSumR]
        ring

end QOU.Mathlib.WeierstrassFactorEstimate
