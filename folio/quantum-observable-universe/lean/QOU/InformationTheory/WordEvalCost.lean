import QOU.InformationTheory.PhysicalIntractability
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# QOU.Information.WordEvalCost — a fixed-width word costs linear time, not `3^c`

Human statement (`prop:bounded-width-trace-cost`). Let `K` be a commutative semiring and
`M₁, …, M_c` be `d × d` matrices over `K`. The evaluator `traceCost` returns
`tr(M₁ ⋯ M_c)` (`traceCost_fst`) and counts `d · c · d²` scalar multiplications
(`traceCost_snd`): `d` matrix–vector passes, one per basis vector, each of `c` steps
costing `d²`. For fixed `d` this count is linear in `c`, hence not super-polynomial
(`traceCost_not_superPoly`).

Reading for the P-vs-NP section: a braid word on a fixed number of strands acts through a
representation of fixed dimension (the regular representation of `H_n` has dimension
`n!`), so its Markov trace never needs the `3^c` skein resolution leaves. The count is in
ring operations; coefficient growth is not counted here.
-/

namespace QOU.Information.WordEval

open Matrix

variable {K : Type*} [CommSemiring K] {d : ℕ}

/-- Apply a word of matrices to a vector, right to left, returning the result and the
    number of scalar multiplications used (`d²` per matrix–vector product). -/
def evalCost : List (Matrix (Fin d) (Fin d) K) → (Fin d → K) → (Fin d → K) × ℕ
  | [], v => (v, 0)
  | M :: l, v => (M *ᵥ (evalCost l v).1, (evalCost l v).2 + d * d)

theorem evalCost_fst (l : List (Matrix (Fin d) (Fin d) K)) (v : Fin d → K) :
    (evalCost l v).1 = l.prod *ᵥ v := by
  induction l with
  | nil => simp [evalCost]
  | cons M l ih => simp [evalCost, ih, Matrix.mulVec_mulVec]

theorem evalCost_snd (l : List (Matrix (Fin d) (Fin d) K)) (v : Fin d → K) :
    (evalCost l v).2 = l.length * (d * d) := by
  induction l with
  | nil => simp [evalCost]
  | cons M l ih => simp only [evalCost, ih, List.length_cons]; ring

/-- The trace of the product, computed by `d` evaluations on the standard basis, with
    the total multiplication count. -/
def traceCost (l : List (Matrix (Fin d) (Fin d) K)) : K × ℕ :=
  (∑ i, (evalCost l (Pi.single i 1)).1 i, d * (l.length * (d * d)))

/-- **The evaluator returns the trace of the product.** -/
theorem traceCost_fst (l : List (Matrix (Fin d) (Fin d) K)) :
    (traceCost l).1 = Matrix.trace l.prod := by
  simp [traceCost, evalCost_fst, Matrix.trace]

/-- **The count is `d · c · d²`**, linear in the word length `c`. -/
theorem traceCost_snd (l : List (Matrix (Fin d) (Fin d) K)) :
    (traceCost l).2 = d * (l.length * (d * d)) := rfl

/-- **At fixed width the cost is not super-polynomial**: it is bounded by `d³ · c`. -/
theorem traceCost_not_superPoly (d : ℕ) :
    ¬ QOU.Information.SuperPolynomial (fun c => d * (c * (d * d))) := by
  intro h
  obtain ⟨n, _, hn⟩ := h (d * d * d) 1
  have e : d * d * d * n ^ 1 = d * (n * (d * d)) := by ring
  rw [e] at hn
  exact lt_irrefl _ hn

end QOU.Information.WordEval
