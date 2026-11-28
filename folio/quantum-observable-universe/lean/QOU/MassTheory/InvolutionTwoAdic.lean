import Mathlib.Tactic

/-!
# 2-adic valuation of the involution numbers

`invNum n` is the number of involutions of `Fin n`, given by its recurrence
`I (n+2) = I (n+1) + (n+1) I n`, `I 0 = I 1 = 1`.  We prove
`I (4k) = 2^k α`, `I (4k+1) = 2^k β` with `α, β` odd and `α ≡ β [ZMOD 8]`,
and deduce `I (4k+2) = 2^(k+1)·odd`, `I (4k+3) = 2^(k+2)·odd`.  This is the
formula `v₂(I m) = ⌊m/4⌋ + (0,0,1,2)[m mod 4]` used in
`conj:cyclotomic-boundary-at-keystone` (cumulant test, 2-adic step).
-/

namespace QOU.Mass.InvolutionTwoAdic

/-- Involution numbers, by the standard recurrence. -/
def invNum : ℕ → ℤ
  | 0 => 1
  | 1 => 1
  | n + 2 => invNum (n + 1) + ((n : ℤ) + 1) * invNum n

lemma invNum_succ_succ (n : ℕ) :
    invNum (n + 2) = invNum (n + 1) + ((n : ℤ) + 1) * invNum n := rfl

/-- Four steps of the recurrence, from the pair `(I m, I (m+1))`. -/
lemma invNum_add_four (m : ℕ) :
    invNum (m + 4) = 2 * ((m : ℤ) + 3) * invNum (m + 1)
      + ((m : ℤ) + 1) * ((m : ℤ) + 4) * invNum m := by
  simp only [invNum_succ_succ, show m + 4 = (m + 2) + 2 from rfl,
    show m + 3 = (m + 1) + 2 from rfl]
  push_cast; ring

lemma invNum_add_five (m : ℕ) :
    invNum (m + 5) = ((m : ℤ) + 3) * ((m : ℤ) + 6) * invNum (m + 1)
      + 2 * ((m : ℤ) + 1) * ((m : ℤ) + 4) * invNum m := by
  simp only [invNum_succ_succ, show m + 5 = (m + 3) + 2 from rfl,
    show m + 4 = (m + 2) + 2 from rfl, show m + 3 = (m + 1) + 2 from rfl]
  push_cast; ring

/-- The invariant: `I (4k) = 2^k α`, `I (4k+1) = 2^k β`, `α` and `β` odd, `8 ∣ α - β`. -/
theorem invNum_four_mul (k : ℕ) :
    ∃ α β : ℤ, invNum (4 * k) = 2 ^ k * α ∧ invNum (4 * k + 1) = 2 ^ k * β ∧
      Odd α ∧ Odd β ∧ (8 : ℤ) ∣ α - β := by
  induction k with
  | zero => exact ⟨1, 1, rfl, rfl, odd_one, odd_one, by norm_num⟩
  | succ k ih =>
    obtain ⟨α, β, hα, hβ, ⟨b, rfl⟩, -, ⟨t, ht⟩⟩ := ih
    obtain rfl : β = 2 * b + 1 - 8 * t := by linarith
    set K : ℤ := (k : ℤ) with hK
    refine ⟨(4 * K + 3) * (2 * b + 1 - 8 * t) + 2 * (K + 1) * (4 * K + 1) * (2 * b + 1),
      (4 * K + 3) * (2 * K + 3) * (2 * b + 1 - 8 * t) + 4 * (K + 1) * (4 * K + 1) * (2 * b + 1),
      ?_, ?_, ?_, ?_, ?_⟩
    · rw [show 4 * (k + 1) = 4 * k + 4 by ring, invNum_add_four, hα, hβ]
      push_cast; ring
    · rw [show 4 * (k + 1) + 1 = 4 * k + 5 by ring, invNum_add_five, hα, hβ]
      push_cast; ring
    · exact ⟨8*b*K^2 + 14*b*K + 5*b + 4*K^2 - 16*K*t + 7*K - 12*t + 2, by ring⟩
    · exact ⟨24*b*K^2 + 38*b*K + 13*b - 32*K^2*t + 12*K^2 - 72*K*t + 19*K - 36*t + 6, by ring⟩
    · exact ⟨-4*b*K^2 - 6*b*K - 2*b + 8*K^2*t - 2*K^2 + 14*K*t - 3*K + 6*t - 1, by ring⟩

/-- `I (4k+2) = 2^(k+1) · odd`. -/
theorem invNum_four_mul_add_two (k : ℕ) :
    ∃ γ : ℤ, invNum (4 * k + 2) = 2 ^ (k + 1) * γ ∧ Odd γ := by
  obtain ⟨α, β, hα, hβ, ⟨b, rfl⟩, -, ⟨t, ht⟩⟩ := invNum_four_mul k
  obtain rfl : β = 2 * b + 1 - 8 * t := by linarith
  refine ⟨2 * b + 1 - 4 * t + 2 * (k : ℤ) * (2 * b + 1), ?_, ?_⟩
  · rw [invNum_succ_succ, hα, hβ]; push_cast; ring
  · exact ⟨b - 2 * t + (k : ℤ) * (2 * b + 1), by ring⟩

/-- `I (4k+3) = 2^(k+2) · odd`. -/
theorem invNum_four_mul_add_three (k : ℕ) :
    ∃ δ : ℤ, invNum (4 * k + 3) = 2 ^ (k + 2) * δ ∧ Odd δ := by
  obtain ⟨α, β, hα, hβ, ⟨b, rfl⟩, -, ⟨t, ht⟩⟩ := invNum_four_mul k
  obtain rfl : β = 2 * b + 1 - 8 * t := by linarith
  refine ⟨4*b*(k:ℤ) + 2*b - 8*(k:ℤ)*t + 2*(k:ℤ) - 6*t + 1, ?_, ?_⟩
  · rw [invNum_succ_succ, invNum_succ_succ, hα, hβ]; push_cast; ring
  · exact ⟨2*b*(k:ℤ) + b - 4*(k:ℤ)*t + (k:ℤ) - 3*t, by ring⟩

end QOU.Mass.InvolutionTwoAdic
