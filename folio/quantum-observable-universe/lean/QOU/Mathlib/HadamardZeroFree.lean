import Mathlib.Analysis.Complex.HasPrimitives
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Analytic.Uniqueness
import Mathlib.Algebra.Polynomial.BigOperators
import QOU.Mathlib.BorelCaratheodory
import QOU.Mathlib.HadamardFactorization

/-!
# The zero-free step of Hadamard factorization

**Proved here, sorry-free.** A zero-free entire function of order `≤ ρ` (in the sense of
`QOU.Mathlib.HadamardFactorization.IsEntireOfOrderLE`, with `0 ≤ ρ`) is `exp` of a polynomial
of degree `≤ ρ` (`exists_polynomial_of_zeroFree`).

The proof has three sorry-free pieces, each stated separately:

* `exists_polynomial_of_norm_le` — **generalised Liouville**: an entire `h` with
  `‖h z‖ ≤ K (1 + ‖z‖)^ρ` is a polynomial of `natDegree ≤ ρ`. The Taylor coefficients at `0`
  are the Cauchy coefficients on every circle (`HasFPowerSeriesAt.eq_formalMultilinearSeries`),
  and the Cauchy estimate gives `‖aₙ‖ ≤ K 2^ρ R^{ρ-n} → 0` for `n > ρ`.
* `exists_entire_log` — a zero-free entire function has an entire logarithm: the wedge
  integral of `f'/f` from `0` is a global primitive (Morera on every ball `ball 0 (‖z‖+1)`),
  and `f · exp(-h)` has zero derivative.
* `exists_norm_le_of_norm_exp_le` — **growth transfer** by Borel–Carathéodory
  (`QOU.Mathlib.BorelCaratheodory.norm_le_of_re_le`, applied to `h - h 0` on `ball 0 (2r)`):
  `Re h ≤ log A + C‖z‖^ρ` implies `‖h z‖ ≤ K (1 + ‖z‖)^ρ`.

**Not proved here.** Nothing about functions with zeros: the canonical product, the
quotient `f / P`, its zero-freeness, and the order estimate on `f / P` (which is the
genuinely hard part of Hadamard: a lower bound on `|P|` off small discs) remain open in
`QOU.Mathlib.HadamardFactorization.hadamard_factorization`.

-- Ref: [leitner2026] standard: Conway, Functions of One Complex Variable I, XI §2–3; Titchmarsh, The Theory of Functions, §5.5, §8.24
-/

open Complex Metric Set Filter Topology
open scoped NNReal ENNReal Real

namespace QOU.Mathlib.HadamardZeroFree

/-! ## Generalised Liouville -/

/-- The Taylor coefficients at `0` of an entire `h` with polynomial growth of order `ρ`
vanish above `ρ`. -/
theorem coeff_eq_zero_of_norm_le {h : ℂ → ℂ} (hh : Differentiable ℂ h) {ρ K : ℝ}
    (hρ : 0 ≤ ρ) (hb : ∀ z, ‖h z‖ ≤ K * (1 + ‖z‖) ^ ρ) {n : ℕ} (hn : ρ < n) :
    (cauchyPowerSeries h 0 ((1 : ℝ≥0) : ℝ)).coeff n = 0 := by
  set p := cauchyPowerSeries h 0 ((1 : ℝ≥0) : ℝ) with hp
  have hK : 0 ≤ K := by
    have := (norm_nonneg _).trans (hb 0)
    simpa using this
  have hser : ∀ R : ℝ≥0, 0 < R → cauchyPowerSeries h 0 R = p := fun R hR =>
    (hh.hasFPowerSeriesOnBall 0 hR).hasFPowerSeriesAt.eq_formalMultilinearSeries
      (hh.hasFPowerSeriesOnBall 0 one_pos).hasFPowerSeriesAt
  -- Cauchy estimate on the circle of radius `R ≥ 1`.
  have hest : ∀ R : ℝ, 1 ≤ R → ‖p.coeff n‖ ≤ K * 2 ^ ρ * R ^ (-((n : ℝ) - ρ)) := by
    intro R hR
    have hR0 : 0 < R := by linarith
    have hRR : ((R.toNNReal : ℝ≥0) : ℝ) = R := Real.coe_toNNReal R hR0.le
    have hpos : (0 : ℝ≥0) < R.toNNReal := by simpa using hR0
    have h1 : ‖p.coeff n‖ = ‖cauchyPowerSeries h 0 R n‖ := by
      rw [← FormalMultilinearSeries.norm_apply_eq_norm_coef, ← hser _ hpos, hRR]
    have hint : (∫ θ in (0 : ℝ)..2 * π, ‖h (circleMap 0 R θ)‖) ≤ 2 * π * (K * (1 + R) ^ ρ) := by
      have hi : IntervalIntegrable (fun θ => ‖h (circleMap 0 R θ)‖) MeasureTheory.volume 0 (2 * π) :=
        ((hh.continuous.comp (continuous_circleMap 0 R)).norm).intervalIntegrable _ _
      calc (∫ θ in (0 : ℝ)..2 * π, ‖h (circleMap 0 R θ)‖)
          ≤ ∫ _ in (0 : ℝ)..2 * π, K * (1 + R) ^ ρ :=
            intervalIntegral.integral_mono_on Real.two_pi_pos.le hi intervalIntegrable_const
              (fun θ _ => by
                have := hb (circleMap 0 R θ)
                rwa [norm_circleMap_zero, abs_of_pos hR0] at this)
        _ = 2 * π * (K * (1 + R) ^ ρ) := by simp; ring
    have h2 := norm_cauchyPowerSeries_le h 0 R n
    rw [abs_of_pos hR0] at h2
    have h3 : ((2 * π)⁻¹ * ∫ θ in (0 : ℝ)..2 * π, ‖h (circleMap 0 R θ)‖) ≤ K * (1 + R) ^ ρ := by
      rw [inv_mul_le_iff₀ (by positivity)]; exact hint
    have h4 : (1 + R) ^ ρ ≤ 2 ^ ρ * R ^ ρ := by
      rw [← Real.mul_rpow (by norm_num) hR0.le]
      exact Real.rpow_le_rpow (by linarith) (by linarith) hρ
    have h5 : R ^ ρ * R⁻¹ ^ n = R ^ (-((n : ℝ) - ρ)) := by
      rw [inv_pow, ← Real.rpow_natCast, ← Real.rpow_neg hR0.le, ← Real.rpow_add hR0]
      congr 1; ring
    have hRn : 0 ≤ R⁻¹ ^ n := by positivity
    rw [h1]
    calc ‖cauchyPowerSeries h 0 R n‖
        ≤ ((2 * π)⁻¹ * ∫ θ in (0 : ℝ)..2 * π, ‖h (circleMap 0 R θ)‖) * R⁻¹ ^ n := h2
      _ ≤ (K * (2 ^ ρ * R ^ ρ)) * R⁻¹ ^ n :=
          mul_le_mul_of_nonneg_right (h3.trans (mul_le_mul_of_nonneg_left h4 hK)) hRn
      _ = K * 2 ^ ρ * (R ^ ρ * R⁻¹ ^ n) := by ring
      _ = K * 2 ^ ρ * R ^ (-((n : ℝ) - ρ)) := by rw [h5]
  have hlim : Tendsto (fun R : ℝ => K * 2 ^ ρ * R ^ (-((n : ℝ) - ρ))) atTop (𝓝 0) := by
    have := (tendsto_rpow_neg_atTop (y := (n : ℝ) - ρ) (by linarith)).const_mul (K * 2 ^ ρ)
    simpa using this
  have hle : ‖p.coeff n‖ ≤ 0 :=
    ge_of_tendsto hlim (eventually_atTop.mpr ⟨1, fun R hR => hest R hR⟩)
  exact norm_le_zero_iff.mp hle

/-- **Generalised Liouville.** An entire function with `‖h z‖ ≤ K (1 + ‖z‖)^ρ`, `0 ≤ ρ`,
is a polynomial of `natDegree ≤ ρ`. -/
theorem exists_polynomial_of_norm_le {h : ℂ → ℂ} (hh : Differentiable ℂ h) {ρ K : ℝ}
    (hρ : 0 ≤ ρ) (hb : ∀ z, ‖h z‖ ≤ K * (1 + ‖z‖) ^ ρ) :
    ∃ g : Polynomial ℂ, (g.natDegree : ℝ) ≤ ρ ∧ ∀ z, h z = g.eval z := by
  set N := ⌊ρ⌋₊ with hN
  set p := cauchyPowerSeries h 0 ((1 : ℝ≥0) : ℝ) with hp
  refine ⟨∑ n ∈ Finset.range (N + 1), Polynomial.C (p.coeff n) * Polynomial.X ^ n, ?_, ?_⟩
  · have hdeg : (∑ n ∈ Finset.range (N + 1), Polynomial.C (p.coeff n) * Polynomial.X ^ n).natDegree
        ≤ N := by
      refine Polynomial.natDegree_sum_le_of_forall_le _ _ (fun n hn => ?_)
      refine (Polynomial.natDegree_C_mul_X_pow_le _ _).trans ?_
      simp only [Finset.mem_range] at hn; omega
    exact (Nat.cast_le.mpr hdeg).trans (Nat.floor_le hρ)
  · intro z
    have hs := (hh.hasFPowerSeriesOnBall 0 (R := 1) one_pos).hasSum
      (y := z) (by simp)
    rw [zero_add] at hs
    have hz : ∀ n ∉ Finset.range (N + 1), (p n fun _ => z) = 0 := by
      intro n hn
      simp only [Finset.mem_range, not_lt] at hn
      have hlt : ρ < n := lt_of_lt_of_le (Nat.lt_floor_add_one ρ) (by exact_mod_cast hn)
      rw [FormalMultilinearSeries.apply_eq_pow_smul_coeff,
        coeff_eq_zero_of_norm_le hh hρ hb hlt, smul_zero]
    rw [hs.unique (hasSum_sum_of_ne_finset_zero hz)]
    rw [Polynomial.eval_finset_sum]
    refine Finset.sum_congr rfl (fun n _ => ?_)
    rw [FormalMultilinearSeries.apply_eq_pow_smul_coeff, smul_eq_mul, Polynomial.eval_mul,
      Polynomial.eval_C, Polynomial.eval_pow, Polynomial.eval_X, mul_comm]

/-! ## Entire logarithm of a zero-free entire function -/

/-- A zero-free entire function has an entire logarithm. -/
theorem exists_entire_log {f : ℂ → ℂ} (hf : Differentiable ℂ f) (hz : ∀ z, f z ≠ 0) :
    ∃ h : ℂ → ℂ, Differentiable ℂ h ∧ ∀ z, f z = Complex.exp (h z) := by
  set φ : ℂ → ℂ := fun z => deriv f z / f z with hφ
  have hdf : Differentiable ℂ (deriv f) := fun z =>
    ((hf.differentiableOn.deriv isOpen_univ) z (mem_univ z)).differentiableAt
      (isOpen_univ.mem_nhds (mem_univ z))
  have hφd : Differentiable ℂ φ := hdf.div hf hz
  set G : ℂ → ℂ := fun z => Complex.wedgeIntegral 0 z φ with hGdef
  have hG : ∀ z, HasDerivAt G (φ z) z := by
    intro z
    have hmem : z ∈ ball (0 : ℂ) (‖z‖ + 1) := by simp
    exact (hφd.differentiableOn (s := ball (0 : ℂ) (‖z‖ + 1))).isConservativeOn
      |>.hasDerivAt_wedgeIntegral hφd.continuous.continuousOn hmem
  set c0 : ℂ := Complex.log (f 0) with hc0
  set h : ℂ → ℂ := fun z => G z - G 0 + c0 with hhdef
  have hhd : ∀ z, HasDerivAt h (φ z) z := fun z => ((hG z).sub_const _).add_const _
  set ψ : ℂ → ℂ := fun z => f z * Complex.exp (-h z) with hψdef
  have hψ : ∀ z, HasDerivAt ψ 0 z := by
    intro z
    have := (hf z).hasDerivAt.mul (hhd z).neg.cexp
    convert this using 1
    simp only [hφ]
    field_simp [hz z]
    ring
  have hconst : ∀ z, ψ z = ψ 0 := fun z =>
    is_const_of_deriv_eq_zero (fun w => (hψ w).differentiableAt) (fun w => (hψ w).deriv) z 0
  have hψ0 : ψ 0 = 1 := by
    simp only [hψdef, hhdef, sub_self, zero_add, hc0, Complex.exp_neg, Complex.exp_log (hz 0)]
    exact mul_inv_cancel₀ (hz 0)
  refine ⟨h, fun z => (hhd z).differentiableAt, fun z => ?_⟩
  have h1 := hconst z
  rw [hψ0] at h1
  simp only [hψdef, Complex.exp_neg] at h1
  exact (mul_inv_eq_one₀ (Complex.exp_ne_zero _)).mp h1

/-! ## Growth transfer via Borel–Carathéodory -/

/-- If `‖exp (h z)‖ ≤ A exp (C ‖z‖^ρ)` for an entire `h`, then `h` has polynomial growth
`‖h z‖ ≤ K (1 + ‖z‖)^ρ`. -/
theorem exists_norm_le_of_norm_exp_le {h : ℂ → ℂ} (hh : Differentiable ℂ h) {ρ A C : ℝ}
    (hρ : 0 ≤ ρ) (hC : 0 < C) (hA : 0 < A)
    (hb : ∀ z, ‖Complex.exp (h z)‖ ≤ A * Real.exp (C * ‖z‖ ^ ρ)) :
    ∃ K : ℝ, ∀ z, ‖h z‖ ≤ K * (1 + ‖z‖) ^ ρ := by
  have hre : ∀ w, (h w).re ≤ Real.log A + C * ‖w‖ ^ ρ := by
    intro w
    have := hb w
    rw [Complex.norm_exp, ← Real.exp_log hA, ← Real.exp_add] at this
    exact Real.exp_le_exp.mp this
  have h0re : -(h 0).re ≤ ‖h 0‖ := (abs_le.mp (Complex.abs_re_le_norm (h 0))).1 |> fun h => by
    linarith
  refine ⟨2 * |Real.log A| + 2 * C * 2 ^ ρ + 3 * ‖h 0‖ + 2, fun z => ?_⟩
  set r : ℝ := 1 + ‖z‖ with hr
  have hr1 : 1 ≤ r := by have := norm_nonneg z; linarith
  set R : ℝ := 2 * r with hR
  set M : ℝ := |Real.log A| + C * R ^ ρ + ‖h 0‖ + 1 with hM
  have hRpos : 0 < R := by linarith
  have hMpos : 0 < M := by
    have : 0 ≤ C * R ^ ρ := mul_nonneg hC.le (Real.rpow_nonneg hRpos.le _)
    have := abs_nonneg (Real.log A); have := norm_nonneg (h 0); linarith
  have hreF : ∀ w ∈ ball (0 : ℂ) R, (h w - h 0).re ≤ M := by
    intro w hw
    have hw' : ‖w‖ < R := by simpa using hw
    have hpow : ‖w‖ ^ ρ ≤ R ^ ρ := Real.rpow_le_rpow (norm_nonneg _) hw'.le hρ
    have := hre w
    have := mul_le_mul_of_nonneg_left hpow hC.le
    have := le_abs_self (Real.log A)
    rw [Complex.sub_re]
    linarith
  have hBC := QOU.Mathlib.BorelCaratheodory.norm_le_of_re_le (R := R) (M := M) (r := r)
    (f := fun w => h w - h 0) hRpos hMpos (by linarith) (hh.sub_const _).differentiableOn
    (sub_self _) hreF (show ‖z‖ ≤ r by linarith)
  have hRr : R - r = r := by rw [hR]; ring
  rw [hRr, mul_div_assoc, div_self (by linarith), mul_one] at hBC
  have htri : ‖h z‖ ≤ ‖h z - h 0‖ + ‖h 0‖ := by
    have := norm_add_le (h z - h 0) (h 0); simpa using this
  have hRρ : R ^ ρ = 2 ^ ρ * r ^ ρ := Real.mul_rpow (by norm_num) (by linarith)
  have hrρ : 1 ≤ r ^ ρ := Real.one_le_rpow hr1 hρ
  have h2ρ : 0 ≤ C * 2 ^ ρ := mul_nonneg hC.le (Real.rpow_nonneg (by norm_num) _)
  have hla := abs_nonneg (Real.log A)
  have hh0 := norm_nonneg (h 0)
  rw [hM, hRρ] at hBC
  nlinarith [mul_nonneg (by linarith : (0:ℝ) ≤ 2 * |Real.log A| + 3 * ‖h 0‖ + 2)
    (by linarith : (0:ℝ) ≤ r ^ ρ - 1)]

/-! ## The zero-free step of Hadamard -/

/-- **Zero-free Hadamard.** A zero-free entire function of order `≤ ρ` (`0 ≤ ρ`) is the
exponential of a polynomial of degree `≤ ρ`. -/
theorem exists_polynomial_of_zeroFree {f : ℂ → ℂ} {ρ : ℝ}
    (hf : QOU.Mathlib.HadamardFactorization.IsEntireOfOrderLE f ρ) (hρ : 0 ≤ ρ)
    (hzero : ∀ z, f z ≠ 0) :
    ∃ g : Polynomial ℂ, (g.natDegree : ℝ) ≤ ρ ∧ ∀ z, f z = Complex.exp (g.eval z) := by
  obtain ⟨hd, A, C, hC, hb⟩ := hf
  obtain ⟨h, hhd, hfe⟩ := exists_entire_log hd hzero
  have hA : 0 < A := by
    by_contra hA
    push_neg at hA
    have h1 := mul_nonpos_of_nonpos_of_nonneg hA (Real.exp_pos (C * ‖(0 : ℂ)‖ ^ ρ)).le
    have h2 := norm_pos_iff.mpr (hzero 0)
    linarith [hb 0]
  have hb' : ∀ z, ‖Complex.exp (h z)‖ ≤ A * Real.exp (C * ‖z‖ ^ ρ) := fun z => by
    rw [← hfe z]; exact hb z
  obtain ⟨K, hK⟩ := exists_norm_le_of_norm_exp_le hhd hρ hC hA hb'
  obtain ⟨g, hdeg, hg⟩ := exists_polynomial_of_norm_le hhd hρ hK
  exact ⟨g, hdeg, fun z => by rw [hfe z, hg z]⟩

/-- Non-vacuity: the hypotheses are satisfiable with a nonconstant exponent — `exp` itself,
of order `≤ 1`, is zero-free. -/
example : ∃ g : Polynomial ℂ, (g.natDegree : ℝ) ≤ 1 ∧ ∀ z, Complex.exp z = Complex.exp (g.eval z) :=
  exists_polynomial_of_zeroFree QOU.Mathlib.HadamardFactorization.isEntireOfOrderLE_exp
    zero_le_one (fun z => Complex.exp_ne_zero z)

end QOU.Mathlib.HadamardZeroFree
