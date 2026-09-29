import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

/-!
# QOU.QBeta.FiveTwoStokesMatrixIdentities

Algebraic consistency of the concrete `5₂` Stokes pair `(S⁺, S⁻)`.

This file **promotes to sorry-free theorems** the numerical checks that
were run in the `5₂` state-integral / Stokes-sandwich campaign
(PR #4487's V1/V2, and the exact-arithmetic checks K1/K2/K3 in
`computations/probes/qbeta_g3_5two_stokes_sandwich.py`). Every statement
here is a **finite, decidable algebraic identity** about **concrete
integer / rational matrices** — genuinely Lean-provable, no analysis.

## What is (and is not) proved

The `5₂` Stokes sandwiches `S±(q)` are `3×3` matrices of integer
`q`-series (Stokes integrality; the K2 check of the sandwich probe).
Write `S±(q) = Σ_k S±[k] · qᵏ` with each `S±[k] ∈ Mat₃(ℤ)`. The
coefficient matrices `S±[0..3]` below are the **exact rational-series
output** of the derived sandwich compute (glyph-decoded `(95a/b)`,
assembled from the fully-pinned tower layer). We prove:

* `det S⁺[0] = 1`, `det S⁻[0] = 1` — the leading (`q→0`) Stokes
  matrices are unimodular (the printed `(96/97)` factorization
  constants `3, 4`). Promotes the `det S±(q) = 1` check (K3) at
  leading order.
* `det W₋₁[0] = -2` — the `q→0` `W₋₁` block has determinant of
  magnitude `2` (the `W₋₁` "det ±2" phenomenon). Here `W₋₁[0]` is
  **rational** (denominators of `6`, from the derived `c`-slot
  subtraction), so the honest statement is over `ℚ` and the value is
  `-2`, not the fitted-integer `+2` an earlier framing assumed.
* **Inversion, leading order:** `(S⁺[0])ᵀ · S⁻[0] = I`. Promotes
  PR #4487's numerical inversion V1 at `q→0`.
* **Inversion, truncated to order `q³`:** the convolution coefficient
  matrices of `(S⁺(q))ᵀ · S⁻(q)` vanish for `k = 1, 2, 3` (and equal
  `I` at `k = 0`). This is the algebraic promotion of V1 **as a
  polynomial identity to order `q³`** — the untruncated
  `(S⁺(q))ᵀ · S⁻(q) = I` for all orders is beaned (`qou-9dvz`
  follow-up) since it needs closed-form series entries not available
  symbolically here.

## Scope (honesty, per AGENTS.md)

These are **fibre-side, purely algebraic** facts about the concrete
Stokes matrices. They do **not** prove FW Theorem 1.4, do **not** show
the analytic integrals `I_{j,k}` satisfy these relations, and — per the
program roast (`qou-l7vf`) — do **not** bridge to the archimedean
`c₃`. No `ℝ`/`ℂ`; no ordering, no `Real.*`; §7c base-ring rule
satisfied (concrete `ℤ[q^±]`-algebra data over `ℤ`/`ℚ`).

Source of the matrix data:
`computations/probes/qbeta_g3_5two_stokes_sandwich.py` (unflipped
`W`-convention, the K1/K2-passing orientation).
-/

namespace QOU.QBeta.FiveTwoStokes

open Matrix

/-! ## Leading (`q→0`) Stokes matrices -/

/-- `S⁺[0]`: the `q→0` limit of the `(95a)` Stokes sandwich `S⁺(q)`,
i.e. the glyph-decoded `(96)` factorization matrix (constant `4`). -/
def Splus0 : Matrix (Fin 3) (Fin 3) ℤ :=
  !![1, 4, 0; 0, 1, 0; -3, -9, 1]

/-- `S⁻[0]`: the `q→0` limit of the `(95b)` Stokes sandwich `S⁻(q)`,
i.e. the glyph-decoded `(97)` factorization matrix (constant `3`). -/
def Sminus0 : Matrix (Fin 3) (Fin 3) ℤ :=
  !![1, 0, 3; -4, 1, -3; 0, 0, 1]

/-- The `q→0` `W₋₁` block (rational; denominators of `6` from the
derived `c`-slot subtraction). -/
def Wminus1_0 : Matrix (Fin 3) (Fin 3) ℚ :=
  !![(-1)/6, 0, 1; 5/6, 1, 1; 23/6, 2, 1]

/-- Leading Stokes matrix `S⁺[0]` is unimodular. -/
theorem Splus0_det : Splus0.det = 1 := by
  simp [Splus0, Matrix.det_fin_three]

/-- Leading Stokes matrix `S⁻[0]` is unimodular. -/
theorem Sminus0_det : Sminus0.det = 1 := by
  simp [Sminus0, Matrix.det_fin_three]

/-- The `q→0` `W₋₁` block has determinant `-2` (magnitude `2`): the
`W₋₁` "det ±2" Stokes phenomenon, over `ℚ`. -/
theorem Wminus1_0_det : Wminus1_0.det = -2 := by
  simp [Wminus1_0, Matrix.det_fin_three]
  norm_num

/-- The `W₋₁` determinant has magnitude `2`. -/
theorem Wminus1_0_det_abs : |Wminus1_0.det| = 2 := by
  rw [Wminus1_0_det]; norm_num

/-! ## Inversion identity — leading order

The exact-arithmetic sandwich compute finds `(S⁺(q))ᵀ · S⁻(q) = I`
(verified to `O(q⁸)` in the probe cross-check). At `q→0` this is the
concrete integer-matrix identity below — PR #4487's numerical V1 at
leading order. -/

theorem Splus0_transpose_mul_Sminus0 : Splus0ᵀ * Sminus0 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Splus0, Sminus0, Matrix.mul_apply, Fin.sum_univ_three,
      Matrix.transpose_apply]

/-! ## Inversion identity — truncated to order `q³`

The full `q`-series coefficient matrices `S±[k]` (`k = 0,1,2,3`), as
produced by the derived sandwich compute, are all **integer** (Stokes
integrality). We prove the order-by-order inversion: the convolution
`Pₖ = Σ_{a+b=k} (S⁺[a])ᵀ · S⁻[b]` is `I` at `k = 0` and `0` at
`k = 1, 2, 3`. Hence `(S⁺(q))ᵀ · S⁻(q) = I + O(q⁴)` as a polynomial
matrix identity. The untruncated all-order statement is beaned
(`qou-9dvz` follow-up). -/

/-- `S⁺[1]`. -/
def Splus1 : Matrix (Fin 3) (Fin 3) ℤ :=
  !![-12, -33, 1; -12, -39, -1; 15, 36, -3]
/-- `S⁺[2]`. -/
def Splus2 : Matrix (Fin 3) (Fin 3) ℤ :=
  !![3, -18, -9; 24, 27, -15; 8, 42, 6]
/-- `S⁺[3]`. -/
def Splus3 : Matrix (Fin 3) (Fin 3) ℤ :=
  !![74, 151, -24; 119, 293, -21; -51, -78, 26]
/-- `S⁻[1]`. -/
def Sminus1 : Matrix (Fin 3) (Fin 3) ℤ :=
  !![-51, 15, -24; 36, -12, 15; -5, 1, -3]
/-- `S⁻[2]`. -/
def Sminus2 : Matrix (Fin 3) (Fin 3) ℤ :=
  !![51, -30, 10; 12, 3, 8; 21, -9, 6]
/-- `S⁻[3]`. -/
def Sminus3 : Matrix (Fin 3) (Fin 3) ℤ :=
  !![397, -145, 126; -177, 74, -51; 75, -24, 26]

/-- Order-`q⁰` coefficient of `(S⁺(q))ᵀ · S⁻(q)` is `I`. -/
theorem inversion_coeff0 : Splus0ᵀ * Sminus0 = 1 :=
  Splus0_transpose_mul_Sminus0

/-- Order-`q¹` coefficient of `(S⁺(q))ᵀ · S⁻(q)` vanishes. -/
theorem inversion_coeff1 :
    Splus0ᵀ * Sminus1 + Splus1ᵀ * Sminus0 = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Splus0, Splus1, Sminus0, Sminus1, Matrix.mul_apply,
      Fin.sum_univ_three, Matrix.transpose_apply, Matrix.add_apply]

/-- Order-`q²` coefficient of `(S⁺(q))ᵀ · S⁻(q)` vanishes. -/
theorem inversion_coeff2 :
    Splus0ᵀ * Sminus2 + Splus1ᵀ * Sminus1 + Splus2ᵀ * Sminus0 = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Splus0, Splus1, Splus2, Sminus0, Sminus1, Sminus2,
      Matrix.mul_apply, Fin.sum_univ_three, Matrix.transpose_apply,
      Matrix.add_apply]

/-- Order-`q³` coefficient of `(S⁺(q))ᵀ · S⁻(q)` vanishes. -/
theorem inversion_coeff3 :
    Splus0ᵀ * Sminus3 + Splus1ᵀ * Sminus2 + Splus2ᵀ * Sminus1
      + Splus3ᵀ * Sminus0 = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Splus0, Splus1, Splus2, Splus3, Sminus0, Sminus1, Sminus2,
      Sminus3, Matrix.mul_apply, Fin.sum_univ_three,
      Matrix.transpose_apply, Matrix.add_apply]

end QOU.QBeta.FiveTwoStokes
