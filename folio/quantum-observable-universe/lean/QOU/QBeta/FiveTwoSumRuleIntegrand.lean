/-
# The 5₂ sum-rule integrand: Vieta, the reciprocal cubic, and its positivity

The 2026-08-06 restatement (bean `qou-0yqu`, Route 5) rewrites the 5₂ saddle
sum rule with no dilogarithm:

    A = Σⱼ Li₂(yⱼ) = −∫₀¹ log(1 − 2z + 3z² − z³) / z  dz

This file proves the **algebraic and positivity skeleton** of that chain,
sorry-free. It does *not* prove the sum rule; see "Scope" below.

## The crux, and why it matters

The reciprocal cubic factors as

    1 − 2z + 3z² − z³ = (1 − z)³ + z                    `recipCubic_eq`

from which positivity on `[0,1]` is immediate (`recipCubic_pos`): both
summands are non-negative there and they never vanish together.

That positivity is the whole reason the restatement is worth having. The
defining series `Σₙ pₙ/n²` **diverges** — `|y₁| = 1.52 > 1` — which is what
made analytic continuation of `Li₂` to `|z| > 1` look mandatory (bean
`qou-gkco`). But the *integral* is over a region where the integrand is
regular, so it converges anyway. No complex dilogarithm, no branch cut.

## Scope — what is proved here and what is not

**Proved, sorry-free, over a generic `CommRing` where possible (§7c):**

* `prod_one_sub_mul_eq` — Vieta: `∏ⱼ(1 − yⱼz) = 1 − 2z + 3z² − z³`;
* `recipCubic_eq` — `1 − 2z + 3z² − z³ = (1−z)³ + z`;
* `recipCubic_pos` — hence `0 < 1 − 2z + 3z² − z³` on `[0,1]` (over `ℝ`);
* `pow_succ_rec` / `powerSum_rec` — the power sums obey the cubic's recurrence,
  which is why `pₙ ∈ ℤ` and the generating function is the reciprocal cubic;
* `recipCubic_ge_half` / `recipCubic_le_one` / `abs_log_recipCubic_le` —
  `|log P(z)| ≤ 4z`, so the apparent singularity of `log P(z)/z` at `z = 0` is
  removable;
* `intervalIntegrable_log_recipCubic_div` — hence **the integral on the right
  of the displayed identity converges**. Route 5 is now a statement about a
  well-defined real number, not a formal expression.

**NOT proved here** (and not stubbed — no `sorry`, no axiom):

* that the integral equals `A` (needs `∫₀¹ log(1−yz)/z = −Li₂(y)`);
* the closed-form evaluation of the integral, i.e. the sum rule itself. **The 5₂ sum
rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. Routes 1–4 in
`qou-0yqu` are dead and Route 5 is a restatement, not a solution; the route that
worked was the complex five-term identity (Routes 51–70).

-- Ref: [leitner2026] bean qou-0yqu Route 5; docs/coordination/1ppq-qbeta.md
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import QOU.MathlibExt.ComplexDilogarithm

namespace QOU.QBeta.FiveTwo

open Complex

/-! ### Vieta: the reciprocal cubic is the product over the roots -/

/-- `∏ⱼ (1 − yⱼ z) = 1 − 2z + 3z² − z³` for any three ring elements with the
5₂ cubic's elementary symmetric functions `e₁ = 2`, `e₂ = 3`, `e₃ = 1`.

This is the generating-function step: it is what makes the power sums
`pₙ = Σⱼ yⱼⁿ` integers and identifies `Σₙ pₙzⁿ/n` with `−log` of this cubic. -/
theorem prod_one_sub_mul_eq {R : Type*} [CommRing R] {y₁ y₂ y₃ : R}
    (e1 : y₁ + y₂ + y₃ = 2) (e2 : y₁ * y₂ + y₁ * y₃ + y₂ * y₃ = 3)
    (e3 : y₁ * y₂ * y₃ = 1) (z : R) :
    (1 - y₁ * z) * (1 - y₂ * z) * (1 - y₃ * z) = 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := by
  linear_combination (-z) * e1 + z ^ 2 * e2 + (-z ^ 3) * e3

/-! ### The crux: the reciprocal cubic is `(1−z)³ + z` -/

/-- `1 − 2z + 3z² − z³ = (1 − z)³ + z`, over any commutative ring.

A one-line `ring` identity, but it is the load-bearing one: it exhibits the
integrand as a sum of two pieces that are separately non-negative on `[0,1]`. -/
theorem recipCubic_eq {R : Type*} [CommRing R] (z : R) :
    1 - 2 * z + 3 * z ^ 2 - z ^ 3 = (1 - z) ^ 3 + z := by ring

/-- **The integrand never vanishes on `[0,1]`.**

Immediate from `recipCubic_eq`: on `[0,1]` both `(1−z)³` and `z` are
non-negative, and at `z = 0` the first is `1`.

This is what makes `∫₀¹ log(1 − 2z + 3z² − z³)/z dz` a convergent *real*
integral, even though the series defining `Σⱼ Li₂(yⱼ)` diverges because
`|y₁| = 1.52 > 1`. It is the technical content behind "Route 5 bypasses the
complex-`Li₂` continuation". -/
theorem recipCubic_pos {z : ℝ} (h0 : 0 ≤ z) (h1 : z ≤ 1) :
    0 < 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := by
  rw [recipCubic_eq]
  have hc : (0 : ℝ) ≤ (1 - z) ^ 3 := pow_nonneg (by linarith) 3
  rcases eq_or_lt_of_le h0 with hz | hz
  · rw [← hz]; norm_num
  · linarith

/-! ### The power-sum recurrence

Each root satisfies the cubic, so its powers obey the associated linear
recurrence; summing over the roots gives the recurrence for `pₙ = Σⱼ yⱼⁿ`,
which is why those power sums are integers (`3, 2, −2, −7, −6, 7, 25, …`). -/

/-- A single root's powers obey the cubic's recurrence. -/
theorem pow_succ_rec {R : Type*} [CommRing R] {y : R}
    (hy : y ^ 3 = 2 * y ^ 2 - 3 * y + 1) (n : ℕ) :
    y ^ (n + 3) = 2 * y ^ (n + 2) - 3 * y ^ (n + 1) + y ^ n := by
  have h : y ^ (n + 3) = y ^ n * y ^ 3 := by ring
  rw [h, hy]; ring

/-- The power sums `pₙ = y₁ⁿ + y₂ⁿ + y₃ⁿ` obey `pₙ₊₃ = 2pₙ₊₂ − 3pₙ₊₁ + pₙ`. -/
theorem powerSum_rec {R : Type*} [CommRing R] {y₁ y₂ y₃ : R}
    (h1 : y₁ ^ 3 = 2 * y₁ ^ 2 - 3 * y₁ + 1)
    (h2 : y₂ ^ 3 = 2 * y₂ ^ 2 - 3 * y₂ + 1)
    (h3 : y₃ ^ 3 = 2 * y₃ ^ 2 - 3 * y₃ + 1) (n : ℕ) :
    y₁ ^ (n + 3) + y₂ ^ (n + 3) + y₃ ^ (n + 3)
      = 2 * (y₁ ^ (n + 2) + y₂ ^ (n + 2) + y₃ ^ (n + 2))
        - 3 * (y₁ ^ (n + 1) + y₂ ^ (n + 1) + y₃ ^ (n + 1))
        + (y₁ ^ n + y₂ ^ n + y₃ ^ n) := by
  rw [pow_succ_rec h1, pow_succ_rec h2, pow_succ_rec h3]; ring

/-! ### Eliminating the complex roots

The restatement's final step drops `y₁, y₂` entirely in favour of the real
root. Both ingredients are Vieta consequences, given that the two non-real
roots are a conjugate pair. -/

/-- **`y₃·‖y₁‖² = 1`.** With `y₂ = conj y₁`, the product relation `e₃ = 1`
says the real root is the reciprocal of `‖y₁‖²`.

This is what turns `log r` into `−½·log y₃` in the restatement, removing the
modulus of the complex root as independent data. -/
theorem real_root_mul_normSq {y₁ y₃ : ℂ}
    (e3 : y₁ * (starRingEnd ℂ) y₁ * y₃ = 1) :
    y₃ * (Complex.normSq y₁ : ℂ) = 1 := by
  rw [Complex.mul_conj] at e3
  linear_combination e3

/-- **The angle is determined by the real root.** With `y₂ = conj y₁`, Vieta's
`e₁ = 2` gives `2·Re y₁ = 2 − y₃`.

Together with `real_root_mul_normSq` (`‖y₁‖² = 1/y₃`) this yields
`cos θ = (2 − y₃)·√y₃ / 2`, the closed form used in the restatement — so the
whole sum rule depends on the single real algebraic number `y₃`. -/
theorem two_mul_re_eq {y₁ y₃ : ℂ}
    (e1 : y₁ + (starRingEnd ℂ) y₁ + y₃ = 2) :
    2 * (y₁.re : ℂ) = 2 - y₃ := by
  have h : y₁ + (starRingEnd ℂ) y₁ = 2 * (y₁.re : ℂ) := by
    rw [Complex.add_conj]; push_cast; ring
  linear_combination e1 - h

/-! ### Route 3, formalized: the Landen image cubic

Numerically (bean `qou-0yqu`, Route 3) the Landen substitution `z = y/(y−1)`
maps the three 5₂ roots exactly onto the roots of `z³ − z² + 1` — residual
`0.0` at all three. That is pure algebra, so it is proved here rather than
left as an observation.

The route is still a dead end for the sum rule: it relates `Σ Li₂(yⱼ)` to a
sum over a *different* algebraic set, giving one new equation and one new
unknown. Proving where Landen lands is not proving that it helps. -/

/-- **The Landen image of a 5₂ saddle root is a root of `z³ − z² + 1`.**

From `y² = (1−y)³` one gets `z² = 1−y` and `z³ = −y` for `z = y/(y−1)`, whence
`z³ = z² − 1`. -/
theorem landen_image_cubic {R : Type*} [Field R] {y : R} (hy : y - 1 ≠ 0)
    (h : y ^ 2 = (1 - y) ^ 3) :
    (y / (y - 1)) ^ 3 - (y / (y - 1)) ^ 2 + 1 = 0 := by
  field_simp
  linear_combination h

/-! ### The power sums are integers

`powerSum_rec` gives the recurrence; with the three base cases it identifies
`pₙ = Σⱼ yⱼⁿ` with an explicitly integer sequence. This is the formal content
of the observed table `3, 2, −2, −7, −6, 7, 25, 23, −22, …`. -/

/-- The integer sequence `3, 2, −2, …` obeying the 5₂ cubic's recurrence. -/
def pSeq : ℕ → ℤ
  | 0 => 3
  | 1 => 2
  | 2 => -2
  | (n + 3) => 2 * pSeq (n + 2) - 3 * pSeq (n + 1) + pSeq n

/-- **`Σⱼ yⱼⁿ = pSeq n`, an integer**, for any three elements with the 5₂
cubic's `e₁ = 2`, `e₂ = 3` each satisfying the cubic.

Base cases: `p₀ = 3`, `p₁ = e₁ = 2`, `p₂ = e₁² − 2e₂ = 4 − 6 = −2`. -/
theorem powerSum_eq_pSeq {R : Type*} [CommRing R] {y₁ y₂ y₃ : R}
    (e1 : y₁ + y₂ + y₃ = 2) (e2 : y₁ * y₂ + y₁ * y₃ + y₂ * y₃ = 3)
    (h1 : y₁ ^ 3 = 2 * y₁ ^ 2 - 3 * y₁ + 1)
    (h2 : y₂ ^ 3 = 2 * y₂ ^ 2 - 3 * y₂ + 1)
    (h3 : y₃ ^ 3 = 2 * y₃ ^ 2 - 3 * y₃ + 1) :
    ∀ n : ℕ, y₁ ^ n + y₂ ^ n + y₃ ^ n = (pSeq n : R)
  | 0 => by norm_num [pSeq]
  | 1 => by simpa [pSeq] using e1
  | 2 => by
      have : y₁ ^ 2 + y₂ ^ 2 + y₃ ^ 2 = (y₁ + y₂ + y₃) ^ 2
          - 2 * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) := by ring
      rw [this, e1, e2]; simp [pSeq]; norm_num
  | (n + 3) => by
      have ih0 := powerSum_eq_pSeq e1 e2 h1 h2 h3 n
      have ih1 := powerSum_eq_pSeq e1 e2 h1 h2 h3 (n + 1)
      have ih2 := powerSum_eq_pSeq e1 e2 h1 h2 h3 (n + 2)
      rw [powerSum_rec h1 h2 h3 n, ih0, ih1, ih2]
      show _ = ((2 * pSeq (n + 2) - 3 * pSeq (n + 1) + pSeq n : ℤ) : R)
      push_cast
      ring

/-! ### The field: discriminant −23

The 2026-08-07 finding (bean `qou-0yqu`) is that the 5₂ saddle cubic has
discriminant `−23`, the **smallest |discriminant| among complex cubic
fields** — which places the whole problem in the classical Zagier /
dilogarithm-ladder setting. That was established with `sympy`; it is pure
algebra, so it is machine-checked here instead.

Note what this does and does not settle. The field identification is exact and
now proved. But the classical `−23` literature (Broadhurst hep-th/9811173
eq (73): `vol(5₂) = 3·Z₂₃,₃`) computes the **volume / Bloch–Wigner** side,
which Route 2 showed carries *no* information about the sum rule. Knowing the
field is not knowing the identity. -/

/-- The discriminant of a monic cubic, as a symmetric-function identity.

`∏_{i<j}(yᵢ − yⱼ)²` expressed in the elementary symmetric functions. A pure
`ring` identity over any commutative ring. -/
theorem disc_eq_symm {R : Type*} [CommRing R] (y₁ y₂ y₃ : R) :
    ((y₁ - y₂) * (y₁ - y₃) * (y₂ - y₃)) ^ 2
      = (y₁ + y₂ + y₃) ^ 2 * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) ^ 2
        - 4 * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) ^ 3
        - 4 * (y₁ + y₂ + y₃) ^ 3 * (y₁ * y₂ * y₃)
        + 18 * (y₁ + y₂ + y₃) * (y₁ * y₂ + y₁ * y₃ + y₂ * y₃) * (y₁ * y₂ * y₃)
        - 27 * (y₁ * y₂ * y₃) ^ 2 := by
  ring

/-- **The 5₂ saddle cubic has discriminant −23.**

Immediate from `disc_eq_symm` and Vieta (`e₁ = 2`, `e₂ = 3`, `e₃ = 1`):
`4·9 − 4·27 − 4·8 + 18·6 − 27 = −23`.

`−23` is the smallest `|discriminant|` among complex cubic fields. The
reciprocal cubic `1 − 2z + 3z² − z³` and the Landen image `z³ − z² + 1` share
it, being related to this one by rational maps. -/
theorem disc_eq_neg_23 {R : Type*} [CommRing R] {y₁ y₂ y₃ : R}
    (e1 : y₁ + y₂ + y₃ = 2) (e2 : y₁ * y₂ + y₁ * y₃ + y₂ * y₃ = 3)
    (e3 : y₁ * y₂ * y₃ = 1) :
    ((y₁ - y₂) * (y₁ - y₃) * (y₂ - y₃)) ^ 2 = -23 := by
  rw [disc_eq_symm, e1, e2, e3]; norm_num

/-! ### Landen, the intermediate steps

`landen_image_cubic` proved where the substitution lands. Its two intermediate
identities were asserted in that proof's docstring; they are recorded here as
lemmas in their own right, since they are what make the route checkable. -/

/-- `z² = 1 − y` for `z = y/(y−1)`, given `y² = (1−y)³`. -/
theorem landen_sq {R : Type*} [Field R] {y : R} (hy : y - 1 ≠ 0)
    (h : y ^ 2 = (1 - y) ^ 3) : (y / (y - 1)) ^ 2 = 1 - y := by
  field_simp
  linear_combination h

/-- `z³ = −y` for `z = y/(y−1)`, given `y² = (1−y)³`. -/
theorem landen_cube {R : Type*} [Field R] {y : R} (hy : y - 1 ≠ 0)
    (h : y ^ 2 = (1 - y) ^ 3) : (y / (y - 1)) ^ 3 = -y := by
  have hsq := landen_sq hy h
  have hsplit : (y / (y - 1)) ^ 3 = (y / (y - 1)) * (y / (y - 1)) ^ 2 := by ring
  rw [hsplit, hsq]
  field_simp
  ring

/-! ### The integrand is bounded: `|log P(z)/z| ≤ 4` on `(0,1]`

Route 5's integral `−∫₀¹ log P(z)/z dz` is over an interval containing the
apparent singularity at `z = 0`. It is only apparent: `P(z) = 1 − 2z + O(z²)`,
so `log P(z) ∼ −2z` and the quotient extends continuously with value `−2`.

The quantitative form is `|log P(z)| ≤ 4z`, proved below from two elementary
bounds sandwiching `log`:

    log P ≤ P − 1        (`Real.log_le_sub_one_of_pos`)
    log P ≥ 1 − 1/P      (`Real.one_sub_inv_le_log_of_pos`)

together with `P ≥ 1/2` on `[0,1]`, which converts the second into a linear
bound. `4` is not tight — the true sup of `|log P(z)/z|` is `2`, attained in
the limit `z → 0` — but a non-tight constant is all an integrability argument
needs, and the slack keeps the polynomial certificates small. -/

/-- `P(z) ≥ 1/2` on `[0,1]`.

Certificate: `z³ ≤ z²` there, so `P − 1/2 ≥ 2z² − 2z + 1/2 = 2(z − ½)²`.
(The true minimum is `0.6151…` at `z = 1 − 1/√3`; `1/2` is the round number
below it that makes the certificate a single square.) -/
theorem recipCubic_ge_half {z : ℝ} (h0 : 0 ≤ z) (h1 : z ≤ 1) :
    1 / 2 ≤ 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := by
  nlinarith [sq_nonneg (z - 1 / 2), mul_nonneg (mul_nonneg h0 h0) (sub_nonneg.2 h1)]

/-- `P(z) ≤ 1` on `[0,1]`: `1 − P = z(1−z)(2−z) ≥ 0`. -/
theorem recipCubic_le_one {z : ℝ} (h0 : 0 ≤ z) (h1 : z ≤ 1) :
    1 - 2 * z + 3 * z ^ 2 - z ^ 3 ≤ 1 := by
  nlinarith [mul_nonneg (mul_nonneg h0 (sub_nonneg.2 h1)) (by linarith : (0 : ℝ) ≤ 2 - z)]

/-- **The integrand's numerator vanishes linearly at `0`**: `|log P(z)| ≤ 4z`
on `[0,1]`.

This is what removes the apparent singularity of `log P(z)/z` at the left
endpoint of Route 5's integral. -/
theorem abs_log_recipCubic_le {z : ℝ} (h0 : 0 ≤ z) (h1 : z ≤ 1) :
    |Real.log (1 - 2 * z + 3 * z ^ 2 - z ^ 3)| ≤ 4 * z := by
  have hpos : 0 < 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := recipCubic_pos h0 h1
  have hle : 1 - 2 * z + 3 * z ^ 2 - z ^ 3 ≤ 1 := recipCubic_le_one h0 h1
  have hhalf : 1 / 2 ≤ 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := recipCubic_ge_half h0 h1
  rw [abs_le]
  constructor
  · -- lower: `log P ≥ 1 − 1/P ≥ −4z`
    refine le_trans ?_ (Real.one_sub_inv_le_log_of_pos hpos)
    have hid : (1 : ℝ) - (1 - 2 * z + 3 * z ^ 2 - z ^ 3)⁻¹
        = ((1 - 2 * z + 3 * z ^ 2 - z ^ 3) - 1) / (1 - 2 * z + 3 * z ^ 2 - z ^ 3) := by
      rw [sub_div, div_self hpos.ne', one_div]
    rw [hid, le_div_iff₀ hpos]
    nlinarith [mul_nonneg h0 (sub_nonneg.2 h1), sq_nonneg z, sq_nonneg (z - 1 / 2),
      mul_nonneg (mul_nonneg h0 h0) (sub_nonneg.2 h1)]
  · -- upper: `log P ≤ P − 1 ≤ 0 ≤ 4z`
    refine le_trans (Real.log_le_sub_one_of_pos hpos) ?_
    nlinarith [mul_nonneg (mul_nonneg h0 (sub_nonneg.2 h1)) (by linarith : (0 : ℝ) ≤ 2 - z)]

/-- **Route 5's integral converges.**

`|log P(z)/z| ≤ 4` on `(0,1]`, immediately from `abs_log_recipCubic_le`, so the
integrand is a bounded measurable function on a set of finite measure. This is
what makes `−∫₀¹ log(1 − 2z + 3z² − z³)/z dz` a well-defined real number, and
hence what makes Route 5 a statement rather than a formal expression.

Contrast the series side: `Σₙ pₙ/n²` **diverges** (`|y₁| = 1.52 > 1`). The
restatement's whole value is that it moves the identity to a place where
convergence is elementary. -/
theorem intervalIntegrable_log_recipCubic_div :
    IntervalIntegrable (fun z : ℝ => Real.log (1 - 2 * z + 3 * z ^ 2 - z ^ 3) / z)
      MeasureTheory.volume 0 1 := by
  rw [intervalIntegrable_iff, Set.uIoc_of_le (by norm_num : (0 : ℝ) ≤ 1)]
  refine MeasureTheory.Measure.integrableOn_of_bounded (M := 4) (by simp) ?_ ?_
  · exact ((Real.measurable_log.comp (by fun_prop)).div measurable_id).aestronglyMeasurable
  · refine (MeasureTheory.ae_restrict_iff' measurableSet_Ioc).2
      (Filter.Eventually.of_forall fun z hz => ?_)
    have h0 : 0 < z := hz.1
    have h1 : z ≤ 1 := hz.2
    rw [Real.norm_eq_abs, abs_div, abs_of_pos h0, div_le_iff₀ h0]
    have hb := abs_log_recipCubic_le h0.le h1
    linarith

/-! ### The integrand identity: `Σⱼ Re Log(1 − yⱼz) = log P(z)` on `[0,1]`

This is the pointwise half of the one link still separating Route 5 from the
sum rule, namely

    Σⱼ Re Li₂(yⱼ) = −∫₀¹ log P(z)/z dz.

The other half is the complex integral representation
`Li₂(y) = −∫₀¹ Log(1 − yz)/z dz`, which for `|y| > 1` *is* the analytic
continuation (the integral converges for any `y ∉ [1,∞)` regardless of `|y|`,
unlike the series). That half is still open — see bean `qou-gkco`.

The pointwise identity below needs no dilogarithm and no continuation. It works
because the **real part** of a complex log is a genuine norm-log, and norms
multiply:

    Σⱼ Re Log(1 − yⱼz) = Σⱼ log‖1 − yⱼz‖ = log ∏ⱼ‖1 − yⱼz‖
                       = log‖∏ⱼ(1 − yⱼz)‖ = log|P(z)| = log P(z)

the last step by `recipCubic_pos`. **No `2πik` correction appears anywhere** —
taking real parts discards exactly the branch ambiguity. (Probe
`qbeta_5two_route5_branch_data_probe` gate G1 saw this numerically: the
correction is identically zero, `3.1e-61` over 40 sample points. It is not a
numerical accident; it is what this proof says.) -/

/-- **`Σⱼ Re Log(1 − yⱼz) = log P(z)` for `z ∈ [0,1]`.**

Real parts, so no branch data enters. `y₁, y₂, y₃` are any three complex
numbers with the 5₂ cubic's elementary symmetric functions. -/
theorem sum_re_log_one_sub_eq_log_recipCubic {y₁ y₂ y₃ : ℂ}
    (e1 : y₁ + y₂ + y₃ = 2) (e2 : y₁ * y₂ + y₁ * y₃ + y₂ * y₃ = 3)
    (e3 : y₁ * y₂ * y₃ = 1) {z : ℝ} (hz0 : 0 ≤ z) (hz1 : z ≤ 1) :
    (Complex.log (1 - y₁ * (z : ℂ))).re + (Complex.log (1 - y₂ * (z : ℂ))).re
        + (Complex.log (1 - y₃ * (z : ℂ))).re
      = Real.log (1 - 2 * z + 3 * z ^ 2 - z ^ 3) := by
  have hP : (0 : ℝ) < 1 - 2 * z + 3 * z ^ 2 - z ^ 3 := recipCubic_pos hz0 hz1
  have hprod : (1 - y₁ * (z : ℂ)) * (1 - y₂ * (z : ℂ)) * (1 - y₃ * (z : ℂ))
      = ((1 - 2 * z + 3 * z ^ 2 - z ^ 3 : ℝ) : ℂ) := by
    rw [prod_one_sub_mul_eq e1 e2 e3 (z : ℂ)]
    push_cast
    ring
  -- each factor is nonzero, since the product is a nonzero real
  have hne : ∀ w : ℂ, w = 1 - y₁ * (z : ℂ) ∨ w = 1 - y₂ * (z : ℂ)
      ∨ w = 1 - y₃ * (z : ℂ) → w ≠ 0 := by
    rintro w (rfl | rfl | rfl) h <;>
      · apply absurd hprod
        rw [h]
        simp only [zero_mul, mul_zero]
        exact fun hc => absurd (Complex.ofReal_eq_zero.mp hc.symm) (ne_of_gt hP)
  have h1 : (1 - y₁ * (z : ℂ)) ≠ 0 := hne _ (Or.inl rfl)
  have h2 : (1 - y₂ * (z : ℂ)) ≠ 0 := hne _ (Or.inr (Or.inl rfl))
  have h3 : (1 - y₃ * (z : ℂ)) ≠ 0 := hne _ (Or.inr (Or.inr rfl))
  -- real part of a complex log is the log of the norm
  rw [Complex.log_re, Complex.log_re, Complex.log_re,
    ← Real.log_mul (norm_ne_zero_iff.mpr h1) (norm_ne_zero_iff.mpr h2),
    ← Real.log_mul (mul_ne_zero (norm_ne_zero_iff.mpr h1) (norm_ne_zero_iff.mpr h2))
      (norm_ne_zero_iff.mpr h3)]
  congr 1
  rw [← norm_mul, ← norm_mul, hprod, Complex.norm_real, Real.norm_eq_abs,
    abs_of_pos hP]

/-! ### The three-root sum collapses to ONE real integral

The assembly step. With the pointwise identity above, plus linearity of the
integral and the fact that `Re` commutes with it, the three separate
dilogarithm-integrals over the roots become a single integral of a real
polynomial's logarithm:

    Σⱼ Re Li₂(yⱼ) = −∫₀¹ log(1 − 2z + 3z² − z³)/z dz

with `Li₂` the integral-defined `QOU.MathlibExt.cLiTwoExt`, which is the object
that makes sense at `‖y₁‖ = 1.52` where the series does not.

One integrability hypothesis per root, and only for the complex-valued
integrand — the real-part versions are derived (`Integrable.re`). For the 5₂
roots the three hypotheses are discharged by
`QOU.MathlibExt.intervalIntegrable_log_one_sub_div`, which needs
`Re(1 − yz) > 0` on `[0,1]` — true for all three.

**This does not prove the sum rule.** It makes Route 5's identity a theorem
about `cLiTwoExt`; what remains is (i) identifying `cLiTwoExt` with the `Li₂` of
the sum rule off the disc — i.e. proving it is the analytic continuation, still
open — and (ii) evaluating the resulting real integral in closed form, which is
untouched. Bean `qou-0yqu`. -/

open MeasureTheory in
/-- **`Σⱼ Re cLiTwoExt(yⱼ) = −∫₀¹ log P(z)/z dz`.** -/
theorem sum_re_cLiTwoExt_eq_integral {y₁ y₂ y₃ : ℂ}
    (e1 : y₁ + y₂ + y₃ = 2) (e2 : y₁ * y₂ + y₁ * y₃ + y₂ * y₃ = 3)
    (e3 : y₁ * y₂ * y₃ = 1)
    (h₁ : IntervalIntegrable (fun z : ℝ => Complex.log (1 - y₁ * (z : ℂ)) / (z : ℂ))
      volume 0 1)
    (h₂ : IntervalIntegrable (fun z : ℝ => Complex.log (1 - y₂ * (z : ℂ)) / (z : ℂ))
      volume 0 1)
    (h₃ : IntervalIntegrable (fun z : ℝ => Complex.log (1 - y₃ * (z : ℂ)) / (z : ℂ))
      volume 0 1) :
    (QOU.MathlibExt.cLiTwoExt y₁).re + (QOU.MathlibExt.cLiTwoExt y₂).re
        + (QOU.MathlibExt.cLiTwoExt y₃).re
      = -∫ z in (0 : ℝ)..1, Real.log (1 - 2 * z + 3 * z ^ 2 - z ^ 3) / z := by
  have hdiv : ∀ (w : ℂ) (r : ℝ), (w / (r : ℂ)).re = w.re / r := by
    intro w r
    rw [div_eq_mul_inv, ← Complex.ofReal_inv, Complex.mul_re, Complex.ofReal_re,
      Complex.ofReal_im, mul_zero, sub_zero, div_eq_mul_inv]
  have hre : ∀ y : ℂ,
      IntervalIntegrable (fun z : ℝ => Complex.log (1 - y * (z : ℂ)) / (z : ℂ)) volume 0 1 →
      IntervalIntegrable (fun z : ℝ => (Complex.log (1 - y * (z : ℂ))).re / z) volume 0 1 := by
    intro y h
    have hb : IntervalIntegrable
        (fun z : ℝ => (Complex.log (1 - y * (z : ℂ)) / (z : ℂ)).re) volume 0 1 :=
      ⟨h.1.re, h.2.re⟩
    have heq : (fun z : ℝ => (Complex.log (1 - y * (z : ℂ)) / (z : ℂ)).re)
        = fun z : ℝ => (Complex.log (1 - y * (z : ℂ))).re / z := by
      funext z
      exact hdiv (Complex.log (1 - y * (z : ℂ))) z
    rwa [heq] at hb
  have r₁ := hre y₁ h₁
  have r₂ := hre y₂ h₂
  have r₃ := hre y₃ h₃
  have key : ∀ (y : ℂ),
      IntervalIntegrable (fun z : ℝ => Complex.log (1 - y * (z : ℂ)) / (z : ℂ)) volume 0 1 →
      (QOU.MathlibExt.cLiTwoExt y).re
        = -∫ z in (0 : ℝ)..1, (Complex.log (1 - y * (z : ℂ))).re / z := by
    intro y h
    rw [QOU.MathlibExt.cLiTwoExt, Complex.neg_re]
    congr 1
    have hcomm := Complex.reCLM.intervalIntegral_comp_comm
      (μ := volume) (a := (0 : ℝ)) (b := 1) h
    rw [show ((∫ z in (0 : ℝ)..1, Complex.log (1 - y * (z : ℂ)) / (z : ℂ)).re)
        = Complex.reCLM (∫ z in (0 : ℝ)..1, Complex.log (1 - y * (z : ℂ)) / (z : ℂ))
      from rfl, ← hcomm]
    refine intervalIntegral.integral_congr fun z _ => ?_
    exact hdiv (Complex.log (1 - y * (z : ℂ))) z
  rw [key y₁ h₁, key y₂ h₂, key y₃ h₃, ← neg_add, ← neg_add,
    ← intervalIntegral.integral_add r₁ r₂,
    ← intervalIntegral.integral_add (r₁.add r₂) r₃]
  congr 1
  refine intervalIntegral.integral_congr fun z hz => ?_
  rw [Set.uIcc_of_le (by norm_num : (0 : ℝ) ≤ 1)] at hz
  rw [← add_div, ← add_div,
    sum_re_log_one_sub_eq_log_recipCubic e1 e2 e3 hz.1 hz.2]

/-! ### Closed-form disc `−23` resolvent & Masbaum cyclotomic-asymmetry odd data (`qou-dq2q`)

Companion to `computations/qbeta/five_two_disc_neg23_cyclotomic_asymmetry_probe.py`
and `computations/qbeta/five-two-disc-neg23-cyclotomic-asymmetry.witness.json`
(beans `qou-dq2q`, `qou-ynff`, `qou-5gh6`, `qou-7lim`, `qou-ized` under `qou-avtq`).

1. **Bézout inverse of `P'(ξ₀) = 3ξ₀² − 4ξ₀ + 3` and quadratic resolvent `ℚ(√−23)`:**
   In `ℤ[x]`, `(3x² − 4x + 3)(10x² − 17x + 18) = 23 + (30x − 31)(x³ − 2x² + 3x − 1)`,
   and `(-3x² + 4x - 8)(3x² - 4x + 3)² + 23 = (-27x³ + 54x² - 81x + 49)(x³ - 2x² + 3x - 1)`.
   Along the Vieta locus `ξ₀ + ξ₁ + ξ₂ = 2`, `ξ₀ξ₁ + ξ₀ξ₂ + ξ₁ξ₂ = 3`, the conjugate-saddle
   difference satisfies `(ξ₁ − ξ₂)² = −3ξ₀² + 4ξ₀ − 8`, so `((ξ₁ − ξ₂)·P'(ξ₀))² = −23`.

2. **Closed-form bar-odd (`σ₁ − σ₂`) resolvent basis projection:**
   For any `K_{5₂}`-element `α = a + bξ + cξ²`, multiplying its conjugate-saddle difference
   `(a + bξ₁ + cξ₁²) − (a + bξ₂ + cξ₂²)` by `10ξ₀² − 17ξ₀ + 18 = 23 / P'(ξ₀)` gives
     `((18b + 26c) − (17b + 22c)ξ₀ + (10b + 17c)ξ₀²) · (ξ₁ − ξ₂)`.
   At 1-loop (`b₁ = 209/2116`, `c₁ = −121/1058`), a factor of `23` cancels in the numerator,
   yielding `Δ_odd(P₁) / √−23 = (11 / (4 · 23²)) · (−10 + 7ξ₀ − 8ξ₀²)`.

3. **Closed-form `n = 1` Masbaum cyclotomic-coefficient bar-asymmetry ratio:**
   For `C_{5₂,1}(q) = −(q² + q⁴)`, the common factor `q + q⁻¹` cancels between
   `O₁(q) = −(q⁴ − q⁻⁴ + q² − q⁻²)/2` and `E₁(q) = −(q⁴ + q⁻⁴ + q² + q⁻²)/2`, giving
   `O₁(q) / E₁(q) = (q³ − q⁻³) / (q³ + q⁻³) = tanh(3 ln q)`. -/

/-- Exact ring isomorphism substitution between the Riley/SnapPy cubic
`x³ − 2x² + 3x − 1` and the Landen/canonical cubic `z³ − z² + 1`:
setting `x = 1 − z²` gives `x³ − 2x² + 3x − 1 = −(z³ + z² − 1)(z³ − z² + 1)`. -/
theorem fiveTwo_cubic_x_of_z_factorization {R : Type*} [CommRing R] (z : R) :
    (1 - z ^ 2) ^ 3 - 2 * (1 - z ^ 2) ^ 2 + 3 * (1 - z ^ 2) - 1
      = -(z ^ 3 + z ^ 2 - 1) * (z ^ 3 - z ^ 2 + 1) := by
  ring

/-- Exact Bézout identity in `ℤ[x]` inverting `P'(x) = 3x² − 4x + 3` modulo
`x³ − 2x² + 3x − 1`: `(3x² − 4x + 3)(10x² − 17x + 18) = 23 + (30x − 31)(x³ − 2x² + 3x − 1)`. -/
theorem fiveTwo_deriv_bezout_identity {R : Type*} [CommRing R] (x : R) :
    (3 * x ^ 2 - 4 * x + 3) * (10 * x ^ 2 - 17 * x + 18)
      = 23 + (30 * x - 31) * (x ^ 3 - 2 * x ^ 2 + 3 * x - 1) := by
  ring

/-- Exact polynomial identity equating `(-3x² + 4x - 8) · P'(x)²` to `−23` modulo
`x³ − 2x² + 3x − 1`. -/
theorem fiveTwo_resolvent_sq_poly_identity {R : Type*} [CommRing R] (x : R) :
    (-3 * x ^ 2 + 4 * x - 8) * (3 * x ^ 2 - 4 * x + 3) ^ 2 + 23
      = (-27 * x ^ 3 + 54 * x ^ 2 - 81 * x + 49) * (x ^ 3 - 2 * x ^ 2 + 3 * x - 1) := by
  ring

/-- Along the Vieta locus `ξ₀ + ξ₁ + ξ₂ = 2` and `ξ₀ξ₁ + ξ₀ξ₂ + ξ₁ξ₂ = 3`, the square of
the conjugate-saddle difference `(ξ₁ − ξ₂)²` is the quadratic polynomial `−3ξ₀² + 4ξ₀ − 8`
in the real root `ξ₀`. -/
theorem fiveTwo_saddle_diff_sq {R : Type*} [CommRing R] {ξ₀ ξ₁ ξ₂ : R}
    (e1 : ξ₀ + ξ₁ + ξ₂ = 2) (e2 : ξ₀ * ξ₁ + ξ₀ * ξ₂ + ξ₁ * ξ₂ = 3) :
    (ξ₁ - ξ₂) ^ 2 = -3 * ξ₀ ^ 2 + 4 * ξ₀ - 8 := by
  linear_combination (ξ₁ + ξ₂ + 3 * ξ₀ + 2) * e1 - 4 * e2

/-- Combining `fiveTwo_saddle_diff_sq` and `fiveTwo_resolvent_sq_poly_identity`: for any root
`ξ₀` of `x³ − 2x² + 3x − 1 = 0`, the element `(ξ₁ − ξ₂)(3ξ₀² − 4ξ₀ + 3)` is a square root
of `−23`, placing `ξ₁ − ξ₂` in `K_{5₂} · ℚ(√−23)`. -/
theorem fiveTwo_saddle_diff_mul_deriv_sq_eq_neg_23 {R : Type*} [CommRing R] {ξ₀ ξ₁ ξ₂ : R}
    (e1 : ξ₀ + ξ₁ + ξ₂ = 2) (e2 : ξ₀ * ξ₁ + ξ₀ * ξ₂ + ξ₁ * ξ₂ = 3)
    (hroot : ξ₀ ^ 3 - 2 * ξ₀ ^ 2 + 3 * ξ₀ - 1 = 0) :
    ((ξ₁ - ξ₂) * (3 * ξ₀ ^ 2 - 4 * ξ₀ + 3)) ^ 2 = -23 := by
  have hdiff := fiveTwo_saddle_diff_sq e1 e2
  have hpoly := fiveTwo_resolvent_sq_poly_identity ξ₀
  rw [hroot, mul_zero] at hpoly
  calc
    ((ξ₁ - ξ₂) * (3 * ξ₀ ^ 2 - 4 * ξ₀ + 3)) ^ 2
        = (ξ₁ - ξ₂) ^ 2 * (3 * ξ₀ ^ 2 - 4 * ξ₀ + 3) ^ 2 := by ring
    _ = (-3 * ξ₀ ^ 2 + 4 * ξ₀ - 8) * (3 * ξ₀ ^ 2 - 4 * ξ₀ + 3) ^ 2 := by rw [hdiff]
    _ = -23 := by linear_combination hpoly

/-- Closed-form bar-odd (`σ₁ − σ₂`) projection in the `{1, ξ₀, ξ₀²}` basis of `K_{5₂}`:
for any `α = a + bξ + cξ²`, multiplying `(σ₁(α) − σ₂(α))` by `10ξ₀² − 17ξ₀ + 18`
(= `23 / P'(ξ₀)`) yields `((18b + 26c) − (17b + 22c)ξ₀ + (10b + 17c)ξ₀²) · (ξ₁ − ξ₂)`. -/
theorem fiveTwo_barOdd_resolvent_basis {R : Type*} [CommRing R] {ξ₀ ξ₁ ξ₂ : R}
    (e1 : ξ₀ + ξ₁ + ξ₂ = 2) (hroot : ξ₀ ^ 3 - 2 * ξ₀ ^ 2 + 3 * ξ₀ - 1 = 0)
    (a b c : R) :
    ((a + b * ξ₁ + c * ξ₁ ^ 2) - (a + b * ξ₂ + c * ξ₂ ^ 2)) * (10 * ξ₀ ^ 2 - 17 * ξ₀ + 18)
      = ((18 * b + 26 * c) - (17 * b + 22 * c) * ξ₀ + (10 * b + 17 * c) * ξ₀ ^ 2)
          * (ξ₁ - ξ₂) := by
  linear_combination
    c * (ξ₁ - ξ₂) * (10 * ξ₀ ^ 2 - 17 * ξ₀ + 18) * e1
      + (-10 * c * (ξ₁ - ξ₂)) * hroot

/-- Closed-form 1-loop (`k = 1`) GSWZ bar-odd coefficients in `K_{5₂} · ℚ(√−23)`:
for `b₁ = 209/2116` and `c₁ = −121/1058`, a factor of `23` cancels in all three basis
coefficients, leaving `(11 / (4 · 23²)) · (−10 + 7ξ₀ − 8ξ₀²)`. -/
theorem fiveTwo_oneLoop_barOdd_factorization (ξ₀ : ℚ) :
    let b₁ : ℚ := 209 / 2116
    let c₁ : ℚ := -121 / 1058
    (18 * b₁ + 26 * c₁) / 23 = -55 / 1058 ∧
    -(17 * b₁ + 22 * c₁) / 23 = 77 / 2116 ∧
    (10 * b₁ + 17 * c₁) / 23 = -22 / 529 ∧
    (-55 / 1058 + (77 / 2116) * ξ₀ - (22 / 529) * ξ₀ ^ 2 : ℚ)
      = (11 / (4 * 23 ^ 2 : ℚ)) * (-10 + 7 * ξ₀ - 8 * ξ₀ ^ 2) := by
  refine ⟨by norm_num, by norm_num, by norm_num, ?_⟩
  ring

/-- Exact closed-form identity for the `n = 1` Masbaum cyclotomic-coefficient bar-asymmetry
ratio `ρ₁(q) = O₁(q) / E₁(q)` of `5₂`: because
`q⁴ + q² − q⁻² − q⁻⁴ = (q + q⁻¹)(q³ − q⁻³)` and
`q⁴ + q² + q⁻² + q⁻⁴ = (q + q⁻¹)(q³ + q⁻³)`,
the factor `q + q⁻¹` cancels identically, giving `ρ₁(q) = (q³ − q⁻³) / (q³ + q⁻³)`. -/
theorem masbaum_c52_one_barOdd_ratio {F : Type*} [Field F] (q : F)
    (hq : q ≠ 0) (hden : -((q ^ 4 + (q⁻¹) ^ 4) + (q ^ 2 + (q⁻¹) ^ 2)) ≠ 0)
    (h3 : q ^ 3 + (q⁻¹) ^ 3 ≠ 0) :
    (-((q ^ 4 - (q⁻¹) ^ 4) + (q ^ 2 - (q⁻¹) ^ 2))) /
      (-((q ^ 4 + (q⁻¹) ^ 4) + (q ^ 2 + (q⁻¹) ^ 2)))
      = (q ^ 3 - (q⁻¹) ^ 3) / (q ^ 3 + (q⁻¹) ^ 3) := by
  rw [div_eq_div_iff hden h3]
  field_simp
  ring

/-- Discriminant squareclass disjointness between the `5₂` quadratic resolvent `ℚ(√−23)` and
the retired Alexander-layer field `ℚ(√−7)`: `(-23) · (-7) = 161` lies strictly between
`12² = 144` and `13² = 169`, so no integer square equals `161`. -/
theorem disc_neg23_neg7_not_int_sq (n : ℤ) : n ^ 2 ≠ (-23 : ℤ) * (-7 : ℤ) := by
  intro h
  have h1 : (-23 : ℤ) * (-7 : ℤ) = 161 := by norm_num
  rw [h1] at h
  have hle : n ≤ 12 ∨ 13 ≤ n := by omega
  rcases hle with hle | hge
  · have hlt : n ≤ -13 ∨ -12 ≤ n := by omega
    rcases hlt with hlt | hmid
    · nlinarith
    · nlinarith
  · nlinarith

end QOU.QBeta.FiveTwo
