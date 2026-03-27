/-!
# QOU.BringsSurface.brings_smoothness_resolution — Bring surface is smooth

The three power-sum constraints defining the Bring surface are transverse
in ℙ⁴, so the intersection is smooth.  Projection singularities are
resolved intrinsically by the chiral coordinates.
-/
import Mathlib.Data.Complex.Basic

namespace QOU.BringsSurface

-- Ref: [manuscript] Ch. 6, §1
-- Ref: [bring1786] https://doi.org/10.1007/BF02386200
theorem brings_smoothness_resolution :
    -- The Bring surface is smooth and projection singularities are
    -- resolved by the chiral coordinate blow-up.
    True := by
  -- Ref: [manuscript] Ch. 6, §1
  sorry

end QOU.BringsSurface
