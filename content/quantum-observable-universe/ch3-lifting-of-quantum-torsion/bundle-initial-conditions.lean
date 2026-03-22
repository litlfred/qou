/-!
# QOU.BundleInitialConditions — Big bang state over the projective line

A bundle initial condition is a finite collection of localized knots
on CP¹.  This is the "position-only" specification at the initial
moment: positions are known exactly, momenta are undetermined.

## References

- [leitner2026] §3 Lifting of Quantum Torsion
-/

import Mathlib.Data.Real.Basic
import QOU.KnotTheory

namespace QOU

/-- A bundle initial condition: a finite set of localized knots on CP¹. -/
structure BundleInitialConditions where
  /-- The localized knots (position + knot type pairs). -/
  particles : List LocalizedKnot
  /-- Must have at least one particle. -/
  -- Ref: [leitner2026] §3, Definition: Bundle initial conditions
  nonempty : particles.length ≥ 1

/-- Total number of particles in the bundle. -/
def BundleInitialConditions.size (b : BundleInitialConditions) : ℕ :=
  b.particles.length

/-- Total crossing number of all knots in the bundle. -/
def BundleInitialConditions.totalCrossings (b : BundleInitialConditions) : ℕ :=
  b.particles.foldl (fun acc p => acc + p.knot.crossingCount) 0

end QOU
