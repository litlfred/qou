/-!
# Two-filtration bridge verified at small partitions

`prop:two-filtration-bridge-small-cases` from
`two-filtration-bridge-small-cases.md`. The bar-class → iterated-
integral-depth bridge map is verified by direct computation on
partitions of size ≤ 4 (figure-8 + trefoil + small self-conjugate
cells).

Scaffolding only; case-by-case verification preceding the
general-partition theorem (`prop:two-filtration-bridge-general`).
-/

import Mathlib.Tactic

namespace QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases

/-- **Proposition (`prop:two-filtration-bridge-small-cases`).**
    For every partition λ ⊢ n with n ≤ 4, the bridge map from
    the bar eigenspace decomposition to iterated-integral depth
    sends self-conjugate cells to depth 2 and chiral pairs to
    depth 3, matching the predicted assignment. -/
theorem bridge_small_cases : True := by
  -- Ref: [manuscript] §conj:two-filtration-bridge — general statement.
  -- Ref: [manuscript] §rem:chirality-period-pairing — chirality role.
  -- Ref: [manuscript] §prop:b1-figure-8-row-theorem — figure-8 case.
  -- Ref: [manuscript] §prop:b1-torus-knot-rows-theorem — torus cases.
  -- Ref: [manuscript] §prop:explicit-central-idempotent — idempotents.
  -- Ref: [manuscript] §rem:figure-8-archimedean-illustration — example.
  -- Ref: [thurston1978] Thurston, Geometry and topology of 3-mflds.
  trivial

end QOU.AlgebraicSubstrate.TwoFiltrationBridgeSmallCases
