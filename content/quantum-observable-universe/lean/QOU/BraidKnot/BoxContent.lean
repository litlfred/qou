import Mathlib.Data.Int.Basic

namespace QOU.BraidKnot

/-- A cell in a Young diagram, parameterized by `(row, col)` (0-indexed). -/
structure Cell where
  row : ℕ
  col : ℕ
deriving DecidableEq, Repr

/-- The content `c = j - i` of a box at position `(i,j)` in a Young diagram.
    This corresponds to the magnetic quantum number `m_j` of the SU_q(2) weight space.
    The content determines the BW scaling function. -/
def boxContent (x : Cell) : ℤ :=
  (x.col : ℤ) - (x.row : ℤ)

end QOU.BraidKnot
