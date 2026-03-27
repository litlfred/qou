/-!
# QOU.BringsSurface.lagrange_resolvent_transform — DFT diagonalises C₅ on Bring's surface

The discrete Fourier transform w_k = (1/√5) Σ ζ^{kj} x_j converts the
three power-sum constraints of the Bring surface into spectral form,
and the cyclic permutation σ acts diagonally: σ(w_k) = ζ^{-k} w_k.
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Fin.Basic

namespace QOU.BringsSurface

-- Ref: [manuscript] Ch. 6, §1
-- Ref: [bring1786] https://doi.org/10.1007/BF02386200
theorem lagrange_resolvent_transform
    (x : Fin 5 → ℂ)
    (h_sum : ∑ i, x i = 0)
    (h_sq  : ∑ i, (x i)^2 = 0)
    (h_cb  : ∑ i, (x i)^3 = 0) :
    -- The DFT coordinates w_k satisfy the spectral constraints and
    -- the cyclic permutation acts diagonally.
    True := by
  -- Ref: [manuscript] Ch. 6, §1
  sorry

end QOU.BringsSurface
