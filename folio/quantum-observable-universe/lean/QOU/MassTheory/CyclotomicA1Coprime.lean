import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# The coprime case of `c ∣ a₁` is empty

Partition count behind `conj:cyclotomic-boundary-at-keystone`. For `n = T_j + r`, `1 ≤ r ≤ j`,
write `B = r + 1`, `C = j - r + 2`, `A = j + 1 = B + C - 2` and `c = C(j+1, r)`. Then
`a₁ / c = j - 2r + 1 + a1Num B C / (B C A)`, so `c ∣ a₁` needs `B C A ∣ a1Num B C`
(that identity is checked in the `.md`, not formalised here). This file proves that when
`A`, `B`, `C` are pairwise coprime, already `A ∣ a1Num B C` is impossible
(`not_dvd_a1Num_of_coprime`): modulo `A` the numerator is `2 C (C-1) (C-2)²`, coprimality gives
`A ∣ 2 (C - 1)`, so `A = 2 (C - 1)`, i.e. `B = C`. If only `A` is coprime to `B` and `C`, the same
step gives `B = C`, and then `B C A ∣ a1Num` reduces to `B ∣ 4` (`eq_and_dvd_four_of_coprime_A`).
-/

namespace QOU.Mass.StaircaseMinimisers

/-- Numerator of `a₁/c - (j - 2r + 1)` over `B C A`, with `B = r + 1`, `C = j - r + 2`,
`A = B + C - 2 = j + 1`. -/
def a1Num (B C : ℤ) : ℤ :=
  (C - 1) * (C - 3) * C * (B + C - 2) + (B - 1) ^ 2 * B * (B + C - 2) - 2 * (C - 1) * (C - 2) * B * C

theorem a1Num_eq (B C : ℤ) :
    a1Num B C = 2 * C * (C - 1) * (C - 2) ^ 2 +
      (B + C - 2) * ((B - C) * ((B + C - 2) ^ 2 - (B + C - 2) * C + 2 * (B + C - 2) + C ^ 2 - 2 * C + 1)) := by
  unfold a1Num; ring

/-- **The coprime case of `c ∣ a₁` is empty.** If `A = B + C - 2` divides the numerator and
`A`, `B`, `C` are pairwise coprime with `B, C ≥ 2`, contradiction. -/
theorem not_dvd_a1Num_of_coprime {B C : ℤ} (hB : 2 ≤ B) (hC : 2 ≤ C)
    (hAB : IsCoprime (B + C - 2) B) (hAC : IsCoprime (B + C - 2) C) (hBC : IsCoprime B C)
    (h : (B + C - 2) ∣ a1Num B C) : False := by
  set A := B + C - 2 with hA
  have h1 : A ∣ 2 * C * (C - 1) * (C - 2) ^ 2 := by
    have := (dvd_sub h (dvd_mul_right A ((B - C) *
      (A ^ 2 - A * C + 2 * A + C ^ 2 - 2 * C + 1))))
    rwa [a1Num_eq, add_sub_cancel_right] at this
  have hA2 : IsCoprime A (C - 2) := by
    have : C - 2 = -B + A * 1 := by rw [hA]; ring
    rw [this]
    exact hAB.neg_right.add_mul_left_right 1
  have h2 : A ∣ 2 * (C - 1) := by
    have e : 2 * C * (C - 1) * (C - 2) ^ 2 = C * ((C - 2) ^ 2 * (2 * (C - 1))) := by ring
    rw [e] at h1
    exact (hA2.pow_right).dvd_of_dvd_mul_left (hAC.dvd_of_dvd_mul_left h1)
  obtain ⟨k, hk⟩ := h2
  have hk1 : k = 1 := by
    have hApos : 0 < A := by rw [hA]; linarith
    have h0 : 0 < k := by
      by_contra hn; push_neg at hn; nlinarith
    have h2' : k < 2 := by
      by_contra hn; push_neg at hn; nlinarith
    omega
  subst hk1
  have hBC' : B = C := by rw [hA] at hk; linarith
  subst hBC'
  have := Int.isUnit_iff.1 (isCoprime_self.1 hBC)
  omega

/-- **`A` coprime to `B` and `C`.** If `A = B + C - 2` is coprime to `B` and to `C` (no condition
on `gcd(B, C)`) and `B C A` divides the numerator, then `B = C` and `B ∣ 4`. With
`B = r + 1`, `C = j - r + 2` this leaves only `(j, r) = (1, 1)` and `(5, 3)`. -/
theorem eq_and_dvd_four_of_coprime_A {B C : ℤ} (hB : 2 ≤ B) (hC : 2 ≤ C)
    (hAB : IsCoprime (B + C - 2) B) (hAC : IsCoprime (B + C - 2) C)
    (h : B * C * (B + C - 2) ∣ a1Num B C) : B = C ∧ B ∣ 4 := by
  set A := B + C - 2 with hA
  have hAN : A ∣ a1Num B C := (dvd_mul_left A (B * C)).trans h
  have h1 : A ∣ 2 * C * (C - 1) * (C - 2) ^ 2 := by
    have := (dvd_sub hAN (dvd_mul_right A ((B - C) *
      (A ^ 2 - A * C + 2 * A + C ^ 2 - 2 * C + 1))))
    rwa [a1Num_eq, add_sub_cancel_right] at this
  have hA2 : IsCoprime A (C - 2) := by
    have : C - 2 = -B + A * 1 := by rw [hA]; ring
    rw [this]
    exact hAB.neg_right.add_mul_left_right 1
  have h2 : A ∣ 2 * (C - 1) := by
    have e : 2 * C * (C - 1) * (C - 2) ^ 2 = C * ((C - 2) ^ 2 * (2 * (C - 1))) := by ring
    rw [e] at h1
    exact (hA2.pow_right).dvd_of_dvd_mul_left (hAC.dvd_of_dvd_mul_left h1)
  obtain ⟨k, hk⟩ := h2
  have hk1 : k = 1 := by
    have hApos : 0 < A := by rw [hA]; linarith
    have h0 : 0 < k := by
      by_contra hn; push_neg at hn; nlinarith
    have h2' : k < 2 := by
      by_contra hn; push_neg at hn; nlinarith
    omega
  subst hk1
  have hBC' : C = B := by rw [hA] at hk; linarith
  subst hBC'
  refine ⟨rfl, ?_⟩
  have hN' : a1Num C C = (C * A) * (C - 2) ^ 2 := by rw [hA]; unfold a1Num; ring
  rw [hN'] at h
  have hCA : C * A ≠ 0 := by
    have : 0 < A := by rw [hA]; linarith
    positivity
  have h3 : C ∣ (C - 2) ^ 2 := by
    have e : C * C * A = (C * A) * C := by ring
    rw [e] at h
    exact (mul_dvd_mul_iff_left hCA).1 h
  have e2 : (4 : ℤ) = (C - 2) ^ 2 - C * (C - 4) := by ring
  rw [e2]
  exact dvd_sub h3 (dvd_mul_right C _)

end QOU.Mass.StaircaseMinimisers
