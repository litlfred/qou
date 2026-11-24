import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Crossing weights from the convention-D Markov trace (prereg Addendum 13)

In `H₂(q)` with `σ² = hσ + 1`, `h = q − q⁻¹`, the Markov trace `τ` has `τ(1) = 1` and
`τ(σ) = z`. Because `σ⁻¹ = σ − h`, `τ(σ⁻¹) = z − h`. We take convention D, `z = q³/(q² + 1)`.

* `trSigma_eq`, `trSigmaInv_eq`: `τ(σ) = q²/[2]`, `τ(σ⁻¹) = q⁻²/[2]`.
* `pairSkein_eq_trace`: the convention-D pair-Skein weights of issue #8923 are exactly these two
  trace values.
* `crossing_sum_eq`: `τ(σ) + τ(σ⁻¹) = (q² + q⁻²)/[2]`.
* `channel_y2_eq`, `channel_y11_eq`, `channel_sum`: the trace weights of the two channels are
  `[3]/[2]²` and `1/[2]²`, and they sum to `τ(1) = 1`.
* `crossing_sum_ne_one_D`, `crossing_sum_ne_one_q`: for real `q > 0`, `q ≠ 1`, the crossing-element
  weights do not sum to `1` at `z = z_D`, nor at `z = q`.

No measured value appears here.
-/

namespace QOU.QBeta.CrossingTraceWeights

section Generic

variable {R : Type*} [Field R]

/-- Convention-D Markov parameter `z_D = q³/(q² + 1)`. -/
def zD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- `τ(σ)` for a Markov parameter `z`. -/
def trSigma (z : R) : R := z

/-- `τ(σ⁻¹) = τ(σ − h) = z − (q − q⁻¹)`. -/
def trSigmaInv (q z : R) : R := z - (q - q⁻¹)

/-- Weight of the symmetric channel: from `τ(1) = y₂ + y₁₁` and `τ(σ) = q y₂ − q⁻¹ y₁₁`. -/
def y2 (q z : R) : R := (z + q⁻¹) / (q + q⁻¹)

/-- Weight of the antisymmetric channel, `1 − y₂`. -/
def y11 (q z : R) : R := 1 - y2 q z

theorem channel_sum (q z : R) : y2 q z + y11 q z = 1 := by
  unfold y11; ring

/-- The channel weights reproduce `τ(σ)` from the eigenvalues `q`, `−q⁻¹`. -/
theorem channel_trSigma (q z : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    q * y2 q z - q⁻¹ * y11 q z = trSigma z := by
  have hs : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  unfold y11 y2 trSigma
  rw [hs]
  field_simp
  ring

theorem trSigma_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trSigma (zD q) = q ^ 2 / (q + q⁻¹) := by
  have hs : q + q⁻¹ ≠ 0 := by
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this]; exact div_ne_zero hq2 hq
  unfold trSigma zD
  field_simp

theorem trSigmaInv_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trSigmaInv q (zD q) = q⁻¹ ^ 2 / (q + q⁻¹) := by
  have hs : q + q⁻¹ ≠ 0 := by
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this]; exact div_ne_zero hq2 hq
  unfold trSigmaInv zD
  field_simp
  ring

/-- The #8923 pair-Skein crossing mass is `τ(σ) μ_a + τ(σ⁻¹) μ_b`. -/
theorem pairSkein_eq_trace (q μa μb : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    (q ^ 2 * μa + q⁻¹ ^ 2 * μb) / (q + q⁻¹)
      = trSigma (zD q) * μa + trSigmaInv q (zD q) * μb := by
  rw [trSigma_eq q hq hq2, trSigmaInv_eq q hq hq2]
  ring

theorem crossing_sum_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trSigma (zD q) + trSigmaInv q (zD q) = (q ^ 2 + q⁻¹ ^ 2) / (q + q⁻¹) := by
  rw [trSigma_eq q hq hq2, trSigmaInv_eq q hq hq2]
  ring

theorem channel_y2_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    y2 q (zD q) = (q ^ 2 + 1 + q⁻¹ ^ 2) / (q + q⁻¹) ^ 2 := by
  have hs : q + q⁻¹ ≠ 0 := by
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this]; exact div_ne_zero hq2 hq
  unfold y2 zD
  field_simp
  ring

theorem channel_y11_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    y11 q (zD q) = 1 / (q + q⁻¹) ^ 2 := by
  have hs : q + q⁻¹ ≠ 0 := by
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this]; exact div_ne_zero hq2 hq
  unfold y11
  rw [channel_y2_eq q hq hq2]
  field_simp
  ring

/-- At the other admissible root `z = q`, the crossing weights sum to `[2] = q + q⁻¹`. -/
theorem crossing_sum_at_q (q : R) :
    trSigma q + trSigmaInv q q = q + q⁻¹ := by
  unfold trSigma trSigmaInv; ring

end Generic

section Real

/-- For real `q > 0`, `q ≠ 1`, `[2]_q > 2`. -/
theorem two_lt_qint (q : ℝ) (hq : 0 < q) (h1 : q ≠ 1) : 2 < q + q⁻¹ := by
  have : q + q⁻¹ - 2 = (q - 1) ^ 2 / q := by field_simp; ring
  have hp : 0 < (q - 1) ^ 2 := by
    have : q - 1 ≠ 0 := sub_ne_zero.mpr h1
    positivity
  have : 0 < q + q⁻¹ - 2 := by rw [this]; positivity
  linarith

/-- Convention D: the crossing-element trace weights do not sum to `1` for `q > 0`, `q ≠ 1`. -/
theorem crossing_sum_ne_one_D (q : ℝ) (hq : 0 < q) (h1 : q ≠ 1) :
    trSigma (zD q) + trSigmaInv q (zD q) ≠ 1 := by
  rw [crossing_sum_eq q hq.ne' (by positivity)]
  have hs : 0 < q + q⁻¹ := by positivity
  have h2 := two_lt_qint q hq h1
  intro h
  rw [div_eq_one_iff_eq hs.ne'] at h
  have key : q ^ 2 + q⁻¹ ^ 2 - (q + q⁻¹) = ((q + q⁻¹) - 2) * ((q + q⁻¹) + 1) := by
    field_simp; ring
  rw [h, sub_self] at key
  have : 0 < ((q + q⁻¹) - 2) * ((q + q⁻¹) + 1) := by
    apply mul_pos <;> linarith
  linarith

/-- The other admissible root `z = q`: the sum is `[2]_q > 2`, so not `1`. -/
theorem crossing_sum_ne_one_q (q : ℝ) (hq : 0 < q) (h1 : q ≠ 1) :
    trSigma q + trSigmaInv q q ≠ 1 := by
  rw [crossing_sum_at_q]
  have := two_lt_qint q hq h1
  linarith

end Real

end QOU.QBeta.CrossingTraceWeights
