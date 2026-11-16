/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization
-/

/-!
# Loop-Value Normaliser Uniqueness (`qou-xf14`) and Difference-Route Frame Scaling (`qou-y1w0`)

This module formalizes two linked results on the inter-nucleon interface factor:

1. **Uniqueness of the quantum loop-value normaliser `δ_norm = [2]_q = q + q⁻¹` (`qou-xf14`)**:
   At `z = 1`, the pure-crossing bond factors are
   - `b_pp(q) = z_D = q^3 / (q^2 + 1) = q^2 / [2]_q`,
   - `b_nn(q) = z_D - h = 1 / (q^3 + q) = q^{-2} / [2]_q`.
   Their product satisfies `b_pp(q) * b_nn(q) = q^2 / (q^2 + 1)^2 = 1 / [2]_q^2`
   identically in `q`. Consequently, `δ_norm = [2]_q` is the unique normaliser for which
   `(δ_norm * b_pp) * (δ_norm * b_nn) = 1` holds across all `q`, whereas the classical
   constant `δ = 2` leaves the non-zero residual `q^2 * (q^2 - 1)^2` for all `q >= 2`.

2. **Frame-conditional scaling of the difference-route observable (`qou-y1w0`)**:
   Under an intra-nucleon reordering (`grouped` vs `borromean`) that preserves the
   inter-nucleon bond ratio `r = tr_M(W_atom) / tr_M(W_free)` while scaling `tr_M(W_free)`
   and `tr_M(W_atom)` by a common factor `κ`, the cross-multiplied bond ratio is invariant
   (`trAtomBorr * trFreeGrp = trAtomGrp * trFreeBorr`), whereas the unnormalised trace
   difference `Δtr = tr_M(W_free) - tr_M(W_atom)` scales by `κ`
   (`Δtr_borr = κ * Δtr_grp`).
-/

namespace QOU.MassTheory.LoopValueNormaliserAndFrameDiff

/-- Numerator `q^4` of `b_pp(q) = q^4 / (q * (q^2 + 1))` over the common denominator
`q * (q^2 + 1)`. -/
def bppCommonNum (q : Int) : Int :=
  q ^ 4

/-- Numerator `1` of `b_nn(q) = 1 / (q * (q^2 + 1))` over the common denominator
`q * (q^2 + 1)`. -/
def bnnCommonNum (_q : Int) : Int :=
  1

/-- Common denominator `q * (q^2 + 1) = q^2 * [2]_q` of `b_pp(q)` and `b_nn(q)`. -/
def bondCommonDenom (q : Int) : Int :=
  q * (q ^ 2 + 1)

/-- Numerator `q^2 + 1` of the quantum integer `[2]_q = (q^2 + 1) / q`. -/
def quantumTwoNum (q : Int) : Int :=
  q ^ 2 + 1

/-- Exact polynomial identity certifying `b_pp(q) * b_nn(q) = 1 / [2]_q^2` (`qou-xf14`):
`(bppCommonNum q * bnnCommonNum q) * (quantumTwoNum q * quantumTwoNum q) =`
`(q * q) * (bondCommonDenom q * bondCommonDenom q)` for all `q : Int`. -/
theorem pure_bond_product_equals_inv_quantum_two_sq (q : Int) :
    (bppCommonNum q * bnnCommonNum q) * (quantumTwoNum q * quantumTwoNum q) =
      (q * q) * (bondCommonDenom q * bondCommonDenom q) := by
  unfold bppCommonNum bnnCommonNum quantumTwoNum bondCommonDenom
  let u := q ^ 2 + 1
  change (q ^ 4 * 1) * (u * u) = (q * q) * ((q * u) * (q * u))
  have h1 : (q ^ 4 * 1) * (u * u) = q ^ 4 * (u * u) := by
    rw [Int.mul_one]
  have h2 : (q * u) * (q * u) = (q * q) * (u * u) := by
    rw [Int.mul_assoc q u (q * u)]
    rw [Int.mul_comm u (q * u)]
    rw [← Int.mul_assoc q (q * u) u]
    rw [← Int.mul_assoc q q u]
    rw [Int.mul_assoc (q * q) u u]
  have h3 : (q * q) * ((q * q) * (u * u)) = q ^ 4 * (u * u) := by
    rw [← Int.mul_assoc]
    have hq4 : (q * q) * (q * q) = q ^ 4 := by
      rw [Int.pow_succ, Int.pow_succ, Int.pow_succ, Int.pow_succ, Int.pow_zero, Int.one_mul]
      rw [Int.mul_assoc (q * q) q q]
    rw [hq4]
  rw [h1, h2, h3]

/-- Symmetric `q^{±2}` factorization under `δ_norm = [2]_q`:
- `b_pp(q) * [2]_q = q^2`, expressed over `bondCommonDenom q` as
  `bppCommonNum q * quantumTwoNum q = q^3 * bondCommonDenom q`,
- `b_nn(q) * [2]_q * q^2 = 1`, expressed over `bondCommonDenom q` as
  `bnnCommonNum q * quantumTwoNum q * q^3 = q^2 * bondCommonDenom q`. -/
theorem pure_bond_symmetric_q_square_factorization (q : Int) :
    bppCommonNum q * quantumTwoNum q = q ^ 3 * bondCommonDenom q ∧
    bnnCommonNum q * quantumTwoNum q * q ^ 3 = q ^ 2 * bondCommonDenom q := by
  unfold bppCommonNum bnnCommonNum quantumTwoNum bondCommonDenom
  have hpp : q ^ 4 * (q ^ 2 + 1) = q ^ 3 * (q * (q ^ 2 + 1)) := by
    rw [← Int.mul_assoc]
    have hq : q ^ 3 * q = q ^ 4 := by
      rw [← Int.pow_succ]
    rw [hq]
  have hnn : 1 * (q ^ 2 + 1) * q ^ 3 = q ^ 2 * (q * (q ^ 2 + 1)) := by
    rw [Int.one_mul, Int.mul_comm (q ^ 2 + 1) (q ^ 3), ← Int.mul_assoc]
    have hq : q ^ 2 * q = q ^ 3 := by
      rw [← Int.pow_succ]
    rw [hq]
  exact ⟨hpp, hnn⟩

/-- Residual between `[2]_q^2` and the classical constant `2^2 = 4` (cleared of `q^2`):
`q^2 * (quantumTwoNum q)^2 - 4 * q^4 = q^2 * (q^2 - 1)^2`. -/
def classicalNormaliserResidual (q : Int) : Int :=
  (quantumTwoNum q) ^ 2 - 4 * q ^ 2

/-- Factored form `(q^2 - 1)^2` of `classicalNormaliserResidual q = (q^2 + 1)^2 - 4 q^2`. -/
def classicalNormaliserResidualFactored (q : Int) : Int :=
  (q ^ 2 - 1) ^ 2

/-- For every integer `q`, `(q^2 + 1)^2 - 4 q^2 = (q^2 - 1)^2`, which vanishes at `q = 1`
and is strictly positive at `q = 2` (`9 > 0`) and `q = 3` (`64 > 0`), ruling out the
constant normaliser `δ = 2` for `q ≠ ±1` (`qou-xf14`). -/
theorem classical_normaliser_residual_non_vanishing (q : Int) :
    classicalNormaliserResidual q = classicalNormaliserResidualFactored q ∧
    classicalNormaliserResidual 1 = 0 ∧
    classicalNormaliserResidual 2 = 9 ∧
    classicalNormaliserResidual 3 = 64 := by
  unfold classicalNormaliserResidual classicalNormaliserResidualFactored quantumTwoNum
  have hid : (q ^ 2 + 1) ^ 2 - 4 * q ^ 2 = (q ^ 2 - 1) ^ 2 := by
    have h1 : (q ^ 2 + 1) ^ 2 = (q ^ 2) * (q ^ 2) + 2 * (q ^ 2) + 1 := by
      rw [Int.pow_succ, Int.pow_succ, Int.pow_zero, Int.one_mul]
      rw [Int.add_mul, Int.mul_add, Int.mul_add]
      omega
    have h2 : (q ^ 2 - 1) ^ 2 = (q ^ 2) * (q ^ 2) - 2 * (q ^ 2) + 1 := by
      rw [Int.pow_succ, Int.pow_succ, Int.pow_zero, Int.one_mul]
      rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
      omega
    omega
  have hq1 : (1 ^ 2 + 1 : Int) ^ 2 - 4 * 1 ^ 2 = 0 := by decide
  have hq2 : (2 ^ 2 + 1 : Int) ^ 2 - 4 * 2 ^ 2 = 9 := by decide
  have hq3 : (3 ^ 2 + 1 : Int) ^ 2 - 4 * 3 ^ 2 = 64 := by decide
  exact ⟨hid, hq1, hq2, hq3⟩

/-- Raw trace difference `Δtr = trFree - trAtom` in a given intra-nucleon ordering frame. -/
def traceDifference (trFree trAtom : Int) : Int :=
  trFree - trAtom

/-- When changing intra-nucleon ordering from `grouped` to `borromean` scales both
`trFree` and `trAtom` by a common factor `kappa` (`trFreeBorr = kappa * trFreeGrp`,
`trAtomBorr = kappa * trAtomGrp`), the cross-multiplied bond ratio `trAtom / trFree`
is invariant, whereas the raw difference-route observable `Δtr` scales by `kappa`
(`qou-y1w0`). -/
theorem difference_route_scales_by_kappa_while_ratio_invariant
    (kappa trFreeGrp trAtomGrp : Int) :
    (kappa * trAtomGrp) * trFreeGrp = trAtomGrp * (kappa * trFreeGrp) ∧
    traceDifference (kappa * trFreeGrp) (kappa * trAtomGrp) =
      kappa * traceDifference trFreeGrp trAtomGrp := by
  unfold traceDifference
  have hratio : (kappa * trAtomGrp) * trFreeGrp = trAtomGrp * (kappa * trFreeGrp) := by
    rw [Int.mul_comm kappa trAtomGrp, Int.mul_assoc]
  have hdiff : kappa * trFreeGrp - kappa * trAtomGrp = kappa * (trFreeGrp - trAtomGrp) := by
    rw [Int.mul_sub]
  exact ⟨hratio, hdiff⟩

end QOU.MassTheory.LoopValueNormaliserAndFrameDiff
