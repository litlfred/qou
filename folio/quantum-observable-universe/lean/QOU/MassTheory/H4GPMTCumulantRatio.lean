import QOU.MassTheory.H4GPMTModifiedDimensionCumulants

/-!
# Closed-Form Ratio `|μ₄ / μ₃|` for `H_4(q)` GPMT Cumulants (`qou-sbn9`)

Completes the final ratio clause of bean `qou-sbn9` on top of
`QOU.MassTheory.H4GPMTModifiedDimensionCumulants` and exposes exact naming aliases
for the theorem identifiers cited by `computations/two_term_qed_isotope_and_nucleon_compute.py`.

## Main Results

1. **Exact Rational Closed Form of `μ₄^{\mathrm{GPMT}, H_4}(q) / μ₃^{\mathrm{GPMT}, H_4}(q)`
   (`mu4GPMT_H4_div_mu3GPMT_H4`):**
   Over any field `R` with `q ≠ 0`, `q² + 1 ≠ 0`, `q⁴ + 1 ≠ 0`, and `q⁴ + q² + 1 ≠ 0`,
   the common factor `q³ / ((q² + 1)(q⁴ + q² + 1))` in `μ₄^{\mathrm{GPMT}, H_4}(q)` and
   `μ₃^{\mathrm{GPMT}, H_4}(q) = -d_D(S^{(1^3)})` cancels identically, giving:
   `mu4GPMT_H4 q / mu3GPMT_H4 q = -(q^8 + 2 q^6 - 2 q^4 + 2 q^2 + 1) / ((q^2 + 1)^2 (q^4 + 1))`.

2. **Strict Magnitude Ratio `|μ₄ / μ₃|` for `q > 0` (`abs_mu4GPMT_H4_div_mu3GPMT_H4`):**
   Over any strict linearly ordered field `R` and any `q > 0`,
   `|mu4GPMT_H4 q / mu3GPMT_H4 q| = (q^8 + 2 q^6 - 2 q^4 + 2 q^2 + 1) / ((q^2 + 1)^2 (q^4 + 1)) > 0`.

-- Ref: [leitner2026] bean qou-sbn9; QOU.MassTheory.H4GPMTModifiedDimensionCumulants
-/

namespace QOU.MassTheory
namespace H4GPMTCumulantRatio

open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace (dMod111)
open QOU.MassTheory.GPMTThreeRowCumulantBridge
open QOU.MassTheory.H4GPMTModifiedDimensionCumulants

section RatioClosedForm

variable {R : Type*} [Field R]

/-- **Exact Closed Form of `μ₄^{\mathrm{GPMT}, H_4}(q) / μ₃^{\mathrm{GPMT}, H_4}(q)` (`qou-sbn9`):**
Cancelling `-dMod111 q = q^3 / ((q^2 + 1)(q^4 + q^2 + 1))` from `mu4GPMT_H4 q` yields
`-(q^8 + 2 q^6 - 2 q^4 + 2 q^2 + 1) / ((q^2 + 1)^2 (q^4 + 1))`. -/
theorem mu4GPMT_H4_div_mu3GPMT_H4 (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq41 : q ^ 4 + 1 ≠ 0) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    mu4GPMT_H4 q / mu3GPMT_H4 q =
      -(q ^ 8 + 2 * q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 + 1) / ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1)) := by
  rcases mu2_mu3_H4_eq_bridge q with ⟨_, hmu3, _⟩
  rw [mu4GPMT_H4_closed_form q hq2 hq41 hq421, hmu3]
  unfold dMod111
  have hden4 : (q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) ≠ 0 :=
    mul_ne_zero (mul_ne_zero (pow_ne_zero 3 hq2) hq41) hq421
  have hden3 : (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) ≠ 0 := mul_ne_zero hq2 hq421
  have hq3 : q ^ 3 ≠ 0 := pow_ne_zero 3 hq
  have hmu3_ne : -(-q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))) ≠ 0 :=
    neg_ne_zero.mpr (div_ne_zero (neg_ne_zero.mpr hq3) hden3)
  have hsub : (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) ≠ 0 := mul_ne_zero (pow_ne_zero 2 hq2) hq41
  rw [div_eq_div_iff hmu3_ne hsub]
  field_simp [hden4, hden3]

/-- Alias matching the producer source reference
`dMod211_eq_neg_qInt3_div_qInt2_sq_mul_qInt4` in `two_term_qed_isotope_and_nucleon_compute.py`. -/
theorem dMod211_eq_neg_qInt3_div_qInt2_sq_mul_qInt4
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) :
    dMod211 q = -qInt3 q / (qInt2 q ^ 2 * qInt4 q) :=
  dMod211_eq_neg_qInt3_div q hq hq2 hq41

/-- Alias matching the producer source reference
`dMod1111_eq_inv_qInt2_sq_mul_qInt3_mul_qInt4` in `two_term_qed_isotope_and_nucleon_compute.py`. -/
theorem dMod1111_eq_inv_qInt2_sq_mul_qInt3_mul_qInt4
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) :
    dMod1111 q = 1 / (qInt2 q ^ 2 * qInt3 q * qInt4 q) :=
  dMod1111_eq_inv_qInts q hq hq2 hq41

end RatioClosedForm

section OrderedMagnitudeRatio

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Strict Positivity and Closed Form of `|μ₄^{\mathrm{GPMT}, H_4}(q) / μ₃^{\mathrm{GPMT}, H_4}(q)|` (`qou-sbn9`):**
For every `q > 0`,
`|mu4GPMT_H4 q / mu3GPMT_H4 q| = (q^8 + 2 q^6 - 2 q^4 + 2 q^2 + 1) / ((q^2 + 1)^2 (q^4 + 1)) > 0`. -/
theorem abs_mu4GPMT_H4_div_mu3GPMT_H4 (q : R) (hq : 0 < q) :
    |mu4GPMT_H4 q / mu3GPMT_H4 q| =
      (q ^ 8 + 2 * q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 + 1) / ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1)) ∧
    0 < |mu4GPMT_H4 q / mu3GPMT_H4 q| := by
  have hq_ne : q ≠ 0 := ne_of_gt hq
  have hq2_pos : 0 < q ^ 2 + 1 := sq_add_one_pos q
  have hq41_pos : 0 < q ^ 4 + 1 := pow_four_add_one_pos q
  have hq421_pos : 0 < q ^ 4 + q ^ 2 + 1 := pow_four_add_sq_add_one_pos q
  have hrat_pos :
      0 < (q ^ 8 + 2 * q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 + 1) / ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1)) :=
    div_pos (octic_numerator_pos_of_pos q hq) (mul_pos (pow_pos hq2_pos 2) hq41_pos)
  have hdiv := mu4GPMT_H4_div_mu3GPMT_H4 q hq_ne (ne_of_gt hq2_pos) (ne_of_gt hq41_pos)
    (ne_of_gt hq421_pos)
  rw [hdiv, neg_div, abs_neg, abs_of_pos hrat_pos]
  exact ⟨rfl, hrat_pos⟩

/-- Alias matching `mu4GPMT_H4_lt_zero` in `two_term_qed_isotope_and_nucleon_compute.py`. -/
theorem mu4GPMT_H4_lt_zero (q : R) (hq : 0 < q) :
    mu4GPMT_H4 q < 0 :=
  mu4GPMT_H4_neg_of_pos q hq

end OrderedMagnitudeRatio

end H4GPMTCumulantRatio
end QOU.MassTheory
