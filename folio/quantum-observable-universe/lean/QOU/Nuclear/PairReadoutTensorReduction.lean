import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import HeckeTemperleyLieb.QCasimirPairGenericQ

/-!
# The two-block q-Casimir readout reduces to per-block traces

Audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §33. `QCasimirPairGenericQ` states its
pair readout through per-block data `a`, `c`. This file proves that reduction for the actual
two-block operator, over any field and any finite block spaces.

Each block carries matrices `e, f, K, K⁻¹` (on `α` for block A, on `β` for block B), a core `W`, and
a charge-sector projector `P` with: `P² = P`; `P` commutes with `K`, `K⁻¹`, `W`; `K·P = k·P` and
`K⁻¹·P = k⁻¹·P` (the sector has one K-value); and `P e P = 0`, `P f P = 0` (`e`, `f` move charge).
The pair operator is `X = h²·Δf·Δe + q K_AK_B + q⁻¹K_A⁻¹K_B⁻¹ − C_A ⊗ 1 − 1 ⊗ C_B` with the
`Ř`-compatible coproduct `Δe = e ⊗ K + 1 ⊗ e`, `Δf = f ⊗ 1 + K⁻¹ ⊗ f`, and
`C = h²·fe + qK + q⁻¹K⁻¹` on each block. The readout is the trace of `(P_A ⊗ P_B)(K_A ⊗ K_B)(W_A ⊗ W_B)·X`.

`readout_eq_pairReadout`: that trace equals `QCasimirPairGenericQ.pairReadout` with
`a = tr(P K W)` and `c = h²·tr(P K W f e)` on each block. The charge-moving terms `f_A ⊗ e_B` and
`K_A⁻¹e_A ⊗ f_B K_B` drop out by the sector conditions. No empirical input.
-/

namespace QOU.QBeta.PairReadoutTensorReduction

open Matrix Kronecker

variable {R : Type*} [Field R]

section Block

variable {α : Type*} [Fintype α]

/-- The sector conditions on one block. -/
structure Sector (e f K Ki W P : Matrix α α R) (k : R) : Prop where
  idem : P * P = P
  commK : P * K = K * P
  commKi : P * Ki = Ki * P
  commW : P * W = W * P
  eigK : K * P = k • P
  eigKi : Ki * P = k⁻¹ • P
  shiftE : P * e * P = 0
  shiftF : P * f * P = 0

variable {e f K Ki W P : Matrix α α R} {k : R}

/-- A charge-moving `Y` (`P Y P = 0`) has zero weighted trace. -/
theorem trace_shift (S : Sector e f K Ki W P k) {Y : Matrix α α R} (hY : P * Y * P = 0) :
    (P * K * W * Y).trace = 0 := by
  have hN : P * (K * W) = (K * W) * P := by
    rw [← Matrix.mul_assoc, S.commK, Matrix.mul_assoc, S.commW, Matrix.mul_assoc]
  calc (P * K * W * Y).trace = (P * P * (K * W) * Y).trace := by
          rw [S.idem, Matrix.mul_assoc P K W]
    _ = (P * ((K * W) * P * Y)).trace := by
          rw [Matrix.mul_assoc P P, hN]; simp only [Matrix.mul_assoc]
    _ = ((K * W) * (P * Y * P)).trace := by
          rw [Matrix.trace_mul_comm]; simp only [Matrix.mul_assoc]
    _ = 0 := by rw [hY, Matrix.mul_zero, Matrix.trace_zero]

/-- Right multiplication by a K-scalar: `tr(P K W K) = k·tr(P K W)`. -/
theorem trace_mulK (S : Sector e f K Ki W P k) : (P * K * W * K).trace = k * (P * K * W).trace := by
  have hPK : P * K = k • P := by rw [S.commK, S.eigK]
  rw [Matrix.trace_mul_comm, ← Matrix.mul_assoc, ← Matrix.mul_assoc, ← S.commK, hPK,
    Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul, ← hPK]

theorem trace_mulKi (S : Sector e f K Ki W P k) :
    (P * K * W * Ki).trace = k⁻¹ * (P * K * W).trace := by
  have hPK : P * Ki = k⁻¹ • P := by rw [S.commKi, S.eigKi]
  have hKP : P * K = K * P := S.commK
  rw [Matrix.trace_mul_comm, ← Matrix.mul_assoc, ← Matrix.mul_assoc, ← S.commKi, hPK,
    Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul]

omit [Field R] in
theorem shift_mul_left {P Y Z : Matrix α α R} [CommRing R] (hY : P * Y * P = 0) (hZ : P * Z = Z * P) :
    P * (Z * Y) * P = 0 := by
  rw [← Matrix.mul_assoc, hZ, Matrix.mul_assoc Z, Matrix.mul_assoc Z, hY, Matrix.mul_zero]

omit [Field R] in
theorem shift_mul_right {P Y Z : Matrix α α R} [CommRing R] (hY : P * Y * P = 0)
    (hZ : P * Z = Z * P) : P * (Y * Z) * P = 0 := by
  rw [Matrix.mul_assoc, Matrix.mul_assoc, ← hZ, ← Matrix.mul_assoc Y, ← Matrix.mul_assoc P,
    ← Matrix.mul_assoc P, hY, Matrix.zero_mul]

end Block

variable {α β : Type*} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β]

/-- Block Casimir `h²·fe + qK + q⁻¹K⁻¹`. -/
def blockCas {ι : Type*} [Fintype ι] [DecidableEq ι] (q h : R) (e f K Ki : Matrix ι ι R) :
    Matrix ι ι R :=
  h ^ 2 • (f * e) + q • K + q⁻¹ • Ki

/-- The pair operator `h²C_AB − h²C_A − h²C_B` with the `Ř`-compatible coproduct. -/
def pairX (q h : R) (eA fA KA KAi : Matrix α α R) (eB fB KB KBi : Matrix β β R) :
    Matrix (α × β) (α × β) R :=
  h ^ 2 • ((fA ⊗ₖ 1 + KAi ⊗ₖ fB) * (eA ⊗ₖ KB + 1 ⊗ₖ eB))
    + q • (KA ⊗ₖ KB) + q⁻¹ • (KAi ⊗ₖ KBi)
    - blockCas q h eA fA KA KAi ⊗ₖ 1 - 1 ⊗ₖ blockCas q h eB fB KB KBi

/-- The two-block readout equals the per-block `pairReadout`. -/
theorem readout_eq_pairReadout (q h kA kB : R)
    {eA fA KA KAi WA PA : Matrix α α R} {eB fB KB KBi WB PB : Matrix β β R}
    (SA : Sector eA fA KA KAi WA PA kA) (SB : Sector eB fB KB KBi WB PB kB) :
    (((PA * KA * WA) ⊗ₖ (PB * KB * WB)) * pairX q h eA fA KA KAi eB fB KB KBi).trace
      = QCasimirPairGenericQ.pairReadout q (PA * KA * WA).trace (PB * KB * WB).trace
          (h ^ 2 * (PA * KA * WA * (fA * eA)).trace) (h ^ 2 * (PB * KB * WB * (fB * eB)).trace)
          kA kB := by
  have zfA := trace_shift SA SA.shiftF
  have zeA := trace_shift SA (shift_mul_left SA.shiftE SA.commKi)
  have zeB := trace_shift SB SB.shiftE
  have zfB := trace_shift SB (shift_mul_right SB.shiftF SB.commK)
  have kA1 := trace_mulK SA
  have kAi := trace_mulKi SA
  have kB1 := trace_mulK SB
  have kBi := trace_mulKi SB
  simp only [pairX, blockCas, Matrix.add_mul, Matrix.mul_add, Matrix.mul_sub, Matrix.mul_smul,
    ← Matrix.mul_kronecker_mul, Matrix.mul_one, Matrix.one_mul, Matrix.add_kronecker,
    Matrix.kronecker_add, Matrix.smul_kronecker, Matrix.kronecker_smul, Matrix.trace_add,
    Matrix.trace_sub, Matrix.trace_smul, smul_eq_mul, Matrix.trace_kronecker]
  simp only [← Matrix.mul_assoc] at zfA zeA zeB zfB ⊢
  rw [zfA, zeA, zeB, zfB, kA1, kAi, kB1, kBi]
  unfold QCasimirPairGenericQ.pairReadout
  ring

end QOU.QBeta.PairReadoutTensorReduction
