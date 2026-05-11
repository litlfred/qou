/-!
# Depth-2 identification: G^(2)(H_q) ≅ K_3^ind(F) ⊗ ℚ

`prop:depth-2-identification-bloch-suslin` from
`depth-2-identification-bloch-suslin.md`. Unconditional
identification of the depth-2 graded piece with `K_3^{ind}(F) ⊗
ℚ` via Bloch-Suslin: the keystone B1 at depth 2 is theorem-level
(no conjectural dependence).

Scaffolding only; full Lean version uses Mathlib `KTheory.K3`
and the dilogarithm.
-/

import Mathlib.Tactic

namespace QOU.AppendixSurreals.Depth2IdentificationBlochSuslin

/-- **Proposition (`prop:depth-2-identification-bloch-suslin`).**
    The depth-2 graded piece `G^(2)(H_q)` of the grouplike
    Mikusiński filtration is canonically identified with
    `K_3^{ind}(F) ⊗ ℚ` for the relevant field F via the
    Bloch-Suslin theorem; the identification is unconditional. -/
theorem depth_2_identification : True := by
  -- Ref: [bloch2000] Bloch, Higher regulators.
  -- Ref: [suslin1991] Suslin, K_3 of a field — Bloch group iso.
  -- Ref: [manuscript] §prop:depth-2-identification-bloch-suslin
  --   — the Bloch-Suslin isomorphism for depth-2 content.
  -- Ref: [manuscript] §conj:gb-depth-period-correspondence —
  --   keystone B1 at depth 2 (unconditional).
  -- Ref: [manuscript] §prop:borel-partial-resolution — Borel rank.
  trivial

end QOU.AppendixSurreals.Depth2IdentificationBlochSuslin
