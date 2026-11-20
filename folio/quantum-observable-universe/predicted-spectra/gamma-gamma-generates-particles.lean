/-
  γγ production generates the operator basis (categorical).

  Two independent colored photons in the Iwahori–Hecke algebra H₃(q),
  γ = 𝟙 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹ (def:photon; the last term is the chiral
  pair-production vertex by owner ruling 2026-11-18, bean qou-99qc, confirmed
  2026-11-20), multiply to a Breit–Wheeler product
  whose normal form reaches every basis operator
  {𝟙, σ₀, σ₁, L₊ = σ₀σ₁, L₋ = σ₁σ₀, e⁻ = σ₀σ₁σ₀}.

  This file formalises the generative core: the chiral pair (L₊, L₋) is
  produced *independently* by the cross-color products φ₀ψ₁ and φ₁ψ₀, so
  L₋ = σ₁σ₀ — absent from every single photon (whose normal-form support is
  {𝟙, σ₀, σ₁, σ₀σ₁}, since σ₀σ₁⁻¹ = σ₀σ₁ − hσ₀) — is reached only through the
  two-photon product. The remaining operator e⁻ opens with the 4-term coupling
  φ₀₁ ≠ 0: its coefficient is φ₀₁ψ₀ + φ₁ψ₀₁.

  The first part of this file states the three-term coefficients (φ₀₁ = ψ₀₁ = 0,
  where the two photon forms coincide). The second part states the same facts on
  the full H₃ normal form `QOU.QuarkState.pairNFChiral` of def:photon.

  The cross-color coefficients are purely algebraic (no q₀ ordering or
  Real construct), so everything is stated over a generic CommRing per
  the §7c base-ring convention.

  -- Ref: [leitner2026] predicted-spectra, breit-wheeler-pair-production
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic
import QOU.QuarkState.PhotonPairNormalForm

namespace QOU.Archimedean.GammaGammaGeneration

variable {R : Type*} [CommRing R]

/-- Coefficient of `L₊ = σ₀σ₁` in the two-photon product `γ₁·γ₂`, as a
    function of the color weights `(φ₀, φ₁)` of `γ₁` and `(ψ₀, ψ₁)` of
    `γ₂`: the cross-color product `φ₀ · ψ₁`. -/
def coeffLplus (φ0 _φ1 _ψ0 ψ1 : R) : R := φ0 * ψ1

/-- Coefficient of `L₋ = σ₁σ₀` in the two-photon product: `φ₁ · ψ₀`. -/
def coeffLminus (_φ0 φ1 ψ0 _ψ1 : R) : R := φ1 * ψ0

/-- **The chiral pair is generated independently by γγ production.**
    For any target pair `(a, b)` there exist photon color weights whose
    two-photon product has `L₊`-coefficient `a` and `L₋`-coefficient `b`
    (take `φ₀ = a, ψ₁ = 1, φ₁ = b, ψ₀ = 1`).  Hence both chiral Hopf
    operators arise from `γγ` production. -/
theorem gamma_gamma_chirality_surjective (a b : R) :
    ∃ φ0 φ1 ψ0 ψ1 : R,
      coeffLplus φ0 φ1 ψ0 ψ1 = a ∧ coeffLminus φ0 φ1 ψ0 ψ1 = b :=
  ⟨a, b, 1, 1, by simp [coeffLplus], by simp [coeffLminus]⟩

/-- The `L₋ = σ₁σ₀` content of a *single* photon
    `γ = 𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` is zero: its normal-form support is
    `{𝟙, σ₀, σ₁, σ₀σ₁}`, which does not include `σ₁σ₀`. -/
def singlePhotonCoeffLminus : R := 0

/-- **γγ production strictly enlarges the reachable operator set.**
    There are photon color weights whose two-photon product carries a
    nonzero `L₋ = σ₁σ₀` operator — content no single photon can hold. -/
theorem gamma_gamma_reaches_Lminus [Nontrivial R] :
    ∃ φ0 φ1 ψ0 ψ1 : R,
      coeffLminus φ0 φ1 ψ0 ψ1 ≠ singlePhotonCoeffLminus := by
  refine ⟨0, 1, 1, 0, ?_⟩
  simp only [coeffLminus, singlePhotonCoeffLminus, mul_one]
  exact one_ne_zero

/-! ### On the H₃ normal form of `def:photon`

Basis order of `pairNFChiral`: `[1, σ₀, σ₁, L₋ = σ₁σ₀, L₊ = σ₀σ₁, e⁻ = σ₀σ₁σ₀]`. -/

open QOU.QuarkState in
/-- A single `def:photon` has no `L₋` and no `e⁻` component. -/
theorem single_photon_no_Lminus_no_eminus (h a0 a1 a2 : R) :
    photon h a0 a1 a2 3 = 0 ∧ photon h a0 a1 a2 5 = 0 := by
  rw [photon_eq]; simp

open QOU.QuarkState in
/-- **The chiral pair from the full product.** `γ(a, b, 0)·γ(1, 1, 0)` has
    `L₊`-coefficient `a` and `L₋`-coefficient `b`, for every `h`. -/
theorem gamma_gamma_chirality_surjective_NF (h a b : R) :
    pairNFChiral h a b 0 1 1 0 4 = a ∧ pairNFChiral h a b 0 1 1 0 3 = b := by
  rw [pairNFChiral_eq]; constructor <;> simp

open QOU.QuarkState in
/-- **`e⁻` is reached.** `γ(0, 0, 1)·γ(1, 0, 0)` has `e⁻`-coefficient `1`: the
    vertex `σ₀σ₁⁻¹` times `σ₀` carries `σ₀σ₁σ₀`. -/
theorem gamma_gamma_reaches_eminus_NF (h : R) : pairNFChiral h 0 0 1 1 0 0 5 = 1 := by
  rw [pairNFChiral_eq]; simp

end QOU.Archimedean.GammaGammaGeneration
