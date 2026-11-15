import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import QOU.Archimedean.TransferMatrix

/-!
# QOU.Archimedean.beta_decay_transfer_matrix

Canonical Lean declaration for content block at
[`quantum-observable-universe/archimedean-universe/beta-decay-transfer-matrix.ts`](quantum-observable-universe/archimedean-universe/beta-decay-transfer-matrix.ts).

The `lean.ref` URI `qou:QOU.Archimedean.beta_decay_transfer_matrix`
resolves to `beta_decay_transfer_matrix` below.

The three crossing transfer matrices are *concrete* `2×2` matrices over
`ℝ`, so the manuscript sub-claims are **genuine computations** (pattern B):
the traces, the unimodularity `det T_pp = det T_nn = -1`, and the
universal-`Δ_β` identity `T_mix − T_nn = T_pp − T_mix` are all *derived*
from the explicit entries by `Matrix.trace_fin_two` / `Matrix.det_fin_two`
and `ring`, not projected from an opaque context field.
-/

-- Declarations here are nested one namespace deeper than `QOU.Archimedean`
-- so this module and `QOU.Archimedean.TransferMatrix` can be imported
-- together. Both declared `T_pp`, `T_nn` and `T_mix` at the same
-- fully-qualified names, and Lean rejects the second import with
-- "environment already contains" (bean `qou-kfcl`).
--
-- They are NOT rival definitions. `TransferMatrix.transferMatrix c d`
-- is `!![c * HA_t + d, c; c, d]` over `ℤ[t, t⁻¹]` with `HA_t = q - q⁻¹`;
-- `betaTransfer q c d` here is `!![c * (q - q⁻¹) + d, c; c, d]` over `ℝ`.
-- One formula, two ground rings — the symbolic one and its archimedean
-- specialisation, which is exactly the §7c layering. Consolidating them
-- onto a single generic `transferMatrix (q c d : R)` over `[CommRing R]`
-- is the right end state and is NOT done here; it changes the signature
-- of a declaration seven modules consume. Measured and left to `qou-u87j`.
namespace QOU.Archimedean.BetaDecayTransfer

open Matrix

/-- The crossing transfer matrix `T(c, d) = !![c·(q − q⁻¹) + d, c; c, d]`
    of the manuscript (a `2×2` matrix over `ℝ`). -/
noncomputable def betaTransfer (q c d : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  transferMatrixOf (q - q⁻¹) c d

/-- `T_pp(q) = T(1, 0) = !![q − q⁻¹, 1; 1, 0]`. -/
noncomputable def T_pp (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := betaTransfer q 1 0

/-- `T_nn(q) = T(1, −(q − q⁻¹)) = !![0, 1; 1, −(q − q⁻¹)]`. -/
noncomputable def T_nn (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  betaTransfer q 1 (-(q - q⁻¹))

/-- `T_mix(q) = T(1, −½(q − q⁻¹))`. -/
noncomputable def T_mix (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  betaTransfer q 1 (-(1 / 2) * (q - q⁻¹))

/-- Trace of `T_pp` is `q − q⁻¹` (derived). -/
theorem trace_T_pp (q : ℝ) : (T_pp q).trace = q - q⁻¹ := by
  simp [T_pp, betaTransfer, Matrix.trace_fin_two]

/-- Trace of `T_nn` is `−(q − q⁻¹)` (derived). -/
theorem trace_T_nn (q : ℝ) : (T_nn q).trace = -(q - q⁻¹) := by
  simp [T_nn, betaTransfer, Matrix.trace_fin_two]

/-- Trace of `T_mix` is `0` (derived). -/
theorem trace_T_mix (q : ℝ) : (T_mix q).trace = 0 := by
  simp [T_mix, betaTransfer, Matrix.trace_fin_two]; ring

/-- `det T_pp = −1` — Hecke unimodularity (derived). -/
theorem det_T_pp (q : ℝ) : (T_pp q).det = -1 := by
  simp [T_pp, betaTransfer, Matrix.det_fin_two]

/-- `det T_nn = −1` — Hecke unimodularity (derived). -/
theorem det_T_nn (q : ℝ) : (T_nn q).det = -1 := by
  simp [T_nn, betaTransfer, Matrix.det_fin_two]

/-- **Universal `Δ_β`** — the two elementary decay matrices coincide:
    `T_mix − T_nn = T_pp − T_mix` (derived entrywise). -/
theorem universal_delta_beta (q : ℝ) :
    T_mix q - T_nn q = T_pp q - T_mix q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [T_pp, T_nn, T_mix, betaTransfer, Matrix.sub_apply] <;> ring

/-- **Beta-decay transfer matrices** (manuscript claims (i)–(iii)).

Beta decay is mediated by the `T_{3,5}` torus knot, whose insertion at the
converting quark produces the universal `2×2` matrix-valued polynomial
`Δ_β(q)`.  The three crossing transfer matrices `T_pp`, `T_nn`, `T_mix`
satisfy:

* (i) `tr T_pp = q − q⁻¹`, `tr T_nn = −(q − q⁻¹)`, `tr T_mix = 0`;
* (ii) `det T_pp = det T_nn = −1` (Hecke unimodularity, forced by the
  eigenvalues `q · (−q⁻¹) = −1`);
* (iii) the two elementary decay matrices coincide,
  `T_mix − T_nn = T_pp − T_mix` (the single universal `Δ_β`).

All three are **derived** from the explicit entries — the lone input is
the substrate parameter `q : ℝ`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/beta-decay-transfer-matrix.ts
theorem beta_decay_transfer_matrix (q : ℝ) :
    ((T_pp q).trace = q - q⁻¹ ∧ (T_nn q).trace = -(q - q⁻¹) ∧
      (T_mix q).trace = 0) ∧
    ((T_pp q).det = -1 ∧ (T_nn q).det = -1) ∧
    (T_mix q - T_nn q = T_pp q - T_mix q) :=
  ⟨⟨trace_T_pp q, trace_T_nn q, trace_T_mix q⟩,
   ⟨det_T_pp q, det_T_nn q⟩,
   universal_delta_beta q⟩

end QOU.Archimedean.BetaDecayTransfer
