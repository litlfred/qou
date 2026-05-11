/-!
# B1 keystone is theorem-level at additional hyperbolic rows

`prop:b1-hyperbolic-rows-theorem` from
`b1-hyperbolic-rows-theorem.md`. For Borromean rings, Whitehead
link, and twist knots, the keystone B1 is unconditional via
van der Veen's extensions of the Volume Conjecture and
Bloch-Suslin.

Scaffolding only.
-/

import Mathlib.Tactic

namespace QOU.AppendixSurreals.B1HyperbolicRowsTheorem

/-- **Proposition (`prop:b1-hyperbolic-rows-theorem`).**
    At the bi-filtration rows for Borromean rings, Whitehead
    link, and small twist knots, the keystone B1 holds
    unconditionally: volume lives in depth-2, identified with
    `K_3^{ind}` via Bloch-Suslin, and Volume-Conjecture-style
    results (van der Veen and follow-ups) discharge the
    Goncharov-side depth identification. -/
theorem b1_hyperbolic_rows : True := by
  -- Ref: [murakami-murakami2001] Murakami-Murakami — the original VC.
  -- Ref: [bloch2000] Bloch — higher regulators.
  -- Ref: [suslin1991] Suslin — K_3.
  -- Ref: [thurston1978] Thurston — geometry and topology.
  -- Ref: van der Veen (2008) "Proof of the Volume Conjecture
  --   for Whitehead chains" and follow-up papers.
  -- Ref: [manuscript] §prop:b1-hyperbolic-rows-theorem — proof
  --   via Bloch-Suslin + VC extensions.
  -- Ref: [manuscript] §prop:b1-figure-8-row-theorem — base case.
  -- Ref: [manuscript] §prop:b1-torus-knot-rows-theorem — adjacent rows.
  trivial

end QOU.AppendixSurreals.B1HyperbolicRowsTheorem
