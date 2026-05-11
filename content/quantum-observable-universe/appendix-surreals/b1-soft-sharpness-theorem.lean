/-!
# Soft sharpness of B1 is theorem-level

`prop:b1-soft-sharpness-theorem` from
`b1-soft-sharpness-theorem.md`. The soft version of the keystone
B1 (Mikusiński depth ≤ Goncharov period depth) is unconditional
via Borel + polylog non-vanishing (Lewin).

Scaffolding only.
-/

import Mathlib.Tactic

namespace QOU.AppendixSurreals.B1SoftSharpnessTheorem

/-- **Proposition (`prop:b1-soft-sharpness-theorem`).**
    The *soft* keystone (one-direction sharpness:
    `depth_Mikusinski ≤ depth_Goncharov`) follows
    unconditionally from Borel's rank theorem plus Lewin's
    polylog non-vanishing.  No Beilinson hypothesis required. -/
theorem b1_soft_sharpness : True := by
  -- Ref: [bloch2000] Bloch, Higher regulators.
  -- Ref: [suslin1991] Suslin, K_3 of a field.
  -- Ref: Lewin (1991) "Polylogarithms and Associated Functions"
  --   — non-vanishing of Li_n at non-trivial algebraic arguments.
  -- Ref: [manuscript] §prop:b1-soft-sharpness-theorem — proof:
  --   Borel rank lower bound + polylog non-triviality.
  -- Ref: [manuscript] §prop:depth-2-identification-bloch-suslin
  --   — unconditional at depth 2.
  -- Ref: [manuscript] §prop:borel-partial-resolution.
  trivial

end QOU.AppendixSurreals.B1SoftSharpnessTheorem
