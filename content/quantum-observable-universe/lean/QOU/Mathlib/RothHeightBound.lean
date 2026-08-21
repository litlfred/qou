/-
  **The height bound at `m = 1`** — the arithmetic half of Roth's lemma's base case.

  Bean `qou-4lbh`.  ⚠ Mathlib-style, Mathlib imports only, no QOU dependency: liftable
  verbatim.

  ═══ ⚠ THIS CORRECTS A RECORDED ASSESSMENT ═══

  `qou-4lbh` was opened on the finding that Roth's lemma's remaining cost is **height
  theory**, and that the `m = 1` base case is "the analytic half of the theorem", blocked on
  two Mahler-measure bridges Mathlib lacks:

    * the Jensen form `M(P) = ‖lead‖ · ∏ max(1, ‖root‖)`,
    * Landau's `M(P) ≤ √(deg+1) · H(P)`.

  **That is wrong for the base case.**  The bound needed at `m = 1` is elementary and is
  proved below with no analysis whatsoever:

    if `(qX − p)^k ∣ P` in `ℤ[X]` and `P ≠ 0`, then `q^k ≤ |lead P| ≤ H(P)`

  because the leading coefficient of `(qX − p)^k` is `q^k`, and in a domain a divisor's
  leading coefficient divides the dividend's.  One line of algebra, not complex analysis.

  ═══ WHAT MAHLER MEASURE IS ACTUALLY FOR ═══

  The textbook route (Gelfond's inequality, or multiplicativity of the Mahler measure) is
  needed to bound the heights of **factors** in terms of the height of a product — going from
  `H(P)` *down to* `H(φ)` and `H(ψ)`.  That is the induction step of Roth's lemma, where the
  auxiliary polynomial is split as `P = ∑ₖ φₖ(x) ψₖ(y)` and the factors' heights must be
  controlled.

  The base case goes the other way — from a *divisor* up to the dividend — and that direction
  is free.  Conflating the two is what produced the wrong assessment.

  ═══ WHAT STILL CONNECTS THIS TO THE INDEX ═══

  To reach the base case in full one still needs `index ≥ θ ⟹ (qX − p)^{θd} ∣ P`, which is
  the index/divisibility bridge (`QOU.Mathlib.RothIndex`, `X_pow_dvd_iff_support`) transported
  to one variable, plus Gauss's lemma to move the divisibility from `ℚ[X]` into `ℤ[X]`.
  Mathlib has the latter: `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`.
-/
import Mathlib.RingTheory.Polynomial.GaussLemma
import Mathlib.Algebra.Polynomial.Degree.Operations

namespace Polynomial

/-- In a domain, a divisor's leading coefficient divides the leading coefficient. -/
theorem leadingCoeff_dvd_of_dvd {R : Type*} [CommRing R] [IsDomain R] {A P : R[X]}
    (h : A ∣ P) : A.leadingCoeff ∣ P.leadingCoeff := by
  obtain ⟨B, rfl⟩ := h
  rw [leadingCoeff_mul]
  exact Dvd.intro _ rfl

/-- The leading coefficient of `q·X − p` is `q`. -/
theorem leadingCoeff_qX_sub_C {q p : ℤ} (hq : q ≠ 0) :
    (C q * X - C p : ℤ[X]).leadingCoeff = q := by
  have h : (C q * X - C p : ℤ[X]) = C q * X + C (-p) := by
    rw [map_neg]; ring
  rw [h, leadingCoeff_linear hq]

/-- **The `m = 1` height bound for Roth's lemma, proved elementarily.**

If `(qX − p)^k` divides `P` in `ℤ[X]` and `P ≠ 0`, then `q^k ≤ |lead P|`, hence `q^k ≤ H(P)`
for any height that dominates the leading coefficient.

This is exactly what the base case of Roth's lemma consumes: with the hypothesis
`H(P) ≤ q^{εd}` it gives `q^{θd} ≤ q^{εd}`, so the index `θ` is at most `ε`. -/
theorem pow_le_abs_leadingCoeff_of_linear_pow_dvd {p q : ℤ} (hq : 0 < q) {P : ℤ[X]}
    (hP : P ≠ 0) (k : ℕ) (h : (C q * X - C p : ℤ[X]) ^ k ∣ P) :
    q ^ k ≤ |P.leadingCoeff| := by
  have hdvd : q ^ k ∣ P.leadingCoeff := by
    have hlc := leadingCoeff_dvd_of_dvd h
    rwa [leadingCoeff_pow, leadingCoeff_qX_sub_C hq.ne'] at hlc
  have hpos : 0 < |P.leadingCoeff| := abs_pos.mpr (leadingCoeff_ne_zero.mpr hP)
  exact Int.le_of_dvd hpos ((dvd_abs _ _).mpr hdvd)

/-! ### Next

1. **Index to divisibility in one variable.**  `index ≥ θ ⟹ (X − p/q)^{θd} ∣ P` over `ℚ[X]`,
   then `(qX − p)` is primitive when `gcd p q = 1`, so Gauss moves it into `ℤ[X]`.
2. **The base case** then follows by combining (1) with the bound above.
3. **The induction step** — and *this* is where Gelfond / Mahler is genuinely needed, to
   bound the heights of the factors `φₖ, ψₖ` in terms of `H(P)`.  The factorization itself is
   already proved (`QOU.Mathlib.SeparatedWronskian`, `det_separated_wronskian`); it is the
   height control on the factors that is missing. -/

end Polynomial
