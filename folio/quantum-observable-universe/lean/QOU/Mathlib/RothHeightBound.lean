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

/-- **Vanishing to order `k` at `p/q` is divisibility by `(qX − p)^k`, over `ℚ`.**

`(qX − p)^k = q^k · (X − p/q)^k` and `C q ^ k` is a unit in `ℚ[X]`, so the two divisibilities
are one statement downstairs.  Extracted because **both** halves of §10 — the leading and the
trailing coefficient — consume exactly this and nothing else. -/
theorem map_qX_sub_C_pow_dvd_of_taylor_coeff_eq_zero {p q : ℤ} (hq : q ≠ 0) {P : ℤ[X]} (k : ℕ)
    (h : ∀ d < k, (taylor ((p : ℚ) / (q : ℚ)) (P.map (algebraMap ℤ ℚ))).coeff d = 0) :
    ((C q * X - C p : ℤ[X]) ^ k).map (algebraMap ℤ ℚ) ∣ P.map (algebraMap ℤ ℚ) := by
  have hqQ : ((q : ℚ)) ≠ 0 := Int.cast_ne_zero.mpr hq
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
  rw [hfactor, mul_comm]
  exact hunit.mul_right_dvd.mpr hdvdQ

/-- **The `m = 1` base case of Roth's lemma, complete.**

If `P ∈ ℤ[X]` vanishes to order `k` at `p/q` — every coefficient of the translate below `k`
is zero — with `p, q` coprime and `q > 0`, then `q^k ≤ |lead P|`.

With Roth's hypothesis `H(P) ≤ q^{εd}` this gives `q^{θd} ≤ q^{εd}`, i.e. the index `θ ≤ ε`.
No Mahler measure anywhere. -/
theorem pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero {p q : ℤ} (hq : 0 < q)
    (hco : IsCoprime p q) {P : ℤ[X]} (hP : P ≠ 0) (k : ℕ)
    (h : ∀ d < k, (taylor ((p : ℚ) / (q : ℚ)) (P.map (algebraMap ℤ ℚ))).coeff d = 0) :
    q ^ k ≤ |P.leadingCoeff| :=
  pow_le_abs_leadingCoeff_of_map_dvd hq hco hP k
    (map_qX_sub_C_pow_dvd_of_taylor_coeff_eq_zero hq.ne' k h)

/-! ### §10's **other** half — the lowest non-zero coefficient

Mahler, §10, verbatim:

> `A(x) = (Qx − P)^j B(x)` where `B(x)` is a certain polynomial with integral coefficients.
> Hence the lowest and the highest non-zero coefficients of `A(x)` are divisible by `P^j` and
> `Q^j`, respectively.  It follows that `H^j ≤ |A| ≤ a`.

Everything above proves the `Q^j` half, and an earlier note in this file called that "the
`m = 1` base case … **complete**".  It is complete as a statement about the *leading*
coefficient; it is **not** §10's bound.  `H` is `max(|P|, |Q|)`, and `|Q|^j ≤ |A|` says
nothing whenever the height is carried by the numerator: `κ = 99/1` has `H = 99` and `Q = 1`,
so the leading-coefficient bound degenerates to `1 ≤ |A|`.  The trailing half is the whole
source of the `H^j`.

⚠ **The two halves are not symmetric in Lean the way they read on the page.**  `q > 0` comes
free — Lean's `ℚ` keeps a positive denominator — but `p ≠ 0` does not, and at `p = 0` Mahler's
sentence is *vacuous* rather than false: `P^j = 0` divides only `0`.  So the trailing lemmas
below carry `p ≠ 0` and the assembled bound discharges `κ = 0` separately, where coprimality
forces `q = 1` and `H^j = 1`.  Reading "the lowest and the highest … respectively" as one
symmetric statement is what hides that case.
-/

/-- In a domain, a divisor's trailing coefficient divides the trailing coefficient.

The mirror of `leadingCoeff_dvd_of_dvd`, and equally cheap: `trailingCoeff` is multiplicative
for the same reason `leadingCoeff` is. -/
theorem trailingCoeff_dvd_of_dvd {R : Type*} [CommRing R] [IsDomain R] {A P : R[X]}
    (h : A ∣ P) : A.trailingCoeff ∣ P.trailingCoeff := by
  obtain ⟨B, rfl⟩ := h
  rw [trailingCoeff_mul]
  exact Dvd.intro _ rfl

/-- Trailing coefficients are multiplicative on powers. -/
theorem trailingCoeff_pow {R : Type*} [CommRing R] [IsDomain R] (A : R[X]) (k : ℕ) :
    (A ^ k).trailingCoeff = A.trailingCoeff ^ k := by
  induction k with
  | zero => simp [trailingCoeff]
  | succ k ih => rw [pow_succ, trailingCoeff_mul, ih, pow_succ]

/-- The trailing coefficient of `q·X − p` is `−p`, when `p ≠ 0`.

Contrast `leadingCoeff_qX_sub_C`, which needs `q ≠ 0` instead: each end of the polynomial is
carried by its own coefficient, so each half of §10 has its own non-vanishing hypothesis. -/
theorem trailingCoeff_qX_sub_C {q p : ℤ} (hp : p ≠ 0) :
    (C q * X - C p : ℤ[X]).trailingCoeff = -p := by
  have h0 : (C q * X - C p : ℤ[X]).coeff 0 = -p := by simp
  have hnt : (C q * X - C p : ℤ[X]).natTrailingDegree = 0 := by
    refine natTrailingDegree_eq_zero_of_constantCoeff_ne_zero ?_
    rw [constantCoeff_apply, h0]
    exact neg_ne_zero.mpr hp
  rw [trailingCoeff, hnt, h0]

/-- **§10's lowest-coefficient bound.**  If `(qX − p)^k ∣ P` in `ℤ[X]` with `p ≠ 0` and
`P ≠ 0`, then `p^k` divides — hence `|p|^k` bounds — `P`'s lowest non-zero coefficient.

`(−p)^k` and `p^k` differ by the unit `(−1)^k`, which is why the sign Mahler suppresses costs
nothing. -/
theorem pow_le_abs_trailingCoeff_of_linear_pow_dvd {p q : ℤ} (hp : p ≠ 0) {P : ℤ[X]}
    (hP : P ≠ 0) (k : ℕ) (h : (C q * X - C p : ℤ[X]) ^ k ∣ P) :
    |p| ^ k ≤ |P.trailingCoeff| := by
  have hdvd : p ^ k ∣ P.trailingCoeff := by
    have htc := trailingCoeff_dvd_of_dvd h
    rw [trailingCoeff_pow, trailingCoeff_qX_sub_C hp] at htc
    exact dvd_trans ⟨(-1) ^ k, by rw [neg_pow]; ring⟩ htc
  have hpos : 0 < |P.trailingCoeff| :=
    abs_pos.mpr (trailingCoeff_nonzero_iff_nonzero.mpr hP)
  rw [← abs_pow]
  exact Int.le_of_dvd hpos ((abs_dvd _ _).mpr ((dvd_abs _ _).mpr hdvd))

/-- The trailing half over `ℚ`, via the same one-sided Gauss bridge as the leading half. -/
theorem pow_le_abs_trailingCoeff_of_map_dvd {p q : ℤ} (hp : p ≠ 0) (hco : IsCoprime p q)
    {P : ℤ[X]} (hP : P ≠ 0) (k : ℕ)
    (h : ((C q * X - C p : ℤ[X]) ^ k).map (algebraMap ℤ ℚ) ∣ P.map (algebraMap ℤ ℚ)) :
    |p| ^ k ≤ |P.trailingCoeff| :=
  pow_le_abs_trailingCoeff_of_linear_pow_dvd hp hP k
    (dvd_of_isPrimitive_of_map_dvd_map ((isPrimitive_qX_sub_C hco).pow k) hP h)

/-- The trailing half from vanishing to order `k` — the mirror of
`pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero`, off the same shared divisibility. -/
theorem pow_le_abs_trailingCoeff_of_taylor_coeff_eq_zero {p q : ℤ} (hq : q ≠ 0) (hp : p ≠ 0)
    (hco : IsCoprime p q) {P : ℤ[X]} (hP : P ≠ 0) (k : ℕ)
    (h : ∀ d < k, (taylor ((p : ℚ) / (q : ℚ)) (P.map (algebraMap ℤ ℚ))).coeff d = 0) :
    |p| ^ k ≤ |P.trailingCoeff| :=
  pow_le_abs_trailingCoeff_of_map_dvd hp hco hP k
    (map_qX_sub_C_pow_dvd_of_taylor_coeff_eq_zero hq k h)

/-- **§10's `H^j`, both halves assembled.**

`H = max(|p|, |q|)` is the height of `κ = p/q`, and each of the two coefficients §10 names is
one of `P`'s coefficients, so the max of their absolute values is bounded by any bound on all
of them.  This is the inequality §10 turns into `Θ₁ ≤ log a / (r log H)`.

The `p = 0` corner is genuine mathematics, not bookkeeping: `κ = 0` offers no `P^j`
divisibility at all, and the bound survives only because coprimality then forces `q = 1`, so
`H = 1`. -/
theorem max_abs_pow_le_max_abs_trailingCoeff_leadingCoeff {p q : ℤ} (hq : 0 < q)
    (hco : IsCoprime p q) {P : ℤ[X]} (hP : P ≠ 0) (k : ℕ)
    (h : ∀ d < k, (taylor ((p : ℚ) / (q : ℚ)) (P.map (algebraMap ℤ ℚ))).coeff d = 0) :
    max |p| |q| ^ k ≤ max |P.trailingCoeff| |P.leadingCoeff| := by
  have hlead : |q| ^ k ≤ max |P.trailingCoeff| |P.leadingCoeff| := by
    rw [abs_of_pos hq]
    exact (pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero hq hco hP k h).trans
      (le_max_right _ _)
  rcases eq_or_ne p 0 with rfl | hp
  · rw [abs_zero, max_eq_right (abs_nonneg q)]
    exact hlead
  · rcases le_total |p| |q| with hle | hle
    · rw [max_eq_right hle]
      exact hlead
    · rw [max_eq_left hle]
      exact (pow_le_abs_trailingCoeff_of_taylor_coeff_eq_zero hq.ne' hp hco hP k h).trans
        (le_max_left _ _)

/-- **§10 verbatim: `H^j ≤ |A| ≤ a`.**

`|A|` is Mahler's height — the sup norm on coefficients — so the hypothesis is exactly
`InRothPolySet`'s third clause at one variable. -/
theorem max_abs_pow_le_of_abs_coeff_le {p q : ℤ} (hq : 0 < q) (hco : IsCoprime p q)
    {P : ℤ[X]} (hP : P ≠ 0) (k : ℕ) {a : ℤ} (ha : ∀ n, |P.coeff n| ≤ a)
    (h : ∀ d < k, (taylor ((p : ℚ) / (q : ℚ)) (P.map (algebraMap ℤ ℚ))).coeff d = 0) :
    max |p| |q| ^ k ≤ a :=
  (max_abs_pow_le_max_abs_trailingCoeff_leadingCoeff hq hco hP k h).trans
    (max_le (ha P.natTrailingDegree) (ha P.natDegree))

end Translate

/-! ### Next

1. ~~Gauss into `ℤ[X]`~~ — **done**.
2. ~~Vanishing to order `k` ⟹ divisibility~~ — **done**.
3. ~~§10's `H^j ≤ |A|`~~ — **done**, `max_abs_pow_le_of_abs_coeff_le`, with no analysis in it.

   ⚠⚠ **This item used to read "the `m = 1` base case of Roth's lemma is
   `pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero`, complete".  That was wrong** — the
   seventeenth correction in this arc.  That theorem is the `Q^j` half of §10 and bounds
   `|q|^k`, but §10's height is `H = max(|p|, |q|)`, so the leading half alone proves nothing
   whenever the numerator is the larger — which is the typical case.  The failure shape is
   the arc's most persistent one: a **true theorem** was labelled with the name of the
   **statement it was a step toward**, and the label was then read back as a completion.
   Same species as corrections 12 and 14, and it survived precisely because the Lean
   type-checks: nothing in a green build objects to a docstring.

4. **The induction step** — the remaining work, and where Gelfond / Mahler is genuinely
   needed: bounding the heights of the factors `φₖ, ψₖ` in terms of `H(P)`.  The
   factorization itself is proved (`QOU.Mathlib.SeparatedWronskian`,
   `det_separated_wronskian`); it is the height control on the factors that is missing.

⚠ The `index`-side hypothesis of (2) is stated as "every coefficient of the translate below
`k` vanishes", which is what `QOU.Mathlib.RothIndex`'s `index`/`translate` machinery produces
in one variable.  Wiring the two together is bookkeeping, not new mathematics, and is
deliberately left until the multivariate statement of Roth's lemma fixes the shape it should
take. -/

end Polynomial
