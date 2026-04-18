/-!
# QOU.BraidKnot.DressedParticle

A dressed particle is the codomain of a dressing morphism
P_bare → P_dressed in the confinement category. Dressings compose
via shell concatenation; stripping is not in general invertible.

LaTeX: `\label{def:dressed-particle}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Dressed particle.** Codomain of a dressing morphism; carries
a bare-particle core, a shell-multiplicity record, and the
composite Markov class. -/
-- Ref: [manuscript] braids-and-knots/dressed-particle
structure DressedParticle (R : Type u) [CommRing R] where
  bareName : String
  shellSize : Nat
  level : Nat

end QOU.BraidKnot
