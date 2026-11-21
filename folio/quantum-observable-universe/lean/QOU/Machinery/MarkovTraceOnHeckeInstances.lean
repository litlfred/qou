import QOU.Machinery.MarkovTraceOnHecke
import Mathlib.Tactic.NormNum
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FinCases

/-!
# `JonesWenzlProjector` after the 2026-11-21 restatement: the two-strand case

The class now carries the generators `σ` and enforces `p ≠ 0` and the
strand-killing relations `p (q•1 − σ_i) = 0 = (q•1 − σ_i) p` for `i < n − 1`.
Before the restatement its only field was `p * p = p`, so `0` and `1`
inhabited it at every rank.

**What is proved (sorry-free).** In `M₂(ℚ)` with the genuine Hecke generator
`σ = diag(2, −1/2)` at `q = 2`:
* `not_jonesWenzlProjector_one` — `1` is no longer a Jones–Wenzl projector at
  `n = 2`. It was one under the old class.
* `jonesWenzlProjector_two` — `p₂ = diag(1, 0) = 1 − e₁` is one. This is the
  genuine two-strand projector `p₂ = 1 − e₁`, with
  `e₁ = jonesIdempotent 2 σ = diag(0, 1)`.
* `jonesWenzlProjector_one_strand` — `1` is the projector for `n ≤ 1`, where
  there are no strands to kill (`p₁ = 1`). This is correct, not a defect.

**What is not proved.** Existence and uniqueness of `p_n` in `H_n(q)` for
general `n` (Wenzl's recursion; needs `[n]_q! ≠ 0`).

-- Ref: [leitner2026] QOU.Machinery.MarkovTraceOnHecke; [wenzl1987]
-- H. Wenzl, On sequences of projections, C. R. Math. Rep. Acad. Sci. Canada 9
-- (1987) 5–9 (the recursive projector and its uniqueness).
-/

namespace QOU.Machinery.Instances

open QOU.Machinery Matrix

/-- The Hecke generator `diag(2, −1/2)` at `q = 2`. -/
def σJW : Matrix (Fin 2) (Fin 2) ℚ := Matrix.of ![![2, 0], ![0, -(2 : ℚ)⁻¹]]

/-- The two-strand projector `diag(1, 0)`. -/
def pJW : Matrix (Fin 2) (Fin 2) ℚ := Matrix.of ![![1, 0], ![0, 0]]

/-- `1` is not a Jones–Wenzl projector on two strands. -/
theorem not_jonesWenzlProjector_one :
    ¬ JonesWenzlProjector ℚ (Matrix (Fin 2) (Fin 2) ℚ) 2 (fun _ => σJW) 2 1 := by
  intro h
  have h1 := congrFun (congrFun (h.kill_right 0 (by norm_num)) 1) 1
  simp [σJW] at h1
  norm_num at h1

/-- `diag(1, 0) = 1 − e₁` is the Jones–Wenzl projector on two strands. -/
theorem jonesWenzlProjector_two :
    JonesWenzlProjector ℚ (Matrix (Fin 2) (Fin 2) ℚ) 2 (fun _ => σJW) 2 pJW where
  idempotent := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [pJW, Matrix.mul_apply, Fin.sum_univ_two]
  ne_zero := by
    intro h
    have := congrFun (congrFun h 0) 0
    simp [pJW] at this
  kill_right _ _ := by
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [pJW, σJW, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;> norm_num
  kill_left _ _ := by
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [pJW, σJW, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;> norm_num

/-- With at most one strand there is nothing to kill, and `1` is the projector. -/
theorem jonesWenzlProjector_one_strand {R H : Type*} [CommRing R] [Ring H]
    [Algebra R H] [Nontrivial H] (q : R) (σ : ℕ → H) {n : ℕ} (hn : n ≤ 1) :
    JonesWenzlProjector R H q σ n 1 where
  idempotent := one_mul 1
  ne_zero := one_ne_zero
  kill_right i hi := absurd hi (by omega)
  kill_left i hi := absurd hi (by omega)

end QOU.Machinery.Instances
