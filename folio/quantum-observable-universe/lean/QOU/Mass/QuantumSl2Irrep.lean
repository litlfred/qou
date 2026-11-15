import QOU.Mass.QuantumSl2Fundamental

/-!
# The `(m+1)`-dimensional irreducible representation of `U_q(sl₂)`

`QuantumSl2Fundamental.lean` gives the representation-data structure `Rep q ι`, the
coproduct and the 2-dimensional fundamental. This file gives the general
`(m+1)`-dimensional representation `V_{m+1}` (highest weight `m`), the input to the
colored Jones polynomial `J_N` with `N = m+1`.

## Conventions

Base: a generic field `𝕜` (§7c), `q ≠ 0`, `q − q⁻¹ ≠ 0`. Basis `v_0, …, v_m` with
`v_0` the highest-weight vector (Kassel, *Quantum Groups*, Thm VI.3.5, `V_{1,m}`):

* `K v_p = q^{m−2p} v_p`,
* `E v_p = [m−p+1] v_{p−1}` (and `E v_0 = 0`),
* `F v_p = [p+1] v_{p+1}` (and `F v_m = 0`),

with `[k] = (q^k − q^{−k})/(q − q⁻¹)`. The relation `[E,F] = (K − K⁻¹)/(q − q⁻¹)` reduces
to the quantum-integer identity `[m−p][p+1] − [p][m−p+1] = [m−2p]`
(`qint_commutator`).

Matrix convention: column `j` is the image of `v_j`, so `E` has entries on the
superdiagonal (`E_{j−1,j}`) and `F` on the subdiagonal (`F_{j+1,j}`).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VI §3
-/

namespace QOU.Mass.QuantumSl2

open Matrix

variable {𝕜 : Type*} [Field 𝕜]

/-- The quantum integer `[k] = (q^k − q^{−k})/(q − q⁻¹)`. -/
def qint (q : 𝕜) (k : ℕ) : 𝕜 := (q ^ k - q⁻¹ ^ k) / (q - q⁻¹)

@[simp] theorem qint_zero (q : 𝕜) : qint q 0 = 0 := by simp [qint]

/-- The quantum-integer identity behind `[E,F] = (K − K⁻¹)/(q − q⁻¹)`:
`[a][p+1] − [p][a+1] = (q^a q^{−p} − q^{−a} q^p)/(q − q⁻¹)`, i.e. `[a − p]` when `a ≥ p`.
Used with `a = m − p`. -/
theorem qint_commutator (q : 𝕜) (hq : q ≠ 0) (a p : ℕ) :
    qint q a * qint q (p + 1) - qint q p * qint q (a + 1)
      = (q - q⁻¹)⁻¹ * (q ^ a * q⁻¹ ^ p - q⁻¹ ^ a * q ^ p) := by
  unfold qint
  simp only [pow_succ, inv_pow]
  have ha : q ^ a ≠ 0 := pow_ne_zero _ hq
  have hp : q ^ p ≠ 0 := pow_ne_zero _ hq
  set A := q ^ a
  set P := q ^ p
  have key : (A - A⁻¹) * (P * q - P⁻¹ * q⁻¹) - (P - P⁻¹) * (A * q - A⁻¹ * q⁻¹)
      = (q - q⁻¹) * (A * P⁻¹ - A⁻¹ * P) := by
    field_simp; ring
  rw [div_mul_div_comm, div_mul_div_comm, ← sub_div, key]
  field_simp

variable (q : 𝕜)

/-- `E` on `V_{m+1}`: `E v_j = [m−j+1] v_{j−1}`. -/
def irrepE (m : ℕ) : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜 :=
  fun i j => if (i : ℕ) + 1 = j then qint q (m - j + 1) else 0

/-- `F` on `V_{m+1}`: `F v_j = [j+1] v_{j+1}`. -/
def irrepF (m : ℕ) : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜 :=
  fun i j => if (i : ℕ) = j + 1 then qint q (j + 1) else 0

/-- `K` on `V_{m+1}`: `K v_j = q^{m−2j} v_j`. -/
def irrepKp (m : ℕ) : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜 :=
  Matrix.diagonal fun j => q ^ (m - (j : ℕ)) * q⁻¹ ^ (j : ℕ)

/-- `K⁻¹` on `V_{m+1}`. -/
def irrepKm (m : ℕ) : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜 :=
  Matrix.diagonal fun j => q⁻¹ ^ (m - (j : ℕ)) * q ^ (j : ℕ)


variable {q}

theorem irrepE_mul_irrepF (m : ℕ) :
    irrepE q m * irrepF q m
      = Matrix.diagonal fun j : Fin (m + 1) => qint q (m - (j : ℕ)) * qint q ((j : ℕ) + 1) := by
  ext ⟨i, hi⟩ ⟨j, hj⟩
  simp only [mul_apply, irrepE, irrepF, diagonal_apply, Fin.mk.injEq]
  rw [Fin.sum_univ_eq_sum_range (fun k => (if i + 1 = k then qint q (m - k + 1) else 0) *
    (if k = j + 1 then qint q (j + 1) else 0))]
  simp only [ite_mul, zero_mul, mul_ite, mul_zero]
  rw [Finset.sum_ite_eq']
  simp only [Finset.mem_range]
  by_cases hij : i = j
  · subst hij
    by_cases him : i + 1 < m + 1
    · simp [him, show m - (i + 1) + 1 = m - i by omega]
    · have : m - i = 0 := by omega
      simp [him, this]
  · simp only [hij, if_false]
    split_ifs <;> first | rfl | omega

theorem irrepF_mul_irrepE (m : ℕ) :
    irrepF q m * irrepE q m
      = Matrix.diagonal fun j : Fin (m + 1) => qint q (j : ℕ) * qint q (m - (j : ℕ) + 1) := by
  ext ⟨i, hi⟩ ⟨j, hj⟩
  simp only [mul_apply, irrepE, irrepF, diagonal_apply, Fin.mk.injEq]
  rw [Fin.sum_univ_eq_sum_range (fun k => (if i = k + 1 then qint q (k + 1) else 0) *
    (if k + 1 = j then qint q (m - j + 1) else 0))]
  by_cases hij : i = j
  · subst hij
    rcases Nat.eq_zero_or_pos i with h0 | hpos
    · subst h0
      simp
    · obtain ⟨k, rfl⟩ : ∃ k, i = k + 1 := ⟨i - 1, by omega⟩
      rw [Finset.sum_eq_single k]
      · simp
      · intro b _ hb; rw [if_neg (by omega), zero_mul]
      · intro h; exact absurd (Finset.mem_range.mpr (by omega)) h
  · simp only [hij, if_false]
    apply Finset.sum_eq_zero
    intro k _
    split_ifs <;> first | omega | simp

/-- **The `(m+1)`-dimensional irreducible representation `V_{m+1}` of `U_q(sl₂)`.** -/
def irrep (hq : q ≠ 0) (m : ℕ) : Rep q (Fin (m + 1)) where
  E := irrepE q m
  F := irrepF q m
  Kp := irrepKp q m
  Km := irrepKm q m
  Kp_Km := by
    rw [irrepKp, irrepKm, diagonal_mul_diagonal, ← diagonal_one]
    congr 1; funext j
    simp only [inv_pow]; field_simp
  Km_Kp := by
    rw [irrepKp, irrepKm, diagonal_mul_diagonal, ← diagonal_one]
    congr 1; funext j
    simp only [inv_pow]; field_simp
  KE := by
    ext ⟨i, hi⟩ ⟨j, hj⟩
    simp only [irrepKp, irrepKm, diagonal_mul, mul_diagonal, irrepE, smul_apply, smul_eq_mul]
    by_cases h : i + 1 = j
    · subst h
      simp only [if_true]
      rw [show m - i = (m - (i + 1)) + 1 by omega]
      simp only [inv_pow, pow_succ]
      field_simp
    · simp [h]
  KF := by
    ext ⟨i, hi⟩ ⟨j, hj⟩
    simp only [irrepKp, irrepKm, diagonal_mul, mul_diagonal, irrepF, smul_apply, smul_eq_mul]
    by_cases h : i = j + 1
    · subst h
      simp only [if_true]
      rw [show m - j = (m - (j + 1)) + 1 by omega]
      simp only [inv_pow, pow_succ]
      field_simp
    · simp [h]
  EF := by
    rw [irrepE_mul_irrepF, irrepF_mul_irrepE, diagonal_sub, irrepKp, irrepKm, diagonal_sub,
      ← diagonal_smul]
    congr 1; funext ⟨j, hj⟩
    simp only [Pi.smul_apply, smul_eq_mul]
    rw [show m - j + 1 = (m - j) + 1 from rfl, qint_commutator q hq (m - j) j]

/-- Consistency: `V_2` is the textbook fundamental `fund'` (all four generators agree). -/
theorem irrep_one_eq_fund' (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) :
    (irrep hq 1).E = (fund' q hq hq2).E ∧ (irrep hq 1).F = (fund' q hq hq2).F ∧
      (irrep hq 1).Kp = (fund' q hq hq2).Kp ∧ (irrep hq 1).Km = (fund' q hq hq2).Km := by
  have h1 : qint q 1 = 1 := by unfold qint; simp [div_self hq2]
  refine ⟨?_, ?_, ?_, ?_⟩ <;> ext i j <;> fin_cases i <;> fin_cases j <;>
    simp [irrep, fund', irrepE, irrepF, irrepKp, irrepKm, h1]

end QOU.Mass.QuantumSl2
