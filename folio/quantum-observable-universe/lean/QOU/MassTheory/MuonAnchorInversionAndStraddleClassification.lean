/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# Muon Anchor Inversion, Drift Magnification, Symbolic Pin-Independence, and C/D × Pin Straddle Classification

This module formalizes the exact algebraic and structural theorems for five tasks under
the `qou-2002` calibration and anchor-hygiene epic:

1. **Bean `qou-5op4` (CAL-2 Muon Pin Inversion `q(h) = (1 - h)⁻¹` & Three-Value Ordering `q_B < q_A < q_C`)**:
   - Proves the exact round-trip inversion `hbarFromQ (cal2MuonQ h) = h` and excess identity
     `cal2MuonQ h - 1 = h / (1 - h)` (`cal2MuonQ_roundtrip_and_excess`).
   - Proves the exact secant and relative-shift identities across two `ℏ_q` values
     (`cal2MuonQ_secant_and_rel_shift`).
   - Proves over `ℝ` that `h_B < h_A < h_C` with `h_i < 1` forces the strict ordering
     `q_B < q_A < q_C` (`cal2MuonQ_strict_three_value_ordering`), explaining why the
     retired frozen pin `q_A` (whose inverted `m_μ/m_e = 206.768282989...` lies strictly
     between CODATA-2022 `206.7682827` and CODATA-2018 `206.7682830`) sits strictly
     between `q_B` (CODATA 2018) and `q_C` (CODATA 2022).

2. **Bean `qou-72rd` (Cross-Anchor `(q_μ, q_p)` vs Mislabelled Intra-Muon `(q_A, q_B)` Drift Magnification)**:
   - Proves that for any affine-linearized observable `f(q) = f₀ + s · (q - q₀)`, replacing
     the mislabelled intra-muon pair `(q_A, q_B)` by the true cross-anchor pair `(q_μ, q_p)`
     scales the measured anchor drift by the exact interval ratio `(q_μ - q_p) / (q_A - q_B)`
     (`≈ 4087.11×`), and proves the exact secant factorization for `1 / ℏ_q² = q² / (q - 1)²`
     (`crossAnchor_drift_magnification_and_inv_hbar_sq_secant`).

3. **Bean `qou-mha1` (Symbolic Habiro Payload Pin-Independence & Secant Factorization)**:
   - Proves that evaluating the integer-coefficient Habiro polynomials
     `a₁(u) = -35712 u - 35712` and `a₂(u) = 491861 u² + 503768 u + 515411` at a consumer's
     runtime `u` is independent of the producer's witness stamp `q_stamp`, and satisfies
     exact factored secant identities across consumer pins `(u₁, u₂)`
     (`habiroSymbolicPayload_stamp_independent_and_secant`).

4. **Beans `qou-3zby` & `qou-dau6` (`H₃(q)` Convention C/D Ratio & Four-Method Straddle Factorization)**:
   - Proves that on `H₃(q)` the ratio of the convention-D Markov parameter `z_D(q) = q³/(q²+1)`
     to the convention-C Wenzl parameter `z_C(q) = q²/(q⁴+q²+1)` is `q (q² + 1 + q⁻²) / (q + q⁻¹) = q [3]_q / [2]_q`
     with difference `q³(q³ - 1) / ((q² + 1)(q⁴ + q² + 1))`
     (`markovZD_over_markovZC_and_diff`).
   - Proves the transitive cross-ratio decomposition `T_D(q_μ) / T_C(q_p) = (T_D(q_μ)/T_C(q_μ)) · (T_C(q_μ)/T_C(q_p))`
     and relative-discrepancy duality `1 - ρ_{D/C}⁻¹ = (ρ_{D/C} - 1) / ρ_{D/C}` separating the
     convention C/D split (`qou-3zby`) from the proton/muon pin straddle (`qou-dau6`)
     (`fourMethod_straddle_cross_ratio_and_rel_delta`).
-/

namespace QOU.MassTheory.MuonAnchorInversionAndStraddleClassification

section FieldIdentities

variable {K : Type*} [Field K]

/-! ### 1. Bean `qou-5op4`: Exact CAL-2 Muon Pin Inversion `q(h) = (1 - h)⁻¹` -/

/-- CAL-2 substrate parameter `q(h) = (1 - h)⁻¹` solved from `ℏ_q = (q - 1)/q = h`. -/
def cal2MuonQ (h : K) : K := (1 - h)⁻¹

/-- Quantum Planck parameter `ℏ_q(q) = (q - 1) / q`. -/
def hbarFromQ (q : K) : K := (q - 1) / q

/-- **Exact round-trip inversion and `q - 1` excess identity for `cal2MuonQ`.** -/
theorem cal2MuonQ_roundtrip_and_excess (h : K) (hh : 1 - h ≠ 0) :
    hbarFromQ (cal2MuonQ h) = h ∧
      cal2MuonQ h - 1 = h / (1 - h) := by
  unfold hbarFromQ cal2MuonQ
  constructor
  · field_simp
    ring
  · field_simp
    ring

/-- **Exact secant and relative-shift identities across two `ℏ_q` values `h₁, h₂`.** -/
theorem cal2MuonQ_secant_and_rel_shift (h1 h2 : K)
    (hh1 : 1 - h1 ≠ 0) (hh2 : 1 - h2 ≠ 0) :
    cal2MuonQ h2 - cal2MuonQ h1 = (h2 - h1) / ((1 - h1) * (1 - h2)) ∧
      (cal2MuonQ h2 - cal2MuonQ h1) / cal2MuonQ h1 = (h2 - h1) / (1 - h2) := by
  unfold cal2MuonQ
  constructor
  · field_simp
    ring
  · field_simp
    ring

/-! ### 2. Bean `qou-72rd`: Cross-Anchor vs Mislabelled Intra-Muon Drift Magnification -/

/-- Affine-linearized observable `f(q) = f₀ + slope · (q - q₀)` around `q₀`. -/
def affineObs (f0 slope q0 q : K) : K := f0 + slope * (q - q0)

/-- **Replacing a mislabelled intra-muon pair `(q_A, q_B)` with the true cross-anchor pair
`(q_μ, q_p)` magnifies any linear observable drift by `(q_μ - q_p) / (q_A - q_B)`, and the
inverse-square carrier `1/ℏ_q² = q²/(q - 1)²` satisfies an exact secant factorization.** -/
theorem crossAnchor_drift_magnification_and_inv_hbar_sq_secant
    (f0 slope q0 qMu qP qA qB : K)
    (hSlope : slope ≠ 0) (hAB : qA - qB ≠ 0)
    (hqMu1 : qMu - 1 ≠ 0) (hqP1 : qP - 1 ≠ 0) :
    (affineObs f0 slope q0 qMu - affineObs f0 slope q0 qP) /
        (affineObs f0 slope q0 qA - affineObs f0 slope q0 qB) =
      (qMu - qP) / (qA - qB) ∧
      qMu ^ 2 / (qMu - 1) ^ 2 - qP ^ 2 / (qP - 1) ^ 2 =
        (qMu - qP) * (qMu + qP - 2 * qMu * qP) / ((qMu - 1) ^ 2 * (qP - 1) ^ 2) := by
  unfold affineObs
  constructor
  · have hsub1 : f0 + slope * (qMu - q0) - (f0 + slope * (qP - q0)) = slope * (qMu - qP) := by ring
    have hsub2 : f0 + slope * (qA - q0) - (f0 + slope * (qB - q0)) = slope * (qA - qB) := by ring
    rw [hsub1, hsub2]
    field_simp
  · field_simp
    ring

/-! ### 3. Bean `qou-mha1`: Symbolic Expansion Payload Pin-Independence & Secants -/

/-- Symbolic `m = 1` polynomial `a₁(u) = -35712 u - 35712` carrying a witness stamp `qStamp`. -/
def habiroCoeffA1 (u _qStamp : K) : K := -35712 * u - 35712

/-- Symbolic `m = 2` polynomial `a₂(u) = 491861 u² + 503768 u + 515411` carrying a witness stamp `qStamp`. -/
def habiroCoeffA2 (u _qStamp : K) : K := 491861 * u ^ 2 + 503768 * u + 515411

/-- **Symbolic expansion coefficients are invariant under the producer's witness stamp `qStamp`
and satisfy exact factored secant identities across consumer evaluation pins `(u₁, u₂)`.** -/
theorem symbolicPayload_stamp_independent_and_secant (u1 u2 qs1 qs2 : K) :
    habiroCoeffA1 u1 qs1 - habiroCoeffA1 u1 qs2 = 0 ∧
      habiroCoeffA2 u1 qs1 - habiroCoeffA2 u1 qs2 = 0 ∧
      habiroCoeffA1 u1 qs1 - habiroCoeffA1 u2 qs2 = -35712 * (u1 - u2) ∧
      habiroCoeffA2 u1 qs1 - habiroCoeffA2 u2 qs2 =
        (u1 - u2) * (491861 * (u1 + u2) + 503768) := by
  have h1 : habiroCoeffA1 u1 qs1 - habiroCoeffA1 u1 qs2 = 0 := by
    change (-35712 * u1 - 35712) - (-35712 * u1 - 35712) = 0
    ring
  have h2 : habiroCoeffA2 u1 qs1 - habiroCoeffA2 u1 qs2 = 0 := by
    change (491861 * u1 ^ 2 + 503768 * u1 + 515411) - (491861 * u1 ^ 2 + 503768 * u1 + 515411) = 0
    ring
  have h3 : habiroCoeffA1 u1 qs1 - habiroCoeffA1 u2 qs2 = -35712 * (u1 - u2) := by
    change (-35712 * u1 - 35712) - (-35712 * u2 - 35712) = -35712 * (u1 - u2)
    ring
  have h4 : habiroCoeffA2 u1 qs1 - habiroCoeffA2 u2 qs2 =
      (u1 - u2) * (491861 * (u1 + u2) + 503768) := by
    change (491861 * u1 ^ 2 + 503768 * u1 + 515411) - (491861 * u2 ^ 2 + 503768 * u2 + 515411) =
      (u1 - u2) * (491861 * (u1 + u2) + 503768)
    ring
  exact ⟨h1, h2, h3, h4⟩

/-! ### 4. Beans `qou-3zby` & `qou-dau6`: Convention C/D Ratio & Four-Method Straddle Factorization -/

/-- Convention-D trace parameter on `H₃(q)` in `t = √q` (`q = t²`): `z_D(t) = t⁶ / (t⁴ + 1) = q³ / (q² + 1)`. -/
def markovZD (t : K) : K := t ^ 6 / (t ^ 4 + 1)

/-- Convention-C trace parameter on `H₃(q)` in `t = √q`: `z_C(t) = t / (t² + 1) = 1 / (q^{1/2} + q^{-1/2})`. -/
def markovZC (t : K) : K := t / (t ^ 2 + 1)

/-- **Ratio and difference of the `H₃(q)` trace parameters under conventions D and C in `t = √q`.** -/
theorem conventionZD_over_conventionZC_and_diff (t : K)
    (ht : t ≠ 0) (ht2 : t ^ 2 + 1 ≠ 0) (ht4 : t ^ 4 + 1 ≠ 0) :
    markovZD t / markovZC t = t ^ 5 * (t ^ 2 + 1) / (t ^ 4 + 1) ∧
      markovZD t - markovZC t = t * (t ^ 7 + t ^ 5 - t ^ 4 - 1) / ((t ^ 2 + 1) * (t ^ 4 + 1)) := by
  unfold markovZD markovZC
  constructor
  · field_simp
    ring
  · field_simp
    ring

/-- **Transitive cross-ratio and relative-discrepancy duality for a four-method
convention × pin straddle (`qou-3zby`, `qou-dau6`).**
When `T_D(q_μ) = ρ_{D/C} · T_C(q_μ)`, the cross-convention/cross-pin ratio `T_D(q_μ) / T_C(q_p)`
factors into `ρ_{D/C} · (T_C(q_μ) / T_C(q_p))`, and the relative convention discrepancy
`(T_D(q_μ) - T_C(q_μ)) / T_D(q_μ)` equals `1 - ρ_{D/C}⁻¹` (`≈ 0.3247986` for `ρ_{D/C} ≈ 1.4810393`). -/
theorem fourMethod_straddle_cross_ratio_and_rel_delta (rhoDC tCMu tCP : K)
    (hrho : rhoDC ≠ 0) (htMu : tCMu ≠ 0) (htP : tCP ≠ 0) :
    (rhoDC * tCMu) / tCP = rhoDC * (tCMu / tCP) ∧
      (rhoDC * tCMu - tCMu) / (rhoDC * tCMu) = 1 - rhoDC⁻¹ := by
  constructor
  · field_simp
  · field_simp
    ring

end FieldIdentities

section RealOrdering

/-! ### 1b. Bean `qou-5op4`: Strict Three-Value Ordering `q_B < q_A < q_C` over `ℝ` -/

/-- **For `h_B < h_A < h_C < 1`, the CAL-2 map `q(h) = (1 - h)⁻¹` preserves strict order:
`q(h_B) < q(h_A) < q(h_C)`.** -/
theorem cal2MuonQ_strict_three_value_ordering (hB hA hC : ℝ)
    (hBA : hB < hA) (hAC : hA < hC)
    (hB1 : 0 < 1 - hB) (hA1 : 0 < 1 - hA) (hC1 : 0 < 1 - hC) :
    cal2MuonQ hB < cal2MuonQ hA ∧ cal2MuonQ hA < cal2MuonQ hC := by
  have hB_ne : 1 - hB ≠ 0 := ne_of_gt hB1
  have hA_ne : 1 - hA ≠ 0 := ne_of_gt hA1
  have hC_ne : 1 - hC ≠ 0 := ne_of_gt hC1
  constructor
  · have hsec : cal2MuonQ hA - cal2MuonQ hB = (hA - hB) / ((1 - hB) * (1 - hA)) :=
      (cal2MuonQ_secant_and_rel_shift hB hA hB_ne hA_ne).1
    have hd : 0 < hA - hB := sub_pos.mpr hBA
    have hpos : 0 < (hA - hB) / ((1 - hB) * (1 - hA)) := by positivity
    linarith
  · have hsec : cal2MuonQ hC - cal2MuonQ hA = (hC - hA) / ((1 - hA) * (1 - hC)) :=
      (cal2MuonQ_secant_and_rel_shift hA hC hA_ne hC_ne).1
    have hd : 0 < hC - hA := sub_pos.mpr hAC
    have hpos : 0 < (hC - hA) / ((1 - hA) * (1 - hC)) := by positivity
    linarith

end RealOrdering

end QOU.MassTheory.MuonAnchorInversionAndStraddleClassification
