/-
  `∑_{n∈ℤ} e^{−a(n−c)²} = √(π/a) · θ₂(−c, iπ/a)` — bean `qou-mlgp` (B).

  WHAT THIS IS FOR.  In the Laplace/saddle-point evaluation of Kashaev's sum
  (`computations/probes/one_loop_c_sigma_tetrahedral_probe.py`, which derives
  `c_σ(4₁) = 3^{−1/4}`) one replaces a DISCRETE sum over `k` by a CONTINUUM
  Gaussian integral near the saddle.  The one-loop constant is the value of that
  integral, so the whole derivation is only as good as the error in that one
  replacement.  Naive Euler–Maclaurin gives `O(a)` — the same order as the
  one-loop term itself, which would sink it.

  The identity below says the true error is `O(e^{−π²/a})`.  Writing out the
  `n = 0` term of the theta series,

      ∑_{n∈ℤ} e^{−a(n−c)²} = √(π/a) · ( 1 + 2∑_{n≥1} e^{−π²n²/a} cos(2πnc) )

  and `√(π/a) = ∫_ℝ e^{−a(x−c)²} dx` is exactly the continuum integral.  So
  sum = integral × (1 + O(e^{−π²/a})): **exponentially** small, not
  polynomially.  There is no `1/N` discretisation correction to the
  saddle-point step at all, and `c_σ` is fixed by the continuum Laplace
  integral alone.

  AT THE `4₁` SADDLE, CONCRETELY.  The tetrahedral probe computes
  `|φ''(k*)| = 2π√3/N`, so `a = |φ''|/2 = π√3/N` and

      √(π/a)   = √(N/√3)        — exactly the Laplace factor that probe uses
      e^{−π²/a} = e^{−πN/√3}    — the entire discretisation error

  which is `10^{−79}` at `N = 100`.  The measured `d log(deviation)/dN` agrees
  with `−π/√3` to 18 digits (`laplace_sum_theta_exactness_probe.py`).  Note
  also that the offset `c` — where the saddle sits relative to the integer
  lattice — enters only inside a `cos` multiplying an already exponentially
  small factor, so it is uniformly harmless.  It was never the obstacle.

  ALL THE MOMENTS AT ONCE, AND THE HIGHER REMAINDER.  Replacing `c` by
  `c + t/2a` and completing the square gives `hasSum_gaussian_theta_tilt` below,
  the exponentially-tilted sum — the moment generating function of the discrete
  Gaussian.  Differentiating it `m` times in `t` at `t = 0` gives
  `∑_k (k−c)^m e^{−a(k−c)²}`, and since `θ₂(−c′, iπ/a) = 1 + O(e^{−π²/a})`
  UNIFORMLY in the shift `c′`, every discrete Gaussian moment equals its
  continuum value to that order.  So expanding `e^R` against the Gaussian —
  which is how the cubic-and-higher remainder `R` of `φ` enters — produces for
  the SUM exactly the series it produces for the INTEGRAL: the two asymptotic
  expansions agree at every order in `1/N`, not merely at leading order.

  WHAT THIS DOES NOT COVER, STATED CAREFULLY.  The `e^{−π²/a}` rate above is for
  an EXACT Gaussian and must not be quoted for the full potential.  Measured on
  the real `4₁` cubic and quartic (`laplace_higher_remainder_probe.py`), the
  cubic/quartic terms move the relevant complex saddle and roughly HALVE the
  rate: `d(−log deviation)/dN ≈ 0.81` against the pure-Gaussian `π/√3 ≈ 1.814`.
  It stays exponential — which is the only thing the one-loop constant needs —
  but it is not the same constant.  Separately, all of this concerns the
  agreement of EXPANSIONS; a bound on the actual sums still needs the usual
  window-plus-tail control, and the integral's own `1/N` corrections are a
  different question again.

  This is the exact complement of `qou-mlgp` (A).  There the sum is
  `s_k = −∑_{j≤k} log(2 sin(jπ/N))`, whose integrand is SINGULAR at the `j = 0`
  endpoint, and the corrections are genuinely polynomial (`O(log N)`) — see
  `QOU/Knot/KashaevProdEndpoint.lean`.  Here the summand is entire and rapidly
  decaying, and Poisson summation kills every polynomial correction.

  WHAT MATHLIB ALREADY HAS, AND WHAT IT DOES NOT.  Mathlib proves the same
  transformation in un-theta'd form:
  `Complex.tsum_exp_neg_quadratic (ha : 0 < a.re) (b : ℂ)`, in
  `Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.lean`, gives
  `∑' n, cexp(−πa n² + 2πb n) = 1/a^{1/2} · ∑' n, cexp(−π/a·(n + Ib)²)`.
  Specialising `a ↦ a/π`, `b ↦ ac/π` recovers the identity below, so this file
  adds NO analytic input.  What it adds is (i) the bridge to `jacobiTheta₂` in
  the normalisation `θ₂(−c, iπ/a)`, where the exponential tail bound is legible
  and Mathlib's theta API (`JacobiTheta/Bounds.lean`) applies, and (ii) a
  `HasSum`, not just a `tsum` — summability is carried, not assumed, which the
  downstream Laplace argument needs in order to split off the tail.

  THE PROOF is one instantiation of `jacobiTheta₂_functional_equation` plus
  bookkeeping.  At `τ = ia/π`, `z = −iac/π` the theta term
  `exp(2πinz + πin²τ)` becomes `e^{ac²}·e^{−a(n−c)²}`, and the functional
  equation's prefactor `1/(−iτ)^{1/2}` becomes `(π/a)^{1/2}`.  The one fiddly
  step is that complex power, which must be identified with the real `√(π/a)`
  on the positive imaginary axis (`hcpow`, via `Complex.ofReal_cpow`).

  -- Ref: [leitner2026] QOU/Knot/KashaevProdEndpoint.lean   (the (A) complement)
  -- Ref: [leitner2026] QOU/MathlibExt/RootsOfUnityProduct.lean
  -- Ref: [leitner2026] computations/probes/one_loop_c_sigma_tetrahedral_probe.py
  -- Ref: [leitner2026] computations/probes/laplace_sum_theta_exactness_probe.py
  -- Ref: [leitner2026] computations/probes/laplace_higher_remainder_probe.py
-/
import Mathlib.NumberTheory.ModularForms.JacobiTheta.TwoVariable

namespace QOU.MathlibExt

open Complex Real

/-- The `jacobiTheta₂` term at `τ = ia/π`, `z = −iac/π` is a shifted Gaussian:
`exp(2πinz + πin²τ) = e^{ac²}·e^{−a(n−c)²}`. -/
theorem jacobiTheta₂_term_gaussian (a c : ℝ) (n : ℤ) :
    jacobiTheta₂_term n (-(Complex.I * a * c / π)) (Complex.I * a / π)
      = Complex.exp ((a : ℂ) * c ^ 2) * Complex.exp (-(a : ℂ) * ((n : ℂ) - c) ^ 2) := by
  unfold jacobiTheta₂_term
  rw [← Complex.exp_add]
  congr 1
  have hπ : (π : ℂ) ≠ 0 := by simp [Real.pi_ne_zero]
  field_simp; ring_nf; simp [Complex.I_sq]; ring

/-- `ia/π` lies in the upper half plane for `a > 0`, which is what
`jacobiTheta₂` needs for convergence. -/
theorem im_I_mul_div_pi_pos (a : ℝ) (ha : 0 < a) : 0 < (Complex.I * a / π).im := by
  have hπ : (0:ℝ) < π := Real.pi_pos
  simp [Complex.div_im, Complex.mul_im, Complex.mul_re, Complex.normSq_apply]
  positivity

/-- The shifted Gaussian family is summable over `ℤ`, with sum the theta value —
this is `hasSum_jacobiTheta₂_term` transported along
`jacobiTheta₂_term_gaussian`. -/
theorem hasSum_gaussian_theta_aux (a c : ℝ) (ha : 0 < a) :
    HasSum (fun n : ℤ => Complex.exp ((a : ℂ) * c ^ 2) *
        Complex.exp (-(a : ℂ) * ((n : ℂ) - c) ^ 2))
      (jacobiTheta₂ (-(Complex.I * a * c / π)) (Complex.I * a / π)) := by
  have h := hasSum_jacobiTheta₂_term (-(Complex.I * (a:ℂ) * c / π)) (im_I_mul_div_pi_pos a ha)
  simpa only [jacobiTheta₂_term_gaussian a c] using h

/-- `jacobiTheta₂_functional_equation` at `τ = ia/π`, `z = −iac/π`, with the
prefactor `1/(−iτ)^{1/2}` identified as the real `(π/a)^{1/2}`. -/
theorem jacobiTheta₂_gaussian_functional_equation (a c : ℝ) (ha : 0 < a) :
    jacobiTheta₂ (-(Complex.I * a * c / π)) (Complex.I * a / π)
      = ((π / a : ℝ) : ℂ) ^ ((1 : ℂ) / 2) * Complex.exp ((a : ℂ) * c ^ 2)
        * jacobiTheta₂ (-(c : ℂ)) (Complex.I * π / a) := by
  have hπ : (π : ℂ) ≠ 0 := by simp [Real.pi_ne_zero]
  have haC : (a : ℂ) ≠ 0 := by exact_mod_cast ha.ne'
  have e1 : -Complex.I * (Complex.I * (a : ℂ) / π) = ((a / π : ℝ) : ℂ) := by
    push_cast; field_simp; ring_nf; simp [Complex.I_sq]
  have e2 : -(Complex.I * (a : ℂ) * c / π) / (Complex.I * a / π) = -(c : ℂ) := by
    field_simp
  have e3 : -1 / (Complex.I * (a : ℂ) / π) = Complex.I * π / a := by
    field_simp; ring_nf; simp [Complex.I_sq]
  have e4 : -(π : ℂ) * Complex.I * (-(Complex.I * (a:ℂ) * c / π)) ^ 2 / (Complex.I * a / π)
      = (a : ℂ) * c ^ 2 := by
    field_simp; ring_nf; simp [Complex.I_sq]
  rw [jacobiTheta₂_functional_equation, e1, e2, e3, e4]
  have hcpow : (1 : ℂ) / ((a / π : ℝ) : ℂ) ^ ((1 : ℂ) / 2)
      = ((π / a : ℝ) : ℂ) ^ ((1 : ℂ) / 2) := by
    rw [show ((1:ℂ)/2) = (((1:ℝ)/2 : ℝ) : ℂ) by norm_num]
    rw [← Complex.ofReal_cpow (by positivity), ← Complex.ofReal_cpow (by positivity)]
    rw [← Complex.ofReal_one, ← Complex.ofReal_div, Complex.ofReal_inj]
    rw [show (π / a : ℝ) = (a / π : ℝ)⁻¹ by field_simp]
    rw [Real.inv_rpow (by positivity)]
    simp
  rw [hcpow]

/-- **`∑_{n∈ℤ} e^{−a(n−c)²} = √(π/a) · θ₂(−c, iπ/a)`**, as a `HasSum`, for every
`a > 0` and every real shift `c`.

Exact — no asymptotics.  The `n = 0` term of `θ₂(−c, iπ/a)` is `1` and the rest
is `O(e^{−π²/a})`, while `√(π/a) = ∫_ℝ e^{−a(x−c)²} dx`; so this is the precise
statement that replacing the Laplace sum by the Laplace integral costs only an
exponentially small relative error, uniformly in the shift `c`. -/
theorem hasSum_gaussian_theta (a c : ℝ) (ha : 0 < a) :
    HasSum (fun n : ℤ => Complex.exp (-(a : ℂ) * ((n : ℂ) - c) ^ 2))
      (((π / a : ℝ) : ℂ) ^ ((1 : ℂ) / 2) * jacobiTheta₂ (-(c : ℂ)) (Complex.I * π / a)) := by
  have hne : Complex.exp ((a : ℂ) * c ^ 2) ≠ 0 := Complex.exp_ne_zero _
  have h := (hasSum_gaussian_theta_aux a c ha).mul_left (Complex.exp ((a : ℂ) * c ^ 2))⁻¹
  rw [jacobiTheta₂_gaussian_functional_equation a c ha] at h
  have hL : ∀ n : ℤ, (Complex.exp ((a : ℂ) * c ^ 2))⁻¹ *
      (Complex.exp ((a : ℂ) * c ^ 2) * Complex.exp (-(a : ℂ) * ((n : ℂ) - c) ^ 2))
        = Complex.exp (-(a : ℂ) * ((n : ℂ) - c) ^ 2) := by
    intro n; field_simp
  have hR : (Complex.exp ((a : ℂ) * c ^ 2))⁻¹ *
      (((π / a : ℝ) : ℂ) ^ ((1 : ℂ) / 2) * Complex.exp ((a : ℂ) * c ^ 2)
        * jacobiTheta₂ (-(c : ℂ)) (Complex.I * π / a))
      = ((π / a : ℝ) : ℂ) ^ ((1 : ℂ) / 2) * jacobiTheta₂ (-(c : ℂ)) (Complex.I * π / a) := by
    field_simp
  rw [hR] at h
  simpa only [hL] using h

/-- **The tilted sum — every Gaussian moment at once.**

`∑_{n∈ℤ} e^{−a(n−c)² + t(n−c)} = e^{t²/4a}·√(π/a)·θ₂(−(c + t/2a), iπ/a)`.

Completing the square is a shift of `c` by `t/2a`, so this is `hasSum_gaussian_theta`
with no new analytic input.  It is the moment generating function of the discrete
Gaussian: the `m`-th `t`-derivative at `0` is `∑_k (k−c)^m e^{−a(k−c)²}`, and the
`e^{t²/4a}·√(π/a)` prefactor is exactly the CONTINUUM generating function
`∫_ℝ e^{−ax²+tx} dx`.  The entire discrete-vs-continuum discrepancy, at every
moment, is therefore the single factor `θ₂(−(c + t/2a), iπ/a) = 1 + O(e^{−π²/a})`,
uniformly in `c` and `t`.

That is the sense in which the cubic-and-higher remainder of a Laplace potential
cannot produce a polynomial correction: it enters only through moments, and the
moments are exponentially faithful.  (The differentiation step itself is not
formalised here — see the file header.) -/
theorem hasSum_gaussian_theta_tilt (a c t : ℝ) (ha : 0 < a) :
    HasSum (fun n : ℤ => Complex.exp (-(a : ℂ) * ((n : ℂ) - c) ^ 2
        + (t : ℂ) * ((n : ℂ) - c)))
      (Complex.exp ((t : ℂ) ^ 2 / (4 * a)) * ((π / a : ℝ) : ℂ) ^ ((1 : ℂ) / 2)
        * jacobiTheta₂ (-((c + t / (2 * a) : ℝ) : ℂ)) (Complex.I * π / a)) := by
  have haC : (a : ℂ) ≠ 0 := by exact_mod_cast ha.ne'
  have h := (hasSum_gaussian_theta a (c + t / (2 * a)) ha).mul_left
    (Complex.exp ((t : ℂ) ^ 2 / (4 * a)))
  have hsq : ∀ n : ℤ, Complex.exp ((t : ℂ) ^ 2 / (4 * a)) *
      Complex.exp (-(a : ℂ) * ((n : ℂ) - ((c + t / (2 * a) : ℝ) : ℂ)) ^ 2)
        = Complex.exp (-(a : ℂ) * ((n : ℂ) - c) ^ 2 + (t : ℂ) * ((n : ℂ) - c)) := by
    intro n
    rw [← Complex.exp_add]
    congr 1
    push_cast
    field_simp
    ring
  simpa only [hsq, mul_assoc] using h

/-- The `tsum` form of `hasSum_gaussian_theta`. -/
theorem tsum_gaussian_theta (a c : ℝ) (ha : 0 < a) :
    ∑' n : ℤ, Complex.exp (-(a : ℂ) * ((n : ℂ) - c) ^ 2)
      = ((π / a : ℝ) : ℂ) ^ ((1 : ℂ) / 2) * jacobiTheta₂ (-(c : ℂ)) (Complex.I * π / a) :=
  (hasSum_gaussian_theta a c ha).tsum_eq

/-- The real form: `∑_{n∈ℤ} e^{−a(n−c)²} = √(π/a)·Re θ₂(−c, iπ/a)`, as a
`HasSum` over `ℤ` of nonnegative reals.

(The theta value is in fact real — pairing `n ↔ −n` — but taking the real part
is enough for the Laplace application and avoids that extra argument.) -/
theorem hasSum_gaussian_theta_real (a c : ℝ) (ha : 0 < a) :
    HasSum (fun n : ℤ => Real.exp (-a * ((n : ℝ) - c) ^ 2))
      (Real.sqrt (π / a) * (jacobiTheta₂ (-(c : ℂ)) (Complex.I * π / a)).re) := by
  have hcast : ∀ n : ℤ, Complex.exp (-(a : ℂ) * ((n : ℂ) - c) ^ 2)
      = ((Real.exp (-a * ((n : ℝ) - c) ^ 2) : ℝ) : ℂ) := by
    intro n
    rw [Complex.ofReal_exp]
    congr 1
    push_cast
    ring
  have hpre : ((π / a : ℝ) : ℂ) ^ ((1 : ℂ) / 2) = ((Real.sqrt (π / a) : ℝ) : ℂ) := by
    rw [show ((1:ℂ)/2) = (((1:ℝ)/2 : ℝ) : ℂ) by norm_num]
    rw [← Complex.ofReal_cpow (by positivity)]
    rw [Real.sqrt_eq_rpow]
  have h := Complex.hasSum_re (hasSum_gaussian_theta a c ha)
  simp only [hcast, hpre, Complex.ofReal_re, Complex.mul_re, Complex.ofReal_im,
    zero_mul, sub_zero] at h
  exact h

end QOU.MathlibExt
