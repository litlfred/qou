import Mathlib.Data.Fin.Basic

/-!
# Edge-gluing exponent data for ideal triangulations

The combinatorics of how tetrahedra are glued: for each edge class `k`, each tetrahedron `i`
and each edge-pair `j`, how many times that edge-pair is glued around `k`. Pure combinatorial
data, split out of `QOU/Transcendental/BraidKnotOctonion/IdealTriangulation.lean` so that the
algebraic gluing equations can be stated outside the transcendental boundary (strangler split,
bean `qou-dk7p`).

-- Ref: [thurston1978] Ch. 4
-- Ref: [neumann-zagier1985]
-/

namespace QOU.MathlibExt

/-- Edge-gluing exponent data: `exp k i j` is the multiplicity with which the
`j`-th edge-pair of tetrahedron `i` meets edge class `k`. -/
structure GluingData (n e : ℕ) where
  /-- The exponents. -/
  exp : Fin e → Fin n → Fin 3 → ℕ

end QOU.MathlibExt
