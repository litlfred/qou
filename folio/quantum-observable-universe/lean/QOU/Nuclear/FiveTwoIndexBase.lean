import Mathlib.Tactic
import QOU.Nuclear.TetIndexDegree

/-!
# QOU.QBeta.FiveTwoIndex — the t-degree of a summand of the m015 index

Bean `qou-vr3q`. The 3d index of the SnapPy triangulation m015 (the 5₂ knot
complement), in the GHRS form (Garoufalidis–Hodgson–Rubinstein–Segerman
1303.5278 §4) with SnapPy's gluing rows for m015 and half-longitude flux
(`computations/probes/half_class_3d_index.py`), reduces to a sum over `ℤ²`:

`I(m,e) = Σ_{a,b ∈ ℤ} (-1)^{b+m} t^{-b} I_Δ(b-m, e-a) I_Δ(b, 2a-e-b) I_Δ(b+m, -a)`,
`t = q^{1/2}`. (Checked against the probe for `|m| ≤ 2`, `|e| ≤ 4` through `t⁸`:
45 charge pairs, 0 mismatches.)

`fdeg m e a b` is the lowest t-degree the `(a,b)` summand can reach, from the
tetrahedron degree `deg2`. This file only defines it and records the flux
reflection `fdeg_neg`. The quadratic growth bounds are in
`FiveTwoDegree0/1/2`, one file each so that they build in parallel.

No measured value enters. No fit.

-- Ref: [garoufalidis-hodgson-rubinstein-segerman2015] GHRS 1303.5278 (§4)
-/

namespace QOU.QBeta.FiveTwoIndex

open QOU.QBeta.TetIndexDegree

/-- Lowest t-degree of the `(a,b)` summand of `I_{m015}(m,e)`. -/
def fdeg (m e a b : ℤ) : ℤ :=
  -b + deg2 (b - m) (e - a) + deg2 b (2 * a - e - b) + deg2 (b + m) (-a)

/-- Flux reflection: tetrahedra 1 and 3 swap under `m ↦ -m`, `(a,e) ↦ (a-e,-e)`. -/
theorem fdeg_neg (m e a b : ℤ) : fdeg (-m) e a b = fdeg m (-e) (a - e) b := by
  unfold fdeg
  rw [show b - -m = b + m by ring, show b + -m = b - m by ring, show -e - (a - e) = -a by ring,
    show 2 * (a - e) - -e - b = 2 * a - e - b by ring, show -(a - e) = e - a by ring]
  ring

end QOU.QBeta.FiveTwoIndex
