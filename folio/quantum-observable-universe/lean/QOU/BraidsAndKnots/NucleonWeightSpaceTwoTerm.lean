import QOU.BraidsAndKnots.NucleonWeightSpaceTraces
import QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder

/-!
# Two-term Cartan + pairwise electromagnetic operators on the nucleon weight spaces

Setting as in `NucleonWeightSpaceTraces` and `NucleonWeightSpaceSecondOrder`: level-2 Jimbo
braiding on `(C²)^{⊗3}`, the proton-type `(2,1)` weight space (basis `e₁e₁e₂, e₁e₂e₁, e₂e₁e₁`)
and the neutron-type `(1,2)` weight space (basis `e₁e₂e₂, e₂e₁e₂, e₂e₂e₁`).

On a single strand `V = C²` (`e₁ = u`, `e₂ = d`), the electric charge matrix
`Q = diag(2/3, -1/3) = (1/6) I + T³` combines the Cartan-involution-odd isospin generator
`T³ = diag(1/2, -1/2)` with the Cartan-involution-even hypercharge offset `(Y/2) I = (1/6) I`.
Consequently, on the three-strand weight spaces `(2,1)` and `(1,2)`:

* The diagonal self-energy charge-squared sum `Q_self = Q₁² + Q₂² + Q₃²` acts as the scalar `1`
  on `(2,1)` and `(2/3)` on `(1,2)`.
* The total pairwise charge product `Q_pair = Q₁Q₂ + Q₁Q₃ + Q₂Q₃` acts as the scalar `0` on
  `(2,1)` and `(-1/3)` on `(1,2)`.
* The position-resolved pairwise charge operators `Q₁₂ = Q ⊗ Q ⊗ 1` and `Q₂₃ = 1 ⊗ Q ⊗ Q` act by
  3×3 diagonal matrices that commute locally with their respective braid crossing generators
  (`[Q₁₂, σ₁^{±1}] = 0` and `[Q₂₃, σ₂^{±1}] = 0`), but are **not** intertwined by the braid
  intertwiner `P(q)` of `NucleonWeightSpaceTraces`:
  `P(q) Q₁₂^{(p)} ≠ Q₁₂^{(n)} P(q)` and `P(q) Q₂₃^{(p)} ≠ Q₂₃^{(n)} P(q)`.
* For every braid word `w`, the two-term trace difference combining the quantum-trace Cartan
  weight `K^{⊗3}` (`q` on `(2,1)`, `q⁻¹` on `(1,2)`) with `c_em • Q_pair` or
  `c_em • (Q₁₂ + Q₂₃)` splits into an `(n - p)` Cartan term `(q⁻¹ - q) tr(w)` and an
  electromagnetic term of opposite sign on positive-trace words.
* On the three-strand Borromean braid `V³ = (σ₁ σ₂⁻¹)³`, the proton adjacent-crossing trace
  `tr((Q₁₂^{(p)} + Q₂₃^{(p)}) V_p³)` cancels at order `(q - 1)³` and vanishes to fourth order
  `(q - 1)⁴`.

No numerical value enters.
-/

namespace QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder

variable {R : Type*} [Field R]

/-! ## 1. Inverse Braid Generators on `(2,1)` and `(1,2)` -/

/-- `σ₁⁻¹` on the `(2,1)` weight space. -/
def A₁Inv (q : R) : Matrix (Fin 3) (Fin 3) R := !![q⁻¹, 0, 0; 0, -(q - q⁻¹), 1; 0, 1, 0]

/-- `σ₂⁻¹` on the `(2,1)` weight space. -/
def A₂Inv (q : R) : Matrix (Fin 3) (Fin 3) R := !![-(q - q⁻¹), 1, 0; 1, 0, 0; 0, 0, q⁻¹]

/-- `σ₁⁻¹` on the `(1,2)` weight space. -/
def B₁Inv (q : R) : Matrix (Fin 3) (Fin 3) R := !![-(q - q⁻¹), 1, 0; 1, 0, 0; 0, 0, q⁻¹]

/-- `σ₂⁻¹` on the `(1,2)` weight space. -/
def B₂Inv (q : R) : Matrix (Fin 3) (Fin 3) R := !![q⁻¹, 0, 0; 0, -(q - q⁻¹), 1; 0, 1, 0]

theorem A₁_mul_A₁Inv (q : R) (hq : q ≠ 0) : A₁ q * A₁Inv q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [A₁, A₁Inv, Matrix.mul_apply, Fin.sum_univ_three]; try field_simp)

theorem A₂_mul_A₂Inv (q : R) (hq : q ≠ 0) : A₂ q * A₂Inv q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [A₂, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three]; try field_simp)

theorem intertwine₁Inv (q : R) (hq : q ≠ 0) : P q * A₁Inv q = B₁Inv q * P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [P, A₁Inv, B₁Inv, Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

theorem intertwine₂Inv (q : R) (hq : q ≠ 0) : P q * A₂Inv q = B₂Inv q * P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [P, A₂Inv, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-! ## 2. Weight-Space Charge Operators: `K^{⊗3}`, `Q_self`, `Q_pair`, `Q₁₂`, `Q₂₃`, `Q₁₃` -/

/-- Cartan quantum-trace weight `K^{⊗3}` on the proton `(2,1)` weight space (`q • 1`). -/
def Kp (q : R) : Matrix (Fin 3) (Fin 3) R := q • (1 : Matrix (Fin 3) (Fin 3) R)

/-- Cartan quantum-trace weight `K^{⊗3}` on the neutron `(1,2)` weight space (`q⁻¹ • 1`). -/
def Kn (q : R) : Matrix (Fin 3) (Fin 3) R := q⁻¹ • (1 : Matrix (Fin 3) (Fin 3) R)

/-- Diagonal self-energy charge-squared sum `Q₁² + Q₂² + Q₃²` on `(2,1)`. -/
def QSelfP : Matrix (Fin 3) (Fin 3) R := (1 : Matrix (Fin 3) (Fin 3) R)

/-- Diagonal self-energy charge-squared sum `Q₁² + Q₂² + Q₃²` on `(1,2)`. -/
def QSelfN : Matrix (Fin 3) (Fin 3) R := (2 / 3 : R) • (1 : Matrix (Fin 3) (Fin 3) R)

/-- Total pairwise charge product `Q₁Q₂ + Q₁Q₃ + Q₂Q₃` on `(2,1)`. -/
def QPairP : Matrix (Fin 3) (Fin 3) R := (0 : Matrix (Fin 3) (Fin 3) R)

/-- Total pairwise charge product `Q₁Q₂ + Q₁Q₃ + Q₂Q₃` on `(1,2)`. -/
def QPairN : Matrix (Fin 3) (Fin 3) R := (-1 / 3 : R) • (1 : Matrix (Fin 3) (Fin 3) R)

/-- Pairwise charge operator `Q₁₂ = Q ⊗ Q ⊗ 1` on the proton `(2,1)` weight space. -/
def Q12p : Matrix (Fin 3) (Fin 3) R := !![4 / 9, 0, 0; 0, -2 / 9, 0; 0, 0, -2 / 9]

/-- Pairwise charge operator `Q₂₃ = 1 ⊗ Q ⊗ Q` on the proton `(2,1)` weight space. -/
def Q23p : Matrix (Fin 3) (Fin 3) R := !![-2 / 9, 0, 0; 0, -2 / 9, 0; 0, 0, 4 / 9]

/-- Pairwise charge operator `Q₁₃ = Q ⊗ 1 ⊗ Q` on the proton `(2,1)` weight space. -/
def Q13p : Matrix (Fin 3) (Fin 3) R := !![-2 / 9, 0, 0; 0, 4 / 9, 0; 0, 0, -2 / 9]

/-- Pairwise charge operator `Q₁₂ = Q ⊗ Q ⊗ 1` on the neutron `(1,2)` weight space. -/
def Q12n : Matrix (Fin 3) (Fin 3) R := !![-2 / 9, 0, 0; 0, -2 / 9, 0; 0, 0, 1 / 9]

/-- Pairwise charge operator `Q₂₃ = 1 ⊗ Q ⊗ Q` on the neutron `(1,2)` weight space. -/
def Q23n : Matrix (Fin 3) (Fin 3) R := !![1 / 9, 0, 0; 0, -2 / 9, 0; 0, 0, -2 / 9]

/-- Pairwise charge operator `Q₁₃ = Q ⊗ 1 ⊗ Q` on the neutron `(1,2)` weight space. -/
def Q13n : Matrix (Fin 3) (Fin 3) R := !![-2 / 9, 0, 0; 0, 1 / 9, 0; 0, 0, -2 / 9]

/-- Sum of the three pairwise charge matrices on `(2,1)` equals `QPairP = 0`. -/
theorem QPairP_eq_sum : (Q12p : Matrix (Fin 3) (Fin 3) R) + Q23p + Q13p = QPairP := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12p, Q23p, Q13p, QPairP] <;> ring

/-- Sum of the three pairwise charge matrices on `(1,2)` equals `QPairN = (-1/3) • 1`. -/
theorem QPairN_eq_sum (h3 : (3 : R) ≠ 0) :
    (Q12n : Matrix (Fin 3) (Fin 3) R) + Q23n + Q13n = QPairN := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12n, Q23n, Q13n, QPairN] <;>
    rw [h9] <;> field_simp <;> ring

/-- Linear relation between the adjacent pairwise sums `Q₁₂ + Q₂₃` on `(1,2)` and `(2,1)`. -/
theorem QAdj_relation :
    (2 : R) • ((Q12n : Matrix (Fin 3) (Fin 3) R) + Q23n) - (Q12p + Q23p) =
      (-4 / 9 : R) • (1 : Matrix (Fin 3) (Fin 3) R) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12n, Q23n, Q12p, Q23p] <;> ring

/-- Each pairwise charge operator on the proton `(2,1)` weight space is traceless. -/
theorem trace_Q12p_zero : trace (Q12p : Matrix (Fin 3) (Fin 3) R) = 0 := by
  simp [Q12p, Matrix.trace_fin_three]; ring

theorem trace_Q23p_zero : trace (Q23p : Matrix (Fin 3) (Fin 3) R) = 0 := by
  simp [Q23p, Matrix.trace_fin_three]; ring

theorem trace_Q13p_zero : trace (Q13p : Matrix (Fin 3) (Fin 3) R) = 0 := by
  simp [Q13p, Matrix.trace_fin_three]; ring

/-- Each pairwise charge operator on the neutron `(1,2)` weight space has trace `-1/3`. -/
theorem trace_Q12n_eq (h3 : (3 : R) ≠ 0) :
    trace (Q12n : Matrix (Fin 3) (Fin 3) R) = -1 / 3 := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12n, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem trace_Q23n_eq (h3 : (3 : R) ≠ 0) :
    trace (Q23n : Matrix (Fin 3) (Fin 3) R) = -1 / 3 := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q23n, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem trace_Q13n_eq (h3 : (3 : R) ≠ 0) :
    trace (Q13n : Matrix (Fin 3) (Fin 3) R) = -1 / 3 := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q13n, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

/-! ## 3. Local Crossing Commutation Laws (`[Q₁₂, σ₁^{±1}] = 0` and `[Q₂₃, σ₂^{±1}] = 0`) -/

theorem Q12p_comm_A1 (q : R) : (Q12p : Matrix (Fin 3) (Fin 3) R) * A₁ q = A₁ q * Q12p := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12p, A₁, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem Q12p_comm_A1Inv (q : R) :
    (Q12p : Matrix (Fin 3) (Fin 3) R) * A₁Inv q = A₁Inv q * Q12p := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12p, A₁Inv, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem Q23p_comm_A2 (q : R) : (Q23p : Matrix (Fin 3) (Fin 3) R) * A₂ q = A₂ q * Q23p := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q23p, A₂, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem Q23p_comm_A2Inv (q : R) :
    (Q23p : Matrix (Fin 3) (Fin 3) R) * A₂Inv q = A₂Inv q * Q23p := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q23p, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem Q12n_comm_B1 (q : R) : (Q12n : Matrix (Fin 3) (Fin 3) R) * B₁ q = B₁ q * Q12n := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12n, B₁, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem Q12n_comm_B1Inv (q : R) :
    (Q12n : Matrix (Fin 3) (Fin 3) R) * B₁Inv q = B₁Inv q * Q12n := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12n, B₁Inv, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem Q23n_comm_B2 (q : R) : (Q23n : Matrix (Fin 3) (Fin 3) R) * B₂ q = B₂ q * Q23n := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q23n, B₂, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem Q23n_comm_B2Inv (q : R) :
    (Q23n : Matrix (Fin 3) (Fin 3) R) * B₂Inv q = B₂Inv q * Q23n := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q23n, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

/-! ## 4. Hypercharge Breaking of the Intertwiner `P(q)` -/

/-- `P(q)` fails to intertwine `QSelfP` and `QSelfN` by `(1/3) • P(q)`. -/
theorem intertwine_QSelf_defect (q : R) (h3 : (3 : R) ≠ 0) :
    P q * QSelfP - QSelfN * P q = (1 / 3 : R) • P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [P, QSelfP, QSelfN] <;>
    field_simp <;> ring

/-- `P(q)` fails to intertwine `QPairP` and `QPairN` by `(1/3) • P(q)`. -/
theorem intertwine_QPair_defect (q : R) :
    P q * QPairP - QPairN * P q = (1 / 3 : R) • P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [P, QPairP, QPairN] <;>
    ring

/-- The `(2,2)` entry of `P(q) Q₁₂^{(p)} - Q₁₂^{(n)} P(q)` is `-1/3`. -/
theorem intertwine_Q12_defect_22 (q : R) (h3 : (3 : R) ≠ 0) :
    ((P q * Q12p - Q12n * P q : Matrix (Fin 3) (Fin 3) R) 2 2) = (-1 / 3 : R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [P, Q12p, Q12n]
  rw [h9]; field_simp; ring

/-- `P(q)` does not intertwine `Q₁₂^{(p)}` and `Q₁₂^{(n)}`. -/
theorem intertwine_Q12_ne (q : R) (h3 : (3 : R) ≠ 0) :
    P q * Q12p ≠ Q12n * P q := by
  intro h
  have h22 : ((P q * Q12p - Q12n * P q : Matrix (Fin 3) (Fin 3) R) 2 2) = 0 := by
    rw [sub_eq_zero.mpr h, Matrix.zero_apply]
  rw [intertwine_Q12_defect_22 q h3] at h22
  exact div_ne_zero (by norm_num) h3 h22

/-- The `(2,2)` entry of `P(q) Q₂₃^{(p)} - Q₂₃^{(n)} P(q)` is `+2/3`. -/
theorem intertwine_Q23_defect_22 (q : R) (h3 : (3 : R) ≠ 0) :
    ((P q * Q23p - Q23n * P q : Matrix (Fin 3) (Fin 3) R) 2 2) = (2 / 3 : R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [P, Q23p, Q23n]
  rw [h9]; field_simp; ring

/-- `P(q)` does not intertwine `Q₂₃^{(p)}` and `Q₂₃^{(n)}`. -/
theorem intertwine_Q23_ne (q : R) (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) :
    P q * Q23p ≠ Q23n * P q := by
  intro h
  have h22 : ((P q * Q23p - Q23n * P q : Matrix (Fin 3) (Fin 3) R) 2 2) = 0 := by
    rw [sub_eq_zero.mpr h, Matrix.zero_apply]
  rw [intertwine_Q23_defect_22 q h3] at h22
  exact div_ne_zero h2 h3 h22

/-- The `(2,2)` entry of `P(q) (Q₁₂^{(p)} + Q₂₃^{(p)}) - (Q₁₂^{(n)} + Q₂₃^{(n)}) P(q)` is `+1/3`. -/
theorem intertwine_QAdj_defect_22 (q : R) (h3 : (3 : R) ≠ 0) :
    ((P q * (Q12p + Q23p) - (Q12n + Q23n) * P q : Matrix (Fin 3) (Fin 3) R) 2 2) = (1 / 3 : R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [P, Q12p, Q23p, Q12n, Q23n]
  rw [h9]; field_simp; ring

/-- `P(q)` does not intertwine `Q₁₂^{(p)} + Q₂₃^{(p)}` and `Q₁₂^{(n)} + Q₂₃^{(n)}`. -/
theorem intertwine_QAdj_ne (q : R) (h3 : (3 : R) ≠ 0) :
    P q * (Q12p + Q23p) ≠ (Q12n + Q23n) * P q := by
  intro h
  have h22 : ((P q * (Q12p + Q23p) - (Q12n + Q23n) * P q : Matrix (Fin 3) (Fin 3) R) 2 2) = 0 := by
    rw [sub_eq_zero.mpr h, Matrix.zero_apply]
  rw [intertwine_QAdj_defect_22 q h3] at h22
  exact one_div_ne_zero h3 h22

/-! ## 5. Two-Term Trace Decompositions on Any Braid Word `w` -/

theorem trace_Kp_word (q : R) (w : List Bool) :
    trace (Kp q * word (A₁ q) (A₂ q) w) = q * trace (word (A₁ q) (A₂ q) w) := by
  rw [Kp, Matrix.smul_mul, Matrix.one_mul, Matrix.trace_smul, smul_eq_mul]

theorem trace_Kn_word (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Bool) :
    trace (Kn q * word (B₁ q) (B₂ q) w) = q⁻¹ * trace (word (A₁ q) (A₂ q) w) := by
  rw [Kn, Matrix.smul_mul, Matrix.one_mul, Matrix.trace_smul, smul_eq_mul,
      ← trace_word_eq q hq hq2 w]

theorem trace_K_diff_word (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Bool) :
    trace (Kn q * word (B₁ q) (B₂ q) w) - trace (Kp q * word (A₁ q) (A₂ q) w) =
      (q⁻¹ - q) * trace (word (A₁ q) (A₂ q) w) := by
  rw [trace_Kn_word q hq hq2 w, trace_Kp_word q w]
  ring

theorem trace_QSelf_diff_word (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h3 : (3 : R) ≠ 0) (w : List Bool) :
    trace (QSelfN * word (B₁ q) (B₂ q) w) - trace (QSelfP * word (A₁ q) (A₂ q) w) =
      (-1 / 3 : R) * trace (word (A₁ q) (A₂ q) w) := by
  rw [QSelfN, QSelfP, Matrix.smul_mul, Matrix.one_mul, Matrix.one_mul,
      Matrix.trace_smul, smul_eq_mul, ← trace_word_eq q hq hq2 w]
  field_simp; ring

theorem trace_QPair_diff_word (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Bool) :
    trace (QPairN * word (B₁ q) (B₂ q) w) - trace (QPairP * word (A₁ q) (A₂ q) w) =
      (-1 / 3 : R) * trace (word (A₁ q) (A₂ q) w) := by
  rw [QPairN, QPairP, Matrix.smul_mul, Matrix.one_mul, Matrix.zero_mul,
      Matrix.trace_smul, Matrix.trace_zero, smul_eq_mul, ← trace_word_eq q hq hq2 w]
  ring

/-- Two-term `K^{⊗3} + c_em • Q_pair` trace difference on any braid word `w`. -/
theorem trace_twoTerm_QPair_diff_word (q c_em : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (w : List Bool) :
    trace ((Kn q + c_em • QPairN) * word (B₁ q) (B₂ q) w) -
      trace ((Kp q + c_em • QPairP) * word (A₁ q) (A₂ q) w) =
      (q⁻¹ - q - c_em / 3) * trace (word (A₁ q) (A₂ q) w) := by
  rw [Matrix.add_mul, Matrix.add_mul, Matrix.trace_add, Matrix.trace_add,
      Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul, Matrix.trace_smul,
      smul_eq_mul, smul_eq_mul, trace_Kn_word q hq hq2 w, trace_Kp_word q w,
      QPairN, QPairP, Matrix.smul_mul, Matrix.one_mul, Matrix.zero_mul,
      Matrix.trace_smul, Matrix.trace_zero, smul_eq_mul, ← trace_word_eq q hq hq2 w]
  ring

/-- Two-term `K^{⊗3} + c_em • Q_self` trace difference on any braid word `w`. -/
theorem trace_twoTerm_QSelf_diff_word (q c_em : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h3 : (3 : R) ≠ 0) (w : List Bool) :
    trace ((Kn q + c_em • QSelfN) * word (B₁ q) (B₂ q) w) -
      trace ((Kp q + c_em • QSelfP) * word (A₁ q) (A₂ q) w) =
      (q⁻¹ - q - c_em / 3) * trace (word (A₁ q) (A₂ q) w) := by
  rw [Matrix.add_mul, Matrix.add_mul, Matrix.trace_add, Matrix.trace_add,
      Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul, Matrix.trace_smul,
      smul_eq_mul, smul_eq_mul, trace_Kn_word q hq hq2 w, trace_Kp_word q w,
      QSelfN, QSelfP, Matrix.smul_mul, Matrix.one_mul, Matrix.one_mul,
      Matrix.trace_smul, smul_eq_mul, ← trace_word_eq q hq hq2 w]
  field_simp; ring

/-- Two-term `K^{⊗3} + c_em • (Q₁₂ + Q₂₃)` trace decomposition on any braid word `w`. -/
theorem trace_twoTerm_QAdj_diff_word (q c_em : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (w : List Bool) :
    trace ((Kn q + c_em • (Q12n + Q23n)) * word (B₁ q) (B₂ q) w) -
      trace ((Kp q + c_em • (Q12p + Q23p)) * word (A₁ q) (A₂ q) w) =
      (q⁻¹ - q) * trace (word (A₁ q) (A₂ q) w) +
        c_em * (trace ((Q12n + Q23n) * word (B₁ q) (B₂ q) w) -
          trace ((Q12p + Q23p) * word (A₁ q) (A₂ q) w)) := by
  rw [Matrix.add_mul, Matrix.add_mul, Matrix.trace_add, Matrix.trace_add,
      Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul, Matrix.trace_smul,
      smul_eq_mul, smul_eq_mul, trace_Kn_word q hq hq2 w, trace_Kp_word q w]
  ring

/-- Adding the symmetric second-order weak insertion `c_weak • (FE + EF)` of
`NucleonWeightSpaceSecondOrder` leaves the two-term `(n - p)` trace difference invariant. -/
theorem trace_twoTerm_with_secondOrder_eq (q c_em c_weak : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (w : List Bool) :
    trace ((Kn q + c_em • (Q12n + Q23n) + c_weak • (FEn q + EFn q)) * word (B₁ q) (B₂ q) w) -
      trace ((Kp q + c_em • (Q12p + Q23p) + c_weak • (FEp q + EFp q)) * word (A₁ q) (A₂ q) w) =
      trace ((Kn q + c_em • (Q12n + Q23n)) * word (B₁ q) (B₂ q) w) -
        trace ((Kp q + c_em • (Q12p + Q23p)) * word (A₁ q) (A₂ q) w) := by
  simp only [Matrix.add_mul, Matrix.trace_add, Matrix.smul_mul, Matrix.trace_smul,
    smul_eq_mul, trace_FEn_eq_EFp q hq hq2 w, trace_EFn_eq_FEp q hq hq2 w]
  ring

/-! ## 6. Closed-Form Evaluations on Half-Twist `Δ₃` and Borromean `V³ = (σ₁ σ₂⁻¹)³` -/

/-- Three-strand half-twist `Δ₃ = σ₁ σ₂ σ₁` on `(2,1)` and `(1,2)`. -/
def halfTwistA (q : R) : Matrix (Fin 3) (Fin 3) R := A₁ q * A₂ q * A₁ q
def halfTwistB (q : R) : Matrix (Fin 3) (Fin 3) R := B₁ q * B₂ q * B₁ q

theorem halfTwistA_eq_halfTwistB (q : R) (hq : q ≠ 0) : halfTwistA q = halfTwistB q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [halfTwistA, halfTwistB, A₁, A₂, B₁, B₂, Matrix.mul_apply, Fin.sum_univ_three];
      try field_simp; try ring)

theorem trace_halfTwistA (q : R) (hq : q ≠ 0) : trace (halfTwistA q) = q ^ 3 := by
  simp [halfTwistA, A₁, A₂, Matrix.trace_fin_three]
  field_simp; ring

theorem trace_Q12_diff_halfTwist (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (Q12n * halfTwistB q) - trace (Q12p * halfTwistA q) =
      q * (q ^ 2 - 1) / 3 := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12n, Q12p, halfTwistA, halfTwistB, A₁, A₂, B₁, B₂, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem trace_Q23_diff_halfTwist (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (Q23n * halfTwistB q) - trace (Q23p * halfTwistA q) =
      -2 * q * (q ^ 2 - 1) / 3 := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q23n, Q23p, halfTwistA, halfTwistB, A₁, A₂, B₁, B₂, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem trace_QAdj_diff_halfTwist (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace ((Q12n + Q23n) * halfTwistB q) - trace ((Q12p + Q23p) * halfTwistA q) =
      -q * (q ^ 2 - 1) / 3 := by
  have hsub :
      trace ((Q12n + Q23n) * halfTwistB q) - trace ((Q12p + Q23p) * halfTwistA q) =
        (trace (Q12n * halfTwistB q) - trace (Q12p * halfTwistA q)) +
          (trace (Q23n * halfTwistB q) - trace (Q23p * halfTwistA q)) := by
    rw [Matrix.add_mul, Matrix.add_mul, Matrix.trace_add, Matrix.trace_add]; ring
  rw [hsub, trace_Q12_diff_halfTwist q hq h3, trace_Q23_diff_halfTwist q hq h3]
  ring

/-- Borromean generator `V = σ₁ σ₂⁻¹` and three-strand Borromean word `V³ = (σ₁ σ₂⁻¹)³`. -/
def borromeanVA (q : R) : Matrix (Fin 3) (Fin 3) R := A₁ q * A₂Inv q
def borromeanVB (q : R) : Matrix (Fin 3) (Fin 3) R := B₁ q * B₂Inv q
def borromeanV3A (q : R) : Matrix (Fin 3) (Fin 3) R := borromeanVA q * borromeanVA q * borromeanVA q
def borromeanV3B (q : R) : Matrix (Fin 3) (Fin 3) R := borromeanVB q * borromeanVB q * borromeanVB q

theorem trace_borromeanV3A (q : R) (hq : q ≠ 0) :
    trace (borromeanV3A q) =
      -(q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6 := by
  simp [borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.trace_fin_three]
  field_simp; ring

theorem trace_Q12p_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (Q12p * borromeanV3A q) =
      -2 * (q - 1) ^ 3 * (q + 1) ^ 3 * (2 * q ^ 6 + 1) / (9 * q ^ 6) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12p, borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem trace_Q23p_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (Q23p * borromeanV3A q) =
      2 * (q - 1) ^ 3 * (q + 1) ^ 3 * (q ^ 6 + 2) / (9 * q ^ 6) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q23p, borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

/-- On the proton `(2,1)` weight space, the adjacent-crossing electromagnetic trace
`tr((Q₁₂^{(p)} + Q₂₃^{(p)}) V_p³)` vanishes to fourth order `(q - 1)⁴` at `q = 1`. -/
theorem trace_QAdjp_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace ((Q12p + Q23p) * borromeanV3A q) =
      -2 * (q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (9 * q ^ 6) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  rw [Matrix.add_mul, Matrix.trace_add,
      trace_Q12p_borromeanV3 q hq h3, trace_Q23p_borromeanV3 q hq h3]
  rw [h9]; field_simp; ring

theorem trace_Q12n_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (Q12n * borromeanV3B q) =
      (2 * q ^ 12 - 9 * q ^ 10 + 15 * q ^ 8 - 16 * q ^ 6 + 9 * q ^ 4 - 6 * q ^ 2 + 2) /
        (9 * q ^ 6) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12n, borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem trace_Q23n_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (Q23n * borromeanV3B q) =
      (2 * q ^ 12 - 6 * q ^ 10 + 9 * q ^ 8 - 16 * q ^ 6 + 15 * q ^ 4 - 9 * q ^ 2 + 2) /
        (9 * q ^ 6) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q23n, borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

theorem trace_QAdjn_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace ((Q12n + Q23n) * borromeanV3B q) =
      (4 * q ^ 12 - 15 * q ^ 10 + 24 * q ^ 8 - 32 * q ^ 6 + 24 * q ^ 4 - 15 * q ^ 2 + 4) /
        (9 * q ^ 6) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  rw [Matrix.add_mul, Matrix.trace_add,
      trace_Q12n_borromeanV3 q hq h3, trace_Q23n_borromeanV3 q hq h3]
  rw [h9]; field_simp; ring

theorem trace_QAdj_diff_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace ((Q12n + Q23n) * borromeanV3B q) - trace ((Q12p + Q23p) * borromeanV3A q) =
      (2 * q ^ 12 - 7 * q ^ 10 + 10 * q ^ 8 - 12 * q ^ 6 + 10 * q ^ 4 - 7 * q ^ 2 + 2) /
        (3 * q ^ 6) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  rw [trace_QAdjn_borromeanV3 q hq h3, trace_QAdjp_borromeanV3 q hq h3]
  rw [h9]; field_simp; ring

/-- The neutron Borromean trace `tr(V_n³)` equals the proton Borromean trace `tr(V_p³)`. -/
theorem trace_borromeanV3B (q : R) (hq : q ≠ 0) :
    trace (borromeanV3B q) =
      -(q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6 := by
  simp [borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.trace_fin_three]
  field_simp; ring

/-- Exact decomposition of the neutron adjacent-crossing charge matrix `Q₁₂^{(n)} + Q₂₃^{(n)}`
into its static scalar `q = 1` component `(-2/9) I₃` (of trace `-2/3`) plus `1/2` of the
traceless proton adjacent-crossing charge matrix `Q₁₂^{(p)} + Q₂₃^{(p)}`. -/
theorem QAdjn_eq_static_add_half_QAdjp (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) :
    (Q12n + Q23n : Matrix (Fin 3) (Fin 3) R) =
      (-2 / 9 : R) • (1 : Matrix (Fin 3) (Fin 3) R) +
        (1 / 2 : R) • (Q12p + Q23p : Matrix (Fin 3) (Fin 3) R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12n, Q23n, Q12p, Q23p, Matrix.add_apply, Matrix.smul_apply]
  all_goals (rw [h9]; field_simp; ring)

/-- Connected fourth-order quantum braid trace on the neutron `(1,2)` weight space:
subtracting the static scalar `q = 1` Coulomb background `(-2/9) tr(V_n³)` from
`tr((Q₁₂^{(n)} + Q₂₃^{(n)}) V_n³)` yields a fourth-order `(q - 1)⁴` polynomial with
opposite sign and half the `q → 1` amplitude of `trace_QAdjp_borromeanV3`. -/
theorem trace_QAdjn_borromeanV3_connected (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : R) * trace (borromeanV3B q) =
      (q - 1) ^ 4 * (q + 1) ^ 4 * (2 * q ^ 4 - q ^ 2 + 2) / (9 * q ^ 6) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  rw [trace_QAdjn_borromeanV3 q hq h3, trace_borromeanV3B q hq]
  rw [h9]; field_simp; ring

/-- Connected fourth-order `(n - p)` electromagnetic trace difference on the Borromean
nucleon `V³ = (σ₁ σ₂⁻¹)³`: both the neutron and proton connected adjacent-crossing traces
are `O((q - 1)⁴)` with opposite signs, so their difference reinforces with exact `q → 1`
ratio `(1/2 - (-1)) / 1 = 3/2` relative to the proton connected trace amplitude. -/
theorem trace_QAdj_connected_diff_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    (trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : R) * trace (borromeanV3B q)) -
      trace ((Q12p + Q23p) * borromeanV3A q) =
      (q - 1) ^ 4 * (q + 1) ^ 4 * (4 * q ^ 4 + q ^ 2 + 4) / (9 * q ^ 6) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  rw [trace_QAdjn_borromeanV3_connected q hq h3, trace_QAdjp_borromeanV3 q hq h3]
  rw [h9]; field_simp; ring

/-- Cyclic crossing-dressing derivative identity across the 3 periods of the Borromean
proton braid `V_p³ = (A₁ A₂⁻¹)³`: summing a local `(Q₁₂^{(p)}, Q₂₃^{(p)})` insertion over all
6 crossings of `V_p³` equals `3 * tr((Q₁₂^{(p)} + Q₂₃^{(p)}) V_p³)`. -/
theorem trace_borromeanV3A_six_crossing_sum (q : R) :
    trace ((Q12p * A₁ q * A₂Inv q + A₁ q * (Q23p * A₂Inv q)) * borromeanVA q * borromeanVA q) +
    trace (borromeanVA q * (Q12p * A₁ q * A₂Inv q + A₁ q * (Q23p * A₂Inv q)) * borromeanVA q) +
    trace (borromeanVA q * borromeanVA q * (Q12p * A₁ q * A₂Inv q + A₁ q * (Q23p * A₂Inv q))) =
      3 * trace ((Q12p + Q23p) * borromeanV3A q) := by
  simp [borromeanV3A, borromeanVA, Q12p, Q23p, A₁, A₂Inv, Matrix.trace_fin_three]
  ring

/-- Cyclic crossing-dressing derivative identity across the 3 periods of the Borromean
neutron braid `V_n³ = (B₁ B₂⁻¹)³`: summing a local `(Q₁₂^{(n)}, Q₂₃^{(n)})` insertion over all
6 crossings of `V_n³` equals `3 * tr((Q₁₂^{(n)} + Q₂₃^{(n)}) V_n³)`. -/
theorem trace_borromeanV3B_six_crossing_sum (q : R) :
    trace ((Q12n * B₁ q * B₂Inv q + B₁ q * (Q23n * B₂Inv q)) * borromeanVB q * borromeanVB q) +
    trace (borromeanVB q * (Q12n * B₁ q * B₂Inv q + B₁ q * (Q23n * B₂Inv q)) * borromeanVB q) +
    trace (borromeanVB q * borromeanVB q * (Q12n * B₁ q * B₂Inv q + B₁ q * (Q23n * B₂Inv q))) =
      3 * trace ((Q12n + Q23n) * borromeanV3B q) := by
  simp [borromeanV3B, borromeanVB, Q12n, Q23n, B₁, B₂Inv, Matrix.trace_fin_three]
  ring

/-! ## Section 7: Central Idempotent Projections `e_{(3)}` and `e_{(2,1)}` on the Borromean Two-Term Trace (Gaps 3 & 4) -/

/-- Quantum integer `[3]_q = q² + 1 + q⁻²`. -/
def qInt3 (q : R) : R := q ^ 2 + 1 + q⁻¹ ^ 2

/-- Central idempotent `e_{(3)}` (`I = 3/2` decuplet projector) on the proton `(2,1)` weight space. -/
def e3p (q : R) : Matrix (Fin 3) (Fin 3) R := (qInt3 q)⁻¹ • FEp q

/-- Central idempotent `e_{(2,1)}` (`I = 1/2` nucleon projector) on the proton `(2,1)` weight space. -/
def e21p (q : R) : Matrix (Fin 3) (Fin 3) R := 1 - e3p q

/-- Central idempotent `e_{(3)}` (`I = 3/2` decuplet projector) on the neutron `(1,2)` weight space. -/
def e3n (q : R) : Matrix (Fin 3) (Fin 3) R := (qInt3 q)⁻¹ • EFn q

/-- Central idempotent `e_{(2,1)}` (`I = 1/2` nucleon projector) on the neutron `(1,2)` weight space. -/
def e21n (q : R) : Matrix (Fin 3) (Fin 3) R := 1 - e3n q

theorem qInt3_eq_div (q : R) (hq : q ≠ 0) :
    qInt3 q = (q ^ 4 + q ^ 2 + 1) / q ^ 2 := by
  unfold qInt3; field_simp

theorem qInt3_inv_eq_div (q : R) (hq : q ≠ 0) :
    (qInt3 q)⁻¹ = q ^ 2 / (q ^ 4 + q ^ 2 + 1) := by
  rw [qInt3_eq_div q hq, inv_div]

theorem q4_add_q2_add_one_ne_zero (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    q ^ 4 + q ^ 2 + 1 ≠ 0 := by
  intro h
  apply hq3
  rw [qInt3_eq_div q hq, h, zero_div]

theorem FEp_comm_borromeanV3A (q : R) (hq : q ≠ 0) :
    FEp q * borromeanV3A q = borromeanV3A q * FEp q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [FEp, borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three];
      try field_simp; try ring)

theorem EFn_comm_borromeanV3B (q : R) (hq : q ≠ 0) :
    EFn q * borromeanV3B q = borromeanV3B q * EFn q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [EFn, borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three];
      try field_simp; try ring)

theorem e21p_comm_borromeanV3A (q : R) (hq : q ≠ 0) :
    e21p q * borromeanV3A q = borromeanV3A q * e21p q := by
  simp only [e21p, e3p, Matrix.sub_mul, Matrix.mul_sub, Matrix.one_mul, Matrix.mul_one,
    Matrix.smul_mul, Matrix.mul_smul, FEp_comm_borromeanV3A q hq]

theorem e21n_comm_borromeanV3B (q : R) (hq : q ≠ 0) :
    e21n q * borromeanV3B q = borromeanV3B q * e21n q := by
  simp only [e21n, e3n, Matrix.sub_mul, Matrix.mul_sub, Matrix.one_mul, Matrix.mul_one,
    Matrix.smul_mul, Matrix.mul_smul, EFn_comm_borromeanV3B q hq]

theorem trace_FEp_borromeanV3 (q : R) (hq : q ≠ 0) :
    trace (FEp q * borromeanV3A q) = qInt3 q := by
  simp [FEp, qInt3, borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.trace_fin_three]
  field_simp; ring

theorem trace_EFn_borromeanV3 (q : R) (hq : q ≠ 0) :
    trace (EFn q * borromeanV3B q) = qInt3 q := by
  simp [EFn, qInt3, borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.trace_fin_three]
  field_simp; ring

/-- On the `I = 3/2` decuplet sector `e_{(3)}`, the proton Borromean trace is identically `1`. -/
theorem trace_e3p_borromeanV3 (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (e3p q * borromeanV3A q) = 1 := by
  rw [e3p, Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul,
      trace_FEp_borromeanV3 q hq, inv_mul_cancel₀ hq3]

/-- On the `I = 3/2` decuplet sector `e_{(3)}`, the neutron Borromean trace is identically `1`. -/
theorem trace_e3n_borromeanV3 (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (e3n q * borromeanV3B q) = 1 := by
  rw [e3n, Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul,
      trace_EFn_borromeanV3 q hq, inv_mul_cancel₀ hq3]

/-- On the `I = 1/2` nucleon sector `e_{(2,1)}`, the proton Borromean trace equals `tr(V_p³) - 1`. -/
theorem trace_e21p_borromeanV3 (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (e21p q * borromeanV3A q) =
      -(q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 2 * q ^ 6 - 2 * q ^ 2 + 1) / q ^ 6 := by
  rw [e21p, Matrix.sub_mul, Matrix.one_mul, Matrix.trace_sub,
      trace_borromeanV3A q hq, trace_e3p_borromeanV3 q hq hq3]
  field_simp; ring

/-- On the `I = 1/2` nucleon sector `e_{(2,1)}`, the neutron Borromean trace equals `tr(V_n³) - 1`. -/
theorem trace_e21n_borromeanV3 (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (e21n q * borromeanV3B q) =
      -(q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 2 * q ^ 6 - 2 * q ^ 2 + 1) / q ^ 6 := by
  rw [e21n, Matrix.sub_mul, Matrix.one_mul, Matrix.trace_sub,
      trace_borromeanV3B q hq, trace_e3n_borromeanV3 q hq hq3]
  field_simp; ring

/-- Strong Cartan `(n - p)` trace difference on the `I = 1/2` nucleon sector `e_{(2,1)}`. -/
theorem trace_e21_strong_cartan_diff_borromeanV3 (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (Kn q * (e21n q * borromeanV3B q)) - trace (Kp q * (e21p q * borromeanV3A q)) =
      (q⁻¹ - q) * (-(q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 2 * q ^ 6 - 2 * q ^ 2 + 1) / q ^ 6) := by
  rw [Kn, Kp, Matrix.smul_mul, Matrix.smul_mul, Matrix.one_mul, Matrix.one_mul,
      Matrix.trace_smul, Matrix.trace_smul, smul_eq_mul, smul_eq_mul,
      trace_e21n_borromeanV3 q hq hq3, trace_e21p_borromeanV3 q hq hq3]
  ring

/-- `e_{(3)}` (`FEp`) adjacent-crossing electromagnetic trace on the proton Borromean braid `V_p³`. -/
theorem trace_FEp_QAdjp_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (FEp q * (Q12p + Q23p) * borromeanV3A q) =
      2 * (q - 1) ^ 2 * (q + 1) ^ 2 / (9 * q ^ 2) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [FEp, Q12p, Q23p, borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

/-- `e_{(3)}` (`EFn`) adjacent-crossing electromagnetic trace on the neutron Borromean braid `V_n³`. -/
theorem trace_EFn_QAdjn_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (EFn q * (Q12n + Q23n) * borromeanV3B q) =
      -(q ^ 4 + 4 * q ^ 2 + 1) / (9 * q ^ 2) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [EFn, Q12n, Q23n, borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

/-- `e_{(2,1)}`-projected adjacent-crossing electromagnetic trace on the proton Borromean braid `V_p³`. -/
theorem trace_e21p_QAdjp_borromeanV3 (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (e21p q * (Q12p + Q23p) * borromeanV3A q) =
      -2 * (q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 12 - q ^ 6 + 1) /
        (9 * q ^ 6 * (q ^ 4 + q ^ 2 + 1)) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := q4_add_q2_add_one_ne_zero q hq hq3
  rw [e21p, e3p, Matrix.sub_mul, Matrix.sub_mul, Matrix.one_mul,
      Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_sub, Matrix.trace_smul, smul_eq_mul,
      trace_QAdjp_borromeanV3 q hq h3, trace_FEp_QAdjp_borromeanV3 q hq h3,
      qInt3_inv_eq_div q hq]
  generalize hD_eq : q ^ 4 + q ^ 2 + 1 = D at hq4 ⊢
  rw [h9]; field_simp
  subst hD_eq; ring

/-- `e_{(2,1)}`-projected adjacent-crossing electromagnetic trace on the neutron Borromean braid `V_n³`. -/
theorem trace_e21n_QAdjn_borromeanV3 (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (e21n q * (Q12n + Q23n) * borromeanV3B q) =
      (4 * q ^ 16 - 11 * q ^ 14 + 13 * q ^ 12 - 22 * q ^ 10 + 20 * q ^ 8 - 22 * q ^ 6 +
        13 * q ^ 4 - 11 * q ^ 2 + 4) / (9 * q ^ 6 * (q ^ 4 + q ^ 2 + 1)) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := q4_add_q2_add_one_ne_zero q hq hq3
  rw [e21n, e3n, Matrix.sub_mul, Matrix.sub_mul, Matrix.one_mul,
      Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_sub, Matrix.trace_smul, smul_eq_mul,
      trace_QAdjn_borromeanV3 q hq h3, trace_EFn_QAdjn_borromeanV3 q hq h3,
      qInt3_inv_eq_div q hq]
  generalize hD_eq : q ^ 4 + q ^ 2 + 1 = D at hq4 ⊢
  rw [h9]; field_simp
  subst hD_eq; ring

/-- `e_{(2,1)}`-projected `(n - p)` adjacent-crossing electromagnetic trace difference on the
Borromean nucleon braid `V³`. -/
theorem trace_e21_QAdj_diff_borromeanV3 (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (e21n q * (Q12n + Q23n) * borromeanV3B q) -
      trace (e21p q * (Q12p + Q23p) * borromeanV3A q) =
      (2 * q ^ 16 - 5 * q ^ 14 + 5 * q ^ 12 - 8 * q ^ 10 + 8 * q ^ 8 - 8 * q ^ 6 +
        5 * q ^ 4 - 5 * q ^ 2 + 2) / (3 * q ^ 6 * (q ^ 4 + q ^ 2 + 1)) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := q4_add_q2_add_one_ne_zero q hq hq3
  rw [trace_e21n_QAdjn_borromeanV3 q hq hq3 h3, trace_e21p_QAdjp_borromeanV3 q hq hq3 h3]
  generalize hD_eq : q ^ 4 + q ^ 2 + 1 = D at hq4 ⊢
  rw [h9]; field_simp
  subst hD_eq; ring

/-- Hadronic energy scale `E₀ = m_e / (q (q - 1))`. -/
def hadronicScaleE0 (m_e q : R) : R := m_e / (q * (q - 1))

/-- Scale-hierarchy identity (Gap 5): `E₀ * (q² (1 - q⁻¹)) = m_e`. -/
theorem hadronicScaleE0_mul_hbar_eq_me (m_e q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    hadronicScaleE0 m_e q * (q ^ 2 * (1 - q⁻¹)) = m_e := by
  unfold hadronicScaleE0
  field_simp

/-! ## Section 8: Gröbner Normal-Form Channel Collapse on the Borromean Nucleon `V³`

In the 6-element Hecke normal-form basis `{1, σ₀, σ₁, L₊ = σ₀σ₁, L₋ = σ₁σ₀, e⁻ = σ₀σ₁σ₀}`:
1. Because `A₁, A₂` (and `B₁, B₂`) are symmetric matrices, `L₋ = (L₊)ᵀ`, so `L₊` and `L₋` share
   identical diagonal entries and identical traces against ANY diagonal charge operator `D`
   (`trace_diag_LminusA_eq_LplusA`, `trace_diag_LminusB_eq_LplusB`).
2. On the Borromean nucleon `V³ = (σ₀ σ₁⁻¹)³`, the trefoil electron coefficient `c_{e⁻}` is
   identically `0`, and the `L₊` and `L₋` coefficients `c_{L₊} = h²(h² + 1)` and `c_{L₋} = -h²`
   cancel their `O(h²)` pieces under any diagonal trace, collapsing to `c_{L₊} + c_{L₋} = h⁴`
   (`borromeanV3A_nf_expansion`, `borromeanV3B_nf_expansion`, `borromeanV3_nf_cL_sum`). -/

/-- For any diagonal operator `Matrix.diagonal d` on the proton `(2,1)` weight space,
`L₋ = A₂ A₁` and `L₊ = A₁ A₂` have identical traces because `A₂ A₁ = (A₁ A₂)ᵀ`. -/
theorem trace_diag_LminusA_eq_LplusA (q : R) (d : Fin 3 → R) :
    trace (Matrix.diagonal d * (A₂ q * A₁ q)) =
      trace (Matrix.diagonal d * (A₁ q * A₂ q)) := by
  simp [A₁, A₂, Matrix.trace_fin_three]
  left; ring

/-- For any diagonal operator `Matrix.diagonal d` on the neutron `(1,2)` weight space,
`L₋ = B₂ B₁` and `L₊ = B₁ B₂` have identical traces because `B₂ B₁ = (B₁ B₂)ᵀ`. -/
theorem trace_diag_LminusB_eq_LplusB (q : R) (d : Fin 3 → R) :
    trace (Matrix.diagonal d * (B₂ q * B₁ q)) =
      trace (Matrix.diagonal d * (B₁ q * B₂ q)) := by
  simp [B₁, B₂, Matrix.trace_fin_three]
  left; ring

/-- In particular, `(Q₁₂^{(p)} + Q₂₃^{(p)})` has identical traces against `L₋ = A₂ A₁` and `L₊ = A₁ A₂`. -/
theorem trace_QAdjp_LminusA_eq_LplusA (q : R) :
    trace ((Q12p + Q23p) * (A₂ q * A₁ q)) =
      trace ((Q12p + Q23p) * (A₁ q * A₂ q)) := by
  simp [Q12p, Q23p, A₁, A₂, Matrix.trace_fin_three]
  left; ring

/-- And `(Q₁₂^{(n)} + Q₂₃^{(n)})` has identical traces against `L₋ = B₂ B₁` and `L₊ = B₁ B₂`. -/
theorem trace_QAdjn_LminusB_eq_LplusB (q : R) :
    trace ((Q12n + Q23n) * (B₂ q * B₁ q)) =
      trace ((Q12n + Q23n) * (B₁ q * B₂ q)) := by
  simp [Q12n, Q23n, B₁, B₂, Matrix.trace_fin_three]
  left; ring

/-- Normal-form coefficients of the Borromean braid `V³ = (σ₀ σ₁⁻¹)³` in the 6D Hecke basis
`{γ = 1, σ₀, σ₁, L₊ = σ₀σ₁, L₋ = σ₁σ₀, e⁻ = σ₀σ₁σ₀}` (with `c_{e⁻} = 0`). -/
def nfBorC1 (q : R) : R := -(q ^ 2 - q - 1) * (q ^ 2 + q - 1) * (q ^ 4 - q ^ 2 + 1) / q ^ 4
def nfBorCs0 (q : R) : R := -(q - 1) ^ 3 * (q + 1) ^ 3 * (q ^ 4 - q ^ 2 + 1) / q ^ 5
def nfBorCs1 (q : R) : R := (q - 1) ^ 3 * (q + 1) ^ 3 / q ^ 3
def nfBorCLplus (q : R) : R := (q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 4 - q ^ 2 + 1) / q ^ 4
def nfBorCLminus (q : R) : R := -(q - 1) ^ 2 * (q + 1) ^ 2 / q ^ 2

/-- When `L₊` and `L₋` combine under any diagonal trace on `V³`, their `O(h²)` pieces cancel
identically, leaving purely fourth order `c_{L₊} + c_{L₋} = (q - q⁻¹)⁴ = (q - 1)⁴(q + 1)⁴ / q⁴`. -/
theorem borromeanV3_nf_cL_sum (q : R) (hq : q ≠ 0) :
    nfBorCLplus q + nfBorCLminus q = (q - 1) ^ 4 * (q + 1) ^ 4 / q ^ 4 := by
  unfold nfBorCLplus nfBorCLminus
  field_simp; ring

/-- Exact 5-term Gröbner normal-form matrix decomposition of `V_p³ = (A₁ A₂⁻¹)³` on `(2,1)`
(with zero `e⁻ = A₁ A₂ A₁` component). -/
theorem borromeanV3A_nf_expansion (q : R) (hq : q ≠ 0) :
    borromeanV3A q =
      nfBorC1 q • (1 : Matrix (Fin 3) (Fin 3) R) +
      nfBorCs0 q • A₁ q +
      nfBorCs1 q • A₂ q +
      nfBorCLplus q • (A₁ q * A₂ q) +
      nfBorCLminus q • (A₂ q * A₁ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [borromeanV3A, borromeanVA, A₁, A₂, A₂Inv,
      nfBorC1, nfBorCs0, nfBorCs1, nfBorCLplus, nfBorCLminus,
      Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-- Exact 5-term Gröbner normal-form matrix decomposition of `V_n³ = (B₁ B₂⁻¹)³` on `(1,2)`
(with zero `e⁻ = B₁ B₂ B₁` component). -/
theorem borromeanV3B_nf_expansion (q : R) (hq : q ≠ 0) :
    borromeanV3B q =
      nfBorC1 q • (1 : Matrix (Fin 3) (Fin 3) R) +
      nfBorCs0 q • B₁ q +
      nfBorCs1 q • B₂ q +
      nfBorCLplus q • (B₁ q * B₂ q) +
      nfBorCLminus q • (B₂ q * B₁ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [borromeanV3B, borromeanVB, B₁, B₂, B₂Inv,
      nfBorC1, nfBorCs0, nfBorCs1, nfBorCLplus, nfBorCLminus,
      Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-! ## Section 9: Switched Four-Term Photon Factorisation `γ'(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁(σ₀σ₁⁻¹)` (`qou-99qc`)

Under the `qou-99qc` working assumption where the fourth photon term is switched from
`L₊ = σ₀σ₁` to the elementary Borromean step `V = σ₀σ₁⁻¹`:
1. The Borromean nucleon `V³ = (σ₀σ₁⁻¹)³` is the exact product of two pure fourth-term
   switched photons (`φ₀ = φ₁ = 0`, `φ₀₁⁺ = +q h`, `φ₀₁⁻ = -q⁻¹ h`, `h = q - q⁻¹`):
   `V³ = (1 + q h V) (1 - q⁻¹ h V) = 1 + h² V - h² V²`
   (`borromeanV3A_eq_switched_photon_product`, `borromeanV3B_eq_switched_photon_product`,
    `borromeanV3A_eq_one_add_h_sq_V_sub_V_sq`, `borromeanV3B_eq_one_add_h_sq_V_sub_V_sq`).
2. Tracing `(Q₁₂ + Q₂₃)` against a single switched step `V` and its square `V²` yields
   `O(h²)` on both proton and connected neutron (`trace_QAdjp_borromeanVA`,
   `trace_QAdjn_borromeanVB_connected`), which multiplied by the two-photon factor `h²`
   in `V³ = 1 + h² (V - V²)` immediately produces the `O(h⁴) = O((q - 1)⁴)` fourth-order
   scaling without ever invoking `L₊` or `L₋` separately. -/

/-- Switched four-term photon `γ'(φ₀, φ₁, φ₀₁) = 1 + φ₀ σ₀ + φ₁ σ₁ + φ₀₁ (σ₀ σ₁⁻¹)` on the
proton `(2,1)` weight space (`V_p = A₁ A₂⁻¹`). -/
def switchedPhotonA (q φ₀ φ₁ φ₀₁ : R) : Matrix (Fin 3) (Fin 3) R :=
  (1 : Matrix (Fin 3) (Fin 3) R) + φ₀ • A₁ q + φ₁ • A₂ q + φ₀₁ • borromeanVA q

/-- Switched four-term photon `γ'(φ₀, φ₁, φ₀₁) = 1 + φ₀ σ₀ + φ₁ σ₁ + φ₀₁ (σ₀ σ₁⁻¹)` on the
neutron `(1,2)` weight space (`V_n = B₁ B₂⁻¹`). -/
def switchedPhotonB (q φ₀ φ₁ φ₀₁ : R) : Matrix (Fin 3) (Fin 3) R :=
  (1 : Matrix (Fin 3) (Fin 3) R) + φ₀ • B₁ q + φ₁ • B₂ q + φ₀₁ • borromeanVB q

/-- Exact two-photon factorisation of the Borromean proton braid `V_p³ = (A₁ A₂⁻¹)³` into two
pure fourth-term switched photons (`φ₀ = φ₁ = 0`) with weights `+q(q - q⁻¹)` and `-q⁻¹(q - q⁻¹)`. -/
theorem borromeanV3A_eq_switched_photon_product (q : R) (hq : q ≠ 0) :
    borromeanV3A q =
      switchedPhotonA q 0 0 (q * (q - q⁻¹)) *
        switchedPhotonA q 0 0 (-q⁻¹ * (q - q⁻¹)) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [borromeanV3A, borromeanVA, switchedPhotonA, A₁, A₂, A₂Inv,
      Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-- Exact two-photon factorisation of the Borromean neutron braid `V_n³ = (B₁ B₂⁻¹)³` into two
pure fourth-term switched photons (`φ₀ = φ₁ = 0`) with weights `+q(q - q⁻¹)` and `-q⁻¹(q - q⁻¹)`. -/
theorem borromeanV3B_eq_switched_photon_product (q : R) (hq : q ≠ 0) :
    borromeanV3B q =
      switchedPhotonB q 0 0 (q * (q - q⁻¹)) *
        switchedPhotonB q 0 0 (-q⁻¹ * (q - q⁻¹)) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [borromeanV3B, borromeanVB, switchedPhotonB, B₁, B₂, B₂Inv,
      Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-- Expanded cubic identity `V_p³ = I₃ + h² V_p - h² V_p²` (`h = q - q⁻¹`) on `(2,1)`. -/
theorem borromeanV3A_eq_one_add_h_sq_V_sub_V_sq (q : R) (hq : q ≠ 0) :
    borromeanV3A q =
      (1 : Matrix (Fin 3) (Fin 3) R) +
        (q - q⁻¹) ^ 2 • borromeanVA q -
        (q - q⁻¹) ^ 2 • (borromeanVA q * borromeanVA q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [borromeanV3A, borromeanVA, A₁, A₂Inv,
      Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-- Expanded cubic identity `V_n³ = I₃ + h² V_n - h² V_n²` (`h = q - q⁻¹`) on `(1,2)`. -/
theorem borromeanV3B_eq_one_add_h_sq_V_sub_V_sq (q : R) (hq : q ≠ 0) :
    borromeanV3B q =
      (1 : Matrix (Fin 3) (Fin 3) R) +
        (q - q⁻¹) ^ 2 • borromeanVB q -
        (q - q⁻¹) ^ 2 • (borromeanVB q * borromeanVB q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [borromeanV3B, borromeanVB, B₁, B₂Inv,
      Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-- On a single switched-photon fourth term `V_p = A₁ A₂⁻¹`, the proton adjacent-charge trace
is strictly `O(h²)`: `tr((Q₁₂^{(p)} + Q₂₃^{(p)}) V_p) = -2(q - 1)²(q + 1)² / (9 q²)`. -/
theorem trace_QAdjp_borromeanVA (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace ((Q12p + Q23p) * borromeanVA q) =
      -2 * (q - 1) ^ 2 * (q + 1) ^ 2 / (9 * q ^ 2) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12p, Q23p, borromeanVA, A₁, A₂Inv, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

/-- On a single switched-photon fourth term `V_n = B₁ B₂⁻¹`, the connected neutron adjacent-charge
trace has the exact opposite sign `O(h²)`:
`tr((Q₁₂^{(n)} + Q₂₃^{(n)}) V_n) + (2/9) tr(V_n) = +2(q - 1)²(q + 1)² / (9 q²)`. -/
theorem trace_QAdjn_borromeanVB_connected (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace ((Q12n + Q23n) * borromeanVB q) + (2 / 9 : R) * trace (borromeanVB q) =
      2 * (q - 1) ^ 2 * (q + 1) ^ 2 / (9 * q ^ 2) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  simp [Q12n, Q23n, borromeanVB, B₁, B₂Inv, Matrix.trace_fin_three]
  rw [h9]; field_simp; ring

end QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
