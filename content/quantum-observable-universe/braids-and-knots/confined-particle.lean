/-!
# QOU.BraidKnot.ConfinedParticle

Confined particle tuple (name, level, Markov-class of closed braid,
coarse strand count). Named via registry (particle-shortcut);
Markov class represented canonically by Gröbner-Shirshov NF.
Confinement at q is a separate SDP-feasibility predicate.

LaTeX: `\label{def:confined-particle}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Confined particle.** A named tuple at a confinement level
with an underlying Markov-class of closed braid and coarse strand
count. Stability predicates layer on top. -/
-- Ref: [manuscript] braids-and-knots/confined-particle
structure ConfinedParticle (R : Type u) [CommRing R] where
  name : String
  level : Nat
  nStrands : Nat
  q : R

end QOU.BraidKnot
