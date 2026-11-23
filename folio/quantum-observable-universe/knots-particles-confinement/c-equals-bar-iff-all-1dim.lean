/-
  Charge conjugation equals the bar involution on characters of H_n(q).

  General statement (narrative proof, Tits deformation): for every n,
  λ ⊢ n and braid word β, χ^λ(C β)(q) = χ^λ(β)(q⁻¹), where
  C : σᵢ ↦ σᵢ⁻¹ and σᵢ² = (q - q⁻¹)σᵢ + 1.

  This file proves the case n = 3, λ = (2,1) for every braid word, over
  any field, by an explicit intertwiner P = diag(1, q²) with
  P σᵢ⁻¹(q) = σᵢ(q⁻¹) P. It replaces an earlier file that encoded the
  false claim "C = bar only when every irrep is one-dimensional".

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

open Matrix

namespace QOU.ParticleInteractions.CBar

variable {K : Type*} [Field K]

/-- The two Hecke generators on the (2,1) representation of `H₃(q)`
(`q` times the reduced Burau matrices at `t = q⁻²`), normalised so that
`σ² = (q - q⁻¹)σ + 1`. -/
def gen (q : K) : Fin 2 → Matrix (Fin 2) (Fin 2) K
  | 0 => !![-q⁻¹, q; 0, q]
  | 1 => !![q, 0; q⁻¹, -q⁻¹]

/-- The inverse generator, `σ⁻¹ = σ - (q - q⁻¹)`. -/
def genInv (q : K) (i : Fin 2) : Matrix (Fin 2) (Fin 2) K :=
  gen q i - (q - q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) K)

/-- The intertwiner `P = diag(1, q²)`. -/
def P (q : K) : Matrix (Fin 2) (Fin 2) K := !![1, 0; 0, q ^ 2]

theorem gen_mul_genInv (q : K) (hq : q ≠ 0) (i : Fin 2) :
    gen q i * genInv q i = 1 := by
  fin_cases i <;>
  · ext a b; fin_cases a <;> fin_cases b <;>
      simp [gen, genInv, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- Intertwining for an inverse generator: `P σᵢ⁻¹(q) = σᵢ(q⁻¹) P`. -/
theorem P_genInv (q : K) (hq : q ≠ 0) (i : Fin 2) :
    P q * genInv q i = gen q⁻¹ i * P q := by
  fin_cases i <;>
  · ext a b; fin_cases a <;> fin_cases b <;>
      simp [gen, genInv, P, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- Intertwining for a generator: `P σᵢ(q) = σᵢ⁻¹(q⁻¹) P`. -/
theorem P_gen (q : K) (hq : q ≠ 0) (i : Fin 2) :
    P q * gen q i = genInv q⁻¹ i * P q := by
  fin_cases i <;>
  · ext a b; fin_cases a <;> fin_cases b <;>
      simp [gen, genInv, P, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- A braid word: a list of letters `(i, positive?)`. -/
abbrev Word := List (Fin 2 × Bool)

/-- The matrix of a braid word on the (2,1) representation. -/
def eval (q : K) : Word → Matrix (Fin 2) (Fin 2) K
  | [] => 1
  | (i, true) :: w => gen q i * eval q w
  | (i, false) :: w => genInv q i * eval q w

/-- Charge conjugation `C : σᵢ ↦ σᵢ⁻¹` on words. -/
def conj (w : Word) : Word := w.map fun x => (x.1, !x.2)

theorem P_eval_conj (q : K) (hq : q ≠ 0) (w : Word) :
    P q * eval q (conj w) = eval q⁻¹ w * P q := by
  induction w with
  | nil => simp [conj, eval]
  | cons x w ih =>
    obtain ⟨i, b⟩ := x
    cases b
    · simp only [conj, List.map_cons, Bool.not_false, eval] at ih ⊢
      rw [← mul_assoc, P_gen q hq, mul_assoc, ih, ← mul_assoc]
    · simp only [conj, List.map_cons, Bool.not_true, eval] at ih ⊢
      rw [← mul_assoc, P_genInv q hq, mul_assoc, ih, ← mul_assoc]

theorem P_mul_Pinv (q : K) (hq : q ≠ 0) :
    P q * !![1, 0; 0, (q ^ 2)⁻¹] = 1 := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [P] ; field_simp

/-- **C = bar on the (2,1) character of `H₃(q)`.** For every braid word `β`,
`χ^{(2,1)}(C β)(q) = χ^{(2,1)}(β)(q⁻¹)`. -/
theorem trace_conj_eq_trace_bar (q : K) (hq : q ≠ 0) (w : Word) :
    (eval q (conj w)).trace = (eval q⁻¹ w).trace := by
  set Q : Matrix (Fin 2) (Fin 2) K := !![1, 0; 0, (q ^ 2)⁻¹]
  have hPQ : P q * Q = 1 := P_mul_Pinv q hq
  have hQP : Q * P q = 1 := by
    ext a b; fin_cases a <;> fin_cases b <;> simp [P, Q]; field_simp
  have h := P_eval_conj q hq w
  have : eval q (conj w) = Q * (eval q⁻¹ w * P q) := by
    rw [← h, ← mul_assoc, hQP, one_mul]
  rw [this, Matrix.trace_mul_comm, mul_assoc, hPQ, mul_one]

end QOU.ParticleInteractions.CBar
