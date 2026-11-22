import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Every three-strand core has the same trace on the charge-1 and charge-2 sectors

Audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §32. This discharges the first block-data
hypothesis of `QCasimirPairGenericQ` (`a(n) = k(n)·τ` with one `τ` for both nucleon sectors).

On three strands `V^{⊗3}`, `V = ⟨u, d⟩`, the Jimbo braiding preserves the number of `u` strands.
Restricted to the 3-dimensional sectors with one `u` (basis `udd, dud, ddu`, the neutron block) and
two `u` (basis `uud, udu, duu`, the proton block), the generators are the 3 × 3 matrices
`A0 = [[0,1,0],[1,h,0],[0,0,q]]`, `A1 = [[q,0,0],[0,0,1],[0,1,h]]`, `h = q − q⁻¹`:
`σ₀ ↦ A0, σ₁ ↦ A1` on the one-`u` sector, `σ₀ ↦ A1, σ₁ ↦ A0` on the two-`u` sector
(read off the 8 × 8 Jimbo matrices; `np_gaudin_generic_q_probe.py` setup). So the two sectors are
the same `H₃(q)` module twisted by the index flip `σ₀ ↔ σ₁`, which is conjugation by the
half twist `Δ = σ₀σ₁σ₀`. Hence `ρ₂(w)·Δ = Δ·ρ₁(w)` for every braid word (`intertwine`), and the
two sector traces agree for every word (`sectorTrace_eq`), over any field and generic `q`.

The second hypothesis `hc` (the Casimir insertion) is discharged below by the same intertwiner.
What stays outside Lean: the reading of the 3 × 3 sector matrices off the 8 × 8 Jimbo and Casimir
operators (exact sympy, `block_sector_matrices_probe.py`), and the reduction of the two-block
64 × 64 readout to block traces (§28). No empirical input.
-/

namespace QOU.QBeta.BlockChargeSectorTrace

open Matrix

variable {K : Type*} [Field K]

/-- `σ₀` on the one-`u` sector. -/
def A0 (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, 0; 1, q - q⁻¹, 0; 0, 0, q]
/-- `σ₁` on the one-`u` sector. -/
def A1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, 0, 1; 0, 1, q - q⁻¹]
/-- `σ₀⁻¹ = σ₀ − h` on the one-`u` sector. -/
def B0 (q : K) : Matrix (Fin 3) (Fin 3) K := !![-(q - q⁻¹), 1, 0; 1, 0, 0; 0, 0, q⁻¹]
/-- `σ₁⁻¹` on the one-`u` sector. -/
def B1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q⁻¹, 0, 0; 0, -(q - q⁻¹), 1; 0, 1, 0]

theorem A0_B0 (q : K) (hq : q ≠ 0) : A0 q * B0 q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A0, B0, Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp
theorem A1_B1 (q : K) (hq : q ≠ 0) : A1 q * B1 q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A1, B1, Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp

/-- A braid letter: generator index and whether it is inverted. -/
abbrev Letter := Bool × Bool

/-- Matrix of a letter on the one-`u` sector (`flip = false`) or the two-`u` sector (`flip = true`). -/
def letterMat (q : K) (flip : Bool) : Letter → Matrix (Fin 3) (Fin 3) K
  | (g, inv) =>
    match xor g flip, inv with
    | false, false => A0 q
    | false, true => B0 q
    | true, false => A1 q
    | true, true => B1 q

/-- Matrix of a word. -/
def wordMat (q : K) (flip : Bool) : List Letter → Matrix (Fin 3) (Fin 3) K
  | [] => 1
  | l :: w => letterMat q flip l * wordMat q flip w

/-- The half twist `Δ = σ₀σ₁σ₀` on the one-`u` sector. -/
def Δ (q : K) : Matrix (Fin 3) (Fin 3) K := A0 q * A1 q * A0 q

theorem letter_intertwine (q : K) (hq : q ≠ 0) (l : Letter) :
    letterMat q true l * Δ q = Δ q * letterMat q false l := by
  obtain ⟨g, inv⟩ := l
  cases g <;> cases inv <;>
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [letterMat, Δ, A0, A1, B0, B1, Matrix.mul_apply, Fin.sum_univ_three] <;>
      (try field_simp) <;> (try ring_nf) <;> (try simp)

/-- `ρ₂(w)·Δ = Δ·ρ₁(w)` for every braid word. -/
theorem intertwine (q : K) (hq : q ≠ 0) (w : List Letter) :
    wordMat q true w * Δ q = Δ q * wordMat q false w := by
  induction w with
  | nil => simp [wordMat]
  | cons l w ih =>
    simp only [wordMat]
    rw [Matrix.mul_assoc, ih, ← Matrix.mul_assoc, letter_intertwine q hq, Matrix.mul_assoc]

theorem det_Δ (q : K) (hq : q ≠ 0) : (Δ q).det = -q ^ 3 := by
  simp [Δ, A0, A1, Matrix.det_fin_three]
  field_simp

/-- The proton-sector and neutron-sector traces of any three-strand core agree. -/
theorem sectorTrace_eq (q : K) (hq : q ≠ 0) (w : List Letter) :
    (wordMat q true w).trace = (wordMat q false w).trace := by
  have hu : IsUnit (Δ q).det := by rw [det_Δ q hq]; exact isUnit_iff_ne_zero.mpr (by simp [hq])
  have h := intertwine q hq w
  have : wordMat q true w = Δ q * wordMat q false w * (Δ q)⁻¹ := by
    rw [← h, Matrix.mul_assoc, Matrix.mul_nonsing_inv _ hu, Matrix.mul_one]
  rw [this, Matrix.trace_mul_cycle, Matrix.nonsing_inv_mul _ hu, Matrix.one_mul]

/-! ## The Casimir insertion: the second block-data hypothesis

`h²C = h²·fe + qK + q⁻¹K⁻¹` (coproduct `Δe = e⊗K + 1⊗e`) restricted to either charge sector is the
same 3 × 3 matrix `G` in the bases above (`block_sector_matrices_probe.py`), and `K^{⊗3}` is the
scalar `k(1) = q⁻¹`, `k(2) = q`. `G` commutes with `A0`, `A1`, hence with `Δ`, so the trace of any
core times `G` is also the same on both sectors (`casimirTrace_eq`). With `fe` inserted,
`h²·fe = G − (q k + (q k)⁻¹)` on sector `k`, which is hypothesis `hc` of `QCasimirPairGenericQ` with
`μ = tr(ρ(w)·G)` (`feTrace_eq`). -/

/-- `h²C` on either charge sector. -/
def G (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![(q ^ 6 + q ^ 4 - q ^ 2 + 1) * q⁻¹ ^ 4, (q ^ 2 - 1) ^ 2 * q⁻¹ ^ 3, (q ^ 2 - 1) ^ 2 * q⁻¹ ^ 2;
     (q ^ 2 - 1) ^ 2 * q⁻¹ ^ 3, 2 * (q ^ 4 - q ^ 2 + 1) * q⁻¹ ^ 2, (q ^ 2 - 1) ^ 2 * q⁻¹;
     (q ^ 2 - 1) ^ 2 * q⁻¹ ^ 2, (q ^ 2 - 1) ^ 2 * q⁻¹, (q ^ 6 - q ^ 4 + q ^ 2 + 1) * q⁻¹ ^ 2]

theorem G_comm_A0 (q : K) (hq : q ≠ 0) : A0 q * G q = G q * A0 q := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A0, G, Matrix.mul_apply, Fin.sum_univ_three] <;>
    (try field_simp) <;> (try ring_nf)

theorem G_comm_A1 (q : K) (hq : q ≠ 0) : A1 q * G q = G q * A1 q := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A1, G, Matrix.mul_apply, Fin.sum_univ_three] <;>
    (try field_simp) <;> (try ring_nf)

theorem G_comm_Δ (q : K) (hq : q ≠ 0) : Δ q * G q = G q * Δ q := by
  simp only [Δ, Matrix.mul_assoc]
  rw [G_comm_A0 q hq, ← Matrix.mul_assoc (A1 q), G_comm_A1 q hq, Matrix.mul_assoc,
    ← Matrix.mul_assoc (A0 q), ← Matrix.mul_assoc (A0 q), G_comm_A0 q hq, Matrix.mul_assoc,
    Matrix.mul_assoc]

/-- The core-times-Casimir trace agrees on both charge sectors. -/
theorem casimirTrace_eq (q : K) (hq : q ≠ 0) (w : List Letter) :
    (wordMat q true w * G q).trace = (wordMat q false w * G q).trace := by
  have hu : IsUnit (Δ q).det := by rw [det_Δ q hq]; exact isUnit_iff_ne_zero.mpr (by simp [hq])
  have h := intertwine q hq w
  have hw : wordMat q true w = Δ q * wordMat q false w * (Δ q)⁻¹ := by
    rw [← h, Matrix.mul_assoc, Matrix.mul_nonsing_inv _ hu, Matrix.mul_one]
  have hG : (Δ q)⁻¹ * G q * Δ q = G q := by
    rw [Matrix.mul_assoc, ← G_comm_Δ q hq, ← Matrix.mul_assoc, Matrix.nonsing_inv_mul _ hu,
      Matrix.one_mul]
  rw [hw, Matrix.mul_assoc, Matrix.mul_assoc, Matrix.trace_mul_comm, Matrix.mul_assoc,
    Matrix.mul_assoc, ← Matrix.mul_assoc (Δ q)⁻¹, hG]

/-- Hypothesis `hc`: with `fe` inserted and the K-weight `k`, the sector trace is
`k·(μ − (q k + (q k)⁻¹)·τ)` with `τ = tr ρ₁(w)` and `μ = tr(ρ₁(w)·G)`, the same `τ, μ` on both
nucleon sectors (`flip = false`: `k = q⁻¹`; `flip = true`: `k = q`). -/
theorem feTrace_eq (q : K) (hq : q ≠ 0) (w : List Letter) (flip : Bool) (k : K) :
    k * (wordMat q flip w * (G q - (q * k + (q * k)⁻¹) • (1 : Matrix (Fin 3) (Fin 3) K))).trace
      = k * ((wordMat q false w * G q).trace
          - (q * k + (q * k)⁻¹) * (wordMat q false w).trace) := by
  rw [Matrix.mul_sub, Matrix.trace_sub, Matrix.mul_smul, Matrix.trace_smul, Matrix.mul_one,
    smul_eq_mul]
  cases flip
  · rfl
  · rw [casimirTrace_eq q hq, sectorTrace_eq q hq]

end QOU.QBeta.BlockChargeSectorTrace
