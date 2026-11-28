import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# The muon/electron ratio from a jet-level weight: an upper bound, so CAL-2 is not derived

Thread "Derive the muon mass relation" (2026-11-28). The owner ruled that `q₀` goes back to the
proton pin unless `m_μ/m_e = Vol(4₁)/ℏ_q²` (CAL-2) is proved. This file tests the derivation
route the corpus has: the ring masses of `def:mass-identity` times a jet-level weight.

Inputs, all in an ordered field `F` (no `ℝ`, no measured value):
* ring masses (N = 2 reading, #9879/#9881): `m_e = (q²+1)(q⁴+1)/q⁶` (Hopf),
  `m_μ = (q²+1)(q⁸+q⁴−q²+1)/q¹²` (T(2,4));
* level weight (#9945, #9952): an order-`r` scale-free operator at level `n` on mode `k`
  carries `(ℏ_q [k]_u)^(r n)`, `ℏ_q = 1 − q⁻¹`, `u = q⁻¹`, `[k]_u = Σ_{i<k} uⁱ`. The mass is
  taken to carry the inverse (`k ≤ 0` exponent, #9945). Laplacian: `r = 2`.

So the level-`n` candidate is `ρ_{n,k}(q) = R(q) / (ℏ_q [k]_u)^(2n)` with
`R = m_μ/m_e = (q⁸+q⁴−q²+1)/(q⁶(q⁴+1))`.

Results.
* `ringRatio_eq`: `m_μ/m_e = R`.
* `ringRatio_one`: `R(1) = 1`; `qInt_one`: `[k]_1 = k`. So `ℏ_q^(2n) ρ_{n,k}` takes the value
  `1/k^(2n)` at the classical point: the leading pole coefficient is **rational**.
* `ringRatio_le_one`: `R(q) ≤ 1` for `q ≥ 1`, from
  `q⁶(q⁴+1) − (q⁸+q⁴−q²+1) = (q²−1)(q⁸+q⁴+1)`.
* `one_le_qInt`: `[k]_u ≥ 1` for `u ≥ 0`, `k ≥ 1`.
* `level_ratio_le`: **for every `q > 1`, level `n ≥ 0`, mode `k ≥ 1`,
  `ℏ_q^(2n) · ρ_{n,k}(q) ≤ 1`.**
* `level_one_ne_cal2`: hence at level 1, for any `V > 1`, `ρ_{1,k}(q) ≠ V/ℏ_q²` at every `q > 1`
  and every mode `k`. With `V = Vol(4₁) ≈ 2.03 > 1`, CAL-2 is **not** produced by the level-one
  Laplacian weight on the ring masses. It stays a calibration (owner ruling, #9952).

Not derived: the level `n` and mode `k` of the muon, and any extra factor. Higher levels
(`n ≥ 2`) are not excluded by this file; see the audit note for the unscored comparison.
-/

namespace QOU.MassTheory.MuonLevelRatio

open Finset

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- `ℏ_q = 1 − q⁻¹`. -/
def hbar (q : F) : F := 1 - q⁻¹

/-- The q-integer `[k]_u = Σ_{i<k} uⁱ` (same as `LevelWeightOrder.qInt`). -/
def qInt (u : F) (k : ℕ) : F := ∑ i ∈ range k, u ^ i

/-- Ring mass of the electron word (Hopf, N = 2 reading). -/
def massE (q : F) : F := (q ^ 2 + 1) * (q ^ 4 + 1) / q ^ 6

/-- Ring mass of the muon word `σ₀⁴σ₁⁻¹` (T(2,4), N = 2 reading). -/
def massMu (q : F) : F := (q ^ 2 + 1) * (q ^ 8 + q ^ 4 - q ^ 2 + 1) / q ^ 12

/-- The ring ratio `R = (q⁸+q⁴−q²+1)/(q⁶(q⁴+1))`. -/
def ringRatio (q : F) : F := (q ^ 8 + q ^ 4 - q ^ 2 + 1) / (q ^ 6 * (q ^ 4 + 1))

/-- The level-`n`, mode-`k` candidate `ρ_{n,k} = R / (ℏ_q [k]_u)^(2n)`. -/
def levelRatio (n k : ℕ) (q : F) : F := ringRatio q / (hbar q * qInt q⁻¹ k) ^ (2 * n)

theorem ringRatio_eq {q : F} (hq : 0 < q) : massMu q / massE q = ringRatio q := by
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  have h4 : q ^ 4 + 1 ≠ 0 := by positivity
  have hq0 : q ≠ 0 := hq.ne'
  unfold massMu massE ringRatio
  field_simp

theorem ringRatio_one : ringRatio (1 : F) = 1 := by
  unfold ringRatio; norm_num

omit [LinearOrder F] [IsStrictOrderedRing F] in
theorem qInt_one (k : ℕ) : qInt (1 : F) k = k := by
  simp [qInt]

/-- `R(q) ≤ 1` for `q ≥ 1`. -/
theorem ringRatio_le_one {q : F} (hq : 1 ≤ q) : ringRatio q ≤ 1 := by
  have hq0 : 0 < q := lt_of_lt_of_le one_pos hq
  have hden : 0 < q ^ 6 * (q ^ 4 + 1) := by positivity
  unfold ringRatio
  rw [div_le_one hden]
  have hq2 : 0 ≤ q ^ 2 - 1 := by nlinarith
  have hkey : q ^ 6 * (q ^ 4 + 1) - (q ^ 8 + q ^ 4 - q ^ 2 + 1)
      = (q ^ 2 - 1) * (q ^ 8 + q ^ 4 + 1) := by ring
  have : 0 ≤ (q ^ 2 - 1) * (q ^ 8 + q ^ 4 + 1) := mul_nonneg hq2 (by positivity)
  linarith

theorem ringRatio_pos {q : F} (hq : 1 ≤ q) : 0 < ringRatio q := by
  have hq0 : 0 < q := lt_of_lt_of_le one_pos hq
  unfold ringRatio
  apply div_pos _ (by positivity)
  nlinarith [pow_pos hq0 2, pow_pos hq0 4, pow_pos hq0 8, one_le_pow₀ (n := 2) hq,
    one_le_pow₀ (n := 4) hq]

/-- `[k]_u ≥ 1` for `u ≥ 0`, `k ≥ 1`. -/
theorem one_le_qInt {u : F} (hu : 0 ≤ u) {k : ℕ} (hk : 1 ≤ k) : 1 ≤ qInt u k := by
  unfold qInt
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hk
  rw [add_comm, sum_range_succ']
  simp only [pow_zero]
  have : 0 ≤ ∑ i ∈ range j, u ^ (i + 1) := sum_nonneg fun i _ => pow_nonneg hu _
  linarith

theorem hbar_pos {q : F} (hq : 1 < q) : 0 < hbar q := by
  unfold hbar
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

/-- **Upper bound.** For `q > 1` and mode `k ≥ 1`: `ℏ_q^(2n) · ρ_{n,k}(q) ≤ 1`. -/
theorem level_ratio_le (n : ℕ) {k : ℕ} (hk : 1 ≤ k) {q : F} (hq : 1 < q) :
    hbar q ^ (2 * n) * levelRatio n k q ≤ 1 := by
  have hh := hbar_pos hq
  have hu : 0 ≤ q⁻¹ := inv_nonneg.mpr (le_of_lt (lt_trans one_pos hq))
  have hK := one_le_qInt hu hk
  have hKp : 0 < qInt q⁻¹ k := lt_of_lt_of_le one_pos hK
  have hKn : 1 ≤ qInt q⁻¹ k ^ (2 * n) := one_le_pow₀ hK
  have hR := ringRatio_le_one hq.le
  have hR0 := ringRatio_pos hq.le
  unfold levelRatio
  rw [mul_pow]
  have hhn : 0 < hbar q ^ (2 * n) := pow_pos hh _
  have hkn : 0 < qInt q⁻¹ k ^ (2 * n) := pow_pos hKp _
  rw [show hbar q ^ (2 * n) * (ringRatio q / (hbar q ^ (2 * n) * qInt q⁻¹ k ^ (2 * n)))
      = ringRatio q / qInt q⁻¹ k ^ (2 * n) by field_simp]
  rw [div_le_one hkn]
  linarith

/-- **Level one cannot give CAL-2.** For any `V > 1`, any mode `k ≥ 1` and any `q > 1`,
`ρ_{1,k}(q) ≠ V / ℏ_q²`. (Apply with `V = Vol(4₁)`.) -/
theorem level_one_ne_cal2 {V : F} (hV : 1 < V) {k : ℕ} (hk : 1 ≤ k) {q : F} (hq : 1 < q) :
    levelRatio 1 k q ≠ V / hbar q ^ 2 := by
  intro h
  have hle := level_ratio_le 1 hk hq
  have hh := (hbar_pos hq).ne'
  rw [h, show 2 * 1 = 2 from rfl, mul_div_cancel₀ _ (pow_ne_zero 2 hh)] at hle
  linarith

/-- The leading coefficient at the classical point: `R(1)/[k]_1^(2n) = 1/k^(2n)`, a rational. -/
theorem leading_coeff (n k : ℕ) :
    ringRatio (1 : F) / qInt (1 : F)⁻¹ k ^ (2 * n) = 1 / (k : F) ^ (2 * n) := by
  rw [inv_one, ringRatio_one, qInt_one]

end QOU.MassTheory.MuonLevelRatio
