import QOU.Basic

namespace QOU.BraidKnot.AlphaShiftTorus

def alphaShift (p k : ℕ) : ℕ := k * (p - 1)

theorem alpha_shift_torus_knot (p k : ℕ) :
    alphaShift p k = k * (p - 1) := by
  -- Ref: [manuscript] prop:alpha-shift-torus-knot
  rfl

end QOU.BraidKnot.AlphaShiftTorus
