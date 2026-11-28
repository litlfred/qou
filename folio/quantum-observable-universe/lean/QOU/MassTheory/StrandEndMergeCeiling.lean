import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination

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

    y_(n) = (1 − u^(n+1)) · (1 − u)⁻¹ · ((1 + u)⁻¹)^n                  (`qint_div_eq_Y`)

and the ratio of `A` single-nucleon weights to the `A`-nucleon weight is shown to lose the
per-strand factor `(1 + u)^(3A)` entirely:

    Y(3)^A = Y(3A) · (1 + u + u² + u³)^A · (1 − u) · (1 − u^(3A+1))⁻¹  (`Y_three_pow_eq`)

So under the ruled law `B = −E₀ log r`, the saturated binding of `A` nucleons is
`A·s + B_inter(A)`, where `s` is what one nucleon gains by relaxing to its own trivial block and

    B_inter(A) = E₀·( A·log(1 + u + u² + u³) + log(1 − u) − log(1 − u^(3A+1)) )

carries no per-strand term at all. The logarithms are read off outside this file (they are
transcendental; this file is pure commutative-ring algebra under §7c).

Nothing here is numerical: `K` is any commutative ring, `q : Kˣ` any unit, with the stated
invertibility (`IsUnit`) conditions. No measured value appears.
-/

namespace QOU.MassTheory.StrandEndMergeCeiling

variable {K : Type*} [CommRing K]

private lemma mul_unit_inv {x : K} (hx : IsUnit x) : x * (↑hx.unit⁻¹ : K) = 1 :=
  calc
    x * (↑hx.unit⁻¹ : K) = (hx.unit : K) * (↑hx.unit⁻¹ : K) :=
      congrArg (· * (↑hx.unit⁻¹ : K)) hx.unit_spec.symm
    _ = 1 := Units.mul_inv hx.unit

/-- The closed form of the trivial-block weight in `u = q⁻²` over a commutative ring. -/
noncomputable def Y {u : K} (h1 : IsUnit (1 - u)) (h2 : IsUnit (1 + u)) (n : ℕ) : K :=
  (1 - u ^ (n + 1)) * (↑h1.unit⁻¹ : K) * (↑h2.unit⁻¹ : K) ^ n

/-- `q^(n+1) · (q⁻¹)^(2(n+1)) = (q⁻¹)^(n+1)`. -/
lemma pow_mul_inv_sq_pow (q : Kˣ) (n : ℕ) :
    (q : K) ^ (n + 1) * ((↑q⁻¹ : K) ^ 2) ^ (n + 1) = (↑q⁻¹ : K) ^ (n + 1) := by
  rw [← mul_pow]
  congr 1
  linear_combination ((↑q⁻¹ : K)) * Units.mul_inv q

/-- The quantum integer numerator identity: `q^(n+1) − q^-(n+1) = q^(n+1)(1 − u^(n+1))`
with `u = q⁻²`. -/
lemma qint_num (q : Kˣ) (n : ℕ) :
    (q : K) ^ (n + 1) - (↑q⁻¹ : K) ^ (n + 1) =
      (q : K) ^ (n + 1) * (1 - ((↑q⁻¹ : K) ^ 2) ^ (n + 1)) := by
  rw [mul_sub, mul_one, pow_mul_inv_sq_pow q n]

/-- `y_(n) = [n+1]_q / [2]_q^n` equals `Y` at `u = q⁻²`. -/
theorem qint_div_eq_Y (q : Kˣ)
    (hd : IsUnit ((q : K) - (↑q⁻¹ : K)))
    (hs : IsUnit ((q : K) + (↑q⁻¹ : K)))
    (h1 : IsUnit (1 - (↑q⁻¹ : K) ^ 2))
    (h2 : IsUnit (1 + (↑q⁻¹ : K) ^ 2)) (n : ℕ) :
    ((q : K) ^ (n + 1) - (↑q⁻¹ : K) ^ (n + 1)) * (↑hd.unit⁻¹ : K) * (↑hs.unit⁻¹ : K) ^ n =
      Y h1 h2 n := by
  have hd_eq : (q : K) - (↑q⁻¹ : K) = (q : K) * (1 - (↑q⁻¹ : K) ^ 2) := by
    linear_combination (↑q⁻¹ : K) * Units.mul_inv q
  have hs_eq : (q : K) + (↑q⁻¹ : K) = (q : K) * (1 + (↑q⁻¹ : K) ^ 2) := by
    linear_combination -(↑q⁻¹ : K) * Units.mul_inv q
  have hnum :
      (q : K) ^ (n + 1) - (↑q⁻¹ : K) ^ (n + 1) =
        Y h1 h2 n * (((q : K) - (↑q⁻¹ : K)) * ((q : K) + (↑q⁻¹ : K)) ^ n) := by
    rw [qint_num q n, hd_eq, hs_eq, Y, mul_pow]
    have e1 : (1 - (↑q⁻¹ : K) ^ 2) * (↑h1.unit⁻¹ : K) = 1 := mul_unit_inv h1
    have e2 : (1 + (↑q⁻¹ : K) ^ 2) ^ n * (↑h2.unit⁻¹ : K) ^ n = 1 := by
      rw [← mul_pow, mul_unit_inv h2, one_pow]
    calc
      (q : K) ^ (n + 1) * (1 - ((↑q⁻¹ : K) ^ 2) ^ (n + 1))
          = (1 - ((↑q⁻¹ : K) ^ 2) ^ (n + 1)) * ((q : K) * (q : K) ^ n) *
              ((1 - (↑q⁻¹ : K) ^ 2) * (↑h1.unit⁻¹ : K)) *
              ((1 + (↑q⁻¹ : K) ^ 2) ^ n * (↑h2.unit⁻¹ : K) ^ n) := by
            rw [e1, e2, pow_succ']; ring
      _ = (1 - ((↑q⁻¹ : K) ^ 2) ^ (n + 1)) * (↑h1.unit⁻¹ : K) * (↑h2.unit⁻¹ : K) ^ n *
            ((q : K) * (1 - (↑q⁻¹ : K) ^ 2) * ((q : K) ^ n * (1 + (↑q⁻¹ : K) ^ 2) ^ n)) := by
            ring
  calc
    ((q : K) ^ (n + 1) - (↑q⁻¹ : K) ^ (n + 1)) * (↑hd.unit⁻¹ : K) * (↑hs.unit⁻¹ : K) ^ n
        = Y h1 h2 n * (((q : K) - (↑q⁻¹ : K)) * (↑hd.unit⁻¹ : K)) *
            (((q : K) + (↑q⁻¹ : K)) * (↑hs.unit⁻¹ : K)) ^ n := by
          rw [hnum, mul_pow]; ring
    _ = Y h1 h2 n := by
          rw [mul_unit_inv hd, mul_unit_inv hs, one_pow, mul_one, mul_one]

/-- `1 − u⁴ = (1 − u)(1 + u + u² + u³)`. -/
lemma one_sub_pow_four (u : K) : 1 - u ^ 4 = (1 - u) * (1 + u + u ^ 2 + u ^ 3) := by ring

/-- The `A`-nucleon weight is the per-strand factor to the `n` times a bounded remainder:
`Y(n) · (1 + u)^n · (1 − u) = 1 − u^(n+1)`. -/
theorem Y_mul_strand_factor {u : K} (h1 : IsUnit (1 - u)) (h2 : IsUnit (1 + u)) (n : ℕ) :
    Y h1 h2 n * (1 + u) ^ n * (1 - u) = 1 - u ^ (n + 1) := by
  unfold Y
  calc
    (1 - u ^ (n + 1)) * (↑h1.unit⁻¹ : K) * (↑h2.unit⁻¹ : K) ^ n * (1 + u) ^ n * (1 - u)
        = (1 - u ^ (n + 1)) * ((1 - u) * (↑h1.unit⁻¹ : K)) *
            ((1 + u) * (↑h2.unit⁻¹ : K)) ^ n := by
          rw [mul_pow]; ring
    _ = 1 - u ^ (n + 1) := by
          rw [mul_unit_inv h1, mul_unit_inv h2, one_pow, mul_one, mul_one]

/-- **The split.** `A` single-nucleon trivial-block weights against the `A`-nucleon one: the
per-strand factor `(1 + u)^(3A)` cancels, leaving
`(1 + u + u² + u³)^A · (1 − u) · (1 − u^(3A+1))⁻¹`. -/
theorem Y_three_pow_eq {u : K} (h1 : IsUnit (1 - u)) (h2 : IsUnit (1 + u)) (A : ℕ)
    (h3 : IsUnit (1 - u ^ (3 * A + 1))) :
    Y h1 h2 3 ^ A =
      Y h1 h2 (3 * A) * ((1 + u + u ^ 2 + u ^ 3) ^ A * (1 - u) * (↑h3.unit⁻¹ : K)) := by
  have hY3 : Y h1 h2 3 * (1 + u) ^ 3 = 1 + u + u ^ 2 + u ^ 3 := by
    unfold Y
    calc
      (1 - u ^ (3 + 1)) * (↑h1.unit⁻¹ : K) * (↑h2.unit⁻¹ : K) ^ 3 * (1 + u) ^ 3
          = (1 - u ^ 4) * (↑h1.unit⁻¹ : K) * ((1 + u) * (↑h2.unit⁻¹ : K)) ^ 3 := by
            rw [mul_pow]; ring
      _ = (1 + u + u ^ 2 + u ^ 3) * ((1 - u) * (↑h1.unit⁻¹ : K)) := by
            rw [mul_unit_inv h2, one_pow, mul_one, one_sub_pow_four]; ring
      _ = 1 + u + u ^ 2 + u ^ 3 := by
            rw [mul_unit_inv h1, mul_one]
  have hLHS : Y h1 h2 3 = (1 + u + u ^ 2 + u ^ 3) * (↑h2.unit⁻¹ : K) ^ 3 := by
    calc
      Y h1 h2 3 = Y h1 h2 3 * ((1 + u) * (↑h2.unit⁻¹ : K)) ^ 3 := by
        rw [mul_unit_inv h2, one_pow, mul_one]
      _ = (Y h1 h2 3 * (1 + u) ^ 3) * (↑h2.unit⁻¹ : K) ^ 3 := by
        rw [mul_pow]; ring
      _ = (1 + u + u ^ 2 + u ^ 3) * (↑h2.unit⁻¹ : K) ^ 3 := by
        rw [hY3]
  rw [hLHS, mul_pow, ← pow_mul]
  unfold Y
  calc
    (1 + u + u ^ 2 + u ^ 3) ^ A * (↑h2.unit⁻¹ : K) ^ (3 * A)
        = (1 + u + u ^ 2 + u ^ 3) ^ A * (↑h2.unit⁻¹ : K) ^ (3 * A) *
            ((1 - u) * (↑h1.unit⁻¹ : K)) *
            ((1 - u ^ (3 * A + 1)) * (↑h3.unit⁻¹ : K)) := by
          rw [mul_unit_inv h1, mul_unit_inv h3, mul_one, mul_one]
    _ = (1 - u ^ (3 * A + 1)) * (↑h1.unit⁻¹ : K) * (↑h2.unit⁻¹ : K) ^ (3 * A) *
          ((1 + u + u ^ 2 + u ^ 3) ^ A * (1 - u) * (↑h3.unit⁻¹ : K)) := by
          ring

/-- Classical point `u = 1` of the inter-nucleon factor: `1 + u + u² + u³ = 4`, two merges
(`log 4 = 2 log 2`) per nucleon. -/
theorem inter_factor_at_one : (1 + (1 : K) + 1 ^ 2 + 1 ^ 3) = 4 := by norm_num

end QOU.MassTheory.StrandEndMergeCeiling
