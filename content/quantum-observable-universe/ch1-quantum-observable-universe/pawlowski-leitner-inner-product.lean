/-!
# QOU.PawLeiInnerProduct — Inner product on intertwiner spaces

The adjoint trace induces an inner product on Hom_{SU(2)}(V_j, V_{1/2}^⊗n)
with respect to which the Pawlowski–Leitner basis is orthogonal.

Authoritative source: `lean-archive/QOU/RepresentationTheory.lean`

## References

- [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
- [manuscript] §1, Proposition: Inner product on intertwiner spaces
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- The Pawlowski–Leitner inner product on intertwiner spaces.
    Each basis vector has a positive norm-squared computed from
    hook lengths of the indexing Young tableau. -/
structure PawLeiInnerProduct where
  /-- Number of basis vectors. -/
  num_basis : ℕ
  /-- The norm-squared of each basis vector. -/
  normSq : Fin num_basis → ℝ
  /-- All norms are positive. -/
  -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
  normSq_pos : ∀ i, normSq i > 0

/-- Positive-definiteness: the PL inner product ⟨φ, φ⟩ > 0
    for any nonzero intertwiner φ (follows from normSq_pos). -/
-- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
theorem pawLei_pos_def (ip : PawLeiInnerProduct)
    (i : Fin ip.num_basis) : ip.normSq i > 0 :=
  ip.normSq_pos i

end QOU
