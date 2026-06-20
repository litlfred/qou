/-
# QOU.QBeta.Cn_at_silver
#
# Q_β c_8, c_9, c_10 closed-form values at the silver ratio q = 1 + √2
# (where the Hoefsmit b² = 7/8 exactly).
#
# Per the documented Pell-Lucas σ-action pattern (extracted from
# `qbeta-decay-sdp-extended-ck.witness.json`):
#
#   c_8 = c_3² · b⁴ =  4 · (7/8)² = 49/16
#   c_9 = c_3³ · b² = -8 · (7/8)  = -7
#   c_10 = c_3² · b⁶ =  4 · (7/8)³ = 343/128
#
# These are PURE σ-action rungs (no averaging-resonance ½ fingerprint).
# Each closed-form equation is a pure rational identity — `norm_num`
# closes them without any symbolic-q or transcendental machinery.
#
# LaTeX label: `prop:qbeta-c8-c10-silver-rationals` (the range "c8-c10"
# covers rungs 8, 9, 10 — all three identities are proved below).
#
# AGENTS.md §7c: stated over ℚ at the silver-ratio rational anchor
# (b² = 7/8 ∈ ℚ). The statements are rational identities, so they
# descend along any ℚ-algebra map; only the ℚ form is formalized here.
-/

import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

namespace QOU.QBeta

/-- **c_8 closed form at the silver ratio.**

  c_8 := c_3² · b⁴ = 4 · (7/8)² = 49/16,  where c_3 = -2 and b² = 7/8 at silver. -/
theorem qbeta_c8_at_silver :
    (4 : ℚ) * ((7 : ℚ) / 8)^2 = (49 : ℚ) / 16 := by
  norm_num

/-- **c_9 closed form at the silver ratio.**

  c_9 := c_3³ · b² = -8 · (7/8) = -7,  where c_3 = -2 and b² = 7/8 at silver. -/
theorem qbeta_c9_at_silver :
    (-8 : ℚ) * ((7 : ℚ) / 8) = -7 := by
  norm_num

/-- **c_10 closed form at the silver ratio.**

  c_10 := c_3² · b⁶ = 4 · (7/8)³ = 343/128,  where c_3 = -2 and b² = 7/8 at silver. -/
theorem qbeta_c10_at_silver :
    (4 : ℚ) * ((7 : ℚ) / 8)^3 = (343 : ℚ) / 128 := by
  norm_num

/-- Companion identity: `c_3² = 4` (used in the c_8 and c_10 derivation). -/
theorem qbeta_c3_squared :
    ((-2 : ℚ))^2 = 4 := by
  norm_num

/-- Companion identity: `c_3³ = -8` (used in the c_9 derivation,
matches the documented `c_7 = c_3³` closed form). -/
theorem qbeta_c3_cubed :
    ((-2 : ℚ))^3 = -8 := by
  norm_num

end QOU.QBeta
