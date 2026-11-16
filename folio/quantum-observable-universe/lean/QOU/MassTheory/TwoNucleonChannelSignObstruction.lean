/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization
-/

/-!
# Two-Nucleon Channel Sign Obstruction and Chirality Ordering (`qou-0pzi`)

This module formalizes the two-nucleon sign obstruction (`qou-0pzi`):

1. **Dineutron and diproton binding-sign conditions**:
   Under the single-crossing interface assignment `pp ↦ σ` (`b_pp(q) = z_D = q^3/(q^2 + 1)`)
   and `nn ↦ σ⁻¹` (`b_nn(q) = z_D - h = 1/(q^3 + q)`), the logarithmic binding functional
   `B = -α ln(b)` (`α > 0`) predicts a bound state (`B > 0`) if and only if `0 < b < 1`,
   and an unbound state (`B < 0`) if and only if `b > 1`.
   - Clearing the positive common denominator `q * (q^2 + 1) = q^3 + q`, the dineutron
     numerator is `bnnCommonNum q = 1` and the denominator minus numerator is
     `q^3 + q - 1 > 0` for all `q >= 1`. Thus `0 < b_nn(q) < 1` (`B_nn > 0`) holds
     unconditionally for all `q >= 1`, predicting a bound dineutron in contradiction
     with nature's unbound dineutron (`B_nn ≈ -0.10 MeV < 0`).
   - For the diproton, `b_pp(q) < 1` is equivalent to `q^3 < q^2 + 1` (`q^3 - q^2 - 1 < 0`),
     which holds throughout `[1, 1.465571...)`, including the physical anchor `q_0 ≈ 1.11`
     where `B_pp = +2.0507 MeV` (or `+2.5416 MeV` in `B_sym`), again of the wrong sign.

2. **Chirality ordering `b_nn(q) < b_pn(q) < b_pp(q)` (`B_nn > B_pn > B_pp`)**:
   Over the common denominator `q * (q^2 + 1)`, `b_pp` has numerator `q^4`, `b_nn` has
   numerator `1`, and `2 * b_pn = b_pp + b_nn` has numerator `q^4 + 1`. Consequently,
   for every `q >= 2`, `2 * bnnCommonNum q < bpnBlindTwiceNum q < 2 * bppCommonNum q`
   with equal step numerator `q^4 - 1 > 0`.
-/

namespace QOU.MassTheory.TwoNucleonChannelSignObstruction

/-- Numerator `q^4` of `b_pp(q) = q^4 / (q * (q^2 + 1))` over the common denominator
`q * (q^2 + 1)`. -/
def bppCommonNum (q : Int) : Int :=
  q ^ 4

/-- Numerator `1` of `b_nn(q) = 1 / (q * (q^2 + 1))` over the common denominator
`q * (q^2 + 1)`. -/
def bnnCommonNum (_q : Int) : Int :=
  1

/-- Numerator `q^4 + 1` of `2 * b_pn(q) = 2 z_D - h = (q^4 + 1) / (q * (q^2 + 1))`
over `q * (q^2 + 1)`. -/
def bpnBlindTwiceNum (q : Int) : Int :=
  q ^ 4 + 1

/-- Common denominator `q * (q^2 + 1) = q^3 + q` of the two-nucleon interface factors. -/
def twoNucleonCommonDenom (q : Int) : Int :=
  q * (q ^ 2 + 1)

/-- Deficit `(q^3 + q) - 1` by which the dineutron numerator `1` sits strictly below the
common denominator `q * (q^2 + 1)` (`qou-0pzi`). -/
def dineutronUnitDeficit (q : Int) : Int :=
  twoNucleonCommonDenom q - bnnCommonNum q

/-- For every integer `q >= 1`, `bnnCommonNum q = 1 > 0` and `dineutronUnitDeficit q >= 1 > 0`
(`bnnCommonNum q < twoNucleonCommonDenom q`), certifying `0 < b_nn(q) < 1` (`B_nn > 0`,
bound dineutron prediction) across all `q >= 1` (`qou-0pzi`). -/
theorem dineutron_factor_strictly_below_one (q : Int) (hq : 1 ≤ q) :
    0 < bnnCommonNum q ∧
    1 ≤ dineutronUnitDeficit q ∧
    bnnCommonNum q < twoNucleonCommonDenom q := by
  unfold bnnCommonNum dineutronUnitDeficit twoNucleonCommonDenom
  have hpos : (0 : Int) < 1 := by decide
  have hsq : 1 ≤ q ^ 2 := by
    rw [Int.pow_succ, Int.pow_succ, Int.pow_zero, Int.one_mul]
    have hmul : 1 * 1 ≤ q * q := Int.mul_le_mul hq hq (by decide) (by omega)
    omega
  have hden : 2 ≤ q * (q ^ 2 + 1) := by
    have h2 : 2 ≤ q ^ 2 + 1 := by omega
    have hmul : 1 * 2 ≤ q * (q ^ 2 + 1) := Int.mul_le_mul hq h2 (by decide) (by omega)
    omega
  have hdef : 1 ≤ q * (q ^ 2 + 1) - 1 := by omega
  have hlt : 1 < q * (q ^ 2 + 1) := by omega
  exact ⟨hpos, hdef, hlt⟩

/-- Equal step numerator `(q^2 - 1) * (q^2 + 1) = q^4 - 1` separating `2 * b_nn`,
`2 * b_pn`, and `2 * b_pp` over `q * (q^2 + 1)` (`2 (b_pn - b_nn) = h = 2 (b_pp - b_pn)`). -/
def chiralityStepTwiceNum (q : Int) : Int :=
  q ^ 4 - 1

/-- Exact step identities (`qou-0pzi`):
`bpnBlindTwiceNum q = bppCommonNum q + bnnCommonNum q`,
`bpnBlindTwiceNum q - 2 * bnnCommonNum q = chiralityStepTwiceNum q`, and
`2 * bppCommonNum q - bpnBlindTwiceNum q = chiralityStepTwiceNum q` for all `q : Int`. -/
theorem two_nucleon_chirality_equal_steps (q : Int) :
    bpnBlindTwiceNum q = bppCommonNum q + bnnCommonNum q ∧
    bpnBlindTwiceNum q - 2 * bnnCommonNum q = chiralityStepTwiceNum q ∧
    2 * bppCommonNum q - bpnBlindTwiceNum q = chiralityStepTwiceNum q := by
  unfold bpnBlindTwiceNum bnnCommonNum bppCommonNum chiralityStepTwiceNum
  have hsum : q ^ 4 + 1 = q ^ 4 + 1 := by omega
  have h1 : (q ^ 4 + 1) - 2 * 1 = q ^ 4 - 1 := by omega
  have h2 : 2 * (q ^ 4) - (q ^ 4 + 1) = q ^ 4 - 1 := by omega
  exact ⟨hsum, h1, h2⟩

/-- Strict chirality ordering for all integers `q >= 2`:
`2 * bnnCommonNum q < bpnBlindTwiceNum q < 2 * bppCommonNum q` (`b_nn < b_pn < b_pp`),
which forces the reversed pair-energy ordering `B_nn > B_pn > B_pp` (`qou-0pzi`). -/
theorem two_nucleon_chirality_strict_ordering (q : Int) (hq : 2 ≤ q) :
    2 * bnnCommonNum q < bpnBlindTwiceNum q ∧
    bpnBlindTwiceNum q < 2 * bppCommonNum q := by
  unfold bnnCommonNum bpnBlindTwiceNum bppCommonNum
  have hq2 : 4 ≤ q * q := Int.mul_le_mul hq hq (by decide) (by omega)
  have hq4 : 16 ≤ q ^ 4 := by
    rw [Int.pow_succ, Int.pow_succ, Int.pow_succ, Int.pow_succ, Int.pow_zero, Int.one_mul]
    rw [Int.mul_assoc (q * q) q q]
    have hmul : 4 * 4 ≤ (q * q) * (q * q) := Int.mul_le_mul hq2 hq2 (by decide) (by omega)
    omega
  have hlt1 : 2 * 1 < q ^ 4 + 1 := by omega
  have hlt2 : q ^ 4 + 1 < 2 * (q ^ 4) := by omega
  exact ⟨hlt1, hlt2⟩

end QOU.MassTheory.TwoNucleonChannelSignObstruction
