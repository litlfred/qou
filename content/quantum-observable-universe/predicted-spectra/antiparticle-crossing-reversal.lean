import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp


/-!
# QOU.Torsion.antiparticle_crossing_reversal — Antiparticles from crossing reversal

The mirror operation σ on a knot composite reverses all crossings.  The crossing
energy changes sign under the bar-involution `q ↦ q⁻¹`, the Coulomb charge
reverses, and the bare mass (total crossing count, hence hyperbolic volume) is
preserved.

LaTeX label: `prop:antiparticle-crossing-reversal`

## References
- [manuscript] Ch. 6, §chirality-trefoil-electron-positron

**Ground ring**: a field `R` carrying the substrate parameter `q`.  The Coulomb
channel and the bar-involution both use `q⁻¹`, so the realisation field must
admit inverses; specialise via `ι : R → ℝ, q ↦ q₀` for numerical evaluation.
-/

namespace QOU.Torsion

variable {R : Type*} [Field R]

/-- A knot composite with crossing counts and a substrate parameter `q`. -/
structure KnotComposite (R : Type*) where
  /-- Number of positive crossings. -/
  pos_crossings : ℕ
  /-- Number of negative crossings. -/
  neg_crossings : ℕ
  /-- Substrate parameter `q`. -/
  q : R

/-- Crossing energy: `+q` per positive crossing, `-q⁻¹` per negative crossing. -/
def KnotComposite.crossingEnergy (H : KnotComposite R) : R :=
  (H.pos_crossings : R) * H.q + (H.neg_crossings : R) * (-H.q⁻¹)

/-- Bar-involution `q ↦ q⁻¹` applied to the crossing energy. -/
def KnotComposite.barCrossingEnergy (H : KnotComposite R) : R :=
  (H.pos_crossings : R) * H.q⁻¹ + (H.neg_crossings : R) * (-H.q)

/-- Mirror operation: swap positive and negative crossings. -/
def KnotComposite.mirror (H : KnotComposite R) : KnotComposite R where
  pos_crossings := H.neg_crossings
  neg_crossings := H.pos_crossings
  q := H.q

/-- Coulomb charge: antisymmetric component of the crossing energy. -/
def KnotComposite.coulombCharge (H : KnotComposite R) : R :=
  ((H.pos_crossings : R) - (H.neg_crossings : R)) * (H.q - H.q⁻¹) / 2

/-- **Crossing-energy bar-reversal** (narrative claim 2):
    `𝔈(𝔥^σ) = −𝔈(𝔥)|_{q ↦ q⁻¹}` — positive crossings `+q` become negative
    `−q⁻¹` and vice versa under the mirror. -/
-- Ref: [manuscript] Ch. 6, §chirality-trefoil-electron-positron
theorem crossing_energy_bar_reversal (H : KnotComposite R) :
    H.mirror.crossingEnergy = - H.barCrossingEnergy := by
  simp only [KnotComposite.crossingEnergy, KnotComposite.barCrossingEnergy,
    KnotComposite.mirror]
  ring

/-- **Coulomb-charge reversal** (narrative claim 3):
    `Q(𝔥^σ) = −Q(𝔥)`; in particular `Q(𝔭^σ) = −1` for the antiproton. -/
-- Ref: [manuscript] Ch. 6, §chirality-trefoil-electron-positron
theorem coulomb_reversal (H : KnotComposite R) :
    H.mirror.coulombCharge = - H.coulombCharge := by
  simp only [KnotComposite.coulombCharge, KnotComposite.mirror]
  ring

/-- **Bare-mass invariance** (narrative claim 4): the mirror preserves the total
    crossing count (hence the knot type and its hyperbolic volume), so a particle
    and its antiparticle have equal bare mass. -/
theorem bare_mass_invariance (H : KnotComposite R) :
    H.mirror.pos_crossings + H.mirror.neg_crossings
      = H.pos_crossings + H.neg_crossings := by
  simp only [KnotComposite.mirror]
  omega

/-- **Antiparticles from crossing reversal** (narrative claims 2–4 bundled).
    The mirror operation σ on a knot composite reverses the crossing energy under
    the bar-involution `q ↦ q⁻¹`, reverses the Coulomb charge, and preserves the
    bare mass.  (Claim 1 — that σ *defines* the antiparticle — is the definition
    of `KnotComposite.mirror` itself.) -/
-- Ref: [manuscript] Ch. 6, §chirality-trefoil-electron-positron
theorem antiparticle_crossing_reversal (H : KnotComposite R) :
    H.mirror.crossingEnergy = - H.barCrossingEnergy
    ∧ H.mirror.coulombCharge = - H.coulombCharge
    ∧ H.mirror.pos_crossings + H.mirror.neg_crossings
        = H.pos_crossings + H.neg_crossings :=
  ⟨crossing_energy_bar_reversal H, coulomb_reversal H, bare_mass_invariance H⟩

end QOU.Torsion
