import Mathlib.Tactic

/-!
# QOU.MassTheory.StrandEndMergeCeiling — the saturated binding splits into a nucleon term and an
inter-nucleon term, exactly

Gap **G5** follow-up (thread "Find the missing half of strong binding", 2026-11-27, epic `qou-myts`).
Audit: `docs/audits/2026-11-27-strand-end-merge-ceiling.md`.

## Setting

Rule (3∞) of `docs/audits/2026-11-27-bond-rules-and-length-cutoff.md` (PR #9659) is the weight-free,
cutoff-free limit of the uniform average over bond words. It equals the trivial-block weight
`y_(n) = [n+1]_q / [2]_q^n` over the free trace, with `n = 3A` strands. That audit evaluated it
at `A = 2, 3`. Here the weight is put in closed form for every `n`, in the variable `u = q⁻²`:

    y_(n) = (1 − u^(n+1)) / ((1 − u)·(1 + u)^n)                      (`qint_div_eq_Y`)

and the ratio of `A` single-nucleon weights to the `A`-nucleon weight is shown to lose the
per-strand factor `(1 + u)^(3A)` entirely:

    Y(3)^A = Y(3A) · (1 + u + u² + u³)^A · (1 − u) / (1 − u^(3A+1))   (`Y_three_pow_eq`)

So under the ruled law `B = −E₀ log r`, the saturated binding of `A` nucleons is
`A·s + B_inter(A)`, where `s` is what one nucleon gains by relaxing to its own trivial block and

    B_inter(A) = E₀·( A·log(1 + u + u² + u³) + log(1 − u) − log(1 − u^(3A+1)) )

carries no per-strand term at all. The logarithms are read off outside this file (they are
transcendental; this file is the algebra over a generic field).

Nothing here is numerical: `K` is any field, `q` any element with `q ≠ 0` and the stated
non-vanishing conditions. No measured value appears.
-/

namespace QOU.MassTheory.StrandEndMergeCeiling

variable {K : Type*} [Field K]

/-- The closed form of the trivial-block weight in `u = q⁻²`. -/
def Y (u : K) (n : ℕ) : K := (1 - u ^ (n + 1)) / ((1 - u) * (1 + u) ^ n)

/-- `q^(n+1) · (q⁻¹)^(2(n+1)) = (q⁻¹)^(n+1)`. -/
lemma pow_mul_inv_sq_pow (q : K) (hq : q ≠ 0) (n : ℕ) :
    q ^ (n + 1) * (q⁻¹ ^ 2) ^ (n + 1) = q⁻¹ ^ (n + 1) := by
  rw [← mul_pow]
  congr 1
  field_simp

/-- The quantum integer numerator identity: `(q^(n+1) − q^-(n+1))·(1 − u) = q^(n+1)(1 − u)(1 − u^(n+1))`
with `u = q⁻²`. -/
lemma qint_num (q : K) (hq : q ≠ 0) (n : ℕ) :
    q ^ (n + 1) - q⁻¹ ^ (n + 1) = q ^ (n + 1) * (1 - (q⁻¹ ^ 2) ^ (n + 1)) := by
  rw [mul_sub, mul_one, pow_mul_inv_sq_pow q hq]

/-- `y_(n) = [n+1]_q / [2]_q^n` equals `Y (q⁻²) n`. -/
theorem qint_div_eq_Y (q : K) (hq : q ≠ 0) (h2 : 1 + q⁻¹ ^ 2 ≠ 0)
    (n : ℕ) :
    (q ^ (n + 1) - q⁻¹ ^ (n + 1)) / (q - q⁻¹) / (q + q⁻¹) ^ n = Y (q⁻¹ ^ 2) n := by
  have hd : q - q⁻¹ = q * (1 - q⁻¹ ^ 2) := by field_simp
  have hs : q + q⁻¹ = q * (1 + q⁻¹ ^ 2) := by field_simp
  rw [qint_num q hq n, hd, hs, Y, mul_pow, pow_succ]
  have hqn : q ^ n ≠ 0 := pow_ne_zero _ hq
  have h2n : (1 + q⁻¹ ^ 2) ^ n ≠ 0 := pow_ne_zero _ h2
  field_simp

/-- `1 − u⁴ = (1 − u)(1 + u + u² + u³)`. -/
lemma one_sub_pow_four (u : K) : 1 - u ^ 4 = (1 - u) * (1 + u + u ^ 2 + u ^ 3) := by ring

/-- **The split.** `A` single-nucleon trivial-block weights against the `A`-nucleon one: the
per-strand factor `(1 + u)^(3A)` cancels, leaving `(1 + u + u² + u³)^A (1 − u) / (1 − u^(3A+1))`. -/
theorem Y_three_pow_eq (u : K) (h1 : 1 - u ≠ 0) (h2 : 1 + u ≠ 0) (A : ℕ)
    (h3 : 1 - u ^ (3 * A + 1) ≠ 0) :
    Y u 3 ^ A = Y u (3 * A) * ((1 + u + u ^ 2 + u ^ 3) ^ A * (1 - u) / (1 - u ^ (3 * A + 1))) := by
  unfold Y
  rw [show (3 : ℕ) + 1 = 4 by rfl, one_sub_pow_four, div_pow, mul_pow, mul_pow, ← pow_mul]
  have hA : (1 - u) ^ A ≠ 0 := pow_ne_zero _ h1
  have h2A : (1 + u) ^ (3 * A) ≠ 0 := pow_ne_zero _ h2
  field_simp

/-- The `A`-nucleon weight is the per-strand factor to the `3A` times a bounded remainder:
`Y(3A) · (1 + u)^(3A) · (1 − u) = 1 − u^(3A+1)`. -/
theorem Y_mul_strand_factor (u : K) (h1 : 1 - u ≠ 0) (h2 : 1 + u ≠ 0) (n : ℕ) :
    Y u n * (1 + u) ^ n * (1 - u) = 1 - u ^ (n + 1) := by
  unfold Y
  have hn : (1 + u) ^ n ≠ 0 := pow_ne_zero _ h2
  field_simp

/-- Classical point `u = 1` of the inter-nucleon factor: `1 + u + u² + u³ = 4`, two merges
(`log 4 = 2 log 2`) per nucleon. -/
theorem inter_factor_at_one : (1 + (1 : K) + 1 ^ 2 + 1 ^ 3) = 4 := by norm_num

end QOU.MassTheory.StrandEndMergeCeiling
