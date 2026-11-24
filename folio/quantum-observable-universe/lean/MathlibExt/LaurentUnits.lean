import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Algebra.Polynomial.RingDivision
import Mathlib.Algebra.GroupWithZero.Associated

/-!
# Units of a Laurent polynomial ring

Over an integral domain `R`, every unit of `R[T;T⁻¹]` is a unit constant times
a monomial: `u = C r * T m` with `IsUnit r`. Over `ℤ` this reads `u = ±T m`.

Mathlib states only the easy direction (`LaurentPolynomial.isUnit_T`). This file
proves the classification, which is the input the bar-invariant (Kazhdan–Lusztig)
coordinate argument in `QOU.MassTheory.ProtonQ3SchurElement` needs.

Proof: clear denominators with `exists_T_pow` on `u` and `u⁻¹`; the two
polynomials multiply to `X ^ k`; `X` is prime over a domain, so each factor is
associated to a power of `X`; units of `R[X]` over a domain are constants.
-/

namespace QOU.MathlibExt.LaurentUnits

open LaurentPolynomial Polynomial

variable {R : Type*} [CommRing R] [IsDomain R]

theorem isUnit_iff_eq_C_mul_T (u : R[T;T⁻¹]) :
    IsUnit u ↔ ∃ (r : R) (m : ℤ), IsUnit r ∧ u = LaurentPolynomial.C r * T m := by
  constructor
  · rintro ⟨v, rfl⟩
    obtain ⟨n, p, hp⟩ := exists_T_pow (v : R[T;T⁻¹])
    obtain ⟨n', p', hp'⟩ := exists_T_pow ((v⁻¹ : (R[T;T⁻¹])ˣ) : R[T;T⁻¹])
    have hprod : toLaurent (p * p') = toLaurent (X ^ (n + n') : R[X]) := by
      rw [map_mul, hp, hp', toLaurent_X_pow]
      calc (v : R[T;T⁻¹]) * T n * (((v⁻¹ : (R[T;T⁻¹])ˣ) : R[T;T⁻¹]) * T n')
          = ((v : R[T;T⁻¹]) * ((v⁻¹ : (R[T;T⁻¹])ˣ) : R[T;T⁻¹])) * (T n * T n') := by ring
        _ = T ((n + n' : ℕ) : ℤ) := by rw [Units.mul_inv, one_mul, ← T_add]; push_cast; rfl
    have hpp : p * p' = X ^ (n + n') := Polynomial.toLaurent_injective hprod
    have hdvd : p ∣ X ^ (n + n') := ⟨p', hpp.symm⟩
    obtain ⟨i, -, hassoc⟩ := (dvd_prime_pow Polynomial.prime_X _).mp hdvd
    obtain ⟨w, hw⟩ := hassoc.symm
    -- hw : X ^ i * ↑w = p
    obtain ⟨r, hr, hrw⟩ := Polynomial.isUnit_iff.mp w.isUnit
    refine ⟨r, (i : ℤ) - n, hr, ?_⟩
    have key : (v : R[T;T⁻¹]) * T n = LaurentPolynomial.C r * T i := by
      rw [← hp, ← hw, map_mul, toLaurent_X_pow, ← hrw, Polynomial.toLaurent_C, mul_comm]
    calc (v : R[T;T⁻¹]) = (v : R[T;T⁻¹]) * T n * T (-(n : ℤ)) := by
          rw [mul_assoc, ← T_add, add_neg_cancel, T_zero, mul_one]
      _ = LaurentPolynomial.C r * T i * T (-(n : ℤ)) := by rw [key]
      _ = LaurentPolynomial.C r * T ((i : ℤ) - n) := by
          rw [mul_assoc, ← T_add, sub_eq_add_neg]
  · rintro ⟨r, m, hr, rfl⟩
    exact (hr.map LaurentPolynomial.C).mul (isUnit_T m)

/-- Over `ℤ`: the units of `ℤ[q, q⁻¹]` are exactly `±q^m`. -/
theorem int_isUnit_iff (u : ℤ[T;T⁻¹]) :
    IsUnit u ↔ ∃ (ε : ℤ) (m : ℤ), (ε = 1 ∨ ε = -1) ∧ u = LaurentPolynomial.C ε * T m := by
  rw [isUnit_iff_eq_C_mul_T]
  simp only [Int.isUnit_iff]

/-- A unit of `R[T;T⁻¹]` that is fixed by the bar involution `T m ↦ T (-m)` is a
constant: its exponent is `0`. This is the integral, bar-invariant
(Kazhdan–Lusztig) coordinate criterion, now with the unit classification proved
rather than assumed. -/
theorem unit_bar_invariant_exponent_zero {r : R} (hr : IsUnit r) (m : ℤ)
    (hbar : LaurentPolynomial.C r * T m = LaurentPolynomial.C r * T (-m)) : m = 0 := by
  have h0 : r ≠ 0 := hr.ne_zero
  have := congrArg LaurentPolynomial.degree hbar
  rw [degree_C_mul_T _ _ h0, degree_C_mul_T _ _ h0] at this
  have h := WithBot.coe_injective this
  omega

/-- Over `ℤ`: a bar-invariant unit of `ℤ[q, q⁻¹]` is `±1`. -/
theorem int_bar_invariant_unit (u : ℤ[T;T⁻¹]) (hu : IsUnit u)
    (hbar : ∀ (ε m : ℤ), u = LaurentPolynomial.C ε * T m →
      LaurentPolynomial.C ε * T m = LaurentPolynomial.C ε * T (-m)) :
    u = 1 ∨ u = -1 := by
  obtain ⟨ε, m, hε, rfl⟩ := (int_isUnit_iff u).mp hu
  have hεu : IsUnit ε := by rcases hε with rfl | rfl <;> simp
  have hm := unit_bar_invariant_exponent_zero hεu m (hbar ε m rfl)
  subst hm
  rcases hε with rfl | rfl <;> simp

end QOU.MathlibExt.LaurentUnits
