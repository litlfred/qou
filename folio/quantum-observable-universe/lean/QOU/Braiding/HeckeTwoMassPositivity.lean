import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Field.Power
import Mathlib.Algebra.Group.Int.Even
import Mathlib.LinearAlgebra.Prod
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# The mass of `σᵏ` on two strands, and when it is positive

`H₂(q)` is spanned by `1, σ` with `(σ - q)(σ + q⁻¹) = 0`. For `q² + 1 ≠ 0` the two eigenvalues are
distinct, so `σ ↦ (q, -q⁻¹)` identifies `H₂(q)` with `K × K`, and `σᵏ ↦ (qᵏ, (-q⁻¹)ᵏ)` for every
`k ∈ ℤ`.

* `markov_two_eq` — a linear functional on `K × K` with `t(1) = 1` and `t(σ) = z_D = q³/(q² + 1)`
  (the two Markov conditions at `n = 2`, convention D) is forced to be
  `t(a, b) = ([3]·a + b)/[2]²`, with `[3] = q² + 1 + q⁻²`, `[2] = q + q⁻¹`. No uniqueness theorem
  is assumed: on two strands the two conditions determine the functional.
* `mass_sigma_zpow` — so the framed mass `𝔪(σᵏ) = [2]² · q^{-2k} · tr(σᵏ)` (`def:mass-identity`,
  writhe `k`) is `q^{-2k} · ([3]·qᵏ + (-q⁻¹)ᵏ)`.
* `mass_pos_iff` — **the `n = 2` positivity rule.** For `q > 0`, `𝔪(σᵏ) > 0` iff `k` is even or
  `[3]·q^{2k} > 1`. So every even power and every positive power at `q ≥ 1` is positive, and an odd
  negative power `σ^{-m}` is positive iff `[3] > q^{2m}`.

Bean `qou-078y` (positivity of `𝔪`, direction 2). The `n ≥ 3` characterisation is open.

Base ring (§7c): the identification is over a generic `[Field K]`; the positivity rule needs an
ordered field (`[LinearOrder K] [IsStrictOrderedRing K]`), and nothing archimedean.
-/

namespace QOU.Braiding.HeckeTwoMass

variable {K : Type*} [Field K]

/-- `[3]_q = q² + 1 + q⁻²`. -/
def q3 (q : K) : K := q ^ 2 + 1 + q⁻¹ ^ 2

/-- **The Markov trace on two strands is forced.** -/
theorem markov_two_eq (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (t : K × K →ₗ[K] K)
    (h1 : t (1, 1) = 1) (hσ : t (q, -q⁻¹) = q ^ 3 / (q ^ 2 + 1)) (a b : K) :
    t (a, b) = (q3 q * a + b) / (q + q⁻¹) ^ 2 := by
  have hs : q + q⁻¹ ≠ 0 := by
    rw [show q + q⁻¹ = (q ^ 2 + 1) / q by field_simp]; exact div_ne_zero hq2 hq
  set β := (a - b) / (q + q⁻¹) with hβ
  set α := a - β * q with hα
  have hdec : ((a, b) : K × K) = α • ((1 : K), (1 : K)) + β • (q, -q⁻¹) := by
    ext
    · simp [hα]
    · simp only [Prod.snd_add, Prod.smul_mk, smul_eq_mul, mul_one, hα, hβ, mul_neg]
      field_simp; ring
  rw [hdec, map_add, map_smul, map_smul, h1, hσ, smul_eq_mul, smul_eq_mul, hα, hβ, q3]
  field_simp; ring

/-- **The framed mass of `σᵏ` on two strands.** -/
theorem mass_sigma_zpow (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (t : K × K →ₗ[K] K)
    (h1 : t (1, 1) = 1) (hσ : t (q, -q⁻¹) = q ^ 3 / (q ^ 2 + 1)) (k : ℤ) :
    (q + q⁻¹) ^ 2 * q ^ (-2 * k) * t (q ^ k, (-q⁻¹) ^ k)
      = q ^ (-2 * k) * (q3 q * q ^ k + (-q⁻¹) ^ k) := by
  have hs : q + q⁻¹ ≠ 0 := by
    rw [show q + q⁻¹ = (q ^ 2 + 1) / q by field_simp]; exact div_ne_zero hq2 hq
  rw [markov_two_eq q hq hq2 t h1 hσ]
  field_simp

variable [LinearOrder K] [IsStrictOrderedRing K]

theorem q3_pos (q : K) : 0 < q3 q := by
  unfold q3; positivity

/-- **The `n = 2` positivity rule.** -/
theorem mass_pos_iff (q : K) (hq : 0 < q) (k : ℤ) :
    0 < q ^ (-2 * k) * (q3 q * q ^ k + (-q⁻¹) ^ k) ↔ Even k ∨ 1 < q3 q * q ^ (2 * k) := by
  have hq0 : q ≠ 0 := hq.ne'
  have hk : 0 < q ^ k := zpow_pos hq k
  have hpre : 0 < q ^ (-2 * k) := zpow_pos hq _
  have hsplit : (-q⁻¹) ^ k = (-1) ^ k * (q ^ k)⁻¹ := by
    rw [neg_eq_neg_one_mul, mul_zpow, inv_zpow]
  have h2k : q ^ (2 * k) = q ^ k * q ^ k := by
    rw [two_mul, zpow_add₀ hq0]
  have key : (q3 q * q ^ k + (-q⁻¹) ^ k) * q ^ k = q3 q * q ^ (2 * k) + (-1) ^ k := by
    rw [hsplit, h2k]; field_simp
  rw [mul_pos_iff_of_pos_left hpre, ← mul_pos_iff_of_pos_right hk, key]
  rcases Int.even_or_odd k with he | ho
  · rw [he.neg_one_zpow]
    have : 0 < q3 q * q ^ (2 * k) := mul_pos (q3_pos q) (zpow_pos hq _)
    exact ⟨fun _ => Or.inl he, fun _ => by linarith⟩
  · rw [ho.neg_one_zpow]
    have hne : ¬ Even k := Int.not_even_iff_odd.mpr ho
    constructor
    · intro h; exact Or.inr (by linarith)
    · rintro (h | h)
      · exact absurd h hne
      · linarith

end QOU.Braiding.HeckeTwoMass
