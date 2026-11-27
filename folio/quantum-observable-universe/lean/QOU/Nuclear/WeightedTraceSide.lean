import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination

/-!
# Which side of a crossing the weighted trace closes

The pair-term readout `T_X(a,b) = Tr(K^{⊗N} Π_ab C X)` weights every strand by
`K = diag(q, q⁻¹)`. This file records, for a single crossing, the local fact behind
the observation that strands to the right of a block leave its parameter alone while
strands to its left free it.

* Closing the **right** strand of the crossing `Ř` with weight `K` leaves the scalar
  `q²` on the left strand (`rightTrace_R`). Nothing about the left strand's weight
  survives.
* Closing the **left** strand with the same weight `K` leaves
  `diag(q² + 1 − q⁻², 1)` on the right strand (`leftTrace_R`). When `q⁴ ≠ 1` this is
  not a scalar (`leftTrace_R_not_scalar`): it counts the weight of the right strand.
  The scalar result on this side needs the weight `K⁻¹` instead (`leftTraceInv_R`).

So a spectator strand standing just left of a block, joined to the block's first
strand by a crossing and traced out by the readout, inserts a weight-counting operator
on that strand. A spectator on the right inserts only a scalar. The inverse crossing
behaves the same way (`rightTrace_Rinv`, `leftTrace_Rinv`).

This is a local statement about one crossing. It does not by itself prove that the
pair-term parameter `α` is fixed for every number of spectators between the blocks;
that remains open.

Conventions: `Ř` is the Jimbo matrix used in
`computations/probes/np_splitting/np_more_strands_symbolic_probe.py` divided by `q`,
on the basis `00, 01, 10, 11` with `0` the weight `+1` state.
-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-/

namespace QOU.QBeta.WeightedTraceSide

variable {F : Type*} [Field F]

/-- The weight `K = diag(q, q⁻¹)` on one strand. -/
def Kw (q : F) : Fin 2 → F := ![q, q⁻¹]

/-- Entry `((i,j),(k,l))` of the Jimbo crossing `Ř` (row `(i,j)`, column `(k,l)`). -/
def R (q : F) (i j k l : Fin 2) : F :=
  if i = 0 ∧ j = 0 ∧ k = 0 ∧ l = 0 then q
  else if i = 0 ∧ j = 1 ∧ k = 1 ∧ l = 0 then 1
  else if i = 1 ∧ j = 0 ∧ k = 0 ∧ l = 1 then 1
  else if i = 1 ∧ j = 0 ∧ k = 1 ∧ l = 0 then q - q⁻¹
  else if i = 1 ∧ j = 1 ∧ k = 1 ∧ l = 1 then q
  else 0

/-- Entry `((i,j),(k,l))` of the inverse crossing `Ř⁻¹`. -/
def Rinv (q : F) (i j k l : Fin 2) : F :=
  if i = 0 ∧ j = 0 ∧ k = 0 ∧ l = 0 then q⁻¹
  else if i = 0 ∧ j = 1 ∧ k = 0 ∧ l = 1 then -(q - q⁻¹)
  else if i = 0 ∧ j = 1 ∧ k = 1 ∧ l = 0 then 1
  else if i = 1 ∧ j = 0 ∧ k = 0 ∧ l = 1 then 1
  else if i = 1 ∧ j = 1 ∧ k = 1 ∧ l = 1 then q⁻¹
  else 0

/-- Close the right strand of a two-strand operator with weight `w`. -/
def rightTrace (w : Fin 2 → F) (Y : Fin 2 → Fin 2 → Fin 2 → Fin 2 → F) (x x' : Fin 2) : F :=
  ∑ y, w y * Y x y x' y

/-- Close the left strand of a two-strand operator with weight `w`. -/
def leftTrace (w : Fin 2 → F) (Y : Fin 2 → Fin 2 → Fin 2 → Fin 2 → F) (x x' : Fin 2) : F :=
  ∑ y, w y * Y y x y x'

/-- `Ř⁻¹` is the inverse of `Ř`. -/
theorem R_mul_Rinv (q : F) (hq : q ≠ 0) (i j k l : Fin 2) :
    ∑ a, ∑ b, R q i j a b * Rinv q a b k l = if i = k ∧ j = l then 1 else 0 := by
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp [R, Rinv, Fin.sum_univ_two] <;> field_simp

/-- Closing the right strand of `Ř` with weight `K` leaves the scalar `q²`. -/
theorem rightTrace_R (q : F) (hq : q ≠ 0) (x x' : Fin 2) :
    rightTrace (Kw q) (R q) x x' = if x = x' then q ^ 2 else 0 := by
  fin_cases x <;> fin_cases x' <;>
    simp [rightTrace, Kw, R, Fin.sum_univ_two] <;> field_simp <;> ring

/-- Closing the right strand of `Ř⁻¹` with weight `K` leaves the scalar `q⁻²`. -/
theorem rightTrace_Rinv (q : F) (hq : q ≠ 0) (x x' : Fin 2) :
    rightTrace (Kw q) (Rinv q) x x' = if x = x' then (q⁻¹) ^ 2 else 0 := by
  fin_cases x <;> fin_cases x' <;>
    simp [rightTrace, Kw, Rinv, Fin.sum_univ_two] <;> field_simp <;> ring

/-- Closing the left strand of `Ř` with weight `K` leaves `diag(q² + 1 − q⁻², 1)`. -/
theorem leftTrace_R (q : F) (hq : q ≠ 0) (x x' : Fin 2) :
    leftTrace (Kw q) (R q) x x' =
      if x = x' then (if x = 0 then q ^ 2 + 1 - (q⁻¹) ^ 2 else 1) else 0 := by
  fin_cases x <;> fin_cases x' <;>
    simp [leftTrace, Kw, R, Fin.sum_univ_two] <;> field_simp <;> ring

/-- Closing the left strand of `Ř⁻¹` with weight `K` leaves `diag(1, q⁻² + 1 − q²)`. -/
theorem leftTrace_Rinv (q : F) (hq : q ≠ 0) (x x' : Fin 2) :
    leftTrace (Kw q) (Rinv q) x x' =
      if x = x' then (if x = 0 then 1 else (q⁻¹) ^ 2 + 1 - q ^ 2) else 0 := by
  fin_cases x <;> fin_cases x' <;>
    simp [leftTrace, Kw, Rinv, Fin.sum_univ_two] <;> field_simp <;> ring

/-- With the weight `K⁻¹`, closing the left strand of `Ř` gives the scalar `q²` again. -/
theorem leftTraceInv_R (q : F) (hq : q ≠ 0) (x x' : Fin 2) :
    leftTrace (fun y => (Kw q y)⁻¹) (R q) x x' = if x = x' then q ^ 2 else 0 := by
  fin_cases x <;> fin_cases x' <;>
    simp [leftTrace, Kw, R, Fin.sum_univ_two] <;> field_simp <;> ring

/-- The left-closed crossing is not a scalar when `q⁴ ≠ 1`: its two diagonal entries
differ by `q² − q⁻²`. -/
theorem leftTrace_R_not_scalar (q : F) (hq : q ≠ 0) (h4 : q ^ 4 ≠ 1) :
    leftTrace (Kw q) (R q) 0 0 ≠ leftTrace (Kw q) (R q) 1 1 := by
  rw [leftTrace_R q hq, leftTrace_R q hq]
  simp only [if_true]
  norm_num
  intro h
  apply h4
  have e : (q ^ 2)⁻¹ = q ^ 2 := by linear_combination -h
  calc q ^ 4 = q ^ 2 * q ^ 2 := by ring
    _ = q ^ 2 * (q ^ 2)⁻¹ := by rw [e]
    _ = 1 := mul_inv_cancel₀ (pow_ne_zero 2 hq)

end QOU.QBeta.WeightedTraceSide
