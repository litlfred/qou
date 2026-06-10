import Mathlib.Tactic

/-!
# QOU.AlgebraicSubstrate.MetallicSilverFamily

Sorry-free proofs that the plancherel-convention cost coincidence
`t_pl(γ) = t_pl(σ₁)` on `H_n(q)` holds on `q > 0` EXACTLY at the silver
metallic ratio `δ_silver = 1 + √2`, for strand counts n = 3, 4, 5 —
extending the proved n = 2 statement
(`MetallicLPIdentities.silver_lp_coincidence`) up the strand ladder and
formalizing the probe finding `S(2) = S(3) = S(4) = S(5) = {δ_silver}`
(PR #2081).

## The closed forms (machine-derived, sympy exact; witness
`metallic-silver-family-closed-forms.witness.json`)

For each n, `Δ_n(q) = t_pl(γ) − t_pl(σ₁)` with plancherel weights
`y_λ = H_q(λ)²/[n]_q!` factors as

    Δ_n(q) = (q² − 2q − 1) · C_n(q)

with `C_n` sign-definite on q > 0 (each closed form below exhibits
`C_n` as ± a product of polynomials positive on q > 0).  The silver
quadratic `q² − 2q − 1` carries ALL the bar-breaking: every cofactor
is palindromic (bar-invariant under `q ↦ q⁻¹` up to the monomial
denominator).

## Theorems proved (all sorry-free)

  - `silver_minpoly_iff`: on q > 0, `q² − 2q − 1 = 0 ↔ q = δ_silver`
  - `silver_family_n3` / `_n4` / `_n5`: `Δ_n(q) = 0 ↔ q = δ_silver`
    on q > 0, for n = 3, 4, 5 (n = 2 is
    `MetallicLPIdentities.silver_lp_coincidence`)

`deltaSilver` here is definitionally `1 + √2`, the same value as
`MetallicLPIdentities.delta_silver`; it is kept LOCAL because that
module is currently red under the v4.24.0 toolchain bump (pre-existing
on main; separate repair thread).  Unify the two once the repair
lands.

-- Ref: [manuscript] rem:sdp-degeneracy-at-metallic-coincidence
-- Ref: [audit] docs/audits/2026-06-09-metallic-qrho-calibration-nova-cascade.md
-- Ref: [witness] folio-assistant/computations/metallic-silver-family-closed-forms.witness.json
-/

namespace QOU.AlgebraicSubstrate.MetallicSilverFamily

/-! ## Positivity helpers -/

lemma quad_minus_pos {q : ℝ} (hq : 0 < q) : 0 < q ^ 2 - q + 1 := by
  nlinarith [sq_nonneg (q - 1)]

lemma quad_plus_pos (q : ℝ) : 0 < q ^ 2 + q + 1 := by
  nlinarith [sq_nonneg (2 * q + 1)]

/-- The 10th-cyclotomic-shaped factor is positive on q > 0. -/
lemma cyc10_pos {q : ℝ} (hq : 0 < q) :
    0 < q ^ 4 - q ^ 3 + q ^ 2 - q + 1 := by
  rcases le_or_lt 1 q with h | h
  · nlinarith [mul_nonneg (mul_nonneg (mul_nonneg hq.le hq.le) hq.le)
      (sub_nonneg.mpr h), mul_nonneg hq.le (sub_nonneg.mpr h)]
  · nlinarith [mul_nonneg (mul_nonneg hq.le hq.le) (sub_nonneg.mpr h.le),
      sub_pos.mpr h, pow_pos hq 4]

/-! ## The silver ratio and its minimal polynomial on q > 0 -/

/-- The silver metallic ratio `δ_silver = 1 + √2` (local copy; see
    module docstring). -/
noncomputable def deltaSilver : ℝ := 1 + Real.sqrt 2

/-- `δ_silver` satisfies `x² − 2x − 1 = 0`. -/
theorem deltaSilver_minpoly :
    deltaSilver ^ 2 - 2 * deltaSilver - 1 = 0 := by
  unfold deltaSilver
  have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)
  ring_nf
  linarith [h2]

/-- On q > 0, the silver quadratic vanishes iff `q = δ_silver`. -/
theorem silver_minpoly_iff {q : ℝ} (hq : 0 < q) :
    q ^ 2 - 2 * q - 1 = 0 ↔ q = deltaSilver := by
  constructor
  · intro heq
    have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)
    have factor :
        (q - 1 - Real.sqrt 2) * (q - 1 + Real.sqrt 2) = q ^ 2 - 2 * q - 1 := by
      ring_nf
      linarith [h2]
    rw [← factor] at heq
    have h3 : Real.sqrt 2 > 1 := by
      have := Real.sqrt_lt_sqrt (by norm_num : (0:ℝ) ≤ 1)
        (by norm_num : (1:ℝ) < 2)
      simpa using this
    rcases mul_eq_zero.mp heq with h1 | h1
    · unfold deltaSilver
      linarith
    · linarith
  · intro h
    subst h
    exact deltaSilver_minpoly

/-! ## n = 3 -/

/-- `Δ₃(q) = t_pl(γ) − t_pl(σ₁)` on `H₃(q)` — machine-derived closed form. -/
noncomputable def Delta3 (q : ℝ) : ℝ :=
  -((q ^ 2 - 2 * q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) *
      (q ^ 4 + 3 * q ^ 2 + 1)) /
    (q ^ 4 * (q ^ 2 + 1))

/-- The n=3 silver-family coincidence: `Δ₃(q) = 0 ↔ q = δ_silver` on q > 0. -/
theorem silver_family_n3 {q : ℝ} (hq : 0 < q) :
    Delta3 q = 0 ↔ q = deltaSilver := by
  unfold Delta3
  have hB := quad_minus_pos hq
  have hC := quad_plus_pos q
  have hD : (0:ℝ) < q ^ 4 + 3 * q ^ 2 + 1 := by positivity
  have hden : (0:ℝ) < q ^ 4 * (q ^ 2 + 1) := by positivity
  rw [div_eq_zero_iff]
  constructor
  · rintro (hnum | hden0)
    · have hprod := neg_eq_zero.mp hnum
      have hA : q ^ 2 - 2 * q - 1 = 0 := by
        by_contra hA
        exact (mul_ne_zero (mul_ne_zero (mul_ne_zero hA (ne_of_gt hB))
          (ne_of_gt hC)) (ne_of_gt hD)) hprod
      exact (silver_minpoly_iff hq).mp hA
    · exact absurd hden0 (ne_of_gt hden)
  · intro h
    subst h
    left
    have hA := deltaSilver_minpoly
    rw [hA]
    ring

/-! ## n = 4 -/

/-- `Δ₄(q)` on `H₄(q)` — machine-derived closed form.  The degree-16
    cofactor has all-positive coefficients (palindromic, even). -/
noncomputable def Delta4 (q : ℝ) : ℝ :=
  -((q ^ 2 + 1) ^ 2 * (q ^ 2 - 2 * q - 1) *
      (q ^ 16 + 2 * q ^ 14 + 9 * q ^ 12 + 8 * q ^ 10 + 17 * q ^ 8 +
        8 * q ^ 6 + 9 * q ^ 4 + 2 * q ^ 2 + 1)) /
    (q ^ 7 * (q ^ 4 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1))

/-- The n=4 silver-family coincidence: `Δ₄(q) = 0 ↔ q = δ_silver` on q > 0. -/
theorem silver_family_n4 {q : ℝ} (hq : 0 < q) :
    Delta4 q = 0 ↔ q = deltaSilver := by
  unfold Delta4
  have hX : (0:ℝ) < (q ^ 2 + 1) ^ 2 := by positivity
  have hP : (0:ℝ) < q ^ 16 + 2 * q ^ 14 + 9 * q ^ 12 + 8 * q ^ 10 +
      17 * q ^ 8 + 8 * q ^ 6 + 9 * q ^ 4 + 2 * q ^ 2 + 1 := by positivity
  have hden : (0:ℝ) < q ^ 7 * (q ^ 4 + 1) * (q ^ 2 - q + 1) *
      (q ^ 2 + q + 1) :=
    mul_pos (mul_pos (mul_pos (by positivity) (by positivity))
      (quad_minus_pos hq)) (quad_plus_pos q)
  rw [div_eq_zero_iff]
  constructor
  · rintro (hnum | hden0)
    · have hprod := neg_eq_zero.mp hnum
      have hA : q ^ 2 - 2 * q - 1 = 0 := by
        by_contra hA
        exact (mul_ne_zero (mul_ne_zero (ne_of_gt hX) hA)
          (ne_of_gt hP)) hprod
      exact (silver_minpoly_iff hq).mp hA
    · exact absurd hden0 (ne_of_gt hden)
  · intro h
    subst h
    left
    have hA := deltaSilver_minpoly
    rw [hA]
    ring

/-! ## n = 5 -/

/-- `Δ₅(q)` on `H₅(q)` — machine-derived closed form.  The degree-36
    cofactor has all-positive coefficients (palindromic, even). -/
noncomputable def Delta5 (q : ℝ) : ℝ :=
  -((q ^ 2 - 2 * q - 1) *
      (q ^ 36 + 6 * q ^ 34 + 21 * q ^ 32 + 58 * q ^ 30 + 136 * q ^ 28 +
        268 * q ^ 26 + 443 * q ^ 24 + 630 * q ^ 22 + 778 * q ^ 20 +
        838 * q ^ 18 + 778 * q ^ 16 + 630 * q ^ 14 + 443 * q ^ 12 +
        268 * q ^ 10 + 136 * q ^ 8 + 58 * q ^ 6 + 21 * q ^ 4 +
        6 * q ^ 2 + 1)) /
    (q ^ 11 * (q ^ 4 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) *
      (q ^ 4 - q ^ 3 + q ^ 2 - q + 1) * (q ^ 4 + q ^ 3 + q ^ 2 + q + 1))

/-- The n=5 silver-family coincidence: `Δ₅(q) = 0 ↔ q = δ_silver` on q > 0. -/
theorem silver_family_n5 {q : ℝ} (hq : 0 < q) :
    Delta5 q = 0 ↔ q = deltaSilver := by
  unfold Delta5
  have hP : (0:ℝ) < q ^ 36 + 6 * q ^ 34 + 21 * q ^ 32 + 58 * q ^ 30 +
      136 * q ^ 28 + 268 * q ^ 26 + 443 * q ^ 24 + 630 * q ^ 22 +
      778 * q ^ 20 + 838 * q ^ 18 + 778 * q ^ 16 + 630 * q ^ 14 +
      443 * q ^ 12 + 268 * q ^ 10 + 136 * q ^ 8 + 58 * q ^ 6 +
      21 * q ^ 4 + 6 * q ^ 2 + 1 := by positivity
  have hden : (0:ℝ) < q ^ 11 * (q ^ 4 + 1) * (q ^ 2 - q + 1) *
      (q ^ 2 + q + 1) * (q ^ 4 - q ^ 3 + q ^ 2 - q + 1) *
      (q ^ 4 + q ^ 3 + q ^ 2 + q + 1) :=
    mul_pos (mul_pos (mul_pos (mul_pos (mul_pos (by positivity)
      (by positivity)) (quad_minus_pos hq)) (quad_plus_pos q))
      (cyc10_pos hq)) (by positivity)
  rw [div_eq_zero_iff]
  constructor
  · rintro (hnum | hden0)
    · have hprod := neg_eq_zero.mp hnum
      have hA : q ^ 2 - 2 * q - 1 = 0 := by
        by_contra hA
        exact (mul_ne_zero hA (ne_of_gt hP)) hprod
      exact (silver_minpoly_iff hq).mp hA
    · exact absurd hden0 (ne_of_gt hden)
  · intro h
    subst h
    left
    have hA := deltaSilver_minpoly
    rw [hA]
    ring

end QOU.AlgebraicSubstrate.MetallicSilverFamily
