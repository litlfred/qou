import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Tactic
import QOU.Mass.KZLevelFromHeckeNormalisation

/-!
# The twist exponent is never real — `e^{2πiμ} = −q²` forces `Im μ = −ln q / π`

Bean `qou-d0qq`, framework-side connection plan §C step 4
(`docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md`).

## Where this sits

`UntwistedMonodromyPrune` showed that no finite-order or quasi-unipotent (untwisted
Gauss–Manin) monodromy has an eigenvalue of modulus `> 1`, so the framework's geometric
connection cannot by itself produce the Hecke eigenvalue ratio `−q²` with real `q > 1`. The
surviving candidate is a **twisted** period — a local system with exponent `μ`, whose
pseudo-reflection monodromy has eigenvalues `{1, e^{2πiμ}}` (Deligne–Mostow (2.11)). Matching
the Hecke pair `{q, −q⁻¹}` up to the overall rescaling that `KZLevelFromHeckeNormalisation`
already handles means matching the **ratio**: `e^{2πiμ} = −q²`.

## What is proved

* `norm_exp_two_pi_I_mul` — `‖e^{2πiμ}‖ = e^{−2π Im μ}`.
* `im_eq_of_exp_eq_neg_sq` — if `e^{2πiμ} = −q²` with real `q > 0`, then
  `Im μ = −ln q / π`. The imaginary part of the exponent **is** the level: with the
  block's `ħ = (2/iπ) ln q`, `Im μ = −(π/2)·(ħ/i)·(1/π)`, i.e. `μ` and `ħ` carry the same
  `ln q`, so the "level" of `KZLevelFromHeckeNormalisation` and the twist exponent here are
  two names for one number.
* `im_ne_zero_of_exp_eq_neg_sq` — for `q > 1` that imaginary part is **non-zero**: no
  twisted period with a *real* exponent — no unitary local system, no rational twist, no
  root-of-unity twist — gives the Hecke ratio. Scope-(b): the invariant is the modulus of the
  monodromy eigenvalue. `not_exp_eq_neg_sq_of_im_eq_zero` is the same statement in refutation
  form.
* `rescaled_pair` — the pseudo-reflection pair `{1, e^{2πiμ}}`, rescaled by any `c` with
  product `−1`, becomes `{±q, ∓q⁻¹}`: `c² = q⁻²` and `(c·e^{2πiμ})² = q²`, through
  `KZLevelFromHeckeNormalisation.eigen_sq_of_product_ratio`.

## What is NOT established

Nothing here says the substrate connection *is* a twisted period, or derives `μ`. It says what
`μ` would have to be if it were — a non-real exponent carrying `ln q₀` — and that a
real-exponent twist is excluded. Under the 2026-08-02 forever-gate `q₀` is an input, so `μ(q₀)`
is a label, not a derivation; the twist itself remains the one thing the framework does not
supply (§C step 2, `colour_cubic_abelian_twist_holonomy_probe`: the abelianised Cartan
connection contributes zero twist). Real-valued only where the modulus and the logarithm
live; `μ` and the eigenvalues are complex.
-/

namespace QOU.Mass.TwistedPeriodEigenvalueRatio

open Complex Real

/-- `‖e^{2πiμ}‖ = e^{−2π·Im μ}`. -/
theorem norm_exp_two_pi_I_mul (μ : ℂ) :
    ‖Complex.exp (2 * π * I * μ)‖ = Real.exp (-(2 * π * μ.im)) := by
  rw [Complex.norm_exp]
  congr 1
  simp [mul_comm, mul_left_comm]

/-- **The exponent's imaginary part is the level.** If `e^{2πiμ} = −q²` with real `q > 0`,
then `Im μ = −ln q / π`. -/
theorem im_eq_of_exp_eq_neg_sq (μ : ℂ) (q : ℝ) (hq : 0 < q)
    (h : Complex.exp (2 * π * I * μ) = -((q : ℂ) ^ 2)) :
    μ.im = -Real.log q / π := by
  have hnorm : Real.exp (-(2 * π * μ.im)) = q ^ 2 := by
    rw [← norm_exp_two_pi_I_mul, h, norm_neg, norm_pow, Complex.norm_real,
      Real.norm_eq_abs, abs_of_pos hq]
  have hlog : -(2 * π * μ.im) = Real.log (q ^ 2) := by
    rw [← hnorm, Real.log_exp]
  rw [Real.log_pow] at hlog
  have hpi : (π : ℝ) ≠ 0 := Real.pi_ne_zero
  field_simp
  push_cast at hlog
  linarith

/-- **The twist exponent is never real.** For real `q > 1`, `e^{2πiμ} = −q²` forces
`Im μ ≠ 0`. -/
theorem im_ne_zero_of_exp_eq_neg_sq (μ : ℂ) (q : ℝ) (hq : 1 < q)
    (h : Complex.exp (2 * π * I * μ) = -((q : ℂ) ^ 2)) : μ.im ≠ 0 := by
  rw [im_eq_of_exp_eq_neg_sq μ q (by linarith) h]
  have hlog : 0 < Real.log q := Real.log_pos hq
  have hpi : 0 < (π : ℝ) := Real.pi_pos
  intro h0
  have : Real.log q = 0 := by
    field_simp at h0
    linarith
  linarith

/-- Refutation form: a **real** exponent never gives the Hecke ratio. Scope-(b), invariant =
the modulus of the monodromy eigenvalue. -/
theorem not_exp_eq_neg_sq_of_im_eq_zero (μ : ℂ) (q : ℝ) (hq : 1 < q) (h0 : μ.im = 0) :
    Complex.exp (2 * π * I * μ) ≠ -((q : ℂ) ^ 2) :=
  fun h => im_ne_zero_of_exp_eq_neg_sq μ q hq h h0

/-- The pseudo-reflection pair `{1, e^{2πiμ}}`, rescaled by `c` so that the product is `−1`,
is the Hecke pair `{±q, ∓q⁻¹}`: `c² = q⁻²` and `(c·e^{2πiμ})² = q²`. -/
theorem rescaled_pair (μ : ℂ) (q : ℝ) (hq : q ≠ 0) (c : ℂ) (hc : c ≠ 0)
    (h : Complex.exp (2 * π * I * μ) = -((q : ℂ) ^ 2))
    (hprod : (c * Complex.exp (2 * π * I * μ)) * c = -1) :
    c ^ 2 = ((q : ℂ) ^ 2)⁻¹ ∧ (c * Complex.exp (2 * π * I * μ)) ^ 2 = (q : ℂ) ^ 2 := by
  have hqC : (q : ℂ) ≠ 0 := by exact_mod_cast hq
  have hratio : (c * Complex.exp (2 * π * I * μ)) / c = -((q : ℂ) ^ 2) := by
    rw [mul_div_cancel_left₀ _ hc, h]
  have hsq := QOU.Mass.KZLevelFromHeckeNormalisation.eigen_sq_of_product_ratio hqC hc hprod hratio
  refine ⟨hsq, ?_⟩
  rw [mul_pow, hsq, h]
  have hq2 : (q : ℂ) ^ 2 ≠ 0 := pow_ne_zero 2 hqC
  field_simp

/-- Vanishing difference form of `norm_exp_two_pi_I_mul`. -/
theorem norm_exp_two_pi_I_mul_sub_eq_zero (μ : ℂ) :
    ‖Complex.exp (2 * π * I * μ)‖ - Real.exp (-(2 * π * μ.im)) = 0 := by
  rw [norm_exp_two_pi_I_mul μ, sub_self]

end QOU.Mass.TwistedPeriodEigenvalueRatio
