import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Invertible.Basic
import Mathlib.Tactic.Ring


/-!
# QOU.Torsion.antiparticle_crossing_reversal — Antiparticles from crossing reversal

The mirror operation σ on a knot composite reverses all crossings.  The crossing
energy changes sign under the bar-involution `q ↦ q⁻¹`, the Coulomb charge
reverses, and the bare mass (total crossing count, hence hyperbolic volume) is
preserved.

LaTeX label: `prop:antiparticle-crossing-reversal`

## References
- [leitner2026] Ch. 6, §chirality-trefoil-electron-positron

**Ground ring (§7c)**: a bare `CommRing R`.  The Coulomb channel and the
bar-involution both use `q⁻¹`, but only ever of the substrate parameter itself,
so `q` is carried as a **unit** `q : Rˣ` rather than a nonzero element of a
field — the statements then hold verbatim over `ℤ[q,q⁻¹]`.  Halving the
antisymmetric component needs only `[Invertible (2 : R)]` (written `⅟(2 : R)`),
the exact characteristic condition.  Specialise via `ι : R → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Torsion

variable {R : Type*} [CommRing R] [Invertible (2 : R)]

/-- A knot composite with crossing counts and a substrate parameter `q`. -/
structure KnotComposite (R : Type*) [CommRing R] where
  /-- Number of positive crossings. -/
  pos_crossings : ℕ
  /-- Number of negative crossings. -/
  neg_crossings : ℕ
  /-- Substrate parameter `q`, carried as a unit (§7c). -/
  q : Rˣ

/-- Crossing energy: `+q` per positive crossing, `-q⁻¹` per negative crossing. -/
def KnotComposite.crossingEnergy (H : KnotComposite R) : R :=
  (H.pos_crossings : R) * (H.q : R) + (H.neg_crossings : R) * (-(↑H.q⁻¹ : R))

/-- Bar-involution `q ↦ q⁻¹` applied to the crossing energy. -/
def KnotComposite.barCrossingEnergy (H : KnotComposite R) : R :=
  (H.pos_crossings : R) * (↑H.q⁻¹ : R) + (H.neg_crossings : R) * (-(H.q : R))

/-- Mirror operation: swap positive and negative crossings. -/
def KnotComposite.mirror (H : KnotComposite R) : KnotComposite R where
  pos_crossings := H.neg_crossings
  neg_crossings := H.pos_crossings
  q := H.q

/-- Coulomb charge: antisymmetric component of the crossing energy. -/
def KnotComposite.coulombCharge (H : KnotComposite R) : R :=
  ((H.pos_crossings : R) - (H.neg_crossings : R)) * ((H.q : R) - (↑H.q⁻¹ : R))
    * ⅟(2 : R)

omit [Invertible (2 : R)] in
/-- **Crossing-energy bar-reversal** (narrative claim 2):
    `𝔈(𝔥^σ) = −𝔈(𝔥)|_{q ↦ q⁻¹}` — positive crossings `+q` become negative
    `−q⁻¹` and vice versa under the mirror. -/
-- Ref: [leitner2026] Ch. 6, §chirality-trefoil-electron-positron
theorem crossing_energy_bar_reversal (H : KnotComposite R) :
    H.mirror.crossingEnergy = - H.barCrossingEnergy := by
  simp only [KnotComposite.crossingEnergy, KnotComposite.barCrossingEnergy,
    KnotComposite.mirror]
  ring

/-- **Coulomb-charge reversal** (narrative claim 3):
    `Q(𝔥^σ) = −Q(𝔥)`; in particular `Q(𝔭^σ) = −1` for the antiproton. -/
-- Ref: [leitner2026] Ch. 6, §chirality-trefoil-electron-positron
theorem coulomb_reversal (H : KnotComposite R) :
    H.mirror.coulombCharge = - H.coulombCharge := by
  simp only [KnotComposite.coulombCharge, KnotComposite.mirror]
  ring

/-- **Bare-mass invariance** (narrative claim 4): the mirror preserves the total
    crossing count (hence the knot type and its hyperbolic volume), so a particle
    and its antiparticle have equal bare mass. -/
theorem bare_mass_invariance {S : Type*} [CommRing S] (H : KnotComposite S) :
    H.mirror.pos_crossings + H.mirror.neg_crossings
      = H.pos_crossings + H.neg_crossings := by
  simp only [KnotComposite.mirror]
  omega

/-- **Antiparticles from crossing reversal** (narrative claims 2–4 bundled).
    The mirror operation σ on a knot composite reverses the crossing energy under
    the bar-involution `q ↦ q⁻¹`, reverses the Coulomb charge, and preserves the
    bare mass.  (Claim 1 — that σ *defines* the antiparticle — is the definition
    of `KnotComposite.mirror` itself.) -/
-- Ref: [leitner2026] Ch. 6, §chirality-trefoil-electron-positron
theorem antiparticle_crossing_reversal (H : KnotComposite R) :
    H.mirror.crossingEnergy = - H.barCrossingEnergy
    ∧ H.mirror.coulombCharge = - H.coulombCharge
    ∧ H.mirror.pos_crossings + H.mirror.neg_crossings
        = H.pos_crossings + H.neg_crossings :=
  ⟨crossing_energy_bar_reversal H, coulomb_reversal H, bare_mass_invariance H⟩

end QOU.Torsion
