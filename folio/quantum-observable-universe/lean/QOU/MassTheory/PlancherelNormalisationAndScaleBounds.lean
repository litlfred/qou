/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# Plancherel Normalisation of `F_Bor`, Hyperbolic Volume Scaling, Berezinian Cross-Terms, and the `m_e` Scale Floor

This module provides the exact algebraic and structural theorems for five tasks under
the `qou-2002` calibration and anchor-hygiene epic:

1. **Bean `qou-24w9` (`q`-Schur vs Wenzl/Markov Plancherel Normalisation of `F_Bor`)**:
   - Proves that the `[3]_q! / q³` factor in `F_Bor` is identically the inverse
     `q`-Schur Plancherel weight `(y_{(3)}^Schur(q))⁻¹` of the trivial partition `(3)`
     whose content sum is `c((3)) = 0 + 1 + 2 = 3` (`qschur_trivial_inv_eq_fbor_normaliser`).
   - Proves the bar-conjugate duality `y_{(1,1,1)}^Schur(q) = y_{(3)}^Schur(q⁻¹)` and
     `(y_{(1,1,1)}^Schur(q))⁻¹ = q⁶ · (y_{(3)}^Schur(q))⁻¹` (`qschur_bar_conjugate_duality`).
   - Proves that the convention-D Wenzl/Markov weights on `H₃(q)` (`z = q³/(q²+1)`)
     satisfy exact trace normalisation `1 · y_{(3)}^Wenzl + 2 · y_{(2,1)}^Wenzl + 1 · y_{(1,1,1)}^Wenzl = 1`
     (`wenzl_weights_trace_normalised`), that the standard block inverse weight is identically
     the Temperley–Lieb loop factor `(y_{(2,1)}^Wenzl(q))⁻¹ = (q + q⁻¹)² = [2]_q²`
     (`wenzl_standard_block_inv_eq_two_bracket_sq`), and that the Wenzl weights combined with
     the Phase-1c character `χ^{(2,1)}(β_Bor, q)` algebraically reconstruct the Lean-proved
     Borromean Markov trace `tr_M(β_Bor, q) = (4 + h² - 3h⁴ - h⁶)/(h² + 4)`
     (`wenzl_reconstructs_borromean_trM`).
   - Proves the combined `m_μ · F_Bor` bar-asymmetry identity relating `ℏ_q = (q - 1)/q`
     and `ℏ_sym² = q - 2 + q⁻¹` (`net_bar_asymmetry_mmu_fbor`).

2. **Bean `qou-r0dn` (Per-Knot Hyperbolic Volume Scaling & `Vol(6₂)` vs `2·Vol(4₁)`)**:
   - Proves that in the per-knot mass law `m(K) = m_e · (Vol(K)/ℏ_q²) · tr_M(K)`, the ratio
     of predictions at two volume assignments with fixed `(m_e, ℏ_q, tr_M)` equals the pure
     volume ratio `V₁ / V₂`, and the relative error from substituting `2·Vol(4₁)` for `Vol(6₂)`
     is `(2·Vol(4₁) - Vol(6₂)) / Vol(6₂)` independent of `(m_e, ℏ_q, tr_M)`.

3. **Bean `qou-hgm6` (Algebraic Identities for `saddle_offset`, `a3_magnitude_berezinian`, `rho_binding_constancy`)**:
   - Proves that `q_quad = (-9 + √193)/56` is the exact root of the `5₂` Stokes quadratic
     balance `1 - 9q - 28q² = 0` (`saddleQuadPoly_at_qQuadRoot`) and lies strictly in
     `(87/1000, 88/1000)` (`qQuadRoot_bounds`).
   - Proves that the super-Berezinian even-face multiplicative lift `(A - B D⁻¹ C)/A` equals
     `1` at zero mixing (`B = 0`) and equals any target `r*` at the unique fit witness
     `B* = A(1 - r*)D C⁻¹` (`berezinianEvenLift_fit_and_residual`).
   - Proves that under a universal Path-3 calibration `B_K = α_M · |tr_M(K)|`, the scale-free
     ratio `B_K / |tr_M(K)|` is constant across atoms and the `T`/`³He` mirror mismatch
     vanishes (`rho_binding_mirror_mismatch_zero_of_universal`).

4. **Bean `qou-cuur` (Algebraic Purity & Lower Bound of `linking_weight_family_a`)**:
   - Proves that `λ_A(q) = 5/2 + (3/4)(q - 2 + q⁻¹)` is bar-symmetric (`λ_A(q⁻¹) = λ_A(q)`),
     has classical limit `λ_A(1) = 5/2`, satisfies `λ_A(q) - 5/2 = 3(q - 1)²/(4q)`, and
     therefore obeys `λ_A(q) > 5/2 > 2461/1000` for every `q > 0` with `(q - 1)² > 0`
     (`linkingWeightFamilyA_properties`), ruling out any equality with the
     CODATA-inverted proton target `≈ 2.461`.

5. **Bean `qou-zufe` (CODATA `m_e` Relative Uncertainty Floor & Ratio Cancellation)**:
   - Proves that the first-order relative variance of `M = m_e · R` is bounded below by the
     CODATA electron-mass relative variance `σ_rel(m_e)²` (`relVarProduct_ge_me_floor`),
     while `m_e` cancels identically in any dimensionless mass ratio `(m_e R₁)/(m_e R₂) = R₁/R₂`
     (`dimensionless_mass_ratio_cancels_me`).
-/

namespace QOU.MassTheory.PlancherelNormalisationAndScaleBounds

section AlgebraicIdentities

variable {K : Type*} [Field K]

/-! ### 1. Bean `qou-24w9`: `q`-Schur vs Wenzl/Markov Plancherel Normalisation -/

/-- Balanced `[3]_q!^bal = (q + q⁻¹)(q² + 1 + q⁻²)`. -/
def qFactThreeBalanced (q : K) : K := (q + q⁻¹) * (q ^ 2 + 1 + (q⁻¹) ^ 2)

/-- `q`-Schur Plancherel weight for `λ = (3)`, content sum `c((3)) = 0 + 1 + 2 = 3`. -/
def ySchur3 (q : K) : K := q ^ 3 / qFactThreeBalanced q

/-- `q`-Schur Plancherel weight for `λ = (2,1)`, content sum `c((2,1)) = 0 + 1 - 1 = 0`. -/
def ySchur21 (q : K) : K := 1 / qFactThreeBalanced q

/-- `q`-Schur Plancherel weight for `λ = (1,1,1)`, content sum `c((1,1,1)) = 0 - 1 - 2 = -3`. -/
def ySchur111 (q : K) : K := (q ^ 3)⁻¹ / qFactThreeBalanced q

/-- **The `F_Bor` normaliser `[3]_q!^bal / q³` is identically `(y_{(3)}^Schur(q))⁻¹`
and expands to `(1 + 2q² + 2q⁴ + q⁶) / q⁶`.** -/
theorem qschur_trivial_inv_eq_fbor_normaliser (q : K) (hq : q ≠ 0) :
    (ySchur3 q)⁻¹ = qFactThreeBalanced q / q ^ 3 ∧
      (ySchur3 q)⁻¹ = (1 + 2 * q ^ 2 + 2 * q ^ 4 + q ^ 6) / q ^ 6 := by
  constructor
  · unfold ySchur3
    field_simp
  · unfold ySchur3 qFactThreeBalanced
    field_simp
    ring

/-- **Bar-conjugate duality of the extremal `q`-Schur Plancherel weights.**
Under `q ↦ q⁻¹`, the trivial block `(3)` and sign block `(1,1,1)` swap, and their
inverse normalisers differ by `q⁶`. -/
theorem qschur_bar_conjugate_duality (q : K) (hq : q ≠ 0) :
    ySchur111 q = ySchur3 q⁻¹ ∧ (ySchur111 q)⁻¹ = q ^ 6 * (ySchur3 q)⁻¹ := by
  constructor
  · unfold ySchur111 ySchur3 qFactThreeBalanced
    field_simp
    ring
  · unfold ySchur111 ySchur3
    field_simp

/-- Convention-D Wenzl/Markov weight for `λ = (3)` on `H₃(q)`:
`y_{(3)}^Wenzl(q) = (q² + q⁻²) / (q + q⁻¹)²`. -/
def yWenzl3 (q : K) : K := (q ^ 2 + (q ^ 2)⁻¹) / (q + q⁻¹) ^ 2

/-- Convention-D Wenzl/Markov weight for `λ = (2,1)` on `H₃(q)`:
`y_{(2,1)}^Wenzl(q) = 1 / (q + q⁻¹)²`. -/
def yWenzl21 (q : K) : K := 1 / (q + q⁻¹) ^ 2

/-- Convention-D Wenzl/Markov weight for `λ = (1,1,1)` on `H₃(q)` vanishes identically. -/
def yWenzl111 (_q : K) : K := 0

/-- **The Wenzl weights on `H₃(q)` are trace-normalised (`tr_M(1) = 1`).** -/
theorem wenzl_weights_trace_normalised (q : K) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) :
    1 * yWenzl3 q + 2 * yWenzl21 q + 1 * yWenzl111 q = 1 := by
  unfold yWenzl3 yWenzl21 yWenzl111
  field_simp
  ring

/-- **The inverse Wenzl weight of the standard `(2,1)` block is `[2]_q² = (q + q⁻¹)² = (q - q⁻¹)² + 4`.**
This collapses the Wenzl standard-block option and the Temperley–Lieb `δ^{n-1}` option
into a single identity and identifies it with the Borromean trace denominator `h² + 4`. -/
theorem wenzl_standard_block_inv_eq_two_bracket_sq (q : K) (hq : q ≠ 0) :
    (yWenzl21 q)⁻¹ = (q + q⁻¹) ^ 2 ∧
      (yWenzl21 q)⁻¹ = (q - q⁻¹) ^ 2 + 4 := by
  constructor
  · unfold yWenzl21
    field_simp
  · unfold yWenzl21
    field_simp
    ring

/-- Phase-1c character `χ^{(2,1)}(β_Bor, q)` on the 3-strand Borromean braid. -/
def chiBorromean21 (q : K) : K :=
  (-q ^ 12 + 3 * q ^ 10 - 3 * q ^ 8 + 4 * q ^ 6 - 3 * q ^ 4 + 3 * q ^ 2 - 1) / q ^ 6

/-- Lean-proved Borromean Markov trace closed form in terms of `h = q - q⁻¹`. -/
def trMBorromean (q : K) : K :=
  (4 + (q - q⁻¹) ^ 2 - 3 * (q - q⁻¹) ^ 4 - (q - q⁻¹) ^ 6) / ((q - q⁻¹) ^ 2 + 4)

/-- **Three-way algebraic reconstruction**: the convention-D Wenzl weights combined with
the Phase-1c character `χ^{(2,1)}(β_Bor, q)` reproduce `trMBorromean q` identically. -/
theorem wenzl_reconstructs_borromean_trM (q : K) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) :
    yWenzl3 q * 1 + yWenzl21 q * chiBorromean21 q + yWenzl111 q * 1 =
      trMBorromean q := by
  unfold yWenzl3 yWenzl21 yWenzl111 chiBorromean21 trMBorromean
  have hdenom : (q - q⁻¹) ^ 2 + 4 = (q + q⁻¹) ^ 2 := by
    field_simp
    ring
  rw [hdenom]
  field_simp
  ring

/-- **Net bar-asymmetry across `m_μ · F_Bor`.**
Since `ℏ_sym² := q - 2 + q⁻¹ = q · ℏ_q²` where `ℏ_q = (q - 1)/q`, combining `1/ℏ_q²`
with `[3]_q!^bal / q³` leaves a net `q⁻²` asymmetry relative to the bar-symmetric
factor `[3]_q!^bal / ℏ_sym²`. -/
theorem net_bar_asymmetry_mmu_fbor (q : K)
    (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (hsym : q - 2 + q⁻¹ ≠ 0) :
    (q - 2 + q⁻¹) = q * ((q - 1) / q) ^ 2 ∧
      (1 / ((q - 1) / q) ^ 2) * (qFactThreeBalanced q / q ^ 3) =
        qFactThreeBalanced q / (q ^ 2 * (q - 2 + q⁻¹)) := by
  constructor
  · field_simp
    ring
  · field_simp
    ring

/-! ### 2. Bean `qou-r0dn`: Per-Knot Hyperbolic Volume Scaling -/

/-- Per-knot mass prediction `m(K) = m_e · (Vol(K) / ℏ_q²) · tr_M(K)`. -/
def perKnotMass (me vol hbar_q trM : K) : K := me * (vol / hbar_q ^ 2) * trM

/-- **Volume-ratio scaling and relative substitution error.**
At fixed `(m_e, ℏ_q, tr_M)`, the ratio of per-knot mass predictions equals `V₁ / V₂`,
and the relative error of substituting `V_sub` for `V_true` equals `(V_sub - V_true) / V_true`. -/
theorem perKnotMass_ratio_and_rel_err (me V_sub V_true hbar_q trM : K)
    (hme : me ≠ 0) (hV : V_true ≠ 0) (hh : hbar_q ≠ 0) (htr : trM ≠ 0) :
    perKnotMass me V_sub hbar_q trM / perKnotMass me V_true hbar_q trM = V_sub / V_true ∧
      (perKnotMass me V_sub hbar_q trM - perKnotMass me V_true hbar_q trM) /
        perKnotMass me V_true hbar_q trM = (V_sub - V_true) / V_true := by
  unfold perKnotMass
  constructor
  · field_simp
  · field_simp
    ring

/-! ### 3. Bean `qou-hgm6`: Berezinian Cross-Term & `ρ_binding` Constancy -/

/-- Multiplicative lift `(A - B D⁻¹ C) / A` on the bar-even face from the Berezinian
off-diagonal cross-term `t = B D⁻¹ C`. -/
def berezinianEvenLift (A B C D : K) : K := (A - B * D⁻¹ * C) / A

/-- **Zero-mixing, exact surjectivity witness, and residual decomposition of the Berezinian lift.** -/
theorem berezinianEvenLift_fit_and_residual (A B C D rStar : K)
    (hA : A ≠ 0) (hC : C ≠ 0) (hD : D ≠ 0) :
    berezinianEvenLift A 0 C D = 1 ∧
      berezinianEvenLift A (A * (1 - rStar) * D * C⁻¹) C D = rStar ∧
      berezinianEvenLift A B C D - rStar = (A * (1 - rStar) - B * D⁻¹ * C) / A := by
  unfold berezinianEvenLift
  refine ⟨?_, ?_, ?_⟩
  · field_simp
  · field_simp
    ring
  · field_simp
    ring

/-- **Scale-free `ρ_binding` constancy across mirror pairs.**
If `B_T = α_M · t_T` and `B_He3 = α_M · t_He3` share a single universal calibration `α_M`,
then their scale-free ratios `B / |tr_M|` agree identically. -/
theorem rho_binding_mirror_mismatch_zero_of_universal (alphaM tT tHe3 : K)
    (htT : tT ≠ 0) (htHe3 : tHe3 ≠ 0) :
    (alphaM * tT) / tT - (alphaM * tHe3) / tHe3 = 0 := by
  field_simp
  ring

/-- **Dimensionless mass ratios cancel the `m_e` scale factor identically (`qou-zufe`).** -/
theorem dimensionless_mass_ratio_cancels_me (me R1 R2 : K) (hme : me ≠ 0) :
    (me * R1) / (me * R2) = R1 / R2 :=
  mul_div_mul_left R1 R2 hme

end AlgebraicIdentities

section RealBounds

/-! ### 3b. Bean `qou-hgm6`: `5₂` Saddle-Offset Quadratic Balance Root over `ℝ` -/

/-- Quadratic-balance truncation `1 - 9q - 28q²` of the `5₂` Stokes offset series `o(q)`. -/
def saddleQuadPoly (q : ℝ) : ℝ := 1 - 9 * q - 28 * q ^ 2

/-- Closed-form positive root `q_quad(s) = (-9 + s) / 56` for `s² = 193`. -/
noncomputable def qQuadRoot (s : ℝ) : ℝ := (-9 + s) / 56

/-- Rational bracket `13.872² < 193 < 13.928²` certifying `√193 ∈ (13.872, 13.928)`. -/
theorem discriminant_193_rational_bracket :
    ((13872 : ℝ) / 1000) ^ 2 < 193 ∧ (193 : ℝ) < ((13928 : ℝ) / 1000) ^ 2 := by
  constructor <;> norm_num

/-- **For `s² = 193` with `13.872 < s < 13.928`, `qQuadRoot s` is an exact root of
`1 - 9q - 28q² = 0` and satisfies `0.087 < qQuadRoot s < 0.088`.** -/
theorem saddleQuadPoly_at_qQuadRoot_and_bounds (s : ℝ)
    (hs : s ^ 2 = 193)
    (hlo : (13872 : ℝ) / 1000 < s)
    (hhi : s < (13928 : ℝ) / 1000) :
    saddleQuadPoly (qQuadRoot s) = 0 ∧
      (87 : ℝ) / 1000 < qQuadRoot s ∧ qQuadRoot s < (88 : ℝ) / 1000 := by
  unfold saddleQuadPoly qQuadRoot
  refine ⟨?_, by linarith, by linarith⟩
  linear_combination -hs / 112

/-! ### 4. Bean `qou-cuur`: Algebraic Purity & Strict Lower Bound of `linking_weight_family_a` -/

/-- Closed-form Family-A linking weight `λ_A(q) = 5/2 + (3/4)(q - 2 + q⁻¹)`. -/
noncomputable def linkingWeightFamilyA (q : ℝ) : ℝ :=
  5 / 2 + (3 / 4) * (q - 2 + q⁻¹)

/-- **`λ_A(q)` is bar-symmetric, equals `5/2` at `q = 1`, and satisfies `λ_A(q) > 5/2 > 2.461`
for every `q > 0` with `(q - 1)² > 0`.**
This proves algebraically that `linking_weight_family_a` is a parameter-free closed form
bounded strictly above the CODATA-inverted proton target (`≈ 2.461`). -/
theorem linkingWeightFamilyA_properties (q : ℝ) (hq : 0 < q) (hsq : 0 < (q - 1) ^ 2) :
    linkingWeightFamilyA q⁻¹ = linkingWeightFamilyA q ∧
      linkingWeightFamilyA 1 = 5 / 2 ∧
      linkingWeightFamilyA q - 5 / 2 = 3 * (q - 1) ^ 2 / (4 * q) ∧
      (2461 : ℝ) / 1000 < 5 / 2 ∧
      5 / 2 < linkingWeightFamilyA q := by
  have hq_ne : q ≠ 0 := ne_of_gt hq
  refine ⟨?_, ?_, ?_, by norm_num, ?_⟩
  · unfold linkingWeightFamilyA
    field_simp
    ring
  · unfold linkingWeightFamilyA
    norm_num
  · unfold linkingWeightFamilyA
    field_simp
    ring
  · have hdiff : linkingWeightFamilyA q - 5 / 2 = 3 * (q - 1) ^ 2 / (4 * q) := by
      unfold linkingWeightFamilyA
      field_simp
      ring
    have hpos : 0 < 3 * (q - 1) ^ 2 / (4 * q) := by positivity
    linarith

/-! ### 5. Bean `qou-zufe`: CODATA `m_e` Relative Uncertainty Floor -/

/-- First-order relative variance `(σ_M / M)² = (σ_{m_e} / m_e)² + (σ_R / R)²`
for a dimensional mass prediction `M = m_e · R`. -/
def relVarProduct (relSigmaMe relSigmaR : ℝ) : ℝ :=
  relSigmaMe ^ 2 + relSigmaR ^ 2

/-- **Every dimensional MeV claim `M = m_e · R` has relative variance bounded below by
`relSigmaMe²`, with excess equal to `relSigmaR² ≥ 0`.** -/
theorem relVarProduct_ge_me_floor (relSigmaMe relSigmaR : ℝ) (hR : 0 ≤ relSigmaR ^ 2) :
    relSigmaMe ^ 2 ≤ relVarProduct relSigmaMe relSigmaR ∧
      relVarProduct relSigmaMe relSigmaR - relSigmaMe ^ 2 = relSigmaR ^ 2 := by
  unfold relVarProduct
  constructor
  · linarith
  · ring

end RealBounds

end QOU.MassTheory.PlancherelNormalisationAndScaleBounds
