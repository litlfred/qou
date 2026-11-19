import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic

/-!
# QOU.Braiding.r_matrix_braiding_structure — Yang–Baxter equation and braid operator

The universal R-matrix of `U_q(su(2))` satisfies the Yang–Baxter equation
and yields a braid group representation via `Ř = P ∘ R`.

LaTeX label: `prop:r-matrix-braiding-structure`

## What this file proves

1. **General equivalence (`yang_baxter_iff_braid_relation`):**
   In any monoid equipped with involutive tensor swaps `P₁₂, P₂₃` satisfying
   `P₁₂ P₂₃ P₁₂ = P₂₃ P₁₂ P₂₃` and `R₁₃ = P₂₃ R₁₂ P₂₃ = P₁₂ R₂₃ P₁₂`,
   the quantum Yang–Baxter equation `R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂` holds if and only if
   the braided operators `Ř₁ = P₁₂ R₁₂` and `Ř₂ = P₂₃ R₂₃` satisfy the Artin braid
   relation `Ř₁ Ř₂ Ř₁ = Ř₂ Ř₁ Ř₂`.
2. **Concrete Jimbo `SU_q(2)` fundamental `R`-matrix (`jimboR2`, `jimboRcheck2`):**
   Constructs the explicit `4 × 4` fundamental `R`-matrix and braid operator
   `Ř(q) = P ∘ R(q)` over any commutative ring `R` with invertible `q` (`q * qInv = 1`),
   proving:
   - `Ř(q) = P · R(q)` (`jimboRcheck2_eq_swap_mul_R2`),
   - The Hecke quadratic relation `(Ř(q) - q · I)(Ř(q) + q⁻¹ · I) = 0` and
     `Ř(q)² = (q - q⁻¹) Ř(q) + I` (`jimboRcheck2_hecke_factor`, `jimboRcheck2_sq`),
   - The 3-dimensional symmetric eigenspace of eigenvalue `q` and 1-dimensional
     antisymmetric eigenspace of eigenvalue `-q⁻¹` (`jimboRcheck2_eigenvectors`).
3. **Unconditional Yang–Baxter and braid relation on `V^{⊗ 3}` (`jimbo_r_matrix_braiding_structure`):**
   Constructs `R₁₂, R₁₃, R₂₃` and `Ř₁₂ = P₁₂ ∘ R₁₂`, `Ř₂₃ = P₂₃ ∘ R₂₃` on
   `V^{⊗ 3} ≅ (Fin 8 → R)` and proves `r_matrix_braiding_structure` unconditionally
   over any `[CommRing R]` (and specifically over `R_q = ℤ[q, q⁻¹]`).
-/

namespace QOU.Braiding

noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)
end

/-- **Yang–Baxter equation** `R₁₂ ∘ R₁₃ ∘ R₂₃ = R₂₃ ∘ R₁₃ ∘ R₁₂`. -/
def YangBaxterHolds {V3 : Type*} (comp : V3 → V3 → V3) (R12 R13 R23 : V3) : Prop :=
  comp (comp R12 R13) R23 = comp (comp R23 R13) R12

/-- **Braid relation** `Ř₁ Ř₂ Ř₁ = Ř₂ Ř₁ Ř₂` for `Ř = P ∘ R`. -/
def BraidRelationHolds {V3 : Type*} (comp : V3 → V3 → V3) (Rcheck1 Rcheck2 : V3) :
    Prop :=
  comp (comp Rcheck1 Rcheck2) Rcheck1 = comp (comp Rcheck2 Rcheck1) Rcheck2

/-- **The claim of `prop:r-matrix-braiding-structure`**: both the Yang–Baxter
equation for `(R₁₂, R₁₃, R₂₃)` and the braid relation for `(Ř₁, Ř₂)` hold. -/
def r_matrix_braiding_structure {V3 : Type*} (comp : V3 → V3 → V3)
    (R12 R13 R23 Rcheck1 Rcheck2 : V3) : Prop :=
  YangBaxterHolds comp R12 R13 R23 ∧ BraidRelationHolds comp Rcheck1 Rcheck2

/-- Alias for the braid-relation half. -/
def braid_rep_from_R_check {V3 : Type*} (comp : V3 → V3 → V3)
    (Rcheck1 Rcheck2 : V3) : Prop :=
  BraidRelationHolds comp Rcheck1 Rcheck2

/-! ## General algebraic equivalence: Quantum Yang–Baxter ↔ Artin Braid Relation -/

section GeneralEquivalence

variable {M : Type*} [Monoid M]

/-- In any monoid `M`, if `P12` and `P23` are involutions (`P12² = 1`, `P23² = 1`)
satisfying the symmetric-group braid relation `P12 P23 P12 = P23 P12 P23`, and
`R13` is intertwined by `P23 R12 P23 = R13` and `P12 R23 P12 = R13`, then
for `Rcheck1 = P12 * R12` and `Rcheck2 = P23 * R23`:
- `Rcheck1 * Rcheck2 * Rcheck1 = (P12 * P23 * P12) * (R23 * R13 * R12)`, and
- `Rcheck2 * Rcheck1 * Rcheck2 = (P12 * P23 * P12) * (R12 * R13 * R23)`. -/
theorem rcheck_triple_products (P12 P23 R12 R13 R23 : M)
    (hP12 : P12 * P12 = 1) (hP23 : P23 * P23 = 1)
    (hPbraid : P12 * P23 * P12 = P23 * P12 * P23)
    (hR13_a : P23 * R12 * P23 = R13)
    (hR13_b : P12 * R23 * P12 = R13) :
    (P12 * R12) * (P23 * R23) * (P12 * R12) =
      (P12 * P23 * P12) * (R23 * R13 * R12) ∧
    (P23 * R23) * (P12 * R12) * (P23 * R23) =
      (P12 * P23 * P12) * (R12 * R13 * R23) := by
  have h1 : R12 * P23 = P23 * R13 := by
    calc R12 * P23 = (1 * R12) * P23 := by rw [one_mul]
    _ = (P23 * P23 * R12) * P23 := by rw [hP23]
    _ = P23 * (P23 * R12 * P23) := by simp [mul_assoc]
    _ = P23 * R13 := by rw [hR13_a]
  have h2 : R23 * P12 = P12 * R13 := by
    calc R23 * P12 = (1 * R23) * P12 := by rw [one_mul]
    _ = (P12 * P12 * R23) * P12 := by rw [hP12]
    _ = P12 * (P12 * R23 * P12) := by simp [mul_assoc]
    _ = P12 * R13 := by rw [hR13_b]
  have h3 : R13 * P12 = P12 * R23 := by
    calc R13 * P12 = (P12 * R23 * P12) * P12 := by rw [← hR13_b]
    _ = P12 * R23 * (P12 * P12) := by simp [mul_assoc]
    _ = P12 * R23 := by rw [hP12, mul_one]
  have h4 : R13 * P23 = P23 * R12 := by
    calc R13 * P23 = (P23 * R12 * P23) * P23 := by rw [← hR13_a]
    _ = P23 * R12 * (P23 * P23) := by simp [mul_assoc]
    _ = P23 * R12 := by rw [hP23, mul_one]
  refine ⟨?_, ?_⟩
  · calc (P12 * R12) * (P23 * R23) * (P12 * R12)
        = P12 * (R12 * P23) * (R23 * P12) * R12 := by simp [mul_assoc]
      _ = P12 * (P23 * R13) * (P12 * R13) * R12 := by rw [h1, h2]
      _ = P12 * P23 * (R13 * P12) * R13 * R12 := by simp [mul_assoc]
      _ = P12 * P23 * (P12 * R23) * R13 * R12 := by rw [h3]
      _ = (P12 * P23 * P12) * (R23 * R13 * R12) := by simp [mul_assoc]
  · calc (P23 * R23) * (P12 * R12) * (P23 * R23)
        = P23 * (R23 * P12) * (R12 * P23) * R23 := by simp [mul_assoc]
      _ = P23 * (P12 * R13) * (P23 * R13) * R23 := by rw [h2, h1]
      _ = P23 * P12 * (R13 * P23) * R13 * R23 := by simp [mul_assoc]
      _ = P23 * P12 * (P23 * R12) * R13 * R23 := by rw [h4]
      _ = (P23 * P12 * P23) * (R12 * R13 * R23) := by simp [mul_assoc]
      _ = (P12 * P23 * P12) * (R12 * R13 * R23) := by rw [← hPbraid]

/-- **Equivalence of the Yang–Baxter equation and the Artin braid relation**
under the tensor-swap twist `Ř = P ∘ R`. -/
theorem yang_baxter_iff_braid_relation (P12 P23 R12 R13 R23 : M)
    (hP12 : P12 * P12 = 1) (hP23 : P23 * P23 = 1)
    (hPbraid : P12 * P23 * P12 = P23 * P12 * P23)
    (hR13_a : P23 * R12 * P23 = R13)
    (hR13_b : P12 * R23 * P12 = R13) :
    YangBaxterHolds (· * ·) R12 R13 R23 ↔
      BraidRelationHolds (· * ·) (P12 * R12) (P23 * R23) := by
  obtain ⟨hL, hR⟩ := rcheck_triple_products P12 P23 R12 R13 R23 hP12 hP23 hPbraid hR13_a hR13_b
  change R12 * R13 * R23 = R23 * R13 * R12 ↔
    (P12 * R12) * (P23 * R23) * (P12 * R12) = (P23 * R23) * (P12 * R12) * (P23 * R23)
  have hPinv : (P12 * P23 * P12) * (P12 * P23 * P12) = 1 := by
    calc (P12 * P23 * P12) * (P12 * P23 * P12)
        = (P12 * P23 * P12) * (P23 * P12 * P23) := by rw [hPbraid]
      _ = P12 * P23 * (P12 * P23 * P12) * P23 := by simp [mul_assoc]
      _ = P12 * P23 * (P23 * P12 * P23) * P23 := by rw [hPbraid]
      _ = P12 * (P23 * P23) * P12 * (P23 * P23) := by simp [mul_assoc]
      _ = 1 := by rw [hP23, mul_one, mul_one, hP12]
  rw [hL, hR]
  constructor
  · intro hYB
    rw [hYB]
  · intro hBraid
    have hcancel := congrArg ((P12 * P23 * P12) * ·) hBraid
    simp only [← mul_assoc, hPinv, one_mul] at hcancel
    exact hcancel.symm

end GeneralEquivalence

/-! ## Concrete `4 × 4` Jimbo `SU_q(2)` Fundamental `R`-Matrix and Hecke Channels -/

section FundamentalTwoStrand

variable {R : Type*} [CommRing R]

/-- The `4 × 4` tensor swap `P : V ⊗ V → V ⊗ V` in the basis `(e₀₀, e₀₁, e₁₀, e₁₁)`. -/
def jimboSwap2 : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, 0, 0;
     0, 0, 0, 1]

/-- The `4 × 4` Jimbo `SU_q(2)` fundamental `R`-matrix `R(q)` on `V ⊗ V`. -/
def jimboR2 (q qInv : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0;
     0, 1, 0, 0;
     0, q - qInv, 1, 0;
     0, 0, 0, q]

/-- The `4 × 4` braided operator `Ř(q) = P ∘ R(q)` on `V ⊗ V`. -/
def jimboRcheck2 (q qInv : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0;
     0, q - qInv, 1, 0;
     0, 1, 0, 0;
     0, 0, 0, q]

/-- `Ř(q) = P · R(q)` as `4 × 4` matrices. -/
theorem jimboRcheck2_eq_swap_mul_R2 (q qInv : R) :
    jimboRcheck2 q qInv = jimboSwap2 * jimboR2 q qInv := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [jimboRcheck2, jimboSwap2, jimboR2, Matrix.mul_apply, Fin.sum_univ_four]

/-- **Hecke quadratic relation for `Ř(q)`:**
`Ř(q)² = (q - q⁻¹) · Ř(q) + I₄` whenever `q * qInv = 1`. -/
theorem jimboRcheck2_sq (q qInv : R) (hq : q * qInv = 1) :
    jimboRcheck2 q qInv * jimboRcheck2 q qInv =
      (q - qInv) • jimboRcheck2 q qInv + (1 : Matrix (Fin 4) (Fin 4) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [jimboRcheck2, Matrix.mul_apply, Fin.sum_univ_four]
  · linear_combination hq
  · linear_combination hq

/-- **Factored Hecke relation for `Ř(q)`:**
`(Ř(q) - q · I₄) * (Ř(q) + q⁻¹ · I₄) = 0`, exhibiting the two Hecke eigenvalues
`q` and `-q⁻¹`. -/
theorem jimboRcheck2_hecke_factor (q qInv : R) (hq : q * qInv = 1) :
    (jimboRcheck2 q qInv - q • (1 : Matrix (Fin 4) (Fin 4) R)) *
      (jimboRcheck2 q qInv + qInv • (1 : Matrix (Fin 4) (Fin 4) R)) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [jimboRcheck2, Matrix.mul_apply, Fin.sum_univ_four]
  · linear_combination -hq
  · linear_combination -hq

/-- Symmetric basis vectors of `Sym²_q(V)` (3D eigenspace with eigenvalue `q`)
and antisymmetric singlet of `Λ²_q(V)` (1D eigenspace with eigenvalue `-q⁻¹`). -/
def symEigVec1 : Fin 4 → R := ![1, 0, 0, 0]
def symEigVec2 : Fin 4 → R := ![0, 0, 0, 1]
def symEigVec3 (q : R) : Fin 4 → R := ![0, q, 1, 0]
def antiEigVec (q : R) : Fin 4 → R := ![0, 1, -q, 0]

/-- Explicit eigenvector equations verifying the symmetric channel (`λ = q`, multiplicity 3)
and the antisymmetric channel (`λ = -q⁻¹`, multiplicity 1) of `Ř(q)`. -/
theorem jimboRcheck2_eigenvectors (q qInv : R) (hq : q * qInv = 1) :
    (jimboRcheck2 q qInv).mulVec symEigVec1 = q • symEigVec1 ∧
    (jimboRcheck2 q qInv).mulVec symEigVec2 = q • symEigVec2 ∧
    (jimboRcheck2 q qInv).mulVec (symEigVec3 q) = q • symEigVec3 q ∧
    (jimboRcheck2 q qInv).mulVec (antiEigVec q) = (-qInv) • antiEigVec q := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · funext i; fin_cases i <;> simp [jimboRcheck2, symEigVec1, Matrix.mulVec, dotProduct, Fin.sum_univ_four]
  · funext i; fin_cases i <;> simp [jimboRcheck2, symEigVec2, Matrix.mulVec, dotProduct, Fin.sum_univ_four]
  · funext i; fin_cases i <;>
      simp [jimboRcheck2, symEigVec3, Matrix.mulVec, dotProduct, Fin.sum_univ_four]
    linear_combination -hq
  · funext i; fin_cases i <;>
      simp [jimboRcheck2, antiEigVec, Matrix.mulVec, dotProduct, Fin.sum_univ_four]
    · ring
    · linear_combination -hq

end FundamentalTwoStrand

/-! ## Concrete `V^{⊗ 3}` Yang–Baxter and Braid Relation Proof for Jimbo's `SU_q(2)` `R`-Matrix

We index the `8`-dimensional three-strand space `V ⊗ V ⊗ V ≅ (Fin 8 → R)` in binary order
`(0:000, 1:001, 2:010, 3:011, 4:100, 5:101, 6:110, 7:111)`. -/

section ThreeStrandJimbo

variable {R : Type*} [CommRing R]

/-- Tensor swap `P₁₂ = P ⊗ id` on `V^{⊗ 3} ≅ (Fin 8 → R)`. -/
def swap12Op (v : Fin 8 → R) : Fin 8 → R :=
  ![v 0, v 1, v 4, v 5, v 2, v 3, v 6, v 7]

/-- Tensor swap `P₂₃ = id ⊗ P` on `V^{⊗ 3} ≅ (Fin 8 → R)`. -/
def swap23Op (v : Fin 8 → R) : Fin 8 → R :=
  ![v 0, v 2, v 1, v 3, v 4, v 6, v 5, v 7]

/-- `R₁₂(q) = R(q) ⊗ id` on `V^{⊗ 3} ≅ (Fin 8 → R)`. -/
def jimboR12Op (q qInv : R) (v : Fin 8 → R) : Fin 8 → R :=
  ![q * v 0, q * v 1, v 2, v 3,
    (q - qInv) * v 2 + v 4, (q - qInv) * v 3 + v 5, q * v 6, q * v 7]

/-- `R₁₃(q)` acting on factors 1 and 3 of `V^{⊗ 3} ≅ (Fin 8 → R)`. -/
def jimboR13Op (q qInv : R) (v : Fin 8 → R) : Fin 8 → R :=
  ![q * v 0, v 1, q * v 2, v 3,
    (q - qInv) * v 1 + v 4, q * v 5, (q - qInv) * v 3 + v 6, q * v 7]

/-- `R₂₃(q) = id ⊗ R(q)` on `V^{⊗ 3} ≅ (Fin 8 → R)`. -/
def jimboR23Op (q qInv : R) (v : Fin 8 → R) : Fin 8 → R :=
  ![q * v 0, v 1, (q - qInv) * v 1 + v 2, q * v 3,
    q * v 4, v 5, (q - qInv) * v 5 + v 6, q * v 7]

/-- `Ř₁₂(q) = P₁₂ ∘ R₁₂(q) = Ř(q) ⊗ id` on `V^{⊗ 3} ≅ (Fin 8 → R)`. -/
def jimboRcheck12Op (q qInv : R) (v : Fin 8 → R) : Fin 8 → R :=
  swap12Op (jimboR12Op q qInv v)

/-- `Ř₂₃(q) = P₂₃ ∘ R₂₃(q) = id ⊗ Ř(q)` on `V^{⊗ 3} ≅ (Fin 8 → R)`. -/
def jimboRcheck23Op (q qInv : R) (v : Fin 8 → R) : Fin 8 → R :=
  swap23Op (jimboR23Op q qInv v)

/-- Operator composition on `V^{⊗ 3} ≅ (Fin 8 → R)`. -/
def compOp (F G : (Fin 8 → R) → (Fin 8 → R)) : (Fin 8 → R) → (Fin 8 → R) :=
  fun v => F (G v)

/-- **Quantum Yang–Baxter equation on `V^{⊗ 3}` for Jimbo's `SU_q(2)` `R`-matrix:**
`R₁₂ ∘ R₁₃ ∘ R₂₃ = R₂₃ ∘ R₁₃ ∘ R₁₂`. -/
theorem jimbo_yang_baxter (q qInv : R) (hq : q * qInv = 1) :
    YangBaxterHolds compOp (jimboR12Op q qInv) (jimboR13Op q qInv) (jimboR23Op q qInv) := by
  unfold YangBaxterHolds compOp
  funext v i
  fin_cases i <;> simp [jimboR12Op, jimboR13Op, jimboR23Op]
  · ring
  · linear_combination (-(q - qInv) * v 1) * hq
  · ring
  · linear_combination ((q - qInv) * v 3) * hq

/-- **Braid relation on `V^{⊗ 3}` for Jimbo's `SU_q(2)` braid operator `Ř = P ∘ R`:**
`Ř₁₂ ∘ Ř₂₃ ∘ Ř₁₂ = Ř₂₃ ∘ Ř₁₂ ∘ Ř₂₃`. -/
theorem jimbo_braid_relation (q qInv : R) (hq : q * qInv = 1) :
    BraidRelationHolds compOp (jimboRcheck12Op q qInv) (jimboRcheck23Op q qInv) := by
  unfold BraidRelationHolds compOp
  funext v i
  fin_cases i <;>
    simp [jimboRcheck12Op, jimboRcheck23Op, swap12Op, swap23Op, jimboR12Op, jimboR23Op]
  · linear_combination ((q - qInv) * v 1) * hq
  · ring
  · linear_combination (-(q - qInv) * v 3) * hq
  · ring

/-- **Unconditional `r_matrix_braiding_structure` theorem for Jimbo's `SU_q(2)` `R`-matrix**
over any commutative ring `R` with `q * qInv = 1`. -/
theorem jimbo_r_matrix_braiding_structure (q qInv : R) (hq : q * qInv = 1) :
    r_matrix_braiding_structure compOp
      (jimboR12Op q qInv) (jimboR13Op q qInv) (jimboR23Op q qInv)
      (jimboRcheck12Op q qInv) (jimboRcheck23Op q qInv) :=
  ⟨jimbo_yang_baxter q qInv hq, jimbo_braid_relation q qInv hq⟩

/-- In `R_q = ℤ[q, q⁻¹]`, `q_param * q_inv_param = 1`. -/
theorem q_param_mul_q_inv_param : q_param * q_inv_param = 1 := by
  unfold q_param q_inv_param
  rw [← LaurentPolynomial.T_add, add_neg_cancel, LaurentPolynomial.T_zero]

/-- **Concrete `r_matrix_braiding_structure` over `R_q = ℤ[q, q⁻¹]`:**
both the Yang–Baxter equation `R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂` and the braid relation
`Ř₁₂ Ř₂₃ Ř₁₂ = Ř₂₃ Ř₁₂ Ř₂₃` hold unconditionally for the fundamental `SU_q(2)`
`R`-matrix over `ℤ[q, q⁻¹]`. -/
theorem su2_laurent_r_matrix_braiding_structure :
    r_matrix_braiding_structure compOp
      (jimboR12Op q_param q_inv_param)
      (jimboR13Op q_param q_inv_param)
      (jimboR23Op q_param q_inv_param)
      (jimboRcheck12Op q_param q_inv_param)
      (jimboRcheck23Op q_param q_inv_param) :=
  jimbo_r_matrix_braiding_structure q_param q_inv_param q_param_mul_q_inv_param

end ThreeStrandJimbo

/-- The R-matrix eigenvalue data on the fundamental of `SU_q(2)`:
    `q` on the symmetric channel and `-q⁻¹` on the antisymmetric channel,
    satisfying the Hecke relation `(σ - q)(σ + q⁻¹) = 0`, i.e.
    `σ² = (q - q⁻¹)σ + 1`. -/
structure RMatrixEigenData where
  /-- Dimension of the representation (fundamental of `SU_q(2)`: dim = 2). -/
  repDim : ℕ
  /-- Symmetric-channel eigenvalue (`= q`). -/
  eigenvalue_symmetric : R_q
  /-- Antisymmetric-channel eigenvalue (`= -q⁻¹`). -/
  eigenvalue_antisymmetric : R_q
  /-- Characteristic-polynomial sum and product of the two Hecke eigenvalues. -/
  hecke_sum  : R_q
  hecke_prod : R_q
  /-- Characteristic-polynomial coefficient witnesses (`σ² = hecke_sum·σ - hecke_prod`). -/
  hecke_sum_eq  : eigenvalue_symmetric + eigenvalue_antisymmetric = hecke_sum
  hecke_prod_eq : eigenvalue_symmetric * eigenvalue_antisymmetric = hecke_prod

/-- For the fundamental representation of `SU_q(2)`, the R-matrix has
    eigenvalues `q` and `-q⁻¹`; their sum is `q - q⁻¹` and their product is
    `-1` (so `σ² = (q - q⁻¹)σ + 1`, the Hecke relation). -/
noncomputable def su2_fundamental_r_matrix (q qInv : R_q)
    (hq : q * qInv = 1) : RMatrixEigenData where
  repDim := 2
  eigenvalue_symmetric := q
  eigenvalue_antisymmetric := -qInv
  hecke_sum := q - qInv
  hecke_prod := -1
  hecke_sum_eq := by ring
  hecke_prod_eq := by
    rw [mul_neg, hq]

end QOU.Braiding
