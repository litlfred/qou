import QOU.QuantumObservableUniverses.CategoricalLagrangianTwoTermBridge

/-!
# The two-term Lagrangian separates the volume term from the own-sector constant

The two-term Lagrangian is `ℒ = 𝒟² + ψ*·𝒟ψ`, with `𝒟 = q⁻¹∇ + (1 − q⁻¹)Reeb`
(`QOU.CategoricalLagrangianTwoTermBridge`).

* The bosonic term `𝒟²` contains no nucleon state. When the proton and the neutron share
  `𝒟`, it cancels in `n − p` (`trace_lagrangian_diff_shared_dirac`). This is where the
  shared volume term sits.
* The matter term `ψ*·𝒟ψ` contains the nucleon's own state, so it is traced on the nucleon's
  own sector.

This file proves the consequence for the horizontal (`∇`) piece of the matter term. Suppose
that piece is the own-sector quantum trace of one common element `c`, so it carries the
Cartan weight `q` on the proton sector and `q⁻¹` on the neutron sector, as in `Kp`/`Kn` of
`NucleonWeightSpaceTwoTerm`. Then the horizontal matter contribution is `c` for the proton
and `q⁻² · c` for the neutron. That is the `K1` reading of the constant term.

**Hypothesis, not result.** `hHorizP` and `hHorizN` state that the horizontal matter trace is
the own-sector trace of a common `c`. Nothing here derives that, and nothing here derives the
value of `c`. The existing bridge puts a different object, the pairwise Coulomb charge, in the
Reeb piece. That object is untouched here.
-/

namespace QOU.MassTheory.TwoTermMatterOwnSector

open CategoryTheory QOU.CategoricalLagrangianTwoTermBridge

universe u v

variable {F : Type*} [Field F]
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
  [Preadditive C] [Linear F C] {fh : FrobeniusHopfData C}

/-- Horizontal matter piece of the proton: `q⁻¹ · (q · c) = c`. It does not depend on `q`. -/
theorem horizontal_matter_proton_of_own_sector
    (τ : (fh.obj ⟶ fh.obj) →ₗ[F] F) (L_p : CategoricalLagrangian F C fh)
    (q c : F) (hq : q ≠ 0) (hQinv : L_p.dirac.qinv = q⁻¹)
    (hHorizP : τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo) = q * c) :
    L_p.dirac.qinv * τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo) = c := by
  rw [hQinv, hHorizP]; field_simp

/-- Horizontal matter piece of the neutron: `q⁻¹ · (q⁻¹ · c) = q⁻² · c`. -/
theorem horizontal_matter_neutron_of_own_sector
    (τ : (fh.obj ⟶ fh.obj) →ₗ[F] F) (L_n : CategoricalLagrangian F C fh)
    (q c : F) (hQinv : L_n.dirac.qinv = q⁻¹)
    (hHorizN : τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) = q⁻¹ * c) :
    L_n.dirac.qinv * τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) = q⁻¹ ^ 2 * c := by
  rw [hQinv, hHorizN]; ring

/-- **The full nucleon difference under the own-sector hypothesis.** With a shared Dirac
operator, `τ ℒ_n − τ ℒ_p` is the horizontal own-sector constant difference `(q⁻² − 1)·c` plus
`(1 − q⁻¹)` times the Reeb matter difference. The bosonic `𝒟²` term has cancelled. -/
theorem nucleon_diff_of_own_sector_horizontal
    (τ : (fh.obj ⟶ fh.obj) →ₗ[F] F) (L_n L_p : CategoricalLagrangian F C fh)
    (q c : F) (hq : q ≠ 0) (hDirac : L_n.dirac = L_p.dirac) (hQinv : L_p.dirac.qinv = q⁻¹)
    (hHorizP : τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo) = q * c)
    (hHorizN : τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) = q⁻¹ * c) :
    τ L_n.lagrangian - τ L_p.lagrangian =
      (q⁻¹ ^ 2 - 1) * c +
      (1 - q⁻¹) * (τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb) -
        τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb)) := by
  have hQn : L_n.dirac.qinv = q⁻¹ := by rw [hDirac]; exact hQinv
  rw [trace_lagrangian_diff_shared_dirac τ L_n L_p hDirac,
    trace_matter_two_term_expansion τ L_n, trace_matter_two_term_expansion τ L_p,
    hQn, hQinv, hHorizP, hHorizN]
  field_simp; ring

/-- Sign of the constant-term difference: for `1 < q` and `0 < c` the horizontal own-sector
piece makes the neutron *lighter* by `(1 − q⁻²)·c`. In the production identity the constant
enters with a minus sign (`m = … − 12·(…)`), so a smaller subtracted constant makes the
neutron heavier. -/
theorem own_sector_constant_neutron_smaller
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (q c : K) (hq : 1 < q) (hc : 0 < c) : q⁻¹ ^ 2 * c < c := by
  have hq0 : 0 < q := by linarith
  have h1 : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have h2 : q⁻¹ ^ 2 < 1 := by
    have : 0 < q⁻¹ := inv_pos.mpr hq0
    nlinarith
  nlinarith

end QOU.MassTheory.TwoTermMatterOwnSector
