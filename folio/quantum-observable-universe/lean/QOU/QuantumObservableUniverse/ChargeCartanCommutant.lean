/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Data.Matrix.Mul
import Mathlib.Data.Fin.VecNotation
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

/-!
# Charge lies outside the braid image but commutes with it (two strands)

This is a check of one structural claim in the charge discussion, on `V ⊗ V` with
`V` two-dimensional and basis order `11, 12, 21, 22`, over any field `K` with `q ≠ 0`.

* `Rh`: the balanced `U_q(sl₂)` braid matrix on `V ⊗ V`.
* `Rh_hecke`: `Rh² = (q - q⁻¹) Rh + 1`, the Hecke relation of the paper.
* `KK`: the total Cartan `K ⊗ K = diag(q², 1, 1, q⁻²)`.
* `KK_comm`: `K ⊗ K` commutes with the braid matrix, so total charge is conserved by
  every crossing.
* `K1_not_comm`: the one-strand Cartan `K ⊗ 1` does not commute with the braid matrix
  when `q² ≠ 1`. So the charge of a single strand is not a braid invariant. Composites
  built from strand Cartans lie outside the braid image.
* `deltaNu_bar`: the defect `(k - k⁻¹)/2` changes sign under `k ↦ k⁻¹`, and the pair
  product of two defects is unchanged.

This is the two-strand case only. The general Jimbo statement (the braid image is the
`U_q(sl₂)` commutant) is cited, not proved here.

No `sorry`.

## References
- [leitner2026] §1 Categorical foundations.
-/

namespace QOU.QuantumObservableUniverse.ChargeCartan

open Matrix

variable {K : Type*} [Field K]

/-- The balanced braid matrix on `V ⊗ V`, eigenvalues `q` and `-q⁻¹`. -/
def Rh (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- Total Cartan `K ⊗ K`. -/
def KK (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q ^ 2, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0; 0, 0, 0, q⁻¹ ^ 2]

/-- One-strand Cartan `K ⊗ 1`. -/
def K1 (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0; 0, q, 0, 0; 0, 0, q⁻¹, 0; 0, 0, 0, q⁻¹]

theorem Rh_hecke (q : K) (hq : q ≠ 0) :
    Rh q * Rh q = (q - q⁻¹) • Rh q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Rh, Matrix.mul_apply, Fin.sum_univ_four] <;>
    field_simp <;> ring

theorem KK_comm (q : K) : KK q * Rh q = Rh q * KK q := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [KK, Rh, Matrix.mul_apply, Fin.sum_univ_four] <;> ring

theorem K1_not_comm (q : K) (hq : q ≠ 0) (h2 : q ^ 2 ≠ 1) :
    K1 q * Rh q ≠ Rh q * K1 q := by
  intro h
  have h12 := congrFun (congrFun h 1) 2
  simp [K1, Rh, Matrix.mul_apply, Fin.sum_univ_four] at h12
  apply h2
  field_simp at h12
  exact h12

/-- The defect `(k - k⁻¹)/2` is odd under `k ↦ k⁻¹`; a product of two is even. -/
theorem deltaNu_bar (k l : K) :
    (k⁻¹ - k⁻¹⁻¹) / 2 = -((k - k⁻¹) / 2) ∧
      ((k⁻¹ - k⁻¹⁻¹) / 2) * ((l⁻¹ - l⁻¹⁻¹) / 2) = ((k - k⁻¹) / 2) * ((l - l⁻¹) / 2) := by
  simp only [inv_inv]
  constructor <;> ring

end QOU.QuantumObservableUniverse.ChargeCartan
