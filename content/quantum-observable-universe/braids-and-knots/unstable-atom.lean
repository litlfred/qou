/-!
# QOU.BraidKnot.UnstableAtom — instability as ILP infeasibility

K is unstable at q iff no x ∈ ℤ_{≥0}^N satisfies G(q) x ≥ 0.

LaTeX: `\label{def:unstable-atom}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Unstable atom predicate** at substrate parameter `q : R`. -/
structure UnstableAtom (R : Type u) [CommRing R] where
  /-- The atom-knot. -/
  knot : AtomKnot
  /-- Substrate parameter. -/
  q : R
  /-- The unstable atom is not feasible (ILP-infeasible). -/
  not_feasible : Bool := true

end QOU.BraidKnot
