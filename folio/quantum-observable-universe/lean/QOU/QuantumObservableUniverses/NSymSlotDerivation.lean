import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.QuantumObservableUniverses.NSymSlotDerivation

What the Hoefsmit slot realisation (`thm:hoefsmit-ew-cell-content`) forces for
`𝒩_sym = tr_F(e_sym^EW · e_H)` of `conj:g-action-on-substrate`.
Audit: `docs/audits/2026-11-20-nsym-derivation.md`.
Compute twin: `computations/nsym_slot_trace_derivation.py`.

Each carrier acts on one strand pair `V ⊗ V`, `V` two-dimensional, through the
Hecke generator `S` (the `Ř`-matrix, eigenvalues `q` and `-q⁻¹`).  The pivotal
trace is `qtr x = trace (diag(q², 1, 1, q⁻²) * x)`.  Over a generic field `R`
(§7c), with `q ≠ 0` and `[2]_q = q + q⁻¹ ≠ 0`:

* `S_hecke`: `S² = (q - q⁻¹) S + 1`.
* `S_pow_mul_ep`, `S_pow_mul_em`: the sym/alt idempotents `e±` are the
  `q^n` / `(-q⁻¹)^n` eigenprojectors of every carrier `Sⁿ` (in particular of
  `σ⁴, σ⁶, σ⁸`), so the image does not depend on the carrier power.
* `qtr_one = [2]²`, `qtr_ep = [3]`, `qtr_em = 1`, `qtr_S = q³ + q`
  (`= z_D [2]²` with `z_D = q³/(q²+1)`, convention D).
* `em_eq_cup_cap`, `cap_cup`: `e⁻ = d · u wᵀ` with `w · u = [2]`: `e⁻` is the
  rank-one idempotent that factors through the unit, the shape (G-4) demands.
* `alt_eigvec_unique`: every `-q⁻¹`-eigenvector of `S` is a multiple of `u`,
  so on a `V ⊗ V` host the (G-3)/(G-4) idempotent is `e⁻` and nothing else.
* `qtr6_kron`: the pivotal trace on `V^{⊗6}` is multiplicative on Kronecker
  products of slot operators.
* `composite_eq_tensor`: on `V^{⊗6}` the composite `(e⁺⊗e⁺⊗1)(1⊗1⊗e⁻)` equals
  the tensor `e⁺⊗e⁺⊗e⁻`, so the composite/tensor alternative of
  `NSymTraceAlgebra` does not arise.
* `nsym_slot`: `qtr6 (e⁺ ⊗ e⁺ ⊗ e⁻) = [3]²`.

The physical identifications (carrier ↔ slot, `e_sym^EW` = sym channel of
the `W` and `Z` slots, `H` slot = `V ⊗ V`) are inputs, not proved here.
The anchor `213.11` is not used.
-/

namespace QOU.QuantumObservableUniverses.NSymSlotDerivation

open Matrix

variable {R : Type*} [Field R]

/-- `[2]_q = q + q⁻¹`. -/
def two (q : R) : R := q + q⁻¹

/-- Hecke generator (`Ř`-matrix) on `V ⊗ V`, basis `00, 01, 10, 11`. -/
def S (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0; 0, q - q⁻¹, 1, 0; 0, 1, 0, 0; 0, 0, 0, q]

/-- Symmetric (eigenvalue `q`) idempotent `e⁺ = (S + q⁻¹)/[2]`. -/
def ep (q : R) : Matrix (Fin 4) (Fin 4) R := (two q)⁻¹ • (S q + q⁻¹ • 1)

/-- Antisymmetric (eigenvalue `-q⁻¹`) idempotent `e⁻ = (q - S)/[2]`. -/
def em (q : R) : Matrix (Fin 4) (Fin 4) R := (two q)⁻¹ • (q • 1 - S q)

/-- Pivotal element `K ⊗ K`, `K = diag(q, q⁻¹)`. -/
def KK (q : R) : Matrix (Fin 4) (Fin 4) R :=
  Matrix.diagonal ![q * q, 1, 1, q⁻¹ * q⁻¹]

/-- Pivotal (quantum) trace on `V ⊗ V`. -/
def qtr (q : R) (x : Matrix (Fin 4) (Fin 4) R) : R := trace (KK q * x)

/-- Cup `u : 𝟙 → V ⊗ V` (the `q`-singlet). -/
def u (q : R) : Fin 4 → R := ![0, 1, -q, 0]

/-- Cap `w : V ⊗ V → 𝟙`. -/
def w (q : R) : Fin 4 → R := ![0, q⁻¹, -1, 0]

/-- `[2]_q ≠ 0` gives `1 + q² ≠ 0`. -/
theorem one_add_sq_ne_zero (q : R) (hq : q ≠ 0) (h2 : two q ≠ 0) : (1 : R) + q ^ 2 ≠ 0 := by
  intro h
  apply h2
  have e : two q = (1 + q ^ 2) / q := by unfold two; field_simp; ring
  rw [e, h, zero_div]

/-- `[2]_q⁻¹ = q/(1 + q²)`. -/
theorem two_inv (q : R) (hq : q ≠ 0) : (two q)⁻¹ = q / (1 + q ^ 2) := by
  have e : two q = (1 + q ^ 2) / q := by unfold two; field_simp; ring
  rw [e, inv_div]

section
variable (q : R) (hq : q ≠ 0)
include hq

theorem S_hecke : S q * S q = (q - q⁻¹) • S q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;>
    field_simp <;> ring

variable (h2 : two q ≠ 0)
include h2

theorem S_mul_ep : S q * ep q = q • ep q := by
  have h2' := one_add_sq_ne_zero q hq h2
  unfold two at h2
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [ep, two, S, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;>
    field_simp <;> ring

theorem S_mul_em : S q * em q = (-q⁻¹) • em q := by
  have h2' := one_add_sq_ne_zero q hq h2
  unfold two at h2
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [em, two, S, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;>
    field_simp <;> ring

/-- Every carrier `Sⁿ` (e.g. `σ⁴, σ⁶, σ⁸`) has `e⁺` as its `qⁿ`-eigenprojector. -/
theorem S_pow_mul_ep (n : ℕ) : S q ^ n * ep q = q ^ n • ep q := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ', Matrix.mul_assoc, ih, Matrix.mul_smul, S_mul_ep q hq h2,
      smul_smul, pow_succ]

/-- … and `e⁻` as its `(-q⁻¹)ⁿ`-eigenprojector. -/
theorem S_pow_mul_em (n : ℕ) : S q ^ n * em q = (-q⁻¹) ^ n • em q := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ', Matrix.mul_assoc, ih, Matrix.mul_smul, S_mul_em q hq h2,
      smul_smul, pow_succ]

theorem ep_add_em : ep q + em q = 1 := by
  have h2' := one_add_sq_ne_zero q hq h2
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [ep, em, two_inv q hq, S, Matrix.one_apply] <;> field_simp <;> ring

/-- `qtr e⁺ = q² + 1 + q⁻² = [3]_q`. -/
theorem qtr_ep : qtr q (ep q) = q ^ 2 + 1 + q⁻¹ ^ 2 := by
  have h2' := one_add_sq_ne_zero q hq h2
  simp [qtr, KK, ep, two_inv q hq, S, Matrix.trace, Fin.sum_univ_four, Matrix.diagonal_mul,
    Matrix.one_apply]
  field_simp
  ring

/-- `qtr e⁻ = 1`. -/
theorem qtr_em : qtr q (em q) = 1 := by
  have h2' := one_add_sq_ne_zero q hq h2
  simp [qtr, KK, em, two_inv q hq, S, Matrix.trace, Fin.sum_univ_four, Matrix.diagonal_mul,
    Matrix.one_apply]
  field_simp

/-- `e⁻ = [2]⁻¹ · u wᵀ`: the alt idempotent factors through the unit. -/
theorem em_eq_cup_cap : em q = (two q)⁻¹ • Matrix.vecMulVec (u q) (w q) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [em, S, u, w, Matrix.vecMulVec, Matrix.one_apply] <;> field_simp

end

section
variable (q : R) (hq : q ≠ 0)
include hq

theorem qtr_one : qtr q 1 = (q + q⁻¹) ^ 2 := by
  simp [qtr, KK, Matrix.trace, Fin.sum_univ_four]
  field_simp
  ring

/-- `qtr S = q³ + q`; with `z_D = q³/(q²+1)` this is `z_D [2]²` (convention D). -/
theorem qtr_S : qtr q (S q) = q ^ 3 + q := by
  simp [qtr, KK, S, Matrix.trace, Fin.sum_univ_four, Matrix.diagonal_mul]
  field_simp
  ring

/-- Convention D: `qtr S / qtr 1 = q³/(q²+1)`. -/
theorem qtr_S_div_qtr_one (hq2 : q ^ 2 + 1 ≠ 0) :
    qtr q (S q) / qtr q 1 = q ^ 3 / (q ^ 2 + 1) := by
  rw [qtr_S q hq, qtr_one q hq]
  field_simp

/-- `w · u = [2]_q`: the loop value. -/
theorem cap_cup : w q ⬝ᵥ u q = q + q⁻¹ := by
  simp [w, u, dotProduct, Fin.sum_univ_four]
  ring

/-- Uniqueness of the singlet: every `-q⁻¹`-eigenvector of `S` is `v 1 • u`
    (given `[2]_q ≠ 0`). -/
theorem alt_eigvec_unique (h2 : q + q⁻¹ ≠ 0) (v : Fin 4 → R)
    (hv : S q *ᵥ v = (-q⁻¹) • v) : v = v 1 • u q := by
  have e0 := congrFun hv 0
  have e2 := congrFun hv 2
  have e3 := congrFun hv 3
  simp [S, Matrix.mulVec, dotProduct, Fin.sum_univ_four] at e0 e2 e3
  have h0 : v 0 = 0 := by
    have : (q + q⁻¹) * v 0 = 0 := by linear_combination e0
    rcases mul_eq_zero.mp this with h | h
    · exact absurd h h2
    · exact h
  have h3 : v 3 = 0 := by
    have : (q + q⁻¹) * v 3 = 0 := by linear_combination e3
    rcases mul_eq_zero.mp this with h | h
    · exact absurd h h2
    · exact h
  have h2' : v 2 = -q * v 1 := by
    rw [e2]; field_simp
  ext i
  fin_cases i <;> simp [u, h0, h3, h2'] <;> ring

end

/-- Pivotal element on `V^{⊗6}` (three slots). -/
def K6 (q : R) := kroneckerMap (· * ·) (KK q) (kroneckerMap (· * ·) (KK q) (KK q))

/-- Pivotal trace on `V^{⊗6}`. -/
def qtr6 (q : R) (x : Matrix (Fin 4 × Fin 4 × Fin 4) (Fin 4 × Fin 4 × Fin 4) R) : R :=
  trace (K6 q * x)

/-- Slot multiplicativity of the pivotal trace. -/
theorem qtr6_kron (q : R) (a b c : Matrix (Fin 4) (Fin 4) R) :
    qtr6 q (kroneckerMap (· * ·) a (kroneckerMap (· * ·) b c)) =
      qtr q a * qtr q b * qtr q c := by
  unfold qtr6 K6 qtr
  rw [← Matrix.mul_kronecker_mul, ← Matrix.mul_kronecker_mul, Matrix.trace_kronecker,
    Matrix.trace_kronecker, mul_assoc]

/-- On `V^{⊗6}`, the composite of the EW-sym idempotent with the Higgs-slot
    idempotent is their tensor product. -/
theorem composite_eq_tensor (a b c : Matrix (Fin 4) (Fin 4) R) :
    kroneckerMap (· * ·) a (kroneckerMap (· * ·) b 1) *
      kroneckerMap (· * ·) 1 (kroneckerMap (· * ·) 1 c) =
      kroneckerMap (· * ·) a (kroneckerMap (· * ·) b c) := by
  rw [← Matrix.mul_kronecker_mul, ← Matrix.mul_kronecker_mul]
  simp

/-- **Slot value of `𝒩_sym`.** `qtr6 (e⁺ ⊗ e⁺ ⊗ e⁻) = [3]_q²`. -/
theorem nsym_slot (q : R) (hq : q ≠ 0) (h2 : two q ≠ 0) :
    qtr6 q (kroneckerMap (· * ·) (ep q) (kroneckerMap (· * ·) (ep q) (em q))) =
      (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2 := by
  rw [qtr6_kron, qtr_ep q hq h2, qtr_em q hq h2]; ring

/-- The all-sym joint idempotent `E(+,+,+)` has trace `[3]_q³`. -/
theorem qtr6_all_sym (q : R) (hq : q ≠ 0) (h2 : two q ≠ 0) :
    qtr6 q (kroneckerMap (· * ·) (ep q) (kroneckerMap (· * ·) (ep q) (ep q))) =
      (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 3 := by
  rw [qtr6_kron, qtr_ep q hq h2]; ring

end QOU.QuantumObservableUniverses.NSymSlotDerivation
