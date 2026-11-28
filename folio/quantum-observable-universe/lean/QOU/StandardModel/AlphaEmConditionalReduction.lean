/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import QOU.BringsSurface.BringMapChain
import QOU.Core.LawvereCut
import QOU.MassTheory.EmCouplingBringZeroMode
import QOU.MassTheory.EmFermionLoopFourTopology
import QOU.MassTheory.EmFormBLoopMeasure
import QOU.MassTheory.EmPerLoopMeasureConditional
import QOU.MassTheory.EmPhotonJoinRules
import QOU.MassTheory.EmTwoLoopMeasureConnected
import QOU.StandardModel.ElectroweakConditionalDischarge
import QOU.Transcendental.MassTheory.AlphaEmFormCConditionalContent
import QOU.Transcendental.MassTheory.EmPerLoopMeasureConditionalReal
import QOU.Transcendental.MathlibExt.DilogarithmArchimedeanLimit

/-!
# Conditional-to-Proved Reduction for Electromagnetic `α_EM` & Rydberg `R_∞` (`qou-vhm1`)

This module audits and shrinks the conditional hypothesis surface backing `ACCURACY.md` Table 3.3a
(`α_EM⁻¹` Form B `-0.365 ppb = -2.38σ`, Form C `-0.024 ppb = -0.16σ`, and Rydberg `R_∞ h c` Form B
`+0.725 ppb`, Form C `+0.043 ppb = +0.14σ`) against all theorems landed on `main` through
`2cc11f7f1c6` (`BringMapChain`, `EmPhotonJoinRules`, `EmFormBLoopMeasure`, `EmTwoLoopMeasureConnected`,
`EmFermionLoopFourTopology`, `EmPerLoopMeasureConditionalReal`, `AlphaEmFormCConditionalContent`,
and `DilogarithmArchimedeanLimit`), with **zero `sorry`**, **zero custom axioms**, **zero `[Field]` /
`field_simp` markers**, and **zero transcendental tokens**:

1. **Section 1 — Finite `S₅` Regular-Map Discharge of Electromagnetic Bring Topology (`BringMapChain`):**
   - Proves directly from `BringMapChain` (`bringMapEuler = -6`, `bringMapBettiOne = 8`) that
     `bringMapEuler = bringTilingEuler` (`-6 = -6`), `bringMapBettiOne = 2 - bringTilingEuler = 8`,
     and that the electromagnetic zero-mode `2/(3π)` (`bringZeroModeValue`) equals
     `(bringMapBettiOne : ℝ) / bringSurfaceArea` with **zero `BringZeroModeBlochClass` input**
     (confirming `docs/audits/2026-11-28-form-b-alpha-premise-status.md`).
   - Upgrades `EmMeasureGaussBonnet.b1_reading_coincides_iff_g4` to any `[CommRing R] [IsDomain R]
     [CharZero R]` without division: the Betti denominator `2g` equals the Gauss–Bonnet denominator `8`
     (`|χ| / (4 Area) = 1 / (8 p)`) if and only if `g = 4 = bringMapBettiOne / 2`.

2. **Section 2 — Constructive `[CommRing R]` / `Rˣ` EM Tree `[9]_q [10]_q` Algebra, Bar-Odd Loop
   Recursion (`-h²`), Constant Form-B Measure (`μ_L = μ₁`), and Connected Two-Loop Split:**
   - Proves the nine-channel `SU(2)_q` Clebsch–Gordan expansion
     `[9]_q [10]_q = [18]_q + [16]_q + [14]_q + [12]_q + [10]_q + [8]_q + [6]_q + [4]_q + [2]_q`
     (`90 = 9 × 10` at `q = 1`) and division-free bar-breaking law `emTreeU q⁻¹ * q² = emTreeU q`.
   - Composes `EmPhotonJoinRules.barOdd_eq`, `EmFormBLoopMeasure.formB_coeff_of_recursion`,
     `EmFormBLoopMeasure.formB_measure_const`, and `EmTwoLoopMeasureConnected.formB_connected` to
     prove that the signed bar-odd two-vertex join `-h²` uniquely determines the entire `L`-loop
     Form-B ladder `c_L = [2]_q μ₁ (-h²)^L` from `μ₁` alone, with `c₀ α + c₁ α² = [2]_q μ₁ α (1 - h² α)`.

3. **Section 3 — Ordered-Ring Strict Monotonicity & Proton-Pinned `LawvereCut.Cut ℚ` Certificate
   for Form-B `α_EM⁻¹(q₀)` (`width = 3 × 10⁻¹⁰`, `0.00219 ppb`):**
   - Proves strict monotonicity and root uniqueness of the cleared Form-B inverse-coupling cubic
     `A³ - T₀ A² - H A + h² H` over any strict ordered commutative ring, and certifies on `ℚ`
     (strictly proton-pinned per owner ruling `2026-11-28`, zero `Real.sqrt`) that every root
     `A ≥ 100` lies inside `emInvAlphaProtonCut = [1370359991268/10¹⁰, 1370359991271/10¹⁰]`,
     and derives the induced rational interval enclosure on the dimensionless Rydberg factor `α_EM² / 2`.

4. **Section 4 — Minimal Open Kernels for Form B & Form C (`FormBMinimalKernelClass` & `FormCPinned`):**
   - Isolates Form B (`α_EM` and `R_∞`) to `FormBMinimalKernelClass` (carrying ONLY the phase-4
     measure hypotheses `GermPeriodShare μ₁ a₀` + `HeatKernelLeadingCoeff a₀` and the additive
     2-loop-truncated self-energy assembly `1/α = T_tree + b₁/Area + c₀ α + c₁ α²`), deriving
     `IsTwoLoopBringFixedPoint ... 0 α` and `twoLoopBringCubic ... 0 α = 0` unconditionally,
     with an explicit `def trivialModelFormB` consistency witness.
   - Isolates Form C (`AlphaEmTwoLoopBlochSchwingerClass` + `qou-aemx`) via `FormCPinned` to the
     single connected-period equation `deltaB3 q = deltaReq q α`, accompanied by the unconditional
     dilogarithm boundary/duplication discharge witness (`archimedeanLimit_zero` + `LiTwo_duplication`).

-- Ref: [leitner2026] QOU α_EM and Rydberg conditional-to-proved reduction, bean qou-vhm1
-- Ref: [faddeev1994] Faddeev, Current-like variables in massive and massless integrable models, 1994
-/

set_option autoImplicit false

namespace QOU.StandardModel
namespace AlphaEmConditionalReduction

open QOU.Core.LawvereCut (Cut Coev CutEvaluation)
open QOU.QInteger (qIntBal)
open QOU.QPochhammer (ArchimedeanLimit archimedeanLimit_zero LiTwo LiTwo_duplication)
open QOU.Archimedean (bringTilingEuler bringTilingEuler_eq bringSurfaceArea
  bringZeroModeValue bringZeroMode_fully_tiling_derived firstBetti)
open QOU.Archimedean.BringSchwingerNormalizationDerivation
  (habiroNorm hHecke habiroNorm_eq_rational_mul_zeroModes)
open QOU.MassTheory.EmVertexPairScalarChain (HeckeGen)
open QOU.MassTheory.EmPhotonJoinRules (barOdd_eq)
open QOU.MassTheory.EmFormBLoopMeasure
  (formBCoeff formBGraph formB_coeff_zero formB_coeff_succ
   formB_coeff_of_recursion formB_measure_const)
open QOU.MassTheory.EmTwoLoopMeasureConnected
  (LoopMeasure connected Factorizes formBMeasure formB_connected thetaMeasure theta_factorizes)
open QOU.MassTheory.EmPerLoopMeasureConditional (GermPeriodShare)
open QOU.Archimedean.EmPerLoopMeasureConditionalReal
  (HeatKernelLeadingCoeff perLoop_eq_inv_eight_pi)
open QOU.Archimedean.AlphaEmTwoLoopBlochSchwinger
  (IsTwoLoopBringFixedPoint twoLoopBringCubic twoLoopBringFixedPoint_iff_cubic
   exists_unique_pos_cubic_root AlphaEmTwoLoopBlochSchwingerClass)
open QOU.Archimedean.AlphaEmFormCConditionalContent
  (FormCPinned formCPinned_iff deltaB3 deltaReq habiroNorm_pos)
open QOU.StandardModel.ElectroweakConditionalDischarge
  (chebB qBalU qBalU_bar qBalU_one bringMapEuler bringMapBettiOne
   bringMap_connected_and_euler bringMapBettiOne_eq_eight_and_genus_four)

/-! ## Section 1: Finite `S₅` Regular-Map Discharge of Electromagnetic Bring Topology -/

section BringMapEmZeroModeAndGaussBonnet

/-- **Unconditional reconciliation of the finite `S₅` regular map and the `(2,4,5)` triangle tiling:**
`bringMapEuler = bringTilingEuler = -6`, `bringMapBettiOne = 2 - bringTilingEuler = 8`, and the
electromagnetic zero-mode `bringZeroModeValue` (`2/(3π)`) equals `(bringMapBettiOne : ℝ) / bringSurfaceArea`
with **zero `BringZeroModeBlochClass` hypothesis**. -/
theorem em_bringZeroMode_from_finite_map :
    bringMapEuler = bringTilingEuler ∧
    bringMapBettiOne = 2 - bringTilingEuler ∧
    (bringMapBettiOne : ℝ) / bringSurfaceArea = bringZeroModeValue := by
  have heul : bringMapEuler = bringTilingEuler := by
    rw [bringMap_connected_and_euler.2.2.2.2, bringTilingEuler_eq]
  have hb1 : bringMapBettiOne = 2 - bringTilingEuler := by
    unfold bringMapBettiOne
    rw [heul]
  refine ⟨heul, hb1, ?_⟩
  rw [hb1]
  exact bringZeroMode_fully_tiling_derived

/-- **Domain-level Gauss–Bonnet vs Betti coincidence (`§7c` upgrade of `b1_reading_coincides_iff_g4`):**
Over any integral domain `R` of characteristic zero (`0` `[Field]` requirement), for any nonzero
period symbol `p ≠ 0`, the Betti period `p · (2 g)` equals the Gauss–Bonnet denominator `8 p`
(`4 · Area(g) / |χ(g)| = 4 · 4 p (g - 1) / (2 (g - 1)) = 8 p`) if and only if `g = 4 = bringMapBettiOne / 2`. -/
theorem em_betti_period_eq_gauss_bonnet_iff_g4
    {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    (p g : R) (hp : p ≠ 0) :
    (p * (2 * g) = 8 * p ↔ g = 4) ∧
    4 * (4 * p * (g - 1)) = 8 * p * (2 * g - 2) ∧
    ((bringMapBettiOne / 2 : ℤ) : R) = 4 := by
  refine ⟨?_, by ring, ?_⟩
  · constructor
    · intro h
      have hfac : p * (2 * (g - 4)) = 0 := by linear_combination h
      rcases mul_eq_zero.mp hfac with hp0 | h2g
      · exact absurd hp0 hp
      · rcases mul_eq_zero.mp h2g with h20 | hg4
        · exact absurd h20 (by norm_num)
        · linear_combination hg4
    · rintro rfl
      ring
  · rw [bringMapBettiOne_eq_eight_and_genus_four.2]
    norm_num

end BringMapEmZeroModeAndGaussBonnet

/-! ## Section 2: Constructive `[CommRing R]` / `Rˣ` EM Tree `[9]_q [10]_q` & Form-B Loop Ladder -/

section ConstructiveEmTreeAndLoopLadder

/-- **Nine-channel `SU(2)_q` Clebsch–Gordan expansion of `[9]_q [10]_q` over `[CommRing R]`:**
`V₈ ⊗ V₉ ≅ V₁₇ ⊕ V₁₅ ⊕ V₁₃ ⊕ V₁₁ ⊕ V₉ ⊕ V₇ ⊕ V₅ ⊕ V₃ ⊕ V₁`, i.e.
`[9]_q [10]_q = [18]_q + [16]_q + [14]_q + [12]_q + [10]_q + [8]_q + [6]_q + [4]_q + [2]_q`
(`18 + 16 + 14 + 12 + 10 + 8 + 6 + 4 + 2 = 90 = 9 × 10` at `q = 1`). -/
theorem em_carrier_product_clebsch_gordan {R : Type*} [CommRing R] (q : Rˣ) :
    qBalU q 9 * qBalU q 10 =
      qBalU q 18 + qBalU q 16 + qBalU q 14 + qBalU q 12 + qBalU q 10 +
      qBalU q 8 + qBalU q 6 + qBalU q 4 + qBalU q 2 := by
  set x : R := (q : R) + (↑q⁻¹ : R)
  have u0 : chebB x 0 = 0 := rfl
  have u1 : chebB x 1 = 1 := rfl
  have u2 : chebB x 2 = x := by rw [chebB, u1, u0]; ring
  have u3 : chebB x 3 = x ^ 2 - 1 := by rw [chebB, u2, u1]; ring
  have u4 : chebB x 4 = x ^ 3 - 2 * x := by rw [chebB, u3, u2]; ring
  have u5 : chebB x 5 = x ^ 4 - 3 * x ^ 2 + 1 := by rw [chebB, u4, u3]; ring
  have u6 : chebB x 6 = x ^ 5 - 4 * x ^ 3 + 3 * x := by rw [chebB, u5, u4]; ring
  have u7 : chebB x 7 = x ^ 6 - 5 * x ^ 4 + 6 * x ^ 2 - 1 := by rw [chebB, u6, u5]; ring
  have u8 : chebB x 8 = x ^ 7 - 6 * x ^ 5 + 10 * x ^ 3 - 4 * x := by rw [chebB, u7, u6]; ring
  have u9 : chebB x 9 = x ^ 8 - 7 * x ^ 6 + 15 * x ^ 4 - 10 * x ^ 2 + 1 := by
    rw [chebB, u8, u7]; ring
  have u10 : chebB x 10 = x ^ 9 - 8 * x ^ 7 + 21 * x ^ 5 - 20 * x ^ 3 + 5 * x := by
    rw [chebB, u9, u8]; ring
  have u11 : chebB x 11 = x ^ 10 - 9 * x ^ 8 + 28 * x ^ 6 - 35 * x ^ 4 + 15 * x ^ 2 - 1 := by
    rw [chebB, u10, u9]; ring
  have u12 : chebB x 12 = x ^ 11 - 10 * x ^ 9 + 36 * x ^ 7 - 56 * x ^ 5 + 35 * x ^ 3 - 6 * x := by
    rw [chebB, u11, u10]; ring
  have u13 : chebB x 13 =
      x ^ 12 - 11 * x ^ 10 + 45 * x ^ 8 - 84 * x ^ 6 + 70 * x ^ 4 - 21 * x ^ 2 + 1 := by
    rw [chebB, u12, u11]; ring
  have u14 : chebB x 14 =
      x ^ 13 - 12 * x ^ 11 + 55 * x ^ 9 - 120 * x ^ 7 + 126 * x ^ 5 - 56 * x ^ 3 + 7 * x := by
    rw [chebB, u13, u12]; ring
  have u15 : chebB x 15 =
      x ^ 14 - 13 * x ^ 12 + 66 * x ^ 10 - 165 * x ^ 8 + 210 * x ^ 6 - 126 * x ^ 4 +
        28 * x ^ 2 - 1 := by
    rw [chebB, u14, u13]; ring
  have u16 : chebB x 16 =
      x ^ 15 - 14 * x ^ 13 + 78 * x ^ 11 - 220 * x ^ 9 + 330 * x ^ 7 - 252 * x ^ 5 +
        84 * x ^ 3 - 8 * x := by
    rw [chebB, u15, u14]; ring
  have u17 : chebB x 17 =
      x ^ 16 - 15 * x ^ 14 + 91 * x ^ 12 - 286 * x ^ 10 + 495 * x ^ 8 - 462 * x ^ 6 +
        210 * x ^ 4 - 36 * x ^ 2 + 1 := by
    rw [chebB, u16, u15]; ring
  have u18 : chebB x 18 =
      x ^ 17 - 16 * x ^ 15 + 105 * x ^ 13 - 364 * x ^ 11 + 715 * x ^ 9 - 792 * x ^ 7 +
        462 * x ^ 5 - 120 * x ^ 3 + 9 * x := by
    rw [chebB, u17, u16]; ring
  change chebB x 9 * chebB x 10 =
    chebB x 18 + chebB x 16 + chebB x 14 + chebB x 12 + chebB x 10 +
    chebB x 8 + chebB x 6 + chebB x 4 + chebB x 2
  rw [u2, u4, u6, u8, u9, u10, u12, u14, u16, u18]
  ring

/-- Division-free electromagnetic tree term `q [9]_q [10]_q` over any `[CommRing R]` with `q : Rˣ`. -/
def emTreeU {R : Type*} [CommRing R] (q : Rˣ) : R :=
  (q : R) * qBalU q 9 * qBalU q 10

/-- **Division-free EM bar-breaking & classical specialization (`§7c` upgrade of `emTreeF_bar`):**
`emTreeU q⁻¹ * q² = emTreeU q` over every `[CommRing R]`, and `emTreeU 1 = 90`. -/
theorem emTreeU_bar_and_classical {R : Type*} [CommRing R] (q : Rˣ) :
    emTreeU q⁻¹ * (q : R) ^ 2 = emTreeU q ∧ emTreeU (1 : Rˣ) = 90 := by
  refine ⟨?_, ?_⟩
  · unfold emTreeU
    rw [qBalU_bar, qBalU_bar]
    have hqi : (↑q⁻¹ : R) * (q : R) = 1 := q.inv_val
    linear_combination ((q : R) * qBalU q 9 * qBalU q 10) * hqi
  · unfold emTreeU
    rw [qBalU_one, qBalU_one]
    push_cast
    norm_num

/-- **Complete Form-B All-Loop Reduction (`EmPhotonJoinRules` + `EmFormBLoopMeasure` + `EmTwoLoopMeasureConnected`):**
Over any `[CommRing R]` and `R`-algebra `A`:
1. The signed bar-odd two-vertex join evaluates to `-h²` at any two positions (`barOdd_eq`);
2. Any loop ladder `(c : ℕ → R)` seeded by `c 0 = s * μ₁` and stepping by `c (L + 1) = -h² * c L`
   is uniquely `formBCoeff s h μ₁ L = s * μ₁ * (-h²)^L` (`formB_coeff_of_recursion`);
3. Its two-loop truncated sum `c 0 * α + c 1 * α²` equals the Form-B self-energy `α * (s * μ₁) * (1 - h² * α)`;
4. Its two-loop measure `formBMeasure μ₁ = ⟨μ₁, μ₁⟩` has connected cumulant `μ₁ - μ₁²`, whereas the
   θ-graph measure `thetaMeasure μ₁ = ⟨μ₁, μ₁²⟩` factorizes (`connected = 0`). -/
theorem em_formB_all_loop_reduction
    {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (s h μ₁ α : R) (g g' : HeckeGen (A := A) h)
    (c : ℕ → R) (h0 : c 0 = s * μ₁) (hstep : ∀ L, c (L + 1) = -h ^ 2 * c L) :
    -((g.σ - g.σinv) * (g'.σ - g'.σinv)) = algebraMap R A (-h ^ 2) ∧
    (∀ L, c L = formBCoeff s h μ₁ L) ∧
    c 0 * α + c 1 * α ^ 2 = α * (s * μ₁) * (1 - h ^ 2 * α) ∧
    connected (formBMeasure μ₁) = μ₁ - μ₁ ^ 2 ∧
    Factorizes (thetaMeasure μ₁) := by
  have hrec := formB_coeff_of_recursion s h μ₁ c h0 hstep
  refine ⟨barOdd_eq g g', hrec, ?_, formB_connected μ₁, theta_factorizes μ₁⟩
  rw [hrec 0, hrec 1]
  unfold formBCoeff
  ring

end ConstructiveEmTreeAndLoopLadder

/-! ## Section 3: Ordered-Ring Monotonicity & Proton-Pinned `LawvereCut.Cut ℚ` for `α_EM⁻¹` & `R_∞` -/

section OrderedRingAndProtonEmCut

/-- Denominator-cleared Form-B inverse-coupling cubic in `A = 1 / α_EM`:
`emFormBClearedInvCubic T0 H h2H A = A³ - T0 * A² - H * A + h2H` (`h2H = h² H`). -/
def emFormBClearedInvCubic {K : Type*} [CommRing K] (T0 H h2H A : K) : K :=
  A ^ 3 - T0 * A ^ 2 - H * A + h2H

/-- **Strict monotonicity above `B` over any strict ordered commutative ring (`0` `[Field]`):**
Whenever `1 ≤ B`, `4 * T0 ≤ 6 * B - 4`, and `H ≤ B`, `emFormBClearedInvCubic T0 H h2H` is strictly
increasing on `{A : K | B ≤ A}` (e.g. `B = 100`, `T0 ≤ 140`, `H ≤ 1`). -/
theorem emFormBClearedInvCubic_strictMono_above
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    {T0 H h2H B : K} (hB : 1 ≤ B) (hTB : 4 * T0 ≤ 6 * B - 4) (hHB : H ≤ B)
    {A₁ A₂ : K} (hA1 : B ≤ A₁) (hlt : A₁ < A₂) :
    emFormBClearedInvCubic T0 H h2H A₁ < emFormBClearedInvCubic T0 H h2H A₂ := by
  have hdiff :
      emFormBClearedInvCubic T0 H h2H A₂ - emFormBClearedInvCubic T0 H h2H A₁ =
        (A₂ - A₁) * (A₂ ^ 2 + A₁ * A₂ + A₁ ^ 2 - T0 * (A₂ + A₁) - H) := by
    unfold emFormBClearedInvCubic; ring
  have hsub_pos : 0 < A₂ - A₁ := sub_pos.mpr hlt
  have hsum_gt : 2 * B < A₂ + A₁ := by linarith
  have h3sum : 4 ≤ 3 * (A₂ + A₁) - 4 * T0 := by linarith
  have h4quad : 4 * B < 4 * (A₂ ^ 2 + A₁ * A₂ + A₁ ^ 2 - T0 * (A₂ + A₁)) := by
    have hid :
        4 * (A₂ ^ 2 + A₁ * A₂ + A₁ ^ 2 - T0 * (A₂ + A₁)) =
          (A₂ - A₁) ^ 2 + (A₂ + A₁) * (3 * (A₂ + A₁) - 4 * T0) := by ring
    rw [hid]
    have hsq : 0 < (A₂ - A₁) ^ 2 := sq_pos_of_pos hsub_pos
    have h40 : (0 : K) ≤ 4 := by norm_num
    have hsum_nonneg : 0 ≤ A₂ + A₁ := by linarith
    have hm := mul_le_mul hsum_gt.le h3sum h40 hsum_nonneg
    linarith
  have hquad : 0 < A₂ ^ 2 + A₁ * A₂ + A₁ ^ 2 - T0 * (A₂ + A₁) - H := by linarith
  have hprod : 0 < (A₂ - A₁) * (A₂ ^ 2 + A₁ * A₂ + A₁ ^ 2 - T0 * (A₂ + A₁) - H) :=
    mul_pos hsub_pos hquad
  linarith

/-- Lower endpoint of the proton-pinned `LawvereCut.Cut ℚ` interval for Form-B `α_EM⁻¹(q₀)`
(`1370359991268 / 10¹⁰`, strictly proton-pinned per owner ruling `2026-11-28`). -/
def emInvAlphaProtonLo : ℚ := 1370359991268 / 10000000000

/-- Upper endpoint of the proton-pinned `LawvereCut.Cut ℚ` interval for Form-B `α_EM⁻¹(q₀)`
(`1370359991271 / 10¹⁰`, width `3 × 10⁻¹⁰`, relative width `0.00219 ppb`). -/
def emInvAlphaProtonHi : ℚ := 1370359991271 / 10000000000

/-- Constructive `LawvereCut.Cut ℚ` observable bracketing proton-pinned Form-B `α_EM⁻¹(q₀)`. -/
def emInvAlphaProtonCut : Cut ℚ :=
  Cut.ofInterval emInvAlphaProtonLo emInvAlphaProtonHi
    (by unfold emInvAlphaProtonLo emInvAlphaProtonHi; norm_num)

/-- Constructive `LawvereCut.Cut ℚ` observable bracketing the dimensionless Rydberg coupling factor
`R_∞ / m_e = α_EM² / 2 = 1 / (2 A²)` on the proton pin. -/
def rydbergFactorProtonLo : ℚ := 1 / (2 * emInvAlphaProtonHi ^ 2)

/-- Upper endpoint of the dimensionless Rydberg coupling factor `α_EM² / 2 = 1 / (2 A²)`. -/
def rydbergFactorProtonHi : ℚ := 1 / (2 * emInvAlphaProtonLo ^ 2)

/-- Constructive `LawvereCut.Cut ℚ` observable for the dimensionless Form-B Rydberg factor `α_EM² / 2`. -/
def rydbergFactorProtonCut : Cut ℚ :=
  Cut.ofInterval rydbergFactorProtonLo rydbergFactorProtonHi
    (by unfold rydbergFactorProtonLo rydbergFactorProtonHi emInvAlphaProtonLo emInvAlphaProtonHi; norm_num)

/-- **Proton-pinned `LawvereCut` interval certificate for Form-B `α_EM⁻¹(q₀)` and `R_∞ / m_e`:**
For every `(T0, H, h2H : ℚ)` inside the certified proton-pin enclosure
`T0 ∈ [137035415444371/10¹², 34258853861093/2.5×10¹¹]`,
`H ∈ [312543141/3906250000, 80011044097/10¹²]`,
`h2H ∈ [1748489689/5×10¹¹, 3496979379/10¹²]`,
`emFormBClearedInvCubic T0 H h2H emInvAlphaProtonLo < 0 < emFormBClearedInvCubic T0 H h2H emInvAlphaProtonHi`,
every root `A ≥ 100` lies inside `emInvAlphaProtonCut`, and its induced Rydberg factor `1 / (2 A²)`
lies inside `rydbergFactorProtonCut`. -/
theorem emFormB_and_rydberg_proton_cut_certified :
    emInvAlphaProtonCut.WithinResolution (3 / 10000000000) ∧
    (∀ T0 H h2H : ℚ,
      137035415444371 / 1000000000000 ≤ T0 → T0 ≤ 34258853861093 / 250000000000 →
      312543141 / 3906250000 ≤ H → H ≤ 80011044097 / 1000000000000 →
      1748489689 / 500000000000 ≤ h2H → h2H ≤ 3496979379 / 1000000000000 →
      emFormBClearedInvCubic T0 H h2H emInvAlphaProtonLo < 0 ∧
      0 < emFormBClearedInvCubic T0 H h2H emInvAlphaProtonHi ∧
      ∀ A : ℚ, 100 ≤ A → emFormBClearedInvCubic T0 H h2H A = 0 →
        emInvAlphaProtonCut.Contains A ∧ rydbergFactorProtonCut.Contains (1 / (2 * A ^ 2))) := by
  refine ⟨?_, ?_⟩
  · have hres :=
      Cut.ofInterval_withinResolution emInvAlphaProtonLo emInvAlphaProtonHi
        (by unfold emInvAlphaProtonLo emInvAlphaProtonHi; norm_num)
    have hwidth : emInvAlphaProtonHi - emInvAlphaProtonLo ≤ 3 / 10000000000 := by
      unfold emInvAlphaProtonLo emInvAlphaProtonHi; norm_num
    exact hres.mono hwidth
  · intro T0 H h2H hTlo hThi hHlo hHhi hh2lo hh2hi
    have hlo_bound :
        emFormBClearedInvCubic (137035415444371 / 1000000000000) (312543141 / 3906250000)
          (3496979379 / 1000000000000) emInvAlphaProtonLo < 0 := by
      unfold emFormBClearedInvCubic emInvAlphaProtonLo; norm_num
    have hhi_bound :
        0 < emFormBClearedInvCubic (34258853861093 / 250000000000) (80011044097 / 1000000000000)
          (1748489689 / 500000000000) emInvAlphaProtonHi := by
      unfold emFormBClearedInvCubic emInvAlphaProtonHi; norm_num
    have hlo_sq : 0 ≤ emInvAlphaProtonLo ^ 2 := sq_nonneg _
    have hlo_pos : 0 ≤ emInvAlphaProtonLo := by unfold emInvAlphaProtonLo; norm_num
    have hhi_sq : 0 ≤ emInvAlphaProtonHi ^ 2 := sq_nonneg _
    have hhi_pos : 0 ≤ emInvAlphaProtonHi := by unfold emInvAlphaProtonHi; norm_num
    have hlo_le :
        emFormBClearedInvCubic T0 H h2H emInvAlphaProtonLo ≤
          emFormBClearedInvCubic (137035415444371 / 1000000000000) (312543141 / 3906250000)
            (3496979379 / 1000000000000) emInvAlphaProtonLo := by
      unfold emFormBClearedInvCubic
      have ht : (137035415444371 / 1000000000000) * emInvAlphaProtonLo ^ 2 ≤ T0 * emInvAlphaProtonLo ^ 2 :=
        mul_le_mul_of_nonneg_right hTlo hlo_sq
      have hh : (312543141 / 3906250000) * emInvAlphaProtonLo ≤ H * emInvAlphaProtonLo :=
        mul_le_mul_of_nonneg_right hHlo hlo_pos
      linarith
    have hhi_ge :
        emFormBClearedInvCubic (34258853861093 / 250000000000) (80011044097 / 1000000000000)
            (1748489689 / 500000000000) emInvAlphaProtonHi ≤
          emFormBClearedInvCubic T0 H h2H emInvAlphaProtonHi := by
      unfold emFormBClearedInvCubic
      have ht : T0 * emInvAlphaProtonHi ^ 2 ≤ (34258853861093 / 250000000000) * emInvAlphaProtonHi ^ 2 :=
        mul_le_mul_of_nonneg_right hThi hhi_sq
      have hh : H * emInvAlphaProtonHi ≤ (80011044097 / 1000000000000) * emInvAlphaProtonHi :=
        mul_le_mul_of_nonneg_right hHhi hhi_pos
      linarith
    have hlo_neg : emFormBClearedInvCubic T0 H h2H emInvAlphaProtonLo < 0 :=
      lt_of_le_of_lt hlo_le hlo_bound
    have hhi_pos_val : 0 < emFormBClearedInvCubic T0 H h2H emInvAlphaProtonHi :=
      lt_of_lt_of_le hhi_bound hhi_ge
    refine ⟨hlo_neg, hhi_pos_val, ?_⟩
    intro A hA hr
    have hTB : 4 * T0 ≤ 6 * (100 : ℚ) - 4 := by linarith
    have hHB : H ≤ (100 : ℚ) := by linarith
    have hAlo : emInvAlphaProtonLo < A := by
      by_contra hle
      push_neg at hle
      rcases lt_or_eq_of_le hle with hlt | rfl
      · have hm :=
          emFormBClearedInvCubic_strictMono_above (h2H := h2H) (B := (100 : ℚ))
            (by norm_num) hTB hHB hA hlt
        linarith
      · linarith
    have hAhi : A < emInvAlphaProtonHi := by
      by_contra hge
      push_neg at hge
      rcases lt_or_eq_of_le hge with hlt | rfl
      · have hm :=
          emFormBClearedInvCubic_strictMono_above (h2H := h2H) (B := (100 : ℚ))
            (by norm_num) hTB hHB (by unfold emInvAlphaProtonHi; norm_num) hlt
        linarith
      · linarith
    have hcontainA : emInvAlphaProtonCut.Contains A :=
      ⟨fun a ha => le_trans ha hAlo.le, fun b hb => le_trans hAhi.le hb⟩
    refine ⟨hcontainA, ?_⟩
    have hlo_strict : 0 < emInvAlphaProtonLo := by unfold emInvAlphaProtonLo; norm_num
    have hA_pos : 0 < A := lt_trans hlo_strict hAlo
    have hsq_lo : 2 * emInvAlphaProtonLo ^ 2 ≤ 2 * A ^ 2 := by nlinarith
    have hsq_hi : 2 * A ^ 2 ≤ 2 * emInvAlphaProtonHi ^ 2 := by nlinarith
    have hden_lo_pos : 0 < 2 * emInvAlphaProtonLo ^ 2 := by positivity
    have hden_A_pos : 0 < 2 * A ^ 2 := by positivity
    have hryd_lo : rydbergFactorProtonLo ≤ 1 / (2 * A ^ 2) :=
      one_div_le_one_div_of_le hden_A_pos hsq_hi
    have hryd_hi : 1 / (2 * A ^ 2) ≤ rydbergFactorProtonHi :=
      one_div_le_one_div_of_le hden_lo_pos hsq_lo
    exact ⟨fun a ha => le_trans ha hryd_lo, fun b hb => le_trans hryd_hi hb⟩

end OrderedRingAndProtonEmCut

/-! ## Section 4: Minimal Open Mathematical Kernels for Form B & Form C (`qou-aemx`) -/

section MinimalFormBAndFormCKernels

/-- **Minimal Form-B Physical Kernel (`§3b-cond`, zero global instances):**
With `ArchimedeanLimit` (`x ∈ (0,1)`), `BlochSuslinRigidity`, `BringMapChain` (`g = 4`, `b₁ = 8`),
`EmPhotonJoinRules` (`-h²`), and `EmFormBLoopMeasure` (`μ_L = μ₁`) all proved unconditionally,
Form-B `α_EM` (and Form-B `R_∞`) rests solely on:
1. Phase-4 one-loop measure hypotheses `GermPeriodShare μ₁ a₀` and `HeatKernelLeadingCoeff a₀`
   (`μ₁ = 1 / (8π)`), and
2. Additive self-energy assembly `1 / α = q [9]_q [10]_q + b₁(Bring) / Area(Bring) + c₀ α + c₁ α²`
   with Form-B ladder coefficients `formBCoeff (q + q⁻¹) (hHecke q) μ₁` (`Δ₂` dropped). -/
class FormBMinimalKernelClass (q μ₁ a₀ α : ℝ) : Prop where
  /-- Hyperbolic substrate regime `1 < q`. -/
  one_lt_q : 1 < q
  /-- Strictly positive electromagnetic coupling `0 < α`. -/
  alpha_pos : 0 < α
  /-- Phase-4 Clause-B / Φ period-share hypothesis (`2 μ₁ = a₀`). -/
  period_share : GermPeriodShare μ₁ a₀
  /-- Phase-4 Clause-A surface heat-kernel leading coefficient (`a₀ = 1/(4π)`). -/
  heat_kernel : HeatKernelLeadingCoeff a₀
  /-- Additive assembly of tree + Bring-map zero-mode + Form-B 1-loop/2-loop skein terms (`Δ₂ = 0`). -/
  additive_assembly :
    1 / α =
      q * qIntBal q 9 * qIntBal q 10 +
      (bringMapBettiOne : ℝ) / bringSurfaceArea +
      formBCoeff (q + q⁻¹) (hHecke q) μ₁ 0 * α +
      formBCoeff (q + q⁻¹) (hHecke q) μ₁ 1 * α ^ 2

/-- **Unconditional Reduction of Form-B `α_EM` (`formBMinimalKernel_imp_twoLoopZeroFixedPoint`):**
Under `[FormBMinimalKernelClass q μ₁ a₀ α]`, `μ₁` is pinned to `(q + q⁻¹)⁻¹ * habiroNorm q`
(`= 1/(8π)`), `α` satisfies `IsTwoLoopBringFixedPoint (q [9]_q [10]_q) 4 q ((hHecke q)²) 0 α`
(`c2_add = 0`), and `twoLoopBringCubic ... 0 α = 0`, with zero `BringZeroModeBlochClass` input. -/
theorem formBMinimalKernel_imp_twoLoopZeroFixedPoint (q μ₁ a₀ α : ℝ)
    [inst : FormBMinimalKernelClass q μ₁ a₀ α] :
    IsTwoLoopBringFixedPoint
      (q * qIntBal q 9 * qIntBal q 10)
      4
      q
      ((hHecke q) ^ 2)
      0
      α ∧
    twoLoopBringCubic
      (q * qIntBal q 9 * qIntBal q 10)
      4
      q
      ((hHecke q) ^ 2)
      0
      α = 0 := by
  haveI : GermPeriodShare μ₁ a₀ := inst.period_share
  haveI : HeatKernelLeadingCoeff a₀ := inst.heat_kernel
  have hhab_mu : (q + q⁻¹) * μ₁ = habiroNorm q := by
    rw [perLoop_eq_inv_eight_pi μ₁ a₀]
    unfold habiroNorm
    ring
  have hb1 : (bringMapBettiOne : ℝ) = 2 * 4 := by
    rw [bringMapBettiOne_eq_eight_and_genus_four.1]
    norm_num
  have hfp :
      IsTwoLoopBringFixedPoint
        (q * qIntBal q 9 * qIntBal q 10) 4 q ((hHecke q) ^ 2) 0 α := by
    unfold IsTwoLoopBringFixedPoint
    have hass := inst.additive_assembly
    unfold formBCoeff at hass
    rw [hb1] at hass
    linear_combination hass + (α * (1 - (hHecke q) ^ 2 * α)) * hhab_mu
  have hα_ne : α ≠ 0 := ne_of_gt inst.alpha_pos
  exact ⟨hfp, (twoLoopBringFixedPoint_iff_cubic _ _ _ _ _ α hα_ne).mp hfp⟩

/-- **Non-vacuity / consistency witness for `FormBMinimalKernelClass` (`def`, NEVER `instance`):**
Constructs an explicit `(q = 2, μ₁, a₀, α)` satisfying `FormBMinimalKernelClass` without
registering any global typeclass instance (`lean-generation` §5). -/
noncomputable def trivialModelFormB :
    ∃ (q μ₁ a₀ α : ℝ), FormBMinimalKernelClass q μ₁ a₀ α := by
  let q : ℝ := 2
  let a₀ : ℝ := habiroNorm 1
  let μ₁ : ℝ := a₀ / 2
  have ha0 : HeatKernelLeadingCoeff a₀ := ⟨by dsimp only [a₀]; unfold habiroNorm; ring⟩
  have hps : GermPeriodShare μ₁ a₀ :=
    QOU.MassTheory.EmPerLoopMeasureConditional.perLoop_share_satisfiable a₀
  have hH_pos : 0 < habiroNorm q := habiroNorm_pos (by dsimp only [q]; norm_num)
  have hHz : habiroNorm q = (3 * (q + q⁻¹) / 16) * bringZeroModeValue :=
    (habiroNorm_eq_rational_mul_zeroModes q).1
  have hHz' : habiroNorm q = (15 / 32) * bringZeroModeValue := by
    rw [hHz]; dsimp only [q]; norm_num
  have hz_pos : 0 < bringZeroModeValue := by linarith
  let t0 : ℝ := q * qIntBal q 9 * qIntBal q 10 + (bringMapBettiOne : ℝ) / bringSurfaceArea
  have hb1_eq : (bringMapBettiOne : ℝ) / bringSurfaceArea = bringZeroModeValue :=
    em_bringZeroMode_from_finite_map.2.2
  have htree_gt : 100 < q * qIntBal q 9 * qIntBal q 10 := by
    rw [QOU.QInteger.qIntBal_def, QOU.QInteger.qIntBal_def]
    dsimp only [q]
    norm_num
  have ht0_gt : 100 < t0 := by
    dsimp only [t0]
    rw [hb1_eq]
    linarith
  have ht0_pos : 0 < t0 := by linarith
  let top : ℝ := 1 / t0
  have htop_pos : 0 < top := one_div_pos.mpr ht0_pos
  let P : ℝ → ℝ := fun x =>
    -((hHecke q) ^ 2) * habiroNorm q * x ^ 3 + habiroNorm q * x ^ 2 + t0 * x - 1
  have hcont : ContinuousOn P (Set.Icc 0 top) := by
    dsimp only [P]
    fun_prop
  have hP0 : P 0 = -1 := by dsimp only [P]; ring
  have hh2_eq : (hHecke q) ^ 2 = 9 / 4 := by
    unfold hHecke; dsimp only [q]; norm_num
  have htop_lt : (9 / 4 : ℝ) * top < 1 := by
    dsimp only [top]
    rw [mul_one_div, div_lt_one ht0_pos]
    linarith
  have hPtop : 0 ≤ P top := by
    have hmul : t0 * top = 1 := mul_one_div_cancel (ne_of_gt ht0_pos)
    have hfac :
        P top = habiroNorm q * top ^ 2 * (1 - (hHecke q) ^ 2 * top) + (t0 * top - 1) := by
      dsimp only [P]; ring
    rw [hfac, hmul, hh2_eq]
    have h1 : 0 ≤ habiroNorm q * top ^ 2 := mul_nonneg hH_pos.le (sq_nonneg top)
    have h2 : 0 ≤ 1 - (9 / 4 : ℝ) * top := by linarith
    nlinarith
  obtain ⟨α, hα_mem, hPα⟩ :=
    intermediate_value_Icc htop_pos.le hcont (by rw [hP0]; exact ⟨by norm_num, hPtop⟩)
  have hα_pos : 0 < α := by
    rcases lt_or_eq_of_le hα_mem.1 with hlt | rfl
    · exact hlt
    · linarith [hP0, hPα]
  have hα_ne : α ≠ 0 := ne_of_gt hα_pos
  haveI : GermPeriodShare μ₁ a₀ := hps
  haveI : HeatKernelLeadingCoeff a₀ := ha0
  have hhab_mu : (q + q⁻¹) * μ₁ = habiroNorm q := by
    rw [perLoop_eq_inv_eight_pi μ₁ a₀]
    unfold habiroNorm
    ring
  refine ⟨q, μ₁, a₀, α,
    { one_lt_q := by dsimp only [q]; norm_num
      alpha_pos := hα_pos
      period_share := hps
      heat_kernel := ha0
      additive_assembly := ?_ }⟩
  rw [div_eq_iff hα_ne]
  unfold formBCoeff
  dsimp only [P, t0] at hPα
  linear_combination -hPα - (α ^ 2 * (1 - (hHecke q) ^ 2 * α)) * hhab_mu

/-- **Unconditional Reduction Summary for Form C (`formC_pinned_and_dilog_duplication_status`):**
1. Boundary `ArchimedeanLimit 0` and the real dilogarithm Landen duplication identity
   `LiTwo x + LiTwo (-x) = (1/2) LiTwo (x²)` (`|x| < 1`) hold unconditionally;
2. Pinning the free parameter `δ` of `AlphaEmTwoLoopBlochSchwingerClass q δ α` to the weight-3
   defect series `deltaB3 q` (`FormCPinned q α`) is equivalent to the **single scalar equation**
   `deltaB3 q = deltaReq q α`, isolating the connected weight-3 measure & canonical arm selection
   (`qou-aemx`) as the sole open Form-C step. -/
theorem formC_pinned_and_dilog_duplication_status
    (q α x : ℝ) (hq : 1 < q) (hα : 0 < α) (hx : |x| < 1) :
    ArchimedeanLimit 0 ∧
    LiTwo x + LiTwo (-x) = (1 / 2) * LiTwo (x ^ 2) ∧
    (FormCPinned q α ↔ deltaB3 q = deltaReq q α) :=
  ⟨archimedeanLimit_zero, LiTwo_duplication x hx, formCPinned_iff hq hα⟩

end MinimalFormBAndFormCKernels

end AlphaEmConditionalReduction
end QOU.StandardModel
