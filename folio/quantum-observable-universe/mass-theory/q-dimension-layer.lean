/-
The q-dimension layer R^|Par(n)|: the per-irrep target structure of the
δ_q decoration.

LaTeX label: `def:q-dimension-layer`
Companion: delta-q-decoration.lean (the map δ_q into this layer)
-/

import Mathlib.Data.Fintype.Card

namespace QOU.BraidKnot

/-- The q-dimension layer: the codomain `R^|Par(n)|` of the δ_q
decoration (`def:delta-q-decoration`), one coordinate per partition
`λ ⊢ n`, recording the per-irrep q-character that the Markov trace
collapses by summing.

Concrete model: the indexing type for the per-irrep tuple is the finite
type of partitions of `n`, here the placeholder `Fin n` (matching the
`delta_q` codomain model in `delta-q-decoration.lean`). The full
per-irrep coordinate ring `R = ℤ[q^±1/2, (q-q⁻¹)⁻¹]` is the upgrade
target shared with `delta_q`.

-- Ref: [wenzl1988] Wenzl 1988, DOI 10.1007/BF01404457
-/
def qDimensionLayer (n : ℕ) : Type := Fin n

end QOU.BraidKnot
