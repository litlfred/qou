/-!
# QOU.Hadron — Composite localized knot (hadronic state)

A hadron is a finite collection of knots at a common base point,
bound by the Hopf link internal structure.  Baryons have three
constituent knots; mesons have two (knot–antiknot pair).

## References

- [leitner2026] §3 Lifting of Quantum Torsion
- [kock2004] https://doi.org/10.1017/CBO9780511615443
-/

import Mathlib.Data.Real.Basic
import QOU.KnotTheory

namespace QOU

/-- A hadron: a composite of knot types at a common point, with
    binding energy from the Hopf link structure. -/
structure Hadron where
  /-- Spherical coordinate θ of the common base point. -/
  theta : ℝ
  /-- Spherical coordinate φ of the common base point. -/
  phi : ℝ
  /-- The constituent knot types (valence quarks in the knot picture). -/
  constituents : List KnotTheory.PlanarDiagram
  /-- A hadron must have at least 2 constituents. -/
  -- Ref: [leitner2026] §3, Definition: Hadron
  constituents_nonempty : constituents.length ≥ 2

/-- A baryon is a hadron with exactly 3 constituents. -/
def Hadron.isBaryon (h : Hadron) : Prop := h.constituents.length = 3

/-- A meson is a hadron with exactly 2 constituents. -/
def Hadron.isMeson (h : Hadron) : Prop := h.constituents.length = 2

end QOU
