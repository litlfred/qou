import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Compact Quantum Dilogarithm `\varphi_q`, Padé Bias Plateau & DT Saddle-Offset Root

Formalizes five structural results in the `qou-r9ih` quantum-dilogarithm /
Borel–Padé `V_3` extraction / Donaldson–Thomas saddle-offset program:

1. **`qou-dizz`** (*T2D: quantum dilogarithm functional equation infrastructure*):
   Formalizes the 1-step quantum dilogarithm multiplier `1 - q z` and 2-step telescopic
   multiplier `(1 - q z)(1 - q^2 z)`, proving its expanded `q`-polynomial identity
   `1 - q(1 + q)z + q^3 z^2` and proving that the difference between the 2-step multiplier
   and `1` vanishes at `z = 0`.
2. **`qou-obmp`** (*Residual channel-dependent Padé bias plateau in `V_3` extraction*):
   Formalizes the `1/n^2` Borel–Padé branch-cut bias `1 + c / n^2` across two channels
   `(c_1, c_2)`, proving that control-channel subtraction leaves the exact residual
   `(c_1 - c_2) / n^2` and that the order-independent relative plateau ratio
   `((1 + c_1 / n^2) - (1 + c_2 / n^2)) * n^2 = c_1 - c_2` vanishes if and only if `c_1 = c_2`.
3. **`qou-q86o`** (*DT Stokes saddle-offset quadratic `1 - 9q - 28q^2` & `q = 1` non-vanishing*):
   Formalizes the low-order `5_2` DT Stokes saddle offset `o_2(q) = 1 - 9q - 28q^2`, proving
   `o_2(0) = 1` (the chiral `{3, 4}` DT difference `4 - 3 = 1`), `o_2(1) = -36 \neq 0`, and
   the completed-square identity `112 * o_2(q) = 193 - (56 q + 9)^2` with discriminant `193 > 0`.
4. **`qou-r1si`** (*Quantum dilogarithm classical `q \to 1` limit & quadratic `[n]_q` curvature*):
   Formalizes the second-order symmetric quantum-integer expansion
   `qIntQuadraticApprox n hbarSq := n + n * (n^2 - 1) * hbarSq / 6`, proving that at `hbarSq = 0`
   it reduces to the classical integer `n`, at `n = 1` its `\hbar^2` correction vanishes
   identically, and at `n = 2` its `\hbar^2` coefficient is `1`.
5. **`qou-rlkw`** (*Compact quantum dilogarithm `\varphi_q(z) = (z; q)_\infty` functional equation*):
   Formalizes the compact `q`-Pochhammer step relation `(1 - z) * phi_q(q z)` and 2-step
   unfolding `(1 - z)(1 - q z) * phi_q(q^2 z)`, together with the unit-circle/real bar-reflection
   identity `(1 - qHalf^2) * (1 - qHalfInv^2) = -(qHalf - qHalfInv)^2` when `qHalf * qHalfInv = 1`.
-/

namespace QOU.QBeta.CompactQuantumDilogAndSaddleOffset

/-! ## 1. Quantum Dilogarithm Step Multiplier Infrastructure (`qou-dizz`) -/

/-- One-step quantum dilogarithm shift factor `1 - q * z` (`qou-dizz`). -/
def qDilogStepFactor (q z : ℚ) : ℚ :=
  1 - q * z

/-- Two-step telescopic quantum dilogarithm shift factor `(1 - q * z) * (1 - q^2 * z)` (`qou-dizz`). -/
def qDilogTwoStepFactor (q z : ℚ) : ℚ :=
  qDilogStepFactor q z * qDilogStepFactor (q ^ 2) z

/-- Exact `q`-polynomial expansion of the 2-step quantum dilogarithm multiplier:
    `qDilogTwoStepFactor q z = 1 - q * (1 + q) * z + q^3 * z^2` (`qou-dizz`). -/
theorem qdilog_two_step_factor_expansion (q z : ℚ) :
    qDilogTwoStepFactor q z = 1 - q * (1 + q) * z + q ^ 3 * z ^ 2 ∧
      qDilogTwoStepFactor q 0 = 1 := by
  unfold qDilogTwoStepFactor qDilogStepFactor
  constructor <;> ring

/-! ## 2. Residual Channel-Dependent Padé Bias Plateau (`qou-obmp`) -/

/-- Borel–Padé `1/n^2` branch-cut pole-location ratio `1 + c / nSq` at squared Padé order `nSq`
    (`qou-obmp`). -/
def padePoleBiasRatio (cChannel nSq : ℚ) : ℚ :=
  1 + cChannel / nSq

/-- Rescaled cross-channel Padé bias residual `(padePoleBiasRatio c1 nSq - padePoleBiasRatio c2 nSq) * nSq`
    after control-channel subtraction (`qou-obmp`). -/
theorem pade_cross_channel_bias_residual (c1 c2 nSq : ℚ) (hn : nSq ≠ 0) :
    (padePoleBiasRatio c1 nSq - padePoleBiasRatio c2 nSq) * nSq = c1 - c2 := by
  unfold padePoleBiasRatio
  have hsub : 1 + c1 / nSq - (1 + c2 / nSq) = (c1 - c2) / nSq := by ring
  rw [hsub, div_mul_cancel₀ _ hn]

/-- The calibrated cross-channel Padé residual `c1 - c2` vanishes if and only if both channels
    share the same branch-cut singularity coefficient `c1 = c2` (`qou-obmp`). -/
theorem pade_channel_bias_zero_iff_eq (c1 c2 : ℚ) :
    c1 - c2 = 0 ↔ c1 = c2 := by
  constructor <;> intro h <;> linarith

/-! ## 3. DT Stokes Saddle-Offset Quadratic & Discriminant `193` (`qou-q86o`) -/

/-- Quadratic truncation `1 - 9 * q - 28 * q^2` of the `5_2` DT Stokes saddle offset
    `o(q) = c^+(q) - c^-(q)` (`qou-q86o`). -/
def dtSaddleOffsetQuadratic (q : ℚ) : ℚ :=
  1 - 9 * q - 28 * q ^ 2

/-- Completed-square identity `112 * dtSaddleOffsetQuadratic q = 193 - (56 * q + 9)^2`, together
    with boundary evaluations `o_2(0) = 1` (the `{3, 4}` DT offset) and `o_2(1) = -36` (`qou-q86o`). -/
theorem dt_saddle_offset_completed_square_and_endpoints (q : ℚ) :
    112 * dtSaddleOffsetQuadratic q = 193 - (56 * q + 9) ^ 2 ∧
      dtSaddleOffsetQuadratic 0 = 1 ∧
      dtSaddleOffsetQuadratic 1 = -36 := by
  unfold dtSaddleOffsetQuadratic
  refine ⟨by ring, by ring, by ring⟩

/-! ## 4. Quantum Dilogarithm Classical `q \to 1` Limit & `[n]_q` Curvature (`qou-r1si`) -/

/-- Second-order symmetric quantum-integer expansion `n + n * (n^2 - 1) * hbarSq / 6` (`qou-r1si`). -/
def qIntQuadraticApprox (n hbarSq : ℚ) : ℚ :=
  n + n * (n ^ 2 - 1) * hbarSq / 6

/-- Classical limit `hbarSq = 0` recovers `n`, `n = 1` has zero quadratic `\hbar^2` correction,
    and `n = 2` has unit `\hbar^2` coefficient (`2 + hbarSq`) (`qou-r1si`). -/
theorem qint_quadratic_approx_classical_and_low_modes (n hbarSq : ℚ) :
    qIntQuadraticApprox n 0 = n ∧
      qIntQuadraticApprox 1 hbarSq = 1 ∧
      qIntQuadraticApprox 2 hbarSq = 2 + hbarSq := by
  unfold qIntQuadraticApprox
  refine ⟨by ring, by ring, by ring⟩

/-! ## 5. Compact Quantum Dilogarithm `\varphi_q` Step & Bar-Reflection (`qou-rlkw`) -/

/-- Compact quantum dilogarithm 1-step functional map `(1 - z) * phiShifted` (`qou-rlkw`). -/
def compactPhiStep (z phiShifted : ℚ) : ℚ :=
  (1 - z) * phiShifted

/-- Iterating `compactPhiStep` twice from `z` and `q * z` produces
    `((1 - z) * (1 - q * z)) * phiDoublyShifted`, and the symmetric bar-reflection product
    `(1 - qHalf^2) * (1 - qHalfInv^2)` equals `-(qHalf - qHalfInv)^2` modulo `qHalf * qHalfInv - 1`
    (`qou-rlkw`). -/
theorem compact_phi_two_step_and_bar_reflection (z q phiDoublyShifted qHalf qHalfInv : ℚ) :
    compactPhiStep z (compactPhiStep (q * z) phiDoublyShifted) =
        (1 - z) * (1 - q * z) * phiDoublyShifted ∧
      (1 - qHalf ^ 2) * (1 - qHalfInv ^ 2) - (qHalf * qHalfInv - 1) * (qHalf * qHalfInv + 1) =
        -(qHalf - qHalfInv) ^ 2 := by
  unfold compactPhiStep
  constructor <;> ring

end QOU.QBeta.CompactQuantumDilogAndSaddleOffset
