import Mathlib.Data.Complex.Basic
import Mathlib.Tactic
import QOU.QBeta.HopfCubicOddCarrier

/-!
# QOU.QBeta.Zeta4DescentCarrier

The bridge between the **KC17 bar-parity descent dichotomy**
(`FMapDirectCyclotomic.lean`, merged PR #3556) and the **bar-odd Hopf-cubic
carrier** (`HopfCubicOddCarrier.lean`, KC20).

The dichotomy `uside_parity_descent_iff_zeta4` shows the u-side cyclotomic
re-basing transports the fibre bar-parity to the `c_k` rungs iff `q² = −1`, and
`uside_parity_never_descends_real` shows this fails at every real substrate. This
file identifies that descent point with the **fibre root of unity** the odd
carrier lives on:

* **`descent_iff_order_four`** — over `ℂ`, `q² = −1 ↔ (q⁴ = 1 ∧ q² ≠ 1)`: the
  descent condition is *exactly* "q is a primitive 4th root of unity" (order-4
  root, i.e. `q = ζ₄ = ±i`). So the parity descends precisely at `ζ₄` — the
  fibre point, off the real substrate axis.

* **`carrier_var_at_descent`** — at the descent point the bar-even loop-trace
  variable `y = q² + q⁻²` (the argument of the Hopf-cubic carrier `cTotal`)
  equals `−2`, the antipode of its `q = 1` value `y = +2` (`cHopf_at_two`).

* **`cTotal_at_descent_image`** — the bar-odd carrier `cTotal` (KC20) is
  **non-degenerate** at that image (`cTotal(−2) = −32 ≠ 0`): the odd channel is
  genuinely present at `ζ₄`, consistent with `ζ₄` being where the fibre parity
  and the odd Hopf-cubic carrier meet.

Net structural picture: the odd (bar-odd, Q_β / S) channel's fibre carrier
connects to the `c_k` parity only at `q = ζ₄` (this file) and never on the real
substrate axis (`uside_parity_never_descends_real`) — so at `q₀` the odd channel
is irreducibly *archimedean*. Derives no `c_k` value; wires nothing; changes no
tier (flip-flop guard §8). All sorry-free, lean-direct verified.
-/

namespace QOU.QBeta

open QOU.QBeta.HopfCubic

/-- **The descent point is a primitive 4th root of unity (`ζ₄`).** Over `ℂ`,
    `q² = −1 ↔ (q⁴ = 1 ∧ q² ≠ 1)` — the right-hand side is exactly the
    order-4-root condition. Combined with `uside_parity_descent_iff_zeta4`
    (`FMapDirectCyclotomic`), the fibre bar-parity descends to the `c_k` rungs
    precisely when `q = ζ₄`. -/
theorem descent_iff_order_four (q : ℂ) : q ^ 2 = -1 ↔ (q ^ 4 = 1 ∧ q ^ 2 ≠ 1) := by
  constructor
  · intro h
    refine ⟨?_, ?_⟩
    · rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, h]; norm_num
    · rw [h]; norm_num
  · rintro ⟨h4, h2⟩
    have hfac : (q ^ 2 - 1) * (q ^ 2 + 1) = 0 := by
      have hz : q ^ 4 - 1 = 0 := by rw [h4]; ring
      linear_combination hz
    rcases mul_eq_zero.mp hfac with h | h
    · exact absurd (sub_eq_zero.mp h) h2
    · linear_combination h

/-- **The carrier variable at the descent point is `y = −2`.** The bar-even
    loop-trace variable `y = q² + q⁻²` (argument of the Hopf-cubic carrier) at
    `q² = −1` equals `−2` — the antipode of the trivial `q = 1` value `y = +2`. -/
theorem carrier_var_at_descent (q : ℂ) (h : q ^ 2 = -1) :
    q ^ 2 + (q ^ 2)⁻¹ = -2 := by
  rw [h]; norm_num

/-- **The bar-odd carrier is non-degenerate at the descent image.** The total
    bar-odd Hopf-cubic carrier `cTotal` (KC20) evaluated at the descent-point
    image `y = −2` is `−32 ≠ 0`: the odd channel is present at `ζ₄`. -/
theorem cTotal_at_descent_image : cTotal (-2 : ℂ) = -32 := by
  simp only [cTotal]; norm_num

/-- The carrier value at the descent image is nonzero (non-degenerate odd
    channel at `ζ₄`). -/
theorem cTotal_at_descent_image_ne_zero : cTotal (-2 : ℂ) ≠ 0 := by
  rw [cTotal_at_descent_image]; norm_num

end QOU.QBeta
