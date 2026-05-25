/-!
# def:quantum-dilogarithm-disambiguation — sibling stub

This sibling stub for the content block
`def:quantum-dilogarithm-disambiguation` is the validation-required
companion of the canonical definitions in
`QOU/BraidKnot/QuantumDilogarithm.lean`.

The canonical content lives there (`phi_q`, `li2_q`, `towerTerm`,
`HasCorrectedMassEndomorphismTower`). This sibling re-exports the
namespace for chapter-level discovery and pins the Lake-package
URI used by the content manifest.

LaTeX label: `\label{def:quantum-dilogarithm-disambiguation}`

Ref: [manuscript] def:quantum-dilogarithm-disambiguation
Ref: [manuscript] prop:mass-endomorphism-tower (parent prop)
-/

import QOU.BraidKnot.QuantumDilogarithm

namespace QOU.BraidKnot

-- Anti-regression discipline: the canonical archimedean
-- specialisation of the mass-endomorphism tower is -li2_q(-|V|),
-- not phi_q. See sibling docs and the
-- HasCorrectedMassEndomorphismTower class above.

end QOU.BraidKnot
