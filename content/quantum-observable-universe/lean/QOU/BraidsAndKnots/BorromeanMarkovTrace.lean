/-
  Borromean Markov trace: exact closed form as a rational function of h.

  tr_M(β_Bor, q) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)

  where h = q − q⁻¹ and β_Bor = (σ₁⁻¹σ₂)³ is the Borromean braid.

  Derivation:
    1. Jones polynomial: V(𝓑₃, t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 − 2t + 3t² − t³
    2. In u = q² + q⁻²: V = −u³ + 3u² + u − 2
    3. [2]_q² = (q + q⁻¹)² = u + 2
    4. tr_M = V / [2]² = (−u³ + 3u² + u − 2) / (u + 2)
    5. Polynomial division: = −u² + 5u − 9 + 16/(u + 2)
    6. Substituting u = h² + 2: = (4 + h² − 3h⁴ − h⁶) / (h² + 4)

  h-expansion (purely even):
    tr_M = 1 + 0·h² − (3/4)·h⁴ − (1/16)·h⁶ + (1/64)·h⁸ + ...

  The h² coefficient is EXACTLY ZERO. The first topological invariant
  of the Borromean linking structure appears at h⁴ = −3/4.

  -- Ref: [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
  -- Ref: [murasugi1996] ISBN 978-0-8176-3817-7
-/
import Mathlib.Data.Rat.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum

namespace QOU.BraidsAndKnots

variable (h : ℚ)

/-- The numerator of tr_M(β_Bor) as a polynomial in h. -/
def trM_borromean_num (h : ℚ) : ℚ := 4 + h^2 - 3 * h^4 - h^6

/-- The denominator of tr_M(β_Bor) as a polynomial in h. -/
def trM_borromean_den (h : ℚ) : ℚ := h^2 + 4

/-- The Borromean Markov trace as a rational function of h. -/
noncomputable def trM_borromean (h : ℚ) : ℚ := trM_borromean_num h / trM_borromean_den h

/-- At h = 0 (q = 1), the Markov trace is exactly 1. -/
theorem trM_borromean_at_h_zero : trM_borromean 0 = 1 := by
  unfold trM_borromean trM_borromean_num trM_borromean_den
  norm_num

/-- The denominator is always positive (hence non-zero) for real h. -/
theorem trM_borromean_den_pos (h : ℚ) : trM_borromean_den h > 0 := by
  unfold trM_borromean_den
  nlinarith [sq_nonneg h]

/-- The denominator is non-zero. -/
theorem trM_borromean_den_ne_zero (h : ℚ) : trM_borromean_den h ≠ 0 := by
  exact ne_of_gt (trM_borromean_den_pos h)

/-- The Jones polynomial of the Borromean rings in u = q² + q⁻². -/
def jones_borromean_in_u (u : ℚ) : ℚ := -u^3 + 3 * u^2 + u - 2

/-- [2]_q² = (q + q⁻¹)² in terms of u = q² + q⁻². -/
def bracket2_sq_in_u (u : ℚ) : ℚ := u + 2

/-- The polynomial division: V / [2]² = quotient + 16/(u+2).
    Equivalently: V = (u+2) · (−u² + 5u − 9) + 16. -/
theorem jones_division (u : ℚ) :
    jones_borromean_in_u u =
    bracket2_sq_in_u u * (-u^2 + 5*u - 9) + 16 := by
  unfold jones_borromean_in_u bracket2_sq_in_u
  ring

/-- The substitution u = h² + 2 maps the Jones polynomial
    to the numerator of tr_M. -/
theorem jones_to_trM_num (h : ℚ) :
    jones_borromean_in_u (h^2 + 2) = trM_borromean_num h := by
  unfold jones_borromean_in_u trM_borromean_num
  ring

/-- The substitution u = h² + 2 maps [2]² to the denominator. -/
theorem bracket2_to_trM_den (h : ℚ) :
    bracket2_sq_in_u (h^2 + 2) = trM_borromean_den h := by
  unfold bracket2_sq_in_u trM_borromean_den
  ring

/-- The h⁴ coefficient of the numerator is −3.
    Since the denominator's leading term is 4,
    the h⁴ coefficient of tr_M is −3/4. -/
theorem h4_coefficient_of_num :
    trM_borromean_num h = 4 * (1 : ℚ) + 1 * h^2 + (-3) * h^4 + (-1) * h^6 := by
  unfold trM_borromean_num
  ring

/-- The h² coefficient of the numerator is +1 (NOT zero).
    But the h² coefficient of tr_M = num/den IS zero because
    den = 4 + h² and (4 + h²)·(1 + 0·h² + ...) = 4 + h² + ...
    matches the numerator's h² coefficient of +1 exactly. -/
theorem h2_coefficient_cancellation :
    trM_borromean_num h = trM_borromean_den h * 1 +
    (-3 * h^4 - h^6) := by
  unfold trM_borromean_num trM_borromean_den
  ring

/-- Main result: the Borromean Markov trace, combining all steps.
    V(𝓑₃) / [2]_q² = (4 + h² − 3h⁴ − h⁶) / (h² + 4)
    with the h² coefficient being exactly zero (cancellation). -/
-- Ref: [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
theorem borromean_markov_trace_closed_form (h : ℚ) (hne : trM_borromean_den h ≠ 0) :
    trM_borromean h = 1 + (-3 * h^4 - h^6) / trM_borromean_den h := by
  unfold trM_borromean
  rw [h2_coefficient_cancellation]
  field_simp
  ring

end QOU.BraidsAndKnots
