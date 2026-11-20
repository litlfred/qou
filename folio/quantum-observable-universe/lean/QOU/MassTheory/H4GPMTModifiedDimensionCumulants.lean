import Mathlib.Tactic
import QOU.MassTheory.GPMTThreeRowCumulantBridge

/-!
# `H_4(q)` Ocneanu/Wedderburn Weights, Killed 3- and 4-Row GPMT Modified Quantum Dimensions, and Per-Partition `A = 4` Cumulants

This module extends the `H_3(q)` Wedderburn weight and Geer–Patureau-Mirand–Turaev (GPMT)
modified-trace formalization of `QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace` and
`QOU.MassTheory.GPMTThreeRowCumulantBridge` from `A = 3` (`H_3(q)`) to `A = 4` (`H_4(q)`).

## Main Results

1. **Section 1 — The 5 Ocneanu/Wedderburn Weights on `H_4(q)` (`w4`, `w31`, `w22`, `w211`, `w1111`):**
   Defines the five rational Wedderburn weights `w_λ(q, z)` corresponding to the five
   partitions of `4`:
   * `λ = (4)` (Specht dimension `f^{(4)} = 1`, `1` row),
   * `λ = (3,1)` (Specht dimension `f^{(3,1)} = 3`, `2` rows),
   * `λ = (2,2)` (Specht dimension `f^{(2,2)} = 2`, `2` rows),
   * `λ = (2,1,1)` (Specht dimension `f^{(2,1,1)} = 3`, `3` rows),
   * `λ = (1^4)` (Specht dimension `f^{(1^4)} = 1`, `4` rows).
   Establishes all five Markov character equations on the minimal-length
   conjugacy-class representatives of `H_4(q)`:
   * `C_1 = 1` (`tr_M(1) = 1`, `w4_add_three_w31_add_two_w22_add_three_w211_add_w1111`),
   * `C_2 = T_1` (`tr_M(T_1) = z`, `h4_markov_char_T1`),
   * `C_3 = T_1 T_2` (`tr_M(T_1 T_2) = z^2`, `h4_markov_char_T1T2`),
   * `C_4 = T_1 T_3` (`tr_M(T_1 T_3) = z^2`, `h4_markov_char_T1T3`),
   * `C_5 = T_1 T_2 T_3` (`tr_M(T_1 T_2 T_3) = z^3`, `h4_markov_char_T1T2T3`).

2. **Section 2 — Convention-D Specialization (`z_D = q^3 / (q^2 + 1)`) & Two-Row Survival:**
   At the `N = 2` Convention-D Markov parameter `z_D = q^3 / (q^2 + 1)`:
   * Both `≥ 3`-row sectors vanish identically:
     `w211_conventionD : w211 q (zD q) = 0` and `w1111_conventionD : w1111 q (zD q) = 0`.
   * The three `≤ 2`-row sectors evaluate to exact positive rational functions of `q`:
     `w4_conventionD`, `w31_conventionD`, `w22_conventionD`, satisfying the two-row
     normalization `w4 q (zD q) + 3 * w31 q (zD q) + 2 * w22 q (zD q) = 1`
     (`weights_h4_conventionD_twoRow_sum_eq_one`).

3. **Section 3 — First-Order GPMT Modified Quantum Dimensions `d_D(S^{(2,1,1)})` and `d_D(S^{(1^4)})`:**
   Because both `w_{(2,1,1)}(q, z)` and `w_{(1^4)}(q, z)` contain the simple factor
   `((q^2 + 1) z - q^3) = (q^2 + 1)(z - z_D)` coming from the row-3 cell `(3, 1)` of content
   `c = -2`, both have a **simple first-order zero** at `z = z_D` (`w211_factor_zD`,
   `w1111_factor_zD`). Their first-order GPMT modified quantum dimensions
   `d_D(S^λ) = ∂w_λ(q, z)/∂z |_{z = z_D}` (`dMod211`, `dMod1111`) satisfy:
   * `dMod211 q = -q^3 (q^4 + q^2 + 1) / ((q^2 + 1)^3 (q^4 + 1)) = -[3]_q / ([2]_q^2 [4]_q) < 0`
     for all `q > 0` (`dMod211_neg_of_pos`, `dMod211_eq_neg_qInt3_div`),
   * `dMod1111 q = +q^7 / ((q^2 + 1)^3 (q^4 + 1) (q^4 + q^2 + 1)) = +1 / ([2]_q^2 [3]_q [4]_q) > 0`
     for all `q > 0` (`dMod1111_pos_of_pos`, `dMod1111_eq_inv_qInts`).
   Why do `dMod211` and `dMod1111` have opposite signs? Because `z_D = z_2` lies strictly
   between the row-2 root `z_1 = q` and the row-4 root `z_3 = q^5 / (q^4 + q^2 + 1)`:
   `z_3 < z_D < z_1` (`zD_sub_z3_pos_of_pos`), so the extra row-4 factor
   `((q^4 + q^2 + 1) z_D - q^5) = q^3 / (q^2 + 1) > 0` flips the sign of `d_D(S^{(1^4)})`
   from negative to positive.

4. **Section 4 — Per-Partition GPMT-Weighted `≥ 3`-Row Stratum & `A = 4` Cumulants:**
   In the unweighted `≥ 3`-row stratum at `A = 4`, the signed Springer dimensions
   `Δ_{(2,1,1)} = (-1)^3 · 3 = -3` and `Δ_{(1^4)} = (-1)^6 · 1 = +1` have opposite signs
   and partially cancel (`-3 + 1 = -2`). When weighted by their per-partition GPMT modified
   quantum dimensions `dMod211 q < 0` and `dMod1111 q > 0`, the row-depth sign flip
   aligns with the Springer parity sign flip so that **both** terms in
   `sRow3GPMT_H4 q 4 = (-3) * dMod211 q + 1 * dMod1111 q` are strictly positive for all
   `q > 0` (`sRow3GPMT_H4_four_both_terms_pos`). The resulting 4-body Mayer cumulant
   `mu4GPMT_H4 q = sRow3GPMT_H4 q 4 - 4 * mu3GPMT_H4 q` has the exact closed form
   `-q^3 (q^8 + 2 q^6 - 2 q^4 + 2 q^2 + 1) / ((q^2 + 1)^3 (q^4 + 1) (q^4 + q^2 + 1))`
   and is strictly negative for all `q > 0` (`mu4GPMT_H4_neg_of_pos`), preserving the
   physical `(μ₂ = 0, μ₃ > 0, μ₄ < 0)` nuclear binding sign window.
-/

namespace QOU.MassTheory
namespace H4GPMTModifiedDimensionCumulants

open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace (zD dMod111)
open QOU.MassTheory.GPMTThreeRowCumulantBridge

/-! ## Section 1: The 5 Ocneanu/Wedderburn Weights on `H_4(q)` -/

section H4WedderburnWeights

variable {K : Type*} [Field K]

/-- Ocneanu/Wedderburn weight `w_{(4)}(q, z)` of the 1D totally symmetric `(4)` sector of `H_4(q)`. -/
def w4 (q z : K) : K :=
  (q * z + 1) * (q ^ 3 * z + q * z + 1) * (q ^ 5 * z + q ^ 3 * z + q * z + 1) /
    ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))

/-- Ocneanu/Wedderburn weight `w_{(3,1)}(q, z)` of the 3D standard `(3,1)` sector of `H_4(q)`. -/
def w31 (q z : K) : K :=
  q * (q - z) * (q * z + 1) * (q ^ 3 * z + q * z + 1) /
    ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1))

/-- Ocneanu/Wedderburn weight `w_{(2,2)}(q, z)` of the 2D two-row `(2,2)` sector of `H_4(q)`. -/
def w22 (q z : K) : K :=
  q ^ 3 * (q - z) * (q * z + 1) /
    ((q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1))

/-- Ocneanu/Wedderburn weight `w_{(2,1,1)}(q, z)` of the 3D three-row `(2,1,1)` sector of `H_4(q)`. -/
def w211 (q z : K) : K :=
  q ^ 2 * (z - q) * (q * z + 1) * ((q ^ 2 + 1) * z - q ^ 3) /
    ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1))

/-- Ocneanu/Wedderburn weight `w_{(1^4)}(q, z)` of the 1D totally antisymmetric `(1^4)` sector of `H_4(q)`. -/
def w1111 (q z : K) : K :=
  -q ^ 3 * (z - q) * ((q ^ 2 + 1) * z - q ^ 3) * ((q ^ 4 + q ^ 2 + 1) * z - q ^ 5) /
    ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))

/-- Common denominator `D_4(q) = (q^2 + 1)^2 (q^4 + 1) (q^4 + q^2 + 1)` of the `H_4(q)` Wedderburn weights. -/
def h4Denom (q : K) : K :=
  (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)

theorem h4Denom_ne_zero (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    h4Denom q ≠ 0 :=
  mul_ne_zero (mul_ne_zero (pow_ne_zero 2 hq2) hq41) hq421

theorem w4_over_h4Denom (q z : K) :
    w4 q z =
      (q * z + 1) * (q ^ 3 * z + q * z + 1) * (q ^ 5 * z + q ^ 3 * z + q * z + 1) / h4Denom q :=
  rfl

theorem w31_over_h4Denom (q z : K) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w31 q z =
      q * (q - z) * (q * z + 1) * (q ^ 3 * z + q * z + 1) * (q ^ 4 + q ^ 2 + 1) / h4Denom q := by
  unfold w31 h4Denom
  exact (mul_div_mul_right _ _ hq421).symm

theorem w22_over_h4Denom (q z : K) (hq41 : q ^ 4 + 1 ≠ 0) :
    w22 q z =
      q ^ 3 * (q - z) * (q * z + 1) * (q ^ 4 + 1) / h4Denom q := by
  unfold w22 h4Denom
  have hcomm :
      (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) =
        (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + 1) := by ring
  rw [hcomm]
  exact (mul_div_mul_right _ _ hq41).symm

theorem w211_over_h4Denom (q z : K) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w211 q z =
      q ^ 2 * (z - q) * (q * z + 1) * ((q ^ 2 + 1) * z - q ^ 3) * (q ^ 4 + q ^ 2 + 1) /
        h4Denom q := by
  unfold w211 h4Denom
  exact (mul_div_mul_right _ _ hq421).symm

theorem w1111_over_h4Denom (q z : K) :
    w1111 q z =
      -q ^ 3 * (z - q) * ((q ^ 2 + 1) * z - q ^ 3) * ((q ^ 4 + q ^ 2 + 1) * z - q ^ 5) /
        h4Denom q :=
  rfl

/-- **First `H_4(q)` Markov Character Equation (Identity Class `1`, Cycle Type `(1^4)`)**:
The Specht-dimension-weighted sum of the 5 Wedderburn weights on `H_4(q)` equals `tr_M(1) = 1`:
`1 · w_{(4)} + 3 · w_{(3,1)} + 2 · w_{(2,2)} + 3 · w_{(2,1,1)} + 1 · w_{(1^4)} = 1`. -/
theorem w4_add_three_w31_add_two_w22_add_three_w211_add_w1111
    (q z : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w4 q z + 3 * w31 q z + 2 * w22 q z + 3 * w211 q z + w1111 q z = 1 := by
  have hden : h4Denom q ≠ 0 := h4Denom_ne_zero q hq2 hq41 hq421
  rw [w4_over_h4Denom, w31_over_h4Denom q z hq421, w22_over_h4Denom q z hq41,
    w211_over_h4Denom q z hq421, w1111_over_h4Denom]
  field_simp [hden]
  unfold h4Denom
  ring

/-- **Second `H_4(q)` Markov Character Equation (Single Generator `T_1`, Cycle Type `(2,1,1)`)**:
Weighted by the irreducible characters `χ_λ(T_1)`
(`q`, `2q - q⁻¹`, `q - q⁻¹`, `q - 2q⁻¹`, `-q⁻¹`), the 5 Wedderburn weights sum to `tr_M(T_1) = z`. -/
theorem h4_markov_char_T1
    (q z : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    q * w4 q z + (2 * q - q⁻¹) * w31 q z + (q - q⁻¹) * w22 q z +
      (q - 2 * q⁻¹) * w211 q z + (-q⁻¹) * w1111 q z = z := by
  have hden : h4Denom q ≠ 0 := h4Denom_ne_zero q hq2 hq41 hq421
  rw [w4_over_h4Denom, w31_over_h4Denom q z hq421, w22_over_h4Denom q z hq41,
    w211_over_h4Denom q z hq421, w1111_over_h4Denom]
  field_simp [hden, hq]
  unfold h4Denom
  ring

/-- **Third `H_4(q)` Markov Character Equation (Adjacent Product `T_1 T_2`, Cycle Type `(3,1)`)**:
Weighted by the irreducible characters `χ_λ(T_1 T_2)`
(`q^2`, `q^2 - 1`, `-1`, `-1 + q⁻²`, `q⁻²`), the 5 Wedderburn weights sum to `tr_M(T_1 T_2) = z^2`. -/
theorem h4_markov_char_T1T2
    (q z : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    q ^ 2 * w4 q z + (q ^ 2 - 1) * w31 q z + (-1) * w22 q z +
      (-1 + (q ^ 2)⁻¹) * w211 q z + (q ^ 2)⁻¹ * w1111 q z = z ^ 2 := by
  have hden : h4Denom q ≠ 0 := h4Denom_ne_zero q hq2 hq41 hq421
  rw [w4_over_h4Denom, w31_over_h4Denom q z hq421, w22_over_h4Denom q z hq41,
    w211_over_h4Denom q z hq421, w1111_over_h4Denom]
  field_simp [hden, hq]
  unfold h4Denom
  ring

/-- **Fourth `H_4(q)` Markov Character Equation (Commuting Pair `T_1 T_3`, Cycle Type `(2,2)`)**:
Weighted by the irreducible characters `χ_λ(T_1 T_3)`
(`q^2`, `q^2 - 2`, `q^2 + q⁻²`, `-2 + q⁻²`, `q⁻²`), the 5 Wedderburn weights sum to `tr_M(T_1 T_3) = z^2`. -/
theorem h4_markov_char_T1T3
    (q z : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    q ^ 2 * w4 q z + (q ^ 2 - 2) * w31 q z + (q ^ 2 + (q ^ 2)⁻¹) * w22 q z +
      (-2 + (q ^ 2)⁻¹) * w211 q z + (q ^ 2)⁻¹ * w1111 q z = z ^ 2 := by
  have hden : h4Denom q ≠ 0 := h4Denom_ne_zero q hq2 hq41 hq421
  rw [w4_over_h4Denom, w31_over_h4Denom q z hq421, w22_over_h4Denom q z hq41,
    w211_over_h4Denom q z hq421, w1111_over_h4Denom]
  field_simp [hden, hq]
  unfold h4Denom
  ring

/-- **Fifth `H_4(q)` Markov Character Equation (Coxeter Element `T_1 T_2 T_3`, Cycle Type `(4)`)**:
Weighted by the irreducible characters `χ_λ(T_1 T_2 T_3)`
(`q^3`, `-q`, `0`, `q⁻¹`, `-q⁻³`), the 5 Wedderburn weights sum to `tr_M(T_1 T_2 T_3) = z^3`. -/
theorem h4_markov_char_T1T2T3
    (q z : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    q ^ 3 * w4 q z + (-q) * w31 q z + 0 * w22 q z +
      q⁻¹ * w211 q z + (-(q ^ 3)⁻¹) * w1111 q z = z ^ 3 := by
  have hden : h4Denom q ≠ 0 := h4Denom_ne_zero q hq2 hq41 hq421
  rw [w4_over_h4Denom, w31_over_h4Denom q z hq421, w22_over_h4Denom q z hq41,
    w211_over_h4Denom q z hq421, w1111_over_h4Denom]
  field_simp [hden, hq]
  unfold h4Denom
  ring

end H4WedderburnWeights

/-! ## Section 2: Convention-D Specialization (`z_D = q^3 / (q^2 + 1)`) & Two-Row Survival -/

section H4ConventionDSpecialization

variable {K : Type*} [Field K]

/-- Helper factor `q21 q = q^2 + 1` so `field_simp` treats `q^2 + 1` as an atomic nonzero denominator. -/
def q21 (q : K) : K := q ^ 2 + 1

/-- At Convention D (`z_D = q^3 / (q^2 + 1)`), the 3-row `(2,1,1)` Wedderburn weight vanishes
identically: `w_{(2,1,1)}(q, z_D) = 0`. -/
theorem w211_conventionD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    w211 q (zD q) = 0 := by
  unfold w211 zD
  have hnum : (q ^ 2 + 1) * (q ^ 3 / (q ^ 2 + 1)) - q ^ 3 = 0 := by
    rw [mul_div_cancel₀ _ hq2, sub_self]
  rw [hnum, mul_zero, zero_div]

/-- At Convention D (`z_D = q^3 / (q^2 + 1)`), the 4-row `(1^4)` Wedderburn weight vanishes
identically: `w_{(1^4)}(q, z_D) = 0`. -/
theorem w1111_conventionD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    w1111 q (zD q) = 0 := by
  unfold w1111 zD
  have hnum : (q ^ 2 + 1) * (q ^ 3 / (q ^ 2 + 1)) - q ^ 3 = 0 := by
    rw [mul_div_cancel₀ _ hq2, sub_self]
  rw [hnum, mul_zero, zero_mul, zero_div]

/-- At Convention D, the symmetric `(4)` weight evaluates to
`(q^8 + q^6 + q^4 + q^2 + 1) / (q^2 + 1)^4 = [5]_q / [2]_q^4`. -/
theorem w4_conventionD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w4 q (zD q) = (q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 4 := by
  have hden : h4Denom q ≠ 0 := h4Denom_ne_zero q hq2 hq41 hq421
  have hq21 : q21 q ≠ 0 := hq2
  rw [w4_over_h4Denom]
  change
    (q * (q ^ 3 / q21 q) + 1) * (q ^ 3 * (q ^ 3 / q21 q) + q * (q ^ 3 / q21 q) + 1) *
        (q ^ 5 * (q ^ 3 / q21 q) + q ^ 3 * (q ^ 3 / q21 q) + q * (q ^ 3 / q21 q) + 1) /
        h4Denom q =
      (q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) / q21 q ^ 4
  field_simp [hden, hq21]
  unfold h4Denom q21
  ring

/-- At Convention D, the 2-row `(3,1)` weight evaluates to
`q^2 (q^4 + q^2 + 1) / (q^2 + 1)^4 = [3]_q / [2]_q^4`. -/
theorem w31_conventionD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w31 q (zD q) = q ^ 2 * (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 4 := by
  have hden : h4Denom q ≠ 0 := h4Denom_ne_zero q hq2 hq41 hq421
  have hq21 : q21 q ≠ 0 := hq2
  rw [w31_over_h4Denom q (zD q) hq421]
  change
    q * (q - q ^ 3 / q21 q) * (q * (q ^ 3 / q21 q) + 1) *
        (q ^ 3 * (q ^ 3 / q21 q) + q * (q ^ 3 / q21 q) + 1) * (q ^ 4 + q ^ 2 + 1) /
        h4Denom q =
      q ^ 2 * (q ^ 4 + q ^ 2 + 1) / q21 q ^ 4
  field_simp [hden, hq21]
  unfold h4Denom q21
  ring

/-- At Convention D, the 2-row `(2,2)` weight evaluates to
`q^4 / (q^2 + 1)^4 = 1 / [2]_q^4`. -/
theorem w22_conventionD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w22 q (zD q) = q ^ 4 / (q ^ 2 + 1) ^ 4 := by
  have hden : h4Denom q ≠ 0 := h4Denom_ne_zero q hq2 hq41 hq421
  have hq21 : q21 q ≠ 0 := hq2
  rw [w22_over_h4Denom q (zD q) hq41]
  change
    q ^ 3 * (q - q ^ 3 / q21 q) * (q * (q ^ 3 / q21 q) + 1) * (q ^ 4 + 1) / h4Denom q =
      q ^ 4 / q21 q ^ 4
  field_simp [hden, hq21]
  unfold h4Denom q21
  ring

/-- **Two-Row Normalization at Convention D on `H_4(q)`**:
Because both `≥ 3`-row sectors `(2,1,1)` and `(1^4)` vanish at `z = z_D`, the surviving
two-row Wedderburn weights satisfy `w_{(4)}(z_D) + 3 w_{(3,1)}(z_D) + 2 w_{(2,2)}(z_D) = 1`. -/
theorem weights_h4_conventionD_twoRow_sum_eq_one
    (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w4 q (zD q) + 3 * w31 q (zD q) + 2 * w22 q (zD q) = 1 := by
  have hq21 : q21 q ≠ 0 := hq2
  rw [w4_conventionD q hq2 hq41 hq421, w31_conventionD q hq2 hq41 hq421,
    w22_conventionD q hq2 hq41 hq421]
  change
    (q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) / q21 q ^ 4 +
      3 * (q ^ 2 * (q ^ 4 + q ^ 2 + 1) / q21 q ^ 4) +
      2 * (q ^ 4 / q21 q ^ 4) = 1
  field_simp [hq21]
  unfold q21
  ring

end H4ConventionDSpecialization

/-! ## Section 3: First-Order GPMT Modified Quantum Dimensions `d_D(S^{(2,1,1)})` & `d_D(S^{(1^4)})` -/

section H4GPMTModifiedDimensions

variable {K : Type*} [Field K]

/-- **GPMT First-Order Factorization of `w_{(2,1,1)}(q, z)`**:
`w_{(2,1,1)}(q, z)` factors as `(z - z_D)` times the regular factor
`q^2 (z - q) (q z + 1) / ((q^2 + 1)(q^4 + 1))`. -/
theorem w211_factor_zD (q z : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    w211 q z =
      (z - zD q) * (q ^ 2 * (z - q) * (q * z + 1) / ((q ^ 2 + 1) * (q ^ 4 + 1))) := by
  unfold w211 zD
  have hsub : z - q ^ 3 / (q ^ 2 + 1) = ((q ^ 2 + 1) * z - q ^ 3) / (q ^ 2 + 1) := by
    rw [sub_div' hq2]; ring
  rw [hsub, div_mul_div_comm]
  ring

/-- **GPMT First-Order Factorization of `w_{(1^4)}(q, z)`**:
`w_{(1^4)}(q, z)` factors as `(z - z_D)` times the regular factor
`-q^3 (z - q) ((q^4 + q^2 + 1) z - q^5) / ((q^2 + 1)(q^4 + 1)(q^4 + q^2 + 1))`. -/
theorem w1111_factor_zD (q z : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    w1111 q z =
      (z - zD q) *
        (-q ^ 3 * (z - q) * ((q ^ 4 + q ^ 2 + 1) * z - q ^ 5) /
          ((q ^ 2 + 1) * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))) := by
  unfold w1111 zD
  have hsub : z - q ^ 3 / (q ^ 2 + 1) = ((q ^ 2 + 1) * z - q ^ 3) / (q ^ 2 + 1) := by
    rw [sub_div' hq2]; ring
  rw [hsub, div_mul_div_comm]
  ring

/-- The first-order Geer–Patureau-Mirand–Turaev modified quantum dimension
`d_D(S^{(2,1,1)}) = ∂w_{(2,1,1)}(q, z)/∂z |_{z = z_D}` of the killed 3-row `(2,1,1)`
sector of `H_4(q)` at Convention D. -/
def dMod211 (q : K) : K :=
  -q ^ 3 * (q ^ 4 + q ^ 2 + 1) / ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1))

/-- The first-order Geer–Patureau-Mirand–Turaev modified quantum dimension
`d_D(S^{(1^4)}) = ∂w_{(1^4)}(q, z)/∂z |_{z = z_D}` of the killed 4-row `(1^4)`
sector of `H_4(q)` at Convention D. -/
def dMod1111 (q : K) : K :=
  q ^ 7 / ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))

/-- The regular factor of `w_{(2,1,1)}(q, z) / (z - z_D)` evaluated at `z = z_D` equals `dMod211 q`. -/
theorem w211_slope_at_zD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) :
    q ^ 2 * (zD q - q) * (q * zD q + 1) / ((q ^ 2 + 1) * (q ^ 4 + 1)) = dMod211 q := by
  have hq21 : q21 q ≠ 0 := hq2
  have hden : q21 q * (q ^ 4 + 1) ≠ 0 := mul_ne_zero hq21 hq41
  have hden3 : q21 q ^ 3 * (q ^ 4 + 1) ≠ 0 := mul_ne_zero (pow_ne_zero 3 hq21) hq41
  change
    q ^ 2 * (q ^ 3 / q21 q - q) * (q * (q ^ 3 / q21 q) + 1) / (q21 q * (q ^ 4 + 1)) =
      -q ^ 3 * (q ^ 4 + q ^ 2 + 1) / (q21 q ^ 3 * (q ^ 4 + 1))
  rw [div_eq_div_iff hden hden3]
  field_simp [hq21]
  unfold q21
  ring

/-- The regular factor of `w_{(1^4)}(q, z) / (z - z_D)` evaluated at `z = z_D` equals `dMod1111 q`. -/
theorem w1111_slope_at_zD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    -q ^ 3 * (zD q - q) * ((q ^ 4 + q ^ 2 + 1) * zD q - q ^ 5) /
        ((q ^ 2 + 1) * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) = dMod1111 q := by
  have hq21 : q21 q ≠ 0 := hq2
  have hden1 : q21 q * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) ≠ 0 :=
    mul_ne_zero (mul_ne_zero hq21 hq41) hq421
  have hden3 : q21 q ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) ≠ 0 :=
    mul_ne_zero (mul_ne_zero (pow_ne_zero 3 hq21) hq41) hq421
  change
    -q ^ 3 * (q ^ 3 / q21 q - q) * ((q ^ 4 + q ^ 2 + 1) * (q ^ 3 / q21 q) - q ^ 5) /
        (q21 q * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) =
      q ^ 7 / (q21 q ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))
  rw [div_eq_div_iff hden1 hden3]
  field_simp [hq21]
  unfold q21
  ring

/-- Symmetric quantum integer `[4]_q = q^3 + q + q⁻¹ + q⁻³`. -/
def qInt4 (q : K) : K := q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3

/-- **Quantum-Integer Form of `dMod211`**:
For every `q ≠ 0` with `q^2 + 1 ≠ 0` and `q^4 + 1 ≠ 0`,
`dMod211 q = -[3]_q / ([2]_q^2 [4]_q)`. -/
theorem dMod211_eq_neg_qInt3_div (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq41 : q ^ 4 + 1 ≠ 0) :
    dMod211 q = -qInt3 q / (qInt2 q ^ 2 * qInt4 q) := by
  unfold dMod211 qInt2 qInt3 qInt4
  have hfac2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  have hfac3 : q ^ 2 + 1 + q⁻¹ ^ 2 = (q ^ 4 + q ^ 2 + 1) / q ^ 2 := by field_simp
  have hfac4 : q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3 = (q ^ 2 + 1) * (q ^ 4 + 1) / q ^ 3 := by
    field_simp; ring
  rw [hfac2, hfac3, hfac4]
  field_simp

/-- **Quantum-Integer Form of `dMod1111`**:
For every `q ≠ 0` with `q^2 + 1 ≠ 0` and `q^4 + 1 ≠ 0`,
`dMod1111 q = 1 / ([2]_q^2 [3]_q [4]_q)`. -/
theorem dMod1111_eq_inv_qInts (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq41 : q ^ 4 + 1 ≠ 0) :
    dMod1111 q = 1 / (qInt2 q ^ 2 * qInt3 q * qInt4 q) := by
  unfold dMod1111 qInt2 qInt3 qInt4
  have hfac2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  have hfac3 : q ^ 2 + 1 + q⁻¹ ^ 2 = (q ^ 4 + q ^ 2 + 1) / q ^ 2 := by field_simp
  have hfac4 : q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3 = (q ^ 2 + 1) * (q ^ 4 + 1) / q ^ 3 := by
    field_simp; ring
  rw [hfac2, hfac3, hfac4]
  field_simp

end H4GPMTModifiedDimensions

/-! ## Section 3b: Strict Sign Theorems for `dMod211` and `dMod1111` over Ordered Fields -/

section H4GPMTModifiedDimensionSigns

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- For any `q : R`, `q^4 + 1` is strictly positive in a strict ordered field. -/
theorem pow_four_add_one_pos (q : R) : 0 < q ^ 4 + 1 := by
  positivity

/-- The rank-3 hook-content Markov root `z_3 = q^5 / (q^4 + q^2 + 1)`. -/
def z3 (q : R) : R := q ^ 5 / (q ^ 4 + q ^ 2 + 1)

/-- **Root Ordering Theorem (`z_3 < z_D < q` for all `q > 0`)**:
The Convention-D root `z_D = q^3 / (q^2 + 1)` lies strictly above the rank-3 root
`z_3 = q^5 / (q^4 + q^2 + 1)`, with exact gap
`zD q - z3 q = q^3 / ((q^2 + 1)(q^4 + q^2 + 1)) > 0`.
Combined with `zD q - q < 0` (`zD_sub_self_neg_of_pos`), this explains why the 3-row
modified quantum dimension `dMod211 q` is negative while the 4-row modified quantum
dimension `dMod1111 q` is positive. -/
theorem zD_sub_z3_eq (q : R) :
    zD q - z3 q = q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  have hq2 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  have hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt (pow_four_add_sq_add_one_pos q)
  unfold zD z3
  rw [div_sub_div _ _ hq2 hq421]
  ring

/-- For all `q > 0`, `0 < zD q - z3 q` (`z_3 < z_D`). -/
theorem zD_sub_z3_pos_of_pos (q : R) (hq : 0 < q) :
    0 < zD q - z3 q := by
  rw [zD_sub_z3_eq q]
  exact div_pos (pow_pos hq 3) (mul_pos (sq_add_one_pos q) (pow_four_add_sq_add_one_pos q))

/-- **Strict Negativity of the 3-Row GPMT Modified Quantum Dimension `d_D(S^{(2,1,1)})`**:
For every `q > 0`, `dMod211 q < 0`. -/
theorem dMod211_neg_of_pos (q : R) (hq : 0 < q) :
    dMod211 q < 0 := by
  unfold dMod211
  rw [neg_mul, neg_div]
  apply neg_neg_of_pos
  apply div_pos
  · exact mul_pos (pow_pos hq 3) (pow_four_add_sq_add_one_pos q)
  · exact mul_pos (pow_pos (sq_add_one_pos q) 3) (pow_four_add_one_pos q)

/-- **Strict Positivity of the 4-Row GPMT Modified Quantum Dimension `d_D(S^{(1^4)})`**:
For every `q > 0`, `0 < dMod1111 q`. -/
theorem dMod1111_pos_of_pos (q : R) (hq : 0 < q) :
    0 < dMod1111 q := by
  unfold dMod1111
  apply div_pos
  · exact pow_pos hq 7
  · exact mul_pos
      (mul_pos (pow_pos (sq_add_one_pos q) 3) (pow_four_add_one_pos q))
      (pow_four_add_sq_add_one_pos q)

end H4GPMTModifiedDimensionSigns

/-! ## Section 4: Per-Partition GPMT-Weighted `≥ 3`-Row Stratum & `A = 4` Cumulants -/

section PerPartitionGPMTCumulants

variable {R : Type*} [Field R]

/-- Common denominator `D_{\mathrm{mod}}(q) = (q^2 + 1)^3 (q^4 + 1) (q^4 + q^2 + 1)`
of the `H_4(q)` GPMT modified quantum dimensions `dMod211` and `dMod1111`. -/
def h4ModDenom (q : R) : R :=
  (q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)

theorem h4ModDenom_ne_zero (q : R) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    h4ModDenom q ≠ 0 :=
  mul_ne_zero (mul_ne_zero (pow_ne_zero 3 hq2) hq41) hq421

theorem dMod211_over_h4ModDenom (q : R) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    dMod211 q = -q ^ 3 * (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / h4ModDenom q := by
  unfold dMod211 h4ModDenom
  exact (mul_div_mul_right _ _ hq421).symm

theorem dMod1111_over_h4ModDenom (q : R) :
    dMod1111 q = q ^ 7 / h4ModDenom q :=
  rfl

theorem dMod111_over_h4ModDenom (q : R) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) :
    dMod111 q = -q ^ 3 * ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1)) / h4ModDenom q := by
  unfold dMod111 h4ModDenom
  have hcomm :
      (q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) =
        (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) * ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1)) := by ring
  rw [hcomm]
  exact (mul_div_mul_right _ _ (mul_ne_zero (pow_ne_zero 2 hq2) hq41)).symm

/-- The per-partition GPMT-weighted `≥ 3`-row single-algebra trace stratum at cluster size `A`:
* For `A ≤ 2`: `0` (no partition has `≥ 3` rows),
* For `A = 3`: `Δ_{(1^3)} · d_D(S^{(1^3)}) = (-1) · dMod111 q = -dMod111 q`,
* For `A = 4`: `Δ_{(2,1,1)} · d_D(S^{(2,1,1)}) + Δ_{(1^4)} · d_D(S^{(1^4)}) = -3 · dMod211 q + dMod1111 q`. -/
def sRow3GPMT_H4 (q : R) : ℕ → R
  | 3 => -dMod111 q
  | 4 => -3 * dMod211 q + dMod1111 q
  | _ => 0

/-- Per-partition GPMT-weighted 2-body (edge) Mayer cumulant `μ₂^{\mathrm{GPMT}, H_4}(q)`. -/
def mu2GPMT_H4 (q : R) : R :=
  sRow3GPMT_H4 q 2

/-- Per-partition GPMT-weighted 3-body (triangle) Mayer cumulant
`μ₃^{\mathrm{GPMT}, H_4}(q) = S(3) - 3 · μ₂(q)`. -/
def mu3GPMT_H4 (q : R) : R :=
  sRow3GPMT_H4 q 3 - 3 * mu2GPMT_H4 q

/-- Per-partition GPMT-weighted 4-body (tetrahedron) Mayer cumulant
`μ₄^{\mathrm{GPMT}, H_4}(q) = S(4) - 6 · μ₂(q) - 4 · μ₃(q)`. -/
def mu4GPMT_H4 (q : R) : R :=
  sRow3GPMT_H4 q 4 - 6 * mu2GPMT_H4 q - 4 * mu3GPMT_H4 q

/-- At `A = 2` and `A = 3`, `mu2GPMT_H4` and `mu3GPMT_H4` agree identically with `mu2GPMT`
and `mu3GPMT` of `QOU.MassTheory.GPMTThreeRowCumulantBridge`. -/
theorem mu2_mu3_H4_eq_bridge (q : R) :
    mu2GPMT_H4 q = 0 ∧
    mu3GPMT_H4 q = -dMod111 q ∧
    mu3GPMT_H4 q = mu3GPMT q := by
  rcases muGPMT_closed_forms q with ⟨_, h3, _⟩
  have h2 : mu2GPMT_H4 q = 0 := rfl
  have h3_H4 : mu3GPMT_H4 q = -dMod111 q := by
    unfold mu3GPMT_H4
    rw [h2]
    change -dMod111 q - 3 * 0 = -dMod111 q
    ring
  refine ⟨h2, h3_H4, ?_⟩
  rw [h3_H4, h3]

/-- **Constructive Reinforcement of the `A = 4` `≥ 3`-Row Stratum**:
For all `q > 0`, because `dMod211 q < 0` matches the negative Springer sign `Δ_{(2,1,1)} = -3 < 0`
while `dMod1111 q > 0` matches the positive Springer sign `Δ_{(1^4)} = +1 > 0`, **both**
per-partition contributions `-3 * dMod211 q` and `dMod1111 q` in `sRow3GPMT_H4 q 4` are
strictly positive (`0 < -3 * dMod211 q`, `0 < dMod1111 q`, `0 < sRow3GPMT_H4 q 4`). -/
theorem sRow3GPMT_H4_four_both_terms_pos [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq : 0 < q) :
    0 < -3 * dMod211 q ∧
    0 < dMod1111 q ∧
    0 < sRow3GPMT_H4 q 4 := by
  have hd211 : dMod211 q < 0 := dMod211_neg_of_pos q hq
  have hd1111 : 0 < dMod1111 q := dMod1111_pos_of_pos q hq
  unfold sRow3GPMT_H4
  refine ⟨by linarith, hd1111, by linarith⟩

/-- Exact rational closed form of the per-partition GPMT-weighted `A = 4` stratum:
`sRow3GPMT_H4 q 4 = q^3 (3 q^8 + 6 q^6 + 10 q^4 + 6 q^2 + 3) / ((q^2 + 1)^3 (q^4 + 1) (q^4 + q^2 + 1))`. -/
theorem sRow3GPMT_H4_four_closed_form (q : R) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq41 : q ^ 4 + 1 ≠ 0) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    sRow3GPMT_H4 q 4 =
      q ^ 3 * (3 * q ^ 8 + 6 * q ^ 6 + 10 * q ^ 4 + 6 * q ^ 2 + 3) /
        ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  have hden : h4ModDenom q ≠ 0 := h4ModDenom_ne_zero q hq2 hq41 hq421
  unfold sRow3GPMT_H4
  rw [dMod211_over_h4ModDenom q hq421, dMod1111_over_h4ModDenom q]
  change
    -3 * (-q ^ 3 * (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / h4ModDenom q) +
      q ^ 7 / h4ModDenom q =
    q ^ 3 * (3 * q ^ 8 + 6 * q ^ 6 + 10 * q ^ 4 + 6 * q ^ 2 + 3) / h4ModDenom q
  field_simp [hden]
  ring

/-- Exact rational closed form of the per-partition GPMT-weighted 4-body Mayer cumulant:
`mu4GPMT_H4 q = -q^3 (q^8 + 2 q^6 - 2 q^4 + 2 q^2 + 1) / ((q^2 + 1)^3 (q^4 + 1) (q^4 + q^2 + 1))`. -/
theorem mu4GPMT_H4_closed_form (q : R) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq41 : q ^ 4 + 1 ≠ 0) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    mu4GPMT_H4 q =
      -q ^ 3 * (q ^ 8 + 2 * q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 + 1) /
        ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  have hden : h4ModDenom q ≠ 0 := h4ModDenom_ne_zero q hq2 hq41 hq421
  rcases mu2_mu3_H4_eq_bridge q with ⟨h2, h3, _⟩
  unfold mu4GPMT_H4
  rw [sRow3GPMT_H4_four_closed_form q hq2 hq41 hq421, h2, h3, dMod111_over_h4ModDenom q hq2 hq41]
  change
    q ^ 3 * (3 * q ^ 8 + 6 * q ^ 6 + 10 * q ^ 4 + 6 * q ^ 2 + 3) / h4ModDenom q -
      6 * 0 - 4 * (-(-q ^ 3 * ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1)) / h4ModDenom q)) =
    -q ^ 3 * (q ^ 8 + 2 * q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 + 1) / h4ModDenom q
  field_simp [hden]
  ring

/-- Sum-of-squares decomposition of the octic numerator polynomial
`q^8 + 2 q^6 - 2 q^4 + 2 q^2 + 1 = (q^4 - 1)^2 + 2 q^6 + 2 q^2`. -/
theorem octic_numerator_eq_sum_of_squares (q : R) :
    q ^ 8 + 2 * q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 + 1 =
      (q ^ 4 - 1) ^ 2 + 2 * q ^ 6 + 2 * q ^ 2 := by
  ring

/-- Strict positivity of `q^8 + 2 q^6 - 2 q^4 + 2 q^2 + 1` for all `q > 0`. -/
theorem octic_numerator_pos_of_pos [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq : 0 < q) :
    0 < q ^ 8 + 2 * q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 + 1 := by
  rw [octic_numerator_eq_sum_of_squares q]
  have h1 : 0 ≤ (q ^ 4 - 1) ^ 2 := sq_nonneg (q ^ 4 - 1)
  have h2 : 0 < 2 * q ^ 6 := mul_pos zero_lt_two (pow_pos hq 6)
  have h3 : 0 < 2 * q ^ 2 := mul_pos zero_lt_two (pow_pos hq 2)
  linarith

/-- **Strict Negativity of the Per-Partition GPMT 4-Body Mayer Cumulant `mu4GPMT_H4`**:
For every `q > 0`, `mu4GPMT_H4 q < 0`, so the per-partition `H_4(q)` GPMT modified-dimension
weighting preserves the physical `(μ₂ = 0, μ₃ > 0, μ₄ < 0)` nuclear binding sign window. -/
theorem mu4GPMT_H4_neg_of_pos [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq : 0 < q) :
    mu4GPMT_H4 q < 0 := by
  have hq2 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  have hq41 : q ^ 4 + 1 ≠ 0 := ne_of_gt (pow_four_add_one_pos q)
  have hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt (pow_four_add_sq_add_one_pos q)
  rw [mu4GPMT_H4_closed_form q hq2 hq41 hq421, neg_mul, neg_div]
  apply neg_neg_of_pos
  apply div_pos
  · exact mul_pos (pow_pos hq 3) (octic_numerator_pos_of_pos q hq)
  · exact mul_pos
      (mul_pos (pow_pos (sq_add_one_pos q) 3) (pow_four_add_one_pos q))
      (pow_four_add_sq_add_one_pos q)

/-- **Combined Sign-Window Theorem for the Per-Partition `H_3(q)` / `H_4(q)` GPMT Cumulants**:
For all `q > 0`, `mu2GPMT_H4 q = 0`, `0 < mu3GPMT_H4 q`, and `mu4GPMT_H4 q < 0`. -/
theorem h4_gpmt_cumulant_sign_window [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq : 0 < q) :
    mu2GPMT_H4 q = 0 ∧
    0 < mu3GPMT_H4 q ∧
    mu4GPMT_H4 q < 0 := by
  rcases mu2_mu3_H4_eq_bridge q with ⟨h2, h3, _⟩
  have hd111 : dMod111 q < 0 := dMod111_neg_of_pos q hq
  refine ⟨h2, by linarith, mu4GPMT_H4_neg_of_pos q hq⟩

end PerPartitionGPMTCumulants

end H4GPMTModifiedDimensionCumulants
end QOU.MassTheory
