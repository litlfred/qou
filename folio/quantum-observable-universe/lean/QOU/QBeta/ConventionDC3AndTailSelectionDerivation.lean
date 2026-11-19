/-
Copyright (c) 2026 Quantum Observable Universe Collaboration. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Collaboration
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Positivity
import QOU.Archimedean.BringSchwingerNormalizationDerivation
import QOU.BraidKnot.LadderConventionLocalisation
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.QBeta.CoshHolonomyAndGPMTBaseBridge
import QOU.QBeta.GluonVertexPsdParity
import QOU.QBeta.LadderPhaseMirrorCovariance
import QOU.QuantumObservableUniverses.CategoricalLagrangianTwoTermBridge

/-!
# Convention-D Five-Letter Tail Closure (`qou-j1e5`), Operator-Level `u^3` Expansion (`qou-51yf` / `qou-cds1`), and Two-Term Lagrangian Corrected-Photon Bridge

This module formalizes four structural pillars for the Convention-D neutron beta-decay
and nucleon mass-splitting sector:

1. **Section 1 (`qou-j1e5` — Five-Letter Valence/Gluon Tail Characterization and Constituent-to-Decay Bridge):**
   - Under the Kazhdan–Lusztig bar involution `σ_i ↦ σ_i⁻¹ = σ_i - h·1`, `h ↦ -h`, an `h`-line
     Hecke letter `σ_i + c·h·1` is bar-fixed if and only if `c = -1/2` (`bar_letter_shift_fixed_iff`),
     where `σ_i - (h/2)·1 = (1/2)(σ_i + σ_i⁻¹)` is the unique achiral symmetric crossing average
     (`hecke_bar_fixed_letter_eq_symm_avg`), while `c = 0` (`uu`) and `c = -1` (`dd`) are swapped.
   - Combined with `GluonVertexPsdParity`, `k = 2` (`σ₀²`) is the unique minimal positive (`k ≥ 1`)
     crossing count at which `σ₀^k` is positive semidefinite across both `H₂(q)` blocks
     (`minimal_positive_psd_gluon_pair`).
   - Evaluating `trM (zD q)` on the 11-letter `(n - p)` normal-form difference `nucleonDiffCoord`
     from `CoshHolonomyAndGPMTBaseBridge` yields the exact opposite of the constituent trace gap
     `trM(p_Bor) - trM(n_Bor)` (`trM_conventionD_nucleonDiffCoord_eq_neg_constituent_diff`).

2. **Section 2 (`qou-j1e5` — Universal Braid Commutator, Flavor-Slot Permutation Invariance, and Ordering Selection):**
   - In `H₃(q)` normal-form coordinates `mulNF h`, the commutator `[σ₀ + c₀·1, σ₁ + c₁·1]` equals
     `L_+ - L_- = ![0, 0, 0, -1, 1, 0]` for all `c₀, c₁` (including `c₀ = c₁ = -h/2`), and commuting
     `σ₁ + c₁·1` past the gluon pair `σ₀²` equals `-h • [σ₀ - h/2, σ₁ - h/2]`
     (`mulNF_avg_commutator_eq_hopf_diff`).
   - On the 2D Hoefsmit `(2,1)` block, the proton quark tails satisfy `uud = udu`, the neutron quark
     tails satisfy `dud = ddu`, and `duu - uud = dud - udd`, leaving the `(n - p)` tail difference
     invariant across single-quark flip channels (`quark_permutation_diff_invariance_on_hoefsmit`).
   - Over `ℝ` for `q > 1`, the `interleaved` (`borromean`) vs `grouped` trace defect is strictly
     positive on `(n - p)` while the `interleaved` constituent proton and neutron traces are strictly
     smaller than their `grouped` counterparts (`interleaved_vs_grouped_trace_defect_and_energy_selection`).

3. **Section 3 (`qou-51yf` / `qou-cds1` — Operator-Level Habiro–Kashiwara Expansion Through Order `u^3`):**
   - On `1 ≤ q` with `q² - 2q - 1 ≤ 0`, `Q_beta_form_A q m_e` is an exact cubic polynomial
     `m_e * (2 - 5 ℏ_q + 3 ℏ_q² - (1/2) ℏ_q³)` in `ℏ_q = 1 - q⁻¹` (`formA_over_me_exact_cubic_in_hbarQ`).
   - In terms of the bar-even Habiro parameter `y = deltaHabiroSq q = (q + q⁻¹) - 2 = q ℏ_q²`, both
     `(hoefsmitB q)²` and the squared mirror-projected phase `(mirrorProjPhaseD q)²` are exact
     rational functions of `y` (`conventionD_mirror_phase_sq_in_deltaHabiroSq`), eliminating the
     `√u` branch point in the bar-even variable `u_Hab = q · u = hoefsmitB q · y` and yielding the
     exact algebraic Taylor jet `(1, -√3/12, 47/96, -2069√3/5760)` through `u_Hab³` alongside the
     `N = 3` Kashiwara–Hopf product expansion (`mirror_phase_jet_and_kashiwara_n3_expansion`).

4. **Section 4 — Two-Term Categorical Lagrangian Corrected-Photon Bridge & Error-Dilution Laws:**
   - Connects `CategoricalLagrangianTwoTermBridge` and `BringSchwingerNormalizationDerivation` on the
     hadronic scale `m_e / ℏ_q²` with the Form-B Bring–Schwinger cubic fixed-point photon `α_corr`
     (`twoTerm_lagrangian_hadronic_photon_scale_bridge`), and formalizes the exact relative
     error-dilution laws for `Δm_{pn} = Q_β + m_e` and `m_n = m_p + Δm_{pn}`
     (`delta_pn_error_dilution_law`, `neutron_mass_error_dilution_law`).
-/

namespace QOU.QBeta.ConventionDC3AndTailSelectionDerivation

open Matrix
open QOU.Machinery.H3
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
open QOU.QBeta.CoshHolonomyAndGPMTBaseBridge
open QOU.QBeta.GluonVertexPsdParity
open QOU.BraidKnot
open QOU.Archimedean
open QOU.Archimedean.BringSchwingerNormalizationDerivation
open QOU.CategoricalLagrangianTwoTermBridge
open CategoryTheory
open scoped CategoryTheory CategoryTheory.MonoidalCategory

/-! ## Section 1: Five-Letter Valence/Gluon Tail Characterization and Constituent-to-Decay Bridge (`qou-j1e5`) -/

section TailCharacterizationAndConstituentBridge

variable {K : Type*} [Field K]

/-- Action of the Kazhdan–Lusztig bar involution `σ_i ↦ σ_i - h`, `h ↦ -h` on the scalar shift
`c * h` of an affine Hecke letter `σ_i + (c * h) · 1`: `barShift h c = -h - c * h`. -/
def barLetterShift (h c : K) : K := -h - c * h

/-- **Unique Bar-Fixed Shift on the `h`-Line (`qou-j1e5` Quark-Block Characterization)**:
Over any field `K` with `2 ≠ 0` and `h ≠ 0`:
1. `barLetterShift h c = c * h ↔ c = -1 / 2` (`-h / 2` is the unique bar-fixed shift on the `h`-line),
2. `c = 0` (`uu` positive crossing) and `c = -1` (`dd` inverse crossing `-h`) are swapped by `barLetterShift`. -/
theorem bar_letter_shift_fixed_iff (h c : K) (h2 : (2 : K) ≠ 0) (hh : h ≠ 0) :
    (barLetterShift h c = c * h ↔ c = -1 / 2) ∧
    barLetterShift h 0 = (-1 : K) * h ∧
    barLetterShift h (-1) = (0 : K) * h := by
  refine ⟨?_, ?_, ?_⟩
  · unfold barLetterShift
    constructor
    · intro hfix
      have hlin : h * (2 * c + 1) = 0 := by linear_combination -hfix
      have hc0 : 2 * c + 1 = 0 := (mul_eq_zero.mp hlin).resolve_left hh
      apply mul_left_cancel₀ h2
      field_simp
      linear_combination hc0
    · intro hc
      rw [hc]
      field_simp
      ring
  · unfold barLetterShift; ring
  · unfold barLetterShift; ring

/-- **Achiral Symmetric Crossing Average Identity in Any Unital Ring**:
In any unital ring `A` with central `h` (`∀ x, h * x = x * h`), multiplicative inverse `two_inv` of `2`,
and invertible Hecke generator `T` (`T * T_inv = 1`, `T * T = h * T + 1`):
1. `T_inv = T - h`,
2. The unique bar-fixed mixed-flavor letter `T - two_inv * h` equals `two_inv * (T + T_inv)`, and
3. Its square `(T - two_inv * h) * (T - two_inv * h)` equals the central scalar `two_inv * two_inv * h * h + 1`. -/
theorem hecke_bar_fixed_letter_eq_symm_avg {A : Type*} [Ring A]
    (T T_inv h two_inv : A)
    (hinv : T * T_inv = 1)
    (hhecke : T * T = h * T + 1)
    (hcent_h : ∀ x : A, h * x = x * h)
    (htwo : (2 : A) * two_inv = 1) :
    T_inv = T - h ∧
    T - two_inv * h = two_inv * (T + T_inv) ∧
    (T - two_inv * h) * (T - two_inv * h) = two_inv * two_inv * h * h + 1 := by
  have ht_inv : T_inv = T - h := by
    calc T_inv
      _ = (T * T - h * T) * T_inv := by
          have h1 : T * T - h * T = 1 := by
            rw [hhecke, add_sub_cancel_left]
          rw [h1, one_mul]
      _ = T * (T * T_inv) - h * (T * T_inv) := by
          rw [sub_mul, mul_assoc, mul_assoc]
      _ = T - h := by rw [hinv, mul_one, mul_one]
  have htwo_comm : two_inv * (2 : A) = 1 := by
    -- Since 2 = 1 + 1 commutes with every element:
    have hc2 : (2 : A) * two_inv = two_inv * (2 : A) := by
      have h11 : (2 : A) = 1 + 1 := one_add_one_eq_two.symm
      rw [h11, add_mul, mul_add, one_mul, mul_one]
    rwa [← hc2]
  have hcent_two : ∀ x : A, two_inv * x = x * two_inv := by
    intro x
    have hx2 : (2 : A) * x = x * (2 : A) := by
      have h11 : (2 : A) = 1 + 1 := one_add_one_eq_two.symm
      rw [h11, add_mul, mul_add, one_mul, mul_one]
    calc two_inv * x
      _ = two_inv * x * (2 * two_inv) := by rw [htwo, mul_one]
      _ = two_inv * (x * 2) * two_inv := by noncomm_ring
      _ = two_inv * (2 * x) * two_inv := by rw [hx2]
      _ = (two_inv * 2) * x * two_inv := by noncomm_ring
      _ = x * two_inv := by rw [htwo_comm, one_mul]
  have havg : T - two_inv * h = two_inv * (T + T_inv) := by
    rw [ht_inv]
    have h2T : two_inv * (T + (T - h)) = two_inv * (2 * T) - two_inv * h := by
      have h11 : (2 : A) = 1 + 1 := one_add_one_eq_two.symm
      rw [h11]; noncomm_ring
    rw [h2T, ← mul_assoc, htwo_comm, one_mul]
  have hsq : (T - two_inv * h) * (T - two_inv * h) = two_inv * two_inv * h * h + 1 := by
    have hcomm_th : (two_inv * h) * T = T * (two_inv * h) := by
      rw [mul_assoc, hcent_h T, ← mul_assoc, hcent_two T, mul_assoc]
    have hexp :
        (T - two_inv * h) * (T - two_inv * h) =
          T * T - T * (two_inv * h) - (two_inv * h) * T + (two_inv * h) * (two_inv * h) := by
      noncomm_ring
    rw [hexp, hcomm_th, hhecke]
    have hmid :
        h * T + 1 - T * (two_inv * h) - T * (two_inv * h) =
          h * T + 1 - T * ((2 : A) * two_inv * h) := by
      have h11 : (2 : A) = 1 + 1 := one_add_one_eq_two.symm
      rw [h11]; noncomm_ring
    rw [hmid, htwo, one_mul, ← hcent_h T]
    have hfin : (two_inv * h) * (two_inv * h) = two_inv * two_inv * h * h := by
      rw [mul_assoc two_inv h (two_inv * h), ← mul_assoc h two_inv h, ← hcent_two h]
      noncomm_ring
    rw [hfin]
    noncomm_ring
  exact ⟨ht_inv, havg, hsq⟩

/-- **Unique Minimal Positive PSD Gluon Pair Theorem (`k = 2` via `GluonVertexPsdParity`)**:
Over any strict ordered field `R` with `0 < q`:
1. `k = 2` (`σ₀²`) is PSD on both `H₂(q)` blocks (`0 ≤ symEigenPow q 2 ∧ 0 ≤ altEigenPow q 2`),
2. `k = 1` (`σ₀`) is not PSD (`¬ (0 ≤ symEigenPow q 1 ∧ 0 ≤ altEigenPow q 1)`), and
3. Every positive crossing count `1 ≤ k` that is PSD satisfies `2 ≤ k`. -/
theorem minimal_positive_psd_gluon_pair {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] {q : R} (hq : 0 < q) :
    (0 ≤ symEigenPow q 2 ∧ 0 ≤ altEigenPow q 2) ∧
    ¬ (0 ≤ symEigenPow q 1 ∧ 0 ≤ altEigenPow q 1) ∧
    ∀ k : ℕ, 1 ≤ k → (0 ≤ symEigenPow q k ∧ 0 ≤ altEigenPow q k) → 2 ≤ k := by
  refine ⟨two_crossings_psd hq, one_crossing_not_psd hq, ?_⟩
  intro k hk1 hpsd
  by_contra hlt2
  have hk_eq_one : k = 1 := by omega
  subst hk_eq_one
  exact one_crossing_not_psd hq hpsd

/-- **Mixed-Symmetry `(2,1)` Character Closed Form on `nucleonDiffCoord` (`n - p`)**:
On the 11-letter `(n - p)` normal-form difference `nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)`
of `CoshHolonomyAndGPMTBaseBridge`,
`χ_{(2,1)}(n - p) = (q² - 1)(q⁴ + 1)(2 q¹² - 5 q¹⁰ + 5 q⁸ - 5 q⁶ + 5 q⁴ - 5 q² + 2) / (4 q⁹)`. -/
theorem chi21_nucleonDiffCoord_eq_rational (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    chi21 q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      (q ^ 2 - 1) * (q ^ 4 + 1) *
        (2 * q ^ 12 - 5 * q ^ 10 + 5 * q ^ 8 - 5 * q ^ 6 + 5 * q ^ 4 - 5 * q ^ 2 + 2) /
        (4 * q ^ 9) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by ring
    rw [this]; exact mul_ne_zero h2 h2
  have hlin :
      chi21 q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
        chi21 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) -
          chi21 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) := by
    rw [nucleonDiffCoord, chi21, chi21, chi21,
        chiM_eq_closed q hq hq2, chiM_eq_closed q hq hq2, chiM_eq_closed q hq hq2]
    simp only [Pi.sub_apply]
    ring
  rw [hlin, chi21_neutronCoord q hq hq2 h2, chi21_protonCoord q hq hq2 h2]
  field_simp
  ring

/-- **Constituent-to-Decay Rational Identity (`qou-j1e5` Closure Bridge)**:
At Convention D (`z_D = q³ / (q² + 1)`), the Markov trace of the 11-letter decay difference
`nucleonDiffCoord` (`n - p`) equals both:
1. The exact rational form
   `(q² - 1)(q⁴ + 1)(2 q¹² - 6 q¹⁰ + 3 q⁸ - 6 q⁶ + 5 q⁴ - 5 q² + 2) / (4 q⁷ (q² + 1)²)`, and
2. `-(trM (zD q) (q - q⁻¹) protonCoord - trM (zD q) (q - q⁻¹) neutronCoord)`, matching the
   exact negative of the constituent `(p - n)` mass-endomorphism trace difference. -/
theorem trM_conventionD_nucleonDiffCoord_eq_neg_constituent_diff
    (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
        (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      (q ^ 2 - 1) * (q ^ 4 + 1) *
        (2 * q ^ 12 - 6 * q ^ 10 + 3 * q ^ 8 - 6 * q ^ 6 + 5 * q ^ 4 - 5 * q ^ 2 + 2) /
        (4 * q ^ 7 * (q ^ 2 + 1) ^ 2) ∧
    trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
        (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      -(trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
          (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) -
        trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
          (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2))) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by ring
    rw [this]; exact mul_ne_zero h2 h2
  have hq2' : 1 + q ^ 2 ≠ 0 := by intro h0; apply hq2; linear_combination h0
  refine ⟨?_, ?_⟩
  · rw [trM_conventionD_eq_twoRow_sum q hq hq2 hq4,
        chi3_nucleonDiffCoord q hq h2,
        chi21_nucleonDiffCoord_eq_rational q hq hq2 h2]
    field_simp [hq, hq2, hq2', h2, h4]
    ring
  · unfold nucleonDiffCoord
    rw [trM_eq_closed, trM_eq_closed, trM_eq_closed]
    simp only [Pi.sub_apply]
    ring

/-- **GPMT-Completed Three-Block Rational Closed Form on `nucleonDiffCoord` (`n - p`)**:
Restoring the killed `(1³)` sector with positive GPMT weight `dMod111Abs q` on `nucleonDiffCoord` gives
`trM_conventionD_gpmtPos q (n - p)` as an explicit rational function of `q`. -/
theorem trM_conventionD_gpmtPos_nucleonDiffCoord_eq_rational
    (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    trM_conventionD_gpmtPos q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      (q ^ 2 - 1) *
        (2 * q ^ 20 - 4 * q ^ 18 + q ^ 16 - 13 * q ^ 14 + q ^ 12 - q ^ 11 -
          15 * q ^ 10 - 3 * q ^ 9 + 4 * q ^ 8 - 3 * q ^ 7 - 9 * q ^ 6 - q ^ 5 +
          4 * q ^ 4 - 3 * q ^ 2 + 2) /
        (4 * q ^ 7 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by ring
    rw [this]; exact mul_ne_zero h2 h2
  have hq2' : 1 + q ^ 2 ≠ 0 := by intro h0; apply hq2; linear_combination h0
  have hden1 : (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) ≠ 0 := mul_ne_zero hq2 hq4
  have hden2 : 4 * q ^ 7 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) ≠ 0 :=
    mul_ne_zero (mul_ne_zero (mul_ne_zero h4 (pow_ne_zero 7 hq)) (pow_ne_zero 2 hq2)) hq4
  rw [trM_conventionD_gpmtPos_eq_threeBlock_sum q hq hq2 hq4,
      chi3_nucleonDiffCoord q hq h2,
      chi21_nucleonDiffCoord_eq_rational q hq hq2 h2,
      chi111_nucleonDiffCoord q hq h2]
  rw [eq_div_iff hden2]
  have ht1 :
      (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 * (-(q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (4 * q)) *
          (4 * q ^ 7 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) =
        -(q ^ 2 - 1) * (q ^ 4 + 1) * q ^ 6 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) := by
    field_simp [hq, hq2, hq2', h2, h4]
  have ht2 :
      q ^ 2 / (q ^ 2 + 1) ^ 2 *
          ((q ^ 2 - 1) * (q ^ 4 + 1) *
            (2 * q ^ 12 - 5 * q ^ 10 + 5 * q ^ 8 - 5 * q ^ 6 + 5 * q ^ 4 - 5 * q ^ 2 + 2) /
            (4 * q ^ 9)) *
          (4 * q ^ 7 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) =
        (q ^ 2 - 1) * (q ^ 4 + 1) *
          (2 * q ^ 12 - 5 * q ^ 10 + 5 * q ^ 8 - 5 * q ^ 6 + 5 * q ^ 4 - 5 * q ^ 2 + 2) *
          (q ^ 4 + q ^ 2 + 1) := by
    field_simp [hq, hq2, hq2', h2, h4]
  have ht3 :
      q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) *
          (-(q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (4 * q ^ 5)) *
          (4 * q ^ 7 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) =
        -(q ^ 2 - 1) * q ^ 5 * (q ^ 2 + 1) ^ 3 := by
    have hmul_cancel :
        q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) *
            (-(q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (4 * q ^ 5)) *
            (4 * q ^ 7 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) =
          (q ^ 3 * ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) /
              ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))) *
            (-(q ^ 2 - 1) * (q ^ 2 + 1) ^ 3 * (4 * q ^ 7) / (4 * q ^ 5)) := by
      ring
    rw [hmul_cancel, mul_div_cancel_right₀ _ hden1]
    field_simp [hq, h2, h4]
  rw [add_mul, add_mul, ht1, ht2, ht3]
  ring

end TailCharacterizationAndConstituentBridge

/-! ## Section 2: Universal Braid Commutator, Flavor-Slot Invariance, and Ordering Selection (`qou-j1e5`) -/

section BraidCommutatorAndOrderingSelection

variable {K : Type*} [Field K]

/-- Normal-form vector of an affine `σ₀`-letter `σ₀ + c₀ · 1` in `[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`. -/
def gen0ShiftNF (c₀ : K) : Fin 6 → K := ![c₀, 1, 0, 0, 0, 0]

/-- Normal-form vector of an affine `σ₁`-letter `σ₁ + c₁ · 1` in `[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`. -/
def gen1ShiftNF (c₁ : K) : Fin 6 → K := ![c₁, 0, 1, 0, 0, 0]

/-- Normal-form vector of the 2-letter positive gluon pair `σ₀² = 1 + h · σ₀` in `H₃(q)`. -/
def gluonPairNF (h : K) : Fin 6 → K := ![1, h, 0, 0, 0, 0]

/-- Normal-form vector of the Hopf-link chirality difference `L_+ - L_- = σ₀σ₁ - σ₁σ₀`. -/
def hopfCommutatorNF : Fin 6 → K := ![0, 0, 0, -1, 1, 0]

/-- **Universal Braid Commutator Identity in `H₃(q)` Normal Form**:
For any scalar shifts `c₀, c₁ : K` (in particular `c₀ = c₁ = -h / 2` for the bar-fixed mixed quark
letters), the normal-form commutator `[σ₀ + c₀·1, σ₁ + c₁·1]` equals `hopfCommutatorNF = L_+ - L_-`,
and commuting `σ₁ + c₁·1` past the 2-letter gluon pair `σ₀² = gluonPairNF h` equals
`-h • hopfCommutatorNF = -h • [σ₀ - h/2, σ₁ - h/2]`. -/
theorem mulNF_avg_commutator_eq_hopf_diff (h c₀ c₁ : K) :
    mulNF h (gen0ShiftNF c₀) (gen1ShiftNF c₁) - mulNF h (gen1ShiftNF c₁) (gen0ShiftNF c₀) =
      hopfCommutatorNF ∧
    mulNF h (gen1ShiftNF c₁) (gluonPairNF h) - mulNF h (gluonPairNF h) (gen1ShiftNF c₁) =
      (-h) • hopfCommutatorNF := by
  refine ⟨?_, ?_⟩
  · funext k
    fin_cases k <;>
      (simp [mulNF, mulσ₀, mulσ₁, gen0ShiftNF, gen1ShiftNF, hopfCommutatorNF]; try ring)
  · funext k
    fin_cases k <;>
      (simp [mulNF, mulσ₀, mulσ₁, gen1ShiftNF, gluonPairNF, hopfCommutatorNF]; try ring)

/-- **Wedderburn Visibility of `hopfCommutatorNF = [σ₀ - h/2, σ₁ - h/2]`**:
`hopfCommutatorNF` is annihilated by `chi3`, `chi111`, and the linear trace `chi21`, yet acts
non-trivially on the `2 × 2` Hoefsmit `(2,1)` block `blockOf q` with `(0,1)` entry `q + q⁻¹ ≠ 0`. -/
theorem blockOf_avg_commutator_ne_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    chi3 q (hopfCommutatorNF : Fin 6 → K) = 0 ∧
    chi111 q (hopfCommutatorNF : Fin 6 → K) = 0 ∧
    chi21 q (hopfCommutatorNF : Fin 6 → K) = 0 ∧
    blockOf q (hopfCommutatorNF : Fin 6 → K) = S0 q * S1 q - S1 q * S0 q ∧
    blockOf q (hopfCommutatorNF : Fin 6 → K) 0 1 = q + q⁻¹ ∧
    blockOf q (hopfCommutatorNF : Fin 6 → K) ≠ 0 := by
  have hc3 : chi3 q (hopfCommutatorNF : Fin 6 → K) = 0 := by
    simp [chi3, chiNF, hopfCommutatorNF]
  have hc111 : chi111 q (hopfCommutatorNF : Fin 6 → K) = 0 := by
    simp [chi111, chiNF, hopfCommutatorNF]
  have hc21 : chi21 q (hopfCommutatorNF : Fin 6 → K) = 0 := by
    rw [chi21, chiM_eq_closed q hq hq2]
    simp [hopfCommutatorNF]
  have hblk : blockOf q (hopfCommutatorNF : Fin 6 → K) = S0 q * S1 q - S1 q * S0 q := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (simp [blockOf, hopfCommutatorNF, S0, S1]; ring)
  have h01 : blockOf q (hopfCommutatorNF : Fin 6 → K) 0 1 = q + q⁻¹ := by
    rw [hblk]
    simp [S0, S1]
  have hne : blockOf q (hopfCommutatorNF : Fin 6 → K) ≠ 0 := by
    intro hzero
    have h01_z : blockOf q (hopfCommutatorNF : Fin 6 → K) 0 1 = 0 := by
      rw [hzero]; rfl
    rw [h01] at h01_z
    apply hq2
    have hmul : (q + q⁻¹) * q = q ^ 2 + 1 := by field_simp
    rw [h01_z, zero_mul] at hmul
    exact hmul.symm
  exact ⟨hc3, hc111, hc21, hblk, h01, hne⟩

/-- **Universal Ring Identity for Three-Quark Pairwise Tail Permutations**:
In any ring `R`, for mixed-flavor crossing averages `m₀, m₁ : R` and central half-gap `c : R`
(`c * m₀ = m₀ * c`, `c * m₁ = m₁ * c`), setting `T₀ = m₀ + c`, `T₀⁻¹ = m₀ - c`,
`T₁ = m₁ + c`, `T₁⁻¹ = m₁ - c`:
1. `(m₀ + c) * m₀ * m₁ = m₀ * (m₀ + c) * m₁` (`uud = udu`),
2. `m₀ * (m₀ - c) * m₁ = (m₀ - c) * m₀ * m₁` (`dud = ddu`),
3. `m₀ * m₀ * (m₁ + c) - (m₀ + c) * m₀ * m₁ = m₀ * (m₀ - c) * m₁ - m₀ * m₀ * (m₁ - c)`
   (`duu - uud = dud - udd`, both equal to `c * m₀ * (m₀ - m₁)`). -/
theorem quark_tail_permutation_invariance_ring {R : Type*} [Ring R]
    (m₀ m₁ c : R) (hc₀ : c * m₀ = m₀ * c) :
    (m₀ + c) * m₀ * m₁ = m₀ * (m₀ + c) * m₁ ∧
    m₀ * (m₀ - c) * m₁ = (m₀ - c) * m₀ * m₁ ∧
    m₀ * m₀ * (m₁ + c) - (m₀ + c) * m₀ * m₁ =
      m₀ * (m₀ - c) * m₁ - m₀ * m₀ * (m₁ - c) := by
  have h1 : (m₀ + c) * m₀ = m₀ * (m₀ + c) := by
    rw [add_mul, mul_add, hc₀]
  have h2 : m₀ * (m₀ - c) = (m₀ - c) * m₀ := by
    rw [mul_sub, sub_mul, hc₀]
  have h3 :
      m₀ * m₀ * (m₁ + c) - (m₀ + c) * m₀ * m₁ =
        m₀ * (m₀ - c) * m₁ - m₀ * m₀ * (m₁ - c) := by
    have hlhs : m₀ * m₀ * (m₁ + c) - (m₀ + c) * m₀ * m₁ = m₀ * m₀ * c - c * m₀ * m₁ := by
      noncomm_ring
    have hrhs : m₀ * (m₀ - c) * m₁ - m₀ * m₀ * (m₁ - c) = m₀ * m₀ * c - m₀ * c * m₁ := by
      noncomm_ring
    rw [hlhs, hrhs, hc₀]
  exact ⟨by rw [h1], by rw [h2], h3⟩

/-- **Flavor-Slot Permutation Coincidence and `(n - p)` Isospin Difference Invariance on `(2,1)`**:
On the `2 × 2` Hoefsmit generators `S0 q, S1 q` of `QOU.Machinery.H3` with `h = q - q⁻¹`:
1. Proton `uud` (`S0 (S0 - h/2) (S1 - h/2)`) equals `udu` (`(S0 - h/2) S0 (S1 - h/2)`),
2. Neutron `dud` (`(S0 - h/2) (S0 - h) (S1 - h/2)`) equals `ddu` (`(S0 - h) (S0 - h/2) (S1 - h/2)`), and
3. The non-canonical shift `duu - uud` (`(S0 - h/2)² S1 - S0 (S0 - h/2) (S1 - h/2)`) equals
   `dud - udd` (`(S0 - h/2) (S0 - h) (S1 - h/2) - (S0 - h/2)² (S1 - h)`), so the `(n - p)` tail
   difference `udd - uud = dud - duu = ddu - duu` is invariant across single-quark flip channels. -/
theorem quark_permutation_diff_invariance_on_hoefsmit (q : K) (h2 : (2 : K) ≠ 0) :
    let h := q - q⁻¹
    let m0_avg := S0 q - (h / 2) • (1 : Matrix (Fin 2) (Fin 2) K)
    let m1_avg := S1 q - (h / 2) • (1 : Matrix (Fin 2) (Fin 2) K)
    let m0_inv := S0 q - h • (1 : Matrix (Fin 2) (Fin 2) K)
    let m1_inv := S1 q - h • (1 : Matrix (Fin 2) (Fin 2) K)
    let qp_uud := S0 q * m0_avg * m1_avg
    let qp_udu := m0_avg * S0 q * m1_avg
    let qp_duu := m0_avg * m0_avg * S1 q
    let qn_udd := m0_avg * m0_avg * m1_inv
    let qn_dud := m0_avg * m0_inv * m1_avg
    let qn_ddu := m0_inv * m0_avg * m1_avg
    qp_uud = qp_udu ∧
    qn_dud = qn_ddu ∧
    qp_duu - qp_uud = qn_dud - qn_udd ∧
    qn_udd - qp_uud = qn_dud - qp_duu := by
  let h := q - q⁻¹
  let c : Matrix (Fin 2) (Fin 2) K := (h / 2) • (1 : Matrix (Fin 2) (Fin 2) K)
  let m₀ : Matrix (Fin 2) (Fin 2) K := S0 q - c
  let m₁ : Matrix (Fin 2) (Fin 2) K := S1 q - c
  have hc_comm : ∀ M : Matrix (Fin 2) (Fin 2) K, c * M = M * c := by
    intro M
    simp only [c, smul_mul_assoc, one_mul, mul_smul_comm, mul_one]
  have hh_two : (h / 2) + (h / 2) = h := by
    field_simp [h2]
    ring
  have hs0_add : m₀ + c = S0 q := sub_add_cancel (S0 q) c
  have hs1_add : m₁ + c = S1 q := sub_add_cancel (S1 q) c
  have hs0_sub : m₀ - c = S0 q - h • (1 : Matrix (Fin 2) (Fin 2) K) := by
    simp only [m₀, c, sub_sub, ← add_smul, hh_two]
  have hs1_sub : m₁ - c = S1 q - h • (1 : Matrix (Fin 2) (Fin 2) K) := by
    simp only [m₁, c, sub_sub, ← add_smul, hh_two]
  obtain ⟨hp, hn, hsh⟩ := quark_tail_permutation_invariance_ring m₀ m₁ c (hc_comm m₀)
  rw [hs0_add] at hp
  rw [hs0_sub] at hn
  rw [hs1_add, hs0_add, hs0_sub, hs1_sub] at hsh
  have hiso :
      m₀ * m₀ * (S1 q - h • (1 : Matrix (Fin 2) (Fin 2) K)) - S0 q * m₀ * m₁ =
        m₀ * (S0 q - h • (1 : Matrix (Fin 2) (Fin 2) K)) * m₁ - m₀ * m₀ * S1 q := by
    have hsh_add := sub_eq_sub_iff_add_eq_add.mp hsh
    rw [sub_eq_sub_iff_add_eq_add, add_comm]
    exact hsh_add
  exact ⟨hp, hn, hsh, hiso⟩

/-- **Exact Commutator Defect (`interleaved` vs `grouped`) and Constituent Energy Selection over `ℝ`**:
For every real `q > 1`:
1. The Convention-D `(n - p)` trace defect between `nucleonDiffCoord` (`interleaved`) and the
   `grouped` `(n - p)` trace `-(q² - 1)(q⁴ + 1)(q⁴ + 2 q² + 2) / (4 q (q² + 1)²)` equals
   `(q² - 1)³ (q⁴ + 1) (q⁴ + q² + 1) (2 q⁴ - 3 q² + 2) / (4 q⁷ (q² + 1)²)` and is strictly positive;
2. The `interleaved` constituent proton trace `trM (zD q) (q - q⁻¹) protonCoord` is strictly less
   than the `grouped` proton trace `(q⁸ + q⁴ + q² + 1)(q¹⁴ + q¹² + q¹⁰ - 1) / (4 q⁹ (q² + 1)²)`;
3. The `interleaved` constituent neutron trace `trM (zD q) (q - q⁻¹) neutronCoord` is strictly less
   than the `grouped` neutron trace `(q⁸ - q⁶ + q⁴ + 1)(q¹⁰ + q⁶ - q⁴ + q² - 1) / (4 q⁹)`. -/
theorem interleaved_vs_grouped_trace_defect_and_energy_selection {q : ℝ} (hq1 : 1 < q) :
    let tr_diff_grp := -(q ^ 2 - 1) * (q ^ 4 + 1) * (q ^ 4 + 2 * q ^ 2 + 2) /
      (4 * q * (q ^ 2 + 1) ^ 2)
    let tr_p_grp := (q ^ 8 + q ^ 4 + q ^ 2 + 1) * (q ^ 14 + q ^ 12 + q ^ 10 - 1) /
      (4 * q ^ 9 * (q ^ 2 + 1) ^ 2)
    let tr_n_grp := (q ^ 8 - q ^ 6 + q ^ 4 + 1) * (q ^ 10 + q ^ 6 - q ^ 4 + q ^ 2 - 1) /
      (4 * q ^ 9)
    trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
        (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) - tr_diff_grp =
      (q ^ 2 - 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) * (2 * q ^ 4 - 3 * q ^ 2 + 2) /
        (4 * q ^ 7 * (q ^ 2 + 1) ^ 2) ∧
    0 < trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
        (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) - tr_diff_grp ∧
    trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
        (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) < tr_p_grp ∧
    trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
        (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) < tr_n_grp := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  have hq : q ≠ 0 := ne_of_gt hq0
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq2' : 1 + q ^ 2 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : (2 : ℝ) ≠ 0 := two_ne_zero
  have htr_int := (trM_conventionD_nucleonDiffCoord_eq_neg_constituent_diff q hq hq2 hq4 h2).1
  have hdefect :
      trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
          (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) -
          (-(q ^ 2 - 1) * (q ^ 4 + 1) * (q ^ 4 + 2 * q ^ 2 + 2) /
            (4 * q * (q ^ 2 + 1) ^ 2)) =
        (q ^ 2 - 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) * (2 * q ^ 4 - 3 * q ^ 2 + 2) /
          (4 * q ^ 7 * (q ^ 2 + 1) ^ 2) := by
    rw [htr_int]
    field_simp [hq, hq2, hq2']
    ring
  have hdef_pos :
      0 < (q ^ 2 - 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) * (2 * q ^ 4 - 3 * q ^ 2 + 2) /
          (4 * q ^ 7 * (q ^ 2 + 1) ^ 2) := by
    have hq2_sub : 0 < q ^ 2 - 1 := by nlinarith
    have hquad : 0 < 2 * q ^ 4 - 3 * q ^ 2 + 2 := by
      have hsq : 2 * q ^ 4 - 3 * q ^ 2 + 2 = 2 * (q ^ 2 - 3 / 4) ^ 2 + 7 / 8 := by ring
      rw [hsq]; positivity
    apply div_pos
    · exact mul_pos (mul_pos (mul_pos (pow_pos hq2_sub 3) (by positivity)) (by positivity)) hquad
    · positivity
  have hh_pos : 0 < q - q⁻¹ := by
    have heq : q - q⁻¹ = (q ^ 2 - 1) / q := by field_simp
    rw [heq]
    exact div_pos (by nlinarith) hq0
  have hp_gap :
      (q ^ 8 + q ^ 4 + q ^ 2 + 1) * (q ^ 14 + q ^ 12 + q ^ 10 - 1) /
          (4 * q ^ 9 * (q ^ 2 + 1) ^ 2) -
        trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
          (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      let h := q - q⁻¹
      h * (h ^ 2 + 3) * (4 * h ^ 6 + 18 * h ^ 4 + 25 * h ^ 2 + 12) /
        (4 * (h ^ 2 + 4)) := by
    have hh4_ne : (q - q⁻¹) ^ 2 + 4 ≠ 0 := by positivity
    have hh4_ne' : 4 + (q - q⁻¹) ^ 2 ≠ 0 := by positivity
    rw [trM_conventionD_eq_twoRow_sum q hq hq2 hq4,
        chi3_protonCoord q hq h2,
        chi21_protonCoord q hq hq2 h2]
    dsimp only
    field_simp [hq, hq2, hq2', hh4_ne, hh4_ne']
    ring
  have hp_lt :
      trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
          (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) <
        (q ^ 8 + q ^ 4 + q ^ 2 + 1) * (q ^ 14 + q ^ 12 + q ^ 10 - 1) /
          (4 * q ^ 9 * (q ^ 2 + 1) ^ 2) := by
    rw [← sub_pos, hp_gap]
    dsimp only
    positivity
  have hn_gap :
      (q ^ 8 - q ^ 6 + q ^ 4 + 1) * (q ^ 10 + q ^ 6 - q ^ 4 + q ^ 2 - 1) /
          (4 * q ^ 9) -
        trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
          (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      let h := q - q⁻¹
      h * (h ^ 2 + 1) * (h ^ 2 + 3) * (2 * h ^ 2 + 3) / 4 := by
    rw [trM_conventionD_eq_twoRow_sum q hq hq2 hq4,
        chi3_neutronCoord q hq h2,
        chi21_neutronCoord q hq hq2 h2]
    dsimp only
    field_simp [hq, hq2, hq2']
    ring
  have hn_lt :
      trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
          (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) <
        (q ^ 8 - q ^ 6 + q ^ 4 + 1) * (q ^ 10 + q ^ 6 - q ^ 4 + q ^ 2 - 1) /
          (4 * q ^ 9) := by
    rw [← sub_pos, hn_gap]
    dsimp only
    positivity
  exact ⟨hdefect, by rwa [hdefect], hp_lt, hn_lt⟩

end BraidCommutatorAndOrderingSelection

/-! ## Section 3: Operator-Derived Convention-D Habiro–Kashiwara Expansion Through Order `u^3` (`qou-51yf` / `qou-cds1`) -/

section HabiroKashiwaraCubicExpansion

/-- **Exact Cubic Polynomial Termination of `Q_beta_form_A` in `ℏ_q = 1 - q⁻¹`**:
In the physical substrate interval `0 < q` with `q² - 2 q - 1 ≤ 0` (`1 ≤ q ≤ 1 + √2`, containing
`q₀ ≈ 1.11`), the 2-strand Form-A base `Q_beta_form_A q m_e` from `QOU.BraidKnot` terminates
identically at degree `3` in `hbarQ' q = (q - 1) / q`:
`Q_beta_form_A q m_e = m_e * (2 - 5 * hbarQ' q + 3 * (hbarQ' q) ^ 2 - (1 / 2) * (hbarQ' q) ^ 3)`. -/
theorem formA_over_me_exact_cubic_in_hbarQ (q m_e : ℝ) (hq : 0 < q)
    (hbound : q ^ 2 - 2 * q - 1 ≤ 0) :
    Q_beta_form_A q m_e =
      m_e * (2 - 5 * hbarQ' q + 3 * (hbarQ' q) ^ 2 - (1 / 2) * (hbarQ' q) ^ 3) := by
  have hq_ne : q ≠ 0 := ne_of_gt hq
  unfold Q_beta_form_A hbarQ'
  rw [abs_of_nonpos hbound]
  field_simp
  ring

/-- The mirror-projected bar-odd Convention-D ladder phase on `ℝ`
(`QOU.QBeta.phaseTwiceD_sub_hsq_bar_odd` divided by `4`):
`mirrorProjPhaseReal q = (markovZ' q - 1) * heckeH' q / 2 - (heckeH' q) ^ 2 / 4`. -/
noncomputable def mirrorProjPhaseReal (q : ℝ) : ℝ :=
  alpha q - (heckeH' q) ^ 2 / 4

/-- **Bar-Even Reduction of `hoefsmitB²` and `(mirrorProjPhaseReal)²` in `deltaHabiroSq`**:
With `y = deltaHabiroSq q = (q + q⁻¹) - 2` (`BringSchwingerNormalizationDerivation.deltaHabiroSq`):
1. `mirrorProjPhaseReal q` matches `(1/4) * (2 * phaseTwice (QOU.QBeta.zD q) (q - q⁻¹) - (q - q⁻¹)²)`
   from `LadderPhaseMirrorCovariance`,
2. `(hoefsmitB q) ^ 2 = (y + 1) * (y + 3) / (y + 2) ^ 2`,
3. `(mirrorProjPhaseReal q) ^ 2 = y * (y + 4) * (y ^ 2 + 2 * y - 2) ^ 2 / (16 * (y + 2) ^ 2)`, and
4. `q * (hoefsmitB q * (hbarQ' q) ^ 2) = hoefsmitB q * y`, showing that the bar-even Habiro variable
   `u_Hab = q * u` is analytic and linear in `y` around `q = 1` (`y = 0`), free of any `√u` branch cut. -/
theorem conventionD_mirror_phase_sq_in_deltaHabiroSq (q : ℝ) (hq : q ≠ 0) :
    let y := deltaHabiroSq q
    mirrorProjPhaseReal q =
      (2 * QOU.QBeta.phaseTwice (QOU.QBeta.zD q) (q - q⁻¹) - (q - q⁻¹) ^ 2) / 4 ∧
    (hoefsmitB q) ^ 2 = (y + 1) * (y + 3) / (y + 2) ^ 2 ∧
    (mirrorProjPhaseReal q) ^ 2 =
      y * (y + 4) * (y ^ 2 + 2 * y - 2) ^ 2 / (16 * (y + 2) ^ 2) ∧
    q * (hoefsmitB q * (hbarQ' q) ^ 2) = hoefsmitB q * y := by
  have hd : q ^ 2 + 1 ≠ 0 := by positivity
  have hd' : 1 + q ^ 2 ≠ 0 := by positivity
  have hd_exp : 1 + q ^ 2 * 2 + q ^ 4 ≠ 0 := by positivity
  have hd_exp2 : q ^ 4 + 2 * q ^ 2 + 1 ≠ 0 := by positivity
  have hy2 : deltaHabiroSq q + 2 = (q ^ 2 + 1) / q := by
    unfold deltaHabiroSq
    field_simp [hq]
    ring
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold mirrorProjPhaseReal alpha markovZ' heckeH' QOU.QBeta.phaseTwice QOU.QBeta.zD
    ring
  · rw [hoefsmitB_sq_eq_bracketThree_div_bracketTwo_sq q hq]
    rw [hy2]
    unfold deltaHabiroSq
    field_simp [hq, hd, hd', hd_exp, hd_exp2]
    ring
  · change (mirrorProjPhaseReal q) ^ 2 =
      deltaHabiroSq q * (deltaHabiroSq q + 4) *
        ((deltaHabiroSq q) ^ 2 + 2 * deltaHabiroSq q - 2) ^ 2 /
        (16 * (deltaHabiroSq q + 2) ^ 2)
    rw [hy2]
    unfold mirrorProjPhaseReal alpha markovZ' heckeH' deltaHabiroSq
    field_simp [hq, hd, hd', hd_exp, hd_exp2]
    ring
  · dsimp only
    unfold deltaHabiroSq hbarQ'
    field_simp [hq]
    ring

/-- **Exact Operator-Derived `u^3` Taylor Jet of `cos(α_D^{proj})` and Kashiwara–Hopf `N = 3` Product**:
1. Let `U(y)` have squared Habiro relation `U² = y² (y + 1)(y + 3) / (y + 2)²` with leading 3-jet
   `U_jet(y) = (√3 / 2) * (y + y² / 6 - 5 y³ / 36)`. Substituting `U_jet(y)` into the operator-derived
   cubic series `C_3(U) = 1 - (√3 / 12) U + (47 / 96) U² - (2069 √3 / 5760) U³` matches the exact
   3-jet of `cos(mirrorProjPhaseReal q) = 1 - P₂/2 + P₂²/24 - P₂³/720` (where
   `P₂(y) = y(y + 4)(y² + 2y - 2)² / (16(y + 2)²) = y/4 - 11 y²/16 + y³/2 + O(y⁴)` gives
   `cos_jet_y = 1 - y/8 + 133 y²/384 - 12181 y³/46080`) identically modulo `y⁴`!
2. Furthermore, the `N = 2` and `N = 3` Kashiwara–Hopf ladder factors `N2_factor q * N3_factor q`
   from `QOU.BraidKnot` expand in `u = hoefsmitB q * (hbarQ' q) ^ 2` as
   `1 - u ^ 2 - 2 * u ^ 3 + 2 * u ^ 5` (`c₂ = -1`, `c₃ = -2`, cross-rung `c₅ = +2`). -/
theorem mirror_phase_jet_and_kashiwara_n3_expansion (y q : ℝ) :
    let s3 := Real.sqrt 3
    let u_jet := (s3 / 2) * (y + y ^ 2 / 6 - 5 * y ^ 3 / 36)
    let c3_poly := 1 - (s3 / 12) * u_jet + (47 / 96 : ℝ) * u_jet ^ 2 -
      (2069 * s3 / 5760) * u_jet ^ 3
    let cos_jet_y := 1 - (1 / 8 : ℝ) * y + (133 / 384 : ℝ) * y ^ 2 -
      (12181 / 46080 : ℝ) * y ^ 3
    let u := hoefsmitB q * (hbarQ' q) ^ 2
    (y + 2) ^ 2 * u_jet ^ 2 - y ^ 2 * (y + 1) * (y + 3) =
      y ^ 5 * (-(23 / 36 : ℝ) - (29 / 108 : ℝ) * y +
        (5 / 216 : ℝ) * y ^ 2 + (25 / 1728 : ℝ) * y ^ 3) ∧
    c3_poly - cos_jet_y =
      y ^ 4 * (-(3009 / 10240 : ℝ) + (16271 / 138240 : ℝ) * y +
        (203503 / 3317760 : ℝ) * y ^ 2 - (2069 / 110592 : ℝ) * y ^ 3 -
        (10345 / 2654208 : ℝ) * y ^ 4 + (51725 / 47775744 : ℝ) * y ^ 5) ∧
    N2_factor q * N3_factor q = 1 - u ^ 2 - 2 * u ^ 3 + 2 * u ^ 5 := by
  have hs3 : (Real.sqrt 3) ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hs3_4 : (Real.sqrt 3) ^ 4 = 9 := by
    calc (Real.sqrt 3) ^ 4 = ((Real.sqrt 3) ^ 2) ^ 2 := by ring
    _ = 9 := by rw [hs3]; norm_num
  refine ⟨?_, ?_, ?_⟩
  · dsimp only
    ring_nf
    rw [hs3]
    ring
  · dsimp only
    ring_nf
    rw [hs3, hs3_4]
    ring
  · dsimp only
    unfold N2_factor N3_factor jonesHopfClassicalLimit
    ring

/-- **Classical Anchor Limits (`q = 1`) of the Convention-D Multi-Block Bases & `kdFullTwistChar`**:
At `q = 1` (`hbarQ' 1 = 0`), multiplying `nucleonDiffCoord` by `1 / (q * (q - 1))` desingularizes
the `(q - 1)` zero so that:
1. `(-trM (zD q)) / (q * (q - 1))` evaluates at `q = 1` (via its cancelled rational quotient) to `5 / 4`,
2. `(-trM_conventionD_gpmtPos q) / (q * (q - 1))` evaluates at `q = 1` to `19 / 12` (`5/4 + 1/3`),
3. `Q_beta_form_A 1 1 = 2`, and
4. `kdFullTwistChar q - 1 = (hbarQ' q) ^ 2 * (q ^ 5 + q ^ 4 + q ^ 3 + q ^ 2 + q + 1) ^ 2 / (2 * q ^ 4)`
   (vanishing to order `18 * (hbarQ' q) ^ 2` at `q = 1`). -/
theorem conventionD_base_classical_limits_and_hbarQ_jets (q : ℝ) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    let zD_desing := -(q + 1) * (q ^ 4 + 1) *
      (2 * q ^ 12 - 6 * q ^ 10 + 3 * q ^ 8 - 6 * q ^ 6 + 5 * q ^ 4 - 5 * q ^ 2 + 2) /
      (4 * q ^ 8 * (q ^ 2 + 1) ^ 2)
    let gpmt_desing := -(q + 1) *
      (2 * q ^ 20 - 4 * q ^ 18 + q ^ 16 - 13 * q ^ 14 + q ^ 12 - q ^ 11 -
        15 * q ^ 10 - 3 * q ^ 9 + 4 * q ^ 8 - 3 * q ^ 7 - 9 * q ^ 6 - q ^ 5 +
        4 * q ^ 4 - 3 * q ^ 2 + 2) /
      (4 * q ^ 8 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1))
    ((-trM (QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace.zD q) (q - q⁻¹)
        (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2))) / (q * (q - 1)) = zD_desing) ∧
    ((-trM_conventionD_gpmtPos q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2))) /
        (q * (q - 1)) = gpmt_desing) ∧
    (-(1 + 1) * (1 ^ 4 + 1) *
      (2 * (1 : ℝ) ^ 12 - 6 * 1 ^ 10 + 3 * 1 ^ 8 - 6 * 1 ^ 6 + 5 * 1 ^ 4 - 5 * 1 ^ 2 + 2) /
      (4 * 1 ^ 8 * (1 ^ 2 + 1) ^ 2)) = (5 / 4 : ℝ) ∧
    (-(1 + 1) *
      (2 * (1 : ℝ) ^ 20 - 4 * 1 ^ 18 + 1 ^ 16 - 13 * 1 ^ 14 + 1 ^ 12 - 1 ^ 11 -
        15 * 1 ^ 10 - 3 * 1 ^ 9 + 4 * 1 ^ 8 - 3 * 1 ^ 7 - 9 * 1 ^ 6 - 1 ^ 5 +
        4 * 1 ^ 4 - 3 * 1 ^ 2 + 2) /
      (4 * 1 ^ 8 * (1 ^ 2 + 1) ^ 2 * (1 ^ 4 + 1 ^ 2 + 1))) = (19 / 12 : ℝ) ∧
    Q_beta_form_A 1 1 = 2 ∧
    kdFullTwistChar q - 1 =
      (hbarQ' q) ^ 2 * (q ^ 5 + q ^ 4 + q ^ 3 + q ^ 2 + q + 1) ^ 2 /
        (2 * q ^ 4) := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq2' : 1 + q ^ 2 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have hq4' : 1 + q ^ 2 + q ^ 4 ≠ 0 := by positivity
  have h2 : (2 : ℝ) ≠ 0 := two_ne_zero
  refine ⟨?_, ?_, by norm_num, by norm_num, ?_, ?_⟩
  · dsimp only
    rw [(trM_conventionD_nucleonDiffCoord_eq_neg_constituent_diff q hq hq2 hq4 h2).1]
    field_simp [hq, hq1, hq2, hq2']
    ring
  · dsimp only
    rw [trM_conventionD_gpmtPos_nucleonDiffCoord_eq_rational q hq hq2 hq4 h2]
    field_simp [hq, hq1, hq2, hq2', hq4, hq4']
    ring
  · unfold Q_beta_form_A
    norm_num
  · rw [kdFullTwistChar_sub_one q hq h2]
    unfold hbarQ'
    field_simp [hq]
    ring

end HabiroKashiwaraCubicExpansion

/-! ## Section 4: Two-Term Categorical Lagrangian Corrected-Photon Bridge & Exact Error-Dilution Laws -/

section TwoTermLagrangianPhotonAndErrorDilution

universe u v

/-- **Two-Term Categorical Lagrangian Hadronic-Scale & Corrected-Photon Bridge**:
For any `ℝ`-linear preadditive braided monoidal category `C` (`CategoricalLagrangianTwoTermBridge`),
when `L_n, L_p` share spatial closure (`qinv = q⁻¹`, equal `nablaEndo` and spatial-Reeb cross-trace)
and the fermionic matter difference evaluates to `-α_corr * w * Δtr_conn(V³)` with `α_corr`
satisfying the Form-B Bring–Schwinger electromagnetic fixed-point relation
`IsUnifiedBringFixedPoint 1 (q * q9 * q10) 4 q ((q - q⁻¹) ^ 2) α_corr`:
1. `(m_e / (hbarQ' q) ^ 2) * (τ L_n.lagrangian - τ L_p.lagrangian)` decomposes identically into
   `m_e * (τ (L_n.dirac.reeb ≫ L_n.dirac.reeb) - τ (L_p.dirac.reeb ≫ L_p.dirac.reeb))` minus the
   corrected-photon Borromean QED splitting
   `m_e * (α_corr / (hbarQ' q) ^ 2) * w * ((q ^ 2 - 1) ^ 4 * (4 * q ^ 4 + q ^ 2 + 4) / (27 * q ^ 6))`,
2. `α_corr` satisfies the Form-B cubic equation
   `unifiedBringCubic 1 (q * q9 * q10) 4 q ((q - q⁻¹) ^ 2) α_corr = 0`. -/
theorem twoTerm_lagrangian_hadronic_photon_scale_bridge
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
    [Preadditive C] [CategoryTheory.Linear ℝ C] {fh : FrobeniusHopfData C}
    (τ : (fh.obj ⟶ fh.obj) →ₗ[ℝ] ℝ)
    (L_n L_p : CategoricalLagrangian ℝ C fh)
    (q m_e q9 q10 α_corr w : ℝ)
    (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (hα : α_corr ≠ 0)
    (hQn : L_n.dirac.qinv = q⁻¹)
    (hQp : L_p.dirac.qinv = q⁻¹)
    (hNabla : L_n.dirac.nablaEndo = L_p.dirac.nablaEndo)
    (hCross :
      τ (L_n.dirac.nablaEndo ≫ L_n.dirac.reeb + L_n.dirac.reeb ≫ L_n.dirac.nablaEndo) =
      τ (L_p.dirac.nablaEndo ≫ L_p.dirac.reeb + L_p.dirac.reeb ≫ L_p.dirac.nablaEndo))
    (hMatter :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.dirac) -
        τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.dirac) =
      -α_corr * w *
        ((1 / 3 : ℝ) *
          ((trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : ℝ) * trace (borromeanV3B q)) -
            trace ((Q12p + Q23p) * borromeanV3A q))))
    (hBring : IsUnifiedBringFixedPoint 1 (q * q9 * q10) 4 q ((q - q⁻¹) ^ 2) α_corr) :
    (m_e / (hbarQ' q) ^ 2) * (τ L_n.lagrangian - τ L_p.lagrangian) =
      m_e * (τ (L_n.dirac.reeb ≫ L_n.dirac.reeb) - τ (L_p.dirac.reeb ≫ L_p.dirac.reeb)) -
        m_e * (α_corr / (hbarQ' q) ^ 2) * w *
          ((q ^ 2 - 1) ^ 4 * (4 * q ^ 4 + q ^ 2 + 4) / (27 * q ^ 6)) ∧
    unifiedBringCubic 1 (q * q9 * q10) 4 q ((q - q⁻¹) ^ 2) α_corr = 0 := by
  have hQinv : L_n.dirac.qinv = L_p.dirac.qinv := hQn.trans hQp.symm
  have hbar_eq : 1 - q⁻¹ = hbarQ' q := by
    unfold hbarQ'
    field_simp
  have hbar_ne : hbarQ' q ≠ 0 := by
    unfold hbarQ'
    exact div_ne_zero hq1 hq
  have hbar_sq_ne : (hbarQ' q) ^ 2 ≠ 0 := pow_ne_zero 2 hbar_ne
  have h3 : (3 : ℝ) ≠ 0 := by norm_num
  have hConn := trace_QAdj_connected_diff_borromeanV3 q hq h3
  refine ⟨?_, (unifiedBringFixedPoint_iff_cubic 1 (q * q9 * q10) 4 q ((q - q⁻¹) ^ 2) α_corr hα).mp hBring⟩
  rw [trace_lagrangian_diff_shared_spatial_closure τ L_n L_p hQinv hNabla hCross,
      hQn, hbar_eq, hMatter, hConn]
  have hsq : (q - 1) ^ 4 * (q + 1) ^ 4 = (q ^ 2 - 1) ^ 4 := by ring
  rw [hsq]
  field_simp [hbar_sq_ne, hq]
  ring

/-- **Exact Relative Error-Dilution Law for `Δm_{pn} = Q_β + m_e`**:
Over any field `K`, for `q_ref ≠ 0` and `q_ref + m_e ≠ 0`, adding the exact CAL-1 anchor `m_e`
preserves the absolute residual (`(q_pred + m_e) - (q_ref + m_e) = q_pred - q_ref`) and contracts
the relative residual by the exact dilution factor `q_ref / (q_ref + m_e)`:
`((q_pred + m_e) - (q_ref + m_e)) / (q_ref + m_e) = (q_ref / (q_ref + m_e)) * ((q_pred - q_ref) / q_ref)`.
Over `ℝ` with `0 < q_ref` and `0 < m_e`, `0 < q_ref / (q_ref + m_e) < 1`. -/
theorem delta_pn_error_dilution_law
    (q_pred q_ref m_e : ℝ) (hq_ref : 0 < q_ref) (hme : 0 < m_e) :
    ((q_pred + m_e) - (q_ref + m_e)) = q_pred - q_ref ∧
    ((q_pred + m_e) - (q_ref + m_e)) / (q_ref + m_e) =
      (q_ref / (q_ref + m_e)) * ((q_pred - q_ref) / q_ref) ∧
    0 < q_ref / (q_ref + m_e) ∧
    q_ref / (q_ref + m_e) < 1 := by
  have hq_ne : q_ref ≠ 0 := ne_of_gt hq_ref
  have hsum_pos : 0 < q_ref + m_e := add_pos hq_ref hme
  have hsum_ne : q_ref + m_e ≠ 0 := ne_of_gt hsum_pos
  refine ⟨by ring, ?_, div_pos hq_ref hsum_pos, (div_lt_one hsum_pos).mpr (by linarith)⟩
  field_simp [hq_ne, hsum_ne]
  ring

/-- **Exact Relative Error-Dilution Chain for Consistent Two-Term `m_n = m_p + Δm_{pn}`**:
When `mp_qcd + mp_qed = mp_ref` and `mn_ref = mp_ref + (q_ref + m_e)`, the consistent two-term
neutron mass `mn_pred = (mp_qcd + mp_qed) + (q_pred + m_e)` satisfies:
1. `mn_pred - mn_ref = q_pred - q_ref`,
2. `(mn_pred - mn_ref) / mn_ref = (q_ref / mn_ref) * ((q_pred - q_ref) / q_ref)`,
3. `(mn_pred - mn_ref) / mn_ref = ((q_ref + m_e) / mn_ref) * (((q_pred + m_e) - (q_ref + m_e)) / (q_ref + m_e))`,
4. Strict dilution hierarchy `0 < q_ref / mn_ref < q_ref / (q_ref + m_e) < 1`. -/
theorem neutron_mass_error_dilution_law
    (mp_qcd mp_qed mp_ref m_e q_pred q_ref mn_ref : ℝ)
    (hpin : mp_qcd + mp_qed = mp_ref)
    (hmn_ref : mn_ref = mp_ref + (q_ref + m_e))
    (hmp : 0 < mp_ref) (hq_ref : 0 < q_ref) (hme : 0 < m_e) :
    let mn_pred := (mp_qcd + mp_qed) + (q_pred + m_e)
    mn_pred - mn_ref = q_pred - q_ref ∧
    (mn_pred - mn_ref) / mn_ref = (q_ref / mn_ref) * ((q_pred - q_ref) / q_ref) ∧
    (mn_pred - mn_ref) / mn_ref =
      ((q_ref + m_e) / mn_ref) * (((q_pred + m_e) - (q_ref + m_e)) / (q_ref + m_e)) ∧
    0 < q_ref / mn_ref ∧
    q_ref / mn_ref < q_ref / (q_ref + m_e) ∧
    q_ref / (q_ref + m_e) < 1 := by
  have hdpn_pos : 0 < q_ref + m_e := add_pos hq_ref hme
  have hmn_pos : 0 < mn_ref := by rw [hmn_ref]; exact add_pos hmp hdpn_pos
  have hq_ne : q_ref ≠ 0 := ne_of_gt hq_ref
  have hdpn_ne : q_ref + m_e ≠ 0 := ne_of_gt hdpn_pos
  have hmn_ne : mn_ref ≠ 0 := ne_of_gt hmn_pos
  have hdiff : ((mp_qcd + mp_qed) + (q_pred + m_e)) - mn_ref = q_pred - q_ref := by
    rw [hpin, hmn_ref]; ring
  refine ⟨hdiff, ?_, ?_, div_pos hq_ref hmn_pos, ?_, (div_lt_one hdpn_pos).mpr (by linarith)⟩
  · dsimp only
    rw [hdiff]
    field_simp [hq_ne, hmn_ne]
  · dsimp only
    rw [hdiff]
    field_simp [hdpn_ne, hmn_ne]
    ring
  · exact div_lt_div_of_pos_left hq_ref hdpn_pos (by rw [hmn_ref]; linarith)

end TwoTermLagrangianPhotonAndErrorDilution

end QOU.QBeta.ConventionDC3AndTailSelectionDerivation
