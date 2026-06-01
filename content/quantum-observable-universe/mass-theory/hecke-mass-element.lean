/-!
# `def:hecke-mass-element` — sibling pointer

The Lean formalisation of the Hecke mass element lives at the Lake-root
module `QOU.Torsion.HeckeMassElement` (file
`lean/QOU/Torsion/HeckeMassElement.lean`), which declares
`namespace QOU.Braiding` / `structure HeckeMassElement` and is imported
by `nuclear-knot-classification.lean` and
`wigner-coefficient-derivation.lean`. This sibling file re-exports it so
the content-block validator (which resolves a `.lean` sibling next to
the `.ts`) finds the formalisation; the block's `lean.ref` is
`qou:QOU.Braiding.HeckeMassElement`.

-- Ref: [manuscript] def:hecke-mass-element
-/

import QOU.Torsion.HeckeMassElement
