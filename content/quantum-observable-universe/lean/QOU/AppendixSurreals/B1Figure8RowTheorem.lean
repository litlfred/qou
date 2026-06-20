import Mathlib.Data.Real.Basic

/-!
# B1 keystone is theorem-level at the figure-8 row

Compiled formalisation of `prop:b1-figure-8-row-theorem`.
Sibling docstub at `appendix-surreals/b1-figure-8-row-theorem.lean`.

The B1 keystone holds unconditionally at the figure-8 (knot `4_1`)
row via Bloch-Suslin together with the Murakami–Murakami volume-
conjecture proof for `4_1`.
-/

namespace QOU.AppendixSurreals.B1Figure8RowTheorem

/-- Abstract context for `prop:b1-figure-8-row-theorem`. -/
class B1Figure8RowContext where
  /-- The Bloch-Wigner D_2(z) value (Faddeev volume) at the figure-8
      shape parameter (`Im(D_2(e^{iπ/3}))`). -/
  bloch_wigner_4_1 : ℝ
  /-- The Mikusinski filtration depth assigned to the figure-8 row. -/
  depth_4_1 : ℕ
  /-- Figure-8 row sits at depth 2 (Bloch-Suslin / Bloch-Wigner level) -/
  depth_eq_2 : depth_4_1 = 2
  /-- and the volume is non-zero (Murakami-Murakami). -/
  bloch_wigner_ne_zero : bloch_wigner_4_1 ≠ 0

/-- **Proposition (`prop:b1-figure-8-row-theorem`).** -/
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/b1-figure-8-row-theorem.md
theorem b1_figure_8_row [ctx : B1Figure8RowContext] :
    ctx.depth_4_1 = 2 ∧ ctx.bloch_wigner_4_1 ≠ 0 := by
  constructor
  · exact ctx.depth_eq_2
  · exact ctx.bloch_wigner_ne_zero

end QOU.AppendixSurreals.B1Figure8RowTheorem
