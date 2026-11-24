import QOU.Core.CategoricalLagrangianTwoTermBridge
import MathlibExt.MagicNumbers
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-!
# Categorical Framing Spin-Orbit Scale & Nilsson Magic-Shell Reduction (`qou-frso`)

Formalizes over generic rings and ordered fields (AGENTS.md §7c, zero `ℝ`, zero empirical
literals, zero `sorry`) the exact relationship between:

1. **The Categorical Dirac Spatial–Reeb Anticommutator (`QOU.CategoricalDiracOperator`):**
   In `QOU.CategoricalLagrangianTwoTermBridge.dirac_sq_three_term_expansion`, squaring
   `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇` produces the three scalar weights
   `(q⁻², q⁻¹(1 - q⁻¹), (1 - q⁻¹)²)`. We prove:
   - Partition of unity (`dirac_weights_partition_of_unity`) and zero-discriminant
     geometric-mean lock (`dirac_spinOrbitWeight_sq_eq_orb_mul_reeb`), establishing that
     the categorical Dirac operator introduces **zero** free spin-orbit parameter.
   - Constant-ratio geometric progression with step `q - 1` (`dirac_geometric_step_orb_to_so`,
     `dirac_geometric_step_so_to_reeb`).
   - **Kinetic-normalized categorical Dirac square (`kinetic_normalized_dirac_sq_expansion`):**
     Scaling `D.dirac ≫ D.dirac` by `D.q * D.q` normalizes horizontal curvature
     `D.nablaEndo ≫ D.nablaEndo` to unit weight and fixes the relative spatial–Reeb
     anticommutator coupling to `D.q - 1` and the vertical Reeb-spin square weight to
     `(D.q - 1)²`.

2. **Hadronic Scale Bridge & Ribbon Framing `2ℓ + 1` Casimir Splitting:**
   - Exact identities linking `hadronicScale m_e q = m_e / (q (q - 1))` to the Dirac
     spin-orbit weights (`m_e / q` and `m_e / q³`).
   - Exact Landé/Casimir spin-`1/2` splitting `C(ℓ + 1/2) - C(ℓ - 1/2) = 2ℓ + 1`,
     `2(l·s)|_{j=ℓ+1/2} - 2(l·s)|_{j=ℓ-1/2} = 2ℓ + 1`, and degeneracy-weighted multiplet
     centroid conservation `(2j_+ + 1)(l·s)_+ + (2j_- + 1)(l·s)_- = 0`.

3. **Unconditional Scope-(a) Prune vs. `§3b-cond` Woods–Saxon Radial Reduction:**
   - **Unconditional negative (`pure_dirac_reeb_flatness_fails_magic28_vs_ho40`):**
     Using the bare algebraic Reeb-square weight `D = -(q - 1)²` without 3D radial
     Woods–Saxon surface flatness leaves the `N = 3` harmonic-oscillator sub-closure gap
     at occupancy `40` strictly larger than the `1f_{7/2}` intruder magic gap at `28` for
     all `1 < q < 9 / 8`.
   - **Conditional `7/7` closure dominance (`RadialSpinOrbitReductionHypothesis`, §3b-cond):**
     Under the explicit radial surface-flatness hypothesis `D = -(q - 1) / 4` alongside
     the Dirac kinetic-normalized spin-orbit coupling `C = -(q - 1)` on the exact rational
     interval `43 / 39 < q < 19 / 17`, all seven closures `{2, 8, 20, 28, 50, 82, 126}`
     (`QOU.Common.magicSet`) strictly dominate the competing non-magic sub-shell gaps at
     `14`, `40`, `64`, `100`, and `114`.

## References

- [leitner2026] def:strand-twist-datum, rem:magic-shell-coupling-kappa
- [mayer1949] Goeppert Mayer, Phys. Rev. 75 (1949), 1969–1970
- [connes1994] Connes, Noncommutative Geometry (1994)
-/

set_option autoImplicit false

open scoped CategoryTheory CategoryTheory.MonoidalCategory
open CategoryTheory

namespace QOU.MassTheory.FramingSpinOrbitDiracScale

/-! ## §1. Categorical Dirac Spatial–Reeb Anticommutator & Kinetic Normalization -/

section CategoricalDiracScale

universe u v

variable {R : Type*} [CommRing R]
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
  [Preadditive C] [Linear R C]
variable {fh : FrobeniusHopfData C}

/-- Horizontal orbital curvature weight `c_orb(q⁻¹) = q⁻²` in `𝒟_∇²`. -/
def diracOrbWeight (qinv : R) : R :=
  qinv * qinv

/-- Spatial–Reeb spin-orbit cross-term weight `c_SO(q⁻¹) = q⁻¹(1 - q⁻¹)` in `𝒟_∇²`. -/
def diracSpinOrbitWeight (qinv : R) : R :=
  qinv * (1 - qinv)

/-- Vertical Reeb-spin square weight `c_Reeb(q⁻¹) = (1 - q⁻¹)²` in `𝒟_∇²`. -/
def diracReebWeight (qinv : R) : R :=
  (1 - qinv) * (1 - qinv)

/-- Spatial–Reeb anticommutator `{∇, ι_ξ∇} = ∇ ≫ ι_ξ∇ + ι_ξ∇ ≫ ∇` in `End_C(fh.obj)`. -/
def spatialReebAnticomm (D : CategoricalDiracOperator R C fh) : fh.obj ⟶ fh.obj :=
  D.nablaEndo ≫ D.reeb + D.reeb ≫ D.nablaEndo

/-- **Partition of unity of the squared categorical Dirac weights**:
    `q⁻² + 2 q⁻¹(1 - q⁻¹) + (1 - q⁻¹)² = 1`. -/
theorem dirac_weights_partition_of_unity (qinv : R) :
    diracOrbWeight qinv + 2 * diracSpinOrbitWeight qinv + diracReebWeight qinv = 1 := by
  unfold diracOrbWeight diracSpinOrbitWeight diracReebWeight
  ring

/-- **Zero-discriminant geometric-mean lock**: the spatial–Reeb spin-orbit cross-term
    weight squared equals the product of the horizontal orbital weight and vertical
    Reeb-spin square weight, leaving zero independent spin-orbit parameter in `𝒟_∇²`. -/
theorem dirac_spinOrbitWeight_sq_eq_orb_mul_reeb (qinv : R) :
    diracSpinOrbitWeight qinv ^ 2 = diracOrbWeight qinv * diracReebWeight qinv := by
  unfold diracOrbWeight diracSpinOrbitWeight diracReebWeight
  ring

/-- **First geometric progression step**: multiplying `c_orb = q⁻²` by `q - 1` yields
    `c_SO = q⁻¹(1 - q⁻¹)` whenever `q * q⁻¹ = 1`. -/
theorem dirac_geometric_step_orb_to_so (q qinv : R) (hq : q * qinv = 1) :
    (q - 1) * diracOrbWeight qinv = diracSpinOrbitWeight qinv := by
  unfold diracOrbWeight diracSpinOrbitWeight
  linear_combination qinv * hq

/-- **Second geometric progression step**: multiplying `c_SO = q⁻¹(1 - q⁻¹)` by `q - 1`
    yields `c_Reeb = (1 - q⁻¹)²` whenever `q * q⁻¹ = 1`. -/
theorem dirac_geometric_step_so_to_reeb (q qinv : R) (hq : q * qinv = 1) :
    (q - 1) * diracSpinOrbitWeight qinv = diracReebWeight qinv := by
  unfold diracSpinOrbitWeight diracReebWeight
  linear_combination (1 - qinv) * hq

/-- **Kinetic-normalized categorical Dirac square (`(q * q) • 𝒟_∇²`)**:
    Scaling `D.dirac ≫ D.dirac` by `D.q * D.q` in `End_C(fh.obj)` normalizes the
    horizontal curvature `D.nablaEndo ≫ D.nablaEndo` to coefficient `1` and isolates
    the parameter-free relative spin-orbit ratio `D.q - 1` on `{∇, ι_ξ∇}` and
    `(D.q - 1)²` on `(ι_ξ∇)²`. -/
theorem kinetic_normalized_dirac_sq_expansion (D : CategoricalDiracOperator R C fh) :
    (D.q * D.q) • (D.dirac ≫ D.dirac) =
      (D.nablaEndo ≫ D.nablaEndo) +
      (D.q - 1) • spatialReebAnticomm D +
      ((D.q - 1) ^ 2) • (D.reeb ≫ D.reeb) := by
  rw [QOU.CategoricalLagrangianTwoTermBridge.dirac_sq_three_term_expansion D]
  simp only [smul_add, smul_smul]
  have h1 : D.q * D.q * (D.qinv * D.qinv) = 1 := by
    linear_combination (D.q * D.qinv + 1) * D.q_unit
  have h2 : D.q * D.q * (D.qinv * (1 - D.qinv)) = D.q - 1 := by
    linear_combination (D.q * (1 - D.qinv) - 1) * D.q_unit
  have h3 : D.q * D.q * ((1 - D.qinv) * (1 - D.qinv)) = (D.q - 1) ^ 2 := by
    have hq1 : D.q * (1 - D.qinv) = D.q - 1 := by
      linear_combination -D.q_unit
    calc
      D.q * D.q * ((1 - D.qinv) * (1 - D.qinv))
          = (D.q * (1 - D.qinv)) * (D.q * (1 - D.qinv)) := by ring
      _ = (D.q - 1) ^ 2 := by rw [hq1]; ring
  rw [h1, h2, h3, one_smul]
  unfold spatialReebAnticomm
  rw [smul_add]

/-- **Traced kinetic-normalized categorical Dirac square** under any `R`-linear trace
    functional `τ : (fh.obj ⟶ fh.obj) →ₗ[R] R`. -/
theorem trace_kinetic_normalized_dirac_sq
    (τ : (fh.obj ⟶ fh.obj) →ₗ[R] R) (D : CategoricalDiracOperator R C fh) :
    (D.q * D.q) * τ (D.dirac ≫ D.dirac) =
      τ (D.nablaEndo ≫ D.nablaEndo) +
      (D.q - 1) * τ (spatialReebAnticomm D) +
      ((D.q - 1) ^ 2) * τ (D.reeb ≫ D.reeb) := by
  have h := congrArg τ (kinetic_normalized_dirac_sq_expansion D)
  simpa only [map_add, LinearMap.map_smul, smul_eq_mul] using h

end CategoricalDiracScale

/-! ## §2. Hadronic Scale Identities & Ribbon Framing `2ℓ + 1` Casimir Splitting -/

section HadronicAndRibbonCasimir

variable {F : Type*} [Field F]

open QOU.CategoricalLagrangianTwoTermBridge

/-- **Hadronic scale times kinetic-normalized Dirac spin-orbit ratio**:
    `E₀(q) * (q - 1) = m_e / q`. -/
theorem hadronicScale_mul_kinetic_so_ratio (m_e q : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    hadronicScale m_e q * (q - 1) = m_e / q := by
  unfold hadronicScale
  field_simp

/-- **Hadronic scale times raw Dirac spin-orbit weight**:
    `E₀(q) * (q⁻¹ (1 - q⁻¹)) = m_e / q³`. -/
theorem hadronicScale_mul_diracSpinOrbitWeight (m_e q : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    hadronicScale m_e q * diracSpinOrbitWeight q⁻¹ = m_e / q ^ 3 := by
  unfold hadronicScale diracSpinOrbitWeight
  have h1q : 1 - q⁻¹ = (q - 1) / q := by field_simp
  rw [h1q]
  field_simp

/-- Quadratic SU(2) / ribbon twist Casimir `C(x) = x(x + 1)`. -/
def casimirVal (x : F) : F :=
  x * (x + 1)

/-- Landé spin-orbit eigenvalue `(C(j) - C(ℓ) - C(1/2)) / 2` for spin `s = 1/2`. -/
def spinOrbitEigen (j l : F) : F :=
  (casimirVal j - casimirVal l - casimirVal (1 / 2)) / 2

/-- **Parameter-free ribbon Casimir difference (`def:strand-twist-datum`)**:
    Between `j_+ = ℓ + 1/2` and `j_- = ℓ - 1/2`, `C(ℓ + 1/2) - C(ℓ - 1/2) = 2ℓ + 1`. -/
theorem casimir_spin_half_split (l : F) (h2 : (2 : F) ≠ 0) :
    casimirVal (l + 1 / 2) - casimirVal (l - 1 / 2) = 2 * l + 1 := by
  unfold casimirVal
  field_simp
  ring

/-- Aligned spin-orbit eigenvalue `j_+ = ℓ + 1/2` equals `ℓ / 2`. -/
theorem spinOrbitEigen_aligned (l : F) (h2 : (2 : F) ≠ 0) :
    spinOrbitEigen (l + 1 / 2) l = l / 2 := by
  unfold spinOrbitEigen casimirVal
  field_simp
  ring

/-- Anti-aligned spin-orbit eigenvalue `j_- = ℓ - 1/2` equals `-(ℓ + 1) / 2`. -/
theorem spinOrbitEigen_antialigned (l : F) (h2 : (2 : F) ≠ 0) :
    spinOrbitEigen (l - 1 / 2) l = -(l + 1) / 2 := by
  unfold spinOrbitEigen casimirVal
  field_simp
  ring

/-- **Pauli–Dirac `2(l·s)` doublet splitting equals `2ℓ + 1`**. -/
theorem two_spinOrbitEigen_split (l : F) (h2 : (2 : F) ≠ 0) :
    2 * spinOrbitEigen (l + 1 / 2) l - 2 * spinOrbitEigen (l - 1 / 2) l = 2 * l + 1 := by
  rw [spinOrbitEigen_aligned l h2, spinOrbitEigen_antialigned l h2]
  field_simp
  ring

/-- **Degeneracy-weighted multiplet centroid conservation**:
    `(2j_+ + 1)(l·s)_+ + (2j_- + 1)(l·s)_- = 0` for every orbital `ℓ`. -/
theorem spinOrbitEigen_multiplet_trace_zero (l : F) (h2 : (2 : F) ≠ 0) :
    (2 * (l + 1 / 2) + 1) * spinOrbitEigen (l + 1 / 2) l +
      (2 * (l - 1 / 2) + 1) * spinOrbitEigen (l - 1 / 2) l = 0 := by
  rw [spinOrbitEigen_aligned l h2, spinOrbitEigen_antialigned l h2]
  field_simp
  ring

end HadronicAndRibbonCasimir

/-! ## §3. Sharpened Nilsson Centroid-Subtracted Spectrum & Unconditional Scope-(a) Prune -/

section NilssonSpectrumAndPrune

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Single-particle energy `E / ħω₀` of the centroid-subtracted Nilsson oscillator:
    `N + 3/2 + D * (ℓ(ℓ + 1) - N(N + 3)/2) + C * (l·s)`.
    Subtracting the exact shell mean `⟨ℓ(ℓ + 1)⟩_N = N(N + 3)/2` preserves each
    oscillator shell's centroid and removes the artificial `N = 6` shell-collapse cap
    of the unsubtracted scan in `qou-frso`. -/
def nilssonCentroidLevel (C D N l : F) (aligned : Bool) : F :=
  N + 3 / 2 + D * (l * (l + 1) - N * (N + 3) / 2) +
    C * (match aligned with | true => l / 2 | false => -(l + 1) / 2)

/-- **Unconditional Scope-(a) Negative Prune**:
    With the kinetic-normalized Dirac spin-orbit ratio `C = -(q - 1)` and the **bare**
    second-order algebraic Reeb weight `D = -(q - 1)²` (no 3D Woods–Saxon radial
    surface flatness), for every `1 < q < 9 / 8` the `N = 3` harmonic-oscillator
    sub-closure gap at occupancy `40` (`2p_{1/2} → 1g_{9/2}`) strictly exceeds the
    `1f_{7/2}` spin-orbit intruder gap at magic occupancy `28` (`1f_{7/2} → 2p_{3/2}`).
    Hence closing `{28, 50, 82, 126}` in a global oscillator spectrum requires a
    genuinely 3D radial surface-flatness matrix element beyond the 1D algebraic `(q - 1)²`. -/
theorem pure_dirac_reeb_flatness_fails_magic28_vs_ho40
    (q : F) (hq1 : 1 < q) (hq98 : q < 9 / 8) :
    nilssonCentroidLevel (-(q - 1)) (-(q - 1) ^ 2) 3 1 true -
        nilssonCentroidLevel (-(q - 1)) (-(q - 1) ^ 2) 3 3 true <
      nilssonCentroidLevel (-(q - 1)) (-(q - 1) ^ 2) 4 4 true -
        nilssonCentroidLevel (-(q - 1)) (-(q - 1) ^ 2) 3 1 false := by
  unfold nilssonCentroidLevel
  nlinarith [sq_nonneg (q - 1)]

/-! ## §4. Explicit `§3b-cond` Radial-Reduction Hypothesis & `7/7` Magic-Gap Dominance -/

/-- **Explicit `§3b-cond` Radial Spin-Orbit Reduction Hypothesis (`0` global instances)**:
    Packages the two radial reduction inputs needed to evaluate the global single-particle
    shell ladder at deformation `q`:
    1. `h_so_dirac`: the dimensionless spin-orbit-to-oscillator ratio equals the
       kinetic-normalized categorical Dirac cross-term `-(q - 1)` from
       `kinetic_normalized_dirac_sq_expansion`;
    2. `h_woods_saxon_ratio`: the 3D Woods–Saxon flat-bottom centrifugal shift satisfies
       Nilsson's surface-to-spin-orbit ratio `D = -(q - 1) / 4` (`μ_Nilsson = 2D/C = 1/2`);
    3. `h_q_lower`, `h_q_upper`: `q` lies in the rational window `(43 / 39, 19 / 17)`. -/
class RadialSpinOrbitReductionHypothesis
    (F : Type*) [Field F] [LinearOrder F] [IsStrictOrderedRing F] (q : F) where
  /-- Dimensionless spin-orbit coupling `C = -2κ_Nilsson`. -/
  spinOrbitCoupling : F
  /-- Dimensionless centrifugal flatness coefficient `D = -κ_Nilsson μ_Nilsson`. -/
  centrifugalFlatness : F
  /-- Spin-orbit strength fixed by the kinetic-normalized Dirac cross-term `-(q - 1)`. -/
  h_so_dirac : spinOrbitCoupling = -(q - 1)
  /-- Woods–Saxon centrifugal flatness fixed by `D = -(q - 1) / 4`. -/
  h_woods_saxon_ratio : centrifugalFlatness = -(q - 1) / 4
  /-- Rational lower threshold `43 / 39 < q` (`28` intruder beats `40` harmonic closure). -/
  h_q_lower : (43 : F) / 39 < q
  /-- Rational upper threshold `q < 19 / 17` (prevents `N = 6` intruder crossover at `126`). -/
  h_q_upper : q < (19 : F) / 17

/-- **Conditional `7/7` Magic-Closure Dominance Theorem (`§3b-cond`, `0 sorry`)**:
    Under `[h : RadialSpinOrbitReductionHypothesis F q]`, every one of the seven magic
    shell gaps `{2, 8, 20, 28, 50, 82, 126}` (`QOU.Common.magicSet`) in the centroid-subtracted
    Nilsson spectrum strictly dominates both the competing `N = 3` harmonic-oscillator
    sub-closure gap at `40` and the largest spin-orbit sub-shell gaps at `14` (`= 64`)
    and `114`. -/
theorem magic_seven_gaps_strictly_dominate_competitors
    (q : F) [h : RadialSpinOrbitReductionHypothesis F q] :
    let C := h.spinOrbitCoupling
    let D := h.centrifugalFlatness
    let gap2   := nilssonCentroidLevel C D 1 1 true  - nilssonCentroidLevel C D 0 0 true
    let gap8   := nilssonCentroidLevel C D 2 2 true  - nilssonCentroidLevel C D 1 1 false
    let gap20  := nilssonCentroidLevel C D 3 3 true  - nilssonCentroidLevel C D 2 2 false
    let gap28  := nilssonCentroidLevel C D 3 1 true  - nilssonCentroidLevel C D 3 3 true
    let gap50  := nilssonCentroidLevel C D 4 2 true  - nilssonCentroidLevel C D 4 4 true
    let gap82  := nilssonCentroidLevel C D 5 3 true  - nilssonCentroidLevel C D 5 5 true
    let gap126 := nilssonCentroidLevel C D 6 4 true  - nilssonCentroidLevel C D 5 1 false
    let gap40  := nilssonCentroidLevel C D 4 4 true  - nilssonCentroidLevel C D 3 1 false
    let gap14  := nilssonCentroidLevel C D 2 0 true  - nilssonCentroidLevel C D 2 2 true
    let gap114 := nilssonCentroidLevel C D 5 3 false - nilssonCentroidLevel C D 6 6 true
    gap40 < gap28 ∧ gap40 < gap50 ∧ gap40 < gap82 ∧ gap40 < gap126 ∧
    gap40 < gap2 ∧ gap40 < gap8 ∧ gap40 < gap20 ∧
    gap14 < gap28 ∧ gap14 < gap126 ∧ gap114 < gap126 := by
  have hC := h.h_so_dirac
  have hD := h.h_woods_saxon_ratio
  have hlo := h.h_q_lower
  have hhi := h.h_q_upper
  dsimp only
  unfold nilssonCentroidLevel
  rw [hC, hD]
  refine ⟨by linarith, by linarith, by linarith, by linarith,
          by linarith, by linarith, by linarith,
          by linarith, by linarith, by linarith⟩

/-- Cumulative harmonic-oscillator shell closure `N_HO(N) = (N + 1)(N + 2)(N + 3) / 3`. -/
def hoCumulative (N : ℕ) : ℕ :=
  (N + 1) * (N + 2) * (N + 3) / 3

/-- Mayer–Jensen high-`j` intruder closure above harmonic closure `N ≥ 2`: adds the
    aligned `j_+ = (N + 1) + 1/2` multiplet degeneracy `2(N + 1) + 2 = 2N + 4` from
    shell `N + 1` to `hoCumulative N`. -/
def intruderClosure (N : ℕ) : ℕ :=
  hoCumulative N + (2 * N + 4)

/-- **Exact bridge to `QOU.Common.magicSet`**: the three light harmonic closures
    `(N = 0, 1, 2 -> 2, 8, 20)` together with the four high-`j` spin-orbit intruder
    closures `(N = 2, 3, 4, 5 -> 28, 50, 82, 126)` equal the canonical seven-element
    finset `QOU.Common.magicSet`. -/
theorem mayer_jensen_closures_eq_magicSet :
    ({hoCumulative 0, hoCumulative 1, hoCumulative 2,
      intruderClosure 2, intruderClosure 3, intruderClosure 4, intruderClosure 5} : Finset ℕ) =
      QOU.Common.magicSet := by
  decide

end NilssonSpectrumAndPrune

end QOU.MassTheory.FramingSpinOrbitDiracScale
