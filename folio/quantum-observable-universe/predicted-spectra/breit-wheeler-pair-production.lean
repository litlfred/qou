/-
  Breit–Wheeler pair production (categorical), restated on `def:photon`.

  The photon is `QOU.Photon.photon`:
      γ(φ) = 𝟙 + φ₀•σ₀ + φ₁•σ₁ + φ₀₁•σ₀σ₁⁻¹
  (owner ruling, bean `qou-99qc`, 2026-11-18, confirmed 2026-11-20: the fourth
  term is the chiral vertex σ₀σ₁⁻¹). It replaces the former one-weight
  `ColoredPhoton` (`γ_φ = 𝟙 + φσ₀ + φσ₁`) and its `pairThreshold`, which were a
  separate, one-parameter object (photon-usage audit 2026-11-17, conflict C4).

  What this file now states:
  * the linear and circular Breit–Wheeler photons are NAMED specialisations of
    the four-term photon with `φ₀₁ = 0` (their weights 0.0487 / 0.0978 are fits
    in the narrative and are not used here);
  * two bare photons fuse to `𝟙`, not to `σ₀²`: a single crossing is a term of
    a photon, not a photon.

  Generic commutative ring `R`, any `R`-algebra `A`, `σ₁` a unit (§7c).

  Ref: [leitner2026] Chapter 6, §3b; def:photon
-/
import QOU.Photon

namespace QOU.Archimedean

open QOU.Photon

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Linear (symmetric) polarisation: `φ₀ = φ₁ = φ`, `φ₀₁ = 0`. -/
def linearColour (φ : R) : Colour R := ⟨φ, φ, 0⟩

/-- Circular polarisation, first photon: `φ₀ = s`, `φ₁ = φ₀₁ = 0`. -/
def circularColourFirst (s : R) : Colour R := ⟨s, 0, 0⟩

/-- Circular polarisation, second photon: `φ₁ = s`, `φ₀ = φ₀₁ = 0`. -/
def circularColourSecond (s : R) : Colour R := ⟨0, s, 0⟩

/-- The linear Breit–Wheeler photon is the `φ₀₁ = 0` specialisation of `def:photon`. -/
theorem photon_linearColour (σ₀ : A) (σ₁ : Aˣ) (φ : R) :
    photon σ₀ σ₁ (linearColour φ) = 1 + φ • σ₀ + φ • (σ₁ : A) :=
  photon_threeTerm σ₀ σ₁ (linearColour φ) rfl

/-- The circular Breit–Wheeler photons are `φ₀₁ = 0` specialisations of `def:photon`. -/
theorem photon_circularColour (σ₀ : A) (σ₁ : Aˣ) (s : R) :
    photon σ₀ σ₁ (circularColourFirst s) = 1 + s • σ₀ ∧
      photon σ₀ σ₁ (circularColourSecond s) = 1 + s • (σ₁ : A) := by
  constructor <;> simp [photon, circularColourFirst, circularColourSecond]

/-- **Breit–Wheeler pair production — bare pair.** Two bare photons fuse to the
    identity (the empty knot), so a bare photon pair carries no crossing at all;
    the former `γγ = σ₀²` read a single crossing as a photon. -/
-- Ref: [leitner2026] Chapter 6, §3b; def:photon
theorem breit_wheeler_pair_production (σ₀ : A) (σ₁ : Aˣ) :
    photon σ₀ σ₁ (bare : Colour R) * photon σ₀ σ₁ (bare : Colour R) = 1 := by
  simp [photon_bare]

end QOU.Archimedean
