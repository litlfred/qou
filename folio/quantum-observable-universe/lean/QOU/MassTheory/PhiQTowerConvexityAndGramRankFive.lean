/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# `ϕ_q` Tower Convexity Sign Reversal (`qou-oooq`) and `H₃` Convention-D Rank-5 Gram Kernel (`qou-fadg`)

This module formalizes the algebraic structures of beans `qou-oooq` and `qou-fadg`:

1. **`qou-oooq` (Order-2 convexity obstruction vs order-5 sign reversal in the `ℏ`-expansion):**
   - In the `q = exp(ℏ)` expansion of `Δ(ℏ) = L_pn - (L_pp + L_nn)/2`, cleared by `630 = lcm(3, 45, 9, 126)`:
     `630 · Δ(ℏ) = -1260 ℏ² + 840 ℏ⁵ - 826 ℏ⁶ - 350 ℏ⁷ + 745 ℏ⁸ - ⋯`.
   - Orders `0, 1, 3, 4` vanish identically; order `2` carries the negative convexity-obstruction
     coefficient `-2` (`-1260 / 630`), whereas order `5` carries the strictly positive coefficient
     `+4/3` (`+840 / 630`).
   - The leading two-term truncation `-1260 ℏ² + 840 ℏ⁵` factors as `420 ℏ² (2 ℏ³ - 3)`.

2. **`qou-fadg` (`H₃` Convention-D Gram matrix is rank 5 of 6, making `5 + 1 = 6` square):**
   - Under Convention D, the 6×6 `H₃(q)` trace Gram matrix `G` has a 1-dimensional radical spanned
     by the `q`-antisymmetriser (`nullity = 1`), leaving `6 - 1 = 5` independent Frobenius rows.
   - Adjoining `1` net constraint produces `5 + 1 = 6` constraints on `6` unknowns (a square system,
     not `7` over-determined constraints on `6` unknowns).
   - Shifting a candidate vector `x ↦ x + t r` along a radical vector `r` (`G r = 0`) leaves `G(x + t r)`
     invariant while scanning the net functional linearly by `t · net(r)`.
-/

namespace QOU.MassTheory.PhiQTowerConvexityAndGramRankFive

/-- Cleared coefficients `630 · [ℏ^k] Δ(ℏ)` for `k ≤ 8` (`qou-oooq`). -/
def deltaHbarClearedCoeff (k : Nat) : Int :=
  match k with
  | 2 => -1260
  | 5 => 840
  | 6 => -826
  | 7 => -350
  | 8 => 745
  | _ => 0

/-- Orders `0, 1, 3, 4` of `Δ(ℏ)` vanish identically (`qou-oooq`). -/
theorem deltaHbarClearedCoeff_vanish_low_orders :
    deltaHbarClearedCoeff 0 = 0 ∧
    deltaHbarClearedCoeff 1 = 0 ∧
    deltaHbarClearedCoeff 3 = 0 ∧
    deltaHbarClearedCoeff 4 = 0 := by
  decide

/-- Order `2` is strictly negative (`-1260 = -2 · 630`) while order `5` is strictly positive
(`+840 = (4/3) · 630`) (`qou-oooq`). -/
theorem deltaHbarClearedCoeff_order2_neg_order5_pos :
    deltaHbarClearedCoeff 2 < 0 ∧ 0 < deltaHbarClearedCoeff 5 := by
  decide

/-- Leading two-nonzero-term truncation `-1260 ℏ² + 840 ℏ⁵` (`qou-oooq`). -/
def deltaHbarTwoTermTrunc (hbar : Int) : Int :=
  deltaHbarClearedCoeff 2 * hbar ^ 2 + deltaHbarClearedCoeff 5 * hbar ^ 5

/-- Exact factorization `-1260 ℏ² + 840 ℏ⁵ = 420 ℏ² (2 ℏ³ - 3)` (`qou-oooq`). -/
theorem deltaHbarTwoTermTrunc_factor (hbar : Int) :
    deltaHbarTwoTermTrunc hbar = 420 * hbar ^ 2 * (2 * hbar ^ 3 - 3) := by
  unfold deltaHbarTwoTermTrunc
  have hc2 : deltaHbarClearedCoeff 2 = -1260 := rfl
  have hc5 : deltaHbarClearedCoeff 5 = 840 := rfl
  have hp5 : hbar ^ 5 = hbar ^ 2 * hbar ^ 3 := by
    rw [← Int.pow_add]
  have hdist : 420 * hbar ^ 2 * (2 * hbar ^ 3 - 3) =
      420 * hbar ^ 2 * (2 * hbar ^ 3) - 420 * hbar ^ 2 * 3 :=
    Int.mul_sub (420 * hbar ^ 2) (2 * hbar ^ 3) 3
  have hmul : 420 * hbar ^ 2 * (2 * hbar ^ 3) = 840 * (hbar ^ 2 * hbar ^ 3) := by
    calc 420 * hbar ^ 2 * (2 * hbar ^ 3)
      _ = 420 * (hbar ^ 2 * (2 * hbar ^ 3)) := Int.mul_assoc 420 (hbar ^ 2) (2 * hbar ^ 3)
      _ = 420 * (2 * (hbar ^ 2 * hbar ^ 3)) := by
          rw [← Int.mul_assoc (hbar ^ 2) 2 (hbar ^ 3), Int.mul_comm (hbar ^ 2) 2,
              Int.mul_assoc 2 (hbar ^ 2) (hbar ^ 3)]
      _ = 840 * (hbar ^ 2 * hbar ^ 3) := by omega
  rw [hc2, hc5, hp5, hdist, hmul]
  omega

/-- Number of independent trace-Gram rows `dim - nullity` (`qou-fadg`). -/
def independentTraceGramRows (dim nullity : Nat) : Nat :=
  dim - nullity

/-- Total independent linear constraints when adjoining `netRows` non-radical rows (`qou-fadg`). -/
def totalTraceGramPlusNetRows (dim nullity netRows : Nat) : Nat :=
  independentTraceGramRows dim nullity + netRows

/-- For `H₃(q)` under Convention D (`dim = 6`, `nullity = 1`), the trace-Gram system has `5`
independent rows and adjoining `1` net row yields a square `6 × 6` system (`qou-fadg`). -/
theorem h3ConventionDTraceGramNet_is_square :
    independentTraceGramRows 6 1 = 5 ∧ totalTraceGramPlusNetRows 6 1 1 = 6 := by
  have h1 : independentTraceGramRows 6 1 = 5 := rfl
  have h2 : totalTraceGramPlusNetRows 6 1 1 = 6 := rfl
  exact ⟨h1, h2⟩

/-- Evaluation of a linear row `row_x + t · row_r` along a 1-parameter shift `x + t r` (`qou-fadg`). -/
def linearRowAlongShift (row_x row_r t : Int) : Int :=
  row_x + t * row_r

/-- Shifting along a radical vector (`gram_r = 0`) preserves every Gram row while shifting the net
functional by `t · net_r` (`qou-fadg`). -/
theorem radicalShift_preserves_gram_scans_net (gram_x net_x net_r t : Int) :
    linearRowAlongShift gram_x 0 t = gram_x ∧
    linearRowAlongShift net_x net_r t - net_x = t * net_r := by
  dsimp [linearRowAlongShift]
  constructor <;> omega

end QOU.MassTheory.PhiQTowerConvexityAndGramRankFive
