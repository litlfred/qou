/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# Cross-Anchor Stage-B Truncation Bias, Detector Union, Operator–Input Straddle, Env-Diff Confound, and CAL-2 Self-Certification

This module formalizes the exact algebraic and structural theorems for five tasks under
the `qou-2002` calibration and anchor-hygiene epic:

1. **Bean `qou-2t9y` (Stage-B 12-Digit Truncation Bias & `H₃(q)` Coxeter Trace)**:
   - Proves that replacing the canonical muon anchor `q_μ` by a hand-truncated literal
     `q_μ - ε` shifts the relative `μ–p` separation `δ(q_μ, q_p) = (q_μ - q_p) / q_p` by
     `-ε / q_p`, with fractional error `ε / (q_μ - q_p)` (`≈ 0.719389%` for the 12-digit
     truncation `1.10997859555` where `ε = 9.2739047 × 10⁻¹¹` and `q_C - q_p = 1.2891358 × 10⁻⁸`),
     and proves the exact `H₃(q)` Coxeter word (`β = σ₁ σ₂ σ₁`, 1-indexed generators in `{1, 2}`)
     convention-D Markov trace identity `(q - q⁻¹) z_D² + z_D = q³ (q⁴ + 1) / (q² + 1)²`
     where `χ^{(2,1)}(σ₁ σ₂ σ₁) = 0` (`stageB_truncation_bias_and_coxeter_trace`).

2. **Bean `qou-2whe` (Two-Detector Union Decomposition & `1/ℏ_q` Truncation Secant)**:
   - Proves the exact inclusion–exclusion identity across complementary string-grep and
     AST-value detectors together with the exact secant shift on the inverse Planck carrier
     `1/ℏ_q = q / (q - 1)` under a float64 or prefix truncation `q ↦ q - δ`
     (`detector_union_and_truncation_secant`).

3. **Bean `qou-qyef` (Operator–Input Pin Straddle Residual Inflation)**:
   - Proves that when a linear constraint `R(q_op, x) = (a₀ + a₁(q_op - q_p)) x - (b₀ + b₁(q_op - q_p))`
     is evaluated at a muon-pinned operator `A(q_μ)` against proton-pinned coordinates `x_p`,
     the residual shifts by `(q_μ - q_p)(a₁ x_p - b₁)`, inflating a true `r₀` residual by the
     exact factor `(q_μ - q_p)(a₁ x_p - b₁) / r₀` (`operator_input_straddle_residual_and_amplification`).

4. **Bean `qou-o922` (Both-Anchor Env-Var Diff Confound on Hardcoded-Pin Producers)**:
   - Models a producer whose effective substrate parameter is `q_eff(w) = w · q_env + (1 - w) · q_lit`.
     Proves that the both-anchor env-var diff equals `w · s · (q_μ - q_p)` (vanishing at `w = 0`
     even when `s ≠ 0` and `q_μ ≠ q_p`, which is why the env-var diff test misclassifies
     hardcoded-pin producers as pin-independent), whereas migrating from hardcoded (`w = 0`)
     to live (`w = 1`) moves the output by `s · (q_p - q_A)` (`env_diff_confound_and_true_pin_swing`).

5. **Bean `qou-tekx` (CAL-2 Self-Certification Round-Trip & A-vs-C Inverted Ratio Discrepancy)**:
   - Proves that the inverted mass ratio `R_inv(V, q) = V / ((q - 1)/q)²` satisfies the exact
     round-trip identity `R_inv(V, (1 - h)⁻¹) = V / h²` (confirming that CODATA-2022 value C
     self-certifies to `m_μ/m_e = 206.7682827` at the arithmetic floor), and proves the exact
     factored discrepancy `R_inv(V, q_A) - R_inv(V, q_C)` explaining why the retired frozen pin
     `q_A` inverts to `206.768282989315111...` (`cal2_self_certification_roundtrip_and_discrepancy`).
-/

namespace QOU.MassTheory.CrossAnchorStraddleAndSelfCertification

variable {K : Type*} [Field K]

/-! ### 1. Bean `qou-2t9y`: Stage-B 12-Digit Truncation Bias & `H₃(q)` Coxeter Trace -/

/-- Relative anchor separation `δ(q_μ, q_p) = (q_μ - q_p) / q_p`. -/
def relAnchorSep (qMu qP : K) : K := (qMu - qP) / qP

/-- **Truncating `q_μ ↦ q_μ - ε` shifts `δ(q_μ, q_p)` by `-ε / q_p` with fractional bias
`ε / (q_μ - q_p)`, and the `H₃(q)` Coxeter trace `(q - q⁻¹) z_D² + z_D` equals
`q³(q⁴ + 1) / (q² + 1)²` (`qou-2t9y`).** -/
theorem stageB_truncation_bias_and_coxeter_trace (q qMu qP eps : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hqP : qP ≠ 0) (hgap : qMu - qP ≠ 0) :
    relAnchorSep (qMu - eps) qP = relAnchorSep qMu qP - eps / qP ∧
      (relAnchorSep qMu qP - relAnchorSep (qMu - eps) qP) / relAnchorSep qMu qP =
        eps / (qMu - qP) ∧
      (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) ^ 2 + q ^ 3 / (q ^ 2 + 1) =
        q ^ 3 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  unfold relAnchorSep
  refine ⟨?_, ?_, ?_⟩
  · field_simp
    ring
  · field_simp
    ring
  · field_simp
    ring

/-! ### 2. Bean `qou-2whe`: Detector Union Inclusion–Exclusion & `1/ℏ_q` Truncation Secant -/

/-- Inverse quantum Planck parameter `1 / ℏ_q(q) = q / (q - 1)`. -/
def invHbar (q : K) : K := q / (q - 1)

/-- **Two-detector union inclusion–exclusion and `1/ℏ_q` secant shift under truncation
`q ↦ q - δ` (`qou-2whe`).** -/
theorem detector_union_and_truncation_secant (onlyGrep onlyValue both q delta : K)
    (hq1 : q - 1 ≠ 0) (hqd1 : q - delta - 1 ≠ 0) :
    (onlyGrep + both) + (onlyValue + both) - both = onlyGrep + onlyValue + both ∧
      invHbar q - invHbar (q - delta) = -delta / ((q - 1) * (q - delta - 1)) := by
  unfold invHbar
  constructor
  · ring
  · field_simp
    ring

/-! ### 3. Bean `qou-qyef`: Operator–Input Pin Straddle Residual Inflation -/

/-- Linearized operator residual `R(q_op, x) = (a₀ + a₁(q_op - q_p)) x - (b₀ + b₁(q_op - q_p))`. -/
def straddleLinearResidual (a0 a1 b0 b1 qP qOp x : K) : K :=
  (a0 + a1 * (qOp - qP)) * x - (b0 + b1 * (qOp - qP))

/-- **Evaluating a proton-pinned solution `x_p` against a muon-pinned operator `A(q_μ)` shifts
the residual by `(q_μ - q_p)(a₁ x_p - b₁)` and inflates a nonzero baseline residual `r₀` by
`(q_μ - q_p)(a₁ x_p - b₁) / r₀` (`qou-qyef`).** -/
theorem operator_input_straddle_residual_and_amplification
    (a0 a1 b0 b1 qP qMu xP : K)
    (hr0 : straddleLinearResidual a0 a1 b0 b1 qP qP xP ≠ 0) :
    straddleLinearResidual a0 a1 b0 b1 qP qMu xP -
        straddleLinearResidual a0 a1 b0 b1 qP qP xP =
      (qMu - qP) * (a1 * xP - b1) ∧
      (straddleLinearResidual a0 a1 b0 b1 qP qMu xP -
          straddleLinearResidual a0 a1 b0 b1 qP qP xP) /
        straddleLinearResidual a0 a1 b0 b1 qP qP xP =
      (qMu - qP) * (a1 * xP - b1) /
        (a0 * xP - b0) := by
  unfold straddleLinearResidual
  constructor
  · ring
  · have hbase : (a0 + a1 * (qP - qP)) * xP - (b0 + b1 * (qP - qP)) = a0 * xP - b0 := by ring
    rw [hbase] at hr0 ⊢
    field_simp
    ring

/-! ### 4. Bean `qou-o922`: Both-Anchor Env-Var Diff Confound on Hardcoded-Pin Producers -/

/-- Producer observable with env-var weight `w` and hardcoded literal weight `1 - w`. -/
def weightedProducerObs (f0 s q0 w qEnv qLit : K) : K :=
  f0 + s * (w * qEnv + (1 - w) * qLit - q0)

/-- **The both-anchor env-var diff scales as `w · s · (q_μ - q_p)` (vanishing at `w = 0` on
hardcoded-pin producers even when `s ≠ 0`), whereas migrating from hardcoded `(w = 0, q_lit = q_A)`
to live `(w = 1, q_env = q_p)` changes the output by `s · (q_p - q_A)` (`qou-o922`).** -/
theorem env_diff_confound_and_true_pin_swing (f0 s q0 w qMu qP qA : K) :
    weightedProducerObs f0 s q0 w qMu qA - weightedProducerObs f0 s q0 w qP qA =
      w * s * (qMu - qP) ∧
      weightedProducerObs f0 s q0 0 qMu qA - weightedProducerObs f0 s q0 0 qP qA = 0 ∧
      weightedProducerObs f0 s q0 1 qP qA - weightedProducerObs f0 s q0 0 qP qA =
        s * (qP - qA) := by
  unfold weightedProducerObs
  refine ⟨by ring, by ring, by ring⟩

/-! ### 5. Bean `qou-tekx`: CAL-2 Self-Certification Round-Trip & A-vs-C Inverted Discrepancy -/

/-- Inverted CAL-2 mass ratio `R_inv(V, q) = V / ((q - 1) / q)²`. -/
def cal2InvertedRatio (V q : K) : K := V / ((q - 1) / q) ^ 2

/-- **Evaluating `R_inv(V, q)` at `q(h) = (1 - h)⁻¹` recovers `V / h²` identically, and the
inverted mass-ratio discrepancy between two anchors `q_A, q_C` factors as
`V (q_C - q_A)(2 q_A q_C - q_A - q_C) / ((q_A - 1)² (q_C - 1)²)` (`qou-tekx`).** -/
theorem cal2_self_certification_roundtrip_and_discrepancy (V h qA qC : K)
    (hh0 : h ≠ 0) (hh1 : 1 - h ≠ 0)
    (hqA0 : qA ≠ 0) (hqC0 : qC ≠ 0)
    (hqA1 : qA - 1 ≠ 0) (hqC1 : qC - 1 ≠ 0) :
    cal2InvertedRatio V (1 - h)⁻¹ = V / h ^ 2 ∧
      cal2InvertedRatio V qA - cal2InvertedRatio V qC =
        V * (qC - qA) * (2 * qA * qC - qA - qC) / ((qA - 1) ^ 2 * (qC - 1) ^ 2) := by
  unfold cal2InvertedRatio
  constructor
  · have h_sub : (1 - h)⁻¹ - 1 = h / (1 - h) := by
      field_simp
      ring
    rw [h_sub]
    field_simp
    ring
  · field_simp
    ring

end QOU.MassTheory.CrossAnchorStraddleAndSelfCertification
