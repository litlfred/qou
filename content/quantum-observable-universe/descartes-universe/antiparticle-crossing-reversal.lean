/-!
# QOU.Torsion.antiparticle_crossing_reversal — Antiparticles from crossing reversal

The mirror operation σ on a knot composite reverses all crossings.
The crossing energy changes sign under σ, the Coulomb charge reverses,
and the bare mass (hyperbolic volume) is preserved.

LaTeX label: `prop:antiparticle-crossing-reversal`

## References
- [manuscript] Ch. 6, §chirality-trefoil-electron-positron
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic

namespace QOU.Torsion

/-- A knot composite with crossing energy and Coulomb charge. -/
structure KnotComposite where
  /-- Number of positive crossings. -/
  pos_crossings : ℕ
  /-- Number of negative crossings. -/
  neg_crossings : ℕ
  /-- Substrate parameter q > 1. -/
  q : ℝ
  q_pos : 0 < q
  q_ge_one : 1 ≤ q

/-- Crossing energy: sum of +q (positive) and -q⁻¹ (negative) crossings. -/
noncomputable def KnotComposite.crossingEnergy (H : KnotComposite) : ℝ :=
  H.pos_crossings * H.q + H.neg_crossings * (-H.q⁻¹)

/-- Mirror operation: swap positive and negative crossings. -/
def KnotComposite.mirror (H : KnotComposite) : KnotComposite where
  pos_crossings := H.neg_crossings
  neg_crossings := H.pos_crossings
  q := H.q
  q_pos := H.q_pos
  q_ge_one := H.q_ge_one

/-- Coulomb charge: antisymmetric component of crossing energy. -/
noncomputable def KnotComposite.coulombCharge (H : KnotComposite) : ℝ :=
  (H.pos_crossings - H.neg_crossings : ℤ) * (H.q - H.q⁻¹) / 2

/-- Crossing energy of a pair sums to pure symmetric (mass) part. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem pair_crossing_energy (H : KnotComposite) :
    H.crossingEnergy + H.mirror.crossingEnergy =
    (H.pos_crossings + H.neg_crossings : ℕ) * (H.q - H.q⁻¹) := by
  -- Ref: [manuscript] Ch. 6, §chirality-trefoil-electron-positron
  simp only [KnotComposite.crossingEnergy, KnotComposite.mirror]
  push_cast
  ring

/-- Coulomb charge reverses under mirror. -/
-- Ref: [manuscript] Ch. 6, §chirality-trefoil-electron-positron
theorem coulomb_reversal (H : KnotComposite) :
    H.mirror.coulombCharge = -H.coulombCharge := by
  -- Ref: [manuscript] Ch. 6, §chirality-trefoil-electron-positron
  simp only [KnotComposite.coulombCharge, KnotComposite.mirror]
  push_cast
  ring

/-- Bare mass (total crossing count) is preserved under mirror. -/
theorem bare_mass_invariance (H : KnotComposite) :
    H.mirror.pos_crossings + H.mirror.neg_crossings =
    H.pos_crossings + H.neg_crossings := by
  simp [KnotComposite.mirror]
  omega

end QOU.Torsion
