import Mathlib.Data.Complex.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic.FinCases

open Matrix

def ctrans (f : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  fun i j => star (f j i)

theorem frobenius_dagger_positive_definite (z : ℂ) :
    let f : Matrix (Fin 2) (Fin 2) ℂ := z • 1
    let f_dag := ctrans f
    f_dag * f = (Complex.normSq z : ℂ) • 1 := by
  intro f f_dag
  ext i j
  dsimp [f, f_dag]
  have h : (starRingEnd ℂ) z * z = (Complex.normSq z : ℂ) := by
    rw [mul_comm, Complex.mul_conj z]
  fin_cases i <;> fin_cases j
  · simp [ctrans, Matrix.mul_apply, Matrix.smul_apply, Matrix.one_apply]
    exact h
  · simp [ctrans, Matrix.mul_apply, Matrix.smul_apply, Matrix.one_apply]
  · simp [ctrans, Matrix.mul_apply, Matrix.smul_apply, Matrix.one_apply]
  · simp [ctrans, Matrix.mul_apply, Matrix.smul_apply, Matrix.one_apply]
    exact h
