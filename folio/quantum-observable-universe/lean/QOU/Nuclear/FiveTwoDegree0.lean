import Mathlib.Tactic
import QOU.Nuclear.FiveTwoIndexBase

/-!
# QOU.QBeta.FiveTwoIndex — quadratic growth of the m015 summand degree, flux 0

Bean `qou-vr3q`. `12·fdeg 0 e a b ≥ a² + b² + e²`. On each of the 27 products of
tetrahedron cones (`deg2_cases`) the degree is one quadratic and the bound is
`nlinarith`. With `fdeg_neg` this also covers flux `-0`. It makes the
`(a,b)` sum of the m015 index finite at every t-degree, and confines the
summands that reach low degree to a small box.

No measured value enters. No fit.
-/

namespace QOU.QBeta.FiveTwoIndex

open QOU.QBeta.TetIndexDegree

set_option maxHeartbeats 4000000 in
theorem fdeg_quad0 (a b e : ℤ) : a ^ 2 + b ^ 2 + e ^ 2 ≤ 12 * fdeg 0 e a b := by
  unfold fdeg
  rcases deg2_cases (b - 0) (e - a) with ⟨p1, p2, d1⟩ | ⟨p1, p2, d1⟩ | ⟨p1, p2, d1⟩ <;>
  rcases deg2_cases b (2 * a - e - b) with ⟨q1, q2, d2⟩ | ⟨q1, q2, d2⟩ | ⟨q1, q2, d2⟩ <;>
  rcases deg2_cases (b + 0) (-a) with ⟨r1, r2, d3⟩ | ⟨r1, r2, d3⟩ | ⟨r1, r2, d3⟩ <;>
  rw [d1, d2, d3] <;>
  nlinarith [sq_nonneg (a + b), sq_nonneg (a - b), sq_nonneg (a + e), sq_nonneg (a - e),
    sq_nonneg (b + e), sq_nonneg (b - e), sq_nonneg (2 * a - e), sq_nonneg (a + b - e)]

end QOU.QBeta.FiveTwoIndex
