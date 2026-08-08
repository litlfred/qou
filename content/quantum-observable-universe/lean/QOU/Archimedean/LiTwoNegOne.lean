import QOU.Archimedean.ComplexDilogBridge
import QOU.MathlibExt.AlternatingZetaTwo

/-!
# `Li₂(−1) = −π²/12`, real and complex

The corollary of `hasSum_alternating_zeta_two` that `qou-rstq` item 4 needs: the
Landen base value, in both the corpus's real `LiTwo` and the complex `cLiTwo`.

Route 33 G4 identified this as the single missing input for the Landen leg —
its analytic core (`hasDerivAt_landenCombo`) being already proved. With it, the
remaining obstacle in item 4 is the **inversion** leg for `x > 1`, which lies on
`cLiTwoExt`'s cut and needs boundary values rather than a constant of
integration.

**The 5₂ sum rule remains verified to 80 dps, unproved.**
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

end QOU.Archimedean
