/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import QOU.MassTheory.AlphaEmTwoLoopBlochSchwinger
import QOU.StandardModel.ElectroweakBringSchwingerBridge
import QOU.StandardModel.ElectroweakSweedlerScaleAndRGThresholds

/-!
# Electroweak Boson Thresholds (`M_W`, `M_Z`), Plancherel Weinberg Angle, and `v`-Independent Higgs Quartic

This module formalizes the coupled electroweak gauge-boson and Higgs mass-threshold identities
atop the Bring–Schwinger weak scale `v_weak(q₀)` and electromagnetic coupling `α_EM(q₀)`
(`Q-Gap-9`: beans `qou-ewsb`, `qou-ukqh`, `qou-z3x8`, `qou-zd6l`):

1. **Section 1 — Generic `[CommRing R]` and `[Field K]` Algebraic Core (`AGENTS.md` §7c):**
   - Exact polynomial positivity decomposition for the quantum-dimension-dressed `Z/W` torus-link
     Plancherel ratio (`W = T(2,4)`, `Z = T(2,6)`):
     `twoMulP 3 h * (h ^ 2 + 4) - twoMulP 2 h * 4 = h ^ 2 * (13 + 22 * h ^ 2 + 9 * h ^ 4 + h ^ 6)`
     (`plancherel_zw_gap_poly_eq`), proving that the `Z/W` splitting vanishes in the unbroken
     `h = 0` (`q = ±1`) limit and has strictly positive even-power coefficients `(13, 22, 9, 1)`.
   - Exact algebraic identities for `plancherelCosSq`, `plancherelSinSq`, and `plancherelCotSq`
     over any `[Field K]`, including `cos² + sin² = 1`, classical limit `sin²(0, 2) = 0`, and the
     cotangent bridge `sin² * (1 + cot²) = 1`.
   - Sirlin radiatively-dressed mass-squared relations (`derivedMWSq`, `derivedMZSq`), exact
     cancellation of `(1 - Δr)`, `π α_EM`, and `v²` in `M_W² / M_Z² = cos² θ_W · ρ`, and the
     custodial equivalence `1 - M_W² / M_Z² = sin² θ_W ↔ ρ = 1`.
   - **Exact Zero-Spread Higgs Unification & `v`-Independent Higgs Quartic (`derivedHiggsQuartic`):**
     When `M_W` and `M_Z` are determined by the dressed Plancherel `Z/W` ratio rather than separate
     empirical inputs, the `W`-anchored and `Z`-anchored Higgs mass formulas agree identically
     (`derived_higgs_w_eq_z_zero_spread`), and the weak vacuum expectation value `v` cancels
     identically out of the Higgs self-coupling `λ_H = m_H² / (2 v²)`
     (`derived_higgs_quartic_vev_independent`).

2. **Section 2 — Ordered-Field Positivity (`0 < sin² θ_W < 1`, `0 < λ_H`) & Global Stability:**
   - Proves over any strict ordered field `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`
     that for every `q ≠ 0` with `q - q⁻¹ ≠ 0`, `0 < plancherelSinSq (q - q⁻¹) (q + q⁻¹) < 1`
     and `0 < derivedHiggsQuartic`, guaranteeing a unique global Higgs potential minimum via
     `QOU.StandardModel.EWSweedlerRG.higgsPotential_unique_global_min_of_pos_quartic`.

3. **Section 3 — Non-Vacuous `§3b-cond` Hypothesis Class & `trivialModel` Consistency Witness (`ℝ`):**
   - Packages the coupled `(α_EM, α_v, M_W, M_Z, m_H, λ_H)` threshold system in
     `ElectroweakBosonThresholdSystemClass` with **zero global instances** and an explicit
     `noncomputable def trivialModel` consistency witness (`lean-generation` §5).
-/

set_option autoImplicit false

namespace QOU.StandardModel

open QOU.QInteger (qIntBal)
open QOU.Archimedean.BringSchwingerNormalizationDerivation (habiroNorm hHecke)
open QOU.Archimedean (firstBetti bringSurfaceArea bringFundamentalTriangleArea)
open QOU.Archimedean.AlphaEmTwoLoopBlochSchwinger (IsTwoLoopBringFixedPoint twoLoopBringCubic
  twoLoopBringFixedPoint_iff_cubic exists_unique_pos_cubic_root)
open QOU.StandardModel.EWSweedlerRG (higgsPotential higgsPotential_unique_global_min_of_pos_quartic)

/-! ## Section 1: Generic `[CommRing R]` & `[Field K]` Plancherel Weinberg and Higgs Identities -/

section GenericCommRing

variable {R : Type*} [CommRing R]

/-- Exact division-free polynomial gap between the quantum-dimension-dressed `Z = T(2,6)` numerator
`2 P₃(h) · (h² + 4)` and the `W = T(2,4)` denominator `2 P₂(h) · 4`:
`twoMulP 3 h * (h ^ 2 + 4) - twoMulP 2 h * 4 = h ^ 2 * (13 + 22 * h ^ 2 + 9 * h ^ 4 + h ^ 6)`. -/
theorem plancherel_zw_gap_poly_eq (h : R) :
    twoMulP 3 h * (h ^ 2 + 4) - twoMulP 2 h * 4 =
      h ^ 2 * (13 + 22 * h ^ 2 + 9 * h ^ 4 + h ^ 6) := by
  unfold twoMulP
  ring

/-- Evaluated at `(h, q2) = (q - qi, q + qi)` with `q * qi = 1`, the dressed `Z/W` numerator gap
factors into `h²` times strictly positive even-power coefficients `(13, 22, 9, 1)`. -/
theorem plancherel_zw_gap_laurent_eq (q qi : R) (hinv : q * qi = 1) :
    twoMulP 3 (q - qi) * (q + qi) ^ 2 - twoMulP 2 (q - qi) * 4 =
      (q - qi) ^ 2 *
        (13 + 22 * (q - qi) ^ 2 + 9 * (q - qi) ^ 4 + (q - qi) ^ 6) := by
  rw [qInt2_sq_eq_h_sq_add_four q qi hinv]
  exact plancherel_zw_gap_poly_eq (q - qi)

/-- Unbroken classical specialization (`h = 0`) of the doubled Plancherel polynomials `m = 2, 3, 4`:
`2 P₂(0) = 1`, `2 P₃(0) = 1`, `2 P₄(0) = 1`. -/
theorem twoMulP_zero_specializations :
    twoMulP 2 (0 : R) = 1 ∧ twoMulP 3 (0 : R) = 1 ∧ twoMulP 4 (0 : R) = 1 := by
  unfold twoMulP
  refine ⟨by ring, by ring, by ring⟩

end GenericCommRing

section GenericField

variable {K : Type*} [Field K]

/-- Bare 2-strand torus-link Plancherel `Z/W` ratio `P₃(h) / P₂(h)` (`W = T(2,4)`, `Z = T(2,6)`). -/
def plancherelBareZWRatio (h : K) : K :=
  twoMulP 3 h / twoMulP 2 h

/-- Quantum-dimension-dressed 2-strand torus-link Plancherel `Z/W` mass ratio
`r_ZW(h, q2) = (P₃(h) / P₂(h)) · (q2 / 2)² = (2 P₃(h) · q2²) / (2 P₂(h) · 4)`. -/
def plancherelZWRatio (h q2 : K) : K :=
  (twoMulP 3 h * q2 ^ 2) / (twoMulP 2 h * 4)

/-- On-shell squared Weinberg cosine from the dressed torus-link Plancherel ratio:
`cos² θ_W^Planch(h, q2) = (2 P₂(h) · 4)² / (2 P₃(h) · q2²)²`. -/
def plancherelCosSq (h q2 : K) : K :=
  (twoMulP 2 h * 4) ^ 2 / (twoMulP 3 h * q2 ^ 2) ^ 2

/-- On-shell squared Weinberg sine from the dressed torus-link Plancherel ratio:
`sin² θ_W^Planch(h, q2) = 1 - cos² θ_W^Planch(h, q2)`. -/
def plancherelSinSq (h q2 : K) : K :=
  1 - plancherelCosSq h q2

/-- Squared Weinberg cotangent associated with `plancherelCosSq` and `plancherelSinSq`:
`cot² θ_W^Planch(h, q2) = (2 P₂(h) · 4)² / ((2 P₃(h) · q2²)² - (2 P₂(h) · 4)²)`. -/
def plancherelCotSq (h q2 : K) : K :=
  (twoMulP 2 h * 4) ^ 2 / ((twoMulP 3 h * q2 ^ 2) ^ 2 - (twoMulP 2 h * 4) ^ 2)

/-- Partition of unity `cos² θ_W + sin² θ_W = 1` over any field `K`. -/
theorem plancherel_cosSq_add_sinSq (h q2 : K) :
    plancherelCosSq h q2 + plancherelSinSq h q2 = 1 := by
  unfold plancherelSinSq
  ring

/-- Inverse-square relation `plancherelCosSq h q2 * (plancherelZWRatio h q2)² = 1` whenever the
`W` and `Z` Plancherel denominators are nonzero. -/
theorem plancherel_cosSq_mul_zwRatio_sq (h q2 : K)
    (hP2 : twoMulP 2 h ≠ 0) (hP3 : twoMulP 3 h ≠ 0) (hq2 : q2 ≠ 0) (h4 : (4 : K) ≠ 0) :
    plancherelCosSq h q2 * (plancherelZWRatio h q2) ^ 2 = 1 := by
  unfold plancherelCosSq plancherelZWRatio
  have hd2 : twoMulP 2 h * 4 ≠ 0 := mul_ne_zero hP2 h4
  have hd3 : twoMulP 3 h * q2 ^ 2 ≠ 0 := mul_ne_zero hP3 (pow_ne_zero 2 hq2)
  field_simp [hd2, hd3]

/-- Unbroken classical limit (`h = 0`, `q2 = 2`): `plancherelZWRatio 0 2 = 1` and
`plancherelSinSq 0 2 = 0` over any field with `4 ≠ 0`. -/
theorem plancherel_classical_unbroken_limit (h4 : (4 : K) ≠ 0) :
    plancherelZWRatio (0 : K) 2 = 1 ∧ plancherelSinSq (0 : K) 2 = 0 := by
  unfold plancherelZWRatio plancherelSinSq plancherelCosSq
  rw [twoMulP_zero_specializations.1, twoMulP_zero_specializations.2.1]
  have h22 : (1 : K) * 2 ^ 2 = 4 := by ring
  have h14 : (1 : K) * 4 = 4 := by ring
  rw [h22, h14, div_self h4, div_self (pow_ne_zero 2 h4), sub_self]
  exact ⟨rfl, rfl⟩

/-- Algebraic bridge to `WeinbergAngleCategorical`'s cotangent parameterization:
`plancherelSinSq h q2 * (1 + plancherelCotSq h q2) = 1` and
`plancherelCosSq h q2 = plancherelCotSq h q2 * plancherelSinSq h q2`. -/
theorem plancherel_sinSq_cotSq_bridge (h q2 : K)
    (hZ : twoMulP 3 h * q2 ^ 2 ≠ 0)
    (hdiff : (twoMulP 3 h * q2 ^ 2) ^ 2 - (twoMulP 2 h * 4) ^ 2 ≠ 0) :
    plancherelSinSq h q2 * (1 + plancherelCotSq h q2) = 1 ∧
    plancherelCosSq h q2 = plancherelCotSq h q2 * plancherelSinSq h q2 := by
  unfold plancherelSinSq plancherelCosSq plancherelCotSq
  set W : K := (twoMulP 2 h * 4) ^ 2
  set Z : K := (twoMulP 3 h * q2 ^ 2) ^ 2
  have hZ2 : Z ≠ 0 := pow_ne_zero 2 hZ
  have hdiff' : Z - W ≠ 0 := hdiff
  refine ⟨?_, ?_⟩
  · field_simp [hZ2, hdiff']
    ring
  · field_simp [hZ2, hdiff']

/-- Radiatively-dressed Sirlin `W`-boson mass squared over `[Field K]`, with `piAlpha` standing for
`π · α_EM(0)` and `oneSubDeltaR` standing for `1 - Δr`:
`M_W² = (π α_EM · v²) / (sin² θ_W · (1 - Δr))`. -/
def derivedMWSq (piAlpha v sinSq oneSubDeltaR : K) : K :=
  (piAlpha * v ^ 2) / (sinSq * oneSubDeltaR)

/-- Radiatively-dressed `Z`-boson mass squared with custodial parameter `ρ`:
`M_Z² = M_W² / (cos² θ_W · ρ)`. -/
def derivedMZSq (piAlpha v sinSq cosSq rho oneSubDeltaR : K) : K :=
  derivedMWSq piAlpha v sinSq oneSubDeltaR / (cosSq * rho)

/-- Cleared Sirlin mass-coupling relation: `M_W² · sin² θ_W · (1 - Δr) = π α_EM · v²`. -/
theorem derived_mwSq_sirlin_relation (piAlpha v sinSq oneSubDeltaR : K)
    (hs : sinSq ≠ 0) (hdr : oneSubDeltaR ≠ 0) :
    derivedMWSq piAlpha v sinSq oneSubDeltaR * sinSq * oneSubDeltaR = piAlpha * v ^ 2 := by
  unfold derivedMWSq
  have hden : sinSq * oneSubDeltaR ≠ 0 := mul_ne_zero hs hdr
  field_simp [hden]

/-- **Exact Cancellation of `(1 - Δr)`, `π α_EM`, and `v²` in `M_W² / M_Z²`:**
In the ratio `derivedMWSq / derivedMZSq`, the Sirlin radiative factor `1 - Δr`, electromagnetic
scale `π α_EM`, and weak VEV `v²` cancel identically, leaving `cos² θ_W · ρ`. -/
theorem derived_mwSq_div_mzSq_eq_cosSq_mul_rho
    (piAlpha v sinSq cosSq rho oneSubDeltaR : K)
    (hpa : piAlpha ≠ 0) (hv : v ≠ 0) (hs : sinSq ≠ 0)
    (hc : cosSq ≠ 0) (hrho : rho ≠ 0) (hdr : oneSubDeltaR ≠ 0) :
    derivedMWSq piAlpha v sinSq oneSubDeltaR /
      derivedMZSq piAlpha v sinSq cosSq rho oneSubDeltaR = cosSq * rho := by
  unfold derivedMZSq derivedMWSq
  have hnum : piAlpha * v ^ 2 ≠ 0 := mul_ne_zero hpa (pow_ne_zero 2 hv)
  have hden1 : sinSq * oneSubDeltaR ≠ 0 := mul_ne_zero hs hdr
  have hden2 : cosSq * rho ≠ 0 := mul_ne_zero hc hrho
  field_simp [hnum, hden1, hden2]

/-- **Custodial `ρ = 1` Equivalence:** When `cosSq + sinSq = 1` and denominators are nonzero,
the Sirlin on-shell observable `1 - M_W² / M_Z²` equals `sinSq` if and only if `rho = 1`. -/
theorem custodial_rho_one_iff_onshell_sinSq
    (piAlpha v sinSq cosSq rho oneSubDeltaR : K)
    (hsum : cosSq + sinSq = 1)
    (hpa : piAlpha ≠ 0) (hv : v ≠ 0) (hs : sinSq ≠ 0)
    (hc : cosSq ≠ 0) (hrho : rho ≠ 0) (hdr : oneSubDeltaR ≠ 0) :
    1 - derivedMWSq piAlpha v sinSq oneSubDeltaR /
        derivedMZSq piAlpha v sinSq cosSq rho oneSubDeltaR = sinSq ↔ rho = 1 := by
  rw [derived_mwSq_div_mzSq_eq_cosSq_mul_rho piAlpha v sinSq cosSq rho oneSubDeltaR
    hpa hv hs hc hrho hdr]
  constructor
  · intro h
    have hcr : cosSq * (rho - 1) = 0 := by linear_combination -h - hsum
    rcases mul_eq_zero.mp hcr with hc0 | hr1
    · exact absurd hc0 hc
    · linear_combination hr1
  · intro hr1
    rw [hr1, mul_one]
    linear_combination -hsum

/-- `W`-anchored Higgs mass formula from any `W` mass `mW`:
`m_H^(W) = mW · (P₄(h) / P₂(h)) · (6 / 5) · (q2 / 2) · cLoop`. -/
def derivedHiggsFromW (mW h q2 cLoop : K) : K :=
  mW * (twoMulP 4 h / twoMulP 2 h) * (6 / 5) * (q2 / 2) * cLoop

/-- `Z`-anchored Higgs mass formula from any `Z` mass `mZ`:
`m_H^(Z) = mZ · (P₄(h) / P₃(h)) · (6 / 5) · (2 / q2) · cLoop`. -/
def derivedHiggsFromZ (mZ h q2 cLoop : K) : K :=
  mZ * (twoMulP 4 h / twoMulP 3 h) * (6 / 5) * (2 / q2) * cLoop

/-- **Exact Zero-Spread Higgs Anchor Unification (`derived_higgs_w_eq_z_zero_spread`):**
Whenever `mZ = mW * plancherelZWRatio h q2` (so both `M_W` and `M_Z` come from the QOU Plancherel
chain rather than separate empirical inputs), `derivedHiggsFromW` and `derivedHiggsFromZ` are
identically equal and their anchor spread vanishes (`m_H^(W) - m_H^(Z) = 0`). -/
theorem derived_higgs_w_eq_z_zero_spread (mW mZ h q2 cLoop : K)
    (hZW : mZ = mW * plancherelZWRatio h q2)
    (hP2 : twoMulP 2 h ≠ 0) (hP3 : twoMulP 3 h ≠ 0)
    (hq2 : q2 ≠ 0) (h2 : (2 : K) ≠ 0) (h5 : (5 : K) ≠ 0) :
    derivedHiggsFromW mW h q2 cLoop = derivedHiggsFromZ mZ h q2 cLoop ∧
    derivedHiggsFromW mW h q2 cLoop - derivedHiggsFromZ mZ h q2 cLoop = 0 := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by ring
    rw [this]
    exact mul_ne_zero h2 h2
  have heq : derivedHiggsFromW mW h q2 cLoop = derivedHiggsFromZ mZ h q2 cLoop := by
    rw [hZW]
    unfold derivedHiggsFromW derivedHiggsFromZ plancherelZWRatio
    field_simp [hP2, hP3, hq2, h2, h4, h5]
    ring
  exact ⟨heq, sub_eq_zero.mpr heq⟩

/-- Squared QOU-derived Higgs mass directly from `(π α_EM, v, sin² θ_W, 1 - Δr, h, q2, cLoop)`
with zero empirical `M_W` or `M_Z` input:
`m_H² = M_W² · ((P₄(h) / P₂(h)) · (6 / 5) · (q2 / 2) · cLoop)²`. -/
def derivedHiggsSq (piAlpha v sinSq oneSubDeltaR h q2 cLoop : K) : K :=
  derivedMWSq piAlpha v sinSq oneSubDeltaR *
    ((twoMulP 4 h / twoMulP 2 h) * (6 / 5) * (q2 / 2) * cLoop) ^ 2

/-- **Scale-Free Derived Higgs Quartic Self-Coupling (`derivedHiggsQuartic`):**
Pure dimensionless function of `(π α_EM, sin² θ_W, 1 - Δr, h, q2, cLoop)` with **no dependence
on `v` (`v_weak`) or `m_e` (`m_p`)**:
`λ_H = (π α_EM / (2 · sin² θ_W · (1 - Δr))) · ((P₄(h) / P₂(h)) · (6 / 5) · (q2 / 2) · cLoop)²`. -/
def derivedHiggsQuartic (piAlpha sinSq oneSubDeltaR h q2 cLoop : K) : K :=
  (piAlpha / (2 * sinSq * oneSubDeltaR)) *
    ((twoMulP 4 h / twoMulP 2 h) * (6 / 5) * (q2 / 2) * cLoop) ^ 2

/-- **`v`-Independence of the Higgs Quartic Self-Coupling (`derived_higgs_quartic_vev_independent`):**
For every nonzero weak VEV `v ≠ 0` over `[Field K]`, `m_H² / (2 v²)` cancels `v²` identically
between numerator and denominator and equals `derivedHiggsQuartic`. -/
theorem derived_higgs_quartic_vev_independent
    (piAlpha v sinSq oneSubDeltaR h q2 cLoop : K)
    (hv : v ≠ 0) (hs : sinSq ≠ 0) (hdr : oneSubDeltaR ≠ 0) (h2 : (2 : K) ≠ 0) :
    derivedHiggsSq piAlpha v sinSq oneSubDeltaR h q2 cLoop / (2 * v ^ 2) =
      derivedHiggsQuartic piAlpha sinSq oneSubDeltaR h q2 cLoop := by
  unfold derivedHiggsSq derivedHiggsQuartic derivedMWSq
  have hv2 : v ^ 2 ≠ 0 := pow_ne_zero 2 hv
  have hden : sinSq * oneSubDeltaR ≠ 0 := mul_ne_zero hs hdr
  field_simp [hv2, hden, h2]

end GenericField

/-! ## Section 2: Ordered-Field Positivity (`0 < sin² θ_W < 1`, `0 < λ_H`) & Higgs Potential Stability -/

section OrderedFieldBounds

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Strictly positive lower bounds `1 ≤ twoMulP m h` (`m = 2, 3, 4`) for every `h : K` in an
ordered field. -/
theorem twoMulP_pos_of_ordered (h : K) :
    0 < twoMulP 2 h ∧ 0 < twoMulP 3 h ∧ 0 < twoMulP 4 h := by
  unfold twoMulP
  have h2 : 0 ≤ h ^ 2 := sq_nonneg h
  have h4 : 0 ≤ h ^ 4 := by
    have : h ^ 4 = (h ^ 2) ^ 2 := by ring
    rw [this]; exact sq_nonneg _
  have h6 : 0 ≤ h ^ 6 := by
    have : h ^ 6 = (h ^ 3) ^ 2 := by ring
    rw [this]; exact sq_nonneg _
  have h8 : 0 ≤ h ^ 8 := by
    have : h ^ 8 = (h ^ 4) ^ 2 := by ring
    rw [this]; exact sq_nonneg _
  refine ⟨by linarith, by linarith, by linarith⟩

/-- **Unconditional Unit-Interval Bound (`0 < sin² θ_W^Planch < 1`) for All `q ∉ {0, 1, -1}`:**
In any strict ordered field `K`, for every nonzero `q : K` with `q - q⁻¹ ≠ 0`, the dressed
torus-link Plancherel Weinberg observable satisfies
`1 < plancherelZWRatio (q - q⁻¹) (q + q⁻¹)` and
`0 < plancherelSinSq (q - q⁻¹) (q + q⁻¹) ∧ plancherelSinSq (q - q⁻¹) (q + q⁻¹) < 1`. -/
theorem plancherel_sinSq_mem_unit_interval (q : K) (hq : q ≠ 0) (hh : q - q⁻¹ ≠ 0) :
    1 < plancherelZWRatio (q - q⁻¹) (q + q⁻¹) ∧
    0 < plancherelSinSq (q - q⁻¹) (q + q⁻¹) ∧
    plancherelSinSq (q - q⁻¹) (q + q⁻¹) < 1 := by
  set h : K := q - q⁻¹
  set q2 : K := q + q⁻¹
  have hinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  obtain ⟨hP2_pos, hP3_pos, _⟩ := twoMulP_pos_of_ordered h
  have hq2_sq : q2 ^ 2 = h ^ 2 + 4 := qInt2_sq_eq_h_sq_add_four q q⁻¹ hinv
  have hq2_sq_pos : 0 < q2 ^ 2 := by
    rw [hq2_sq]
    have : 0 ≤ h ^ 2 := sq_nonneg h
    linarith
  have hW_pos : 0 < twoMulP 2 h * 4 := by linarith
  have hZ_pos : 0 < twoMulP 3 h * q2 ^ 2 := mul_pos hP3_pos hq2_sq_pos
  have hh2_pos : 0 < h ^ 2 := sq_pos_of_ne_zero hh
  have hgap_pos : 0 < twoMulP 3 h * q2 ^ 2 - twoMulP 2 h * 4 := by
    have hgap := plancherel_zw_gap_laurent_eq q q⁻¹ hinv
    change twoMulP 3 h * q2 ^ 2 - twoMulP 2 h * 4 =
      h ^ 2 * (13 + 22 * h ^ 2 + 9 * h ^ 4 + h ^ 6) at hgap
    rw [hgap]
    have h4 : 0 ≤ h ^ 4 := by
      have : h ^ 4 = (h ^ 2) ^ 2 := by ring
      rw [this]; exact sq_nonneg _
    have h6 : 0 ≤ h ^ 6 := by
      have : h ^ 6 = (h ^ 3) ^ 2 := by ring
      rw [this]; exact sq_nonneg _
    exact mul_pos hh2_pos (by linarith)
  have hWZ_lt : twoMulP 2 h * 4 < twoMulP 3 h * q2 ^ 2 := sub_pos.mp hgap_pos
  have hr_gt1 : 1 < plancherelZWRatio h q2 := by
    unfold plancherelZWRatio
    exact (one_lt_div hW_pos).mpr hWZ_lt
  have hcos_pos : 0 < plancherelCosSq h q2 := by
    unfold plancherelCosSq
    exact div_pos (pow_pos hW_pos 2) (pow_pos hZ_pos 2)
  have hcos_lt1 : plancherelCosSq h q2 < 1 := by
    unfold plancherelCosSq
    rw [div_lt_one (pow_pos hZ_pos 2)]
    have hdiff_sq :
        (twoMulP 3 h * q2 ^ 2) ^ 2 - (twoMulP 2 h * 4) ^ 2 =
          (twoMulP 3 h * q2 ^ 2 - twoMulP 2 h * 4) *
            (twoMulP 3 h * q2 ^ 2 + twoMulP 2 h * 4) := by ring
    have hsq_pos : 0 < (twoMulP 3 h * q2 ^ 2) ^ 2 - (twoMulP 2 h * 4) ^ 2 := by
      rw [hdiff_sq]
      exact mul_pos hgap_pos (by linarith)
    linarith
  unfold plancherelSinSq
  exact ⟨hr_gt1, by linarith, by linarith⟩

/-- **Strict Positivity of `derivedHiggsQuartic` & Global Higgs Potential Stability:**
Whenever `0 < piAlpha`, `0 < vSq`, `0 < oneSubDeltaR`, `0 < q`, `q - q⁻¹ ≠ 0`, and `cLoop ≠ 0`,
the scale-free QOU Higgs quartic `λ_H` is strictly positive (`0 < λ_H`) and the quartic Higgs
potential `higgsPotential (λ_H * vSq) λ_H phiSq` attains its unique strict global minimum on
`Φ†Φ = phiSq` at `phiSq = vSq / 2`. -/
theorem derived_higgs_quartic_pos_and_vacuum_stable
    (piAlpha vSq oneSubDeltaR q cLoop : K)
    (hpa : 0 < piAlpha) (hvSq : 0 < vSq) (hdr : 0 < oneSubDeltaR)
    (hq_pos : 0 < q) (hh : q - q⁻¹ ≠ 0) (hcl : cLoop ≠ 0) :
    let h := q - q⁻¹
    let q2 := q + q⁻¹
    let sinSq := plancherelSinSq h q2
    let lamH := derivedHiggsQuartic piAlpha sinSq oneSubDeltaR h q2 cLoop
    0 < lamH ∧
    higgsPotential (lamH * vSq) lamH (vSq / 2) < higgsPotential (lamH * vSq) lamH 0 ∧
    (∀ phiSq : K,
      higgsPotential (lamH * vSq) lamH (vSq / 2) ≤ higgsPotential (lamH * vSq) lamH phiSq) ∧
    (∀ phiSq : K,
      higgsPotential (lamH * vSq) lamH phiSq = higgsPotential (lamH * vSq) lamH (vSq / 2) ↔
        phiSq = vSq / 2) := by
  intro h q2 sinSq lamH
  have hq_ne : q ≠ 0 := ne_of_gt hq_pos
  have hsin_pos : 0 < sinSq := (plancherel_sinSq_mem_unit_interval q hq_ne hh).2.1
  obtain ⟨hP2_pos, _, hP4_pos⟩ := twoMulP_pos_of_ordered h
  have hq2_pos : 0 < q2 := add_pos hq_pos (inv_pos.mpr hq_pos)
  have hfac_ne : (twoMulP 4 h / twoMulP 2 h) * (6 / 5) * (q2 / 2) * cLoop ≠ 0 := by
    have h65 : (6 / 5 : K) ≠ 0 := div_ne_zero (by norm_num) (by norm_num)
    have hq22 : q2 / 2 ≠ 0 := div_ne_zero (ne_of_gt hq2_pos) (by norm_num)
    exact mul_ne_zero
      (mul_ne_zero (mul_ne_zero (div_ne_zero (ne_of_gt hP4_pos) (ne_of_gt hP2_pos)) h65) hq22) hcl
  have hlam_pos : 0 < lamH := by
    dsimp only [lamH, derivedHiggsQuartic]
    have hden_pos : 0 < 2 * sinSq * oneSubDeltaR := by positivity
    exact mul_pos (div_pos hpa hden_pos) (sq_pos_of_ne_zero hfac_ne)
  have hstab := higgsPotential_unique_global_min_of_pos_quartic lamH vSq hlam_pos hvSq
  exact ⟨hlam_pos, hstab.2.1, hstab.2.2.1, hstab.2.2.2⟩

end OrderedFieldBounds

/-! ## Section 3: Non-Vacuous `§3b-cond` Hypothesis Class & `trivialModel` Consistency Witness (`ℝ`) -/

section ConditionalElectroweakThresholdBridge

/-- **Conjecture Carrier (`§3b-cond`, Content-Bearing, Zero Global Instances)**:
Packages the coupled working-assumption electroweak threshold system at substrate modulus `q > 1`:
1. `α_em > 0` satisfies the two-loop Bring–Schwinger fixed-point equation (`AlphaEmTwoLoopBlochSchwinger`);
2. `α_v > 0` satisfies the Bring Seifert–Hodge + 1-loop Schwinger weak-VEV equation (`v = m_p / α_v`);
3. `(M_W², M_Z², m_H², λ_H)` are generated from `(π α_em, v, plancherelSinSq, 1 - Δr, c_loop)` with
   `Δr < 1` and `c_loop > 0` (zero empirical `M_W`, `M_Z`, or `m_H` inputs). -/
class ElectroweakBosonThresholdSystemClass
    (q delta_B3 α_em α_v m_p delta_r c_loop : ℝ) : Prop where
  /-- Hyperbolic real-`q` substrate regime `q > 1`. -/
  one_lt_q : 1 < q
  /-- Non-negative weight-3 Bloch-`B₃` trilogarithm defect `Δ_{B₃}(q) ≥ 0`. -/
  delta_B3_nonneg : 0 ≤ delta_B3
  /-- Strictly positive electromagnetic coupling `α_em > 0`. -/
  alpha_em_pos : 0 < α_em
  /-- Strictly positive inverse weak-crossing coupling `α_v = m_p / v > 0`. -/
  alpha_v_pos : 0 < α_v
  /-- Strictly positive derived proton scale `m_p(q) > 0`. -/
  mp_pos : 0 < m_p
  /-- Perturbative radiative Sirlin dressing remains below the pole (`Δr < 1`). -/
  delta_r_lt_one : delta_r < 1
  /-- Strictly positive 1-loop Higgs topological dressing factor `c_loop > 0`. -/
  c_loop_pos : 0 < c_loop
  /-- Two-loop Bring–Schwinger electromagnetic fixed-point equation holds. -/
  em_fixed_point :
    IsTwoLoopBringFixedPoint
      (q * qIntBal q 9 * qIntBal q 10)
      4
      q
      ((hHecke q) ^ 2)
      (habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4)))
      α_em
  /-- Electroweak Bring zero-mode + 1-loop Schwinger VEV fixed-point equation holds. -/
  ew_vev_fixed_point : IsElectroweakVevFixedPoint q α_v

/-- **Master Conditional Electroweak Threshold Theorem (`§3b-cond`)**:
Under `[ElectroweakBosonThresholdSystemClass q delta_B3 α_em α_v m_p delta_r c_loop]`:
- both characteristic Bring–Schwinger cubics (`twoLoopBringCubic` and `ewFixedPointCubic`) vanish;
- `0 < sin² θ_W^Planch(q) < 1`;
- `m_H^(W)` and `m_H^(Z)` from derived `(M_W, M_Z)` have **identically zero** anchor spread;
- `λ_H = m_H² / (2 v²)` is strictly positive and independent of `m_p` and `v = m_p / α_v`. -/
theorem electroweak_boson_thresholds_master
    (q delta_B3 α_em α_v m_p delta_r c_loop : ℝ)
    [inst : ElectroweakBosonThresholdSystemClass q delta_B3 α_em α_v m_p delta_r c_loop] :
    let h := q - q⁻¹
    let q2 := q + q⁻¹
    let v := m_p / α_v
    let sinSq := plancherelSinSq h q2
    let oneSubDr := 1 - delta_r
    twoLoopBringCubic
      (q * qIntBal q 9 * qIntBal q 10)
      4 q ((hHecke q) ^ 2)
      (habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4))) α_em = 0 ∧
    ewFixedPointCubic q α_v = 0 ∧
    (0 < sinSq ∧ sinSq < 1) ∧
    (∀ mW : ℝ,
      derivedHiggsFromW mW h q2 c_loop =
        derivedHiggsFromZ (mW * plancherelZWRatio h q2) h q2 c_loop) ∧
    derivedHiggsSq (Real.pi * α_em) v sinSq oneSubDr h q2 c_loop / (2 * v ^ 2) =
      derivedHiggsQuartic (Real.pi * α_em) sinSq oneSubDr h q2 c_loop ∧
    0 < derivedHiggsQuartic (Real.pi * α_em) sinSq oneSubDr h q2 c_loop := by
  intro h q2 v sinSq oneSubDr
  have hq_pos : 0 < q := lt_trans zero_lt_one inst.one_lt_q
  have hq_ne : q ≠ 0 := ne_of_gt hq_pos
  have hqi_lt1 : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ inst.one_lt_q
  have hh_pos : 0 < h := by dsimp only [h]; linarith [inst.one_lt_q]
  have hh_ne : h ≠ 0 := ne_of_gt hh_pos
  have hq2_pos : 0 < q2 := by
    dsimp only [q2]
    exact add_pos hq_pos (inv_pos.mpr hq_pos)
  have h1 :
      twoLoopBringCubic
        (q * qIntBal q 9 * qIntBal q 10)
        4 q ((hHecke q) ^ 2)
        (habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4))) α_em = 0 :=
    (twoLoopBringFixedPoint_iff_cubic _ _ _ _ _ α_em (ne_of_gt inst.alpha_em_pos)).mp
      inst.em_fixed_point
  have h2 : ewFixedPointCubic q α_v = 0 :=
    (ewFixedPoint_iff_cubic q α_v (ne_of_gt inst.alpha_v_pos)).mp inst.ew_vev_fixed_point
  have hsin_bounds := (plancherel_sinSq_mem_unit_interval q hq_ne hh_ne).2
  obtain ⟨hP2_pos, hP3_pos, _⟩ := twoMulP_pos_of_ordered h
  have h4 : ∀ mW : ℝ,
      derivedHiggsFromW mW h q2 c_loop =
        derivedHiggsFromZ (mW * plancherelZWRatio h q2) h q2 c_loop := fun mW =>
    (derived_higgs_w_eq_z_zero_spread mW (mW * plancherelZWRatio h q2) h q2 c_loop rfl
      (ne_of_gt hP2_pos) (ne_of_gt hP3_pos) (ne_of_gt hq2_pos) (by norm_num) (by norm_num)).1
  have hv_pos : 0 < v := div_pos inst.mp_pos inst.alpha_v_pos
  have hdr_pos : 0 < oneSubDr := sub_pos.mpr inst.delta_r_lt_one
  have h5 := derived_higgs_quartic_vev_independent
    (Real.pi * α_em) v sinSq oneSubDr h q2 c_loop
    (ne_of_gt hv_pos) (ne_of_gt hsin_bounds.1) (ne_of_gt hdr_pos) (by norm_num)
  have hpa_pos : 0 < Real.pi * α_em := mul_pos Real.pi_pos inst.alpha_em_pos
  have h6 := (derived_higgs_quartic_pos_and_vacuum_stable
    (Real.pi * α_em) (v ^ 2) oneSubDr q c_loop
    hpa_pos (sq_pos_of_pos hv_pos) hdr_pos hq_pos hh_ne (ne_of_gt inst.c_loop_pos)).1
  exact ⟨h1, h2, hsin_bounds, h4, h5, h6⟩

/-- Existence of a positive root `α_v ∈ (0, 1]` for `a₃ * x³ - a₂ * x² + a₁ * x - 1 = 0` whenever
`0 ≤ a₃`, `a₂ < 1`, and `2 < a₁`. -/
theorem exists_pos_ew_cubic_root (a₃ a₂ a₁ : ℝ)
    (ha3 : 0 ≤ a₃) (ha2 : a₂ < 1) (ha1 : 2 < a₁) :
    ∃ r : ℝ, 0 < r ∧ a₃ * r ^ 3 - a₂ * r ^ 2 + a₁ * r - 1 = 0 := by
  let f : ℝ → ℝ := fun x => a₃ * x ^ 3 - a₂ * x ^ 2 + a₁ * x - 1
  have hcont : Continuous f := by continuity
  have hf0 : f 0 = -1 := by simp [f]
  have hf1 : 0 ≤ f 1 := by dsimp only [f]; linarith
  obtain ⟨r, hr_mem, hr_eq⟩ :=
    intermediate_value_Icc (zero_le_one' ℝ) hcont.continuousOn
      (by rw [hf0]; exact ⟨by norm_num, hf1⟩)
  have hr_pos : 0 < r := by
    rcases lt_or_eq_of_le hr_mem.1 with hlt | rfl
    · exact hlt
    · linarith [hf0, hr_eq]
  exact ⟨r, hr_pos, hr_eq⟩

/-- **Non-Vacuity / Consistency Witness (`def`, NEVER `instance` — `lean-generation` §5)**:
Constructs an explicit mathematical witness at `q = 2` inhabiting
`ElectroweakBosonThresholdSystemClass`, proving the coupled hypothesis class is consistent without
registering any global typeclass instance. -/
noncomputable def trivialModel :
    ∃ (q delta_B3 α_em α_v m_p delta_r c_loop : ℝ),
      ElectroweakBosonThresholdSystemClass q delta_B3 α_em α_v m_p delta_r c_loop := by
  let q : ℝ := 2
  let delta_B3 : ℝ := (Real.pi * firstBetti 4) * (hHecke q) ^ 2
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  have hb1_pos : 0 < firstBetti 4 := by unfold firstBetti; norm_num
  have hdelta_nonneg : 0 ≤ delta_B3 :=
    mul_nonneg (le_of_lt (mul_pos hπ_pos hb1_pos)) (sq_nonneg _)
  have hqbal_gt_two : ∀ n : ℕ, 2 ≤ n → 2 < qIntBal q n := by
    intro n hn
    rw [QOU.QInteger.qIntBal_def]
    dsimp only [q]
    rw [lt_div_iff₀ (by norm_num)]
    have hpow : (4 : ℝ) ≤ (2 : ℝ) ^ n := by
      calc (4 : ℝ) = (2 : ℝ) ^ 2 := by norm_num
      _ ≤ (2 : ℝ) ^ n := pow_le_pow_right₀ (by norm_num) hn
    have hinv : ((2 : ℝ)⁻¹) ^ n < 1 := pow_lt_one₀ (by norm_num) (by norm_num) (by omega)
    linarith
  -- 1. Positive root α_em of `IsTwoLoopBringFixedPoint` at `q = 2`
  let t_em_tree : ℝ := q * qIntBal q 9 * qIntBal q 10
  let c2 : ℝ := habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4))
  have hc3_zero : c2 - (hHecke q) ^ 2 * habiroNorm q = 0 := by
    dsimp only [c2, delta_B3]
    have hden : Real.pi * firstBetti 4 ≠ 0 := ne_of_gt (mul_pos hπ_pos hb1_pos)
    field_simp
    ring
  have hhab_nonneg : 0 ≤ habiroNorm q := by
    unfold habiroNorm
    apply div_nonneg
    · dsimp only [q]; norm_num
    · linarith
  have ht_em_pos : 0 < t_em_tree + (2 * (4 : ℝ)) / bringSurfaceArea := by
    apply add_pos
    · have h9 : 0 < qIntBal q 9 := lt_trans (by norm_num) (hqbal_gt_two 9 (by omega))
      have h10 : 0 < qIntBal q 10 := lt_trans (by norm_num) (hqbal_gt_two 10 (by omega))
      have hq_pos : 0 < q := by dsimp only [q]; norm_num
      dsimp only [t_em_tree]
      exact mul_pos (mul_pos hq_pos h9) h10
    · unfold bringSurfaceArea bringFundamentalTriangleArea
      apply div_pos (by norm_num)
      linarith
  obtain ⟨α_em, ⟨hα_em_pos, hα_em_root⟩, _⟩ :=
    exists_unique_pos_cubic_root 0 (habiroNorm q) (t_em_tree + (2 * (4 : ℝ)) / bringSurfaceArea)
      (le_refl 0) hhab_nonneg ht_em_pos
  have hem_fp :
      IsTwoLoopBringFixedPoint t_em_tree 4 q ((hHecke q) ^ 2) c2 α_em := by
    rw [twoLoopBringFixedPoint_iff_cubic _ _ _ _ _ α_em (ne_of_gt hα_em_pos)]
    unfold twoLoopBringCubic
    rw [hc3_zero]
    exact hα_em_root
  -- 2. Positive root α_v of `IsElectroweakVevFixedPoint` at `q = 2`
  have hq2_val : qIntBal q 2 = 5 / 2 := by
    rw [QOU.QInteger.qIntBal_def]
    dsimp only [q]
    norm_num
  have ha2_nonneg : 0 ≤ ewHabiroNorm q := by
    unfold ewHabiroNorm
    rw [hq2_val]
    exact div_nonneg (by norm_num) (by linarith)
  have ha2_lt1 : ewHabiroNorm q < 1 := by
    unfold ewHabiroNorm
    have hpi2 : (2 : ℝ) ≤ Real.pi := Real.two_le_pi
    rw [hq2_val, div_lt_one (by linarith)]
    linarith
  have ha3_nonneg : 0 ≤ (ewHbarQ q) ^ 2 * ewHabiroNorm q :=
    mul_nonneg (sq_nonneg _) ha2_nonneg
  have ha1_gt2 : 2 < ewFixedPointConst q := by
    unfold ewFixedPointConst ewDressedTreeComplexity ewBareCrossingComplexity
    rw [ewBringZeroMode_eq_one_div_pi, hq2_val]
    have h4 : 2 < qIntBal q 4 := hqbal_gt_two 4 (by omega)
    have h6 : 2 < qIntBal q 6 := hqbal_gt_two 6 (by omega)
    have h8 : 2 < qIntBal q 8 := hqbal_gt_two 8 (by omega)
    have hq_eq : q = 2 := rfl
    have hm1 : 4 < q * qIntBal q 4 := by rw [hq_eq]; linarith
    have hm2 : 8 < q * qIntBal q 4 * qIntBal q 6 := by nlinarith
    have hm3 : 16 < q * qIntBal q 4 * qIntBal q 6 * qIntBal q 8 := by nlinarith
    have hz_pos : 0 < 1 / Real.pi := div_pos zero_lt_one hπ_pos
    linarith
  obtain ⟨α_v, hα_v_pos, hα_v_eq⟩ :=
    exists_pos_ew_cubic_root ((ewHbarQ q) ^ 2 * ewHabiroNorm q) (ewHabiroNorm q)
      (ewFixedPointConst q) ha3_nonneg ha2_lt1 ha1_gt2
  have hew_fp : IsElectroweakVevFixedPoint q α_v := by
    rw [ewFixedPoint_iff_cubic q α_v (ne_of_gt hα_v_pos)]
    exact hα_v_eq
  refine ⟨q, delta_B3, α_em, α_v, 1, 0, 1,
    ⟨by dsimp only [q]; norm_num, hdelta_nonneg, hα_em_pos, hα_v_pos,
      zero_lt_one, zero_lt_one, zero_lt_one, hem_fp, hew_fp⟩⟩

end ConditionalElectroweakThresholdBridge

end QOU.StandardModel
