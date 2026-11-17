import Mathlib.Tactic

/-!
# Wedderburn Mass Splitting and q-Deformation Asymmetry Roast (`qou-q6pp`, `qou-q7ga`)

This module formalizes two nuclear-binding algebraic results under `qou-v2om`:

1. **Wedderburn atomic mass decomposition and isobaric `A = 1` difference (`qou-q6pp`)**:
   In `m(Z, N) = Z m_p + N m_n + Z m_e + α (Φ₁ - 2[3]_q Φ₂ + h_A² Φ₃)`, the nucleon
   mass difference `m_n - m_p` enters as the leading input term while `α (Φ₁ - ...)` is
   the binding correction; because `Φ₂` is `p/n`-identical, it cancels in the `A = 1`
   difference. Furthermore, the atomic Hecke algebra `H_{A+Z}(q)` has `A + Z - 1`
   generators (`1, 2, 3, 5` for `¹H, D, T, ⁴He`), and the chirality integer weight rule
   `w(Z, N) = 4Z` (`N = 0`) / `6Z` (`N ≥ 1`) yields `(4, 6, 6, 12, 12)` across
   `(¹H, D, T, ³He, ⁴He)`.

2. **First-order `q`-deformation asymmetry and exact pure-crossing ratio (`qou-q7ga`)**:
   Expanding the bond factors in `e = q - 1` around `z(1) = 1/2` gives
   `b_pp = 1/2 + e`, `b_pn = 1/2`, `b_nn = 1/2 - e`, so the linear deformation in a
   chain of `(Z - 1)` `pp` bonds, `1` `pn` bond, and `(N - 1)` `nn` bonds is
   `+2 e (N - Z)`, whereas bar-swapping `e ↦ -e` reverses the sign to `-2 e (N - Z)`.
   In exact loop-normalised form, `b_pp(q) = q² / (q + 1/q)` and
   `b_nn(q) = q⁻² / (q + 1/q)` satisfy `b_pp(q) / b_nn(q) = q⁴` and
   `b_pp(q) · b_nn(q) = 1 / (q + 1/q)²`.
-/

namespace QOU.MassTheory

/-- Wedderburn atomic mass formula `Z m_p + N m_n + Z m_e + α (Φ₁ - q3_2 Φ₂ + h_sq Φ₃)`. -/
def wedderburnAtomMass
    (Z N m_p m_n m_e alpha Phi_1 q3_2 Phi_2 h_sq Phi_3 : ℚ) : ℚ :=
  Z * m_p + N * m_n + Z * m_e + alpha * (Phi_1 - q3_2 * Phi_2 + h_sq * Phi_3)

/-- In the `A = 1` difference between `(Z=0, N=1)` and `(Z=1, N=0)`, `(m_n - m_p - m_e)`
is the leading input term, the shared `Φ₂` term cancels identically, and the binding
correction contributes `α ((Φ₁(n) - Φ₁(p)) + h² (Φ₃(n) - Φ₃(p)))` (`qou-q6pp`). -/
theorem wedderburn_isobaric_pn_diff_separates_leading_and_correction
    (m_p m_n m_e alpha Phi_1_p Phi_1_n q3_2 Phi_2 h_sq Phi_3_p Phi_3_n : ℚ) :
    wedderburnAtomMass 0 1 m_p m_n m_e alpha Phi_1_n q3_2 Phi_2 h_sq Phi_3_n -
      wedderburnAtomMass 1 0 m_p m_n m_e alpha Phi_1_p q3_2 Phi_2 h_sq Phi_3_p =
      (m_n - m_p - m_e) +
        alpha * ((Phi_1_n - Phi_1_p) + h_sq * (Phi_3_n - Phi_3_p)) := by
  unfold wedderburnAtomMass
  ring

/-- Number of braid generators `A + Z - 1` of the atomic Hecke algebra `H_{A+Z}(q)` (`qou-q6pp`). -/
def atomicGeneratorCount (A Z : ℕ) : ℕ :=
  A + Z - 1

/-- Integer chirality weight `w(Z, N)` in units of `h² ln q`: `4Z` at `N = 0` and `6Z` for `N ≥ 1` (`qou-q6pp`). -/
def chiralityWeightRule (Z N : ℕ) : ℕ :=
  if N = 0 then 4 * Z else 6 * Z

/-- Exact generator counts `(1, 2, 3, 5)` for `(¹H, D, T, ⁴He)` and quantized chirality
weights `(4, 6, 6, 12, 12)` across `(¹H, D, T, ³He, ⁴He)` (`qou-q6pp`). -/
theorem atomic_generator_and_chirality_weight_table :
    atomicGeneratorCount 1 1 = 1 ∧
    atomicGeneratorCount 2 1 = 2 ∧
    atomicGeneratorCount 3 1 = 3 ∧
    atomicGeneratorCount 4 2 = 5 ∧
    chiralityWeightRule 1 0 = 4 ∧
    chiralityWeightRule 1 1 = 6 ∧
    chiralityWeightRule 1 2 = 6 ∧
    chiralityWeightRule 2 1 = 12 ∧
    chiralityWeightRule 2 2 = 12 := by
  decide

/-- First-order `pp` bond factor `1/2 + e` in `e = q - 1` (`qou-q7ga`). -/
def b_pp_firstOrder (e : ℚ) : ℚ := 1 / 2 + e

/-- First-order `pn` bond factor `1/2` in `e = q - 1` (`qou-q7ga`). -/
def b_pn_firstOrder : ℚ := 1 / 2

/-- First-order `nn` bond factor `1/2 - e` in `e = q - 1` (`qou-q7ga`). -/
def b_nn_firstOrder (e : ℚ) : ℚ := 1 / 2 - e

/-- Linear deformation contribution `(Z - 1)(-2e) + (N - 1)(2e)` of the chain law (`qou-q7ga`). -/
def chainDeformationLinear (e Z N : ℚ) : ℚ :=
  (Z - 1) * (-2 * e) + (N - 1) * (2 * e)

/-- The first-order like-species bonds average to `b_pn = 1/2`, differ by `2e`, and produce
net chain asymmetry `+2e(N - Z)` that flips sign under bar swap `e ↦ -e` (`qou-q7ga`). -/
theorem firstOrder_bonds_and_asymmetry_sign (e Z N : ℚ) :
    b_pp_firstOrder e + b_nn_firstOrder e = 2 * b_pn_firstOrder ∧
    b_pp_firstOrder e - b_nn_firstOrder e = 2 * e ∧
    chainDeformationLinear e Z N = 2 * e * (N - Z) ∧
    chainDeformationLinear (-e) Z N = -(2 * e * (N - Z)) := by
  unfold b_pp_firstOrder b_pn_firstOrder b_nn_firstOrder chainDeformationLinear
  refine ⟨by ring, by ring, by ring, by ring⟩

/-- Loop-normalised pure-crossing `pp` bond `q² / (q + 1/q)` (`qou-q7ga`). -/
def pureCrossingBondPP (q : ℚ) : ℚ :=
  q ^ 2 / (q + 1 / q)

/-- Loop-normalised pure-crossing `nn` bond `q⁻² / (q + 1/q)` (`qou-q7ga`). -/
def pureCrossingBondNN (q : ℚ) : ℚ :=
  (1 / q ^ 2) / (q + 1 / q)

/-- Exact ratio `b_pp / b_nn = q⁴` and product `b_pp · b_nn = 1 / [2]_q²` for the
loop-normalised pure-crossing bonds (`qou-q7ga`). -/
theorem pureCrossing_ratio_and_product (q : ℚ) (hq : q ≠ 0) (hd : q + 1 / q ≠ 0) :
    pureCrossingBondPP q / pureCrossingBondNN q = q ^ 4 ∧
    pureCrossingBondPP q * pureCrossingBondNN q = 1 / (q + 1 / q) ^ 2 := by
  unfold pureCrossingBondPP pureCrossingBondNN
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  constructor
  · field_simp [hq, hq2, hd]
  · field_simp [hq, hq2, hd]

end QOU.MassTheory
