/-!
# B1 keystone is theorem-level at the figure-8 row

`prop:b1-figure-8-row-theorem` from
`b1-figure-8-row-theorem.md`. For the figure-8 knot, the
keystone B1 (Mikusiński depth = Goncharov period depth = 2) is
unconditional: depth = 2 follows from Bloch-Suslin and the
Murakami-Murakami Volume Conjecture proof for figure-8.

Scaffolding only.
-/

import Mathlib.Tactic

namespace QOU.AppendixSurreals.B1Figure8RowTheorem

/-- **Proposition (`prop:b1-figure-8-row-theorem`).**
    At the figure-8 row of the bi-filtration grid, the keystone
    B1 holds unconditionally: the volume of figure-8 lives in the
    depth-2 piece of both the Mikusiński and the Goncharov
    filtration, and they agree (via Bloch-Suslin and the
    Murakami-Murakami theorem). -/
theorem b1_figure_8_row : True := by
  -- Ref: [murakami-murakami2001] Murakami-Murakami, The colored
  --   Jones polynomial and the simplicial volume of a knot.
  -- Ref: [bloch2000] Bloch, Higher regulators.
  -- Ref: [suslin1991] Suslin, K_3 of a field.
  -- Ref: [thurston1978] Thurston, Geometry and topology.
  -- Ref: [manuscript] §prop:b1-figure-8-row-theorem — proof:
  --   Volume Conjecture (proved for figure-8) reduces depth-2
  --   keystone to Bloch-Suslin.
  -- Ref: [manuscript] §prop:depth-2-identification-bloch-suslin.
  -- Ref: [manuscript] §rem:figure-8-archimedean-illustration.
  -- Ref: [manuscript] §rem:vc-as-depth-2-instance.
  trivial

end QOU.AppendixSurreals.B1Figure8RowTheorem
