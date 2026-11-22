import QOU.QuantumObservableUniverses.QDifferentialGeometry
import QOU.Torsion.MassTraceIdentity
import QOU.MassTheory.NeutronProtonEMSign
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.CategoryTheory.Preadditive.Basic

/-!
# Categorical Lagrangian Two-Term Bridge (`qou-dl1k` & `qou-r8hb`)

Genuine category-theoretic and `R`-linear expansion of `QOU.CategoricalDiracOperator`
and `QOU.CategoricalLagrangian` (`QOU.QuantumObservableUniverses.QDifferentialGeometry`)
over an `R`-linear preadditive monoidal category `C`, welded to:
1. The discrete non-abelian holonomy trace identity
   (`QOU.Torsion.MassTraceIdentity.massTrace_eq_functional_hol_of_frobeniusForm_eq_counit`),
2. The rational pairwise quark Coulomb self-energy gap
   (`QOU.MassTheory.NeutronProtonEMSign.em_gap_eq`), and
3. The concrete 3-strand weight-space matrix & scale-hierarchy theorems
   (`QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm`), closing Gaps 1, 2, and 5.

## Main Theorems

- `dirac_sq_four_term_expansion` / `dirac_sq_three_term_expansion`:
  Bilinear expansion of `D.dirac ≫ D.dirac` in `End_C(fh.obj)` into the three-term
  `q`-Laplacian tower `(q⁻², q⁻¹(1 - q⁻¹), (1 - q⁻¹)²)`.
- `matter_term_two_term_expansion`:
  Expansion of the fermionic matter coupling `L.costate ≫ L.state ≫ L.dirac.dirac`
  into horizontal (`q⁻¹`) and Reeb-contracted (`1 - q⁻¹`) components.
- `lagrangian_five_term_expansion`:
  Full 5-term decomposition of `L.lagrangian : fh.obj ⟶ fh.obj`.
- `trace_lagrangian_two_term_split` & `trace_lagrangian_diff_shared_dirac`:
  Image of `L.lagrangian` under any `R`-linear trace functional
  `τ : (fh.obj ⟶ fh.obj) →ₗ[R] R` and cancellation of the bosonic core when
  `L_n.dirac = L_p.dirac`.
- `trace_lagrangian_diff_shared_spatial_closure`:
  For two configurations `(L_n, L_p)` sharing the spatial connection `nablaEndo`,
  scale `qinv`, and traced spatial-Reeb cross-coupling on a common 3-strand braid
  closure, `τ L_n.lagrangian - τ L_p.lagrangian` decomposes into the `(1 - q⁻¹)²`
  Reeb-spin trace difference plus the fermionic matter trace difference.
- `reeb_holonomy_leftTrace_eq_functional_hol`:
  Bridges the Reeb-spin square `D.reeb ≫ D.reeb` to the discrete boundary holonomy
  trace `casimir fh ≫ leftMul fh (hol fh w) ≫ fh.frobeniusForm`.
- `trace_matter_diff_coulomb_specialization`:
  Over `ℚ`, evaluates the fermionic matter trace difference on the nucleon pairwise
  Coulomb charge factors `chargeStructure qUp qDown qDown` (`udd`) and
  `chargeStructure qUp qUp qDown` (`uud`) via `NeutronProtonEMSign.em_gap_eq`.
- `hadronicScale_mul_q_sq_hbar_eq_me` & `hadronicScale_strong_to_matter_ratio` (Gap 5):
  Exact Lagrangian scale hierarchy between the `(1 - q⁻¹)²` strong Reeb-spin square
  and the `(1 - q⁻¹)` matter Reeb coupling under `E₀(q) = m_e / (q (q - 1))`.
- `trace_lagrangian_diff_concrete_borromean_weight_space` &
  `trace_lagrangian_diff_concrete_borromean_connected` (Gap 2):
  Parameter-free concrete 3×3 weight-space matrix specialization of
  `τ L_n.lagrangian - τ L_p.lagrangian` on the Borromean braid `V³ = (σ₁ σ₂⁻¹)³`.
- `trace_matter_reeb_proton_eq_one_third_six_crossing_sum` &
  `trace_matter_reeb_neutron_eq_one_third_six_crossing_sum` (Gap 1):
  Bridges the matter Reeb trace directly to `(1 / 3)` times the 6-crossing cyclic
  boundary sum across the 3 periods of `V_p³` and `V_n³`.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory
open CategoryTheory CategoryTheory.Limits

namespace QOU.CategoricalLagrangianTwoTermBridge

universe u v

variable {R : Type*} [CommRing R]
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
  [Preadditive C] [Linear R C]
variable {fh : FrobeniusHopfData C}

/-- **Four-term ungrouped bilinear expansion of `D.dirac ≫ D.dirac`** in `fh.obj ⟶ fh.obj`. -/
theorem dirac_sq_four_term_expansion (D : CategoricalDiracOperator R C fh) :
    D.dirac ≫ D.dirac =
      (D.qinv * D.qinv) • (D.nablaEndo ≫ D.nablaEndo) +
      (D.qinv * (1 - D.qinv)) • (D.nablaEndo ≫ D.reeb) +
      ((1 - D.qinv) * D.qinv) • (D.reeb ≫ D.nablaEndo) +
      ((1 - D.qinv) * (1 - D.qinv)) • (D.reeb ≫ D.reeb) := by
  conv_lhs => rw [D.dirac_formula]
  rw [Preadditive.add_comp, Preadditive.comp_add, Preadditive.comp_add]
  simp only [Linear.smul_comp, Linear.comp_smul, smul_smul, mul_comm (1 - D.qinv) D.qinv]
  abel

/-- **Three-term `q`-Laplacian expansion of `D.dirac ≫ D.dirac`** in `fh.obj ⟶ fh.obj`.
    Groups the middle cross-terms `(D.nablaEndo ≫ D.reeb + D.reeb ≫ D.nablaEndo)` under
    the shared coefficient `D.qinv * (1 - D.qinv)`. -/
theorem dirac_sq_three_term_expansion (D : CategoricalDiracOperator R C fh) :
    D.dirac ≫ D.dirac =
      (D.qinv * D.qinv) • (D.nablaEndo ≫ D.nablaEndo) +
      (D.qinv * (1 - D.qinv)) • (D.nablaEndo ≫ D.reeb + D.reeb ≫ D.nablaEndo) +
      ((1 - D.qinv) * (1 - D.qinv)) • (D.reeb ≫ D.reeb) := by
  rw [dirac_sq_four_term_expansion, mul_comm (1 - D.qinv) D.qinv, smul_add]
  abel

/-- **Two-term expansion of the fermionic matter coupling `L.costate ≫ L.state ≫ L.dirac.dirac`**
    in `fh.obj ⟶ fh.obj`. -/
theorem matter_term_two_term_expansion (L : CategoricalLagrangian R C fh) :
    L.costate ≫ L.state ≫ L.dirac.dirac =
      L.dirac.qinv • (L.costate ≫ L.state ≫ L.dirac.nablaEndo) +
      (1 - L.dirac.qinv) • (L.costate ≫ L.state ≫ L.dirac.reeb) := by
  conv_lhs => rw [L.dirac.dirac_formula]
  simp only [Preadditive.comp_add, Linear.comp_smul]

/-- **Full five-term expansion of `L.lagrangian : fh.obj ⟶ fh.obj`** in an `R`-linear
    preadditive monoidal category. -/
theorem lagrangian_five_term_expansion (L : CategoricalLagrangian R C fh) :
    L.lagrangian =
      ((L.dirac.qinv * L.dirac.qinv) • (L.dirac.nablaEndo ≫ L.dirac.nablaEndo) +
        (L.dirac.qinv * (1 - L.dirac.qinv)) •
          (L.dirac.nablaEndo ≫ L.dirac.reeb + L.dirac.reeb ≫ L.dirac.nablaEndo) +
        ((1 - L.dirac.qinv) * (1 - L.dirac.qinv)) • (L.dirac.reeb ≫ L.dirac.reeb)) +
      (L.dirac.qinv • (L.costate ≫ L.state ≫ L.dirac.nablaEndo) +
        (1 - L.dirac.qinv) • (L.costate ≫ L.state ≫ L.dirac.reeb)) := by
  rw [L.lagrangian_formula, dirac_sq_three_term_expansion, matter_term_two_term_expansion]

/-- **Two-term trace decomposition of `L.lagrangian`** under any `R`-linear trace functional
    `τ : (fh.obj ⟶ fh.obj) →ₗ[R] R`. -/
theorem trace_lagrangian_two_term_split
    (τ : (fh.obj ⟶ fh.obj) →ₗ[R] R) (L : CategoricalLagrangian R C fh) :
    τ L.lagrangian =
      τ (L.dirac.dirac ≫ L.dirac.dirac) + τ (L.costate ≫ L.state ≫ L.dirac.dirac) := by
  rw [L.lagrangian_formula, map_add]

/-- **Three-term traced `q`-Laplacian expansion** under an `R`-linear trace functional
    `τ : (fh.obj ⟶ fh.obj) →ₗ[R] R`. -/
theorem trace_dirac_sq_three_term_expansion
    (τ : (fh.obj ⟶ fh.obj) →ₗ[R] R) (D : CategoricalDiracOperator R C fh) :
    τ (D.dirac ≫ D.dirac) =
      (D.qinv * D.qinv) * τ (D.nablaEndo ≫ D.nablaEndo) +
      (D.qinv * (1 - D.qinv)) * τ (D.nablaEndo ≫ D.reeb + D.reeb ≫ D.nablaEndo) +
      ((1 - D.qinv) * (1 - D.qinv)) * τ (D.reeb ≫ D.reeb) := by
  rw [dirac_sq_three_term_expansion]
  simp only [map_add, LinearMap.map_smul, smul_eq_mul]

/-- **Two-term traced matter expansion** under an `R`-linear trace functional
    `τ : (fh.obj ⟶ fh.obj) →ₗ[R] R`. -/
theorem trace_matter_two_term_expansion
    (τ : (fh.obj ⟶ fh.obj) →ₗ[R] R) (L : CategoricalLagrangian R C fh) :
    τ (L.costate ≫ L.state ≫ L.dirac.dirac) =
      L.dirac.qinv * τ (L.costate ≫ L.state ≫ L.dirac.nablaEndo) +
      (1 - L.dirac.qinv) * τ (L.costate ≫ L.state ≫ L.dirac.reeb) := by
  rw [matter_term_two_term_expansion]
  simp only [map_add, LinearMap.map_smul, smul_eq_mul]

/-- **Shared-Dirac state difference cancellation**: when two matter configurations
    `L_n L_p : CategoricalLagrangian R C fh` share the exact same bosonic Dirac operator
    (`L_n.dirac = L_p.dirac`), the bosonic trace `τ (D.dirac ≫ D.dirac)` cancels identically
    in `τ L_n.lagrangian - τ L_p.lagrangian`. -/
theorem trace_lagrangian_diff_shared_dirac
    (τ : (fh.obj ⟶ fh.obj) →ₗ[R] R)
    (L_n L_p : CategoricalLagrangian R C fh)
    (hDirac : L_n.dirac = L_p.dirac) :
    τ L_n.lagrangian - τ L_p.lagrangian =
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.dirac) -
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.dirac) := by
  rw [trace_lagrangian_two_term_split τ L_n, trace_lagrangian_two_term_split τ L_p, hDirac]
  ring

/-- **Two-term nucleon splitting decomposition on a shared spatial braid closure**:
    When two configurations `L_n L_p : CategoricalLagrangian R C fh` share the same
    deformation parameter `qinv`, the same spatial connection `nablaEndo`, and the same
    traced spatial-Reeb cross-coupling on the common 3-strand closure, the classical
    spatial curvature `q⁻² τ(∇²)` and cross-coupling cancel identically in
    `τ L_n.lagrangian - τ L_p.lagrangian`, leaving strictly:
    1. The `(1 - q⁻¹)²` Reeb-spin square trace difference, plus
    2. The fermionic matter trace difference. -/
theorem trace_lagrangian_diff_shared_spatial_closure
    (τ : (fh.obj ⟶ fh.obj) →ₗ[R] R)
    (L_n L_p : CategoricalLagrangian R C fh)
    (hQinv : L_n.dirac.qinv = L_p.dirac.qinv)
    (hNabla : L_n.dirac.nablaEndo = L_p.dirac.nablaEndo)
    (hCross :
      τ (L_n.dirac.nablaEndo ≫ L_n.dirac.reeb + L_n.dirac.reeb ≫ L_n.dirac.nablaEndo) =
      τ (L_p.dirac.nablaEndo ≫ L_p.dirac.reeb + L_p.dirac.reeb ≫ L_p.dirac.nablaEndo)) :
    τ L_n.lagrangian - τ L_p.lagrangian =
      ((1 - L_n.dirac.qinv) * (1 - L_n.dirac.qinv)) *
        (τ (L_n.dirac.reeb ≫ L_n.dirac.reeb) - τ (L_p.dirac.reeb ≫ L_p.dirac.reeb)) +
      (τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.dirac) -
        τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.dirac)) := by
  rw [trace_lagrangian_two_term_split τ L_n, trace_lagrangian_two_term_split τ L_p,
    trace_dirac_sq_three_term_expansion τ L_n.dirac,
    trace_dirac_sq_three_term_expansion τ L_p.dirac,
    hCross, ← hQinv, ← hNabla]
  ring

/-- **Bridge from Reeb-spin square `D.reeb ≫ D.reeb` to discrete boundary holonomy trace**
    (`QOU.Torsion.MassTraceIdentity.massTrace_eq_functional_hol_of_frobeniusForm_eq_counit`):
    when the Reeb-spin square endomorphism `D.reeb ≫ D.reeb` is realized via non-abelian
    Stokes descent as the mass endomorphism `leftMul fh (hol fh w) ≫ massIntegrand fh` of a
    boundary transport word `w`, its categorical trace `fh.leftTrace (D.reeb ≫ D.reeb)`
    under `fh.frobeniusForm = fh.counit` equals the Frobenius functional
    `casimir fh ≫ leftMul fh (hol fh w) ≫ fh.frobeniusForm`. -/
theorem reeb_holonomy_leftTrace_eq_functional_hol
    (D : CategoricalDiracOperator R C fh)
    (hCounit : fh.frobeniusForm = fh.counit)
    (w : List (𝟙_ C ⟶ fh.obj))
    (hStokes : D.reeb ≫ D.reeb =
      Torsion.MassTraceIdentity.leftMul fh (Torsion.MassTraceIdentity.hol fh w) ≫
        Torsion.MassTraceIdentity.massIntegrand fh) :
    fh.leftTrace (D.reeb ≫ D.reeb) =
      Torsion.MassTraceIdentity.casimir fh ≫
        Torsion.MassTraceIdentity.leftMul fh (Torsion.MassTraceIdentity.hol fh w) ≫
        fh.frobeniusForm := by
  rw [hStokes,
    Torsion.MassTraceIdentity.massTrace_eq_functional_hol_of_frobeniusForm_eq_counit fh hCounit w]

/-- **Bridge from the fermionic matter trace difference to the pairwise quark Coulomb gap**
    (`QOU.MassTheory.NeutronProtonEMSign.em_gap_eq`):
    Over `ℚ`, when the horizontal matter traces of neutron (`L_n`) and proton (`L_p`)
    agree and their Reeb-contracted matter traces evaluate to `k` times the pairwise
    quark Coulomb charge factors `chargeStructure qUp qDown qDown` (`udd`) and
    `chargeStructure qUp qUp qDown` (`uud`), the fermionic matter trace difference
    evaluates to `-(1 - q⁻¹) * (k / 3)`. -/
theorem trace_matter_diff_coulomb_specialization
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
    [Preadditive C] [Linear ℚ C] {fh : FrobeniusHopfData C}
    (τ : (fh.obj ⟶ fh.obj) →ₗ[ℚ] ℚ)
    (L_n L_p : CategoricalLagrangian ℚ C fh)
    (k : ℚ)
    (hQinv : L_n.dirac.qinv = L_p.dirac.qinv)
    (hHoriz :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) =
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo))
    (hNeutronCoulomb :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb) =
      k * MassTheory.NeutronProtonEMSign.chargeStructure
        MassTheory.NeutronProtonEMSign.qUp
        MassTheory.NeutronProtonEMSign.qDown
        MassTheory.NeutronProtonEMSign.qDown)
    (hProtonCoulomb :
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb) =
      k * MassTheory.NeutronProtonEMSign.chargeStructure
        MassTheory.NeutronProtonEMSign.qUp
        MassTheory.NeutronProtonEMSign.qUp
        MassTheory.NeutronProtonEMSign.qDown) :
    τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.dirac) -
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.dirac) =
      -(1 - L_n.dirac.qinv) * (k / 3) := by
  rw [trace_matter_two_term_expansion τ L_n, trace_matter_two_term_expansion τ L_p,
    ← hQinv, hHoriz, hNeutronCoulomb, hProtonCoulomb,
    MassTheory.NeutronProtonEMSign.chargeStructure_udd,
    MassTheory.NeutronProtonEMSign.chargeStructure_uud]
  ring

/-- **Combined Two-Term Nucleon Traced Lagrangian Splitting Theorem over `ℚ`**:
    Under the shared 3-strand spatial closure hypotheses (`hQinv`, `hNabla`, `hCross`)
    and the pairwise Coulomb specialization (`hHoriz`, `hNeutronCoulomb`, `hProtonCoulomb`),
    the total traced Lagrangian difference `τ L_n.lagrangian - τ L_p.lagrangian` equals
    the positive-weighted Reeb-spin square trace difference minus `(1 - q⁻¹) * (k / 3)`. -/
theorem trace_lagrangian_nucleon_splitting_with_coulomb_gap
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
    [Preadditive C] [Linear ℚ C] {fh : FrobeniusHopfData C}
    (τ : (fh.obj ⟶ fh.obj) →ₗ[ℚ] ℚ)
    (L_n L_p : CategoricalLagrangian ℚ C fh)
    (k : ℚ)
    (hQinv : L_n.dirac.qinv = L_p.dirac.qinv)
    (hNabla : L_n.dirac.nablaEndo = L_p.dirac.nablaEndo)
    (hCross :
      τ (L_n.dirac.nablaEndo ≫ L_n.dirac.reeb + L_n.dirac.reeb ≫ L_n.dirac.nablaEndo) =
      τ (L_p.dirac.nablaEndo ≫ L_p.dirac.reeb + L_p.dirac.reeb ≫ L_p.dirac.nablaEndo))
    (hHoriz :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) =
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo))
    (hNeutronCoulomb :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb) =
      k * MassTheory.NeutronProtonEMSign.chargeStructure
        MassTheory.NeutronProtonEMSign.qUp
        MassTheory.NeutronProtonEMSign.qDown
        MassTheory.NeutronProtonEMSign.qDown)
    (hProtonCoulomb :
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb) =
      k * MassTheory.NeutronProtonEMSign.chargeStructure
        MassTheory.NeutronProtonEMSign.qUp
        MassTheory.NeutronProtonEMSign.qUp
        MassTheory.NeutronProtonEMSign.qDown) :
    τ L_n.lagrangian - τ L_p.lagrangian =
      ((1 - L_n.dirac.qinv) * (1 - L_n.dirac.qinv)) *
        (τ (L_n.dirac.reeb ≫ L_n.dirac.reeb) - τ (L_p.dirac.reeb ≫ L_p.dirac.reeb)) -
      (1 - L_n.dirac.qinv) * (k / 3) := by
  rw [trace_lagrangian_diff_shared_spatial_closure τ L_n L_p hQinv hNabla hCross,
    trace_matter_diff_coulomb_specialization τ L_n L_p k hQinv hHoriz hNeutronCoulomb hProtonCoulomb]
  ring

/-! ## 5. Concrete 3-Strand Weight-Space Matrix & Scale-Hierarchy Bridge (Closing Gaps 1, 2, 5) -/

section ConcreteWeightSpaceAndScaleBridge

variable {F : Type*} [Field F]
variable {C_F : Type u} [Category.{v} C_F] [MonoidalCategory C_F] [BraidedCategory C_F]
  [Preadditive C_F] [Linear F C_F]
variable {fh_F : FrobeniusHopfData C_F}

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-- **Hadronic energy scale `E₀(q) = m_e / (q (q - 1))`** relating the fundamental electronic
    scale `m_e` to the categorical Lagrangian `ħ_q = 1 - q⁻¹` hierarchy. -/
def hadronicScale (m_e q : F) : F :=
  m_e / (q * (q - 1))

/-- **Gap 5 (Exact Lagrangian Scale Hierarchy — Electronic Calibration):**
    Multiplying `hadronicScale m_e q = m_e / (q (q - 1))` by `q² * (1 - q⁻¹)` (the `q²`
    factor times the first-order matter Reeb prefactor `ħ_q = 1 - q⁻¹`) recovers `m_e`
    identically. -/
theorem hadronicScale_mul_q_sq_hbar_eq_me (m_e q : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    hadronicScale m_e q * (q ^ 2 * (1 - q⁻¹)) = m_e := by
  unfold hadronicScale
  field_simp

/-- **Gap 5 (Strong Reeb-Spin Square vs. Matter Reeb Scale Ratio):**
    In `CategoricalLagrangian`, the matter Reeb term carries prefactor `1 - q⁻¹ = ħ_q`
    while the bosonic Reeb-spin square `D.reeb ≫ D.reeb` carries `(1 - q⁻¹)² = ħ_q²`.
    Consequently, the ratio of the `hadronicScale`-weighted matter prefactor to the
    strong `(1 - q⁻¹)²` prefactor is `m_e / (q - 1)²`. -/
theorem hadronicScale_strong_to_matter_ratio (m_e q : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    (hadronicScale m_e q * (1 - q⁻¹)) / (1 - q⁻¹) ^ 2 = m_e / (q - 1) ^ 2 := by
  unfold hadronicScale
  have h1q : 1 - q⁻¹ = (q - 1) / q := by
    field_simp
  rw [h1q]
  field_simp

/-- **Gap 2 (Parameter-Free Concrete 3-Strand Weight-Space Specialization on Borromean `V³`):**
    When the Reeb-spin square traces `τ (D_n.reeb ≫ D_n.reeb)` and `τ (D_p.reeb ≫ D_p.reeb)`
    are evaluated on the 3-strand neutron `(1,2)` and proton `(2,1)` weight spaces with
    Cartan weights `K^{⊗3}` (`q⁻¹` on `W_n`, `q` on `W_p`) on the Borromean braid
    `V³ = (σ₁ σ₂⁻¹)³` (`borromeanV3B q`, `borromeanV3A q`), and the Reeb-contracted matter
    traces evaluate to the adjacent pairwise charge traces `tr((Q₁₂ + Q₂₃) V³)`, the traced
    Lagrangian difference `τ L_n.lagrangian - τ L_p.lagrangian` evaluates to the exact
    parameter-free rational function of `q` with zero free coupling `k`. -/
theorem trace_lagrangian_diff_concrete_borromean_weight_space
    (τ : (fh_F.obj ⟶ fh_F.obj) →ₗ[F] F)
    (L_n L_p : CategoricalLagrangian F C_F fh_F)
    (q : F) (hq : q ≠ 0) (h3 : (3 : F) ≠ 0)
    (hQn : L_n.dirac.qinv = q⁻¹)
    (hQp : L_p.dirac.qinv = q⁻¹)
    (hNabla : L_n.dirac.nablaEndo = L_p.dirac.nablaEndo)
    (hCross :
      τ (L_n.dirac.nablaEndo ≫ L_n.dirac.reeb + L_n.dirac.reeb ≫ L_n.dirac.nablaEndo) =
      τ (L_p.dirac.nablaEndo ≫ L_p.dirac.reeb + L_p.dirac.reeb ≫ L_p.dirac.nablaEndo))
    (hReebN :
      τ (L_n.dirac.reeb ≫ L_n.dirac.reeb) = q⁻¹ * trace (borromeanV3B q))
    (hReebP :
      τ (L_p.dirac.reeb ≫ L_p.dirac.reeb) = q * trace (borromeanV3A q))
    (hHoriz :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) =
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo))
    (hMatReebN :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb) =
      trace ((Q12n + Q23n) * borromeanV3B q))
    (hMatReebP :
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb) =
      trace ((Q12p + Q23p) * borromeanV3A q)) :
    τ L_n.lagrangian - τ L_p.lagrangian =
      (1 - q⁻¹) ^ 2 * (q⁻¹ - q) *
        (-(q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6) +
      (1 - q⁻¹) *
        ((2 * q ^ 12 - 7 * q ^ 10 + 10 * q ^ 8 - 12 * q ^ 6 + 10 * q ^ 4 - 7 * q ^ 2 + 2) /
          (3 * q ^ 6)) := by
  have hQinv : L_n.dirac.qinv = L_p.dirac.qinv := hQn.trans hQp.symm
  rw [trace_lagrangian_diff_shared_spatial_closure τ L_n L_p hQinv hNabla hCross,
    trace_matter_two_term_expansion τ L_n, trace_matter_two_term_expansion τ L_p,
    hQn, hQp, hHoriz, hReebN, hReebP, hMatReebN, hMatReebP]
  have hMatDiff :
      trace ((Q12n + Q23n) * borromeanV3B q) - trace ((Q12p + Q23p) * borromeanV3A q) =
        (2 * q ^ 12 - 7 * q ^ 10 + 10 * q ^ 8 - 12 * q ^ 6 + 10 * q ^ 4 - 7 * q ^ 2 + 2) /
          (3 * q ^ 6) :=
    trace_QAdj_diff_borromeanV3 q hq h3
  rw [trace_borromeanV3B q hq, trace_borromeanV3A q hq]
  linear_combination (1 - q⁻¹) * hMatDiff

/-- **Gap 2 (Connected Fourth-Order `(q - 1)⁴` Decomposition of the Concrete Traced Lagrangian Difference):**
    Under the hypotheses of `trace_lagrangian_diff_concrete_borromean_weight_space`, separating
    the static `q = 1` Coulomb background `(-2 / 9) * tr(V_n³)` from the neutron matter trace
    via `trace_QAdj_connected_diff_borromeanV3` expresses `τ L_n.lagrangian - τ L_p.lagrangian`
    as the Cartan Reeb-spin term, the static `-2/9` Coulomb term, and the reinforcing
    fourth-order connected quantum braid trace `(q - 1)⁴ (q + 1)⁴ (4 q⁴ + q² + 4) / (9 q⁶)`. -/
theorem trace_lagrangian_diff_concrete_borromean_connected
    (τ : (fh_F.obj ⟶ fh_F.obj) →ₗ[F] F)
    (L_n L_p : CategoricalLagrangian F C_F fh_F)
    (q : F) (hq : q ≠ 0) (h3 : (3 : F) ≠ 0)
    (hQn : L_n.dirac.qinv = q⁻¹)
    (hQp : L_p.dirac.qinv = q⁻¹)
    (hNabla : L_n.dirac.nablaEndo = L_p.dirac.nablaEndo)
    (hCross :
      τ (L_n.dirac.nablaEndo ≫ L_n.dirac.reeb + L_n.dirac.reeb ≫ L_n.dirac.nablaEndo) =
      τ (L_p.dirac.nablaEndo ≫ L_p.dirac.reeb + L_p.dirac.reeb ≫ L_p.dirac.nablaEndo))
    (hReebN :
      τ (L_n.dirac.reeb ≫ L_n.dirac.reeb) = q⁻¹ * trace (borromeanV3B q))
    (hReebP :
      τ (L_p.dirac.reeb ≫ L_p.dirac.reeb) = q * trace (borromeanV3A q))
    (hHoriz :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) =
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo))
    (hMatReebN :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb) =
      trace ((Q12n + Q23n) * borromeanV3B q))
    (hMatReebP :
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb) =
      trace ((Q12p + Q23p) * borromeanV3A q)) :
    τ L_n.lagrangian - τ L_p.lagrangian =
      (1 - q⁻¹) ^ 2 * (q⁻¹ - q) * trace (borromeanV3A q) +
      (1 - q⁻¹) * ((-2 / 9 : F) * trace (borromeanV3B q) +
        (q - 1) ^ 4 * (q + 1) ^ 4 * (4 * q ^ 4 + q ^ 2 + 4) / (9 * q ^ 6)) := by
  have hQinv : L_n.dirac.qinv = L_p.dirac.qinv := hQn.trans hQp.symm
  rw [trace_lagrangian_diff_shared_spatial_closure τ L_n L_p hQinv hNabla hCross,
    trace_matter_two_term_expansion τ L_n, trace_matter_two_term_expansion τ L_p,
    hQn, hQp, hHoriz, hReebN, hReebP, hMatReebN, hMatReebP]
  have hV3eq : trace (borromeanV3B q) = trace (borromeanV3A q) := by
    rw [trace_borromeanV3B q hq, trace_borromeanV3A q hq]
  have hConn :
      (trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : F) * trace (borromeanV3B q)) -
        trace ((Q12p + Q23p) * borromeanV3A q) =
        (q - 1) ^ 4 * (q + 1) ^ 4 * (4 * q ^ 4 + q ^ 2 + 4) / (9 * q ^ 6) :=
    trace_QAdj_connected_diff_borromeanV3 q hq h3
  linear_combination (1 - q⁻¹) ^ 2 * q⁻¹ * hV3eq + (1 - q⁻¹) * hConn

/-- **Gap 1 (Boundary 6-Crossing Cyclic Sum Bridge for Proton `V_p³ = (A₁ A₂⁻¹)³`):**
    Connects the proton Reeb-contracted matter trace `τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb)`
    directly to `(1 / 3)` times the 6-crossing cyclic boundary sum across the 3 periods of `V_p³`
    via `trace_borromeanV3A_six_crossing_sum`. -/
theorem trace_matter_reeb_proton_eq_one_third_six_crossing_sum
    (τ : (fh_F.obj ⟶ fh_F.obj) →ₗ[F] F)
    (L_p : CategoricalLagrangian F C_F fh_F)
    (q : F) (h3 : (3 : F) ≠ 0)
    (hMatReebP :
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb) =
      trace ((Q12p + Q23p) * borromeanV3A q)) :
    τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb) =
      (1 / 3 : F) *
        (trace ((Q12p * A₁ q * A₂Inv q + A₁ q * (Q23p * A₂Inv q)) * borromeanVA q * borromeanVA q) +
         trace (borromeanVA q * (Q12p * A₁ q * A₂Inv q + A₁ q * (Q23p * A₂Inv q)) * borromeanVA q) +
         trace (borromeanVA q * borromeanVA q * (Q12p * A₁ q * A₂Inv q + A₁ q * (Q23p * A₂Inv q)))) := by
  rw [hMatReebP, trace_borromeanV3A_six_crossing_sum q]
  field_simp

/-- **Gap 1 (Boundary 6-Crossing Cyclic Sum Bridge for Neutron `V_n³ = (B₁ B₂⁻¹)³`):**
    Connects the neutron Reeb-contracted matter trace `τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb)`
    directly to `(1 / 3)` times the 6-crossing cyclic boundary sum across the 3 periods of `V_n³`
    via `trace_borromeanV3B_six_crossing_sum`. -/
theorem trace_matter_reeb_neutron_eq_one_third_six_crossing_sum
    (τ : (fh_F.obj ⟶ fh_F.obj) →ₗ[F] F)
    (L_n : CategoricalLagrangian F C_F fh_F)
    (q : F) (h3 : (3 : F) ≠ 0)
    (hMatReebN :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb) =
      trace ((Q12n + Q23n) * borromeanV3B q)) :
    τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb) =
      (1 / 3 : F) *
        (trace ((Q12n * B₁ q * B₂Inv q + B₁ q * (Q23n * B₂Inv q)) * borromeanVB q * borromeanVB q) +
         trace (borromeanVB q * (Q12n * B₁ q * B₂Inv q + B₁ q * (Q23n * B₂Inv q)) * borromeanVB q) +
         trace (borromeanVB q * borromeanVB q * (Q12n * B₁ q * B₂Inv q + B₁ q * (Q23n * B₂Inv q)))) := by
  rw [hMatReebN, trace_borromeanV3B_six_crossing_sum q]
  field_simp

end ConcreteWeightSpaceAndScaleBridge

end QOU.CategoricalLagrangianTwoTermBridge
