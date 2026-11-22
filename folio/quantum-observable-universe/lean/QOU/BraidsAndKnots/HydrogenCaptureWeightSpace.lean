import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

/-!
# The hydrogen capture braid on four strands: the weight-space reduction

Level-2 Jimbo braiding on `(C²)^{⊗4}`, `h = q - q⁻¹`:
`Ř e₀₀ = q e₀₀`, `Ř e₀₁ = e₁₀`, `Ř e₁₀ = e₀₁ + h e₁₀`, `Ř e₁₁ = q e₁₁`.
`Ř` preserves the number of zeros, so every braid word is block diagonal over the weights.

* `A i` is `σ_i` on the weight space with one zero (basis: the zero on strand `0, 1, 2, 3`).
* `B i` is `σ_i` on the weight space with one one (basis index `k` = the one on strand `3 - k`).
* `Ai i`, `Bi i` are the inverses `σ_i⁻¹ = σ_i - h` (Hecke relation; checked in `A_mul_Ai`).

**Intertwiner.** An explicit invertible `P` (`det P = -q⁶(q⁴ + q² + 1)`) satisfies
`P · A i = B i · P` for `i = 0, 1, 2`. So every braid word has the same trace on the two weight
spaces (`trace_wordA_eq_wordB`), as for three strands in
`NucleonWeightSpaceTraces.trace_word_eq`.

**The functional.** In the four-strand probe of the m_n own-identity work (draft PR #8804,
`mn_hydrogen_capture_chirality_probe`), `F(O) = tr(T³ · W · Π_O)` with `T³ = (#0 − #1)/2`, and
`Π_O` projects onto states whose three proton strands carry two zeros (`O₊`) or one zero (`O₋`).
On those states `T³ = z − 2` with `z` the number of zeros, and `z = 2` contributes `T³ = 0`.
So with the proton on strands `0–2` only the two four-dimensional weight spaces enter:

  `F(O₊) = W_B 1 1 + W_B 2 2 + W_B 3 3`,   `F(O₋) = −(W_A 0 0 + W_A 1 1 + W_A 2 2)`.

This reduction is stated in the docstring, not formalised here. The theorems below start from
these weight-space expressions.

**Results (generic field `R`, `q ≠ 0`, `q⁴ + q² + 1 ≠ 0`).**
* `S_eq_entry_diff`: `S = F(O₊) + F(O₋) = W_A 3 3 − W_B 0 0` for every braid word. So the
  orientation asymmetry is the minority-spin-on-the-electron diagonal entry of one weight space
  minus that of the other.
* The capture word `W_L = (σ₀σ₁⁻¹)³ · (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹` (proton strands `0–2`, electron strand
  `3`): `W_A 3 3 = 1` and `W_B 0 0 = (q⁸ − q² + 1)/q⁶`, hence
  `S = −(q² − 1)²(q⁴ + q² + 1)/q⁶ = −h²[3]_q/q²`.
* `F(O₊; W_L) = −P(q)/q¹⁰` with `P = q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1`. This is the same
  polynomial as the numerator of `ε_flavour(V³) = (q² − 1)P/(q⁴(q² + 1)³)` in
  `FlavourWeightSplit`. That match is recorded as a computed fact; no link between the two
  objects is derived here.
* Placement mirror: the capture word with the proton on strands `1–3`
  (`(σ₁σ₂⁻¹)³ · (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹`) gives `S = +(q² − 1)²(q⁴ + q² + 1)/q⁶`.

`(σ₀σ₁⁻¹)³` is the γγ product of the photon `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`
(`borromeanV3A_eq_switched_photon_product`). No numerical value enters.
-/

namespace QOU.BraidsAndKnots.HydrogenCaptureWeightSpace

open Matrix

variable {R : Type*} [Field R]

-- The generated step vectors do not all mention `q`, and not every step needs `hq`.
set_option linter.unusedVariables false

/-! ### Generators on the one-zero weight space -/
def A0 (q : R) : Matrix (Fin 4) (Fin 4) R := !![0, 1, 0, 0; 1, q - q⁻¹, 0, 0; 0, 0, q, 0; 0, 0, 0, q]
def A1 (q : R) : Matrix (Fin 4) (Fin 4) R := !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]
def A2 (q : R) : Matrix (Fin 4) (Fin 4) R := !![q, 0, 0, 0; 0, q, 0, 0; 0, 0, 0, 1; 0, 0, 1, q - q⁻¹]
def A0i (q : R) : Matrix (Fin 4) (Fin 4) R := !![-(q - q⁻¹), 1, 0, 0; 1, 0, 0, 0; 0, 0, q⁻¹, 0; 0, 0, 0, q⁻¹]
def A1i (q : R) : Matrix (Fin 4) (Fin 4) R := !![q⁻¹, 0, 0, 0; 0, -(q - q⁻¹), 1, 0; 0, 1, 0, 0; 0, 0, 0, q⁻¹]
def A2i (q : R) : Matrix (Fin 4) (Fin 4) R := !![q⁻¹, 0, 0, 0; 0, q⁻¹, 0, 0; 0, 0, -(q - q⁻¹), 1; 0, 0, 1, 0]

/-! ### Generators on the one-one weight space -/
def B0 (q : R) : Matrix (Fin 4) (Fin 4) R := !![q, 0, 0, 0; 0, q, 0, 0; 0, 0, 0, 1; 0, 0, 1, q - q⁻¹]
def B1 (q : R) : Matrix (Fin 4) (Fin 4) R := !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]
def B2 (q : R) : Matrix (Fin 4) (Fin 4) R := !![0, 1, 0, 0; 1, q - q⁻¹, 0, 0; 0, 0, q, 0; 0, 0, 0, q]
def B0i (q : R) : Matrix (Fin 4) (Fin 4) R := !![q⁻¹, 0, 0, 0; 0, q⁻¹, 0, 0; 0, 0, -(q - q⁻¹), 1; 0, 0, 1, 0]
def B1i (q : R) : Matrix (Fin 4) (Fin 4) R := !![q⁻¹, 0, 0, 0; 0, -(q - q⁻¹), 1, 0; 0, 1, 0, 0; 0, 0, 0, q⁻¹]
def B2i (q : R) : Matrix (Fin 4) (Fin 4) R := !![-(q - q⁻¹), 1, 0, 0; 1, 0, 0, 0; 0, 0, q⁻¹, 0; 0, 0, 0, q⁻¹]

set_option hygiene false in
macro "matTac" : tactic => `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
  simp [A0, A1, A2, A0i, A1i, A2i, B0, B1, B2, B0i, B1i, B2i, P, Matrix.mul_apply,
    Fin.sum_univ_four, Matrix.one_apply] <;> field_simp <;> ring))

/-- The intertwiner. -/
def P (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![1, q, q ^ 2, 0; q, q ^ 2, 0, q ^ 2; q ^ 2, 0, q ^ 2, q ^ 3; 0, q ^ 2, q ^ 3, q ^ 4]

theorem A0_mul_A0i (q : R) (hq : q ≠ 0) : A0 q * A0i q = 1 := by matTac
theorem A1_mul_A1i (q : R) (hq : q ≠ 0) : A1 q * A1i q = 1 := by matTac
theorem A2_mul_A2i (q : R) (hq : q ≠ 0) : A2 q * A2i q = 1 := by matTac
theorem B0_mul_B0i (q : R) (hq : q ≠ 0) : B0 q * B0i q = 1 := by matTac
theorem B1_mul_B1i (q : R) (hq : q ≠ 0) : B1 q * B1i q = 1 := by matTac
theorem B2_mul_B2i (q : R) (hq : q ≠ 0) : B2 q * B2i q = 1 := by matTac

theorem det_P (q : R) : (P q).det = -(q ^ 6 * (q ^ 4 + q ^ 2 + 1)) := by
  simp [P, Matrix.det_succ_row_zero, Fin.sum_univ_succ, Matrix.submatrix]
  simp [Fin.succAbove, Fin.castSucc, Fin.succ, Fin.castAdd, Fin.castLE]
  ring

theorem intertwine0 (q : R) (hq : q ≠ 0) : P q * A0 q = B0 q * P q := by matTac
theorem intertwine1 (q : R) (hq : q ≠ 0) : P q * A1 q = B1 q * P q := by matTac
theorem intertwine2 (q : R) (hq : q ≠ 0) : P q * A2 q = B2 q * P q := by matTac
theorem intertwine0i (q : R) (hq : q ≠ 0) : P q * A0i q = B0i q * P q := by matTac
theorem intertwine1i (q : R) (hq : q ≠ 0) : P q * A1i q = B1i q * P q := by matTac
theorem intertwine2i (q : R) (hq : q ≠ 0) : P q * A2i q = B2i q * P q := by matTac

/-- A letter: strand index and `true` for an inverse crossing. -/
abbrev Letter := Fin 3 × Bool

def gA (q : R) : Letter → Matrix (Fin 4) (Fin 4) R
  | (0, false) => A0 q | (1, false) => A1 q | (2, false) => A2 q
  | (0, true) => A0i q | (1, true) => A1i q | (2, true) => A2i q

def gB (q : R) : Letter → Matrix (Fin 4) (Fin 4) R
  | (0, false) => B0 q | (1, false) => B1 q | (2, false) => B2 q
  | (0, true) => B0i q | (1, true) => B1i q | (2, true) => B2i q

/-- A braid word acting on the one-zero weight space (product in list order). -/
def wordA (q : R) : List Letter → Matrix (Fin 4) (Fin 4) R
  | [] => 1
  | l :: w => gA q l * wordA q w

/-- A braid word acting on the one-one weight space. -/
def wordB (q : R) : List Letter → Matrix (Fin 4) (Fin 4) R
  | [] => 1
  | l :: w => gB q l * wordB q w

theorem intertwine_letter (q : R) (hq : q ≠ 0) (l : Letter) :
    P q * gA q l = gB q l * P q := by
  obtain ⟨i, b⟩ := l
  fin_cases i <;> cases b <;> simp only [gA, gB] <;>
    first
    | exact intertwine0 q hq | exact intertwine1 q hq | exact intertwine2 q hq
    | exact intertwine0i q hq | exact intertwine1i q hq | exact intertwine2i q hq

theorem intertwine_word (q : R) (hq : q ≠ 0) (w : List Letter) :
    P q * wordA q w = wordB q w * P q := by
  induction w with
  | nil => simp [wordA, wordB]
  | cons l w ih =>
    simp only [wordA, wordB]
    rw [← mul_assoc, intertwine_letter q hq l, mul_assoc, ih, mul_assoc]

/-- **Equal traces.** Every braid word has the same trace on the two weight spaces. -/
theorem trace_wordA_eq_wordB (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0)
    (w : List Letter) : trace (wordA q w) = trace (wordB q w) := by
  have hdet : IsUnit (P q).det := by
    rw [det_P]
    exact isUnit_iff_ne_zero.mpr (neg_ne_zero.mpr (mul_ne_zero (pow_ne_zero 6 hq) h3))
  have key : wordB q w = P q * wordA q w * (P q)⁻¹ := by
    rw [intertwine_word q hq w, mul_assoc, Matrix.mul_nonsing_inv _ hdet, mul_one]
  rw [key, Matrix.trace_mul_cycle, Matrix.nonsing_inv_mul _ hdet, one_mul]

/-- `F(O₊)` with the proton on strands `0–2`, on the one-one weight space. -/
def FplusL (WB : Matrix (Fin 4) (Fin 4) R) : R := WB 1 1 + WB 2 2 + WB 3 3
/-- `F(O₋)` with the proton on strands `0–2`, on the one-zero weight space. -/
def FminusL (WA : Matrix (Fin 4) (Fin 4) R) : R := -(WA 0 0 + WA 1 1 + WA 2 2)

/-- **The orientation sum is one entry minus another** (proton on strands `0–2`). -/
theorem S_eq_entry_diff (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0)
    (w : List Letter) :
    FplusL (wordB q w) + FminusL (wordA q w) = wordA q w 3 3 - wordB q w 0 0 := by
  have ht := trace_wordA_eq_wordB q hq h3 w
  simp only [Matrix.trace, Matrix.diag, Fin.sum_univ_four] at ht
  simp only [FplusL, FminusL]
  linear_combination -ht

/-- Same, with the proton on strands `1–3` (electron strand `0`). -/
theorem S_eq_entry_diff_right (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0)
    (w : List Letter) :
    (wordB q w 0 0 + wordB q w 1 1 + wordB q w 2 2)
      - (wordA q w 1 1 + wordA q w 2 2 + wordA q w 3 3)
      = wordA q w 0 0 - wordB q w 3 3 := by
  have ht := trace_wordA_eq_wordB q hq h3 w
  simp only [Matrix.trace, Matrix.diag, Fin.sum_univ_four] at ht
  linear_combination -ht

/-! ### The capture words -/

/-- `(σ₀σ₁⁻¹)³ · (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹`: proton on strands `0–2`, electron strand `3`. -/
def capL : List Letter :=
  [(0, false), (1, true), (0, false), (1, true), (0, false), (1, true),
   (2, true), (1, true), (0, true), (0, true), (1, true), (2, true)]

/-- `(σ₁σ₂⁻¹)³ · (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹`: proton on strands `1–3`, electron strand `0`. -/
def capR : List Letter :=
  [(1, false), (2, true), (1, false), (2, true), (1, false), (2, true),
   (0, true), (1, true), (2, true), (2, true), (1, true), (0, true)]

theorem wordA_mulVec_cons (q : R) (l : Letter) (w : List Letter) (v : Fin 4 → R) :
    (wordA q (l :: w)).mulVec v = (gA q l).mulVec ((wordA q w).mulVec v) := by
  simp [wordA, Matrix.mulVec_mulVec]

theorem wordB_mulVec_cons (q : R) (l : Letter) (w : List Letter) (v : Fin 4 → R) :
    (wordB q (l :: w)).mulVec v = (gB q l).mulVec ((wordB q w).mulVec v) := by
  simp [wordB, Matrix.mulVec_mulVec]

set_option hygiene false in
macro "stepTac" : tactic => `(tactic| (ext i; fin_cases i <;>
  simp [A0, A1, A2, A0i, A1i, A2i, B0, B1, B2, B0i, B1i, B2i, Matrix.mulVec, dotProduct,
    Fin.sum_univ_four, Pi.single_apply] <;> (try field_simp) <;> (try ring)))

@[simp] def capLA3_v0 (q : R) : Fin 4 → R := ![(0), (0), (1), (0)]

theorem capLA3_step0 (q : R) (hq : q ≠ 0) :
    (A2i q).mulVec (Pi.single 3 1) = capLA3_v0 q := by
  stepTac

@[simp] def capLA3_v1 (q : R) : Fin 4 → R := ![(0), (1), (0), (0)]

theorem capLA3_step1 (q : R) (hq : q ≠ 0) :
    (A1i q).mulVec (capLA3_v0 q) = capLA3_v1 q := by
  stepTac

@[simp] def capLA3_v2 (q : R) : Fin 4 → R := ![(1), (0), (0), (0)]

theorem capLA3_step2 (q : R) (hq : q ≠ 0) :
    (A0i q).mulVec (capLA3_v1 q) = capLA3_v2 q := by
  stepTac

@[simp] def capLA3_v3 (q : R) : Fin 4 → R := ![((1 - q^2) / q), (1), (0), (0)]

theorem capLA3_step3 (q : R) (hq : q ≠ 0) :
    (A0i q).mulVec (capLA3_v2 q) = capLA3_v3 q := by
  stepTac

@[simp] def capLA3_v4 (q : R) : Fin 4 → R := ![((1 - q^2) / q^2), ((1 - q^2) / q), (1), (0)]

theorem capLA3_step4 (q : R) (hq : q ≠ 0) :
    (A1i q).mulVec (capLA3_v3 q) = capLA3_v4 q := by
  stepTac

@[simp] def capLA3_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capLA3_step5 (q : R) (hq : q ≠ 0) :
    (A2i q).mulVec (capLA3_v4 q) = capLA3_v5 q := by
  stepTac

@[simp] def capLA3_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1) / q)]

theorem capLA3_step6 (q : R) (hq : q ≠ 0) :
    (A1i q).mulVec (capLA3_v5 q) = capLA3_v6 q := by
  stepTac

@[simp] def capLA3_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capLA3_step7 (q : R) (hq : q ≠ 0) :
    (A0 q).mulVec (capLA3_v6 q) = capLA3_v7 q := by
  stepTac

@[simp] def capLA3_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1) / q)]

theorem capLA3_step8 (q : R) (hq : q ≠ 0) :
    (A1i q).mulVec (capLA3_v7 q) = capLA3_v8 q := by
  stepTac

@[simp] def capLA3_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capLA3_step9 (q : R) (hq : q ≠ 0) :
    (A0 q).mulVec (capLA3_v8 q) = capLA3_v9 q := by
  stepTac

@[simp] def capLA3_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1) / q)]

theorem capLA3_step10 (q : R) (hq : q ≠ 0) :
    (A1i q).mulVec (capLA3_v9 q) = capLA3_v10 q := by
  stepTac

@[simp] def capLA3_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capLA3_step11 (q : R) (hq : q ≠ 0) :
    (A0 q).mulVec (capLA3_v10 q) = capLA3_v11 q := by
  stepTac



@[simp] def capLB0_v0 (q : R) : Fin 4 → R := ![((1 - q^2) / q), (1), (0), (0)]

theorem capLB0_step0 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (Pi.single 0 1) = capLB0_v0 q := by
  stepTac

@[simp] def capLB0_v1 (q : R) : Fin 4 → R := ![((1 - q^2) / q^2), ((1 - q^2) / q), (1), (0)]

theorem capLB0_step1 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB0_v0 q) = capLB0_v1 q := by
  stepTac

@[simp] def capLB0_v2 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capLB0_step2 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (capLB0_v1 q) = capLB0_v2 q := by
  stepTac

@[simp] def capLB0_v3 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1 - q^2) / q^3), ((q^4 - q^2 + 1) / q^2), ((1 - q^2) / q)]

theorem capLB0_step3 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (capLB0_v2 q) = capLB0_v3 q := by
  stepTac

@[simp] def capLB0_v4 (q : R) : Fin 4 → R := ![((1 - q^2) / q^5), ((q^6 - q^2 + 1) / q^4), ((1 - q^2) / q^3), ((1 - q^2) / q^2)]

theorem capLB0_step4 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB0_v3 q) = capLB0_v4 q := by
  stepTac

@[simp] def capLB0_v5 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3)]

theorem capLB0_step5 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (capLB0_v4 q) = capLB0_v5 q := by
  stepTac

@[simp] def capLB0_v6 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^7), ((1 - q^2) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4)]

theorem capLB0_step6 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB0_v5 q) = capLB0_v6 q := by
  stepTac

@[simp] def capLB0_v7 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3)]

theorem capLB0_step7 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB0_v6 q) = capLB0_v7 q := by
  stepTac

@[simp] def capLB0_v8 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^7), ((1 - q^2) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4)]

theorem capLB0_step8 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB0_v7 q) = capLB0_v8 q := by
  stepTac

@[simp] def capLB0_v9 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3)]

theorem capLB0_step9 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB0_v8 q) = capLB0_v9 q := by
  stepTac

@[simp] def capLB0_v10 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^7), ((1 - q^2) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4)]

theorem capLB0_step10 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB0_v9 q) = capLB0_v10 q := by
  stepTac

@[simp] def capLB0_v11 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3)]

theorem capLB0_step11 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB0_v10 q) = capLB0_v11 q := by
  stepTac



@[simp] def capLB1_v0 (q : R) : Fin 4 → R := ![(1), (0), (0), (0)]

theorem capLB1_step0 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (Pi.single 1 1) = capLB1_v0 q := by
  stepTac

@[simp] def capLB1_v1 (q : R) : Fin 4 → R := ![((1) / q), (0), (0), (0)]

theorem capLB1_step1 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB1_v0 q) = capLB1_v1 q := by
  stepTac

@[simp] def capLB1_v2 (q : R) : Fin 4 → R := ![((1) / q^2), (0), (0), (0)]

theorem capLB1_step2 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (capLB1_v1 q) = capLB1_v2 q := by
  stepTac

@[simp] def capLB1_v3 (q : R) : Fin 4 → R := ![((1) / q^3), (0), (0), (0)]

theorem capLB1_step3 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (capLB1_v2 q) = capLB1_v3 q := by
  stepTac

@[simp] def capLB1_v4 (q : R) : Fin 4 → R := ![((1) / q^4), (0), (0), (0)]

theorem capLB1_step4 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB1_v3 q) = capLB1_v4 q := by
  stepTac

@[simp] def capLB1_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / q^5), ((1) / q^4), (0), (0)]

theorem capLB1_step5 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (capLB1_v4 q) = capLB1_v5 q := by
  stepTac

@[simp] def capLB1_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / q^6), ((1 - q^2) / q^5), ((1) / q^4), (0)]

theorem capLB1_step6 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB1_v5 q) = capLB1_v6 q := by
  stepTac

@[simp] def capLB1_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / q^5), ((1 - q^2) / q^4), (0), ((1) / q^4)]

theorem capLB1_step7 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB1_v6 q) = capLB1_v7 q := by
  stepTac

@[simp] def capLB1_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((1 - q^2) / q^4), ((1) / q^5)]

theorem capLB1_step8 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB1_v7 q) = capLB1_v8 q := by
  stepTac

@[simp] def capLB1_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((1) / q^5), ((-q^4 + 2*q^2 - 1) / q^6)]

theorem capLB1_step9 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB1_v8 q) = capLB1_v9 q := by
  stepTac

@[simp] def capLB1_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / q^6), ((-q^6 + 3*q^4 - 3*q^2 + 2) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^7)]

theorem capLB1_step10 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB1_v9 q) = capLB1_v10 q := by
  stepTac

@[simp] def capLB1_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / q^5), ((-q^6 + 3*q^4 - 3*q^2 + 2) / q^4), ((-q^4 + 2*q^2 - 1) / q^7), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^8)]

theorem capLB1_step11 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB1_v10 q) = capLB1_v11 q := by
  stepTac



@[simp] def capLB2_v0 (q : R) : Fin 4 → R := ![(0), (0), ((1) / q), (0)]

theorem capLB2_step0 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (Pi.single 2 1) = capLB2_v0 q := by
  stepTac

@[simp] def capLB2_v1 (q : R) : Fin 4 → R := ![(0), ((1) / q), (0), (0)]

theorem capLB2_step1 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB2_v0 q) = capLB2_v1 q := by
  stepTac

@[simp] def capLB2_v2 (q : R) : Fin 4 → R := ![(0), ((1) / q^2), (0), (0)]

theorem capLB2_step2 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (capLB2_v1 q) = capLB2_v2 q := by
  stepTac

@[simp] def capLB2_v3 (q : R) : Fin 4 → R := ![(0), ((1) / q^3), (0), (0)]

theorem capLB2_step3 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (capLB2_v2 q) = capLB2_v3 q := by
  stepTac

@[simp] def capLB2_v4 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / q^4), ((1) / q^3), (0)]

theorem capLB2_step4 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB2_v3 q) = capLB2_v4 q := by
  stepTac

@[simp] def capLB2_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), (0), ((1) / q^4), (0)]

theorem capLB2_step5 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (capLB2_v4 q) = capLB2_v5 q := by
  stepTac

@[simp] def capLB2_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / q^5), ((1) / q^4), (0), (0)]

theorem capLB2_step6 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB2_v5 q) = capLB2_v6 q := by
  stepTac

@[simp] def capLB2_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1) / q^3), (0), (0)]

theorem capLB2_step7 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB2_v6 q) = capLB2_v7 q := by
  stepTac

@[simp] def capLB2_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1) / q^3), (0)]

theorem capLB2_step8 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB2_v7 q) = capLB2_v8 q := by
  stepTac

@[simp] def capLB2_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1 - q^2) / q^3), (0), ((1) / q^3)]

theorem capLB2_step9 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB2_v8 q) = capLB2_v9 q := by
  stepTac

@[simp] def capLB2_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((1 - q^2) / q^3), ((1) / q^4)]

theorem capLB2_step10 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB2_v9 q) = capLB2_v10 q := by
  stepTac

@[simp] def capLB2_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((1) / q^4), ((-q^4 + 2*q^2 - 1) / q^5)]

theorem capLB2_step11 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB2_v10 q) = capLB2_v11 q := by
  stepTac



@[simp] def capLB3_v0 (q : R) : Fin 4 → R := ![(0), (0), (0), ((1) / q)]

theorem capLB3_step0 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (Pi.single 3 1) = capLB3_v0 q := by
  stepTac

@[simp] def capLB3_v1 (q : R) : Fin 4 → R := ![(0), (0), (0), ((1) / q^2)]

theorem capLB3_step1 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB3_v0 q) = capLB3_v1 q := by
  stepTac

@[simp] def capLB3_v2 (q : R) : Fin 4 → R := ![(0), (0), ((1) / q^2), (0)]

theorem capLB3_step2 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (capLB3_v1 q) = capLB3_v2 q := by
  stepTac

@[simp] def capLB3_v3 (q : R) : Fin 4 → R := ![(0), (0), ((1 - q^2) / q^3), ((1) / q^2)]

theorem capLB3_step3 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (capLB3_v2 q) = capLB3_v3 q := by
  stepTac

@[simp] def capLB3_v4 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / q^3), (0), ((1) / q^3)]

theorem capLB3_step4 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB3_v3 q) = capLB3_v4 q := by
  stepTac

@[simp] def capLB3_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), (0), (0), ((1) / q^4)]

theorem capLB3_step5 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (capLB3_v4 q) = capLB3_v5 q := by
  stepTac

@[simp] def capLB3_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), (0), (0), ((1) / q^5)]

theorem capLB3_step6 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB3_v5 q) = capLB3_v6 q := by
  stepTac

@[simp] def capLB3_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), (0), ((1) / q^5), ((q^2 - 1) / q^6)]

theorem capLB3_step7 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB3_v6 q) = capLB3_v7 q := by
  stepTac

@[simp] def capLB3_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1) / q^5), (0), ((q^2 - 1) / q^7)]

theorem capLB3_step8 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB3_v7 q) = capLB3_v8 q := by
  stepTac

@[simp] def capLB3_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1) / q^4), ((q^2 - 1) / q^7), ((q^4 - 2*q^2 + 1) / q^8)]

theorem capLB3_step9 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB3_v8 q) = capLB3_v9 q := by
  stepTac

@[simp] def capLB3_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((-q^4 + 2*q^2 - 1) / q^7), ((1) / q^4), ((q^4 - 2*q^2 + 1) / q^9)]

theorem capLB3_step10 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capLB3_v9 q) = capLB3_v10 q := by
  stepTac

@[simp] def capLB3_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((-q^4 + 2*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^9), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^10)]

theorem capLB3_step11 (q : R) (hq : q ≠ 0) :
    (B0 q).mulVec (capLB3_v10 q) = capLB3_v11 q := by
  stepTac



@[simp] def capRA0_v0 (q : R) : Fin 4 → R := ![((1 - q^2) / q), (1), (0), (0)]

theorem capRA0_step0 (q : R) (hq : q ≠ 0) :
    (A0i q).mulVec (Pi.single 0 1) = capRA0_v0 q := by
  stepTac

@[simp] def capRA0_v1 (q : R) : Fin 4 → R := ![((1 - q^2) / q^2), ((1 - q^2) / q), (1), (0)]

theorem capRA0_step1 (q : R) (hq : q ≠ 0) :
    (A1i q).mulVec (capRA0_v0 q) = capRA0_v1 q := by
  stepTac

@[simp] def capRA0_v2 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capRA0_step2 (q : R) (hq : q ≠ 0) :
    (A2i q).mulVec (capRA0_v1 q) = capRA0_v2 q := by
  stepTac

@[simp] def capRA0_v3 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1 - q^2) / q^3), ((q^4 - q^2 + 1) / q^2), ((1 - q^2) / q)]

theorem capRA0_step3 (q : R) (hq : q ≠ 0) :
    (A2i q).mulVec (capRA0_v2 q) = capRA0_v3 q := by
  stepTac

@[simp] def capRA0_v4 (q : R) : Fin 4 → R := ![((1 - q^2) / q^5), ((q^6 - q^2 + 1) / q^4), ((1 - q^2) / q^3), ((1 - q^2) / q^2)]

theorem capRA0_step4 (q : R) (hq : q ≠ 0) :
    (A1i q).mulVec (capRA0_v3 q) = capRA0_v4 q := by
  stepTac

@[simp] def capRA0_v5 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3)]

theorem capRA0_step5 (q : R) (hq : q ≠ 0) :
    (A0i q).mulVec (capRA0_v4 q) = capRA0_v5 q := by
  stepTac

@[simp] def capRA0_v6 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^7), ((1 - q^2) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4)]

theorem capRA0_step6 (q : R) (hq : q ≠ 0) :
    (A2i q).mulVec (capRA0_v5 q) = capRA0_v6 q := by
  stepTac

@[simp] def capRA0_v7 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3)]

theorem capRA0_step7 (q : R) (hq : q ≠ 0) :
    (A1 q).mulVec (capRA0_v6 q) = capRA0_v7 q := by
  stepTac

@[simp] def capRA0_v8 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^7), ((1 - q^2) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4)]

theorem capRA0_step8 (q : R) (hq : q ≠ 0) :
    (A2i q).mulVec (capRA0_v7 q) = capRA0_v8 q := by
  stepTac

@[simp] def capRA0_v9 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3)]

theorem capRA0_step9 (q : R) (hq : q ≠ 0) :
    (A1 q).mulVec (capRA0_v8 q) = capRA0_v9 q := by
  stepTac

@[simp] def capRA0_v10 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^7), ((1 - q^2) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4)]

theorem capRA0_step10 (q : R) (hq : q ≠ 0) :
    (A2i q).mulVec (capRA0_v9 q) = capRA0_v10 q := by
  stepTac

@[simp] def capRA0_v11 (q : R) : Fin 4 → R := ![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3)]

theorem capRA0_step11 (q : R) (hq : q ≠ 0) :
    (A1 q).mulVec (capRA0_v10 q) = capRA0_v11 q := by
  stepTac



@[simp] def capRB3_v0 (q : R) : Fin 4 → R := ![(0), (0), (1), (0)]

theorem capRB3_step0 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (Pi.single 3 1) = capRB3_v0 q := by
  stepTac

@[simp] def capRB3_v1 (q : R) : Fin 4 → R := ![(0), (1), (0), (0)]

theorem capRB3_step1 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capRB3_v0 q) = capRB3_v1 q := by
  stepTac

@[simp] def capRB3_v2 (q : R) : Fin 4 → R := ![(1), (0), (0), (0)]

theorem capRB3_step2 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (capRB3_v1 q) = capRB3_v2 q := by
  stepTac

@[simp] def capRB3_v3 (q : R) : Fin 4 → R := ![((1 - q^2) / q), (1), (0), (0)]

theorem capRB3_step3 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (capRB3_v2 q) = capRB3_v3 q := by
  stepTac

@[simp] def capRB3_v4 (q : R) : Fin 4 → R := ![((1 - q^2) / q^2), ((1 - q^2) / q), (1), (0)]

theorem capRB3_step4 (q : R) (hq : q ≠ 0) :
    (B1i q).mulVec (capRB3_v3 q) = capRB3_v4 q := by
  stepTac

@[simp] def capRB3_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capRB3_step5 (q : R) (hq : q ≠ 0) :
    (B0i q).mulVec (capRB3_v4 q) = capRB3_v5 q := by
  stepTac

@[simp] def capRB3_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1) / q)]

theorem capRB3_step6 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (capRB3_v5 q) = capRB3_v6 q := by
  stepTac

@[simp] def capRB3_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capRB3_step7 (q : R) (hq : q ≠ 0) :
    (B1 q).mulVec (capRB3_v6 q) = capRB3_v7 q := by
  stepTac

@[simp] def capRB3_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1) / q)]

theorem capRB3_step8 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (capRB3_v7 q) = capRB3_v8 q := by
  stepTac

@[simp] def capRB3_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capRB3_step9 (q : R) (hq : q ≠ 0) :
    (B1 q).mulVec (capRB3_v8 q) = capRB3_v9 q := by
  stepTac

@[simp] def capRB3_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / q^4), ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1) / q)]

theorem capRB3_step10 (q : R) (hq : q ≠ 0) :
    (B2i q).mulVec (capRB3_v9 q) = capRB3_v10 q := by
  stepTac

@[simp] def capRB3_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

theorem capRB3_step11 (q : R) (hq : q ≠ 0) :
    (B1 q).mulVec (capRB3_v10 q) = capRB3_v11 q := by
  stepTac



/-! ### Chaining the steps: matrix entries of the capture words -/

theorem wordA_nil (q : R) : wordA q [] = 1 := rfl
theorem wordB_nil (q : R) : wordB q [] = 1 := rfl

theorem entry_eq_mulVec_single (M : Matrix (Fin 4) (Fin 4) R) (i j : Fin 4) :
    M i j = (M.mulVec (Pi.single j 1)) i := by
  simp [Matrix.mulVec, dotProduct, Pi.single_apply]

theorem capLA3_col (q : R) (hq : q ≠ 0) :
    (wordA q capL).mulVec (Pi.single 3 1) = capLA3_v11 q := by
  simp only [capL, wordA_mulVec_cons, wordA_nil, Matrix.one_mulVec, gA]
  rw [capLA3_step0 q hq, capLA3_step1 q hq, capLA3_step2 q hq, capLA3_step3 q hq, capLA3_step4 q hq, capLA3_step5 q hq, capLA3_step6 q hq, capLA3_step7 q hq, capLA3_step8 q hq, capLA3_step9 q hq, capLA3_step10 q hq, capLA3_step11 q hq]

theorem capLB0_col (q : R) (hq : q ≠ 0) :
    (wordB q capL).mulVec (Pi.single 0 1) = capLB0_v11 q := by
  simp only [capL, wordB_mulVec_cons, wordB_nil, Matrix.one_mulVec, gB]
  rw [capLB0_step0 q hq, capLB0_step1 q hq, capLB0_step2 q hq, capLB0_step3 q hq, capLB0_step4 q hq, capLB0_step5 q hq, capLB0_step6 q hq, capLB0_step7 q hq, capLB0_step8 q hq, capLB0_step9 q hq, capLB0_step10 q hq, capLB0_step11 q hq]

theorem capLB1_col (q : R) (hq : q ≠ 0) :
    (wordB q capL).mulVec (Pi.single 1 1) = capLB1_v11 q := by
  simp only [capL, wordB_mulVec_cons, wordB_nil, Matrix.one_mulVec, gB]
  rw [capLB1_step0 q hq, capLB1_step1 q hq, capLB1_step2 q hq, capLB1_step3 q hq, capLB1_step4 q hq, capLB1_step5 q hq, capLB1_step6 q hq, capLB1_step7 q hq, capLB1_step8 q hq, capLB1_step9 q hq, capLB1_step10 q hq, capLB1_step11 q hq]

theorem capLB2_col (q : R) (hq : q ≠ 0) :
    (wordB q capL).mulVec (Pi.single 2 1) = capLB2_v11 q := by
  simp only [capL, wordB_mulVec_cons, wordB_nil, Matrix.one_mulVec, gB]
  rw [capLB2_step0 q hq, capLB2_step1 q hq, capLB2_step2 q hq, capLB2_step3 q hq, capLB2_step4 q hq, capLB2_step5 q hq, capLB2_step6 q hq, capLB2_step7 q hq, capLB2_step8 q hq, capLB2_step9 q hq, capLB2_step10 q hq, capLB2_step11 q hq]

theorem capLB3_col (q : R) (hq : q ≠ 0) :
    (wordB q capL).mulVec (Pi.single 3 1) = capLB3_v11 q := by
  simp only [capL, wordB_mulVec_cons, wordB_nil, Matrix.one_mulVec, gB]
  rw [capLB3_step0 q hq, capLB3_step1 q hq, capLB3_step2 q hq, capLB3_step3 q hq, capLB3_step4 q hq, capLB3_step5 q hq, capLB3_step6 q hq, capLB3_step7 q hq, capLB3_step8 q hq, capLB3_step9 q hq, capLB3_step10 q hq, capLB3_step11 q hq]

theorem capRA0_col (q : R) (hq : q ≠ 0) :
    (wordA q capR).mulVec (Pi.single 0 1) = capRA0_v11 q := by
  simp only [capR, wordA_mulVec_cons, wordA_nil, Matrix.one_mulVec, gA]
  rw [capRA0_step0 q hq, capRA0_step1 q hq, capRA0_step2 q hq, capRA0_step3 q hq, capRA0_step4 q hq, capRA0_step5 q hq, capRA0_step6 q hq, capRA0_step7 q hq, capRA0_step8 q hq, capRA0_step9 q hq, capRA0_step10 q hq, capRA0_step11 q hq]

theorem capRB3_col (q : R) (hq : q ≠ 0) :
    (wordB q capR).mulVec (Pi.single 3 1) = capRB3_v11 q := by
  simp only [capR, wordB_mulVec_cons, wordB_nil, Matrix.one_mulVec, gB]
  rw [capRB3_step0 q hq, capRB3_step1 q hq, capRB3_step2 q hq, capRB3_step3 q hq, capRB3_step4 q hq, capRB3_step5 q hq, capRB3_step6 q hq, capRB3_step7 q hq, capRB3_step8 q hq, capRB3_step9 q hq, capRB3_step10 q hq, capRB3_step11 q hq]

/-- Proton left: `W_A 3 3 = 1`. -/
theorem capL_WA33 (q : R) (hq : q ≠ 0) : wordA q capL 3 3 = 1 := by
  rw [entry_eq_mulVec_single (wordA q capL) 3 3, capLA3_col q hq]; simp [capLA3_v11]

/-- Proton left: `W_B 0 0 = (q⁸ − q² + 1)/q⁶`. -/
theorem capL_WB00 (q : R) (hq : q ≠ 0) : wordB q capL 0 0 = (q ^ 8 - q ^ 2 + 1) / q ^ 6 := by
  rw [entry_eq_mulVec_single (wordB q capL) 0 0, capLB0_col q hq]; simp [capLB0_v11]

/-- **Proton left: `S = −(q² − 1)²(q⁴ + q² + 1)/q⁶ = −h²[3]_q/q²`.** -/
theorem capL_S (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    FplusL (wordB q capL) + FminusL (wordA q capL)
      = -((q ^ 2 - 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) / q ^ 6 := by
  rw [S_eq_entry_diff q hq h3, capL_WA33 q hq, capL_WB00 q hq]
  field_simp; ring

/-- `S` in terms of `h = q − q⁻¹` and `[3]_q = q² + 1 + q⁻²`. -/
theorem capL_S_h (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    FplusL (wordB q capL) + FminusL (wordA q capL)
      = -((q - q⁻¹) ^ 2 * (q ^ 2 + 1 + q⁻¹ ^ 2)) / q ^ 2 := by
  rw [capL_S q hq h3]; field_simp

/-- **`F(O₊; W_L) = −P(q)/q¹⁰`**, `P = q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1`. -/
theorem capL_Fplus (q : R) (hq : q ≠ 0) :
    FplusL (wordB q capL)
      = -(q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 10 := by
  simp only [FplusL]
  rw [entry_eq_mulVec_single (wordB q capL) 1 1, entry_eq_mulVec_single (wordB q capL) 2 2,
    entry_eq_mulVec_single (wordB q capL) 3 3, capLB1_col q hq, capLB2_col q hq, capLB3_col q hq]
  simp [capLB1_v11, capLB2_v11, capLB3_v11]
  field_simp; ring

/-- **Placement mirror, proton right: `S = +(q² − 1)²(q⁴ + q² + 1)/q⁶`.** -/
theorem capR_S (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    (wordB q capR 0 0 + wordB q capR 1 1 + wordB q capR 2 2)
      - (wordA q capR 1 1 + wordA q capR 2 2 + wordA q capR 3 3)
      = (q ^ 2 - 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) / q ^ 6 := by
  rw [S_eq_entry_diff_right q hq h3, entry_eq_mulVec_single (wordA q capR) 0 0,
    entry_eq_mulVec_single (wordB q capR) 3 3, capRA0_col q hq, capRB3_col q hq]
  simp [capRA0_v11, capRB3_v11]
  field_simp; ring

/-- **Chirality × placement sign:** the two placements give opposite `S`. -/
theorem capL_S_add_capR_S (q : R) (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    (FplusL (wordB q capL) + FminusL (wordA q capL))
      + ((wordB q capR 0 0 + wordB q capR 1 1 + wordB q capR 2 2)
        - (wordA q capR 1 1 + wordA q capR 2 2 + wordA q capR 3 3)) = 0 := by
  rw [capL_S q hq h3, capR_S q hq h3]; ring

end QOU.BraidsAndKnots.HydrogenCaptureWeightSpace
