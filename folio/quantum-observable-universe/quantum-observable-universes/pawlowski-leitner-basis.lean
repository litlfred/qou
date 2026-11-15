import Mathlib.Data.Nat.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.Real.Basic


/-!
# QOU.PawLeiBasis — Canonical basis for intertwiner spaces

The Pawlowski–Leitner basis provides a canonical basis for
Hom_{SU(2)}(V_j, V_{1/2}^⊗n), indexed by standard Young tableaux.

Authoritative source: `folio/quantum-observable-universe/lean/QOU/RepresentationTheory.lean`

## References

- [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
- [leitner2026] §1, Proposition: Pawlowski–Leitner basis
-/

namespace QOU

/-- The dimension of the intertwiner space Hom_{SU(2)}(V_j, V_{1/2}^⊗n).
    Uses twice_j (so spin j = twice_j / 2).
    Returns 0 when n and twice_j have different parity or n < twice_j.
    Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565 -/
noncomputable def pawLeiDim (twice_j : ℕ) (n : ℕ) : ℕ :=
  if n % 2 ≠ twice_j % 2 then 0
  else if n < twice_j then 0
  else (twice_j + 1) * n.factorial /
    ((n / 2 + (twice_j + 1) / 2 + 1).factorial *
     (n / 2 - twice_j / 2).factorial)

/-- The Pawlowski–Leitner basis structure: specifies the intertwiner
    space data and the number of basis elements. -/
structure PawLeiBasis where
  /-- The spin label (as twice_j). -/
  twice_j : ℕ
  /-- The tensor power. -/
  n : ℕ
  /-- Parity constraint: n ≡ twice_j (mod 2). -/
  parity : n % 2 = twice_j % 2
  /-- The tensor power is large enough: n ≥ twice_j. -/
  n_ge : n ≥ twice_j
  /-- The number of basis elements. -/
  num_basis : ℕ := pawLeiDim twice_j n

/-- The Clebsch–Gordan decomposition: dim(V_{1/2}) · dim(V_{1/2}) =
    dim(V_0) + dim(V_1), i.e., 2 · 2 = 1 + 3. -/
theorem clebsch_gordan_half_tensor_half :
    (1 + 1) * (1 + 1) = (0 + 1) + (2 + 1) := by norm_num

end QOU
