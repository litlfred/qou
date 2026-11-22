import QOU.BraidKnot.CentralIdempotentSignTwist
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.RingTheory.Localization.FractionRing

/-
# The central-idempotent theorem over `Frac R[q, q⁻¹]`

`R` is any integral domain: `R = ℤ` gives `ℚ(q)`, `R = 𝔽_p` gives `𝔽_p(q)`.
`e_λ` is not an element of the Laurent-polynomial Hecke algebra over `R[q, q⁻¹]`
itself: its Lagrange factors divide by `q^{2m} − 1`, which are not units there.
It is defined over the fraction field, where `q` is not a root of unity. This
file instantiates `explicit_central_idempotent_cross_checks` at that field.
-/

open LaurentPolynomial

namespace QOU.BraidKnot.CentralIdempotentLaurent

variable (R : Type*) [CommRing R] [IsDomain R]

/-- The fraction field of the Laurent polynomials `R[q, q⁻¹]`. -/
abbrev Kq := FractionRing (LaurentPolynomial R)

/-- The generic parameter `q = T 1`. -/
noncomputable def qGen : Kq R := algebraMap (LaurentPolynomial R) (Kq R) (T 1)

theorem T_eq_one_iff (m : ℤ) : (T m : LaurentPolynomial R) = 1 ↔ m = 0 := by
  constructor
  · intro h
    rw [← T_zero] at h
    exact (Finsupp.single_left_inj (one_ne_zero)).mp h
  · rintro rfl; exact T_zero

theorem qGen_ne_zero : qGen R ≠ 0 := by
  intro h
  have : (T 1 : LaurentPolynomial R) = 0 :=
    (IsFractionRing.injective (LaurentPolynomial R) (Kq R)) (by rw [map_zero]; exact h)
  have h1 : (T 1 : LaurentPolynomial R) * T (-1) = 1 := by rw [← T_add]; simp
  rw [this, zero_mul] at h1
  exact zero_ne_one h1

theorem qGen_notRootOfUnity : QOU.SchurWeyl.GenericParameter.NotRootOfUnity (qGen R) := by
  intro m hm h
  have h1 : algebraMap (LaurentPolynomial R) (Kq R) (T (m : ℤ)) = algebraMap (LaurentPolynomial R) (Kq R) 1 := by
    rw [map_one, ← h, qGen, ← map_pow, T_pow, mul_one]
  have := (T_eq_one_iff R (m : ℤ)).mp (IsFractionRing.injective (LaurentPolynomial R) (Kq R) h1)
  omega

open QOU.SchurWeyl ExplicitCentralIdempotentGeneral in
/-- **The theorem over `Frac R[q, q⁻¹]`** (any characteristic), with `q` the Laurent variable:
the elements `e_λ` are central, idempotent, pairwise orthogonal and sum to `1`. -/
theorem cross_checks_laurent (n : ℕ) :
    (∀ lam, ∀ x : Hecke (Kq R) (qGen R) (qGen R)⁻¹ n,
        centralIdem (qGen R) n lam * x = x * centralIdem (qGen R) n lam) ∧
    (∀ lam, centralIdem (qGen R) n lam * centralIdem (qGen R) n lam = centralIdem (qGen R) n lam) ∧
    (∀ lam mu, lam ≠ mu → centralIdem (qGen R) n lam * centralIdem (qGen R) n mu = 0) ∧
    (∑ lam, centralIdem (qGen R) n lam = 1) :=
  explicit_central_idempotent_cross_checks (qGen R) (qGen_ne_zero R) (qGen_notRootOfUnity R) n

/-- `ℚ(q)`. -/
example (n : ℕ) := cross_checks_laurent ℤ n

/-- `𝔽_p(q)`, positive characteristic. -/
example (p : ℕ) [Fact p.Prime] (n : ℕ) := cross_checks_laurent (ZMod p) n

end QOU.BraidKnot.CentralIdempotentLaurent
