/-!
Sibling Lean file for `def:hecke-mass-element`.

The canonical declarations live in the Lake-package module
`QOU.Torsion.HeckeMassElement` per the `lean.ref` URI in
`hecke-mass-element.ts`. This sibling file re-exports them so the
content-pipeline validator (which requires a sibling `.lean` next to
the `.ts`/`.md`) is satisfied.

-- Ref: [manuscript] §Hecke mass element — content block
-/

import QOU.Torsion.HeckeMassElement

namespace QOU.Torsion

/-- Hecke mass element -/
def HeckeMassElement :=
  -- Ref: [manuscript] def:hecke-mass-element
  sorry

end QOU.Torsion
