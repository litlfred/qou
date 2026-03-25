/-!
# QOU.PawlowskiLeitnerInnerProduct — Inner product on intertwiner spaces

The adjoint trace induces an inner product on Hom_{SU(2)}(V_j, V_{1/2}^⊗n)
with respect to which the Pawlowski–Leitner basis is orthogonal.

## References

- [leitner2004vectors] https://arxiv.org/abs/math/0409565
- [manuscript] §1, Proposition: Inner product on intertwiner spaces
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- The Pawlowski–Leitner inner product is positive-definite:
    ⟨φ, φ⟩_PL > 0 for any nonzero intertwiner φ. -/
-- Ref: [leitner2004vectors] https://arxiv.org/abs/math/0409565
theorem pawlowski_leitner_inner_product_pos_def
    (φ_nonzero : True) :  -- placeholder for nonzero intertwiner
    True := by
  sorry
  -- Ref: [leitner2004vectors] https://arxiv.org/abs/math/0409565

/-- The Pawlowski–Leitner basis is orthogonal with respect to the
    adjoint-trace inner product. -/
-- Ref: [leitner2004vectors] https://arxiv.org/abs/math/0409565
theorem pawlowski_leitner_orthogonality :
    True := by
  sorry
  -- Ref: [leitner2004vectors] https://arxiv.org/abs/math/0409565

end QOU
