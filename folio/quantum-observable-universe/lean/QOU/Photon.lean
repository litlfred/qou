/-
  Photon: the four-term Hecke element
      γ(φ) = 𝟙 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹.

  Library home of `def:photon` (knots-particles-confinement/photon.md). It lives in the
  library, not as a content-block sibling, so that library modules can import
  it and state their photons with this one `photon` rather than a local copy.

  The fourth term is the chiral pair-production vertex `V = σ₀σ₁⁻¹`, the γγ̄
  vertex of the corpus (owner ruling, bean `qou-99qc` entry of 2026-11-18,
  confirmed 2026-11-20). It is NOT `σ₀σ₁`. The earlier form
  `𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁` is the same family of elements in different
  coordinates: in `H_n(q)`, where `σ₁⁻¹ = σ₁ − h` with `h = q − q⁻¹`,
  `γ(φ₀, φ₁, φ₀₁) = 𝟙 + (φ₀ − hφ₀₁)σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁`
  (`QOU.Mass.PhotonTraceLemmas.photon_eq_straight`).

  Stated in any `R`-algebra `A`, with `σ₀ : A` and `σ₁ : Aˣ` a unit, so that
  `σ₁⁻¹` is a genuine two-sided inverse and no relation of `H_n(q)` is used
  in the definition. Generic commutative ring `R` (§7c: no ordering, no Real
  construct).

  -- Ref: [leitner2026] predicted-spectra, def:photon
-/
import Mathlib.Algebra.Algebra.Defs

namespace QOU.Photon

/-- The three colour weights `(φ₀, φ₁, φ₀₁)` of a photon. -/
structure Colour (R : Type*) where
  phi0 : R
  phi1 : R
  phi01 : R

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- The chiral pair-production vertex `σ₀σ₁⁻¹`. -/
def vertex (σ₀ : A) (σ₁ : Aˣ) : A := σ₀ * ↑σ₁⁻¹

/-- **The photon** `γ(φ) = 𝟙 + φ₀•σ₀ + φ₁•σ₁ + φ₀₁•(σ₀σ₁⁻¹)`. -/
def photon (σ₀ : A) (σ₁ : Aˣ) (c : Colour R) : A :=
  1 + c.phi0 • σ₀ + c.phi1 • (σ₁ : A) + c.phi01 • vertex σ₀ σ₁

/-- The bare photon: all colour weights zero. -/
def bare : Colour R := ⟨0, 0, 0⟩

/-- The bare photon is the identity element (the empty knot). -/
theorem photon_bare (σ₀ : A) (σ₁ : Aˣ) : photon σ₀ σ₁ (bare : Colour R) = 1 := by
  simp [photon, bare]

/-- The three-term form is the specialisation `φ₀₁ = 0`. -/
theorem photon_threeTerm (σ₀ : A) (σ₁ : Aˣ) (c : Colour R) (h : c.phi01 = 0) :
    photon σ₀ σ₁ c = 1 + c.phi0 • σ₀ + c.phi1 • (σ₁ : A) := by
  simp [photon, h]

/-- The vertex times `σ₁` is `σ₀`: `(σ₀σ₁⁻¹)σ₁ = σ₀`. -/
theorem vertex_mul (σ₀ : A) (σ₁ : Aˣ) : vertex σ₀ σ₁ * (σ₁ : A) = σ₀ := by
  simp [vertex, mul_assoc]

end QOU.Photon
