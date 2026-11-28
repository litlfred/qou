import QOU.MassTheory.CyclotomicA1Coprime
import Mathlib.Tactic

/-!
# `c ∣ a₁`: the closed form, and the case `gcd(A, B) = 1`

Continues `CyclotomicA1Coprime.lean` (`conj:cyclotomic-boundary-at-keystone`). For
`n = T_j + r`, `1 ≤ r ≤ j`, put `B = r + 1`, `C = j - r + 2`, `A = j + 1 = B + C - 2`.

* `a1_div_c_eq`: the rational identity the `.md` checks by hand,

      −4j − 2 + 2r(j−r)/(j+1) + j(j+2)/(r+1) + (j+2)²/(j−r+2)
        = j − 2r + 1 + a1Num B C / (B C A).

  So `c ∣ a₁` (given the partition-count formula for `a₁/c`, which is not formalised) is exactly
  `B C A ∣ a1Num B C`.
* `dvd_two_mul_gcd_of_coprime`: if `gcd(A, B) = 1` and `A ∣ a1Num B C`, then
  `A ∣ 2 · gcd(A, C) · gcd(B − 1, C − 1)`.
* `eq_or_eq_two_mul_of_coprime`: so `A = g h` or `A = 2 g h`, where `g = gcd(A, C)` and
  `h = gcd(B − 1, C − 1)`. This is the reduction stated in the `.md`. The solutions
  `(j, r) = (11, 10), (14, 6), (98, 55)` are of this kind.

This narrows the problem but does not prove that `c ∣ a₁` has finitely many solutions. That
finiteness is still open. Pure integer arithmetic. No measured values.
-/

namespace QOU.Mass.StaircaseMinimisers

/-- **The closed form of `a₁ / c`.** With `B = r + 1`, `C = j - r + 2`, `A = j + 1`. -/
theorem a1_div_c_eq (j r : ℤ) (h1 : (j : ℚ) + 1 ≠ 0) (h2 : (r : ℚ) + 1 ≠ 0)
    (h3 : (j : ℚ) - r + 2 ≠ 0) :
    (-4 * j - 2 + 2 * r * (j - r) / (j + 1) + j * (j + 2) / (r + 1) + (j + 2) ^ 2 / (j - r + 2) : ℚ) =
      j - 2 * r + 1 + (a1Num (r + 1) (j - r + 2) : ℚ) / ((r + 1) * (j - r + 2) * (j + 1)) := by
  unfold a1Num
  push_cast
  field_simp
  ring

/-- `gcd(A, C − 1) = gcd(B − 1, C − 1)`, since `A = (B − 1) + (C − 1)`. -/
theorem gcd_A_Cm1 (B C : ℤ) : Int.gcd (B + C - 2) (C - 1) = Int.gcd (B - 1) (C - 1) := by
  have : B + C - 2 = (B - 1) + 1 * (C - 1) := by ring
  rw [this, Int.gcd_add_mul_right_left]

/-- If `A ∣ 2 x y` with `gcd(x, y)` arbitrary, then `A ∣ 2 · gcd(A, x) · y`. -/
theorem dvd_two_gcd_mul {A x y : ℤ} (h : A ∣ 2 * x * y) : A ∣ 2 * (Int.gcd A x : ℤ) * y := by
  rw [Int.gcd_eq_gcd_ab A x]
  have e : 2 * (A * Int.gcdA A x + x * Int.gcdB A x) * y =
      A * (2 * Int.gcdA A x * y) + Int.gcdB A x * (2 * x * y) := by ring
  rw [e]
  exact dvd_add (dvd_mul_right _ _) (dvd_mul_of_dvd_right h _)

/-- **The case `gcd(A, B) = 1`.** If `A ∣ a1Num B C` and `A` is coprime to `B`, then
`A ∣ 2 · gcd(A, C) · gcd(B − 1, C − 1)`. -/
theorem dvd_two_mul_gcd_of_coprime {B C : ℤ} (hAB : IsCoprime (B + C - 2) B)
    (h : (B + C - 2) ∣ a1Num B C) :
    (B + C - 2) ∣ 2 * (Int.gcd (B + C - 2) C : ℤ) * (Int.gcd (B - 1) (C - 1) : ℤ) := by
  set A := B + C - 2 with hA
  have h1 : A ∣ 2 * C * (C - 1) * (C - 2) ^ 2 := by
    have := (dvd_sub h (dvd_mul_right A ((B - C) *
      (A ^ 2 - A * C + 2 * A + C ^ 2 - 2 * C + 1))))
    rwa [a1Num_eq, add_sub_cancel_right] at this
  have hA2 : IsCoprime A (C - 2) := by
    have : C - 2 = -B + A * 1 := by rw [hA]; ring
    rw [this]
    exact hAB.neg_right.add_mul_left_right 1
  have h2 : A ∣ 2 * C * (C - 1) := by
    have e : 2 * C * (C - 1) * (C - 2) ^ 2 = (C - 2) ^ 2 * (2 * C * (C - 1)) := by ring
    rw [e] at h1
    exact hA2.pow_right.dvd_of_dvd_mul_left h1
  have h3 : A ∣ 2 * (Int.gcd A C : ℤ) * (C - 1) := dvd_two_gcd_mul h2
  have h4 : A ∣ 2 * (Int.gcd A (C - 1) : ℤ) * (Int.gcd A C : ℤ) := by
    have e : 2 * (Int.gcd A C : ℤ) * (C - 1) = 2 * (C - 1) * (Int.gcd A C : ℤ) := by ring
    rw [e] at h3
    exact dvd_two_gcd_mul h3
  rw [gcd_A_Cm1] at h4
  have e : 2 * (Int.gcd (B - 1) (C - 1) : ℤ) * (Int.gcd A C : ℤ) =
      2 * (Int.gcd A C : ℤ) * (Int.gcd (B - 1) (C - 1) : ℤ) := by ring
  rwa [e] at h4

/-- **So `A = g h` or `A = 2 g h`**, with `g = gcd(A, C)`, `h = gcd(B − 1, C − 1)`. -/
theorem eq_or_eq_two_mul_of_coprime {B C : ℤ} (hB : 2 ≤ B) (hC : 2 ≤ C)
    (hAB : IsCoprime (B + C - 2) B) (h : (B + C - 2) ∣ a1Num B C) :
    B + C - 2 = (Int.gcd (B + C - 2) C : ℤ) * Int.gcd (B - 1) (C - 1) ∨
      B + C - 2 = 2 * ((Int.gcd (B + C - 2) C : ℤ) * Int.gcd (B - 1) (C - 1)) := by
  have hAd := dvd_two_mul_gcd_of_coprime hAB h
  have hg : (Int.gcd (B + C - 2) C : ℤ) ∣ B + C - 2 := Int.gcd_dvd_left _ _
  have hgC : (Int.gcd (B + C - 2) C : ℤ) ∣ C := Int.gcd_dvd_right _ _
  have hk : (Int.gcd (B - 1) (C - 1) : ℤ) ∣ B + C - 2 := by
    rw [← gcd_A_Cm1]; exact Int.gcd_dvd_left _ _
  have hkC : (Int.gcd (B - 1) (C - 1) : ℤ) ∣ C - 1 := Int.gcd_dvd_right _ _
  have hg0 : (0 : ℤ) ≤ (Int.gcd (B + C - 2) C : ℤ) := Int.natCast_nonneg _
  have hk0 : (0 : ℤ) ≤ (Int.gcd (B - 1) (C - 1) : ℤ) := Int.natCast_nonneg _
  generalize (Int.gcd (B + C - 2) C : ℤ) = g at *
  generalize (Int.gcd (B - 1) (C - 1) : ℤ) = k at *
  have hCC : IsCoprime C (C - 1) := ⟨1, -1, by ring⟩
  obtain ⟨c', hc'⟩ := hgC
  obtain ⟨d', hd'⟩ := hkC
  have hgk : IsCoprime g k := by
    rw [hd'] at hCC
    rw [hc'] at hCC
    exact (hCC.of_mul_left_left).of_mul_right_left
  obtain ⟨m, hm⟩ := hgk.mul_dvd hg hk
  have hApos : 0 < B + C - 2 := by linarith
  rw [hm] at hAd hApos ⊢
  have hm2 : m ∣ 2 := by
    have hgk0 : g * k ≠ 0 := by rintro h0; rw [h0, zero_mul] at hApos; exact lt_irrefl _ hApos
    rw [show 2 * g * k = (g * k) * 2 by ring] at hAd
    exact (mul_dvd_mul_iff_left hgk0).1 hAd
  rcases Int.natAbs_dvd_natAbs.mpr hm2 |> fun h => (Nat.dvd_prime Nat.prime_two).1 h with h1 | h1
  · rcases Int.natAbs_eq m with e | e <;> rw [h1] at e <;> subst e
    · left; ring
    · nlinarith [hApos, mul_nonneg hg0 hk0]
  · rcases Int.natAbs_eq m with e | e <;> rw [h1] at e <;> subst e
    · right; ring
    · nlinarith [hApos, mul_nonneg hg0 hk0]

end QOU.Mass.StaircaseMinimisers
