import QOU.LiftingDescent.GmFormalLog
import Mathlib.RingTheory.PowerSeries.WellKnown

/-!
# The formal exponential of `G_m`: `log` is an isomorphism `(1 + t K⟦t⟧, ×) ≃ (t K⟦t⟧, +)`

`GmFormalLog.lean` proves that `formalLog f = ∫ f′/f` is a homomorphism. This file supplies the
inverse, so the logarithm is an **isomorphism** from the `K⟦t⟧`-points of `Ĝ_m` (series with
constant term `1`) onto those of `Ĝ_a` (series with constant term `0`), over a field `K` of
characteristic `0`.

* `gmExp h`: the solution of `E′ = h′ E`, `E(0) = 1`, built coefficient by coefficient
  (`(n+1) e_{n+1} = Σ_{i ≤ n} (h′)_i e_{n−i}`). No composition of series and no analysis.
* `formalLog_gmExp`: `log (exp h) = h` when `h(0) = 0`.
* `formalLog_injective`: `log` is injective on series with constant term `1`.
* `gmExp_formalLog`: `exp (log f) = f` when `f(0) = 1`.
* `gmExp_add`: `exp (h₁ + h₂) = exp h₁ · exp h₂`.
* `gmExp_C_mul_X`: `exp (a t) = Σ aⁿ tⁿ / n!`, i.e. Mathlib's `rescale a (exp K)`. In particular
  `a = 1/2` gives the series whose truncations are the associator exponentials
  `expHalfTrunc N = Σ_{k<N} X^k / (2^k k!)` (`coeff_gmExp_half`): **the hexagon exponential is the
  `G_m` point with logarithm `t/2`.**

So the categorical logarithm (the energy reading, `invLogDeriv_eq`) and the exponential that the
associator tower uses are the two halves of one isomorphism `Ĝ_m ≅ Ĝ_a`.

Pure algebra: power series over `K`, no measured values.
-/

namespace QOU.FormalGroups.GmLog

open PowerSeries

noncomputable section

variable {K : Type*} [Field K] [CharZero K]

/-! ### Derivative zero means constant; `log` is injective on `1 + t K⟦t⟧` -/

theorem eq_C_of_derivative_eq_zero {f : K⟦X⟧} (h : d⁄dX K f = 0) : f = C (constantCoeff f) := by
  apply derivative.ext
  · rw [h, derivative_C]
  · rw [constantCoeff_C]

omit [CharZero K] in
theorem mul_inv_eq_one {f : K⟦X⟧} (hf : constantCoeff f ≠ 0) : f * f⁻¹ = 1 :=
  PowerSeries.mul_inv_cancel f hf

theorem formalLog_inv {g : K⟦X⟧} (hg : constantCoeff g ≠ 0) :
    formalLog g⁻¹ = -formalLog g := by
  have hgi : constantCoeff g⁻¹ ≠ 0 := by
    rw [PowerSeries.constantCoeff_inv]; exact inv_ne_zero hg
  have h := formalLog_mul hg hgi
  rw [mul_inv_eq_one hg, formalLog_one] at h
  linear_combination -h

/-- **`log` is injective on series with constant term `1`.** -/
theorem formalLog_injective {f g : K⟦X⟧} (hf : constantCoeff f = 1) (hg : constantCoeff g = 1)
    (h : formalLog f = formalLog g) : f = g := by
  have hf0 : constantCoeff f ≠ 0 := by rw [hf]; exact one_ne_zero
  have hg0 : constantCoeff g ≠ 0 := by rw [hg]; exact one_ne_zero
  have hgi : constantCoeff g⁻¹ ≠ 0 := by
    rw [PowerSeries.constantCoeff_inv]; exact inv_ne_zero hg0
  set u := f * g⁻¹ with hu
  have hu1 : constantCoeff u = 1 := by
    rw [hu, map_mul, PowerSeries.constantCoeff_inv, hf, hg, inv_one, mul_one]
  have hu0 : constantCoeff u ≠ 0 := by rw [hu1]; exact one_ne_zero
  have hlog : formalLog u = 0 := by
    rw [hu, formalLog_mul hf0 hgi, formalLog_inv hg0, h, add_neg_cancel]
  have hd : d⁄dX K u = 0 := by
    have h1 := derivative_formalLog u
    rw [hlog, map_zero] at h1
    have h2 : d⁄dX K u = d⁄dX K u * u⁻¹ * u := by
      rw [mul_assoc, mul_comm u⁻¹ u, mul_inv_eq_one hu0, mul_one]
    rw [h2, ← h1, zero_mul]
  have huC := eq_C_of_derivative_eq_zero hd
  rw [hu1, map_one] at huC
  calc f = f * g⁻¹ * g := by rw [mul_assoc, mul_comm g⁻¹ g, mul_inv_eq_one hg0, mul_one]
    _ = g := by rw [← hu, huC, one_mul]

/-! ### The exponential, coefficient by coefficient -/

/-- Coefficients of `exp h`: `e₀ = 1`, `(n+1) e_{n+1} = Σ_{i ≤ n} (h′)_i e_{n−i}`. -/
def expCoeff (h : K⟦X⟧) : ℕ → K
  | 0 => 1
  | n + 1 => (∑ i ∈ Finset.range (n + 1), coeff i (d⁄dX K h) * expCoeff h (n - i)) / (n + 1)
decreasing_by omega

/-- **The formal exponential** of `G_m`. -/
def gmExp (h : K⟦X⟧) : K⟦X⟧ := mk (expCoeff h)

omit [CharZero K] in
theorem constantCoeff_gmExp (h : K⟦X⟧) : constantCoeff (gmExp h) = 1 := by
  rw [← coeff_zero_eq_constantCoeff_apply, gmExp, coeff_mk, expCoeff]

/-- **`exp h` solves `E′ = h′ E`.** -/
theorem derivative_gmExp (h : K⟦X⟧) : d⁄dX K (gmExp h) = d⁄dX K h * gmExp h := by
  ext n
  rw [coeff_derivative, gmExp, coeff_mk, expCoeff, coeff_mul,
    Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk]
  have : ((n : K) + 1) ≠ 0 := by exact_mod_cast Nat.succ_ne_zero n
  simp only [coeff_mk]
  field_simp

theorem formalLog_gmExp {h : K⟦X⟧} (h0 : constantCoeff h = 0) : formalLog (gmExp h) = h := by
  apply derivative.ext
  · rw [derivative_formalLog, derivative_gmExp, mul_assoc,
      mul_inv_eq_one (by rw [constantCoeff_gmExp]; exact one_ne_zero), mul_one]
  · rw [constantCoeff_formalLog, h0]

/-- **`exp (log f) = f`** on `1 + t K⟦t⟧`. -/
theorem gmExp_formalLog {f : K⟦X⟧} (hf : constantCoeff f = 1) : gmExp (formalLog f) = f :=
  formalLog_injective (constantCoeff_gmExp _) hf (formalLog_gmExp (constantCoeff_formalLog f))

/-- **`exp` is a homomorphism `G_a → G_m`.** -/
theorem gmExp_add {h₁ h₂ : K⟦X⟧} (h₁0 : constantCoeff h₁ = 0) (h₂0 : constantCoeff h₂ = 0) :
    gmExp (h₁ + h₂) = gmExp h₁ * gmExp h₂ := by
  have c1 : constantCoeff (gmExp h₁) ≠ 0 := by rw [constantCoeff_gmExp]; exact one_ne_zero
  have c2 : constantCoeff (gmExp h₂) ≠ 0 := by rw [constantCoeff_gmExp]; exact one_ne_zero
  apply formalLog_injective (constantCoeff_gmExp _)
  · rw [map_mul, constantCoeff_gmExp, constantCoeff_gmExp, mul_one]
  · rw [formalLog_mul c1 c2, formalLog_gmExp h₁0, formalLog_gmExp h₂0,
      formalLog_gmExp (by rw [map_add, h₁0, h₂0, add_zero])]

/-! ### `exp (a t)` is Mathlib's `rescale a (exp K)`; the associator exponential -/

theorem derivative_rescale_exp (a : K) :
    d⁄dX K (rescale a (exp K)) = C a * rescale a (exp K) := by
  ext n
  rw [coeff_derivative, coeff_C_mul, coeff_rescale, coeff_rescale, coeff_exp, coeff_exp]
  simp only [eq_ratCast, Rat.cast_div, Rat.cast_one, Rat.cast_natCast, Nat.factorial_succ]
  have h1 : ((n.factorial : ℕ) : K) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero n
  have h2 : ((n : K) + 1) ≠ 0 := by exact_mod_cast Nat.succ_ne_zero n
  push_cast
  field_simp
  ring

theorem formalLog_rescale_exp (a : K) : formalLog (rescale a (exp K)) = C a * X := by
  have hc : constantCoeff (rescale a (exp K)) = 1 := by
    rw [← coeff_zero_eq_constantCoeff_apply, coeff_rescale, coeff_exp]; simp
  apply derivative.ext
  · rw [derivative_formalLog, derivative_rescale_exp, mul_assoc,
      mul_inv_eq_one (by rw [hc]; exact one_ne_zero), mul_one, Derivation.leibniz, derivative_C,
      derivative_X, smul_eq_mul, smul_zero, add_zero, mul_one]
  · rw [constantCoeff_formalLog, map_mul, constantCoeff_X, mul_zero]

/-- **`exp (a t) = Σ aⁿ tⁿ/n!`.** -/
theorem gmExp_C_mul_X (a : K) : gmExp (C a * X) = rescale a (exp K) := by
  have hc : constantCoeff (rescale a (exp K)) = 1 := by
    rw [← coeff_zero_eq_constantCoeff_apply, coeff_rescale, coeff_exp]; simp
  rw [← formalLog_rescale_exp a, gmExp_formalLog hc]

/-- **The associator exponential is the `G_m` point with logarithm `t/2`:** the coefficients of
`exp(t/2)` are `1/(2ᵏ k!)`, those of `expHalfTrunc`. -/
theorem coeff_gmExp_half (k : ℕ) :
    coeff k (gmExp (C (1 / 2 : K) * X)) = ((2 ^ k * k.factorial : ℕ) : K)⁻¹ := by
  rw [gmExp_C_mul_X, coeff_rescale, coeff_exp]
  simp only [eq_ratCast, Rat.cast_div, Rat.cast_one, Rat.cast_natCast]
  push_cast
  field_simp
  rw [← mul_pow]; norm_num

end

end QOU.FormalGroups.GmLog
