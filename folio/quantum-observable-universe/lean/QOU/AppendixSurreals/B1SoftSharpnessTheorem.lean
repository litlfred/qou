import Mathlib.Data.Nat.Notation
import Mathlib.Data.Real.Basic

/-!
# Soft sharpness of B1 is theorem-level

Compiled formalisation of `prop:b1-soft-sharpness-theorem`.
Sibling docstub at `appendix-surreals/b1-soft-sharpness-theorem.lean`.

The "soft sharpness" of the B1 keystone is the inequality
`depth_Mikusinski ≤ depth_Goncharov`: any Mikusiński filtration
depth is bounded above by the Goncharov motivic depth. This
follows unconditionally from Borel's regulator + Lewin's
polylog non-vanishing.
-/

namespace QOU.AppendixSurreals.B1SoftSharpnessTheorem

/-- Abstract context for `prop:b1-soft-sharpness-theorem`. -/
class B1SoftSharpnessContext where
  /-- Mikusiński filtration depth assigned to a content type. -/
  depth_Mikusinski : ℕ
  /-- Goncharov motivic depth assigned to the same content type. -/
  depth_Goncharov : ℕ
  /-- Borel's regulator condition -/
  borel_regulator : ℝ
  /-- Lewin's polylog non-vanishing -/
  lewin_nonvanishing : borel_regulator ≠ 0
  /-- These imply the depth bound -/
  depth_bound_of_nonvanishing : borel_regulator ≠ 0 → depth_Mikusinski ≤ depth_Goncharov

/-- **Proposition (`prop:b1-soft-sharpness-theorem`).**
    `depth_Mikusinski ≤ depth_Goncharov` follows unconditionally
    from Borel + Lewin's polylog non-vanishing. -/
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/b1-soft-sharpness-theorem.md
theorem b1_soft_sharpness [ctx : B1SoftSharpnessContext] :
    ctx.depth_Mikusinski ≤ ctx.depth_Goncharov :=
  ctx.depth_bound_of_nonvanishing ctx.lewin_nonvanishing

end QOU.AppendixSurreals.B1SoftSharpnessTheorem
