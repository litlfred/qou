import Mathlib.Tactic

/-!
# QOU.Archimedean.QuarkAntiquarkProduction

**Canonical declaration** for content block at
[`quantum-observable-universe/particle-interactions/quark-antiquark-production-reduction.ts`](quantum-observable-universe/particle-interactions/quark-antiquark-production-reduction.ts).

Formalises the manuscript **normal form** of the two-colored-photon product
`γ₁·γ₂` in `H₃(q)` (3-term specialisation
`γᵢ = 𝟏 + φ_i σ₀ + ψ_i σ₁`), whose `NF` has coefficients

- `γ`  : `1 + φ₀ψ₀ + φ₁ψ₁`
- `σ₀` : `φ₀ + ψ₀ + φ₀ψ₀h`,  `σ₁` : `φ₁ + ψ₁ + φ₁ψ₁h`
- `L₊ = σ₀σ₁` : `φ₀ψ₁`,  `L₋ = σ₁σ₀` : `φ₁ψ₀`  (cross-color only)

with `h = q − q⁻¹`. Generic over any `CommRing` (§7c-clean; the `σ`
non-commutativity is carried by the coefficient formulas).
-/

namespace QOU.Archimedean

/-- Coefficient data for `NF(γ₁·γ₂)`.

    A `definition` carrier: the two photons' color weights `φ₀,φ₁` and
    `ψ₀,ψ₁`, the deformation `h`, and the five normal-form coefficients each
    pinned to its manuscript value. -/
structure QuarkAntiquarkProduction (R : Type*) [CommRing R] where
  /-- Color weights of `γ₁`. -/
  φ₀ : R
  φ₁ : R
  /-- Color weights of `γ₂`. -/
  ψ₀ : R
  ψ₁ : R
  /-- Deformation `h = q − q⁻¹`. -/
  h : R
  /-- Coefficient of `γ` (the identity knot). -/
  cγ : R
  /-- Coefficient of `σ₀`. -/
  cσ₀ : R
  /-- Coefficient of `σ₁`. -/
  cσ₁ : R
  /-- Coefficient of `L₊ = σ₀σ₁` (closure in B₃: unknot). -/
  cLp : R
  /-- Coefficient of `L₋ = σ₁σ₀` (closure in B₃: unknot). -/
  cLm : R
  cγ_def : cγ = 1 + φ₀ * ψ₀ + φ₁ * ψ₁
  cσ₀_def : cσ₀ = φ₀ + ψ₀ + φ₀ * ψ₀ * h
  cσ₁_def : cσ₁ = φ₁ + ψ₁ + φ₁ * ψ₁ * h
  cLp_def : cLp = φ₀ * ψ₁
  cLm_def : cLm = φ₁ * ψ₀

-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/quark-antiquark-production-reduction.ts

namespace QuarkAntiquarkProduction

variable {R : Type*} [CommRing R] (P : QuarkAntiquarkProduction R)

/-- **Classical limit** `h = 0`: the `σ₀` coefficient loses its
    `q`-correction and reduces to the free-product value `φ₀ + ψ₀`. -/
theorem cσ₀_classical (hh : P.h = 0) : P.cσ₀ = P.φ₀ + P.ψ₀ := by
  rw [P.cσ₀_def, hh]; ring

/-- The Hopf-link coefficients arise purely from the cross-color products;
    their product is the fully symmetric `φ₀φ₁ψ₀ψ₁`. -/
theorem cLp_mul_cLm : P.cLp * P.cLm = P.φ₀ * P.φ₁ * P.ψ₀ * P.ψ₁ := by
  rw [P.cLp_def, P.cLm_def]; ring

/-- When the two photons are identical (`φ = ψ`) the Hopf link is
    balanced: the `L₊` and `L₋` coefficients agree. -/
theorem cLp_eq_cLm_of_eq (h0 : P.φ₀ = P.ψ₀) (h1 : P.φ₁ = P.ψ₁) :
    P.cLp = P.cLm := by
  rw [P.cLp_def, P.cLm_def, h0, h1]; ring

end QuarkAntiquarkProduction

end QOU.Archimedean
