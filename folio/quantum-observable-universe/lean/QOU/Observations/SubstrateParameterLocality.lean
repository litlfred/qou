import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Substrate Parameter Locality and Varying-Constants Co-Variation (`qou-1u7x`, `qou-cweq`, `ovud`, `i5p0`, `qou-cgbd`)

Formalizes the algebraic identities underlying:
1. **`qou-1u7x` (`conj:substrate-parameter-locality`)**: The substrate parameter
   `q₀` is an observed-local calibration parameter (pinned by CAL-2 / proton mass),
   not derived from a parameter-free equation. Under any slow spatial or cosmological
   perturbation `δ(ln q₀)`, all `q`-dependent dimensionless observables `O_i(q)`
   co-vary with locked logarithmic sensitivities `κ_i(q₀) := d ln O_i / d ln q |_{q₀}`:
   * Leading mass-ratio scaling `O_μ(q) ∝ ℏ_q⁻² = (1 − q⁻¹)⁻²` has logarithmic
     sensitivity `κ_μ(q) = −2 / (q − 1) = −2 c_q(q)` (`≈ −18.185` at `q₀`).
   * Quantum-integer fine-structure channel `O_α(q) ∝ [3]_q⁻¹ = (q² + 1 + q⁻²)⁻¹`
     has logarithmic sensitivity `κ_α^{[3]}(q) = −2(q² − q⁻²) / (q² + 1 + q⁻²)`
     (`≈ −0.276` at `q₀`), and for `[2]_q⁻¹ = (q + q⁻¹)⁻¹`,
     `κ_α^{[2]}(q) = −(q − q⁻¹) / (q + q⁻¹)` (`≈ −0.104` at `q₀`).
   * Eliminating the unobservable perturbation `δ(ln q₀)` yields a parameter-free,
     falsifiable co-variation slope `R_{μ/α} = κ_μ(q₀) / κ_α(q₀)` (`+65.83` for `[3]_q`,
     `+174.92` for `[2]_q`) testable against Webb et al. quasar `Δα/α` and `H₂/NH₃`
     `Δμ/μ` bounds.
2. **`qou-cweq`**: The contact-affine speed-of-light ratio `c_q = q⁻¹ / (1 − q⁻¹)`
   equals `1 / (q − 1)`, and its relative shift between two anchors `q_p, q_μ`
   satisfies `(c_q(q_p) − c_q(q_μ)) / c_q(q_p) = (q_μ − q_p) / (q_μ − 1)`.
3. **`ovud`**: The `/q³` normalisation in `F_Bor(q) = |tr_M(β_Bor)| · [3]_q! / q³`
   is the exact `q`-factorial Laurent balancing
   `[3]_q [2]_q [1]_q = q³ (1 + 2 q⁻² + 2 q⁻⁴ + q⁻⁶)` over any commutative ring
   with `q · qi = 1`, not an empirical fit.
4. **`i5p0`**: Any homogeneous `1 / ℏ_q` enhancement `F̃_q(K) = ℏ_q⁻¹ · F_0(K)`
   (such as `log Φ_q(z) ~ Li₂(z) / ℏ_q`) cancels identically in a homogeneous
   per-braid lepton ratio `F̃_q(K_μ) / F̃_q(K_e) = F_0(K_μ) / F_0(K_e)`.

-- Ref: [leitner2026] conj:substrate-parameter-locality
-/

namespace QOU.Observations

section CommRingIdentities

variable {R : Type*} [CommRing R]

/-- **Bean `ovud`: `/q³` in `F_Bor` is an exact Laurent-polynomial balancing.**
Over any commutative ring `R` with `q * qi = 1` (`qi = q⁻¹`), the balanced
quantum factorial `[3]_q! = (q² + 1 + qi²) * (q + qi) * 1` satisfies
`[3]_q! = q³ * (1 + 2 * qi² + 2 * qi⁴ + qi⁶)` identically. -/
theorem qfact3_eq_q3_mul_laurent_balancing (q qi : R) (hqi : q * qi = 1) :
    (q ^ 2 + 1 + qi ^ 2) * (q + qi) =
      q ^ 3 * (1 + 2 * qi ^ 2 + 2 * qi ^ 4 + qi ^ 6) := by
  linear_combination
    (-q ^ 2 * qi ^ 5 - 2 * q ^ 2 * qi ^ 3 - 2 * q ^ 2 * qi
      - q * qi ^ 4 - 2 * q * qi ^ 2 - q - qi ^ 3 - qi) * hqi

/-- Expanded symmetric Laurent form of `[3]_q! = q³ + 2q + 2q⁻¹ + q⁻³`. -/
theorem qfact3_expanded_laurent (q qi : R) (hqi : q * qi = 1) :
    (q ^ 2 + 1 + qi ^ 2) * (q + qi) = q ^ 3 + 2 * q + 2 * qi + qi ^ 3 := by
  linear_combination (q + qi) * hqi

/-- Division-free form of the contact-affine ratio identity `c_q = q⁻¹ / (1 − q⁻¹) = 1 / (q − 1)`:
`qi * (q - 1) = 1 * (1 - qi)` whenever `q * qi = 1`. -/
theorem cq_hbarQ_cross_identity (q qi : R) (hqi : q * qi = 1) :
    qi * (q - 1) = 1 - qi := by
  linear_combination hqi

end CommRingIdentities

section FieldIdentities

variable {F : Type*} [Field F]

/-- Contact-affine speed-of-light ratio `c_q(q) = 1 / (q − 1)`. -/
def cq (q : F) : F := 1 / (q - 1)

/-- Leading mass-ratio logarithmic sensitivity `κ_μ(q) = d ln(ℏ_q⁻²) / d ln q = −2 / (q − 1)`. -/
def kappaMu (q : F) : F := -2 / (q - 1)

/-- Fine-structure logarithmic sensitivity for `[3]_q = q² + 1 + q⁻²`:
`κ_α^{[3]}(q) = −2(q² − q⁻²) / (q² + 1 + q⁻²)`. -/
def kappaAlpha3 (q qi : F) : F :=
  -2 * (q ^ 2 - qi ^ 2) / (q ^ 2 + 1 + qi ^ 2)

/-- Fine-structure logarithmic sensitivity for `[2]_q = q + q⁻¹`:
`κ_α^{[2]}(q) = −(q − q⁻¹) / (q + q⁻¹)`. -/
def kappaAlpha2 (q qi : F) : F :=
  -(q - qi) / (q + qi)

/-- **Bean `qou-cweq`: Exact anchor-shift identity for `c_q`.**
Between any two substrate pins `q_p, q_μ ≠ 1`, the relative shift in `c_q` is
`(c_q(q_p) − c_q(q_μ)) / c_q(q_p) = (q_μ − q_p) / (q_μ − 1)`. -/
theorem cq_anchor_relative_shift (qp qmu : F) (hp : qp - 1 ≠ 0) (hmu : qmu - 1 ≠ 0) :
    (cq qp - cq qmu) / cq qp = (qmu - qp) / (qmu - 1) := by
  unfold cq
  field_simp [hp, hmu]
  ring

/-- **Bean `qou-1u7x`: Mass-ratio sensitivity equals `−2 · c_q(q)`.** -/
theorem kappaMu_eq_neg_two_cq (q : F) :
    kappaMu q = -2 * cq q := by
  unfold kappaMu cq
  ring

/-- **Bean `qou-1u7x`: Parameter-free linear-response co-variation law.**
If two observables respond to a local perturbation `δq = δ(ln q₀)` via
`δO₁ = κ₁ · δq` and `δO₂ = κ₂ · δq` with `δq ≠ 0`, then the unobservable
perturbation `δq` cancels identically: `δO₁ / δO₂ = κ₁ / κ₂`. -/
theorem linear_response_covariation_eliminates_dq
    (kappa1 kappa2 dq : F) (hdq : dq ≠ 0) :
    (kappa1 * dq) / (kappa2 * dq) = kappa1 / kappa2 := by
  exact mul_div_mul_right kappa1 kappa2 hdq

/-- **Bean `qou-1u7x`: Closed-form co-variation slope `R_{μ/α}^{[3]}(q)`.** -/
theorem covariation_ratio_alpha3 (q qi : F)
    (hq1 : q - 1 ≠ 0) (hdiff : q ^ 2 - qi ^ 2 ≠ 0) (hq3 : q ^ 2 + 1 + qi ^ 2 ≠ 0) :
    kappaMu q / kappaAlpha3 q qi =
      (q ^ 2 + 1 + qi ^ 2) / ((q - 1) * (q ^ 2 - qi ^ 2)) := by
  unfold kappaMu kappaAlpha3
  field_simp [hq1, hdiff, hq3]
  ring

/-- **Bean `qou-1u7x`: Closed-form co-variation slope `R_{μ/α}^{[2]}(q)`.** -/
theorem covariation_ratio_alpha2 (q qi : F)
    (hq1 : q - 1 ≠ 0) (hdiff : q - qi ≠ 0) (hq2 : q + qi ≠ 0) :
    kappaMu q / kappaAlpha2 q qi =
      2 * (q + qi) / ((q - 1) * (q - qi)) := by
  unfold kappaMu kappaAlpha2
  field_simp [hq1, hdiff, hq2]
  ring

/-- **Bean `i5p0`: Homogeneous `1 / ℏ_q` enhancement cancels in lepton mass ratios.**
If a per-braid tower functional scales homogeneously as `F̃_q(K) = h⁻¹ · F_0(K)`
with `h ≠ 0`, then `F̃_q(K_μ) / F̃_q(K_e) = F_0(K_μ) / F_0(K_e)`.
Hence a `1 / ℏ_q` prefactor shared by both numerator and denominator cannot
generate the `1 / ℏ_q² ≈ 101.86` scale separation between `m_μ` and `m_e`. -/
theorem homogeneous_hbar_scaling_cancels (h F_mu F_e : F) (hh : h ≠ 0) :
    (h⁻¹ * F_mu) / (h⁻¹ * F_e) = F_mu / F_e := by
  have hinv : h⁻¹ ≠ 0 := inv_ne_zero hh
  exact mul_div_mul_left F_mu F_e hinv

end FieldIdentities

section RealBounds

/-- **Bean `qou-1u7x`: Same-sign positive co-variation slope on `q > 1`.**
In the QOU regime `1 < q`, both `κ_μ(q) < 0` and `κ_α^{[2]}(q, q⁻¹) < 0`, so
their co-variation ratio `R_{μ/α}^{[2]}(q) = κ_μ(q) / κ_α^{[2]}(q, q⁻¹)` is
strictly positive: any spatial or cosmological drift `δq₀` shifts `m_μ/m_e`
(and `m_p/m_e`) and `α_EM` with the **same sign**. -/
theorem covariation_ratio_alpha2_pos_of_gt_one (q : ℝ) (hq : 1 < q) :
    0 < kappaMu q / kappaAlpha2 q q⁻¹ := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hq1 : 0 < q - 1 := sub_pos.mpr hq
  have hqi_lt_one : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hdiff : 0 < q - q⁻¹ := by linarith
  have hsum : 0 < q + q⁻¹ := by positivity
  have h_eq : kappaMu q / kappaAlpha2 q q⁻¹ = 2 * (q + q⁻¹) / ((q - 1) * (q - q⁻¹)) :=
    covariation_ratio_alpha2 q q⁻¹ (ne_of_gt hq1) (ne_of_gt hdiff) (ne_of_gt hsum)
  rw [h_eq]
  positivity

end RealBounds

end QOU.Observations
