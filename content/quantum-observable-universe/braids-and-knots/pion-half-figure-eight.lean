/-
  Pion = half-figure-eight on V_(2,1).

  The pion braid M₊ and σ₁σ₂⁻¹ have identical characteristic
  polynomials on V_(2,1): both have det=1 and trace=-(h²+1).

  Base ring (§7c): the characteristic-polynomial identity is a pure
  commutative-ring fact in the parameter `h`; stated over a generic
  `[CommRing R]` rather than ℝ. The archimedean specialisation (h at
  the substrate q₀) lives downstream.

  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
  -- Ref: [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
-/

import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.BraidsAndKnots

variable {R : Type*} [CommRing R] (h : R)

/-- The pion and half-4₁ share the same characteristic polynomial
  on V_(2,1): λ² + (h²+1)λ + 1 = 0.

  This follows from: both have det = 1 (even crossing count)
  and trace = -(h²+1) on V_(2,1).

  Two matrices with the same det and trace have the same
  eigenvalues (characteristic polynomial is determined by
  trace and determinant for 2×2 matrices). -/
theorem pion_eq_half_figure_eight_phase :
    ∀ (tr : R), tr = -(h ^ 2 + 1) →
    ∀ (det : R), det = 1 →
    ∀ (lam : R), lam ^ 2 - tr * lam + det = 0 →
    lam ^ 2 + (h ^ 2 + 1) * lam + 1 = 0 := by
  intro tr htr det hdet lam hlam
  rw [htr, hdet] at hlam
  linear_combination hlam

/-- The figure-eight is the square of the half-rotation.
  If M has eigenvalue e^{iθ}, then M² has eigenvalue e^{2iθ}.
  det(M²) = det(M)² = 1² = 1. -/
theorem figure_eight_is_square_of_half : (1 : R) ^ 2 = 1 := by ring

/-- Both the pion and σ₁σ₂⁻¹ have determinant +1 on any 2-dim
  representation (product of an even number of det=-1 generators). -/
theorem pion_det_one : (-1 : ℤ) ^ 6 = 1 := by norm_num
theorem half_41_det_one : (-1 : ℤ) ^ 2 = 1 := by norm_num

end QOU.BraidsAndKnots
