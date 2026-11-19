import Mathlib.Tactic.Positivity
import QOU.BraidKnot.QBetaCategoricalPrecisionLadder
import QOU.BraidKnot.LadderConventionLocalisation
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.QBeta.CoshHolonomyAndGPMTBaseBridge
import QOU.QBeta.WedderburnPhaseAndTwoTermPinBridge

/-!
# First-Principles Quartic Habiro Rung `c_4` (`O(u^4) = O(ℏ_q^8)`), Wedderburn Kurtosis, and Connected Borromean QED Subleading Series (`qou-51yf`)

This module formalizes the exact algebraic, formal-series-remainder, and real-analytic bounds for the
fourth-order Habiro / Kashiwara / Wedderburn ladder rung `c_4` (`u(q)^4 = b(q)^4 ℏ_q^8 ≈ 5.263 × 10⁻⁹`)
under Convention D (`z_D = q^3 / (q^2 + 1)`):

1. **Section 1 — Rationality of All Even Habiro Rungs (`u^{2m}(q) ∈ ℚ(q)`) and `ℏ_q^8` Classical Anchor**:
   * Whereas odd ladder powers `u(q)^{2m+1}` carry the quadratic radical `b(q) = √(q^4 + q^2 + 1)/(q^2 + 1)`,
     all even ladder powers `u(q)^{2m} = ((h^2 + 3)/(h^2 + 4))^m ℏ_q^{4m}` lie in `ℚ(q)` with zero radicals
     (`uSq_rational_in_q`, `uFourth_rational_in_q`, `uEvenPow_rational_in_q`).
   * Exact rational Taylor polynomial remainder identities (`uSq_taylor_poly8_remainder`,
     `uFourth_at_classical_leading`, `uFourth_taylor_poly10_remainder`) certify the `(9/16) ℏ_q^8`
     classical leading coefficient of `u(q)^4` and the vanishing of the `ℏ_q^9` term.

2. **Section 2 — Contribution A: Even-Rung Kashiwara Divided-Power, Habiro Cyclotomic Norm, and Chebyshev Holonomy**:
   * `even_product_rung_c2_c4_expansion` and `N2_factor_mul_quartic_rung`: product expansion of
     `(1 - u^2)(1 + c_4 u^4) = 1 - u^2 + c_4 u^4 - c_4 u^6`.
   * `habiroCyclotomicIdeal4_factor` and `habiroPochhammerNorm4_ratio_uFourth`: cyclotomic
     factorization of the 4th Habiro ideal `Φ_1 Φ_2 Φ_3 Φ_4` and rational ratio `u^4(q) / η_4(q)`
     (`= 1/1024` at `q = 1`).
   * `kashiwaraQuarticCoeff_eq_div`, `kashiwaraDividedCos4_eq_product_add_uSix`, and
     `kashiwaraQuarticCoeff_taylor_poly4_remainder`: exact `m = 2` divided-power Kashiwara crystal
     cosine coefficient `[2]_q / ([3]_q [4]_q)` (`→ +1/6` at `q = 1`).
   * `kdFullTwistChar_eq_chebyshev_hSq_cubic`: exact degree-3 Chebyshev polynomial representation of
     `C_KD^{(6)}(q) = (q^6 + q⁻⁶)/2` in `h^2 = (q - q⁻¹)^2` with zero `h^8` coefficient.

3. **Section 3 — Contribution B: Fourth Cumulant (Kurtosis `κ_4 = μ_4 - 3 μ_2^2`) of `H_3(q)` Wedderburn & GPMT+ Traces**:
   * `fourBlock_kurtosis_identity`: general 4-slot cumulant polynomial identity on normalized weights
     `(p_1, p_2, p_3, p_4)` matching the `1 + 2 + 1 = 4` seminormal basis dimensions of `H_3(q)`.
   * `wedderburnVarianceD_eq_div`, `wedderburnKurtosisD_eq_div`, and
     `wedderburnKurtosisD_taylor_poly8_remainder`: closed form and `ℏ_q^8` Taylor polynomial remainder
     of the Convention-D Jucys–Murphy content kurtosis (`κ_4^D(1) = -1/8`, excess kurtosis
     `γ_2^D(1) = -2 = jonesHopfClassicalLimit`), coincidence of the variance-matched cumulant rung
     `1/2 + γ_2^D(1)/6 = +1/6` with `kashiwaraQuarticCoeff 1`, and GPMT+ 3-block kurtosis at `q = 1`
     (`κ_4^{GPMT+}(1) = -516/2401`, rung `+101/288`).

4. **Section 4 — Contribution C: Connected Borromean QED `ℏ_q^4..ℏ_q^8` Series & `m_n` `1σ_exp` Envelope Bound**:
   * `trConnDiffPlain_taylor_poly8_remainder`: exact `ℏ_q^4..ℏ_q^8` rational Taylor expansion
     `(16/3) ℏ_q^4 + (32/3) ℏ_q^5 + (760/27) ℏ_q^6 + (520/9) ℏ_q^7 + 107 ℏ_q^8` of
     `trConnDiffPlain q = (q^2 - 1)^4 (4 q^4 + q^2 + 4) / (27 q^6)`.
   * `uFourth_strictly_inside_mn_sigma_envelope`: over `ℝ`, for `q₀ ∈ (110/100, 1111/1000)`,
     `u(q₀)^4 < 6 × 10⁻⁹` and `u(q₀)^5 < 5 × 10⁻¹¹`, bounding the `N ≥ 5` truncation remainder
     strictly below `10⁻⁴ σ_exp(m_n)` and `< 0.05 ppt` of `m_n` (with wide-window `< 10⁻⁸` bound
     on `(110/100, 112/100)` in `uFourth_lt_ten_neg8_on_wide_window`).

Compute companion: `computations/qbeta/qbeta_convention_d_c4_quartic_derivation_probe.py`
Witness: `computations/qbeta/qbeta-convention-d-c4-quartic-derivation.witness.json`
-/

namespace QOU.QBeta.ConventionDC4QuarticCumulantDerivation

open QOU.BraidKnot
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.QBeta.CoshHolonomyAndGPMTBaseBridge
open QOU.QBeta.WedderburnPhaseAndTwoTermPinBridge

/-! ## Section 1: Rationality of Even Habiro Rungs (`u^{2m}(q) ∈ ℚ(q)`) and `ℏ_q^8` Classical Leading Term -/

section EvenHabiroRungsRationality

variable {K : Type*} [Field K]

/-- Field-polymorphic quantum Planck parameter `ℏ_q = 1 - q⁻¹ = (q - 1)/q`. -/
def hbarQField (q : K) : K := 1 - q⁻¹

/-- Field-polymorphic squared Hoefsmit coupling `b(q)^2 = ((q - q⁻¹)^2 + 3) / ((q - q⁻¹)^2 + 4)`. -/
def hoefsmitBSqField (q : K) : K :=
  ((q - q⁻¹) ^ 2 + 3) / ((q - q⁻¹) ^ 2 + 4)

/-- Field-polymorphic quadratic Habiro ladder power `u(q)^2 = b(q)^2 · ℏ_q^4`. -/
def uSqField (q : K) : K :=
  hoefsmitBSqField q * hbarQField q ^ 4

/-- Field-polymorphic quartic Habiro ladder power `u(q)^4 = b(q)^4 · ℏ_q^8`. -/
def uFourthField (q : K) : K :=
  hoefsmitBSqField q ^ 2 * hbarQField q ^ 8

/-- Field-polymorphic `2m`-th even Habiro ladder power `u(q)^{2m} = b(q)^{2m} · ℏ_q^{4m}`. -/
def uEvenPowField (m : ℕ) (q : K) : K :=
  hoefsmitBSqField q ^ m * hbarQField q ^ (4 * m)

/-- Equivalence of `hoefsmitBSqField q` with `1 - w_{(2,1)}(z_D)` and with the cyclotomic rational
ratio `(q^4 + q^2 + 1) / (q^2 + 1)^2`. -/
theorem hoefsmitBSqField_eq_conventionD_complement (q : K) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    hoefsmitBSqField q = 1 - w21 q (zD q) ∧
      hoefsmitBSqField q = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  have hden : (q - q⁻¹) ^ 2 + 4 = (q ^ 2 + 1) ^ 2 / q ^ 2 := by
    field_simp
    ring
  have hrat : hoefsmitBSqField q = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
    unfold hoefsmitBSqField
    rw [hden]
    have hnum : (q - q⁻¹) ^ 2 + 3 = (q ^ 4 + q ^ 2 + 1) / q ^ 2 := by
      field_simp
      ring
    rw [hnum]
    field_simp
  refine ⟨?_, hrat⟩
  rw [hrat, w21_conventionD q hq2 hq4]
  field_simp
  ring

/-- Cyclotomic factorization of `uSqField q` over `[Field K]`:
`u(q)^2 = (q - 1)^4 (q^2 - q + 1)(q^2 + q + 1) / (q^4 (q^2 + 1)^2)`. -/
theorem uSqField_eq_div (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    uSqField q =
      (q - 1) ^ 4 * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) / (q ^ 4 * (q ^ 2 + 1) ^ 2) := by
  unfold uSqField hbarQField
  rw [(hoefsmitBSqField_eq_conventionD_complement q hq hq2 hq4).2]
  field_simp
  ring

/-- Cyclotomic factorization of `uFourthField q` over `[Field K]`:
`u(q)^4 = (q - 1)^8 (q^2 - q + 1)^2 (q^2 + q + 1)^2 / (q^8 (q^2 + 1)^4)`. -/
theorem uFourthField_eq_div (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    uFourthField q =
      (q - 1) ^ 8 * (q ^ 2 - q + 1) ^ 2 * (q ^ 2 + q + 1) ^ 2 /
        (q ^ 8 * (q ^ 2 + 1) ^ 4) := by
  have hu2 := uSqField_eq_div q hq hq2 hq4
  have hsq : uFourthField q = uSqField q ^ 2 := by
    unfold uFourthField uSqField
    ring
  rw [hsq, hu2, div_pow]
  ring

/-- Over `ℝ`, the squared ladder variable `(hoefsmitB q * hbarQ' q ^ 2) ^ 2` equals `1 - N2_factor q`
and coincides with the pure rational quotient
`(q - 1)^4 (q^2 - q + 1)(q^2 + q + 1) / (q^4 (q^2 + 1)^2)` for every `q ≠ 0`. -/
theorem uSq_rational_in_q (q : ℝ) (hq : q ≠ 0) :
    (hoefsmitB q * hbarQ' q ^ 2) ^ 2 =
      (q - 1) ^ 4 * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) / (q ^ 4 * (q ^ 2 + 1) ^ 2) ∧
    (hoefsmitB q * hbarQ' q ^ 2) ^ 2 = 1 - N2_factor q := by
  have hnn : (0 : ℝ) ≤ q ^ 4 + q ^ 2 + 1 := by positivity
  have hd : q ^ 2 + 1 ≠ 0 := by positivity
  constructor
  · unfold hoefsmitB hbarQ'
    rw [mul_pow, div_pow, Real.sq_sqrt hnn, ← pow_mul, div_pow]
    field_simp
    ring
  · unfold N2_factor
    ring

/-- Over `ℝ`, the fourth power `(hoefsmitB q * hbarQ' q ^ 2) ^ 4` of the Habiro ladder variable
is a pure rational function in `ℚ(q)` with zero square roots. -/
theorem uFourth_rational_in_q (q : ℝ) (hq : q ≠ 0) :
    (hoefsmitB q * hbarQ' q ^ 2) ^ 4 =
      (q - 1) ^ 8 * (q ^ 2 - q + 1) ^ 2 * (q ^ 2 + q + 1) ^ 2 /
        (q ^ 8 * (q ^ 2 + 1) ^ 4) := by
  have hpow : (hoefsmitB q * hbarQ' q ^ 2) ^ 4 = ((hoefsmitB q * hbarQ' q ^ 2) ^ 2) ^ 2 := by
    ring
  rw [hpow, (uSq_rational_in_q q hq).1, div_pow]
  ring

/-- Over `ℝ`, every even Habiro ladder power `(hoefsmitB q * hbarQ' q ^ 2) ^ (2 * m)` equals the
rational power `((q^4 + q^2 + 1) / (q^2 + 1)^2)^m · ((q - 1)/q)^{4m}` with classical leading
coefficient `(3/4)^m` at `q = 1`. -/
theorem uEvenPow_rational_in_q (m : ℕ) (q : ℝ) :
    (hoefsmitB q * hbarQ' q ^ 2) ^ (2 * m) =
      ((q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2) ^ m * ((q - 1) / q) ^ (4 * m) ∧
    (((1 : ℝ) ^ 4 + 1 ^ 2 + 1) / (1 ^ 2 + 1) ^ 2) ^ m = (3 / 4 : ℝ) ^ m := by
  have hnn : (0 : ℝ) ≤ q ^ 4 + q ^ 2 + 1 := by positivity
  constructor
  · rw [pow_mul]
    have hb2 : (hoefsmitB q * hbarQ' q ^ 2) ^ 2 =
        ((q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2) * ((q - 1) / q) ^ 4 := by
      unfold hoefsmitB hbarQ'
      rw [mul_pow, div_pow, Real.sq_sqrt hnn, ← pow_mul]
    rw [hb2, mul_pow, ← pow_mul]
  · norm_num

/-- Exact rational Taylor polynomial remainder of `uSqField q` through `ℏ_q^8` over `[Field K]`:
`u(q)^2 = (3/4) ℏ_q^4 + (1/4) ℏ_q^6 + (1/4) ℏ_q^7 + (1/16) ℏ_q^8 + O((q - 1)^9)`. -/
theorem uSq_taylor_poly8_remainder (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    uSqField q -
        ((3 / 4 : K) * hbarQField q ^ 4 + (1 / 4 : K) * hbarQField q ^ 6 +
          (1 / 4 : K) * hbarQField q ^ 7 + (1 / 16 : K) * hbarQField q ^ 8) =
      -(q - 1) ^ 9 * (5 * q ^ 3 + q ^ 2 + 3 * q - 1) / (16 * q ^ 8 * (q ^ 2 + 1) ^ 2) := by
  have h4 : (4 : K) = 2 * 2 := by ring
  have h16 : (16 : K) = 2 * 2 * 2 * 2 := by ring
  rw [uSqField_eq_div q hq hq2 hq4]
  unfold hbarQField
  rw [h4, h16]
  field_simp
  ring

/-- Classical leading term of `u(q)^4`: subtracting `(9/16) ℏ_q^8` leaves a strictly 10th-order
remainder `(q - 1)^{10} (q + 1)^2 (7 q^4 + 10 q^2 + 7) / (16 q^8 (q^2 + 1)^4)`, confirming both the
`9/16 = (3/4)^2` leading coefficient and the identical vanishing of the `ℏ_q^9` coefficient. -/
theorem uFourth_at_classical_leading (q : ℝ) (hq : q ≠ 0) :
    (hoefsmitB q * hbarQ' q ^ 2) ^ 4 - (9 / 16 : ℝ) * hbarQ' q ^ 8 =
      (q - 1) ^ 10 * (q + 1) ^ 2 * (7 * q ^ 4 + 10 * q ^ 2 + 7) /
        (16 * q ^ 8 * (q ^ 2 + 1) ^ 4) := by
  have hd : q ^ 2 + 1 ≠ 0 := by positivity
  rw [uFourth_rational_in_q q hq]
  unfold hbarQ'
  field_simp
  ring

/-- Exact rational Taylor polynomial remainder of `uFourthField q` through `ℏ_q^{10}` over `[Field K]`:
`u(q)^4 = (9/16) ℏ_q^8 + (3/8) ℏ_q^{10} + O((q - 1)^{11})`. -/
theorem uFourth_taylor_poly10_remainder (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    uFourthField q - ((9 / 16 : K) * hbarQField q ^ 8 + (3 / 8 : K) * hbarQField q ^ 10) =
      (q - 1) ^ 11 *
        (q ^ 7 + 15 * q ^ 6 + 8 * q ^ 5 + 28 * q ^ 4 + 9 * q ^ 3 + 23 * q ^ 2 + 6 * q + 6) /
        (16 * q ^ 10 * (q ^ 2 + 1) ^ 4) := by
  have h8 : (8 : K) = 2 * 2 * 2 := by ring
  have h16 : (16 : K) = 2 * 2 * 2 * 2 := by ring
  rw [uFourthField_eq_div q hq hq2 hq4]
  unfold hbarQField
  rw [h8, h16]
  field_simp
  ring

end EvenHabiroRungsRationality

/-! ## Section 2: Contribution A — Even-Rung Kashiwara Divided-Power, Habiro Cyclotomic Norm & Chebyshev Holonomy -/

section ContributionAKashiwaraHabiroChebyshev

/-- Product expansion of the `c_2 = -1` and `c_4` even ladder rungs over any commutative ring:
`(1 - u^2)(1 + c_4 u^4) = 1 - u^2 + c_4 u^4 - c_4 u^6`. -/
theorem even_product_rung_c2_c4_expansion {R : Type*} [CommRing R] (u c4 : R) :
    (1 - u ^ 2) * (1 + c4 * u ^ 4) = 1 - u ^ 2 + c4 * u ^ 4 - c4 * u ^ 6 := by
  ring

/-- Product expansion of `N2_factor q` from `QBetaCategoricalPrecisionLadder` with `(1 + c_4 u^4)`. -/
theorem N2_factor_mul_quartic_rung (q c4 : ℝ) :
    N2_factor q * (1 + c4 * (hoefsmitB q * hbarQ' q ^ 2) ^ 4) =
      1 - (hoefsmitB q * hbarQ' q ^ 2) ^ 2 + c4 * (hoefsmitB q * hbarQ' q ^ 2) ^ 4 -
        c4 * (hoefsmitB q * hbarQ' q ^ 2) ^ 6 := by
  unfold N2_factor
  ring

variable {K : Type*} [Field K]

/-- Cyclotomic polynomial product identity for the 4th Habiro cyclotomic ideal generator
`Φ_1(q) Φ_2(q) Φ_3(q) Φ_4(q) = (q - 1)(q + 1)(q^2 + q + 1)(q^2 + 1) = (q^4 - 1)(q^2 + q + 1)`. -/
theorem habiroCyclotomicIdeal4_factor (q : K) :
    (q - 1) * (q + 1) * (q ^ 2 + q + 1) * (q ^ 2 + 1) =
      (q ^ 4 - 1) * (q ^ 2 + q + 1) := by
  ring

/-- Four-step bar-even Habiro cyclotomic `q`-Pochhammer norm
`η_4(q) = ∏_{j=1}^4 (q^{j/2} - q^{-j/2})^2 = (q - 1)^2 (q^2 - 1)^2 (q^3 - 1)^2 (q^4 - 1)^2 / q^{10}`. -/
def habiroPochhammerNorm4 (q : K) : K :=
  (q - 1) ^ 2 * (q ^ 2 - 1) ^ 2 * (q ^ 3 - 1) ^ 2 * (q ^ 4 - 1) ^ 2 / q ^ 10

/-- Rational ratio between `uFourthField q` and `habiroPochhammerNorm4 q`: `uFourthField q` equals
`(1 - w_{(2,1)}(z_D))^2 · ℏ_q^8`, and in `uFourthField q / habiroPochhammerNorm4 q` the 8th-order
`(q - 1)^8` zero and `Φ_3(q)^2` factor cancel identically, leaving
`q^2 (q^2 - q + 1)^2 / ((q + 1)^4 (q^2 + 1)^6)` (`= 1 / 1024` at `q = 1`). -/
theorem habiroPochhammerNorm4_ratio_uFourth (q : K) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0)
    (hqp1 : q + 1 ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq3 : q ^ 2 + q + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    uFourthField q = (1 - w21 q (zD q)) ^ 2 * hbarQField q ^ 8 ∧
      uFourthField q / habiroPochhammerNorm4 q =
        q ^ 2 * (q ^ 2 - q + 1) ^ 2 / ((q + 1) ^ 4 * (q ^ 2 + 1) ^ 6) ∧
      ((1 : ℚ) ^ 2 * (1 ^ 2 - 1 + 1) ^ 2 / ((1 + 1) ^ 4 * (1 ^ 2 + 1) ^ 6)) = 1 / 1024 := by
  have hq3m1 : q ^ 3 - 1 ≠ 0 := by
    have hf : q ^ 3 - 1 = (q - 1) * (q ^ 2 + q + 1) := by ring
    rw [hf]
    exact mul_ne_zero hq1 hq3
  have hq2m1 : q ^ 2 - 1 ≠ 0 := by
    have hf : q ^ 2 - 1 = (q - 1) * (q + 1) := by ring
    rw [hf]
    exact mul_ne_zero hq1 hqp1
  have hq4m1 : q ^ 4 - 1 ≠ 0 := by
    have hf : q ^ 4 - 1 = (q ^ 2 - 1) * (q ^ 2 + 1) := by ring
    rw [hf]
    exact mul_ne_zero hq2m1 hq2
  refine ⟨?_, ?_, by norm_num⟩
  · unfold uFourthField
    rw [(hoefsmitBSqField_eq_conventionD_complement q hq hq2 hq4).1]
  · rw [uFourthField_eq_div q hq hq2 hq4]
    unfold habiroPochhammerNorm4
    field_simp
    ring

/-- Symmetric quantum integer `[4]_q = (q^4 - q⁻⁴) / (q - q⁻¹) = (q + q⁻¹)(q^2 + q⁻²)`. -/
def qInt4Sym (q : K) : K :=
  (q + q⁻¹) * (q ^ 2 + q⁻¹ ^ 2)

/-- Parameter-free Kashiwara `q`-divided-power cosine quartic coefficient
`c_4^{Kash,div}(q) = ([2]_q!)^2 / [4]_q! = [2]_q / ([3]_q [4]_q)` from
`∑_{m=0}^2 (-1)^m X^{2m} / [2m]_q!` normalized at `m = 1` by `X^2 = [2]_q! · u^2`. -/
def kashiwaraQuarticCoeff (q : K) : K :=
  (q + q⁻¹) / (QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.qInt3 q * qInt4Sym q)

/-- Cyclotomic rational closed form of `kashiwaraQuarticCoeff q`, `[2]_q`-cancelled `[3]_q` form,
and classical value `+1/6` at `q = 1`. -/
theorem kashiwaraQuarticCoeff_eq_div (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + 1 ≠ 0) (hq3 : QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.qInt3 q ≠ 0) :
    kashiwaraQuarticCoeff q =
      1 / (QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.qInt3 q * (q ^ 2 + q⁻¹ ^ 2)) ∧
    kashiwaraQuarticCoeff q =
      q ^ 4 / ((q ^ 4 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1)) ∧
    kashiwaraQuarticCoeff (1 : ℚ) = 1 / 6 := by
  have h2q : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  have h4q : q ^ 2 + q⁻¹ ^ 2 = (q ^ 4 + 1) / q ^ 2 := by field_simp
  have hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0 :=
    QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.q4_add_q2_add_one_ne_zero q hq hq3
  refine ⟨?_, ?_, ?_⟩
  · unfold kashiwaraQuarticCoeff qInt4Sym
    rw [h2q]
    field_simp
  · unfold kashiwaraQuarticCoeff qInt4Sym
    rw [QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.qInt3_eq_div q hq, h2q, h4q]
    have hmul : (q ^ 4 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) =
        (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) := by ring
    rw [hmul]
    field_simp
  · unfold kashiwaraQuarticCoeff qInt4Sym QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.qInt3
    norm_num

/-- Multiplicative factorization of the `m ≤ 2` Kashiwara `q`-divided-power cosine polynomial
at `u = hoefsmitB q * hbarQ' q ^ 2` into `N2_factor q * (1 + c_4^{Kash,div}(q) u^4)` plus `c_4^{Kash,div}(q) u^6`. -/
theorem kashiwaraDividedCos4_eq_product_add_uSix (q : ℝ) :
    1 - (hoefsmitB q * hbarQ' q ^ 2) ^ 2 +
        kashiwaraQuarticCoeff q * (hoefsmitB q * hbarQ' q ^ 2) ^ 4 =
      N2_factor q * (1 + kashiwaraQuarticCoeff q * (hoefsmitB q * hbarQ' q ^ 2) ^ 4) +
        kashiwaraQuarticCoeff q * (hoefsmitB q * hbarQ' q ^ 2) ^ 6 := by
  unfold N2_factor
  ring

/-- Rational Taylor polynomial remainder of `kashiwaraQuarticCoeff q` through `ℏ_q^4`:
`[2]_q / ([3]_q [4]_q) = 1/6 - (5/9) ℏ_q^2 - (5/9) ℏ_q^3 + (77/108) ℏ_q^4 + O((q - 1)^5)`. -/
theorem kashiwaraQuarticCoeff_taylor_poly4_remainder (q : K) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + 1 ≠ 0)
    (hq3 : QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.qInt3 q ≠ 0)
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    kashiwaraQuarticCoeff q -
        ((1 / 6 : K) - (5 / 9 : K) * hbarQField q ^ 2 - (5 / 9 : K) * hbarQField q ^ 3 +
          (77 / 108 : K) * hbarQField q ^ 4) =
      (q - 1) ^ 5 *
        (25 * q ^ 7 + 133 * q ^ 6 + 218 * q ^ 5 + 266 * q ^ 4 + 214 * q ^ 3 +
          214 * q ^ 2 + 137 * q + 77) /
        (108 * q ^ 4 * (q ^ 4 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1)) := by
  have h6 : (6 : K) = 2 * 3 := by ring
  have h9 : (9 : K) = 3 * 3 := by ring
  have h108 : (108 : K) = 2 * 2 * 3 * 3 * 3 := by ring
  have hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0 :=
    QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.q4_add_q2_add_one_ne_zero q hq hq3
  rw [(kashiwaraQuarticCoeff_eq_div q hq hq2 hq4 hq3).2.1]
  have hden : 108 * q ^ 4 * (q ^ 4 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) =
      108 * q ^ 4 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) := by ring
  have hden1 : (q ^ 4 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) =
      (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) := by ring
  rw [hden, hden1]
  generalize hD_eq : q ^ 4 + q ^ 2 + 1 = D at hq421 ⊢
  unfold hbarQField
  rw [h6, h9, h108]
  field_simp
  subst hD_eq
  ring

/-- Degree-3 Chebyshev polynomial representation of the 6-crossing full-twist hyperbolic holonomy
`kdFullTwistChar q = (q^6 + q⁻⁶) / 2` in `h^2 = (q - q⁻¹)^2`:
`C_KD^{(6)}(q) = 1 + (9/2) h^2 + 3 h^4 + (1/2) h^6`, carrying zero `h^8` quartic term. -/
theorem kdFullTwistChar_eq_chebyshev_hSq_cubic (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    kdFullTwistChar q =
      1 + (9 / 2 : K) * (q - q⁻¹) ^ 2 + 3 * (q - q⁻¹) ^ 4 + (1 / 2 : K) * (q - q⁻¹) ^ 6 := by
  unfold kdFullTwistChar
  field_simp
  ring

end ContributionAKashiwaraHabiroChebyshev

/-! ## Section 3: Contribution B — 4th Cumulant (Kurtosis `κ_4`) of `H_3(q)` Multi-Block Wedderburn & GPMT+ Traces -/

section ContributionBWedderburnKurtosis

/-- General 4-slot fourth cumulant (`κ_4 = μ_4 - 3 μ_2^2`) identity over any commutative ring:
for normalized weights `p1 + p2 + p3 + p4 = 1` (corresponding on `H_3(q)` to the `1 + 2 + 1 = 4`
seminormal basis slots) and eigenvalues `(x1, x2, x3, x4)`, the central fourth cumulant equals
`m_4 - 4 m_3 m_1 + 12 m_2 m_1^2 - 3 m_2^2 - 6 m_1^4` in the raw moments `m_r = ∑_i p_i x_i^r`. -/
theorem fourBlock_kurtosis_identity {R : Type*} [CommRing R]
    (p1 p2 p3 p4 x1 x2 x3 x4 : R) (hp : p1 + p2 + p3 + p4 = 1) :
    let m1 := p1 * x1 + p2 * x2 + p3 * x3 + p4 * x4
    let m2 := p1 * x1 ^ 2 + p2 * x2 ^ 2 + p3 * x3 ^ 2 + p4 * x4 ^ 2
    let m3 := p1 * x1 ^ 3 + p2 * x2 ^ 3 + p3 * x3 ^ 3 + p4 * x4 ^ 3
    let m4 := p1 * x1 ^ 4 + p2 * x2 ^ 4 + p3 * x3 ^ 4 + p4 * x4 ^ 4
    let mu2 := p1 * (x1 - m1) ^ 2 + p2 * (x2 - m1) ^ 2 + p3 * (x3 - m1) ^ 2 + p4 * (x4 - m1) ^ 2
    let mu4 := p1 * (x1 - m1) ^ 4 + p2 * (x2 - m1) ^ 4 + p3 * (x3 - m1) ^ 4 + p4 * (x4 - m1) ^ 4
    mu4 - 3 * mu2 ^ 2 = m4 - 4 * m3 * m1 + 12 * m2 * m1 ^ 2 - 3 * m2 ^ 2 - 6 * m1 ^ 4 := by
  dsimp only
  have hp4 : p4 = 1 - p1 - p2 - p3 := by linear_combination hp
  rw [hp4]
  ring

variable {K : Type*} [Field K]

/-- Convention-D second central moment (variance `κ_2^D = μ_2^D`) of the per-strand normalized
Jucys–Murphy / transposition content spectrum `(+1, 0, -1)` under `(w_{(3)}(z_D), 2 w_{(2,1)}(z_D), 0)`. -/
def wedderburnVarianceD (q : K) : K :=
  w3 q (zD q) * (1 - jmContentMeanD q) ^ 2 +
    (2 * w21 q (zD q)) * (0 - jmContentMeanD q) ^ 2 +
    w111 q (zD q) * (-1 - jmContentMeanD q) ^ 2

/-- Convention-D fourth central moment `μ_4^D` of the per-strand normalized Jucys–Murphy content
spectrum `(+1, 0, -1)`. -/
def wedderburnFourthCentralD (q : K) : K :=
  w3 q (zD q) * (1 - jmContentMeanD q) ^ 4 +
    (2 * w21 q (zD q)) * (0 - jmContentMeanD q) ^ 4 +
    w111 q (zD q) * (-1 - jmContentMeanD q) ^ 4

/-- Convention-D fourth cumulant (kurtosis `κ_4^D = μ_4^D - 3 (μ_2^D)^2`) of the `H_3(q)` Wedderburn
block distribution on `(+1, 0, -1)`. -/
def wedderburnKurtosisD (q : K) : K :=
  wedderburnFourthCentralD q - 3 * wedderburnVarianceD q ^ 2

/-- Variance-matched Convention-D block-phase cumulant quartic rung coefficient
`c_4^{cum,D}(q) = 1/2 + κ_4^D(q) / (6 (κ_2^D(q))^2)` from `Re log E[e^{i Φ}] = -u^2 + (κ_4/(6 κ_2^2)) u^4`
factored against `(1 - u^2)(1 + c_4 u^4)`. -/
def wedderburnCumulantRungC4D (q : K) : K :=
  1 / 2 + wedderburnKurtosisD q / (6 * wedderburnVarianceD q ^ 2)

/-- Bernoulli product identity and rational closed form of `wedderburnVarianceD q`:
`κ_2^D(q) = 2 w_{(3)}(z_D) w_{(2,1)}(z_D) = 2 q^2 (q^4 + 1) / (q^2 + 1)^4` (`= 1/4` at `q = 1`). -/
theorem wedderburnVarianceD_eq_div (q : K) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    wedderburnVarianceD q = 2 * w3 q (zD q) * w21 q (zD q) ∧
      wedderburnVarianceD q = 2 * q ^ 2 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 4 := by
  have hm := (jmContentMeanD_eq_transpositionMomentD q hq2 hq4).1
  have ht := (jmContentMeanD_eq_transpositionMomentD q hq2 hq4).2
  have hclosed : wedderburnVarianceD q = 2 * q ^ 2 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 4 := by
    unfold wedderburnVarianceD
    rw [hm, ht, w3_conventionD q hq2 hq4, w21_conventionD q hq2 hq4, w111_conventionD q hq2]
    field_simp
    ring
  refine ⟨?_, hclosed⟩
  rw [hclosed, w3_conventionD q hq2 hq4, w21_conventionD q hq2 hq4]
  field_simp

/-- Rational closed form of `wedderburnKurtosisD q` and its classical value `κ_4^D(1) = -1/8`
(standardized excess kurtosis `κ_4^D(1) / (κ_2^D(1))^2 = -2 = jonesHopfClassicalLimit`). -/
theorem wedderburnKurtosisD_eq_div (q : K) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    wedderburnKurtosisD q =
      2 * q ^ 2 * (q ^ 4 + 1) * (q ^ 8 - 8 * q ^ 6 + 6 * q ^ 4 - 8 * q ^ 2 + 1) /
        (q ^ 2 + 1) ^ 8 ∧
    wedderburnKurtosisD (1 : ℝ) / wedderburnVarianceD (1 : ℝ) ^ 2 =
      jonesHopfClassicalLimit := by
  constructor
  · have hm := (jmContentMeanD_eq_transpositionMomentD q hq2 hq4).1
    have ht := (jmContentMeanD_eq_transpositionMomentD q hq2 hq4).2
    unfold wedderburnKurtosisD wedderburnFourthCentralD
    rw [(wedderburnVarianceD_eq_div q hq2 hq4).2, hm, ht, w3_conventionD q hq2 hq4,
        w21_conventionD q hq2 hq4, w111_conventionD q hq2]
    field_simp
    ring
  · unfold wedderburnKurtosisD wedderburnFourthCentralD wedderburnVarianceD
      jmContentMeanD w3 w21 w111 zD jonesHopfClassicalLimit
    norm_num

/-- Bernoulli kurtosis product form `2 w_{(3)}(z_D) w_{(2,1)}(z_D) (1 - 12 w_{(3)}(z_D) w_{(2,1)}(z_D))`
and exact rational Taylor polynomial remainder of `wedderburnKurtosisD q` through `ℏ_q^8`:
`κ_4^D(q) = -1/8 + (1/2) ℏ_q^4 + ℏ_q^5 + (3/4) ℏ_q^6 - (1/4) ℏ_q^7 - (51/32) ℏ_q^8 + O((q - 1)^9)`. -/
theorem wedderburnKurtosisD_taylor_poly8_remainder (q : K) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    wedderburnKurtosisD q =
      2 * w3 q (zD q) * w21 q (zD q) * (1 - 12 * w3 q (zD q) * w21 q (zD q)) ∧
    wedderburnKurtosisD q -
        (-(1 / 8 : K) + (1 / 2 : K) * hbarQField q ^ 4 + hbarQField q ^ 5 +
          (3 / 4 : K) * hbarQField q ^ 6 - (1 / 4 : K) * hbarQField q ^ 7 -
          (51 / 32 : K) * hbarQField q ^ 8) =
      -(q - 1) ^ 9 *
        (9 * q ^ 15 + 177 * q ^ 14 + 457 * q ^ 13 + 1537 * q ^ 12 + 2005 * q ^ 11 +
          3645 * q ^ 10 + 2821 * q ^ 9 + 4157 * q ^ 8 + 2183 * q ^ 7 + 3103 * q ^ 6 +
          1111 * q ^ 5 + 1503 * q ^ 4 + 331 * q ^ 3 + 419 * q ^ 2 + 43 * q + 51) /
        (32 * q ^ 8 * (q ^ 2 + 1) ^ 8) := by
  have h4 : (4 : K) = 2 * 2 := by ring
  have h8 : (8 : K) = 2 * 2 * 2 := by ring
  have h32 : (32 : K) = 2 * 2 * 2 * 2 * 2 := by ring
  constructor
  · rw [(wedderburnKurtosisD_eq_div q hq2 hq4).1, w3_conventionD q hq2 hq4, w21_conventionD q hq2 hq4]
    field_simp
    ring
  · rw [(wedderburnKurtosisD_eq_div q hq2 hq4).1]
    unfold hbarQField
    rw [h4, h8, h32]
    field_simp
    ring

/-- Wedderburn weight reciprocal form `1 / (12 w_{(3)}(z_D) w_{(2,1)}(z_D)) - 1 / 2`, rational
closed form, `ℏ_q^4` Taylor expansion, and classical coincidence
`wedderburnCumulantRungC4D 1 = kashiwaraQuarticCoeff 1 = 1 / 6`. -/
theorem wedderburnCumulantRungC4D_eq_div (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq41 : q ^ 4 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0)
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    wedderburnCumulantRungC4D q = 1 / (12 * w3 q (zD q) * w21 q (zD q)) - 1 / 2 ∧
    wedderburnCumulantRungC4D q =
      (q ^ 8 - 2 * q ^ 6 + 6 * q ^ 4 - 2 * q ^ 2 + 1) / (12 * q ^ 2 * (q ^ 4 + 1)) ∧
    wedderburnCumulantRungC4D q - ((1 / 6 : K) + (2 / 3 : K) * hbarQField q ^ 4) =
      (q - 1) ^ 5 * (q ^ 5 + 5 * q ^ 4 + 3 * q ^ 3 + 7 * q ^ 2 + 8 * q + 8) /
        (12 * q ^ 4 * (q ^ 4 + 1)) ∧
    wedderburnCumulantRungC4D (1 : ℚ) = kashiwaraQuarticCoeff (1 : ℚ) := by
  have h6 : (6 : K) = 2 * 3 := by ring
  have h12 : (12 : K) = 2 * 2 * 3 := by ring
  have hvar := (wedderburnVarianceD_eq_div q hq2 hq4).2
  have hkurt := (wedderburnKurtosisD_eq_div q hq2 hq4).1
  have hvar_ne : wedderburnVarianceD q ≠ 0 := by
    rw [hvar]
    exact div_ne_zero (mul_ne_zero (mul_ne_zero h2 (pow_ne_zero 2 hq)) hq41) (pow_ne_zero 4 hq2)
  have hclosed : wedderburnCumulantRungC4D q =
      (q ^ 8 - 2 * q ^ 6 + 6 * q ^ 4 - 2 * q ^ 2 + 1) / (12 * q ^ 2 * (q ^ 4 + 1)) := by
    unfold wedderburnCumulantRungC4D
    have hv_nz : wedderburnVarianceD q ^ 2 ≠ 0 := pow_ne_zero 2 hvar_ne
    rw [hkurt, hvar]
    rw [h6, h12]
    field_simp
    ring
  refine ⟨?_, hclosed, ?_, ?_⟩
  · rw [hclosed, w3_conventionD q hq2 hq4, w21_conventionD q hq2 hq4]
    rw [h12]
    field_simp
    ring
  · rw [hclosed]
    unfold hbarQField
    rw [h6, h12]
    field_simp
    ring
  · unfold wedderburnCumulantRungC4D wedderburnKurtosisD wedderburnFourthCentralD
      wedderburnVarianceD jmContentMeanD w3 w21 w111 zD
      kashiwaraQuarticCoeff qInt4Sym QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.qInt3
    norm_num

/-- Normalized 3-block GPMT+ Jucys–Murphy content mean, variance, fourth cumulant, and
variance-matched quartic cumulant rung at the classical point `q = 1`:
restoring the killed `(1^3)` sector with `|d_D(S^{(1^3)})|_{q=1} = 1/6` yields normalized weights
`(3/7, 3/7, 1/7)`, mean `2/7`, variance `24/49`, fourth cumulant `-516/2401`, and cumulant rung `+101/288`. -/
theorem gpmtPosKurtosis_at_one :
    let zTot : ℚ := 1 + dMod111Abs 1
    let p3 : ℚ := w3 1 (zD 1) / zTot
    let p21 : ℚ := 2 * w21 1 (zD 1) / zTot
    let p111 : ℚ := dMod111Abs 1 / zTot
    let m1 : ℚ := p3 * 1 + p21 * 0 + p111 * (-1)
    let mu2 : ℚ := p3 * (1 - m1) ^ 2 + p21 * (0 - m1) ^ 2 + p111 * (-1 - m1) ^ 2
    let mu4 : ℚ := p3 * (1 - m1) ^ 4 + p21 * (0 - m1) ^ 4 + p111 * (-1 - m1) ^ 4
    let kappa4 : ℚ := mu4 - 3 * mu2 ^ 2
    m1 = 2 / 7 ∧ mu2 = 24 / 49 ∧ kappa4 = -516 / 2401 ∧
      (1 / 2 + kappa4 / (6 * mu2 ^ 2)) = 101 / 288 := by
  dsimp only
  unfold dMod111Abs dMod111 w3 w21 zD
  norm_num

end ContributionBWedderburnKurtosis

/-! ## Section 4: Contribution C — Connected Borromean QED `ℏ_q^4..ℏ_q^8` Expansion & `m_n` `1σ_exp` Envelope -/

section ContributionCBorromeanQEDAndEnvelope

variable {K : Type*} [Field K]

/-- Exact rational Taylor polynomial remainder of the connected 4th-order Borromean `V^3` `(n - p)`
electromagnetic trace difference `trConnDiffPlain q = (q^2 - 1)^4 (4 q^4 + q^2 + 4) / (27 q^6)`
through `ℏ_q^8`:
`Δtr_conn^{plain}(V^3) = (16/3) ℏ_q^4 + (32/3) ℏ_q^5 + (760/27) ℏ_q^6 + (520/9) ℏ_q^7 + 107 ℏ_q^8 + O((q - 1)^9)`. -/
theorem trConnDiffPlain_taylor_poly8_remainder (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnDiffPlain q -
        ((16 / 3 : K) * hbarQField q ^ 4 + (32 / 3 : K) * hbarQField q ^ 5 +
          (760 / 27 : K) * hbarQField q ^ 6 + (520 / 9 : K) * hbarQField q ^ 7 +
          107 * hbarQField q ^ 8) =
      (q - 1) ^ 9 *
        (4 * q ^ 5 + 36 * q ^ 4 + 165 * q ^ 3 + 525 * q ^ 2 + 1329 * q + 2889) /
        (27 * q ^ 8) := by
  have h9 : (9 : K) = 3 * 3 := by ring
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  rw [trConnDiffPlain_eq_div q hq h3]
  unfold hbarQField
  rw [h9, h27]
  field_simp
  ring

/-- Upper bound `0 < hoefsmitB q ∧ hoefsmitB q < 87 / 100` for all real `q ∈ (1, 112 / 100)`. -/
theorem hoefsmitB_lt_87_div_100 {q : ℝ} (hq1 : 1 < q) (hq2 : q < 112 / 100) :
    0 < hoefsmitB q ∧ hoefsmitB q < 87 / 100 := by
  have hq_pos : 0 < q := lt_trans zero_lt_one hq1
  have hrad_pos : 0 < q ^ 4 + q ^ 2 + 1 := by positivity
  have hden_pos : 0 < q ^ 2 + 1 := by positivity
  constructor
  · unfold hoefsmitB
    positivity
  · unfold hoefsmitB
    rw [div_lt_iff₀ hden_pos]
    have hrhs_pos : 0 < (87 / 100 : ℝ) * (q ^ 2 + 1) := by positivity
    have hsq_lt : q ^ 4 + q ^ 2 + 1 < ((87 / 100 : ℝ) * (q ^ 2 + 1)) ^ 2 := by
      have hx1 : 1 < q ^ 2 := by nlinarith
      have hx2 : q ^ 2 < 784 / 625 := by nlinarith
      have hprod : 0 < (q ^ 2 - 1) * (784 / 625 - q ^ 2) :=
        mul_pos (sub_pos.mpr hx1) (sub_pos.mpr hx2)
      nlinarith
    have hsqrt_sq : (Real.sqrt (q ^ 4 + q ^ 2 + 1)) ^ 2 <
        ((87 / 100 : ℝ) * (q ^ 2 + 1)) ^ 2 := by
      rwa [Real.sq_sqrt hrad_pos.le]
    nlinarith [Real.sqrt_nonneg (q ^ 4 + q ^ 2 + 1)]

/-- Monotonicity bound `0 < hbarQ' q ∧ hbarQ' q < (qHi - 1) / qHi` for `1 < q < qHi`. -/
theorem hbarQ_pos_and_lt {q qHi : ℝ} (hq1 : 1 < q) (hq2 : q < qHi) :
    0 < hbarQ' q ∧ hbarQ' q < (qHi - 1) / qHi := by
  have hq_pos : 0 < q := lt_trans zero_lt_one hq1
  have hqHi_pos : 0 < qHi := lt_trans hq_pos hq2
  unfold hbarQ'
  constructor
  · exact div_pos (sub_pos.mpr hq1) hq_pos
  · rw [div_lt_div_iff₀ hq_pos hqHi_pos]
    linarith

/-- Wide-window bound on `(110 / 100, 112 / 100)`: `u(q)^4 < 10⁻⁸` and `u(q)^5 < 10⁻¹⁰`, paired
with the right-endpoint check `u(112 / 100)^4 > 9 × 10⁻⁹` showing why `< 6 × 10⁻⁹` requires the
tighter physical proton/muon/two-term window `(110 / 100, 1111 / 1000)`. -/
theorem uFourth_lt_ten_neg8_on_wide_window {q : ℝ}
    (hq_lo : 110 / 100 < q) (hq_hi : q < 112 / 100) :
    (hoefsmitB q * hbarQ' q ^ 2) ^ 4 < (10 : ℝ)⁻¹ ^ 8 ∧
      (hoefsmitB q * hbarQ' q ^ 2) ^ 5 < (10 : ℝ)⁻¹ ^ 10 ∧
      9 * (10 : ℝ)⁻¹ ^ 9 < (hoefsmitB (112 / 100) * hbarQ' (112 / 100) ^ 2) ^ 4 := by
  have hq1 : 1 < q := by linarith
  obtain ⟨hb0, hb_ub⟩ := hoefsmitB_lt_87_div_100 hq1 hq_hi
  obtain ⟨ht0, ht_ub⟩ := hbarQ_pos_and_lt hq1 hq_hi
  have ht_ub' : hbarQ' q < 3 / 28 := by
    calc hbarQ' q < (112 / 100 - 1) / (112 / 100) := ht_ub
      _ = 3 / 28 := by norm_num
  have hu0 : 0 < hoefsmitB q * hbarQ' q ^ 2 := by positivity
  have hu_ub : hoefsmitB q * hbarQ' q ^ 2 < (87 / 100 : ℝ) * (3 / 28) ^ 2 := by
    have ht2 : hbarQ' q ^ 2 < (3 / 28 : ℝ) ^ 2 := sq_lt_sq' (by linarith) ht_ub'
    calc hoefsmitB q * hbarQ' q ^ 2
        < (87 / 100 : ℝ) * hbarQ' q ^ 2 := mul_lt_mul_of_pos_right hb_ub (sq_pos_of_pos ht0)
      _ < (87 / 100 : ℝ) * (3 / 28) ^ 2 := mul_lt_mul_of_pos_left ht2 (by norm_num)
  refine ⟨?_, ?_, ?_⟩
  · calc (hoefsmitB q * hbarQ' q ^ 2) ^ 4
        < ((87 / 100 : ℝ) * (3 / 28) ^ 2) ^ 4 := pow_lt_pow_left₀ hu_ub hu0.le (by norm_num)
      _ < (10 : ℝ)⁻¹ ^ 8 := by norm_num
  · calc (hoefsmitB q * hbarQ' q ^ 2) ^ 5
        < ((87 / 100 : ℝ) * (3 / 28) ^ 2) ^ 5 := pow_lt_pow_left₀ hu_ub hu0.le (by norm_num)
      _ < (10 : ℝ)⁻¹ ^ 10 := by norm_num
  · rw [uFourth_rational_in_q (112 / 100) (by norm_num)]
    norm_num

/-- **Physical Substrate Envelope Bound (`q₀ ∈ (110 / 100, 1111 / 1000)`)**:
For every substrate parameter `q₀ ∈ (110 / 100, 1111 / 1000)` (enclosing `q_{1t}`, `q_{2t}`, and
`q_μ ≈ 1.10997859`) and every `Q_β ≤ 4/5` MeV, `σ_exp(m_n) ≥ 4.8 × 10⁻⁷` MeV (`0.48 eV`),
and `m_n ≥ 939` MeV:
1. `u(q₀)^4 < 6 × 10⁻⁹`,
2. `u(q₀)^5 < 5 × 10⁻¹¹`,
3. `Q_β · u(q₀)^5 < 10⁻⁴ · σ_exp(m_n)` (strictly `< 10⁻⁴ σ_exp(m_n)`),
4. `(Q_β · u(q₀)^5) / m_n < 5 × 10⁻¹⁴` (`< 0.05 ppt` of `m_n`). -/
theorem uFourth_strictly_inside_mn_sigma_envelope {q0 qBeta sigmaMn mN : ℝ}
    (hq_lo : 110 / 100 < q0) (hq_hi : q0 < 1111 / 1000)
    (hqBeta_ub : qBeta ≤ 4 / 5)
    (hsigma_lb : 48 * (10 : ℝ)⁻¹ ^ 8 ≤ sigmaMn)
    (hmN_lb : 939 ≤ mN) :
    (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 4 < 6 * (10 : ℝ)⁻¹ ^ 9 ∧
      (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5 < 5 * (10 : ℝ)⁻¹ ^ 11 ∧
      qBeta * (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5 < (10 : ℝ)⁻¹ ^ 4 * sigmaMn ∧
      qBeta * (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5 / mN < 5 * (10 : ℝ)⁻¹ ^ 14 := by
  have hq1 : 1 < q0 := by linarith
  have hq112 : q0 < 112 / 100 := by linarith
  obtain ⟨hb0, hb_ub⟩ := hoefsmitB_lt_87_div_100 hq1 hq112
  obtain ⟨ht0, ht_ub⟩ := hbarQ_pos_and_lt hq1 hq_hi
  have ht_ub' : hbarQ' q0 < 111 / 1111 := by
    calc hbarQ' q0 < (1111 / 1000 - 1) / (1111 / 1000) := ht_ub
      _ = 111 / 1111 := by norm_num
  have hu0 : 0 < hoefsmitB q0 * hbarQ' q0 ^ 2 := by positivity
  have hu_ub : hoefsmitB q0 * hbarQ' q0 ^ 2 < (87 / 100 : ℝ) * (111 / 1111) ^ 2 := by
    have ht2 : hbarQ' q0 ^ 2 < (111 / 1111 : ℝ) ^ 2 := sq_lt_sq' (by linarith) ht_ub'
    calc hoefsmitB q0 * hbarQ' q0 ^ 2
        < (87 / 100 : ℝ) * hbarQ' q0 ^ 2 := mul_lt_mul_of_pos_right hb_ub (sq_pos_of_pos ht0)
      _ < (87 / 100 : ℝ) * (111 / 1111) ^ 2 := mul_lt_mul_of_pos_left ht2 (by norm_num)
  have hu4 : (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 4 < 6 * (10 : ℝ)⁻¹ ^ 9 := by
    calc (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 4
        < ((87 / 100 : ℝ) * (111 / 1111) ^ 2) ^ 4 := pow_lt_pow_left₀ hu_ub hu0.le (by norm_num)
      _ < 6 * (10 : ℝ)⁻¹ ^ 9 := by norm_num
  have hu5 : (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5 < 5 * (10 : ℝ)⁻¹ ^ 11 := by
    calc (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5
        < ((87 / 100 : ℝ) * (111 / 1111) ^ 2) ^ 5 := pow_lt_pow_left₀ hu_ub hu0.le (by norm_num)
      _ < 5 * (10 : ℝ)⁻¹ ^ 11 := by norm_num
  have hu5_pos : 0 < (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5 := pow_pos hu0 5
  have hqbu5 : qBeta * (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5 < 4 * (10 : ℝ)⁻¹ ^ 11 := by
    calc qBeta * (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5
        ≤ (4 / 5 : ℝ) * (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5 :=
          mul_le_mul_of_nonneg_right hqBeta_ub hu5_pos.le
      _ < (4 / 5 : ℝ) * (5 * (10 : ℝ)⁻¹ ^ 11) :=
          mul_lt_mul_of_pos_left hu5 (by norm_num)
      _ = 4 * (10 : ℝ)⁻¹ ^ 11 := by norm_num
  refine ⟨hu4, hu5, ?_, ?_⟩
  · calc qBeta * (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5
        < 4 * (10 : ℝ)⁻¹ ^ 11 := hqbu5
      _ < (10 : ℝ)⁻¹ ^ 4 * (48 * (10 : ℝ)⁻¹ ^ 8) := by norm_num
      _ ≤ (10 : ℝ)⁻¹ ^ 4 * sigmaMn :=
          mul_le_mul_of_nonneg_left hsigma_lb (by positivity)
  · have hmN_pos : 0 < mN := by linarith
    rw [div_lt_iff₀ hmN_pos]
    calc qBeta * (hoefsmitB q0 * hbarQ' q0 ^ 2) ^ 5
        < 4 * (10 : ℝ)⁻¹ ^ 11 := hqbu5
      _ < 5 * (10 : ℝ)⁻¹ ^ 14 * 939 := by norm_num
      _ ≤ 5 * (10 : ℝ)⁻¹ ^ 14 * mN :=
          mul_le_mul_of_nonneg_left hmN_lb (by positivity)

end ContributionCBorromeanQEDAndEnvelope

end QOU.QBeta.ConventionDC4QuarticCumulantDerivation
