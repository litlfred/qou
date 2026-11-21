/-!
# QOU.Torsion.LinkingOperation — the two geometric linking operations

The two linking operations that build composite knots from the
torus-knot generators: Hopf linking on the exceptional divisor and
color-tube threading of the color-tube fibration.

LaTeX label: `def:linking-operations`

## References

- [leitner2026] §11/knot-particle-generation
-/

namespace QOU.Torsion

/-- The two geometric linking operations acting on the exceptional
    divisor and the color-tube fibration. -/
-- Ref: [leitner2026] §11/knot-particle-generation
inductive LinkingOperation
  /-- Hopf linking on the exceptional divisor. -/
  | hopfLinking
  /-- Color-tube threading of the color-tube fibration. -/
  | colorTubeThreading

end QOU.Torsion
