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
  which is why `pₙ ∈ ℤ` and the generating function is the reciprocal cubic.

**NOT proved here** (and not stubbed — no `sorry`, no axiom):

* that the integral equals `A` (needs `∫₀¹ log(1−yz)/z = −Li₂(y)`);
* the closed-form evaluation of the integral, i.e. the sum rule itself. That
  remains **verified to 80 dps, unproved**; routes 1–4 in `qou-0yqu` are dead
  and Route 5 is a restatement, not a solution.

-- Ref: [manuscript] bean qou-0yqu Route 5; docs/coordination/1ppq-qbeta.md
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log

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

end QOU.QBeta.FiveTwo
