/-!
# QOU.LocalizedKnot — Knot localized at a point on the projective line

A localized knot is a pair (p, K) where p is a categorical point of
the projective line P(V) = G/T and K is a knot type.  This is the
fundamental unit of matter in the QOU framework.

## References

- [leitner2026] §3 Lifting of Quantum Torsion
-/

import Mathlib.Data.Real.Basic
import QOU.KnotTheory

namespace QOU

/-- A localized knot: a knot type placed at a point on the base manifold.
    The point is represented abstractly as an element of the projective line
    (in the archimedean case, a point on CP¹ ≅ S²). -/
structure LocalizedKnot where
  /-- Spherical coordinate θ ∈ [0, π] on CP¹ ≅ S². -/
  theta : ℝ
  /-- Spherical coordinate φ ∈ [0, 2π) on CP¹ ≅ S². -/
  phi : ℝ
  /-- The knot type at this point (given by its planar diagram). -/
  knot : KnotTheory.PlanarDiagram
  /-- θ is in valid range. -/
  theta_range : 0 ≤ theta ∧ theta ≤ Real.pi
  /-- φ is in valid range. -/
  -- Ref: [leitner2026] §3, Definition: Localized knot
  phi_range : 0 ≤ phi ∧ phi < 2 * Real.pi

end QOU
