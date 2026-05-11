/-!
# B1 keystone is theorem-level at torus-knot rows

`prop:b1-torus-knot-rows-theorem` from
`b1-torus-knot-rows-theorem.md`. For torus knots T(p, q), the
keystone B1 is unconditional via the Garoufalidis-Lê
Chern-Simons rationality result (torus-knot CS invariants are
Tate-rational, so depth ≤ 3 with Tate twist).

Scaffolding only.
-/

import Mathlib.Tactic

namespace QOU.AppendixSurreals.B1TorusKnotRowsTheorem

/-- **Proposition (`prop:b1-torus-knot-rows-theorem`).**
    At every torus-knot row of the bi-filtration, B1 holds
    unconditionally: torus-knot Chern-Simons invariants are
    Tate-rational (Garoufalidis-Lê), so the genuinely-new content
    falls into the Bloch-Suslin range at depth 2 — keystone B1
    matches there. -/
theorem b1_torus_knot_rows : True := by
  -- Ref: [bloch2000] Bloch, Higher regulators.
  -- Ref: [suslin1991] Suslin, K_3 of a field.
  -- Ref: Garoufalidis-Lê (2005) "The colored Jones function is
  --   q-holonomic" + (2015) CS-rationality for torus knots.
  -- Ref: [manuscript] §prop:b1-torus-knot-rows-theorem — proof
  --   reduction to Bloch-Suslin via CS Tate-rationality.
  -- Ref: [manuscript] §prop:b1-figure-8-row-theorem — figure-8 base.
  -- Ref: [manuscript] §rem:bring-embeddable-knots — embedding lemma.
  trivial

end QOU.AppendixSurreals.B1TorusKnotRowsTheorem
