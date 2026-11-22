/-
  The single-wrap element `Δ_S` is invisible to the two-row block of `H₃(q)`:
  its `(2,1)` character vanishes, `χ_(2,1)(Δ_S) = 0`, identically in `q`.

  CONTEXT (bean `qou-cds1`, entry 2026-10-10 (2); owner question "what
  element or functional supplies a factor above 1 on the ruled base").
  `Δ_S = (h²/2)·1 − (h/2)(σ₁ + σ₂)` with `h = q − q⁻¹` is the owner-ruled
  single-wrap element. Under convention D the three-row weight vanishes, so a
  trace sees `Δ_S` through the `(3)` and `(2,1)` blocks only. This file proves
  that the `(2,1)` block contributes NOTHING, so every convention-D functional
  on `Δ_S` is a multiple of `χ_(3)(Δ_S)`, and the only freedom left is the
  weight on the trivial block. That is the exact half of the 2026-10-10
  "no admissible functional supplies the factor" result.

  WHAT IS PROVED, over an arbitrary field `K` (no ordering, no `ℝ`):

  §1 The general statement, independent of any choice of basis:
     for ANY `A B : Matrix (Fin 2) (Fin 2) K` with `tr A = tr B = h`,
     `tr((h²/2)·1 − (h/2)(A + B)) = 0`.
  §2 A concrete witness that the hypothesis is the `(2,1)` block of the Hecke
     algebra in this normalisation, `(σ − q)(σ + q⁻¹) = 0`:
         σ₁ = [[q, 0], [0, −q⁻¹]],   σ₂ = [[h − z_D, 1], [b², z_D]],
     with `z_D = q³/(q²+1)` (the convention-D Markov parameter) and
     `b² = (q⁴+q²+1)/(q²+1)²` (the Hoefsmit coupling squared). Both satisfy the
     quadratic relation, they satisfy the braid relation, and each has trace
     `h`. So §1 applies to this representation, and `tr ρ(Δ_S) = 0` for it.

  SCOPE, stated rather than implied. §2 exhibits a 2-dimensional
  representation in which both generators have eigenvalues `{q, −q⁻¹}`; that
  it IS the `(2,1)` irreducible (for generic `q`) is the standard Hoefsmit /
  seminormal-form fact and is not re-proved here. §1 does not need it: it
  holds for every representation whose generators have trace `h`, which is
  what "the `(2,1)` character takes the value `h` on `σᵢ`" means.
  Nothing numerical enters; nothing is wired.
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

namespace QOU.QBeta.DeltaSTwoRow

open Matrix

variable {K : Type*} [Field K]

/-- `h = q − q⁻¹`. -/
def h (q : K) : K := q - q⁻¹

/-- The convention-D Markov parameter `z_D = q³/(q²+1)`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- The Hoefsmit coupling squared, `b² = (q⁴+q²+1)/(q²+1)²`. -/
def bSq (q : K) : K := (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2

/-- The single-wrap element evaluated on a pair of generator images. -/
def deltaS (q : K) (A B : Matrix (Fin 2) (Fin 2) K) : Matrix (Fin 2) (Fin 2) K :=
  (h q ^ 2 / 2) • (1 : Matrix (Fin 2) (Fin 2) K) - (h q / 2) • (A + B)

/-! ## §1 The general statement -/

/-- For ANY two `2 × 2` matrices whose traces are `h`, the image of `Δ_S` is
traceless. Needs only `2 ≠ 0`. -/
theorem trace_deltaS_eq_zero (q : K) (h2 : (2 : K) ≠ 0)
    (A B : Matrix (Fin 2) (Fin 2) K) (hA : A.trace = h q) (hB : B.trace = h q) :
    (deltaS q A B).trace = 0 := by
  simp only [deltaS, trace_sub, trace_smul, trace_add, hA, hB, trace_one,
    Fintype.card_fin, smul_eq_mul]
  field_simp
  ring

/-! ## §2 The explicit `(2,1)` representation -/

/-- `σ₁ ↦ diag(q, −q⁻¹)`. -/
def s1 (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, 0; 0, -q⁻¹]

/-- `σ₂ ↦ [[h − z_D, 1], [b², z_D]]`. -/
def s2 (q : K) : Matrix (Fin 2) (Fin 2) K := !![h q - zD q, 1; bSq q, zD q]

theorem trace_s1 (q : K) : (s1 q).trace = h q := by
  simp [s1, h, Matrix.trace, Fin.sum_univ_two, sub_eq_add_neg]

theorem trace_s2 (q : K) :
    (s2 q).trace = h q := by
  simp [s2, Matrix.trace, Fin.sum_univ_two]

/-- `h − z_D = −1/(q(q²+1))`: the top-left entry of `σ₂` in closed form. -/
theorem h_sub_zD (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    h q - zD q = -1 / (q * (q ^ 2 + 1)) := by
  simp only [zD, h]
  field_simp
  ring

theorem s1_quadratic (q : K) :
    (s1 q - q • (1 : Matrix (Fin 2) (Fin 2) K)) * (s1 q + q⁻¹ • 1) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [s1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]

theorem s2_quadratic (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    (s2 q - q • (1 : Matrix (Fin 2) (Fin 2) K)) * (s2 q + q⁻¹ • 1) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [s2, zD, h, bSq, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

theorem braid (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    s1 q * s2 q * s1 q = s2 q * s1 q * s2 q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [s1, s2, zD, h, bSq, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **`χ_(2,1)(Δ_S) = 0`** in the explicit representation of §2. -/
theorem chi21_deltaS_eq_zero (q : K) (h2 : (2 : K) ≠ 0) :
    (deltaS q (s1 q) (s2 q)).trace = 0 :=
  trace_deltaS_eq_zero q h2 _ _ (trace_s1 q) (trace_s2 q)

end QOU.QBeta.DeltaSTwoRow
