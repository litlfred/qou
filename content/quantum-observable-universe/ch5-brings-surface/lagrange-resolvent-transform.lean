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
noncomputable def ζ : ℂ := Complex.exp (2 * Real.pi * Complex.I / 5)

/-- The Lagrange resolvent (DFT) of coordinates on the Bring surface. -/
noncomputable def lagrangeResolvent (x : Fin 5 → ℂ) (k : Fin 5) : ℂ :=
  (1 / Complex.ofReal (Real.sqrt 5)) * ∑ j : Fin 5, ζ ^ (k.val * j.val) * x j

/-- The cyclic permutation σ: x_j ↦ x_{j+1 mod 5}. -/
def cyclicPerm (x : Fin 5 → ℂ) : Fin 5 → ℂ :=
  fun j => x ⟨(j.val + 1) % 5, Nat.mod_lt _ (by omega)⟩

theorem lagrange_resolvent_transform
    (x : Fin 5 → ℂ)
    (h_sum : ∑ i, x i = 0)
    (h_sq  : ∑ i, (x i)^2 = 0)
    (h_cb  : ∑ i, (x i)^3 = 0) :
    -- (1) w_0 = 0 (from h_sum)
    lagrangeResolvent x ⟨0, by omega⟩ = 0 ∧
    -- (2) The cyclic permutation acts diagonally: σ(w_k) = ζ^{-k} w_k
    (∀ k : Fin 5, lagrangeResolvent (cyclicPerm x) k = ζ⁻¹ ^ k.val * lagrangeResolvent x k) := by
  -- Ref: [manuscript] Ch. 6, §1
  -- Ref: [bring1786] https://doi.org/10.1007/BF02386200
  sorry

end QOU.BringsSurface
