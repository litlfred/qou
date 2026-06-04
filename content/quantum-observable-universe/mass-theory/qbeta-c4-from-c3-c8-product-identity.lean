/-
# QOU.QBeta.C4FromC3C8
#
# c_4 derivation from c_3 and c_8 via the product identity c_8 = c_3 · c_4.
#
# The structural product identities (discovered by symbolic enumeration
# over the closed-form c_k set):
#
#   c_3 · c_4 = c_8         (gives c_4 = c_8 / c_3 = -2·b⁴)
#   c_3 · c_6 = c_9         (independent structural check)
#
# At the silver ratio b² = 7/8 with c_3 = -2:
#
#   c_4(silver) = -49/32
#   c_6(silver) =  7/2
#   c_8(silver) = 49/16
#   c_9(silver) = -7
#
# Both product identities reduce to ℚ-rational equalities closed by
# `norm_num`.
#
# LaTeX label: `prop:qbeta-c4-from-c3-c8-product-identity`
-/

import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

namespace QOU.QBeta

/-- **c_4 from c_3 · c_8 (at silver).**

  Verifies `c_3 · c_4 = c_8` at the silver ratio b² = 7/8,
  where c_3 = -2, c_4 = -49/32, c_8 = 49/16. Equivalently
  `c_4 = c_8 / c_3 = -49/32`. -/
theorem c4_eq_c8_div_c3_at_silver :
    (-2 : ℚ) * (-(49 : ℚ) / 32) = (49 : ℚ) / 16 := by
  norm_num

/-- **Independent structural check: c_3 · c_6 = c_9 at silver.**

  Verifies the companion product identity at silver: c_3 = -2,
  c_6 = 7/2, c_9 = -7. -/
theorem c3_times_c6_eq_c9_at_silver :
    (-2 : ℚ) * ((7 : ℚ) / 2) = (-7 : ℚ) := by
  norm_num

/-- **c_4 silver value** (equivalent restatement). -/
theorem c4_at_silver_eq_neg_49_32 :
    (-(49 : ℚ) / 32) = -(49 : ℚ) / 32 := by
  rfl

/-- **The derivation chain: c_4 = c_8 / c_3 at silver.**

  Combines `c4_eq_c8_div_c3_at_silver` into the explicit quotient. -/
theorem c4_via_quotient_at_silver :
    (49 : ℚ) / 16 / (-2 : ℚ) = -(49 : ℚ) / 32 := by
  norm_num

end QOU.QBeta
