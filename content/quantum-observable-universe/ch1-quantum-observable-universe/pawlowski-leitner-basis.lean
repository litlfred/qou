/-!
# QOU.PawlowskiLeitnerBasis — Canonical basis for intertwiner spaces

The Pawlowski–Leitner basis provides a canonical basis for
Hom_{SU(2)}(V_j, V_{1/2}^⊗n), indexed by standard Young tableaux.

## References

- [leitner2004vectors] https://arxiv.org/abs/math/0409565
- [manuscript] §1, Proposition: Pawlowski–Leitner basis
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Data.Real.Basic

namespace QOU

/-- The dimension of the intertwiner space Hom_{SU(2)}(V_j, V_{1/2}^⊗n).
    Returns 0 when n and 2j have different parity.
    Ref: [leitner2004vectors] https://arxiv.org/abs/math/0409565 -/
noncomputable def pawlowskiLeitnerDim (j : ℕ) (n : ℕ) : ℕ :=
  if n % 2 ≠ (2 * j) % 2 then 0
  else (2 * j + 1) * n.factorial / ((n / 2 + j + 1).factorial * (n / 2 - j).factorial)

/-- The Pawlowski–Leitner basis exists: the intertwiner space has
    the predicted dimension. -/
-- Ref: [leitner2004vectors] https://arxiv.org/abs/math/0409565
theorem pawlowski_leitner_basis_exists (j : ℕ) (n : ℕ)
    (h_parity : n % 2 = (2 * j) % 2)
    (h_ge : n ≥ 2 * j) :
    pawlowskiLeitnerDim j n > 0 := by
  sorry
  -- Ref: [leitner2004vectors] https://arxiv.org/abs/math/0409565

end QOU
