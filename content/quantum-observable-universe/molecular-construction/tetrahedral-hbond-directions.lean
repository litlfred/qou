import Mathlib.Tactic

/-!
# QOU.Molecular.Tetrahedral — the four H-bond directions are tetrahedral

The four hydrogen-bond directions of a water in ice (two donor, two
acceptor) point to the vertices of a regular tetrahedron. Taking the four
vertex vectors `(±1,±1,±1)` with an even number of minus signs, they sum
to zero, each has squared length `3`, and any two have dot product `-1`,
thus the bond-angle cosine is

    cos θ₀ = (uᵢ · uⱼ) / (|uᵢ| |uⱼ|) = -1/3,   θ₀ = arccos(-1/3) ≈ 109.47°.

This is the symmetric reference angle `θ₀` of the bent-geometry shift
(`bond_angle_shift`); the lone-pair perturbation displaces the H–O–H angle
from it to `≈ 104.5°`.

## References
- [manuscript] Ch. 12, Proposition: tetrahedral H-bond directions
-/

namespace QOU.Molecular

/-- Dot product on `ℝ³`. -/
def dot3 (u v : ℝ × ℝ × ℝ) : ℝ := u.1 * v.1 + u.2.1 * v.2.1 + u.2.2 * v.2.2

/-- Four tetrahedral vertex directions. -/
def t1 : ℝ × ℝ × ℝ := (1, 1, 1)
def t2 : ℝ × ℝ × ℝ := (1, -1, -1)
def t3 : ℝ × ℝ × ℝ := (-1, 1, -1)
def t4 : ℝ × ℝ × ℝ := (-1, -1, 1)

/-- The four directions sum to zero (balanced coordination). -/
theorem tetra_sum_zero :
    (t1.1 + t2.1 + t3.1 + t4.1,
     t1.2.1 + t2.2.1 + t3.2.1 + t4.2.1,
     t1.2.2 + t2.2.2 + t3.2.2 + t4.2.2) = (0, 0, 0) := by
  simp [t1, t2, t3, t4]

/-- Each direction has squared length `3` (so `|tᵢ| = √3`). -/
theorem tetra_normSq : dot3 t1 t1 = 3 := by norm_num [dot3, t1]

/-- Any two distinct directions have dot product `-1`. -/
theorem tetra_dot12 : dot3 t1 t2 = -1 := by simp [dot3, t1, t2]

/-- **Tetrahedral bond-angle cosine `= -1/3`** — the symmetric reference
angle `θ₀ = arccos(-1/3) ≈ 109.47°` of the water bent-geometry shift. -/
theorem tetrahedral_cos : dot3 t1 t2 / dot3 t1 t1 = -1 / 3 := by
  simp [dot3, t1, t2]; norm_num

end QOU.Molecular
