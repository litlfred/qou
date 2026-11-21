import QOU.QuarkState.WeakVertexMidpoint

/-!
# The chirality swap has two eigenlines on `span{1, σ}`

The n–p splitting thread compares candidate shapes `a • σ + b • 1` for the u–d crossing.
An overall scalar cancels in the n–p difference, so only the shape matters.

The chirality swap `ι : s ↦ h − s` (`Helicity.swap`, with `ι(V) = V̄` on the pair,
`ChiralityPairBit.iota_vertex`) is an automorphism of the Hecke algebra. On the span of
`1` and a letter `s` it acts by `a • s + b • 1 ↦ a • (h − s) + b • 1`. This file proves:

* `iotaSpan_odd_iff`: `a • s + b • 1` is `ι`-odd iff `2 b = −a h`, i.e. iff it is
  `a • symCrossing q s`, a multiple of the averaged crossing `½(σ + σ⁻¹)`.
* `iotaSpan_even_iff`: when `1` and `s` are linearly independent, `a • s + b • 1` is
  `ι`-even iff `a = 0`, i.e. iff it is a multiple of `1`.

So the two shapes on the table (the averaged crossing and the identity) are exactly the two
definite-chirality choices, and every other shape mixes the two parities. The weak vertex is
a multiple of the odd one (`WeakVertexMidpoint.grading_eq_midpoint`).

This is a statement about shapes. It does not say which parity the nucleon's u–d crossing
must have; that requirement is not derived here.

-- Ref: [leitner2026] prop:weak-vertex-left-projector
-/

namespace QOU.QuarkState.ChiralityParity

open QOU.QuarkState.Helicity QOU.QuarkState.WeakVertexMidpoint

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]

/-- The chirality swap extended linearly to `span{1, s}`. -/
def iotaSpan (q : K) (s : A) (a b : K) : A := a • swap q s + b • (1 : A)

/-- The element `a • s + b • 1`. -/
def spanElt (s : A) (a b : K) : A := a • s + b • (1 : A)

theorem iotaSpan_add_spanElt (q : K) (s : A) (a b : K) :
    iotaSpan q s a b + spanElt s a b = (a * (q - q⁻¹) + 2 * b) • (1 : A) := by
  unfold iotaSpan spanElt swap
  rw [smul_sub, smul_smul, add_smul, two_mul, add_smul]
  abel

/-- **Odd line.** `a • s + b • 1` is `ι`-odd iff `a h + 2 b = 0`. -/
theorem iotaSpan_odd_iff [Nontrivial A] (q : K) (s : A) (a b : K) :
    iotaSpan q s a b = -spanElt s a b ↔ a * (q - q⁻¹) + 2 * b = 0 := by
  rw [← add_eq_zero_iff_eq_neg, iotaSpan_add_spanElt, smul_eq_zero]
  simp

/-- The odd line is the averaged crossing: if `a h + 2 b = 0` then
    `a • s + b • 1 = a • symCrossing q s`. -/
theorem spanElt_eq_symCrossing_of_odd (h2 : (2 : K) ≠ 0) (q : K) (s : A) {a b : K}
    (hab : a * (q - q⁻¹) + 2 * b = 0) : spanElt s a b = a • symCrossing q s := by
  have hb : b = -(a * ((q - q⁻¹) / 2)) := by
    apply mul_left_cancel₀ h2
    rw [mul_neg, mul_left_comm, mul_div_cancel₀ _ h2]
    linear_combination hab
  rw [symCrossing_eq h2, spanElt, hb, smul_sub, smul_smul, neg_smul]
  abel

/-- **Even line.** If `1` and `s` are linearly independent, `a • s + b • 1` is `ι`-even
    iff `a = 0`. -/
theorem iotaSpan_even_iff (h2 : (2 : K) ≠ 0) (q : K) (s : A)
    (hind : ∀ c d : K, c • s + d • (1 : A) = 0 → c = 0 ∧ d = 0) (a b : K) :
    iotaSpan q s a b = spanElt s a b ↔ a = 0 := by
  constructor
  · intro h
    have key : (-(2 * a)) • s + (a * (q - q⁻¹)) • (1 : A) = 0 := by
      have h' : iotaSpan q s a b - spanElt s a b = 0 := sub_eq_zero.mpr h
      unfold iotaSpan spanElt swap at h'
      rw [← h']
      rw [neg_smul, smul_sub, smul_smul, mul_smul, two_smul]
      abel
    have := (hind _ _ key).1
    have h2a : 2 * a = 0 := neg_eq_zero.mp this
    rcases mul_eq_zero.mp h2a with h | h
    · exact absurd h h2
    · exact h
  · rintro rfl
    simp [iotaSpan, spanElt]

end QOU.QuarkState.ChiralityParity
