import QOU.Archimedean.ComplexDilogBridge
import QOU.MathlibExt.AlternatingZetaTwo
import QOU.MathlibExt.ComplexDilogarithmBoundary

/-!
# `Li₂(−1) = −π²/12`, real and complex

The corollary of `hasSum_alternating_zeta_two` that `qou-rstq` item 4 needs: the
Landen base value, in both the corpus's real `LiTwo` and the complex `cLiTwo`.

Route 33 G4 identified this as the single missing input for the Landen leg —
its analytic core (`hasDerivAt_landenCombo`) being already proved.

`cLiTwoExt_neg_one` is the form the Landen argument actually consumes, and
getting it needed real infrastructure: `cLiTwoExt_eq_cLiTwo` holds on the
**open** disc, while `−1` sits on the boundary. `ComplexDilogarithmBoundary`
closes that one-point gap for **every** boundary point off the cut.

With it, the remaining obstacle in item 4 is the **inversion** leg for `x > 1`,
which lies *on* `cLiTwoExt`'s cut — where no continuity argument in that file
applies — and needs boundary values from off the cut.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.Archimedean

open Real Complex QOU.MathlibExt QOU.QPochhammer

/-- **`LiTwo(−1) = −π²/12`.** The corpus's series at `x = −1` is exactly the
alternating `ζ(2)`, termwise. -/
theorem LiTwo_neg_one : LiTwo (-1) = -(π ^ 2 / 12) := by
  unfold LiTwo
  exact hasSum_alternating_zeta_two.tsum_eq

/-- The same for the complex series, through `cLiTwo_ofReal`. -/
theorem cLiTwo_neg_one : cLiTwo (-1) = -((π : ℂ) ^ 2 / 12) := by
  have h : ((-1 : ℝ) : ℂ) = (-1 : ℂ) := by norm_num
  have := cLiTwo_ofReal (-1)
  rw [h, LiTwo_neg_one] at this
  rw [this]
  push_cast
  ring

/-- **The continuation's value at `−1`**, which is what the Landen argument
consumes. `−1` is on the boundary of the disc, so this needs
`cLiTwoExt_eq_cLiTwo_of_norm_le_one`, not the open-disc agreement. -/
theorem cLiTwoExt_neg_one : cLiTwoExt (-1) = -((π : ℂ) ^ 2 / 12) := by
  have hnc : (-1 : ℂ) ∈ notCut := Or.inr (by norm_num)
  rw [cLiTwoExt_eq_cLiTwo_of_norm_le_one (by norm_num) hnc]
  exact cLiTwo_neg_one

/-- **Cleared-denominator real Landen base identity:** `12 · Li₂(−1) + π² = 0`. -/
theorem twelve_mul_LiTwo_neg_one : 12 * LiTwo (-1) + π ^ 2 = 0 := by
  rw [LiTwo_neg_one]
  ring

/-- **Cleared-denominator complex continuation Landen base identity:**
    `12 · cLiTwoExt(−1) + π² = 0`. -/
theorem twelve_mul_cLiTwoExt_neg_one : 12 * cLiTwoExt (-1) + (π : ℂ) ^ 2 = 0 := by
  rw [cLiTwoExt_neg_one]
  ring

end QOU.Archimedean
