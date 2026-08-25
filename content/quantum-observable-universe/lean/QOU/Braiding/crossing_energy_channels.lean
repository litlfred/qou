/-
  Crossing-energy channel weights and composite channels.

  RELOCATED (no mathematical change).  These five definitions were declared in
  `content/quantum-observable-universe/observations/crossing-energy-decomposition.lean`.  They
  move here because `pair_cancellation` — a declaration the content-block resolver could not
  reach in that chapter-directory file — is stated and proved in terms of them, and a Lake-tree
  module cannot import a chapter `.lean`.  The source file imports this module back: the
  theorems that stay there (`crossingEnergy_split`, the mirror lemmas, the ratio identities)
  still use these definitions.

  The declarations below are verbatim as they stood in the source file — same statements, same
  `-- Ref:` citations.
-/

import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.Braiding

/-- The symmetric (strong) channel weight: cosh(ln q). -/
noncomputable def symmetricWeight (q : ℝ) : ℝ := (q + q⁻¹) / 2

/-- The antisymmetric (Coulomb) channel weight: sinh(ln q). -/
noncomputable def antisymmetricWeight (q : ℝ) : ℝ := (q - q⁻¹) / 2

/-- Total crossing energy of a composite with `p` positive and `m`
negative crossings: `p·q - m·q⁻¹`. -/
noncomputable def crossingEnergy (p m : ℕ) (q : ℝ) : ℝ :=
  (p : ℝ) * q - (m : ℝ) * q⁻¹

/-- Symmetric (strong-binding) channel of the composite. The multiplicity
is `p - m`: the `cosh` part carries the crossing sign. -/
noncomputable def symChannel (p m : ℕ) (q : ℝ) : ℝ :=
  ((p : ℝ) - (m : ℝ)) * symmetricWeight q

/-- Antisymmetric (Coulomb) channel of the composite. The multiplicity is
`p + m`: the `sinh` part is sign-blind, contributing `+sinh λ` for a
negative crossing just as for a positive one. -/
noncomputable def asymChannel (p m : ℕ) (q : ℝ) : ℝ :=
  ((p : ℝ) + (m : ℝ)) * antisymmetricWeight q

end QOU.Braiding
