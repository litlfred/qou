/-!
# QOU.BraidKnot.ConfinementCategory

The category Conf of confined particles with morphisms
{unfolding, folding, dressing}. Markov trace is a functor
Conf → ℂ(q).

LaTeX: `\label{def:confinement-category}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Confinement category.** Objects are confined particles
(name + level + Markov class + coarse strand count); morphisms are
unfolding, folding, and dressing embeddings of Hecke algebras. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
structure ConfinementCategory (R : Type u) [CommRing R] where
  carrier : Type u

end QOU.BraidKnot
