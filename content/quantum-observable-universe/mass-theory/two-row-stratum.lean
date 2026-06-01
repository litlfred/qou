/-!
# `def:two-row-stratum` — sibling pointer

The Lean formalisation of the two-row Wedderburn stratum `Λ²(n)` lives
at the Lake-root module `QOU.BraidKnot.TwoRowStratum` (file
`lean/QOU/BraidKnot/TwoRowStratum.lean`), which declares
`namespace QOU.BraidKnot.TwoRowStratum` / `def TwoRowStratum` and is
imported by `he4-two-row-dominance.lean`. This sibling file re-exports
it so the content-block validator (which resolves a `.lean` sibling next
to the `.ts`) finds the formalisation; the block's `lean.ref` is
`qou:QOU.BraidKnot.TwoRowStratum.TwoRowStratum`.

-- Ref: [manuscript] def:two-row-stratum
-/

import QOU.BraidKnot.TwoRowStratum
