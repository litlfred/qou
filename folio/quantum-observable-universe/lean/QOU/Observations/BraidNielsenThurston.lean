/-
# Nielsen–Thurston type of three-braids via `B₃ → SL(2,ℤ)`: the pseudo-Anosov selector

Thread "Derive the electron's categorical weight" (2026-11-27). Owner: "Derive what you can",
"Work anosov". This file works the pseudo-Anosov selector with one carrier shared by all
generations, leaving the ruling `e = Δ`, `μ = Δ³`, `τ = Δ⁵` unchanged. Audit:
`docs/audits/2026-11-27-electron-categorical-weight.md` §15.

`σ₁ ↦ A = [[1,1],[0,1]]`, `σ₂ ↦ B = [[1,0],[−1,1]]` defines `B₃ → SL(2,ℤ)` (`braid_rel`), and it
induces `B₃/Z(B₃) ≅ PSL(2,ℤ)`. By Nielsen–Thurston (cited), a 3-braid is periodic, reducible or
pseudo-Anosov according as `|tr| < 2`, `= 2` or `> 2`. Its dilatation `λ` solves
`λ + λ⁻¹ = |tr|`.

* `img_delta`: `Δ ↦ [[0,1],[−1,0]]`, trace `0`. `img_delta_sq`: `Δ² ↦ −I`, central.
* `trace_mul_delta_sq`: `tr(M·(−I)^k) = ±tr M`. So `|tr|`, and with it the Nielsen–Thurston type
  and the dilatation, does not depend on the number of full twists. In particular
  `trace_lepton_ladder`: every ruled lepton word `Δ^{2k+1}` has trace `0`, so all three are periodic.
* `img_carrier`: `σ₁σ₂⁻¹ ↦ [[2,1],[1,1]]`, trace `3`.
  `least_pA_trace`: an integer trace with `|t| > 2` has `|t| ≥ 3`, so `σ₁σ₂⁻¹` is a least-trace
  pseudo-Anosov. `golden_dilatation`: `φ² + φ⁻² = 3` for `φ² = (3+√5)/2` (in any field with a root
  of `x² − 5`).

**Consequence.** With one carrier shared by all generations, and generations that differ only by
`Δ²`, the carrier's type, dilatation and trace are the same for `e`, `μ` and `τ`. The selector
therefore explains which carrier is used (the least pseudo-Anosov, `σ₁σ₂⁻¹`, square closing to
`4₁`), but it cannot tell the generations apart. Any generation dependence must come from a
non-central change. No measured value enters.
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

namespace QOU.Observations.BraidNielsenThurston

open Matrix

abbrev M2 := Matrix (Fin 2) (Fin 2) ℤ

def A : M2 := !![1, 1; 0, 1]
def B : M2 := !![1, 0; -1, 1]
def Ainv : M2 := !![1, -1; 0, 1]
def Binv : M2 := !![1, 0; 1, 1]

theorem A_mul_Ainv : A * Ainv = 1 := by
  simp [A, Ainv, Matrix.mul_fin_two, Matrix.one_fin_two]

theorem B_mul_Binv : B * Binv = 1 := by
  simp [B, Binv, Matrix.mul_fin_two, Matrix.one_fin_two]

/-- **Braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂`. -/
theorem braid_rel : A * B * A = B * A * B := by
  simp [A, B, Matrix.mul_fin_two]

/-- `Δ = σ₁σ₂σ₁ ↦ [[0,1],[−1,0]]`. -/
theorem img_delta : A * B * A = !![0, 1; -1, 0] := by
  simp [A, B, Matrix.mul_fin_two]

/-- `Δ² ↦ −I`. -/
theorem img_delta_sq : (A * B * A) * (A * B * A) = -1 := by
  rw [img_delta]; simp [Matrix.mul_fin_two, Matrix.one_fin_two]

/-- **Full twists only change the sign of the trace.** -/
theorem trace_mul_delta_sq (M : M2) (k : ℕ) :
    (M * ((A * B * A) * (A * B * A)) ^ k).trace = (-1) ^ k * M.trace := by
  rw [img_delta_sq, neg_one_pow_eq_pow_mod_two]
  rcases Nat.mod_two_eq_zero_or_one k with h | h <;> simp [h, neg_one_pow_eq_pow_mod_two,
    Matrix.trace_neg]

/-- **Every ruled lepton word `Δ^{2k+1}` has trace `0`**: all are periodic. -/
theorem trace_lepton_ladder (k : ℕ) :
    ((A * B * A) * ((A * B * A) * (A * B * A)) ^ k).trace = 0 := by
  rw [trace_mul_delta_sq, img_delta]
  simp [Matrix.trace_fin_two]

/-- The carrier `σ₁σ₂⁻¹ ↦ [[2,1],[1,1]]`, trace `3`. -/
theorem img_carrier : A * Binv = !![2, 1; 1, 1] := by
  simp [A, Binv, Matrix.mul_fin_two]

theorem trace_carrier : (A * Binv).trace = 3 := by
  rw [img_carrier]; simp [Matrix.trace_fin_two]

/-- **Least pseudo-Anosov trace**: an integer `t` with `|t| > 2` has `|t| ≥ 3`. -/
theorem least_pA_trace (t : ℤ) (ht : 2 < |t|) : 3 ≤ |t| := by omega

/-- **Golden dilatation**: if `s² = 5` and `λ = (3 + s)/2`, then `λ + λ⁻¹ = 3`. -/
theorem golden_dilatation {K : Type*} [Field K] [CharZero K] (s : K) (hs : s ^ 2 = 5) :
    (3 + s) / 2 + ((3 + s) / 2)⁻¹ = 3 := by
  have h : (3 + s) ≠ 0 := by
    intro h0
    have : s = -3 := by linear_combination h0
    rw [this] at hs; norm_num at hs
  field_simp
  linear_combination hs

end QOU.Observations.BraidNielsenThurston
