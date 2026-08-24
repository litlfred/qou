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
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.Algebra.Polynomial.Taylor
import Mathlib.Algebra.Polynomial.Div

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

/-! ### Moving the divisibility from `ℚ[X]` into `ℤ[X]`

What "`P` vanishes to order `k` at `p/q`" gives is divisibility over `ℚ`.  The bound above
needs it over `ℤ`.  Gauss's lemma bridges the two — but Mathlib's form wants *both*
polynomials primitive, and the auxiliary polynomial of Roth's lemma is not. -/

/-- `q·X − p` is primitive when `p` and `q` are coprime: any constant dividing it divides
both coefficients. -/
theorem isPrimitive_qX_sub_C {p q : ℤ} (h : IsCoprime p q) :
    (C q * X - C p : ℤ[X]).IsPrimitive := by
  rw [isPrimitive_iff_isUnit_of_C_dvd]
  intro r hr
  rw [C_dvd_iff_dvd_coeff] at hr
  have h1 : r ∣ q := by
    have hr1 := hr 1
    rwa [coeff_sub, coeff_C_mul, coeff_X_one, mul_one, coeff_C, if_neg one_ne_zero,
      sub_zero] at hr1
  have h0 : r ∣ p := by
    have hr0 := hr 0
    simp only [coeff_sub, coeff_C_mul, coeff_X_zero, mul_zero, coeff_C_zero, zero_sub] at hr0
    exact (dvd_neg).mp hr0
  exact h.isUnit_of_dvd' h0 h1

/-- **Gauss, one-sided.**  A *primitive* divisor over `ℚ` is a divisor over `ℤ`, with no
primitivity hypothesis on the dividend.

Mathlib's `IsPrimitive.dvd_of_fraction_map_dvd_fraction_map` requires **both** polynomials
primitive, which the auxiliary polynomial of Roth's lemma is not.  Splitting off the content
removes that hypothesis: the content is a unit downstairs, so it cancels. -/
theorem dvd_of_isPrimitive_of_map_dvd_map {A P : ℤ[X]} (hA : A.IsPrimitive) (hP : P ≠ 0)
    (h : A.map (algebraMap ℤ ℚ) ∣ P.map (algebraMap ℤ ℚ)) : A ∣ P := by
  have hcz : P.content ≠ 0 := fun hc => hP (content_eq_zero_iff.mp hc)
  have hcq : ((P.content : ℚ)) ≠ 0 := Int.cast_ne_zero.mpr hcz
  have hmap : P.map (algebraMap ℤ ℚ)
      = C ((P.content : ℚ)) * P.primPart.map (algebraMap ℤ ℚ) := by
    conv_lhs => rw [eq_C_content_mul_primPart P]
    simp
  rw [hmap] at h
  have hunit : IsUnit (C ((P.content : ℚ)) : ℚ[X]) :=
    isUnit_C.mpr (isUnit_iff_ne_zero.mpr hcq)
  have h2 : A.map (algebraMap ℤ ℚ) ∣ P.primPart.map (algebraMap ℤ ℚ) :=
    hunit.dvd_mul_left.mp h
  exact (hA.dvd_of_fraction_map_dvd_fraction_map (isPrimitive_primPart P) h2).trans
    (primPart_dvd P)

/-- Powers of a primitive polynomial are primitive. -/
theorem IsPrimitive.pow {R : Type*} [CommRing R] [IsDomain R] [NormalizedGCDMonoid R]
    {A : R[X]} (hA : A.IsPrimitive) :
    ∀ k : ℕ, (A ^ k).IsPrimitive
  | 0 => by
      rw [pow_zero]
      rw [isPrimitive_iff_isUnit_of_C_dvd]
      intro r hr
      exact isUnit_of_dvd_one (by simpa using (C_dvd_iff_dvd_coeff r 1).mp hr 0)
  | k + 1 => by
      rw [pow_succ]
      exact (IsPrimitive.pow hA k).mul hA

/-- **The `m = 1` base case of Roth's lemma, assembled.**

If `(qX − p)^k` divides `P` *over `ℚ`* — which is what "`P` vanishes to order `k` at `p/q`"
gives — with `p, q` coprime and `q > 0`, then `q^k ≤ |lead P|`.

Gauss moves the divisibility into `ℤ[X]`, where the leading coefficient argument applies.
No Mahler measure, no analysis. -/
theorem pow_le_abs_leadingCoeff_of_map_dvd {p q : ℤ} (hq : 0 < q) (hco : IsCoprime p q)
    {P : ℤ[X]} (hP : P ≠ 0) (k : ℕ)
    (h : ((C q * X - C p : ℤ[X]) ^ k).map (algebraMap ℤ ℚ) ∣ P.map (algebraMap ℤ ℚ)) :
    q ^ k ≤ |P.leadingCoeff| :=
  pow_le_abs_leadingCoeff_of_linear_pow_dvd hq hP k
    (dvd_of_isPrimitive_of_map_dvd_map ((isPrimitive_qX_sub_C hco).pow k) hP h)

/-! ### Vanishing to order `k` is divisibility

The last step of the base case: what the index gives is that the low coefficients of the
*translate* vanish, and that must become divisibility by `(X − a)^k`. -/

section Translate

variable {R : Type*} [CommRing R]

theorem taylor_sub_C_pow (a : R) (k : ℕ) :
    taylor a ((X - C a) ^ k) = (X : R[X]) ^ k := by
  rw [taylor_apply, pow_comp]
  congr 1
  simp [sub_comp]

theorem taylor_neg_X_pow (a : R) (k : ℕ) :
    taylor (-a) ((X : R[X]) ^ k) = (X - C a) ^ k := by
  rw [taylor_apply, pow_comp, X_comp]
  congr 1
  simp [sub_eq_add_neg]

/-- **Vanishing to order `k` at `a` is divisibility by `(X − a)^k`**, read off the translate.

`taylor a P` is `P(X + a)`, so its low coefficients are exactly the derivatives at `a`. -/
theorem sub_C_pow_dvd_iff_X_pow_dvd_taylor {a : R} {k : ℕ} {P : R[X]} :
    (X - C a) ^ k ∣ P ↔ (X : R[X]) ^ k ∣ taylor a P := by
  constructor
  · rintro ⟨Q, rfl⟩
    exact ⟨taylor a Q, by rw [taylor_mul, taylor_sub_C_pow]⟩
  · rintro ⟨Q, hQ⟩
    refine ⟨taylor (-a) Q, ?_⟩
    have h := congrArg (taylor (-a)) hQ
    rw [taylor_taylor, neg_add_cancel, taylor_zero] at h
    rw [h, taylor_mul, taylor_neg_X_pow]

/-- **The `m = 1` base case of Roth's lemma, complete.**

If `P ∈ ℤ[X]` vanishes to order `k` at `p/q` — every coefficient of the translate below `k`
is zero — with `p, q` coprime and `q > 0`, then `q^k ≤ |lead P|`.

With Roth's hypothesis `H(P) ≤ q^{εd}` this gives `q^{θd} ≤ q^{εd}`, i.e. the index `θ ≤ ε`.
No Mahler measure anywhere. -/
theorem pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero {p q : ℤ} (hq : 0 < q)
    (hco : IsCoprime p q) {P : ℤ[X]} (hP : P ≠ 0) (k : ℕ)
    (h : ∀ d < k, (taylor ((p : ℚ) / (q : ℚ)) (P.map (algebraMap ℤ ℚ))).coeff d = 0) :
    q ^ k ≤ |P.leadingCoeff| := by
  have hqQ : ((q : ℚ)) ≠ 0 := Int.cast_ne_zero.mpr hq.ne'
  -- vanishing ⟹ divisibility by `(X − p/q)^k` over ℚ
  have hdvdQ : ((X : ℚ[X]) - C ((p : ℚ) / (q : ℚ))) ^ k ∣ P.map (algebraMap ℤ ℚ) :=
    sub_C_pow_dvd_iff_X_pow_dvd_taylor.mpr (X_pow_dvd_iff.mpr h)
  -- `qX − p` is `q · (X − p/q)`, and `C q` is a unit downstairs
  have hfactor : ((C q * X - C p : ℤ[X]) ^ k).map (algebraMap ℤ ℚ)
      = C ((q : ℚ)) ^ k * ((X : ℚ[X]) - C ((p : ℚ) / (q : ℚ))) ^ k := by
    rw [Polynomial.map_pow, ← mul_pow]
    congr 1
    simp only [Polynomial.map_sub, Polynomial.map_mul, map_X, algebraMap_int_eq,
      eq_intCast, mul_sub, ← C_mul]
    rw [mul_div_cancel₀ _ hqQ]
    simp
  have hunit : IsUnit ((C ((q : ℚ)) : ℚ[X]) ^ k) :=
    (isUnit_C.mpr (isUnit_iff_ne_zero.mpr hqQ)).pow k
  have hmapdvd : ((C q * X - C p : ℤ[X]) ^ k).map (algebraMap ℤ ℚ)
      ∣ P.map (algebraMap ℤ ℚ) := by
    rw [hfactor, mul_comm]
    exact hunit.mul_right_dvd.mpr hdvdQ
  exact pow_le_abs_leadingCoeff_of_map_dvd hq hco hP k hmapdvd

end Translate

/-! ### Next

1. ~~Gauss into `ℤ[X]`~~ — **done**.
2. ~~Vanishing to order `k` ⟹ divisibility~~ — **done**.  The `m = 1` base case of Roth's
   lemma is `pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero` above, **complete and with no
   analysis in it**.
3. **The induction step** — the remaining work, and where Gelfond / Mahler is genuinely
   needed: bounding the heights of the factors `φₖ, ψₖ` in terms of `H(P)`.  The
   factorization itself is proved (`QOU.Mathlib.SeparatedWronskian`,
   `det_separated_wronskian`); it is the height control on the factors that is missing.

⚠ The `index`-side hypothesis of (2) is stated as "every coefficient of the translate below
`k` vanishes", which is what `QOU.Mathlib.RothIndex`'s `index`/`translate` machinery produces
in one variable.  Wiring the two together is bookkeeping, not new mathematics, and is
deliberately left until the multivariate statement of Roth's lemma fixes the shape it should
take. -/

end Polynomial
