import QOU.Basic
import QOU.ParticleInteractions.AtomKnot


/-!
# QOU.BraidKnot.StableAtom — stability via ILP feasibility

K is stable at q iff ∃ x ∈ ℤ_{≥0}^N with G(q) x ≥ 0.

LaTeX: `\label{def:stable-atom}`
-/

namespace QOU.BraidKnot

universe u

/-- **Stable atom predicate** at substrate parameter `q : R`.

    Records ILP feasibility of the Frobenius positivity constraints
    in the confinement filtration `J^ℓ(q)`. -/
structure StableAtom (R : Type u) [CommRing R] where
  /-- The atom-knot. -/
  knot : AtomKnot
  /-- Substrate parameter. -/
  q : R
  /-- Boolean: ILP feasible at q. -/
  feasible : Bool

end QOU.BraidKnot
