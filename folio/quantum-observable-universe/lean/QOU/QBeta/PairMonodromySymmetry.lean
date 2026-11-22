import QOU.QBeta.BlockSectorRestriction

namespace QOU.QBeta.PairMonodromySymmetry

open Matrix Kronecker QOU.QBeta.BlockChargeSectorTrace QOU.QBeta.BlockSectorRestriction
  QOU.QBeta.PairReadoutTensorReduction

variable {F : Type*} [Field F]

/-! ## Single block: the flip-reverse symmetry `θ` and the half twist `Δ` -/

/-- `u ↔ d` on one strand. -/
def fl : Fin 2 → Fin 2
  | 0 => 1
  | 1 => 0

/-- Flip every strand and reverse their order. -/
def φ (x : ι) : ι := (fl x.2.2, fl x.2.1, fl x.1)

theorem φ_φ (x : ι) : φ (φ x) = x := by
  obtain ⟨a, b, c⟩ := x; fin_cases a <;> fin_cases b <;> fin_cases c <;> rfl

def φe : ι ≃ ι := ⟨φ, φ, φ_φ, φ_φ⟩

/-- `θ M = M ∘ (φ × φ)`: conjugation by the flip-reverse permutation. -/
def θ (M : Matrix ι ι F) : Matrix ι ι F := M.submatrix φ φ

theorem θ_mul (M N : Matrix ι ι F) : θ (M * N) = θ M * θ N := by
  simp only [θ]; exact (Matrix.submatrix_mul_equiv M N φ φe φ).symm

def swapL : Letter → Letter
  | (g, i) => (!g, i)

theorem θ_letter (q : F) (l : Letter) : θ (letter8 q l) = letter8 q (swapL l) := by
  obtain ⟨g, i⟩ := l
  cases g <;> cases i <;>
  · ext ⟨a, b, c⟩ ⟨a', b', c'⟩
    fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
      simp [θ, φ, fl, swapL, letter8, site0, site1, R4, R4i, pr]

theorem θ_e3 (q : F) : θ (e3 q) = f3 q := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp [θ, φ, fl, e3, f3, e1, f1, d1, k1, ki1, kv1] <;> ring

theorem θ_f3 (q : F) : θ (f3 q) = e3 q := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp [θ, φ, fl, e3, f3, e1, f1, d1, k1, ki1, kv1] <;> ring

theorem θ_diag (d : ι → F) : θ (diagonal d) = diagonal (d ∘ φ) :=
  Matrix.submatrix_diagonal_equiv d φe

theorem kv_φ (q : F) (hq : q ≠ 0) (x : ι) : kv q (φ x) = (kv q x)⁻¹ := by
  obtain ⟨a, b, c⟩ := x
  fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [φ, fl, kv, kv1] <;> field_simp

theorem θ_K3 (q : F) (hq : q ≠ 0) : θ (K3 q) = K3i q := by
  rw [K3, θ_diag, K3i]; congr 1; funext x; exact kv_φ q hq x

theorem θ_K3i (q : F) (hq : q ≠ 0) : θ (K3i q) = K3 q := by
  rw [K3i, θ_diag, K3]; congr 1; funext x; simp [kv_φ q hq]

theorem θ_P (flip : Bool) : θ (P (F := F) flip) = P (!flip) := by
  cases flip <;>
  · ext ⟨a, b, c⟩ ⟨a', b', c'⟩
    fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
      simp [θ, φ, fl, P, uc, z, nOf, Matrix.diagonal]

theorem θ_one : θ (1 : Matrix ι ι F) = 1 := by
  have hinj : Function.Injective φ := φe.injective
  ext x y; simp only [θ, Matrix.submatrix_apply, Matrix.one_apply, hinj.eq_iff]

/-! ### Relations on one block (exact, by entries) -/

theorem site0_mul (M N : Matrix (Fin 4) (Fin 4) F) :
    site0 M * site0 N = site0 (M * N) := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  simp only [site0, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, Fin.sum_univ_four]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp [pr] <;> ring

theorem site1_mul (M N : Matrix (Fin 4) (Fin 4) F) :
    site1 M * site1 N = site1 (M * N) := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  simp only [site1, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, Fin.sum_univ_four]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp [pr] <;> ring

theorem site0_one : site0 (1 : Matrix (Fin 4) (Fin 4) F) = 1 := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp [site0, pr, Matrix.one_apply]

theorem site1_one : site1 (1 : Matrix (Fin 4) (Fin 4) F) = 1 := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp [site1, pr, Matrix.one_apply]

theorem R4_mul_R4i (q : F) (hq : q ≠ 0) : R4 q * R4i q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [R4, R4i, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> field_simp <;> ring

theorem R4i_mul_R4 (q : F) (hq : q ≠ 0) : R4i q * R4 q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [R4, R4i, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> field_simp <;> ring

theorem letter_inv (q : F) (hq : q ≠ 0) (g : Bool) :
    letter8 q (g, false) * letter8 q (g, true) = 1 := by
  cases g
  · simp only [letter8, site0_mul, R4_mul_R4i q hq, site0_one]
  · simp only [letter8, site1_mul, R4_mul_R4i q hq, site1_one]

theorem letter_inv' (q : F) (hq : q ≠ 0) (g : Bool) :
    letter8 q (g, true) * letter8 q (g, false) = 1 := by
  cases g
  · simp only [letter8, site0_mul, R4i_mul_R4 q hq, site0_one]
  · simp only [letter8, site1_mul, R4i_mul_R4 q hq, site1_one]

set_option maxHeartbeats 8000000 in
theorem ybe8 (q : F) (hq : q ≠ 0) :
    letter8 q (false, false) * letter8 q (true, false) * letter8 q (false, false)
      = letter8 q (true, false) * letter8 q (false, false) * letter8 q (true, false) := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  simp only [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, letter8, site0, site1]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp [R4, pr] <;> field_simp <;> ring

/-! ### Quantum-group relations on one block -/

macro "brute8" : tactic => `(tactic| (
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  simp only [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, Matrix.sub_apply,
    Matrix.smul_apply, smul_eq_mul, Matrix.diagonal_apply, Matrix.add_apply]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp [letter8, site0, site1, R4, pr, e3, f3, e1, f1, d1, k1, ki1, kv1, kv, K3, K3i] <;>
    (try field_simp) <;> (try ring_nf) <;> (try simp)))

set_option maxHeartbeats 8000000 in
theorem efK (q : F) (hq : q ≠ 0) : (q - q⁻¹) • (e3 q * f3 q - f3 q * e3 q) = K3 q - K3i q := by
  brute8
set_option maxHeartbeats 8000000 in
theorem eKi (q : F) (hq : q ≠ 0) : e3 q * K3i q = q ^ 2 • (K3i q * e3 q) := by
  brute8
set_option maxHeartbeats 8000000 in
theorem Kf (q : F) (hq : q ≠ 0) : K3 q * f3 q = (q ^ 2)⁻¹ • (f3 q * K3 q) := by
  brute8
set_option maxHeartbeats 8000000 in
theorem l0_e (q : F) (hq : q ≠ 0) : letter8 q (false, false) * e3 q = e3 q * letter8 q (false, false) := by
  brute8
set_option maxHeartbeats 8000000 in
theorem l1_e (q : F) (hq : q ≠ 0) : letter8 q (true, false) * e3 q = e3 q * letter8 q (true, false) := by
  brute8
set_option maxHeartbeats 8000000 in
theorem l0_f (q : F) (hq : q ≠ 0) : letter8 q (false, false) * f3 q = f3 q * letter8 q (false, false) := by
  brute8
set_option maxHeartbeats 8000000 in
theorem l1_f (q : F) (hq : q ≠ 0) : letter8 q (true, false) * f3 q = f3 q * letter8 q (true, false) := by
  brute8
set_option maxHeartbeats 8000000 in
theorem l0_K (q : F) (hq : q ≠ 0) : letter8 q (false, false) * K3 q = K3 q * letter8 q (false, false) := by
  brute8
set_option maxHeartbeats 8000000 in
theorem l1_K (q : F) (hq : q ≠ 0) : letter8 q (true, false) * K3 q = K3 q * letter8 q (true, false) := by
  brute8

/-! ## Six strands: two nucleons side by side -/

abbrev S := ι × ι
abbrev Q := Fin 2 × Fin 2 × Fin 2 × Fin 2
abbrev T := Fin 2 × Fin 2

def prU (x : T) : Fin 4 := pr x.1 x.2

/-- Site-pair `(a0,a1)` window. -/
def E0 : S ≃ T × Q where
  toFun := fun ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ => ((a0, a1), (a2, b0, b1, b2))
  invFun := fun ⟨⟨a0, a1⟩, ⟨a2, b0, b1, b2⟩⟩ => ((a0, a1, a2), (b0, b1, b2))
  left_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
  right_inv := fun ⟨⟨_, _⟩, ⟨_, _, _, _⟩⟩ => rfl

def op (E : S ≃ T × Q) (R : Matrix T T F) : Matrix S S F :=
  (R ⊗ₖ (1 : Matrix Q Q F)).submatrix E E

theorem op_mul (E : S ≃ T × Q) (R R' : Matrix T T F) : op E R * op E R' = op E (R * R') := by
  rw [op, op, op, Matrix.submatrix_mul_equiv _ _ _ E _, ← Matrix.mul_kronecker_mul, Matrix.one_mul]

theorem op_E0 (R : Matrix (Fin 4) (Fin 4) F) :
    op E0 (R.submatrix prU prU) = site0 R ⊗ₖ (1 : Matrix ι ι F) := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E0, site0, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all


def E1 : S ≃ T × Q where
  toFun := fun ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ => ((a1, a2), (a0, b0, b1, b2))
  invFun := fun ⟨⟨a1, a2⟩, ⟨a0, b0, b1, b2⟩⟩ => ((a0, a1, a2), (b0, b1, b2))
  left_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
  right_inv := fun ⟨⟨_, _⟩, ⟨_, _, _, _⟩⟩ => rfl
def E2 : S ≃ T × Q where
  toFun := fun ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ => ((a2, b0), (a0, a1, b1, b2))
  invFun := fun ⟨⟨a2, b0⟩, ⟨a0, a1, b1, b2⟩⟩ => ((a0, a1, a2), (b0, b1, b2))
  left_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
  right_inv := fun ⟨⟨_, _⟩, ⟨_, _, _, _⟩⟩ => rfl
def E3 : S ≃ T × Q where
  toFun := fun ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ => ((b0, b1), (a0, a1, a2, b2))
  invFun := fun ⟨⟨b0, b1⟩, ⟨a0, a1, a2, b2⟩⟩ => ((a0, a1, a2), (b0, b1, b2))
  left_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
  right_inv := fun ⟨⟨_, _⟩, ⟨_, _, _, _⟩⟩ => rfl
def E4 : S ≃ T × Q where
  toFun := fun ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ => ((b1, b2), (a0, a1, a2, b0))
  invFun := fun ⟨⟨b1, b2⟩, ⟨a0, a1, a2, b0⟩⟩ => ((a0, a1, a2), (b0, b1, b2))
  left_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
  right_inv := fun ⟨⟨_, _⟩, ⟨_, _, _, _⟩⟩ => rfl

/-- Three-strand windows `S ≃ ι × ι`. -/
def W12 : S ≃ ι × ι where
  toFun := fun ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ => ((a1, a2, b0), (a0, b1, b2))
  invFun := fun ⟨⟨a1, a2, b0⟩, ⟨a0, b1, b2⟩⟩ => ((a0, a1, a2), (b0, b1, b2))
  left_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
  right_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
def W23 : S ≃ ι × ι where
  toFun := fun ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ => ((a2, b0, b1), (a0, a1, b2))
  invFun := fun ⟨⟨a2, b0, b1⟩, ⟨a0, a1, b2⟩⟩ => ((a0, a1, a2), (b0, b1, b2))
  left_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
  right_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
def V02 : S ≃ ι × ι where
  toFun := fun ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ => ((a0, a1, b1), (a2, b0, b2))
  invFun := fun ⟨⟨a0, a1, b1⟩, ⟨a2, b0, b2⟩⟩ => ((a0, a1, a2), (b0, b1, b2))
  left_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
  right_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
def V24 : S ≃ ι × ι where
  toFun := fun ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ => ((a2, b0, a0), (b1, b2, a1))
  invFun := fun ⟨⟨a2, b0, a0⟩, ⟨b1, b2, a1⟩⟩ => ((a0, a1, a2), (b0, b1, b2))
  left_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl
  right_inv := fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl

theorem op_E1 (R : Matrix (Fin 4) (Fin 4) F) :
    op E1 (R.submatrix prU prU) = site1 R ⊗ₖ (1 : Matrix ι ι F) := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E1, site1, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E3 (R : Matrix (Fin 4) (Fin 4) F) :
    op E3 (R.submatrix prU prU) = (1 : Matrix ι ι F) ⊗ₖ site0 R := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E3, site0, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E4 (R : Matrix (Fin 4) (Fin 4) F) :
    op E4 (R.submatrix prU prU) = (1 : Matrix ι ι F) ⊗ₖ site1 R := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E4, site1, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E1_W (R : Matrix (Fin 4) (Fin 4) F) :
    op E1 (R.submatrix prU prU) = (site0 R ⊗ₖ (1 : Matrix ι ι F)).submatrix W12 W12 := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E1, W12, site0, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E2_W (R : Matrix (Fin 4) (Fin 4) F) :
    op E2 (R.submatrix prU prU) = (site1 R ⊗ₖ (1 : Matrix ι ι F)).submatrix W12 W12 := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E2, W12, site1, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E2_W' (R : Matrix (Fin 4) (Fin 4) F) :
    op E2 (R.submatrix prU prU) = (site0 R ⊗ₖ (1 : Matrix ι ι F)).submatrix W23 W23 := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E2, W23, site0, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E3_W' (R : Matrix (Fin 4) (Fin 4) F) :
    op E3 (R.submatrix prU prU) = (site1 R ⊗ₖ (1 : Matrix ι ι F)).submatrix W23 W23 := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E3, W23, site1, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E0_V (R : Matrix (Fin 4) (Fin 4) F) :
    op E0 (R.submatrix prU prU) = (site0 R ⊗ₖ (1 : Matrix ι ι F)).submatrix V02 V02 := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E0, V02, site0, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E2_V (R : Matrix (Fin 4) (Fin 4) F) :
    op E2 (R.submatrix prU prU) = ((1 : Matrix ι ι F) ⊗ₖ site0 R).submatrix V02 V02 := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E2, V02, site0, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E2_V' (R : Matrix (Fin 4) (Fin 4) F) :
    op E2 (R.submatrix prU prU) = (site0 R ⊗ₖ (1 : Matrix ι ι F)).submatrix V24 V24 := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E2, V24, site0, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all
theorem op_E4_V (R : Matrix (Fin 4) (Fin 4) F) :
    op E4 (R.submatrix prU prU) = ((1 : Matrix ι ι F) ⊗ₖ site0 R).submatrix V24 V24 := by
  ext ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ ⟨⟨c0, c1, c2⟩, ⟨d0, d1, d2⟩⟩
  simp [op, E4, V24, site0, prU, Matrix.kroneckerMap_apply, Matrix.one_apply, ite_and]
  split_ifs <;> simp_all



/-! ### Strand reversal with all strands flipped -/

theorem fl_fl (x : Fin 2) : fl (fl x) = x := by fin_cases x <;> rfl

def πf (x : S) : S := (φ x.2, φ x.1)
def τ (x : T) : T := (fl x.2, fl x.1)
def ρ (x : Q) : Q := (fl x.2.2.2, fl x.2.2.1, fl x.2.1, fl x.1)

theorem πf_πf (x : S) : πf (πf x) = x := by
  obtain ⟨⟨a0, a1, a2⟩, ⟨b0, b1, b2⟩⟩ := x; simp [πf, φ, fl_fl]
theorem ρ_ρ (x : Q) : ρ (ρ x) = x := by
  obtain ⟨a, b, c, d⟩ := x; simp [ρ, fl_fl]
theorem τ_τ (x : T) : τ (τ x) = x := by
  obtain ⟨a, b⟩ := x; simp [τ, fl_fl]

def Θ (N : Matrix S S F) : Matrix S S F := N.submatrix πf πf

theorem Θ_mul (M N : Matrix S S F) : Θ (M * N) = Θ M * Θ N := by
  let e : S ≃ S := ⟨πf, πf, πf_πf, πf_πf⟩
  exact (Matrix.submatrix_mul_equiv M N πf e πf).symm

theorem Θ_trace (N : Matrix S S F) : (Θ N).trace = N.trace := by
  let e : S ≃ S := ⟨πf, πf, πf_πf, πf_πf⟩
  simp only [Θ, Matrix.trace, Matrix.diag_apply, Matrix.submatrix_apply]
  exact Equiv.sum_comp e (fun x => N x x)

theorem E_comp (E E' : S ≃ T × Q) (h : ∀ x, E (πf x) = (τ (E' x).1, ρ (E' x).2))
    (R : Matrix T T F) : Θ (op E R) = op E' (R.submatrix τ τ) := by
  have hρ : Function.Injective ρ := fun a b hab => by simpa [ρ_ρ] using congrArg ρ hab
  ext x y
  simp only [Θ, op, Matrix.submatrix_apply, h, Matrix.kroneckerMap_apply, Matrix.one_apply,
    hρ.eq_iff]

theorem Θ_E0 (R : Matrix T T F) : Θ (op E0 R) = op E4 (R.submatrix τ τ) :=
  E_comp _ _ (fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl) R
theorem Θ_E1 (R : Matrix T T F) : Θ (op E1 R) = op E3 (R.submatrix τ τ) :=
  E_comp _ _ (fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl) R
theorem Θ_E2 (R : Matrix T T F) : Θ (op E2 R) = op E2 (R.submatrix τ τ) :=
  E_comp _ _ (fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl) R
theorem Θ_E3 (R : Matrix T T F) : Θ (op E3 R) = op E1 (R.submatrix τ τ) :=
  E_comp _ _ (fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl) R
theorem Θ_E4 (R : Matrix T T F) : Θ (op E4 R) = op E0 (R.submatrix τ τ) :=
  E_comp _ _ (fun ⟨⟨_, _, _⟩, ⟨_, _, _⟩⟩ => rfl) R


theorem Θ_kron (A B : Matrix ι ι F) : Θ (A ⊗ₖ B) = θ B ⊗ₖ θ A := by
  ext x y; simp [Θ, θ, πf, Matrix.kroneckerMap_apply, mul_comm]

/-- `Ř` is invariant under strand swap with both strands flipped. -/
theorem R4_τ (q : F) : ((R4 q).submatrix prU prU).submatrix τ τ = (R4 q).submatrix prU prU := by
  ext ⟨a, b⟩ ⟨c, d⟩; fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;> rfl
theorem R4i_τ (q : F) : ((R4i q).submatrix prU prU).submatrix τ τ = (R4i q).submatrix prU prU := by
  ext ⟨a, b⟩ ⟨c, d⟩; fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;> rfl



/-! ### Six-strand letters and their relations -/

def win : Fin 5 → (S ≃ T × Q) := ![E0, E1, E2, E3, E4]

/-- Positive crossing on strands `i, i+1` of the six (block A then block B). -/
def σ (q : F) (i : Fin 5) : Matrix S S F := op (win i) ((R4 q).submatrix prU prU)

theorem sub_mul_sub {α : Type*} [Fintype α] [DecidableEq α] (W : S ≃ α) (M N : Matrix α α F) :
    M.submatrix W W * N.submatrix W W = (M * N).submatrix W W :=
  Matrix.submatrix_mul_equiv M N W W W

theorem kron1_mul (A B : Matrix ι ι F) :
    (A ⊗ₖ (1 : Matrix ι ι F)) * (B ⊗ₖ 1) = (A * B) ⊗ₖ 1 := by
  rw [← Matrix.mul_kronecker_mul, Matrix.one_mul]
theorem one_kron_mul (A B : Matrix ι ι F) :
    ((1 : Matrix ι ι F) ⊗ₖ A) * (1 ⊗ₖ B) = 1 ⊗ₖ (A * B) := by
  rw [← Matrix.mul_kronecker_mul, Matrix.one_mul]
theorem kron_comm (A B : Matrix ι ι F) :
    (A ⊗ₖ (1 : Matrix ι ι F)) * (1 ⊗ₖ B) = (1 ⊗ₖ B) * (A ⊗ₖ 1) := by
  rw [← Matrix.mul_kronecker_mul, ← Matrix.mul_kronecker_mul, Matrix.one_mul, Matrix.mul_one,
    Matrix.one_mul, Matrix.mul_one]

theorem σ0 (q : F) : σ q 0 = letter8 q (false, false) ⊗ₖ 1 := op_E0 _
theorem σ1 (q : F) : σ q 1 = letter8 q (true, false) ⊗ₖ 1 := op_E1 _
theorem σ3 (q : F) : σ q 3 = 1 ⊗ₖ letter8 q (false, false) := op_E3 _
theorem σ4 (q : F) : σ q 4 = 1 ⊗ₖ letter8 q (true, false) := op_E4 _

section Relations
variable (q : F)
  (hybe : letter8 q (false, false) * letter8 q (true, false) * letter8 q (false, false)
      = letter8 q (true, false) * letter8 q (false, false) * letter8 q (true, false))
include hybe

theorem ybe01 : σ q 0 * σ q 1 * σ q 0 = σ q 1 * σ q 0 * σ q 1 := by
  rw [σ0, σ1, kron1_mul, kron1_mul, kron1_mul, kron1_mul, hybe]
theorem ybe34 : σ q 3 * σ q 4 * σ q 3 = σ q 4 * σ q 3 * σ q 4 := by
  rw [σ3, σ4, one_kron_mul, one_kron_mul, one_kron_mul, one_kron_mul, hybe]
theorem ybe12 : σ q 1 * σ q 2 * σ q 1 = σ q 2 * σ q 1 * σ q 2 := by
  have h1 : σ q 1 = (letter8 q (false, false) ⊗ₖ 1).submatrix W12 W12 := op_E1_W _
  have h2 : σ q 2 = (letter8 q (true, false) ⊗ₖ 1).submatrix W12 W12 := op_E2_W _
  rw [h1, h2, sub_mul_sub, sub_mul_sub, sub_mul_sub, sub_mul_sub, kron1_mul, kron1_mul,
    kron1_mul, kron1_mul, hybe]
theorem ybe23 : σ q 2 * σ q 3 * σ q 2 = σ q 3 * σ q 2 * σ q 3 := by
  have h2 : σ q 2 = (letter8 q (false, false) ⊗ₖ 1).submatrix W23 W23 := op_E2_W' _
  have h3 : σ q 3 = (letter8 q (true, false) ⊗ₖ 1).submatrix W23 W23 := op_E3_W' _
  rw [h2, h3, sub_mul_sub, sub_mul_sub, sub_mul_sub, sub_mul_sub, kron1_mul, kron1_mul,
    kron1_mul, kron1_mul, hybe]
end Relations

theorem far02 (q : F) : σ q 0 * σ q 2 = σ q 2 * σ q 0 := by
  have h0 : σ q 0 = (letter8 q (false, false) ⊗ₖ 1).submatrix V02 V02 := op_E0_V _
  have h2 : σ q 2 = (1 ⊗ₖ letter8 q (false, false)).submatrix V02 V02 := op_E2_V _
  rw [h0, h2, sub_mul_sub, sub_mul_sub, kron_comm]
theorem far24 (q : F) : σ q 2 * σ q 4 = σ q 4 * σ q 2 := by
  have h2 : σ q 2 = (letter8 q (false, false) ⊗ₖ 1).submatrix V24 V24 := op_E2_V' _
  have h4 : σ q 4 = (1 ⊗ₖ letter8 q (false, false)).submatrix V24 V24 := op_E4_V _
  rw [h2, h4, sub_mul_sub, sub_mul_sub, kron_comm]
theorem far03 (q : F) : σ q 0 * σ q 3 = σ q 3 * σ q 0 := by rw [σ0, σ3, kron_comm]
theorem far04 (q : F) : σ q 0 * σ q 4 = σ q 4 * σ q 0 := by rw [σ0, σ4, kron_comm]
theorem far13 (q : F) : σ q 1 * σ q 3 = σ q 3 * σ q 1 := by rw [σ1, σ3, kron_comm]
theorem far14 (q : F) : σ q 1 * σ q 4 = σ q 4 * σ q 1 := by rw [σ1, σ4, kron_comm]

theorem Θ_σ0 (q : F) : Θ (σ q 0) = σ q 4 := by
  change Θ (op E0 _) = op E4 _; rw [Θ_E0, R4_τ]
theorem Θ_σ1 (q : F) : Θ (σ q 1) = σ q 3 := by
  change Θ (op E1 _) = op E3 _; rw [Θ_E1, R4_τ]
theorem Θ_σ2 (q : F) : Θ (σ q 2) = σ q 2 := by
  change Θ (op E2 _) = op E2 _; rw [Θ_E2, R4_τ]
theorem Θ_σ3 (q : F) : Θ (σ q 3) = σ q 1 := by
  change Θ (op E3 _) = op E1 _; rw [Θ_E3, R4_τ]
theorem Θ_σ4 (q : F) : Θ (σ q 4) = σ q 0 := by
  change Θ (op E4 _) = op E0 _; rw [Θ_E4, R4_τ]



/-! ### Words and the full twist -/

def σw (q : F) (l : List (Fin 5)) : Matrix S S F := (l.map (σ q)).prod

theorem sw (q : F) (l1 l2 : List (Fin 5)) (a b : Fin 5) (h : σ q a * σ q b = σ q b * σ q a) :
    σw q (l1 ++ a :: b :: l2) = σw q (l1 ++ b :: a :: l2) := by
  simp only [σw, List.map_append, List.map_cons, List.prod_append, List.prod_cons, ← mul_assoc, h]

theorem yb (q : F) (l1 l2 : List (Fin 5)) (a b : Fin 5)
    (h : σ q a * σ q b * σ q a = σ q b * σ q a * σ q b) :
    σw q (l1 ++ a :: b :: a :: l2) = σw q (l1 ++ b :: a :: b :: l2) := by
  simp only [σw, List.map_append, List.map_cons, List.prod_append, List.prod_cons, ← mul_assoc, h]

theorem σw_snoc (q : F) (l : List (Fin 5)) (a : Fin 5) : σw q (l ++ [a]) = σw q l * σ q a := by
  simp [σw, List.prod_append]
theorem σw_cons (q : F) (l : List (Fin 5)) (a : Fin 5) : σw q (a :: l) = σ q a * σw q l := by
  simp [σw]

/-- `β`: block A passes over block B (three strands over three). -/
def cw : List (Fin 5) := [2, 3, 4, 1, 2, 3, 0, 1, 2]
def dw : List (Fin 5) := [2, 1, 0, 3, 2, 1, 4, 3, 2]

theorem c_eq_d (q : F) : σw q cw = σw q dw := by
  have s1 := sw q [2, 3] [2, 3, 0, 1, 2] 4 1 (far14 q).symm
  have s2 := sw q [2] [4, 2, 3, 0, 1, 2] 3 1 (far13 q).symm
  have s3 := sw q [2, 1, 3, 4, 2] [1, 2] 3 0 (far03 q).symm
  have s4 := sw q [2, 1, 3, 4] [3, 1, 2] 2 0 (far02 q).symm
  have s5 := sw q [2, 1, 3] [2, 3, 1, 2] 4 0 (far04 q).symm
  have s6 := sw q [2, 1] [4, 2, 3, 1, 2] 3 0 (far03 q).symm
  have s7 := sw q [2, 1, 0, 3] [3, 1, 2] 4 2 (far24 q).symm
  have s8 := sw q [2, 1, 0, 3, 2, 4] [2] 3 1 (far13 q).symm
  have s9 := sw q [2, 1, 0, 3, 2] [3, 2] 4 1 (far14 q).symm
  simp only [List.cons_append, List.nil_append] at s1 s2 s3 s4 s5 s6 s7 s8 s9
  rw [cw, dw, s1, s2, s3, s4, s5, s6, s7, s8, s9]

section Twist
variable (q : F)
  (hybe : letter8 q (false, false) * letter8 q (true, false) * letter8 q (false, false)
      = letter8 q (true, false) * letter8 q (false, false) * letter8 q (true, false))
include hybe

theorem β_σ0 : σw q cw * σ q 0 = σ q 3 * σw q cw := by
  have s1 := sw q [2, 3, 4, 1, 2, 3, 0, 1] [] 2 0 (far02 q).symm
  have s2 := yb q [2, 3, 4, 1, 2, 3] [2] 0 1 (ybe01 q hybe)
  have s3 := sw q [2, 3, 4, 1, 2] [0, 1, 2] 3 1 (far13 q).symm
  have s4 := yb q [2, 3, 4] [3, 0, 1, 2] 1 2 (ybe12 q hybe)
  have s5 := sw q [2, 3] [1, 2, 3, 0, 1, 2] 4 2 (far24 q).symm
  have s6 := yb q [] [4, 1, 2, 3, 0, 1, 2] 2 3 (ybe23 q hybe)
  simp only [List.cons_append, List.nil_append] at s1 s2 s3 s4 s5 s6
  rw [← σw_snoc, ← σw_cons, cw]
  simp only [List.cons_append, List.nil_append]
  rw [s1, s2, s3, s4, s5, s6]

theorem β_σ1 : σw q cw * σ q 1 = σ q 4 * σw q cw := by
  have s1 := yb q [2, 3, 4, 1, 2, 3, 0] [] 1 2 (ybe12 q hybe)
  have s2 := sw q [2, 3, 4, 1, 2, 3] [1, 2] 0 2 (far02 q)
  have s3 := yb q [2, 3, 4, 1] [0, 1, 2] 2 3 (ybe23 q hybe)
  have s4 := sw q [2, 3, 4] [2, 3, 0, 1, 2] 1 3 (far13 q)
  have s5 := yb q [2] [1, 2, 3, 0, 1, 2] 3 4 (ybe34 q hybe)
  have s6 := sw q [] [3, 4, 1, 2, 3, 0, 1, 2] 2 4 (far24 q)
  simp only [List.cons_append, List.nil_append] at s1 s2 s3 s4 s5 s6
  rw [← σw_snoc, ← σw_cons, cw]
  simp only [List.cons_append, List.nil_append]
  rw [s1, s2, s3, s4, s5, s6]

theorem β_σ3 : σw q cw * σ q 3 = σ q 0 * σw q cw := by
  rw [c_eq_d]
  have s1 := yb q [2, 1, 0, 3, 2, 1, 4] [] 3 2 (ybe23 q hybe).symm
  have s2 := sw q [2, 1, 0, 3, 2, 1] [3, 2] 4 2 (far24 q).symm
  have s3 := yb q [2, 1, 0, 3] [4, 3, 2] 2 1 (ybe12 q hybe).symm
  have s4 := sw q [2, 1, 0] [2, 1, 4, 3, 2] 3 1 (far13 q).symm
  have s5 := yb q [2] [3, 2, 1, 4, 3, 2] 1 0 (ybe01 q hybe).symm
  have s6 := sw q [] [1, 0, 3, 2, 1, 4, 3, 2] 2 0 (far02 q).symm
  simp only [List.cons_append, List.nil_append] at s1 s2 s3 s4 s5 s6
  rw [← σw_snoc, ← σw_cons, dw]
  simp only [List.cons_append, List.nil_append]
  rw [s1, s2, s3, s4, s5, s6]

theorem β_σ4 : σw q cw * σ q 4 = σ q 1 * σw q cw := by
  rw [c_eq_d]
  have s1 := sw q [2, 1, 0, 3, 2, 1, 4, 3] [] 2 4 (far24 q)
  have s2 := yb q [2, 1, 0, 3, 2, 1] [2] 4 3 (ybe34 q hybe).symm
  have s3 := sw q [2, 1, 0, 3, 2] [4, 3, 2] 1 3 (far13 q)
  have s4 := yb q [2, 1, 0] [1, 4, 3, 2] 3 2 (ybe23 q hybe).symm
  have s5 := sw q [2, 1] [3, 2, 1, 4, 3, 2] 0 2 (far02 q)
  have s6 := yb q [] [0, 3, 2, 1, 4, 3, 2] 2 1 (ybe12 q hybe).symm
  simp only [List.cons_append, List.nil_append] at s1 s2 s3 s4 s5 s6
  rw [← σw_snoc, ← σw_cons, dw]
  simp only [List.cons_append, List.nil_append]
  rw [s1, s2, s3, s4, s5, s6]

/-- The full twist `M = β²` commutes with every in-block positive letter. -/
theorem M_σ0 : Commute (σw q cw * σw q cw) (σ q 0) := by
  unfold Commute SemiconjBy
  rw [mul_assoc, β_σ0 q hybe, ← mul_assoc, β_σ3 q hybe, mul_assoc]
theorem M_σ1 : Commute (σw q cw * σw q cw) (σ q 1) := by
  unfold Commute SemiconjBy
  rw [mul_assoc, β_σ1 q hybe, ← mul_assoc, β_σ4 q hybe, mul_assoc]
theorem M_σ3 : Commute (σw q cw * σw q cw) (σ q 3) := by
  unfold Commute SemiconjBy
  rw [mul_assoc, β_σ3 q hybe, ← mul_assoc, β_σ0 q hybe, mul_assoc]
theorem M_σ4 : Commute (σw q cw * σw q cw) (σ q 4) := by
  unfold Commute SemiconjBy
  rw [mul_assoc, β_σ4 q hybe, ← mul_assoc, β_σ1 q hybe, mul_assoc]
end Twist

theorem Θ_one : Θ (1 : Matrix S S F) = 1 := by
  have hinj : Function.Injective πf := fun a b h => by simpa [πf_πf] using congrArg πf h
  ext x y; simp only [Θ, Matrix.submatrix_apply, Matrix.one_apply, hinj.eq_iff]

def mir (i : Fin 5) : Fin 5 := 4 - i

theorem Θ_σ (q : F) (i : Fin 5) : Θ (σ q i) = σ q (mir i) := by
  fin_cases i
  · exact Θ_σ0 q
  · exact Θ_σ1 q
  · exact Θ_σ2 q
  · exact Θ_σ3 q
  · exact Θ_σ4 q

theorem Θ_σw (q : F) (l : List (Fin 5)) : Θ (σw q l) = σw q (l.map mir) := by
  induction l with
  | nil => simp [σw, Θ_one]
  | cons a l ih => rw [σw_cons, Θ_mul, ih, Θ_σ, List.map_cons, σw_cons]

theorem Θ_M (q : F) : Θ (σw q cw * σw q cw) = σw q cw * σw q cw := by
  rw [Θ_mul, Θ_σw, show cw.map mir = dw by decide, ← c_eq_d]


/-! ## The half twist `Δ` on one block -/

theorem conj_of {R : Type*} [Monoid R] {D a b a' b' : R} (h : D * a = b * D) (ha : a * a' = 1)
    (hb : b' * b = 1) : D * a' = b' * D := by
  calc D * a' = (b' * b) * D * a' := by rw [hb, one_mul]
    _ = b' * (D * a) * a' := by rw [h]; simp only [mul_assoc]
    _ = b' * D * (a * a') := by simp only [mul_assoc]
    _ = b' * D := by rw [ha, mul_one]

theorem commute_inv {R : Type*} [Monoid R] {x a a' : R} (h : Commute a x) (h1 : a * a' = 1)
    (h2 : a' * a = 1) : Commute a' x :=
  (conj_of h.eq.symm h1 h2).symm

def Δ8 (q : F) : Matrix ι ι F := word8 q [(false, false), (true, false), (false, false)]
def Δ8i (q : F) : Matrix ι ι F := word8 q [(false, true), (true, true), (false, true)]

theorem Δ8_mul (q : F) (hq : q ≠ 0) : Δ8 q * Δ8i q = 1 := by
  simp only [Δ8, Δ8i, word8, mul_one, mul_assoc]
  rw [← mul_assoc (letter8 q (false, false)) (letter8 q (false, true)), letter_inv q hq, one_mul,
    ← mul_assoc (letter8 q (true, false)) (letter8 q (true, true)), letter_inv q hq, one_mul,
    letter_inv q hq]

theorem Δ8i_mul (q : F) (hq : q ≠ 0) : Δ8i q * Δ8 q = 1 := by
  simp only [Δ8, Δ8i, word8, mul_one, mul_assoc]
  rw [← mul_assoc (letter8 q (false, true)) (letter8 q (false, false)), letter_inv' q hq, one_mul,
    ← mul_assoc (letter8 q (true, true)) (letter8 q (true, false)), letter_inv' q hq, one_mul,
    letter_inv' q hq]

theorem Δ_letter (q : F) (hq : q ≠ 0) (l : Letter) :
    Δ8 q * letter8 q l = letter8 q (swapL l) * Δ8 q := by
  have h0 : Δ8 q * letter8 q (false, false) = letter8 q (true, false) * Δ8 q := by
    simp only [Δ8, word8, mul_one, ← mul_assoc]; rw [ybe8 q hq]
  have h1 : Δ8 q * letter8 q (true, false) = letter8 q (false, false) * Δ8 q := by
    have h := congrArg (letter8 q (false, false) * ·) (ybe8 q hq)
    simp only [← mul_assoc] at h
    simp only [Δ8, word8, mul_one, ← mul_assoc]
    exact h.symm
  obtain ⟨g, i⟩ := l
  cases g <;> cases i
  · exact h0
  · exact conj_of h0 (letter_inv q hq false) (letter_inv' q hq true)
  · exact h1
  · exact conj_of h1 (letter_inv q hq true) (letter_inv' q hq false)

theorem Δ_word (q : F) (hq : q ≠ 0) (w : List Letter) :
    Δ8 q * word8 q w = word8 q (w.map swapL) * Δ8 q := by
  induction w with
  | nil => simp [word8]
  | cons l w ih =>
    simp only [word8, List.map_cons]
    rw [← mul_assoc, Δ_letter q hq, mul_assoc, ih, mul_assoc]

theorem θ_word (q : F) (w : List Letter) : θ (word8 q w) = word8 q (w.map swapL) := by
  induction w with
  | nil => simp [word8, θ_one]
  | cons l w ih => simp only [word8, List.map_cons, θ_mul, θ_letter, ih]

theorem word_swap_eq (q : F) (hq : q ≠ 0) (w : List Letter) :
    word8 q (w.map swapL) = Δ8 q * word8 q w * Δ8i q := by
  rw [Δ_word q hq, mul_assoc, Δ8_mul q hq, mul_one]

/-- Anything commuting with both positive letters commutes with every word. -/
theorem word_comm (q : F) (hq : q ≠ 0) {x : Matrix ι ι F}
    (h0 : Commute (letter8 q (false, false)) x) (h1 : Commute (letter8 q (true, false)) x) :
    ∀ w, Commute (word8 q w) x := by
  have hl : ∀ l, Commute (letter8 q l) x := by
    rintro ⟨g, i⟩
    cases g <;> cases i
    · exact h0
    · exact commute_inv h0 (letter_inv q hq false) (letter_inv' q hq false)
    · exact h1
    · exact commute_inv h1 (letter_inv q hq true) (letter_inv' q hq true)
  intro w
  induction w with
  | nil => exact Commute.one_left x
  | cons l w ih => exact (hl l).mul_left ih

theorem K3_mul (q : F) (hq : q ≠ 0) : K3 q * K3i q = 1 := by
  have hk : ∀ i, kv q i ≠ 0 := by
    rintro ⟨a, b, c⟩; simp only [kv, kv1]; split_ifs <;> simp [hq]
  rw [K3, K3i, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1; funext i; exact mul_inv_cancel₀ (hk i)
theorem K3i_mul (q : F) (hq : q ≠ 0) : K3i q * K3 q = 1 := by
  have hk : ∀ i, kv q i ≠ 0 := by
    rintro ⟨a, b, c⟩; simp only [kv, kv1]; split_ifs <;> simp [hq]
  rw [K3, K3i, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1; funext i; exact inv_mul_cancel₀ (hk i)

theorem Δ_e (q : F) (hq : q ≠ 0) : Commute (Δ8 q) (e3 q) := word_comm q hq (l0_e q hq) (l1_e q hq) _
theorem Δ_f (q : F) (hq : q ≠ 0) : Commute (Δ8 q) (f3 q) := word_comm q hq (l0_f q hq) (l1_f q hq) _
theorem Δ_K (q : F) (hq : q ≠ 0) : Commute (Δ8 q) (K3 q) := word_comm q hq (l0_K q hq) (l1_K q hq) _
theorem Δ_Ki (q : F) (hq : q ≠ 0) : Commute (Δ8 q) (K3i q) :=
  (commute_inv (Δ_K q hq).symm (K3_mul q hq) (K3i_mul q hq)).symm
theorem Δ_cas (q h : F) (hq : q ≠ 0) :
    Commute (Δ8 q) (blockCas q h (e3 q) (f3 q) (K3 q) (K3i q)) := by
  unfold blockCas
  exact ((((Δ_f q hq).mul_right (Δ_e q hq)).smul_right _).add_right ((Δ_K q hq).smul_right _)).add_right
    ((Δ_Ki q hq).smul_right _)

/-! ## The pair operator is reversal-invariant and commutes with `Δ ⊗ Δ` -/

theorem θ_add (A B : Matrix ι ι F) : θ (A + B) = θ A + θ B := by ext; simp [θ]
theorem θ_smul (c : F) (A : Matrix ι ι F) : θ (c • A) = c • θ A := by ext; simp [θ]
theorem Θ_add (A B : Matrix S S F) : Θ (A + B) = Θ A + Θ B := by ext; simp [Θ]
theorem Θ_sub (A B : Matrix S S F) : Θ (A - B) = Θ A - Θ B := by ext; simp [Θ]
theorem Θ_smul (c : F) (A : Matrix S S F) : Θ (c • A) = c • Θ A := by ext; simp [Θ]

theorem θ_cas (q : F) (hq : q ≠ 0) :
    θ (blockCas q (q - q⁻¹) (e3 q) (f3 q) (K3 q) (K3i q))
      = blockCas q (q - q⁻¹) (e3 q) (f3 q) (K3 q) (K3i q) := by
  have hrel := efK q hq
  have key : (q - q⁻¹) ^ 2 • (e3 q * f3 q)
      = (q - q⁻¹) ^ 2 • (f3 q * e3 q) + (q - q⁻¹) • (K3 q - K3i q) := by
    rw [← hrel]; simp only [smul_sub, smul_smul, ← sq]; abel
  simp only [blockCas, θ_add, θ_smul, θ_mul, θ_e3, θ_f3, θ_K3 q hq, θ_K3i q hq, key]
  simp only [sub_smul, smul_sub]; abel

theorem sub_kron (A B C : Matrix ι ι F) : (A - B) ⊗ₖ C = A ⊗ₖ C - B ⊗ₖ C := by
  ext; simp [Matrix.kroneckerMap_apply, _root_.sub_mul]
theorem kron_sub (A B C : Matrix ι ι F) : A ⊗ₖ (B - C) = A ⊗ₖ B - A ⊗ₖ C := by
  ext; simp [Matrix.kroneckerMap_apply, _root_.mul_sub]

/-- `h(ΔeΔf − ΔfΔe) = K⊗K − K⁻¹⊗K⁻¹` on the two blocks. -/
theorem pair_efK (q : F) (hq : q ≠ 0) :
    (q - q⁻¹) • ((e3 q ⊗ₖ K3 q + 1 ⊗ₖ e3 q) * (f3 q ⊗ₖ 1 + K3i q ⊗ₖ f3 q)
      - (f3 q ⊗ₖ 1 + K3i q ⊗ₖ f3 q) * (e3 q ⊗ₖ K3 q + 1 ⊗ₖ e3 q))
      = K3 q ⊗ₖ K3 q - K3i q ⊗ₖ K3i q := by
  have key : (e3 q * K3i q) ⊗ₖ (K3 q * f3 q) = (K3i q * e3 q) ⊗ₖ (f3 q * K3 q) := by
    rw [eKi q hq, Kf q hq, Matrix.smul_kronecker, Matrix.kronecker_smul, smul_smul,
      mul_inv_cancel₀ (pow_ne_zero 2 hq), one_smul]
  have expand : (e3 q ⊗ₖ K3 q + 1 ⊗ₖ e3 q) * (f3 q ⊗ₖ 1 + K3i q ⊗ₖ f3 q)
      - (f3 q ⊗ₖ 1 + K3i q ⊗ₖ f3 q) * (e3 q ⊗ₖ K3 q + 1 ⊗ₖ e3 q)
      = (e3 q * f3 q - f3 q * e3 q) ⊗ₖ K3 q + K3i q ⊗ₖ (e3 q * f3 q - f3 q * e3 q) := by
    simp only [add_mul, mul_add, ← Matrix.mul_kronecker_mul, Matrix.one_mul, Matrix.mul_one, key,
      sub_kron, kron_sub]
    abel
  rw [expand, smul_add, ← Matrix.smul_kronecker, ← Matrix.kronecker_smul, efK q hq,
    sub_kron, kron_sub]
  abel

/-- The two-nucleon pair operator `X = h²C_AB − h²C_A − h²C_B`, both blocks alike. -/
def Xp (q : F) : Matrix S S F :=
  pairX q (q - q⁻¹) (e3 q) (f3 q) (K3 q) (K3i q) (e3 q) (f3 q) (K3 q) (K3i q)

theorem Θ_X (q : F) (hq : q ≠ 0) : Θ (Xp q) = Xp q := by
  have hrel := pair_efK q hq
  have key : (q - q⁻¹) ^ 2 • ((e3 q ⊗ₖ K3 q + 1 ⊗ₖ e3 q) * (f3 q ⊗ₖ 1 + K3i q ⊗ₖ f3 q))
      = (q - q⁻¹) ^ 2 • ((f3 q ⊗ₖ 1 + K3i q ⊗ₖ f3 q) * (e3 q ⊗ₖ K3 q + 1 ⊗ₖ e3 q))
        + (q - q⁻¹) • (K3 q ⊗ₖ K3 q - K3i q ⊗ₖ K3i q) := by
    rw [← hrel]; simp only [smul_sub, smul_smul, ← sq]; abel
  simp only [Xp, pairX, Θ_add, Θ_sub, Θ_smul, Θ_mul, Θ_kron, θ_one, θ_e3, θ_f3, θ_K3 q hq,
    θ_K3i q hq, θ_cas q hq]
  rw [add_comm (1 ⊗ₖ e3 q) (e3 q ⊗ₖ K3 q), add_comm (K3i q ⊗ₖ f3 q) (f3 q ⊗ₖ 1), key]
  simp only [sub_smul, smul_sub]
  abel

theorem kron_commute {D A B : Matrix ι ι F} (hA : Commute D A) (hB : Commute D B) :
    Commute (D ⊗ₖ D) (A ⊗ₖ B) := by
  unfold Commute SemiconjBy
  rw [← Matrix.mul_kronecker_mul, ← Matrix.mul_kronecker_mul, hA.eq, hB.eq]

theorem D_X (q : F) (hq : q ≠ 0) : Commute (Δ8 q ⊗ₖ Δ8 q) (Xp q) := by
  have h1 : Commute (Δ8 q) (1 : Matrix ι ι F) := Commute.one_right _
  have he := Δ_e q hq
  have hf := Δ_f q hq
  have hK := Δ_K q hq
  have hKi := Δ_Ki q hq
  have hC := Δ_cas q (q - q⁻¹) hq
  have t1 := ((kron_commute hf h1).add_right (kron_commute hKi hf)).mul_right
    ((kron_commute he hK).add_right (kron_commute h1 he))
  have t2 := ((t1.smul_right ((q - q⁻¹) ^ 2)).add_right ((kron_commute hK hK).smul_right q)).add_right
    ((kron_commute hKi hKi).smul_right q⁻¹)
  exact (t2.sub_right (kron_commute hC h1)).sub_right (kron_commute h1 hC)

/-! ## The full twist commutes with `Δ ⊗ Δ` -/

def Mt (q : F) : Matrix S S F := σw q cw * σw q cw

theorem M_wordA (q : F) (hq : q ≠ 0) (w : List Letter) :
    Commute (Mt q) (word8 q w ⊗ₖ (1 : Matrix ι ι F)) := by
  have hl : ∀ l, Commute (Mt q) (letter8 q l ⊗ₖ (1 : Matrix ι ι F)) := by
    have h0 : Commute (Mt q) (letter8 q (false, false) ⊗ₖ (1 : Matrix ι ι F)) := by
      rw [← σ0]; exact M_σ0 q (ybe8 q hq)
    have h1 : Commute (Mt q) (letter8 q (true, false) ⊗ₖ (1 : Matrix ι ι F)) := by
      rw [← σ1]; exact M_σ1 q (ybe8 q hq)
    rintro ⟨g, i⟩
    cases g <;> cases i
    · exact h0
    · exact (commute_inv h0.symm (by rw [kron1_mul, letter_inv q hq, Matrix.one_kronecker_one])
        (by rw [kron1_mul, letter_inv' q hq, Matrix.one_kronecker_one])).symm
    · exact h1
    · exact (commute_inv h1.symm (by rw [kron1_mul, letter_inv q hq, Matrix.one_kronecker_one])
        (by rw [kron1_mul, letter_inv' q hq, Matrix.one_kronecker_one])).symm
  induction w with
  | nil => simp only [word8, Matrix.one_kronecker_one]; exact Commute.one_right _
  | cons l w ih => rw [word8, ← kron1_mul]; exact (hl l).mul_right ih

theorem M_wordB (q : F) (hq : q ≠ 0) (w : List Letter) :
    Commute (Mt q) ((1 : Matrix ι ι F) ⊗ₖ word8 q w) := by
  have hl : ∀ l, Commute (Mt q) ((1 : Matrix ι ι F) ⊗ₖ letter8 q l) := by
    have h0 : Commute (Mt q) ((1 : Matrix ι ι F) ⊗ₖ letter8 q (false, false)) := by
      rw [← σ3]; exact M_σ3 q (ybe8 q hq)
    have h1 : Commute (Mt q) ((1 : Matrix ι ι F) ⊗ₖ letter8 q (true, false)) := by
      rw [← σ4]; exact M_σ4 q (ybe8 q hq)
    rintro ⟨g, i⟩
    cases g <;> cases i
    · exact h0
    · exact (commute_inv h0.symm (by rw [one_kron_mul, letter_inv q hq, Matrix.one_kronecker_one])
        (by rw [one_kron_mul, letter_inv' q hq, Matrix.one_kronecker_one])).symm
    · exact h1
    · exact (commute_inv h1.symm (by rw [one_kron_mul, letter_inv q hq, Matrix.one_kronecker_one])
        (by rw [one_kron_mul, letter_inv' q hq, Matrix.one_kronecker_one])).symm
  induction w with
  | nil => simp only [word8, Matrix.one_kronecker_one]; exact Commute.one_right _
  | cons l w ih => rw [word8, ← one_kron_mul]; exact (hl l).mul_right ih

theorem D_M (q : F) (hq : q ≠ 0) : Commute (Δ8 q ⊗ₖ Δ8 q) (Mt q) := by
  have hsplit : Δ8 q ⊗ₖ Δ8 q = (Δ8 q ⊗ₖ (1 : Matrix ι ι F)) * (1 ⊗ₖ Δ8 q) := by
    rw [← Matrix.mul_kronecker_mul, Matrix.mul_one, Matrix.one_mul]
  rw [hsplit]
  exact ((M_wordA q hq [(false, false), (true, false), (false, false)]).symm.mul_left
    (M_wordB q hq [(false, false), (true, false), (false, false)]).symm)

theorem Θ_Mt (q : F) (hq : q ≠ 0) : Θ (Mt q) = Mt q := Θ_M q

/-! ## The readout symmetry -/

/-- Two-nucleon sector readout `Tr((P_a K w_A) ⊗ (P_b K w_B) · Y)`. -/
def rd (q : F) (a b : Bool) (wA wB : List Letter) (Y : Matrix S S F) : F :=
  (((P a * K3 q * word8 q wA) ⊗ₖ (P b * K3 q * word8 q wB)) * Y).trace

theorem PKi_nn (q : F) (hq : q ≠ 0) :
    P false * K3i q = q ^ 2 • (P false * K3 q) := by
  have hs := sector q hq false []
  rw [hs.commKi, hs.eigKi, hs.commK, hs.eigK, smul_smul]
  congr 1
  simp only [kOf, Bool.false_eq_true, ↓reduceIte, inv_inv]
  field_simp

theorem block_image (q : F) (hq : q ≠ 0) (w : List Letter) :
    θ (P true * K3 q * word8 q w)
      = q ^ 2 • (Δ8 q * (P false * K3 q * word8 q w) * Δ8i q) := by
  have hP : P false * Δ8 q = Δ8 q * P false := P_comm_pres false (word_pres q _)
  have hK : K3 q * Δ8 q = Δ8 q * K3 q := (Δ_K q hq).eq.symm
  rw [θ_mul, θ_mul, θ_P, θ_K3 q hq, θ_word, word_swap_eq q hq, Bool.not_true, PKi_nn q hq,
    Matrix.smul_mul]
  congr 1
  simp only [← Matrix.mul_assoc]
  rw [Matrix.mul_assoc (P false) (K3 q) (Δ8 q), hK, ← Matrix.mul_assoc, hP]

/-- **Strand-reversal symmetry.** For any `Y` fixed by the reversal and commuting with `Δ ⊗ Δ`,
`T_pp(w_A, w_B; Y) = q⁴ · T_nn(w_B, w_A; Y)`, exactly in `q`. -/
theorem rd_sym (q : F) (hq : q ≠ 0) (wA wB : List Letter) (Y : Matrix S S F)
    (hΘ : Θ Y = Y) (hD : Commute (Δ8 q ⊗ₖ Δ8 q) Y) :
    rd q true true wA wB Y = q ^ 4 * rd q false false wB wA Y := by
  have hinv : (Δ8i q ⊗ₖ Δ8i q) * (Δ8 q ⊗ₖ Δ8 q) = 1 := by
    rw [← Matrix.mul_kronecker_mul, Δ8i_mul q hq, Matrix.one_kronecker_one]
  have hconj : θ (P true * K3 q * word8 q wB) ⊗ₖ θ (P true * K3 q * word8 q wA)
      = q ^ 4 • ((Δ8 q ⊗ₖ Δ8 q) * ((P false * K3 q * word8 q wB) ⊗ₖ (P false * K3 q * word8 q wA))
          * (Δ8i q ⊗ₖ Δ8i q)) := by
    rw [block_image q hq wB, block_image q hq wA, Matrix.smul_kronecker, Matrix.kronecker_smul,
      smul_smul, Matrix.mul_kronecker_mul, Matrix.mul_kronecker_mul]
    congr 1; ring
  rw [rd, ← Θ_trace, Θ_mul, Θ_kron, hΘ, hconj, Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul, rd]
  congr 1
  set D := Δ8 q ⊗ₖ Δ8 q
  set Di := Δ8i q ⊗ₖ Δ8i q
  set N := (P false * K3 q * word8 q wB) ⊗ₖ (P false * K3 q * word8 q wA)
  rw [Matrix.mul_assoc (D * N) Di Y, Matrix.mul_assoc D N, Matrix.trace_mul_comm D,
    Matrix.mul_assoc N, Matrix.mul_assoc Di Y D, ← hD.eq, ← Matrix.mul_assoc Di D Y, hinv,
    Matrix.one_mul]

/-- **pp = nn for the full-twist core.** With the same in-block word in both nucleons and the
full twist `β²` appended, the pre-registered cross product of §35 vanishes identically in `q`:
`T_X[pp]·T_1[nn] = T_X[nn]·T_1[pp]`. -/
theorem fullTwist_pp_eq_nn (q : F) (hq : q ≠ 0) (w : List Letter) :
    rd q true true w w (Mt q * Xp q) * rd q false false w w (Mt q)
      = rd q false false w w (Mt q * Xp q) * rd q true true w w (Mt q) := by
  rw [rd_sym q hq w w _ (by rw [Θ_mul, Θ_Mt q hq, Θ_X q hq]) ((D_M q hq).mul_right (D_X q hq)),
    rd_sym q hq w w _ (Θ_Mt q hq) (D_M q hq)]
  ring


end QOU.QBeta.PairMonodromySymmetry
