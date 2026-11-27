/-
Copyright (c) 2026. All rights reserved.
Released under CC BY 4.0 license.

# μ–p residual: open-worldline projector insertions on `4₁`

Bean `qou-6gf9`. Companion to `MuPProjectorInsertionWOrder`, which tested the
photon projector `e_i = (q − σ_i)/[2]_q` inserted into `4₁ = (σ₁σ₂⁻¹)²` with the
closed-knot normalisation `1/tr_M(4₁)`, and found it does not force a `w²`
coefficient (`w = q + q⁻¹ − 2`).

Here the worldline is left open: the `(1,1)`-tangle normalisation divides by the
unknot (`tr_M(1) = y₃ + 2·y₂₁ = 1`) instead of by the knot. The observables are
the un-normalised traces `tr_M(X·4₁)`.

Results, all exact and over a generic field unless stated:

* `open_closed_ratio`: the closed correlator is the open one divided by the open
  knot trace. So the closed class is the open class divided by `tr_M(4₁)`.
* `openPair_eq`, `trM41_eq_s`: in `s = [2]_q`,
  `⟨e₁+e₂⟩_open = (s⁴−6s²+7)/s²` and `tr_M(4₁) = (s⁴−5s²+5)/s²`. The only pole is
  `s = 0`, i.e. `w = −2`. The open class therefore has radius of convergence 2 in
  `w`, against `|w*| = 2 − 2cos(π/10) ≈ 0.098` for the closed class. The
  closed class's 10×-per-order growth comes from the normalisation alone.
* Taylor data `(O(1), O(w), O(w²))` as exact remainder identities:
  `tr_M(4₁)`: `(1/4, 11/4, 31/16)`; pair: `(−1/4, 9/4, 37/16)`;
  doubles `D`: `(−11/4, 24, 99/4)`; connected `C`: `(−27/8, 141/4, −229/16)`.
  The `D` and `C` numerators in `w` come from the probe; the pair and knot trace
  are derived here from the matrices.
* `open_w2_not_forced`: `x₀·1 + x₁·tr_M(4₁) + x₂·pair` with
  `(x₀,x₁,x₂) = (5c/8, −9c/8, 11c/8)` has vanishing `O(1)` and `O(w)` and
  `O(w²) = c` for every `c`. So the `w²` coefficient is not forced here either.

No empirical input enters any statement here.
-/
import QOU.BraidsAndKnots.MuPProjectorInsertionWOrder

namespace QOU.BraidsAndKnots.MuPOpenWorldlineWOrder

open Matrix QOU.BraidsAndKnots.MuPProjectorInsertionWOrder

variable {K : Type*} [Field K]

/-- The Markov trace of the identity is `1`: the open strand is normalised by the unknot. -/
theorem trM_one (q : K) (h2 : q ^ 2 + 1 ≠ 0) : y3 q + 2 * y21 q = 1 := by
  unfold y3 y21; field_simp; ring

/-- Open-worldline bar-symmetric single insertion `tr_M((e₁ + e₂)·4₁)`; the
projectors kill the trivial representation, so only `y₂₁` contributes. -/
def openPair (q : K) : K := y21 q * (trace (E1 q * word41 q) + trace (E2 q * word41 q))

/-- The closed correlator is the open one divided by the open knot trace. -/
theorem open_closed_ratio (q : K) : pairCorr q = openPair q / trM41 q := rfl

theorem openPair_eq_q (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    openPair q = (q ^ 10 - q ^ 8 - q ^ 6 - q ^ 4 - q ^ 2 + 1) / (q ^ 2 * (q ^ 2 + 1) ^ 3) := by
  rw [openPair, trace_E1_word41 q hq h2, trace_E2_word41 q hq h2, y21]
  field_simp
  ring

theorem s_ne_zero (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : q + q⁻¹ ≠ 0 := by
  intro h; apply h2; field_simp at h; linear_combination h

/-- Open pair in `s = [2]_q`: its only pole is `s = 0`. -/
theorem openPair_eq (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    openPair q = ((q + q⁻¹) ^ 4 - 6 * (q + q⁻¹) ^ 2 + 7) / (q + q⁻¹) ^ 2 := by
  have hs := s_ne_zero q hq h2
  rw [openPair_eq_q q hq h2, div_eq_div_iff
    (mul_ne_zero (pow_ne_zero 2 hq) (pow_ne_zero 3 h2)) (pow_ne_zero 2 hs)]
  field_simp
  ring

/-- The knot trace itself in `s`: `tr_M(4₁) = (s⁴ − 5s² + 5)/s²`. -/
theorem trM41_eq_s (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    trM41 q = ((q + q⁻¹) ^ 4 - 5 * (q + q⁻¹) ^ 2 + 5) / (q + q⁻¹) ^ 2 := by
  have hs := s_ne_zero q hq h2
  rw [trM41_eq q hq h2, div_eq_div_iff
    (mul_ne_zero (pow_ne_zero 2 hq) (pow_ne_zero 3 h2)) (pow_ne_zero 2 hs)]
  field_simp
  ring

/-- At `q = 1` the open pair is `−1/4` and the knot trace `1/4`: both leading
terms are nonzero. -/
theorem open_at_one : openPair (1 : ℚ) = -1 / 4 ∧ trM41 (1 : ℚ) = 1 / 4 := by
  refine ⟨?_, ?_⟩
  · rw [openPair_eq (1 : ℚ) one_ne_zero (by norm_num)]; norm_num
  · rw [trM41_eq_s (1 : ℚ) one_ne_zero (by norm_num)]; norm_num

/-! ## Taylor data in `w = s − 2` (denominators are powers of `w + 2`) -/

theorem knot_num_eq (s : K) :
    (s - 2) ^ 4 + 8 * (s - 2) ^ 3 + 19 * (s - 2) ^ 2 + 12 * (s - 2) + 1 =
      s ^ 4 - 5 * s ^ 2 + 5 := by ring

theorem pair_num_eq' (s : K) :
    (s - 2) ^ 4 + 8 * (s - 2) ^ 3 + 18 * (s - 2) ^ 2 + 8 * (s - 2) - 1 =
      s ^ 4 - 6 * s ^ 2 + 7 := by ring

/-- Knot trace: `(1/4, 11/4, 31/16)`. -/
theorem knot_taylor (w : ℚ) :
    (w ^ 4 + 8 * w ^ 3 + 19 * w ^ 2 + 12 * w + 1) -
      (w + 2) ^ 2 * (1 / 4 + 11 / 4 * w + 31 / 16 * w ^ 2) =
      w ^ 3 * (-15 / 16 * w - 5 / 2) := by ring

/-- Open pair: `(−1/4, 9/4, 37/16)`. -/
theorem open_pair_taylor (w : ℚ) :
    (w ^ 4 + 8 * w ^ 3 + 18 * w ^ 2 + 8 * w - 1) -
      (w + 2) ^ 2 * (-1 / 4 + 9 / 4 * w + 37 / 16 * w ^ 2) =
      w ^ 3 * (-21 / 16 * w - 7 / 2) := by ring

/-- Open doubles (w-form from the probe): `(−11/4, 24, 99/4)`. -/
theorem open_doubles_taylor (w : ℚ) :
    2 * (5 * w ^ 6 + 60 * w ^ 5 + 272 * w ^ 4 + 576 * w ^ 3 + 549 * w ^ 2 + 148 * w - 22) -
      (w + 2) ^ 4 * (-11 / 4 + 24 * w + 99 / 4 * w ^ 2) =
      w ^ 3 * (-59 / 4 * w ^ 3 - 102 * w ^ 2 - 957 / 4 * w - 194) := by ring

/-- Open connected doubles (w-form from the probe): `(−27/8, 141/4, −229/16)`. -/
theorem open_connected_taylor (w : ℚ) :
    -2 * (w + 1) * (w + 3) * (5 * w ^ 6 + 60 * w ^ 5 + 240 * w ^ 4 + 320 * w ^ 3 -
        22 * w ^ 2 - 88 * w + 9) - (w + 2) ^ 4 * (-27 / 8 + 141 / 4 * w - 229 / 16 * w ^ 2) =
      w ^ 3 * (-10 * w ^ 5 - 160 * w ^ 4 - 15611 / 16 * w ^ 3 - 11363 / 4 * w ^ 2 -
        31129 / 8 * w - 1929) := by ring

/-- **Non-forcing, open class.** With Taylor vectors `1 = (1,0,0)`,
`tr_M(4₁) = (1/4, 11/4, 31/16)`, pair `= (−1/4, 9/4, 37/16)`, the combination
`(5c/8, −9c/8, 11c/8)` kills `O(1)` and `O(w)` and has `O(w²) = c`, for every `c`. -/
theorem open_w2_not_forced (c : ℚ) :
    ∃ x0 x1 x2 : ℚ,
      x0 * 1 + x1 * (1 / 4) + x2 * (-1 / 4) = 0 ∧
      x1 * (11 / 4) + x2 * (9 / 4) = 0 ∧
      x1 * (31 / 16) + x2 * (37 / 16) = c := by
  refine ⟨5 * c / 8, -9 * c / 8, 11 * c / 8, ?_, ?_, ?_⟩ <;> ring

/-- No member of the open class has a vanishing leading term:
`1/4, −1/4, −11/4, −27/8`. -/
theorem open_leading_terms_nonzero :
    (1 / 4 : ℚ) ≠ 0 ∧ (-1 / 4 : ℚ) ≠ 0 ∧ (-11 / 4 : ℚ) ≠ 0 ∧ (-27 / 8 : ℚ) ≠ 0 := by norm_num

end QOU.BraidsAndKnots.MuPOpenWorldlineWOrder
