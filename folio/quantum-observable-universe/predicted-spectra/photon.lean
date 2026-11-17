/-
  Photon: the four-term Hecke element γ(φ) = 𝟙 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁.

  Stated in any R-algebra A containing the two Hecke generators σ₀, σ₁, over
  a generic commutative ring R (§7c: no ordering, no Real construct).

  -- Ref: [leitner2026] predicted-spectra, def:photon
-/
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Tactic

namespace QOU.Photon

/-- The three colour weights `(φ₀, φ₁, φ₀₁)` of a photon. -/
structure Colour (R : Type*) where
  phi0 : R
  phi1 : R
  phi01 : R

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **The photon** `γ(φ) = 𝟙 + φ₀•σ₀ + φ₁•σ₁ + φ₀₁•(σ₀σ₁)`. -/
def photon (σ₀ σ₁ : A) (c : Colour R) : A :=
  1 + c.phi0 • σ₀ + c.phi1 • σ₁ + c.phi01 • (σ₀ * σ₁)

/-- The bare photon: all colour weights zero. -/
def bare : Colour R := ⟨0, 0, 0⟩

/-- The bare photon is the identity element (the empty knot). -/
theorem photon_bare (σ₀ σ₁ : A) : photon σ₀ σ₁ (bare : Colour R) = 1 := by
  simp [photon, bare]

/-- The three-term form is the specialisation `φ₀₁ = 0`. -/
theorem photon_threeTerm (σ₀ σ₁ : A) (c : Colour R) (h : c.phi01 = 0) :
    photon σ₀ σ₁ c = 1 + c.phi0 • σ₀ + c.phi1 • σ₁ := by
  simp [photon, h]

end QOU.Photon
