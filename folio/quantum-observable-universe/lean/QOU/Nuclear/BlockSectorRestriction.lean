import Mathlib.LinearAlgebra.Matrix.Kronecker
import QOU.Nuclear.BlockChargeSectorTrace
import QOU.Nuclear.PairReadoutTensorReduction

/-!
# The 8 × 8 block operators restrict to the 3 × 3 sector matrices

Audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §34. One nucleon block is three strands,
`V^{⊗3}` with `V = ⟨u, d⟩`, `u = 0`. This file defines the Jimbo braid letters, `e, f, K, K⁻¹` with
the `Ř`-compatible coproduct, and the charge-sector projectors on the 8-dimensional block space, and
proves that on the one-`u` and two-`u` sectors they restrict to the 3 × 3 matrices of
`BlockChargeSectorTrace` (`letter_restrict`, `cas_restrict`). It then checks the sector conditions of
`PairReadoutTensorReduction` and assembles the whole chain: for every three-strand core word `w`,
used in both nucleon blocks, the two-nucleon q-Casimir readout gives pp = nn
(`readout_pp_eq_nn`). No empirical input. Tower status: two blocks, n = 6.
-/

namespace QOU.QBeta.BlockSectorRestriction

open Matrix Kronecker QOU.QBeta.BlockChargeSectorTrace QOU.QBeta.PairReadoutTensorReduction

variable {F : Type*} [Field F]

/-- Basis of one block: three strands, `0 = u`, `1 = d`. -/
abbrev ι := Fin 2 × Fin 2 × Fin 2

/-- Number of `u` strands. -/
def z (a : Fin 2) : ℕ := if a = 0 then 1 else 0

def uc (i : ι) : ℕ := z i.1 + z i.2.1 + z i.2.2

/-- Two-strand index `uu, ud, du, dd ↦ 0, 1, 2, 3`. -/
def pr : Fin 2 → Fin 2 → Fin 4
  | 0, 0 => 0
  | 0, 1 => 1
  | 1, 0 => 2
  | 1, 1 => 3

/-- Jimbo `Ř` and its inverse on two strands. -/
def R4 (q : F) : Matrix (Fin 4) (Fin 4) F := !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]
def R4i (q : F) : Matrix (Fin 4) (Fin 4) F :=
  !![q⁻¹, 0, 0, 0; 0, -(q - q⁻¹), 1, 0; 0, 1, 0, 0; 0, 0, 0, q⁻¹]

def site0 (M : Matrix (Fin 4) (Fin 4) F) : Matrix ι ι F := fun i j =>
  M (pr i.1 i.2.1) (pr j.1 j.2.1) * if i.2.2 = j.2.2 then 1 else 0
def site1 (M : Matrix (Fin 4) (Fin 4) F) : Matrix ι ι F := fun i j =>
  (if i.1 = j.1 then 1 else 0) * M (pr i.2.1 i.2.2) (pr j.2.1 j.2.2)

/-- A braid letter on the 8-dimensional block. -/
def letter8 (q : F) : Letter → Matrix ι ι F
  | (false, false) => site0 (R4 q)
  | (false, true) => site0 (R4i q)
  | (true, false) => site1 (R4 q)
  | (true, true) => site1 (R4i q)

def word8 (q : F) : List Letter → Matrix ι ι F
  | [] => 1
  | l :: w => letter8 q l * word8 q w

/-- Single-strand `K` value: `q` on `u`, `q⁻¹` on `d`. -/
def kv1 (q : F) (a : Fin 2) : F := if a = 0 then q else q⁻¹

def kv (q : F) (i : ι) : F := kv1 q i.1 * kv1 q i.2.1 * kv1 q i.2.2

def K3 (q : F) : Matrix ι ι F := diagonal (kv q)
def K3i (q : F) : Matrix ι ι F := diagonal fun i => (kv q i)⁻¹

/-- `e` raises `d → u`, `f` lowers; `Δe = e⊗K⊗K + 1⊗e⊗K + 1⊗1⊗e`, `Δf = f⊗1⊗1 + K⁻¹⊗f⊗1 + K⁻¹⊗K⁻¹⊗f`. -/
def e1 (a b : Fin 2) : F := if a = 0 ∧ b = 1 then 1 else 0
def f1 (a b : Fin 2) : F := if a = 1 ∧ b = 0 then 1 else 0
def d1 (a b : Fin 2) : F := if a = b then 1 else 0
def k1 (q : F) (a b : Fin 2) : F := if a = b then kv1 q a else 0
def ki1 (q : F) (a b : Fin 2) : F := if a = b then (kv1 q a)⁻¹ else 0

def e3 (q : F) : Matrix ι ι F := fun i j =>
  e1 i.1 j.1 * k1 q i.2.1 j.2.1 * k1 q i.2.2 j.2.2 + d1 i.1 j.1 * e1 i.2.1 j.2.1 * k1 q i.2.2 j.2.2
    + d1 i.1 j.1 * d1 i.2.1 j.2.1 * e1 i.2.2 j.2.2
def f3 (q : F) : Matrix ι ι F := fun i j =>
  f1 i.1 j.1 * d1 i.2.1 j.2.1 * d1 i.2.2 j.2.2 + ki1 q i.1 j.1 * f1 i.2.1 j.2.1 * d1 i.2.2 j.2.2
    + ki1 q i.1 j.1 * ki1 q i.2.1 j.2.1 * f1 i.2.2 j.2.2

/-- Sector embeddings: one `u` (`udd, dud, ddu`) and two `u` (`uud, udu, duu`). -/
def emb : Bool → Fin 3 → ι
  | false => ![(0, 1, 1), (1, 0, 1), (1, 1, 0)]
  | true => ![(0, 0, 1), (0, 1, 0), (1, 0, 0)]

def nOf (flip : Bool) : ℕ := if flip then 2 else 1

/-- Sector projector. -/
def P (flip : Bool) : Matrix ι ι F := diagonal fun i => if uc i = nOf flip then 1 else 0

theorem letter_restrict (q : F) (flip : Bool) (l : Letter) :
    (letter8 q l).submatrix (emb flip) (emb flip) = letterMat q flip l := by
  obtain ⟨g, inv⟩ := l
  cases flip <;> cases g <;> cases inv <;>
  · ext a b; fin_cases a <;> fin_cases b <;>
      simp [letter8, letterMat, emb, site0, site1, R4, R4i, pr, A0, A1, B0, B1]

/-- Charge-preserving: no entries between different `u`-counts. -/
def Pres (M : Matrix ι ι F) : Prop := ∀ i j, uc i ≠ uc j → M i j = 0

theorem R4_pres (q : F) (a b c d : Fin 2) (h : z a + z b ≠ z c + z d) :
    R4 q (pr a b) (pr c d) = 0 ∧ R4i q (pr a b) (pr c d) = 0 := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;> simp_all [z, pr, R4, R4i]

theorem letter_pres (q : F) (l : Letter) : Pres (letter8 q l) := by
  intro ⟨a, b, c⟩ ⟨a', b', c'⟩ h
  simp only [uc] at h
  obtain ⟨g, inv⟩ := l
  cases g <;> cases inv <;> simp only [letter8, site0, site1]
  all_goals
    first
    | (by_cases hc : c = c'
       · subst hc; have := R4_pres q a b a' b' (by omega); simp [this.1, this.2]
       · simp [hc])
    | (by_cases ha : a = a'
       · subst ha; have := R4_pres q b c b' c' (by omega); simp [this.1, this.2]
       · simp [ha])

theorem pres_one : Pres (1 : Matrix ι ι F) := by
  intro i j h; rw [Matrix.one_apply_ne]; rintro rfl; exact h rfl

theorem pres_mul {M N : Matrix ι ι F} (hM : Pres M) (hN : Pres N) : Pres (M * N) := by
  intro i j h
  rw [Matrix.mul_apply]
  refine Finset.sum_eq_zero fun k _ => ?_
  by_cases hk : uc i = uc k
  · rw [hN k j (by omega), mul_zero]
  · rw [hM i k hk, zero_mul]

theorem word_pres (q : F) (w : List Letter) : Pres (word8 q w) := by
  induction w with
  | nil => exact pres_one
  | cons l w ih => exact pres_mul (letter_pres q l) ih

theorem emb_inj (flip : Bool) : Function.Injective (emb flip) := by
  cases flip <;> decide

theorem uc_emb (flip : Bool) (a : Fin 3) : uc (emb flip a) = nOf flip := by
  cases flip <;> fin_cases a <;> rfl

theorem filter_eq_map (flip : Bool) :
    (Finset.univ.filter fun k : ι => uc k = nOf flip) = Finset.univ.map ⟨emb flip, emb_inj flip⟩ := by
  cases flip <;> decide

/-- Sum over the sector, written through the embedding. -/
theorem sum_sector (flip : Bool) (g : ι → F) (hg : ∀ k, uc k ≠ nOf flip → g k = 0) :
    ∑ k, g k = ∑ a, g (emb flip a) := by
  rw [← Finset.sum_filter_of_ne (p := fun k => uc k = nOf flip) (fun k _ hk => by
    by_contra h; exact hk (hg k h)), filter_eq_map, Finset.sum_map]
  rfl

theorem sub_mul {M N : Matrix ι ι F} (flip : Bool) (hM : Pres M) :
    (M * N).submatrix (emb flip) (emb flip)
      = M.submatrix (emb flip) (emb flip) * N.submatrix (emb flip) (emb flip) := by
  ext a b
  simp only [Matrix.submatrix_apply, Matrix.mul_apply]
  exact sum_sector flip _ fun k hk => by
    rw [hM _ k (by rw [uc_emb]; exact fun h => hk h.symm), zero_mul]

theorem word_restrict (q : F) (flip : Bool) (w : List Letter) :
    (word8 q w).submatrix (emb flip) (emb flip) = wordMat q flip w := by
  induction w with
  | nil =>
    ext a b; simp only [word8, wordMat, Matrix.submatrix_apply, Matrix.one_apply,
      (emb_inj flip).eq_iff]
  | cons l w ih => rw [word8, sub_mul flip (letter_pres q l), letter_restrict, ih, wordMat]

/-- `K` on the sector: `q⁻¹` with one `u`, `q` with two. -/
def kOf (q : F) (flip : Bool) : F := if flip then q else q⁻¹

/-- `h²·fe` restricted to either sector is `G − (q k + (q k)⁻¹)`. -/
theorem cas_restrict (q : F) (hq : q ≠ 0) (flip : Bool) :
    ((q - q⁻¹) ^ 2 • (f3 q * e3 q)).submatrix (emb flip) (emb flip)
      = G q - (q * kOf q flip + (q * kOf q flip)⁻¹) • (1 : Matrix (Fin 3) (Fin 3) F) := by
  cases flip <;>
  · ext a b; fin_cases a <;> fin_cases b <;>
      simp [emb, kOf, G, f3, e3, e1, f1, d1, k1, ki1, kv1, Matrix.mul_apply, Fintype.sum_prod_type,
        Fin.sum_univ_two] <;>
      (try field_simp) <;> (try ring_nf)

theorem e3_zero (q : F) (i j : ι) (h : uc i = uc j) : e3 q i j = 0 := by
  obtain ⟨a, b, c⟩ := i; obtain ⟨a', b', c'⟩ := j
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp_all [uc, z, e3, e1, d1, k1]

theorem f3_zero (q : F) (i j : ι) (h : uc i = uc j) : f3 q i j = 0 := by
  obtain ⟨a, b, c⟩ := i; obtain ⟨a', b', c'⟩ := j
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;> fin_cases c' <;>
    simp_all [uc, z, f3, f1, d1, ki1]

theorem kv_sector (q : F) (hq : q ≠ 0) (flip : Bool) (i : ι) (hi : uc i = nOf flip) :
    kv q i = kOf q flip := by
  obtain ⟨a, b, c⟩ := i
  cases flip <;> fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp_all [uc, z, nOf, kv, kv1, kOf]

theorem shift_zero {Y : Matrix ι ι F} (flip : Bool) (hY : ∀ i j, uc i = uc j → Y i j = 0) :
    P flip * Y * P flip = 0 := by
  ext i j
  simp only [P, Matrix.diagonal_mul, Matrix.mul_diagonal, Matrix.zero_apply]
  by_cases hi : uc i = nOf flip
  · by_cases hj : uc j = nOf flip
    · rw [hY i j (by rw [hi, hj]), mul_zero, zero_mul]
    · simp [hj]
  · simp [hi]

theorem P_comm_pres {M : Matrix ι ι F} (flip : Bool) (hM : Pres M) :
    P flip * M = M * P flip := by
  ext i j
  simp only [P, Matrix.diagonal_mul, Matrix.mul_diagonal]
  by_cases h : uc i = uc j
  · rw [h]; ring
  · rw [hM i j h, mul_zero, zero_mul]

theorem P_comm_diag (flip : Bool) (d : ι → F) : P flip * diagonal d = diagonal d * P flip := by
  simp only [P, Matrix.diagonal_mul_diagonal, mul_comm]

theorem sector (q : F) (hq : q ≠ 0) (flip : Bool) (w : List Letter) :
    Sector (e3 q) (f3 q) (K3 q) (K3i q) (word8 q w) (P flip) (kOf q flip) where
  idem := by
    simp only [P, Matrix.diagonal_mul_diagonal]; congr 1; ext i; split_ifs <;> simp
  commK := P_comm_diag flip _
  commKi := P_comm_diag flip _
  commW := P_comm_pres flip (word_pres q w)
  eigK := by
    ext i j
    simp only [K3, P, Matrix.diagonal_mul_diagonal, Matrix.smul_apply, Matrix.diagonal_apply]
    split_ifs with h1 h2 <;> simp_all [kv_sector q hq flip]
  eigKi := by
    ext i j
    simp only [K3i, P, Matrix.diagonal_mul_diagonal, Matrix.smul_apply, Matrix.diagonal_apply]
    split_ifs with h1 h2 <;> simp_all [kv_sector q hq flip]
  shiftE := shift_zero flip (e3_zero q)
  shiftF := shift_zero flip (f3_zero q)

theorem trace_P (flip : Bool) (M : Matrix ι ι F) :
    (P flip * M).trace = (M.submatrix (emb flip) (emb flip)).trace := by
  simp only [Matrix.trace, Matrix.diag, P, Matrix.diagonal_mul, Matrix.submatrix_apply]
  rw [sum_sector flip _ fun k hk => by simp [hk]]
  simp [uc_emb]

theorem PK (q : F) (hq : q ≠ 0) (flip : Bool) (w : List Letter) :
    P flip * K3 q = kOf q flip • P flip := by
  rw [(sector q hq flip w).commK, (sector q hq flip w).eigK]

theorem a_eq (q : F) (hq : q ≠ 0) (flip : Bool) (w : List Letter) :
    (P flip * K3 q * word8 q w).trace = kOf q flip * (wordMat q false w).trace := by
  rw [PK q hq flip w, Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul, trace_P, word_restrict]
  cases flip
  · rfl
  · rw [sectorTrace_eq q hq]

theorem c_eq (q : F) (hq : q ≠ 0) (flip : Bool) (w : List Letter) :
    (q - q⁻¹) ^ 2 * (P flip * K3 q * word8 q w * (f3 q * e3 q)).trace
      = QCasimirPairGenericQ.blockC q (wordMat q false w).trace
          ((wordMat q false w * G q).trace) (kOf q flip) := by
  rw [PK q hq flip w, Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul,
    Matrix.mul_assoc, trace_P, sub_mul flip (word_pres q w), word_restrict]
  have hs : (q - q⁻¹) ^ 2 * (wordMat q flip w * (f3 q * e3 q).submatrix (emb flip) (emb flip)).trace
      = (wordMat q flip w * ((q - q⁻¹) ^ 2 • (f3 q * e3 q)).submatrix (emb flip) (emb flip)).trace := by
    have hsub : ((q - q⁻¹) ^ 2 • (f3 q * e3 q)).submatrix (emb flip) (emb flip)
        = (q - q⁻¹) ^ 2 • (f3 q * e3 q).submatrix (emb flip) (emb flip) := by
      ext a b; simp
    rw [hsub, Matrix.mul_smul, Matrix.trace_smul, smul_eq_mul]
  rw [mul_left_comm, hs, cas_restrict q hq, feTrace_eq q hq w flip]
  rfl

/-- **pp = nn end to end.** For every three-strand core word `w` in both nucleon blocks, the
two-nucleon q-Casimir readout, divided by the identity readout, is the same in the two-proton and
two-neutron sectors (stated cross-multiplied). -/
theorem readout_pp_eq_nn (q : F) (hq : q ≠ 0) (w : List Letter) :
    (((P true * K3 q * word8 q w) ⊗ₖ (P true * K3 q * word8 q w))
        * pairX q (q - q⁻¹) (e3 q) (f3 q) (K3 q) (K3i q) (e3 q) (f3 q) (K3 q) (K3i q)).trace
      * ((P false * K3 q * word8 q w) ⊗ₖ (P false * K3 q * word8 q w)).trace
    = (((P false * K3 q * word8 q w) ⊗ₖ (P false * K3 q * word8 q w))
        * pairX q (q - q⁻¹) (e3 q) (f3 q) (K3 q) (K3i q) (e3 q) (f3 q) (K3 q) (K3i q)).trace
      * ((P true * K3 q * word8 q w) ⊗ₖ (P true * K3 q * word8 q w)).trace := by
  rw [readout_eq_pairReadout q (q - q⁻¹) _ _ (sector q hq true w) (sector q hq true w),
    readout_eq_pairReadout q (q - q⁻¹) _ _ (sector q hq false w) (sector q hq false w),
    Matrix.trace_kronecker, Matrix.trace_kronecker, a_eq q hq, a_eq q hq, c_eq q hq, c_eq q hq]
  have := QCasimirPairGenericQ.pairReadout_pp_eq_nn_of_blockData q (wordMat q false w).trace
    ((wordMat q false w * G q).trace) hq
  simpa [QCasimirPairGenericQ.sectorReadout, QCasimirPairGenericQ.sectorNorm,
    QCasimirPairGenericQ.blockA, kOf] using this

end QOU.QBeta.BlockSectorRestriction
