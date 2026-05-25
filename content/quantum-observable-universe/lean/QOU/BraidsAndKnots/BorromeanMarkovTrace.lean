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

/-- **Structural h² = 0 and h⁴ leading-order corollary.**
    The Borromean Markov trace minus its h=0 value (which is 1)
    factors through h⁴ — i.e. there is no h⁰, h¹, h², h³ correction:
    $$\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q) - 1
       = h^4 \cdot \frac{-3 - h^2}{h^2 + 4}.$$
    The leading h⁴ coefficient is therefore the value of the right
    factor at h = 0, which is $-3/4$.

    This makes the h² = 0 structural fact explicit (no Taylor-series
    machinery needed; it follows by algebraic division of the
    rational expression).

    Audit chain: `docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`
    (T1 closure). -/
theorem trM_minus_one_factors_through_h_to_the_fourth
    (h : ℚ) (hne : trM_borromean_den h ≠ 0) :
    trM_borromean h - 1 = h^4 * (-3 - h^2) / trM_borromean_den h := by
  rw [borromean_markov_trace_closed_form h hne]
  field_simp
  ring

/-- The leading h⁴ coefficient of (tr_M − 1) is exactly −3/4,
    obtained by evaluating the right factor at h = 0. -/
theorem h4_leading_coefficient_eq_neg_three_quarters :
    (-3 - (0 : ℚ)^2) / trM_borromean_den 0 = -3 / 4 := by
  unfold trM_borromean_den
  norm_num

/-! ### Bar-(anti-)symmetric structure of the Borromean trace

The bar-involution sends `q ↦ q^{-1}`, equivalently `h = q − q^{-1} ↦ −h`.

The Borromean closed form is purely even in `h`:
both numerator `4 + h² − 3h⁴ − h⁶` and denominator `h² + 4` involve
only even powers of `h`. Therefore `trM_borromean` is invariant under
`h ↦ −h` (bar-symmetric), and its bar-anti-symmetric companion
`Q_borromean h := (trM_borromean h − trM_borromean (−h)) / 2` vanishes
identically.

Compare PR #1153 (`sinh_bar_antisymmetric_partner.py`) for the torus
`T(2, 2m)` family: those `Q_m(h)` are non-zero (carry the Coulomb /
EM channel via `sinh((2m+1) η)`). The Borromean braid `𝓑₃` is NOT
in the torus family — it is hyperbolic (the 3-cusped Borromean rings
have Vol ≈ 7.32) — and its bar-anti-symmetric companion is structurally
zero, not merely "small at substrate".

Audit chain: PR #1153 audit `docs/audits/2026-05-24-sinh-bar-anti-
symmetric-partner-probe.md` §"Refined-framing note" cites this fact;
PR #1196 audit `docs/audits/2026-05-24-sinh-cosh-lean-integration-
audit.md` flags it as the next concrete Lean proof gap (this
section closes it).
-/

/-- The numerator polynomial `4 + h² − 3h⁴ − h⁶` is even in `h`. -/
theorem trM_borromean_num_even (h : ℚ) :
    trM_borromean_num (-h) = trM_borromean_num h := by
  unfold trM_borromean_num
  ring

/-- The denominator polynomial `h² + 4` is even in `h`. -/
theorem trM_borromean_den_even (h : ℚ) :
    trM_borromean_den (-h) = trM_borromean_den h := by
  unfold trM_borromean_den
  ring

/-- The Borromean Markov trace is invariant under the bar-involution
    `h ↦ −h` (equivalently `q ↦ q^{-1}`). -/
theorem trM_borromean_bar_invariant (h : ℚ) :
    trM_borromean (-h) = trM_borromean h := by
  unfold trM_borromean
  rw [trM_borromean_num_even, trM_borromean_den_even]

/-- The bar-anti-symmetric companion of the Borromean Markov trace:
    `Q_borromean(h) := (tr_M(h) − tr_M(−h)) / 2`.

    Defined by analogy with `Q_m` from PR #1153 for the torus family
    `T(2, 2m)`, where `Q_m(h) = (q^{2m+1} − q^{−(2m+1)}) / (2 [2]_q)`
    is the odd-h projection of the full Markov trace. -/
noncomputable def Q_borromean (h : ℚ) : ℚ :=
  (trM_borromean h - trM_borromean (-h)) / 2

/-- **The bar-anti-symmetric companion of the Borromean Markov trace
    vanishes identically.** Direct consequence of
    `trM_borromean_bar_invariant`.

    Categorical interpretation: the Borromean braid 𝓑₃ carries no
    bar-anti-symmetric (Coulomb / EM-channel) component in its
    Markov trace. This contrasts with the torus family `T(2, 2m)`,
    whose `Q_m` is non-zero and equals `sinh((2m+1) η) / (2 cosh η)`
    at substrate (PR #1153).

    Closes the `Q_borromean_eq_zero : True := trivial` placeholder
    in `QOU.BraidKnot.BarSymmetricBarAntiSymmetricIdentities` (added
    by commit `d4d640ce7`, flagged as the next concrete Lean gap by
    PR #1196's audit). -/
theorem Q_borromean_eq_zero (h : ℚ) : Q_borromean h = 0 := by
  unfold Q_borromean
  rw [trM_borromean_bar_invariant]
  ring

end QOU.BraidsAndKnots
