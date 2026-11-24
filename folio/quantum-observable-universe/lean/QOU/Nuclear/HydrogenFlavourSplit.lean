import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination

/-!
# Ruled flavour split on the four-strand hydrogen element: left placement keeps `q⁻²`

Level-2 Jimbo braiding `Ř` on `(C²)^{⊗4}` (`Ř e₀₀ = q e₀₀`, `Ř e₀₁ = e₁₀`,
`Ř e₁₀ = e₀₁ + h e₁₀`, `Ř e₁₁ = q e₁₁`, `h = q − q⁻¹`; bit `0` is the `K = q` vector, the
up strand). `Ř` keeps the number `z` of zeros, so a braid word is block diagonal; this file
uses the blocks `z = 1, 2, 3` (`blk z`, basis = the bit strings with `z` zeros in
lexicographic order). Inverse letters are `σ − h` (Hecke relation).

**The ruled functional** (`FlavourWeightSplit`, `NeutronHeavierSign`):
`E_c(W) = Tr(K^{⊗4} Π_c W)/[2]⁴`, `K = diag(q, q⁻¹)`. With the nucleon on strands `0–2`,
`Π_p` keeps states with two zeros there and `Π_n` states with one. `tp`, `tn` below are
`[2]⁴ · E_p`, `[2]⁴ · E_n`, written out on the blocks (weight `q^{2z−4}`); the blocks
`z = 0, 4` do not meet either sector.

**Elements** (product in list order, as in
`computations/probes/np_splitting/np_hydrogen_flavour_split_probe.py`):
* `wL = (σ₀σ₁⁻¹)³ · (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹` — the γγ core with the electron capture on strand 3;
* `wAL = (σ₀σ₁⁻¹)³ · σ₂⁻²` — the adjacent capture;
* `wR = (σ₂σ₁⁻¹)³ · (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹` — the strand reflection of `wL`, nucleon on strands `1–3`.

**Results (generic field, `q ≠ 0`, `q² + 1 ≠ 0`).**
* `left_ratio`: for **every** four-strand braid word, with the nucleon on strands `0–2`,
  `tn = q⁻² · tp`, the same ratio as on the bare core `V³` (`FlavourWeightSplit`). Proof: two
  explicit intertwiners `P32 : blk 3 → blk 2`, `P21 : blk 2 → blk 1` commute with every letter,
  and the functional `tn − q⁻²tp` is `Σ_z tr(M_z W_z)` with `M = (P21N21, P32N32 − N21P21,
  −N32P32)`, which cancels by cyclicity. So the electron strand on the right never changes the
  ratio, whatever the capture word.
* Closed forms `wL_tp`, `wAL_tp`, and `wL_eps` for the ruled split `ε = (tp − tn)/[2]⁴`.
* Right placement (nucleon on `1–3`): the ratio fails for the mirrored capture `wR`, with an
  explicit defect of order `h²` (`wR_defect`).

This is exact algebra; no numerical value enters. Which placement is the hydrogen element is
not derived here (audit `2026-11-21-neutron-heavier-sign.md` §20).
-/

namespace QOU.QBeta.HydrogenFlavourSplit

open Matrix

variable {R : Type*} [Field R]

set_option linter.unusedVariables false

/-- A letter: strand index and `true` for an inverse crossing. -/
abbrev Letter := Fin 3 × Bool

def g1_0 (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![(0), (1), (0), (0); (1), ((q^2 - 1) / (q)), (0), (0); (0), (0), (q), (0); (0), (0), (0), (q)]

def g1_0i (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((1 - q^2) / (q)), (1), (0), (0); (1), (0), (0), (0); (0), (0), ((1) / (q)), (0); (0), (0), (0), ((1) / (q))]

def g1_1 (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![(q), (0), (0), (0); (0), (0), (1), (0); (0), (1), ((q^2 - 1) / (q)), (0); (0), (0), (0), (q)]

def g1_1i (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((1) / (q)), (0), (0), (0); (0), ((1 - q^2) / (q)), (1), (0); (0), (1), (0), (0); (0), (0), (0), ((1) / (q))]

def g1_2 (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![(q), (0), (0), (0); (0), (q), (0), (0); (0), (0), (0), (1); (0), (0), (1), ((q^2 - 1) / (q))]

def g1_2i (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((1) / (q)), (0), (0), (0); (0), ((1) / (q)), (0), (0); (0), (0), ((1 - q^2) / (q)), (1); (0), (0), (1), (0)]

def gl1 (q : R) : Letter → Matrix (Fin 4) (Fin 4) R
  | (0, false) => g1_0 q | (1, false) => g1_1 q | (2, false) => g1_2 q
  | (0, true) => g1_0i q | (1, true) => g1_1i q | (2, true) => g1_2i q

/-- A braid word on block `z = 1` (product in list order). -/
def word1 (q : R) : List Letter → Matrix (Fin 4) (Fin 4) R
  | [] => 1
  | l :: w => gl1 q l * word1 q w

theorem word1_mulVec_cons (q : R) (l : Letter) (w : List Letter) (v : Fin 4 → R) :
    (word1 q (l :: w)).mulVec v = (gl1 q l).mulVec ((word1 q w).mulVec v) := by
  simp [word1, Matrix.mulVec_mulVec]

theorem word1_nil (q : R) : word1 q [] = 1 := rfl

def g2_0 (q : R) : Matrix (Fin 6) (Fin 6) R :=
  !![(q), (0), (0), (0), (0), (0); (0), (0), (0), (1), (0), (0); (0), (0), (0), (0), (1), (0); (0), (1), (0), ((q^2 - 1) / (q)), (0), (0); (0), (0), (1), (0), ((q^2 - 1) / (q)), (0); (0), (0), (0), (0), (0), (q)]

def g2_0i (q : R) : Matrix (Fin 6) (Fin 6) R :=
  !![((1) / (q)), (0), (0), (0), (0), (0); (0), ((1 - q^2) / (q)), (0), (1), (0), (0); (0), (0), ((1 - q^2) / (q)), (0), (1), (0); (0), (1), (0), (0), (0), (0); (0), (0), (1), (0), (0), (0); (0), (0), (0), (0), (0), ((1) / (q))]

def g2_1 (q : R) : Matrix (Fin 6) (Fin 6) R :=
  !![(0), (1), (0), (0), (0), (0); (1), ((q^2 - 1) / (q)), (0), (0), (0), (0); (0), (0), (q), (0), (0), (0); (0), (0), (0), (q), (0), (0); (0), (0), (0), (0), (0), (1); (0), (0), (0), (0), (1), ((q^2 - 1) / (q))]

def g2_1i (q : R) : Matrix (Fin 6) (Fin 6) R :=
  !![((1 - q^2) / (q)), (1), (0), (0), (0), (0); (1), (0), (0), (0), (0), (0); (0), (0), ((1) / (q)), (0), (0), (0); (0), (0), (0), ((1) / (q)), (0), (0); (0), (0), (0), (0), ((1 - q^2) / (q)), (1); (0), (0), (0), (0), (1), (0)]

def g2_2 (q : R) : Matrix (Fin 6) (Fin 6) R :=
  !![(q), (0), (0), (0), (0), (0); (0), (0), (1), (0), (0), (0); (0), (1), ((q^2 - 1) / (q)), (0), (0), (0); (0), (0), (0), (0), (1), (0); (0), (0), (0), (1), ((q^2 - 1) / (q)), (0); (0), (0), (0), (0), (0), (q)]

def g2_2i (q : R) : Matrix (Fin 6) (Fin 6) R :=
  !![((1) / (q)), (0), (0), (0), (0), (0); (0), ((1 - q^2) / (q)), (1), (0), (0), (0); (0), (1), (0), (0), (0), (0); (0), (0), (0), ((1 - q^2) / (q)), (1), (0); (0), (0), (0), (1), (0), (0); (0), (0), (0), (0), (0), ((1) / (q))]

def gl2 (q : R) : Letter → Matrix (Fin 6) (Fin 6) R
  | (0, false) => g2_0 q | (1, false) => g2_1 q | (2, false) => g2_2 q
  | (0, true) => g2_0i q | (1, true) => g2_1i q | (2, true) => g2_2i q

/-- A braid word on block `z = 2` (product in list order). -/
def word2 (q : R) : List Letter → Matrix (Fin 6) (Fin 6) R
  | [] => 1
  | l :: w => gl2 q l * word2 q w

theorem word2_mulVec_cons (q : R) (l : Letter) (w : List Letter) (v : Fin 6 → R) :
    (word2 q (l :: w)).mulVec v = (gl2 q l).mulVec ((word2 q w).mulVec v) := by
  simp [word2, Matrix.mulVec_mulVec]

theorem word2_nil (q : R) : word2 q [] = 1 := rfl

def g3_0 (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![(q), (0), (0), (0); (0), (q), (0), (0); (0), (0), (0), (1); (0), (0), (1), ((q^2 - 1) / (q))]

def g3_0i (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((1) / (q)), (0), (0), (0); (0), ((1) / (q)), (0), (0); (0), (0), ((1 - q^2) / (q)), (1); (0), (0), (1), (0)]

def g3_1 (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![(q), (0), (0), (0); (0), (0), (1), (0); (0), (1), ((q^2 - 1) / (q)), (0); (0), (0), (0), (q)]

def g3_1i (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((1) / (q)), (0), (0), (0); (0), ((1 - q^2) / (q)), (1), (0); (0), (1), (0), (0); (0), (0), (0), ((1) / (q))]

def g3_2 (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![(0), (1), (0), (0); (1), ((q^2 - 1) / (q)), (0), (0); (0), (0), (q), (0); (0), (0), (0), (q)]

def g3_2i (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((1 - q^2) / (q)), (1), (0), (0); (1), (0), (0), (0); (0), (0), ((1) / (q)), (0); (0), (0), (0), ((1) / (q))]

def gl3 (q : R) : Letter → Matrix (Fin 4) (Fin 4) R
  | (0, false) => g3_0 q | (1, false) => g3_1 q | (2, false) => g3_2 q
  | (0, true) => g3_0i q | (1, true) => g3_1i q | (2, true) => g3_2i q

/-- A braid word on block `z = 3` (product in list order). -/
def word3 (q : R) : List Letter → Matrix (Fin 4) (Fin 4) R
  | [] => 1
  | l :: w => gl3 q l * word3 q w

theorem word3_mulVec_cons (q : R) (l : Letter) (w : List Letter) (v : Fin 4 → R) :
    (word3 q (l :: w)).mulVec v = (gl3 q l).mulVec ((word3 q w).mulVec v) := by
  simp [word3, Matrix.mulVec_mulVec]

theorem word3_nil (q : R) : word3 q [] = 1 := rfl

theorem entry_eq_mulVec_single {n : ℕ} (M : Matrix (Fin n) (Fin n) R) (i j : Fin n) :
    M i j = (M.mulVec (Pi.single j 1)) i := by
  simp [Matrix.mulVec, dotProduct, Pi.single_apply]

set_option hygiene false in
macro "stepTac" : tactic => `(tactic| (ext i; fin_cases i <;>
  simp [g1_0, g1_0i, g1_1, g1_1i, g1_2, g1_2i, g2_0, g2_0i, g2_1, g2_1i, g2_2, g2_2i, g3_0, g3_0i, g3_1, g3_1i, g3_2, g3_2i, Matrix.mulVec, dotProduct,
    Fin.sum_univ_four, Fin.sum_univ_six, Pi.single_apply] <;> (try field_simp) <;> (try ring)))

def wL : List Letter :=
  [(0, false), (1, true), (0, false), (1, true), (0, false), (1, true), (2, true), (1, true), (0, true), (0, true), (1, true), (2, true)]

def wAL : List Letter :=
  [(0, false), (1, true), (0, false), (1, true), (0, false), (1, true), (2, true), (2, true)]

def wR : List Letter :=
  [(2, false), (1, true), (2, false), (1, true), (2, false), (1, true), (0, true), (1, true), (2, true), (2, true), (1, true), (0, true)]

/-- `[2]⁴ · E_p` with the nucleon on strands 0–2, on blocks `z = 1, 2, 3`. -/
def tpL (q : R) (W1 W3 : Matrix (Fin 4) (Fin 4) R) (W2 : Matrix (Fin 6) (Fin 6) R) : R :=
  (1) * W2 0 0 + (1) * W2 1 1 + (1) * W2 3 3 + (q^2) * W3 1 1 + (q^2) * W3 2 2 + (q^2) * W3 3 3

/-- `[2]⁴ · E_n` with the nucleon on strands 0–2, on blocks `z = 1, 2, 3`. -/
def tnL (q : R) (W1 W3 : Matrix (Fin 4) (Fin 4) R) (W2 : Matrix (Fin 6) (Fin 6) R) : R :=
  ((1) / (q^2)) * W1 0 0 + ((1) / (q^2)) * W1 1 1 + ((1) / (q^2)) * W1 2 2 + (1) * W2 2 2 + (1) * W2 4 4 + (1) * W2 5 5

/-- `[2]⁴ · E_p` with the nucleon on strands 1–3, on blocks `z = 1, 2, 3`. -/
def tpR (q : R) (W1 W3 : Matrix (Fin 4) (Fin 4) R) (W2 : Matrix (Fin 6) (Fin 6) R) : R :=
  (1) * W2 3 3 + (1) * W2 4 4 + (1) * W2 5 5 + (q^2) * W3 0 0 + (q^2) * W3 1 1 + (q^2) * W3 2 2

/-- `[2]⁴ · E_n` with the nucleon on strands 1–3, on blocks `z = 1, 2, 3`. -/
def tnR (q : R) (W1 W3 : Matrix (Fin 4) (Fin 4) R) (W2 : Matrix (Fin 6) (Fin 6) R) : R :=
  ((1) / (q^2)) * W1 1 1 + ((1) / (q^2)) * W1 2 2 + ((1) / (q^2)) * W1 3 3 + (1) * W2 0 0 + (1) * W2 1 1 + (1) * W2 2 2

/-! ### Intertwiners and the universal left ratio -/

def P32 (q : R) : Matrix (Fin 6) (Fin 4) R :=
  !![((1) / (q^3)), ((1) / (q^2)), (0), (0); ((1) / (q^2)), (0), ((1) / (q^2)), (0); (0), ((1) / (q^2)), ((1) / (q)), (0); ((1) / (q)), (0), (0), ((1) / (q^2)); (0), ((1) / (q)), (0), ((1) / (q)); (0), (0), ((1) / (q)), (1)]

def P21 (q : R) : Matrix (Fin 4) (Fin 6) R :=
  !![((1) / (q^3)), ((1) / (q^2)), ((1) / (q)), (0), (0), (0); ((1) / (q^2)), (0), (0), ((1) / (q^2)), ((1) / (q)), (0); (0), ((1) / (q^2)), (0), ((1) / (q)), (0), ((1) / (q)); (0), (0), ((1) / (q^2)), (0), ((1) / (q)), (1)]

def N32 (q : R) : Matrix (Fin 4) (Fin 6) R :=
  !![(0), (0), (0), (0), (0), (0); (0), (0), ((q^2) / (q^2 + 1)), (0), ((q^3) / (q^2 + 1)), ((-q^2) / (q^2 + 1)); (0), (0), ((q^3) / (q^2 + 1)), (0), ((-q^2) / (q^2 + 1)), ((q) / (q^2 + 1)); (0), (0), ((-q^2) / (q^2 + 1)), (0), ((q) / (q^2 + 1)), ((q^2) / (q^2 + 1))]

def N21 (q : R) : Matrix (Fin 6) (Fin 4) R :=
  !![((q) / (q^2 + 1)), ((q^2) / (q^2 + 1)), ((-q) / (q^2 + 1)), (0); ((q^2) / (q^2 + 1)), ((-q) / (q^2 + 1)), ((1) / (q^2 + 1)), (0); (0), (0), (0), (0); ((-q) / (q^2 + 1)), ((1) / (q^2 + 1)), ((q) / (q^2 + 1)), (0); (0), (0), (0), (0); (0), (0), (0), (0)]

def M1 (q : R) : Matrix (Fin 4) (Fin 4) R :=
  Matrix.diagonal ![((1) / (q^2)), ((1) / (q^2)), ((1) / (q^2)), (0)]

def M2 (q : R) : Matrix (Fin 6) (Fin 6) R :=
  Matrix.diagonal ![((-1) / (q^2)), ((-1) / (q^2)), (1), ((-1) / (q^2)), (1), (1)]

def M3 (q : R) : Matrix (Fin 4) (Fin 4) R :=
  Matrix.diagonal ![(0), (-1), (-1), (-1)]

set_option hygiene false in
macro "matTac" : tactic => `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
  simp [g1_0, g1_0i, g1_1, g1_1i, g1_2, g1_2i, g2_0, g2_0i, g2_1, g2_1i, g2_2, g2_2i, g3_0, g3_0i, g3_1, g3_1i, g3_2, g3_2i, P32, P21, N32, N21, M1, M2, M3, Matrix.mul_apply, Matrix.diagonal,
    Fin.sum_univ_four, Fin.sum_univ_six, Matrix.one_apply] <;> (try field_simp) <;> (try ring)))

theorem P32_g0 (q : R) (hq : q ≠ 0) : P32 q * g3_0 q = g2_0 q * P32 q := by matTac

theorem P32_g0i (q : R) (hq : q ≠ 0) : P32 q * g3_0i q = g2_0i q * P32 q := by matTac

theorem P32_g1 (q : R) (hq : q ≠ 0) : P32 q * g3_1 q = g2_1 q * P32 q := by matTac

theorem P32_g1i (q : R) (hq : q ≠ 0) : P32 q * g3_1i q = g2_1i q * P32 q := by matTac

theorem P32_g2 (q : R) (hq : q ≠ 0) : P32 q * g3_2 q = g2_2 q * P32 q := by matTac

theorem P32_g2i (q : R) (hq : q ≠ 0) : P32 q * g3_2i q = g2_2i q * P32 q := by matTac


theorem P32_letter (q : R) (hq : q ≠ 0) (l : Letter) : P32 q * gl3 q l = gl2 q l * P32 q := by
  obtain ⟨i, b⟩ := l
  fin_cases i <;> cases b <;> simp only [gl3, gl2] <;>
    first
    | exact P32_g0 q hq | exact P32_g1 q hq | exact P32_g2 q hq
    | exact P32_g0i q hq | exact P32_g1i q hq | exact P32_g2i q hq

theorem P32_word (q : R) (hq : q ≠ 0) (w : List Letter) :
    P32 q * word3 q w = word2 q w * P32 q := by
  induction w with
  | nil => simp [word3, word2]
  | cons l w ih =>
    simp only [word3, word2]
    rw [← Matrix.mul_assoc, P32_letter q hq l, Matrix.mul_assoc, ih, Matrix.mul_assoc]

theorem P21_g0 (q : R) (hq : q ≠ 0) : P21 q * g2_0 q = g1_0 q * P21 q := by matTac

theorem P21_g0i (q : R) (hq : q ≠ 0) : P21 q * g2_0i q = g1_0i q * P21 q := by matTac

theorem P21_g1 (q : R) (hq : q ≠ 0) : P21 q * g2_1 q = g1_1 q * P21 q := by matTac

theorem P21_g1i (q : R) (hq : q ≠ 0) : P21 q * g2_1i q = g1_1i q * P21 q := by matTac

theorem P21_g2 (q : R) (hq : q ≠ 0) : P21 q * g2_2 q = g1_2 q * P21 q := by matTac

theorem P21_g2i (q : R) (hq : q ≠ 0) : P21 q * g2_2i q = g1_2i q * P21 q := by matTac


theorem P21_letter (q : R) (hq : q ≠ 0) (l : Letter) : P21 q * gl2 q l = gl1 q l * P21 q := by
  obtain ⟨i, b⟩ := l
  fin_cases i <;> cases b <;> simp only [gl2, gl1] <;>
    first
    | exact P21_g0 q hq | exact P21_g1 q hq | exact P21_g2 q hq
    | exact P21_g0i q hq | exact P21_g1i q hq | exact P21_g2i q hq

theorem P21_word (q : R) (hq : q ≠ 0) (w : List Letter) :
    P21 q * word2 q w = word1 q w * P21 q := by
  induction w with
  | nil => simp [word2, word1]
  | cons l w ih =>
    simp only [word2, word1]
    rw [← Matrix.mul_assoc, P21_letter q hq l, Matrix.mul_assoc, ih, Matrix.mul_assoc]


set_option maxHeartbeats 4000000 in
theorem M1_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : M1 q = P21 q * N21 q := by matTac
set_option maxHeartbeats 4000000 in
theorem M2_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    M2 q = P32 q * N32 q - N21 q * P21 q := by matTac
set_option maxHeartbeats 4000000 in
theorem M3_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : M3 q = -(N32 q * P32 q) := by matTac

/-- `tn − q⁻² tp` is a sum of weighted block traces. -/
theorem phi_eq_traces (q : R) (hq : q ≠ 0) (W1 W3 : Matrix (Fin 4) (Fin 4) R)
    (W2 : Matrix (Fin 6) (Fin 6) R) :
    tnL q W1 W3 W2 - q⁻¹ ^ 2 * tpL q W1 W3 W2
      = trace (M1 q * W1) + trace (M2 q * W2) + trace (M3 q * W3) := by
  simp only [tnL, tpL, M1, M2, M3, Matrix.trace, Matrix.diag, Matrix.diagonal_mul,
    Fin.sum_univ_four, Fin.sum_univ_six]
  simp
  field_simp
  ring

/-- **Left placement keeps the ratio, for every word.** With the nucleon on strands `0–2`
and the ruled functional, `E_n = q⁻² · E_p` for every braid word on four strands. -/
theorem left_ratio (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (w : List Letter) :
    tnL q (word1 q w) (word3 q w) (word2 q w)
      = q⁻¹ ^ 2 * tpL q (word1 q w) (word3 q w) (word2 q w) := by
  have key := phi_eq_traces q hq (word1 q w) (word3 q w) (word2 q w)
  have i21 := P21_word q hq w
  have i32 := P32_word q hq w
  have t1 : trace (P21 q * N21 q * word1 q w) = trace (N21 q * P21 q * word2 q w) := by
    rw [Matrix.trace_mul_cycle, ← i21, Matrix.trace_mul_cycle]
  have t2 : trace (P32 q * N32 q * word2 q w) = trace (N32 q * P32 q * word3 q w) := by
    rw [Matrix.trace_mul_cycle, ← i32, Matrix.trace_mul_cycle]
  rw [M1_eq q hq h2, M2_eq q hq h2, M3_eq q hq h2, Matrix.sub_mul, Matrix.trace_sub,
    Matrix.neg_mul, Matrix.trace_neg, t1, t2] at key
  linear_combination key

@[simp] def wL_2_0_v0 (q : R) : Fin 6 → R := ![((1) / (q)), (0), (0), (0), (0), (0)]

theorem wL_2_0_s0 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (Pi.single 0 1) = wL_2_0_v0 q := by
  stepTac

@[simp] def wL_2_0_v1 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^2)), ((1) / (q)), (0), (0), (0), (0)]

theorem wL_2_0_s1 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_0_v0 q) = wL_2_0_v1 q := by
  stepTac

@[simp] def wL_2_0_v2 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^3)), ((1 - q^2) / (q^2)), (0), ((1) / (q)), (0), (0)]

theorem wL_2_0_s2 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wL_2_0_v1 q) = wL_2_0_v2 q := by
  stepTac

@[simp] def wL_2_0_v3 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^4)), ((q^4 - q^2 + 1) / (q^3)), (0), ((1 - q^2) / (q^2)), (0), (0)]

theorem wL_2_0_s3 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wL_2_0_v2 q) = wL_2_0_v3 q := by
  stepTac

@[simp] def wL_2_0_v4 (q : R) : Fin 6 → R := ![((q^6 - q^2 + 1) / (q^5)), ((1 - q^2) / (q^4)), (0), ((1 - q^2) / (q^3)), (0), (0)]

theorem wL_2_0_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_0_v3 q) = wL_2_0_v4 q := by
  stepTac

@[simp] def wL_2_0_v5 (q : R) : Fin 6 → R := ![((q^6 - q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((1 - q^2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), (0)]

theorem wL_2_0_s5 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wL_2_0_v4 q) = wL_2_0_v5 q := by
  stepTac

@[simp] def wL_2_0_v6 (q : R) : Fin 6 → R := ![((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^7)), ((q^6 - q^2 + 1) / (q^6)), ((1 - q^2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3))]

theorem wL_2_0_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_0_v5 q) = wL_2_0_v6 q := by
  stepTac

@[simp] def wL_2_0_v7 (q : R) : Fin 6 → R := ![((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((q^4 - 3*q^2 + 2) / (q^3)), ((1 - q^2) / (q^2))]

theorem wL_2_0_s7 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wL_2_0_v6 q) = wL_2_0_v7 q := by
  stepTac

@[simp] def wL_2_0_v8 (q : R) : Fin 6 → R := ![((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^7)), ((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((2*q^4 - 3*q^2 + 2) / (q^5)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^4)), ((q^4 - 3*q^2 + 2) / (q^3))]

theorem wL_2_0_s8 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_0_v7 q) = wL_2_0_v8 q := by
  stepTac

@[simp] def wL_2_0_v9 (q : R) : Fin 6 → R := ![((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^6)), ((2*q^4 - 3*q^2 + 2) / (q^5)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^4)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^6)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^5)), ((q^4 - 3*q^2 + 2) / (q^2))]

theorem wL_2_0_s9 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wL_2_0_v8 q) = wL_2_0_v9 q := by
  stepTac

@[simp] def wL_2_0_v10 (q : R) : Fin 6 → R := ![((-q^12 + 4*q^10 - 7*q^8 + 8*q^6 - 4*q^4 + 1) / (q^7)), ((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^6)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^5)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^7)), ((q^10 - 4*q^8 + 7*q^6 - 8*q^4 + 5*q^2 - 1) / (q^6)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^5))]

theorem wL_2_0_s10 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_0_v9 q) = wL_2_0_v10 q := by
  stepTac

@[simp] def wL_2_0_v11 (q : R) : Fin 6 → R := ![((-q^12 + 4*q^10 - 7*q^8 + 8*q^6 - 4*q^4 + 1) / (q^6)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^7)), ((q^10 - 4*q^8 + 7*q^6 - 8*q^4 + 5*q^2 - 1) / (q^6)), ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 9*q^4 - 4*q^2 + 1) / (q^8)), ((q^12 - 5*q^10 + 10*q^8 - 12*q^6 + 9*q^4 - 4*q^2 + 1) / (q^7)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^4))]

theorem wL_2_0_s11 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wL_2_0_v10 q) = wL_2_0_v11 q := by
  stepTac

theorem wL_2_0_entry (q : R) (hq : q ≠ 0) :
    word2 q wL 0 0 = ((-q^12 + 4*q^10 - 7*q^8 + 8*q^6 - 4*q^4 + 1) / (q^6)) := by
  rw [entry_eq_mulVec_single (word2 q wL) 0 0]
  simp only [wL, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wL_2_0_s0 q hq, wL_2_0_s1 q hq, wL_2_0_s2 q hq, wL_2_0_s3 q hq, wL_2_0_s4 q hq, wL_2_0_s5 q hq, wL_2_0_s6 q hq, wL_2_0_s7 q hq, wL_2_0_s8 q hq, wL_2_0_s9 q hq, wL_2_0_s10 q hq, wL_2_0_s11 q hq]
  simp [wL_2_0_v11]

@[simp] def wL_2_1_v0 (q : R) : Fin 6 → R := ![(0), ((1 - q^2) / (q)), (1), (0), (0), (0)]

theorem wL_2_1_s0 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (Pi.single 1 1) = wL_2_1_v0 q := by
  stepTac

@[simp] def wL_2_1_v1 (q : R) : Fin 6 → R := ![((1 - q^2) / (q)), (0), ((1) / (q)), (0), (0), (0)]

theorem wL_2_1_s1 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_1_v0 q) = wL_2_1_v1 q := by
  stepTac

@[simp] def wL_2_1_v2 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^2)), (0), ((1 - q^2) / (q^2)), (0), ((1) / (q)), (0)]

theorem wL_2_1_s2 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wL_2_1_v1 q) = wL_2_1_v2 q := by
  stepTac

@[simp] def wL_2_1_v3 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^3)), (0), ((q^4 - q^2 + 1) / (q^3)), (0), ((1 - q^2) / (q^2)), (0)]

theorem wL_2_1_s3 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wL_2_1_v2 q) = wL_2_1_v3 q := by
  stepTac

@[simp] def wL_2_1_v4 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), ((q^4 - q^2 + 1) / (q^4)), (0), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2))]

theorem wL_2_1_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_1_v3 q) = wL_2_1_v4 q := by
  stepTac

@[simp] def wL_2_1_v5 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^5)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((1 - q^2) / (q^3)), ((q^4 - 2*q^2 + 1) / (q^3)), (0), ((1 - q^2) / (q^3))]

theorem wL_2_1_s5 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wL_2_1_v4 q) = wL_2_1_v5 q := by
  stepTac

@[simp] def wL_2_1_v6 (q : R) : Fin 6 → R := ![((q^6 - q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((1 - q^2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), (0)]

theorem wL_2_1_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_1_v5 q) = wL_2_1_v6 q := by
  stepTac

@[simp] def wL_2_1_v7 (q : R) : Fin 6 → R := ![((q^6 - q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2)), (0)]

theorem wL_2_1_s7 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wL_2_1_v6 q) = wL_2_1_v7 q := by
  stepTac

@[simp] def wL_2_1_v8 (q : R) : Fin 6 → R := ![((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^6)), ((q^6 - q^2 + 1) / (q^5)), ((1 - q^2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2))]

theorem wL_2_1_s8 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_1_v7 q) = wL_2_1_v8 q := by
  stepTac

@[simp] def wL_2_1_v9 (q : R) : Fin 6 → R := ![((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((2*q^4 - 3*q^2 + 2) / (q^3)), ((q^4 - 3*q^2 + 2) / (q^2)), ((1 - q^2) / (q))]

theorem wL_2_1_s9 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wL_2_1_v8 q) = wL_2_1_v9 q := by
  stepTac

@[simp] def wL_2_1_v10 (q : R) : Fin 6 → R := ![((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^6)), ((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^3)), ((q^4 - 3*q^2 + 2) / (q^2))]

theorem wL_2_1_s10 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_1_v9 q) = wL_2_1_v10 q := by
  stepTac

@[simp] def wL_2_1_v11 (q : R) : Fin 6 → R := ![((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^5)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^3)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^5)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^4)), ((q^4 - 3*q^2 + 2) / (q))]

theorem wL_2_1_s11 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wL_2_1_v10 q) = wL_2_1_v11 q := by
  stepTac

theorem wL_2_1_entry (q : R) (hq : q ≠ 0) :
    word2 q wL 1 1 = ((2*q^4 - 3*q^2 + 2) / (q^4)) := by
  rw [entry_eq_mulVec_single (word2 q wL) 1 1]
  simp only [wL, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wL_2_1_s0 q hq, wL_2_1_s1 q hq, wL_2_1_s2 q hq, wL_2_1_s3 q hq, wL_2_1_s4 q hq, wL_2_1_s5 q hq, wL_2_1_s6 q hq, wL_2_1_s7 q hq, wL_2_1_s8 q hq, wL_2_1_s9 q hq, wL_2_1_s10 q hq, wL_2_1_s11 q hq]
  simp [wL_2_1_v11]

@[simp] def wL_2_3_v0 (q : R) : Fin 6 → R := ![(0), (0), (0), ((1 - q^2) / (q)), (1), (0)]

theorem wL_2_3_s0 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (Pi.single 3 1) = wL_2_3_v0 q := by
  stepTac

@[simp] def wL_2_3_v1 (q : R) : Fin 6 → R := ![(0), (0), (0), ((1 - q^2) / (q^2)), ((1 - q^2) / (q)), (1)]

theorem wL_2_3_s1 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_3_v0 q) = wL_2_3_v1 q := by
  stepTac

@[simp] def wL_2_3_v2 (q : R) : Fin 6 → R := ![(0), ((1 - q^2) / (q^2)), ((1 - q^2) / (q)), (0), (0), ((1) / (q))]

theorem wL_2_3_s2 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wL_2_3_v1 q) = wL_2_3_v2 q := by
  stepTac

@[simp] def wL_2_3_v3 (q : R) : Fin 6 → R := ![(0), ((q^4 - 2*q^2 + 1) / (q^3)), ((q^4 - 2*q^2 + 1) / (q^2)), ((1 - q^2) / (q^2)), ((1 - q^2) / (q)), ((1) / (q^2))]

theorem wL_2_3_s3 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wL_2_3_v2 q) = wL_2_3_v3 q := by
  stepTac

@[simp] def wL_2_3_v4 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^3)), (0), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^3)), ((q^4 - 2*q^2 + 2) / (q^2)), ((1 - q^2) / (q))]

theorem wL_2_3_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_3_v3 q) = wL_2_3_v4 q := by
  stepTac

@[simp] def wL_2_3_v5 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), (0), ((q^6 - q^4 + 1) / (q^4)), ((1 - q^2) / (q^3)), ((1 - q^2) / (q^2))]

theorem wL_2_3_s5 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wL_2_3_v4 q) = wL_2_3_v5 q := by
  stepTac

@[simp] def wL_2_3_v6 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), (0), ((q^6 - q^4 + 1) / (q^5)), ((1 - q^2) / (q^4)), ((1 - q^2) / (q^3))]

theorem wL_2_3_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_3_v5 q) = wL_2_3_v6 q := by
  stepTac

@[simp] def wL_2_3_v7 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((q^6 - q^4 + 1) / (q^5)), ((1 - q^2) / (q^4)), ((q^8 - q^6 - q^4 + 2*q^2 - 1) / (q^6)), ((-q^4 + 2*q^2 - 1) / (q^5)), ((1 - q^2) / (q^2))]

theorem wL_2_3_s7 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wL_2_3_v6 q) = wL_2_3_v7 q := by
  stepTac

@[simp] def wL_2_3_v8 (q : R) : Fin 6 → R := ![((2*q^4 - 3*q^2 + 2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^5)), ((q^8 - q^6 - q^4 + 2*q^2 - 1) / (q^7)), ((-2*q^4 + 3*q^2 - 1) / (q^6)), ((-q^4 + 2*q^2 - 1) / (q^5))]

theorem wL_2_3_s8 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_3_v7 q) = wL_2_3_v8 q := by
  stepTac

@[simp] def wL_2_3_v9 (q : R) : Fin 6 → R := ![((2*q^4 - 3*q^2 + 2) / (q^4)), ((q^8 - q^6 - q^4 + 2*q^2 - 1) / (q^7)), ((-2*q^4 + 3*q^2 - 1) / (q^6)), ((q^10 - q^8 - 2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^8)), ((-2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^7)), ((-q^4 + 2*q^2 - 1) / (q^4))]

theorem wL_2_3_s9 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wL_2_3_v8 q) = wL_2_3_v9 q := by
  stepTac

@[simp] def wL_2_3_v10 (q : R) : Fin 6 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^7)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((-2*q^4 + 3*q^2 - 1) / (q^7)), ((q^10 - q^8 - 2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^9)), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / (q^8)), ((-2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^7))]

theorem wL_2_3_s10 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wL_2_3_v9 q) = wL_2_3_v10 q := by
  stepTac

@[simp] def wL_2_3_v11 (q : R) : Fin 6 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^6)), ((q^10 - q^8 - 2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^9)), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / (q^8)), ((q^12 - 4*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^10)), ((q^10 - 5*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^9)), ((-2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6))]

theorem wL_2_3_s11 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wL_2_3_v10 q) = wL_2_3_v11 q := by
  stepTac

theorem wL_2_3_entry (q : R) (hq : q ≠ 0) :
    word2 q wL 3 3 = ((q^12 - 4*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^10)) := by
  rw [entry_eq_mulVec_single (word2 q wL) 3 3]
  simp only [wL, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wL_2_3_s0 q hq, wL_2_3_s1 q hq, wL_2_3_s2 q hq, wL_2_3_s3 q hq, wL_2_3_s4 q hq, wL_2_3_s5 q hq, wL_2_3_s6 q hq, wL_2_3_s7 q hq, wL_2_3_s8 q hq, wL_2_3_s9 q hq, wL_2_3_s10 q hq, wL_2_3_s11 q hq]
  simp [wL_2_3_v11]

@[simp] def wL_3_1_v0 (q : R) : Fin 4 → R := ![(1), (0), (0), (0)]

theorem wL_3_1_s0 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (Pi.single 1 1) = wL_3_1_v0 q := by
  stepTac

@[simp] def wL_3_1_v1 (q : R) : Fin 4 → R := ![((1) / (q)), (0), (0), (0)]

theorem wL_3_1_s1 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_1_v0 q) = wL_3_1_v1 q := by
  stepTac

@[simp] def wL_3_1_v2 (q : R) : Fin 4 → R := ![((1) / (q^2)), (0), (0), (0)]

theorem wL_3_1_s2 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (wL_3_1_v1 q) = wL_3_1_v2 q := by
  stepTac

@[simp] def wL_3_1_v3 (q : R) : Fin 4 → R := ![((1) / (q^3)), (0), (0), (0)]

theorem wL_3_1_s3 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (wL_3_1_v2 q) = wL_3_1_v3 q := by
  stepTac

@[simp] def wL_3_1_v4 (q : R) : Fin 4 → R := ![((1) / (q^4)), (0), (0), (0)]

theorem wL_3_1_s4 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_1_v3 q) = wL_3_1_v4 q := by
  stepTac

@[simp] def wL_3_1_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((1) / (q^4)), (0), (0)]

theorem wL_3_1_s5 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wL_3_1_v4 q) = wL_3_1_v5 q := by
  stepTac

@[simp] def wL_3_1_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^6)), ((1 - q^2) / (q^5)), ((1) / (q^4)), (0)]

theorem wL_3_1_s6 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_1_v5 q) = wL_3_1_v6 q := by
  stepTac

@[simp] def wL_3_1_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((1 - q^2) / (q^4)), (0), ((1) / (q^4))]

theorem wL_3_1_s7 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wL_3_1_v6 q) = wL_3_1_v7 q := by
  stepTac

@[simp] def wL_3_1_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((1 - q^2) / (q^4)), ((1) / (q^5))]

theorem wL_3_1_s8 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_1_v7 q) = wL_3_1_v8 q := by
  stepTac

@[simp] def wL_3_1_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1) / (q^5)), ((-q^4 + 2*q^2 - 1) / (q^6))]

theorem wL_3_1_s9 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wL_3_1_v8 q) = wL_3_1_v9 q := by
  stepTac

@[simp] def wL_3_1_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^6)), ((-q^6 + 3*q^4 - 3*q^2 + 2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^7))]

theorem wL_3_1_s10 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_1_v9 q) = wL_3_1_v10 q := by
  stepTac

@[simp] def wL_3_1_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((-q^6 + 3*q^4 - 3*q^2 + 2) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^7)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^8))]

theorem wL_3_1_s11 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wL_3_1_v10 q) = wL_3_1_v11 q := by
  stepTac

theorem wL_3_1_entry (q : R) (hq : q ≠ 0) :
    word3 q wL 1 1 = ((-q^6 + 3*q^4 - 3*q^2 + 2) / (q^4)) := by
  rw [entry_eq_mulVec_single (word3 q wL) 1 1]
  simp only [wL, word3_mulVec_cons, word3_nil, Matrix.one_mulVec, gl3]
  rw [wL_3_1_s0 q hq, wL_3_1_s1 q hq, wL_3_1_s2 q hq, wL_3_1_s3 q hq, wL_3_1_s4 q hq, wL_3_1_s5 q hq, wL_3_1_s6 q hq, wL_3_1_s7 q hq, wL_3_1_s8 q hq, wL_3_1_s9 q hq, wL_3_1_s10 q hq, wL_3_1_s11 q hq]
  simp [wL_3_1_v11]

@[simp] def wL_3_2_v0 (q : R) : Fin 4 → R := ![(0), (0), ((1) / (q)), (0)]

theorem wL_3_2_s0 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (Pi.single 2 1) = wL_3_2_v0 q := by
  stepTac

@[simp] def wL_3_2_v1 (q : R) : Fin 4 → R := ![(0), ((1) / (q)), (0), (0)]

theorem wL_3_2_s1 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_2_v0 q) = wL_3_2_v1 q := by
  stepTac

@[simp] def wL_3_2_v2 (q : R) : Fin 4 → R := ![(0), ((1) / (q^2)), (0), (0)]

theorem wL_3_2_s2 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (wL_3_2_v1 q) = wL_3_2_v2 q := by
  stepTac

@[simp] def wL_3_2_v3 (q : R) : Fin 4 → R := ![(0), ((1) / (q^3)), (0), (0)]

theorem wL_3_2_s3 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (wL_3_2_v2 q) = wL_3_2_v3 q := by
  stepTac

@[simp] def wL_3_2_v4 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / (q^4)), ((1) / (q^3)), (0)]

theorem wL_3_2_s4 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_2_v3 q) = wL_3_2_v4 q := by
  stepTac

@[simp] def wL_3_2_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), (0), ((1) / (q^4)), (0)]

theorem wL_3_2_s5 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wL_3_2_v4 q) = wL_3_2_v5 q := by
  stepTac

@[simp] def wL_3_2_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((1) / (q^4)), (0), (0)]

theorem wL_3_2_s6 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_2_v5 q) = wL_3_2_v6 q := by
  stepTac

@[simp] def wL_3_2_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((1) / (q^3)), (0), (0)]

theorem wL_3_2_s7 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wL_3_2_v6 q) = wL_3_2_v7 q := by
  stepTac

@[simp] def wL_3_2_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((1 - q^2) / (q^4)), ((1) / (q^3)), (0)]

theorem wL_3_2_s8 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_2_v7 q) = wL_3_2_v8 q := by
  stepTac

@[simp] def wL_3_2_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((1 - q^2) / (q^3)), (0), ((1) / (q^3))]

theorem wL_3_2_s9 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wL_3_2_v8 q) = wL_3_2_v9 q := by
  stepTac

@[simp] def wL_3_2_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), ((1) / (q^4))]

theorem wL_3_2_s10 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_2_v9 q) = wL_3_2_v10 q := by
  stepTac

@[simp] def wL_3_2_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^5))]

theorem wL_3_2_s11 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wL_3_2_v10 q) = wL_3_2_v11 q := by
  stepTac

theorem wL_3_2_entry (q : R) (hq : q ≠ 0) :
    word3 q wL 2 2 = ((1) / (q^4)) := by
  rw [entry_eq_mulVec_single (word3 q wL) 2 2]
  simp only [wL, word3_mulVec_cons, word3_nil, Matrix.one_mulVec, gl3]
  rw [wL_3_2_s0 q hq, wL_3_2_s1 q hq, wL_3_2_s2 q hq, wL_3_2_s3 q hq, wL_3_2_s4 q hq, wL_3_2_s5 q hq, wL_3_2_s6 q hq, wL_3_2_s7 q hq, wL_3_2_s8 q hq, wL_3_2_s9 q hq, wL_3_2_s10 q hq, wL_3_2_s11 q hq]
  simp [wL_3_2_v11]

@[simp] def wL_3_3_v0 (q : R) : Fin 4 → R := ![(0), (0), (0), ((1) / (q))]

theorem wL_3_3_s0 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (Pi.single 3 1) = wL_3_3_v0 q := by
  stepTac

@[simp] def wL_3_3_v1 (q : R) : Fin 4 → R := ![(0), (0), (0), ((1) / (q^2))]

theorem wL_3_3_s1 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_3_v0 q) = wL_3_3_v1 q := by
  stepTac

@[simp] def wL_3_3_v2 (q : R) : Fin 4 → R := ![(0), (0), ((1) / (q^2)), (0)]

theorem wL_3_3_s2 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (wL_3_3_v1 q) = wL_3_3_v2 q := by
  stepTac

@[simp] def wL_3_3_v3 (q : R) : Fin 4 → R := ![(0), (0), ((1 - q^2) / (q^3)), ((1) / (q^2))]

theorem wL_3_3_s3 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (wL_3_3_v2 q) = wL_3_3_v3 q := by
  stepTac

@[simp] def wL_3_3_v4 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / (q^3)), (0), ((1) / (q^3))]

theorem wL_3_3_s4 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_3_v3 q) = wL_3_3_v4 q := by
  stepTac

@[simp] def wL_3_3_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^3)), (0), (0), ((1) / (q^4))]

theorem wL_3_3_s5 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wL_3_3_v4 q) = wL_3_3_v5 q := by
  stepTac

@[simp] def wL_3_3_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), (0), (0), ((1) / (q^5))]

theorem wL_3_3_s6 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_3_v5 q) = wL_3_3_v6 q := by
  stepTac

@[simp] def wL_3_3_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^3)), (0), ((1) / (q^5)), ((q^2 - 1) / (q^6))]

theorem wL_3_3_s7 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wL_3_3_v6 q) = wL_3_3_v7 q := by
  stepTac

@[simp] def wL_3_3_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((1) / (q^5)), (0), ((q^2 - 1) / (q^7))]

theorem wL_3_3_s8 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_3_v7 q) = wL_3_3_v8 q := by
  stepTac

@[simp] def wL_3_3_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^3)), ((1) / (q^4)), ((q^2 - 1) / (q^7)), ((q^4 - 2*q^2 + 1) / (q^8))]

theorem wL_3_3_s9 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wL_3_3_v8 q) = wL_3_3_v9 q := by
  stepTac

@[simp] def wL_3_3_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^7)), ((1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^9))]

theorem wL_3_3_s10 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wL_3_3_v9 q) = wL_3_3_v10 q := by
  stepTac

@[simp] def wL_3_3_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^3)), ((-q^4 + 2*q^2 - 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^9)), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / (q^10))]

theorem wL_3_3_s11 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wL_3_3_v10 q) = wL_3_3_v11 q := by
  stepTac

theorem wL_3_3_entry (q : R) (hq : q ≠ 0) :
    word3 q wL 3 3 = ((2*q^6 - 3*q^4 + 3*q^2 - 1) / (q^10)) := by
  rw [entry_eq_mulVec_single (word3 q wL) 3 3]
  simp only [wL, word3_mulVec_cons, word3_nil, Matrix.one_mulVec, gl3]
  rw [wL_3_3_s0 q hq, wL_3_3_s1 q hq, wL_3_3_s2 q hq, wL_3_3_s3 q hq, wL_3_3_s4 q hq, wL_3_3_s5 q hq, wL_3_3_s6 q hq, wL_3_3_s7 q hq, wL_3_3_s8 q hq, wL_3_3_s9 q hq, wL_3_3_s10 q hq, wL_3_3_s11 q hq]
  simp [wL_3_3_v11]

@[simp] def wAL_2_0_v0 (q : R) : Fin 6 → R := ![((1) / (q)), (0), (0), (0), (0), (0)]

theorem wAL_2_0_s0 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (Pi.single 0 1) = wAL_2_0_v0 q := by
  stepTac

@[simp] def wAL_2_0_v1 (q : R) : Fin 6 → R := ![((1) / (q^2)), (0), (0), (0), (0), (0)]

theorem wAL_2_0_s1 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wAL_2_0_v0 q) = wAL_2_0_v1 q := by
  stepTac

@[simp] def wAL_2_0_v2 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^3)), ((1) / (q^2)), (0), (0), (0), (0)]

theorem wAL_2_0_s2 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wAL_2_0_v1 q) = wAL_2_0_v2 q := by
  stepTac

@[simp] def wAL_2_0_v3 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^2)), (0), (0), ((1) / (q^2)), (0), (0)]

theorem wAL_2_0_s3 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wAL_2_0_v2 q) = wAL_2_0_v3 q := by
  stepTac

@[simp] def wAL_2_0_v4 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2)), (0), ((1) / (q^3)), (0), (0)]

theorem wAL_2_0_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wAL_2_0_v3 q) = wAL_2_0_v4 q := by
  stepTac

@[simp] def wAL_2_0_v5 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^2)), ((1) / (q^3)), (0), ((-q^4 + 2*q^2 - 1) / (q^4)), (0), (0)]

theorem wAL_2_0_s5 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wAL_2_0_v4 q) = wAL_2_0_v5 q := by
  stepTac

@[simp] def wAL_2_0_v6 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 3*q^2 + 2) / (q^3)), ((q^4 - 2*q^2 + 1) / (q^2)), (0), ((-q^4 + 2*q^2 - 1) / (q^5)), (0), (0)]

theorem wAL_2_0_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wAL_2_0_v5 q) = wAL_2_0_v6 q := by
  stepTac

@[simp] def wAL_2_0_v7 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 3*q^2 + 2) / (q^2)), ((-q^4 + 2*q^2 - 1) / (q^5)), (0), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6)), (0), (0)]

theorem wAL_2_0_s7 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wAL_2_0_v6 q) = wAL_2_0_v7 q := by
  stepTac

theorem wAL_2_0_entry (q : R) (hq : q ≠ 0) :
    word2 q wAL 0 0 = ((-q^6 + 3*q^4 - 3*q^2 + 2) / (q^2)) := by
  rw [entry_eq_mulVec_single (word2 q wAL) 0 0]
  simp only [wAL, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wAL_2_0_s0 q hq, wAL_2_0_s1 q hq, wAL_2_0_s2 q hq, wAL_2_0_s3 q hq, wAL_2_0_s4 q hq, wAL_2_0_s5 q hq, wAL_2_0_s6 q hq, wAL_2_0_s7 q hq]
  simp [wAL_2_0_v7]

@[simp] def wAL_2_1_v0 (q : R) : Fin 6 → R := ![(0), ((1 - q^2) / (q)), (1), (0), (0), (0)]

theorem wAL_2_1_s0 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (Pi.single 1 1) = wAL_2_1_v0 q := by
  stepTac

@[simp] def wAL_2_1_v1 (q : R) : Fin 6 → R := ![(0), ((q^4 - q^2 + 1) / (q^2)), ((1 - q^2) / (q)), (0), (0), (0)]

theorem wAL_2_1_s1 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wAL_2_1_v0 q) = wAL_2_1_v1 q := by
  stepTac

@[simp] def wAL_2_1_v2 (q : R) : Fin 6 → R := ![((q^4 - q^2 + 1) / (q^2)), (0), ((1 - q^2) / (q^2)), (0), (0), (0)]

theorem wAL_2_1_s2 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wAL_2_1_v1 q) = wAL_2_1_v2 q := by
  stepTac

@[simp] def wAL_2_1_v3 (q : R) : Fin 6 → R := ![((q^4 - q^2 + 1) / (q)), (0), (0), (0), ((1 - q^2) / (q^2)), (0)]

theorem wAL_2_1_s3 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wAL_2_1_v2 q) = wAL_2_1_v3 q := by
  stepTac

@[simp] def wAL_2_1_v4 (q : R) : Fin 6 → R := ![((-q^6 + 2*q^4 - 2*q^2 + 1) / (q^2)), ((q^4 - q^2 + 1) / (q)), (0), (0), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2))]

theorem wAL_2_1_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wAL_2_1_v3 q) = wAL_2_1_v4 q := by
  stepTac

@[simp] def wAL_2_1_v5 (q : R) : Fin 6 → R := ![((-q^6 + 2*q^4 - 2*q^2 + 1) / (q)), (0), ((q^4 - 2*q^2 + 1) / (q^3)), ((q^4 - q^2 + 1) / (q)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^4)), ((1 - q^2) / (q))]

theorem wAL_2_1_s5 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wAL_2_1_v4 q) = wAL_2_1_v5 q := by
  stepTac

@[simp] def wAL_2_1_v6 (q : R) : Fin 6 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^2)), ((-q^6 + 2*q^4 - 2*q^2 + 1) / (q)), ((q^4 - 2*q^2 + 1) / (q^4)), ((q^4 - q^2 + 1) / (q^2)), ((-q^8 + 3*q^6 - 5*q^4 + 4*q^2 - 1) / (q^5)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^4))]

theorem wAL_2_1_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wAL_2_1_v5 q) = wAL_2_1_v6 q := by
  stepTac

@[simp] def wAL_2_1_v7 (q : R) : Fin 6 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q)), ((q^4 - q^2 + 1) / (q^2)), ((-q^8 + 3*q^6 - 5*q^4 + 4*q^2 - 1) / (q^5)), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / (q^3)), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / (q^6)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^3))]

theorem wAL_2_1_s7 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wAL_2_1_v6 q) = wAL_2_1_v7 q := by
  stepTac

theorem wAL_2_1_entry (q : R) (hq : q ≠ 0) :
    word2 q wAL 1 1 = ((q^4 - q^2 + 1) / (q^2)) := by
  rw [entry_eq_mulVec_single (word2 q wAL) 1 1]
  simp only [wAL, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wAL_2_1_s0 q hq, wAL_2_1_s1 q hq, wAL_2_1_s2 q hq, wAL_2_1_s3 q hq, wAL_2_1_s4 q hq, wAL_2_1_s5 q hq, wAL_2_1_s6 q hq, wAL_2_1_s7 q hq]
  simp [wAL_2_1_v7]

@[simp] def wAL_2_3_v0 (q : R) : Fin 6 → R := ![(0), (0), (0), ((1 - q^2) / (q)), (1), (0)]

theorem wAL_2_3_s0 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (Pi.single 3 1) = wAL_2_3_v0 q := by
  stepTac

@[simp] def wAL_2_3_v1 (q : R) : Fin 6 → R := ![(0), (0), (0), ((q^4 - q^2 + 1) / (q^2)), ((1 - q^2) / (q)), (0)]

theorem wAL_2_3_s1 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wAL_2_3_v0 q) = wAL_2_3_v1 q := by
  stepTac

@[simp] def wAL_2_3_v2 (q : R) : Fin 6 → R := ![(0), (0), (0), ((q^4 - q^2 + 1) / (q^3)), ((q^4 - 2*q^2 + 1) / (q^2)), ((1 - q^2) / (q))]

theorem wAL_2_3_s2 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wAL_2_3_v1 q) = wAL_2_3_v2 q := by
  stepTac

@[simp] def wAL_2_3_v3 (q : R) : Fin 6 → R := ![(0), ((q^4 - q^2 + 1) / (q^3)), ((q^4 - 2*q^2 + 1) / (q^2)), ((q^6 - 2*q^4 + 2*q^2 - 1) / (q^4)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^3)), (1 - q^2)]

theorem wAL_2_3_s3 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wAL_2_3_v2 q) = wAL_2_3_v3 q := by
  stepTac

@[simp] def wAL_2_3_v4 (q : R) : Fin 6 → R := ![((q^4 - q^2 + 1) / (q^3)), (0), ((q^4 - 2*q^2 + 1) / (q^3)), ((q^6 - 2*q^4 + 2*q^2 - 1) / (q^5)), ((-q^8 + 3*q^6 - 5*q^4 + 4*q^2 - 1) / (q^4)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^3))]

theorem wAL_2_3_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wAL_2_3_v3 q) = wAL_2_3_v4 q := by
  stepTac

@[simp] def wAL_2_3_v5 (q : R) : Fin 6 → R := ![((q^4 - q^2 + 1) / (q^2)), ((q^6 - 2*q^4 + 2*q^2 - 1) / (q^5)), ((-q^8 + 3*q^6 - 5*q^4 + 4*q^2 - 1) / (q^4)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6)), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / (q^5)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^2))]

theorem wAL_2_3_s5 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wAL_2_3_v4 q) = wAL_2_3_v5 q := by
  stepTac

@[simp] def wAL_2_3_v6 (q : R) : Fin 6 → R := ![((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / (q^5)), ((q^4 - q^2 + 1) / (q^2)), ((-q^8 + 3*q^6 - 5*q^4 + 4*q^2 - 1) / (q^5)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^7)), ((q^12 - 4*q^10 + 8*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / (q^6)), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / (q^5))]

theorem wAL_2_3_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wAL_2_3_v5 q) = wAL_2_3_v6 q := by
  stepTac

@[simp] def wAL_2_3_v7 (q : R) : Fin 6 → R := ![((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / (q^4)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^7)), ((q^12 - 4*q^10 + 8*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / (q^6)), ((2*q^10 - 5*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^8)), ((q^14 - 5*q^12 + 11*q^10 - 16*q^8 + 16*q^6 - 11*q^4 + 5*q^2 - 1) / (q^7)), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / (q^4))]

theorem wAL_2_3_s7 (q : R) (hq : q ≠ 0) :
    (g2_0 q).mulVec (wAL_2_3_v6 q) = wAL_2_3_v7 q := by
  stepTac

theorem wAL_2_3_entry (q : R) (hq : q ≠ 0) :
    word2 q wAL 3 3 = ((2*q^10 - 5*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^8)) := by
  rw [entry_eq_mulVec_single (word2 q wAL) 3 3]
  simp only [wAL, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wAL_2_3_s0 q hq, wAL_2_3_s1 q hq, wAL_2_3_s2 q hq, wAL_2_3_s3 q hq, wAL_2_3_s4 q hq, wAL_2_3_s5 q hq, wAL_2_3_s6 q hq, wAL_2_3_s7 q hq]
  simp [wAL_2_3_v7]

@[simp] def wAL_3_1_v0 (q : R) : Fin 4 → R := ![(1), (0), (0), (0)]

theorem wAL_3_1_s0 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (Pi.single 1 1) = wAL_3_1_v0 q := by
  stepTac

@[simp] def wAL_3_1_v1 (q : R) : Fin 4 → R := ![((1 - q^2) / (q)), (1), (0), (0)]

theorem wAL_3_1_s1 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wAL_3_1_v0 q) = wAL_3_1_v1 q := by
  stepTac

@[simp] def wAL_3_1_v2 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^2)), ((1 - q^2) / (q)), (1), (0)]

theorem wAL_3_1_s2 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wAL_3_1_v1 q) = wAL_3_1_v2 q := by
  stepTac

@[simp] def wAL_3_1_v3 (q : R) : Fin 4 → R := ![((1 - q^2) / (q)), (1 - q^2), (0), (1)]

theorem wAL_3_1_s3 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wAL_3_1_v2 q) = wAL_3_1_v3 q := by
  stepTac

@[simp] def wAL_3_1_v4 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^2)), ((q^4 - 2*q^2 + 1) / (q)), (1 - q^2), ((1) / (q))]

theorem wAL_3_1_s4 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wAL_3_1_v3 q) = wAL_3_1_v4 q := by
  stepTac

@[simp] def wAL_3_1_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / (q)), (q^4 - 2*q^2 + 1), ((1) / (q)), ((-q^4 + 2*q^2 - 1) / (q^2))]

theorem wAL_3_1_s5 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wAL_3_1_v4 q) = wAL_3_1_v5 q := by
  stepTac

@[simp] def wAL_3_1_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^2)), ((-q^6 + 3*q^4 - 3*q^2 + 2) / (q)), (q^4 - 2*q^2 + 1), ((-q^4 + 2*q^2 - 1) / (q^3))]

theorem wAL_3_1_s6 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wAL_3_1_v5 q) = wAL_3_1_v6 q := by
  stepTac

@[simp] def wAL_3_1_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / (q)), (-q^6 + 3*q^4 - 3*q^2 + 2), ((-q^4 + 2*q^2 - 1) / (q^3)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^4))]

theorem wAL_3_1_s7 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wAL_3_1_v6 q) = wAL_3_1_v7 q := by
  stepTac

theorem wAL_3_1_entry (q : R) (hq : q ≠ 0) :
    word3 q wAL 1 1 = (-q^6 + 3*q^4 - 3*q^2 + 2) := by
  rw [entry_eq_mulVec_single (word3 q wAL) 1 1]
  simp only [wAL, word3_mulVec_cons, word3_nil, Matrix.one_mulVec, gl3]
  rw [wAL_3_1_s0 q hq, wAL_3_1_s1 q hq, wAL_3_1_s2 q hq, wAL_3_1_s3 q hq, wAL_3_1_s4 q hq, wAL_3_1_s5 q hq, wAL_3_1_s6 q hq, wAL_3_1_s7 q hq]
  simp [wAL_3_1_v7]

@[simp] def wAL_3_2_v0 (q : R) : Fin 4 → R := ![(0), (0), ((1) / (q)), (0)]

theorem wAL_3_2_s0 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (Pi.single 2 1) = wAL_3_2_v0 q := by
  stepTac

@[simp] def wAL_3_2_v1 (q : R) : Fin 4 → R := ![(0), (0), ((1) / (q^2)), (0)]

theorem wAL_3_2_s1 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wAL_3_2_v0 q) = wAL_3_2_v1 q := by
  stepTac

@[simp] def wAL_3_2_v2 (q : R) : Fin 4 → R := ![(0), ((1) / (q^2)), (0), (0)]

theorem wAL_3_2_s2 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wAL_3_2_v1 q) = wAL_3_2_v2 q := by
  stepTac

@[simp] def wAL_3_2_v3 (q : R) : Fin 4 → R := ![(0), ((1) / (q)), (0), (0)]

theorem wAL_3_2_s3 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wAL_3_2_v2 q) = wAL_3_2_v3 q := by
  stepTac

@[simp] def wAL_3_2_v4 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / (q^2)), ((1) / (q)), (0)]

theorem wAL_3_2_s4 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wAL_3_2_v3 q) = wAL_3_2_v4 q := by
  stepTac

@[simp] def wAL_3_2_v5 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / (q)), (0), ((1) / (q))]

theorem wAL_3_2_s5 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wAL_3_2_v4 q) = wAL_3_2_v5 q := by
  stepTac

@[simp] def wAL_3_2_v6 (q : R) : Fin 4 → R := ![(0), ((q^4 - 2*q^2 + 1) / (q^2)), ((1 - q^2) / (q)), ((1) / (q^2))]

theorem wAL_3_2_s6 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wAL_3_2_v5 q) = wAL_3_2_v6 q := by
  stepTac

@[simp] def wAL_3_2_v7 (q : R) : Fin 4 → R := ![(0), ((q^4 - 2*q^2 + 1) / (q)), ((1) / (q^2)), ((-q^4 + 2*q^2 - 1) / (q^3))]

theorem wAL_3_2_s7 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wAL_3_2_v6 q) = wAL_3_2_v7 q := by
  stepTac

theorem wAL_3_2_entry (q : R) (hq : q ≠ 0) :
    word3 q wAL 2 2 = ((1) / (q^2)) := by
  rw [entry_eq_mulVec_single (word3 q wAL) 2 2]
  simp only [wAL, word3_mulVec_cons, word3_nil, Matrix.one_mulVec, gl3]
  rw [wAL_3_2_s0 q hq, wAL_3_2_s1 q hq, wAL_3_2_s2 q hq, wAL_3_2_s3 q hq, wAL_3_2_s4 q hq, wAL_3_2_s5 q hq, wAL_3_2_s6 q hq, wAL_3_2_s7 q hq]
  simp [wAL_3_2_v7]

@[simp] def wAL_3_3_v0 (q : R) : Fin 4 → R := ![(0), (0), (0), ((1) / (q))]

theorem wAL_3_3_s0 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (Pi.single 3 1) = wAL_3_3_v0 q := by
  stepTac

@[simp] def wAL_3_3_v1 (q : R) : Fin 4 → R := ![(0), (0), (0), ((1) / (q^2))]

theorem wAL_3_3_s1 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wAL_3_3_v0 q) = wAL_3_3_v1 q := by
  stepTac

@[simp] def wAL_3_3_v2 (q : R) : Fin 4 → R := ![(0), (0), (0), ((1) / (q^3))]

theorem wAL_3_3_s2 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wAL_3_3_v1 q) = wAL_3_3_v2 q := by
  stepTac

@[simp] def wAL_3_3_v3 (q : R) : Fin 4 → R := ![(0), (0), ((1) / (q^3)), ((q^2 - 1) / (q^4))]

theorem wAL_3_3_s3 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wAL_3_3_v2 q) = wAL_3_3_v3 q := by
  stepTac

@[simp] def wAL_3_3_v4 (q : R) : Fin 4 → R := ![(0), ((1) / (q^3)), (0), ((q^2 - 1) / (q^5))]

theorem wAL_3_3_s4 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wAL_3_3_v3 q) = wAL_3_3_v4 q := by
  stepTac

@[simp] def wAL_3_3_v5 (q : R) : Fin 4 → R := ![(0), ((1) / (q^2)), ((q^2 - 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^6))]

theorem wAL_3_3_s5 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wAL_3_3_v4 q) = wAL_3_3_v5 q := by
  stepTac

@[simp] def wAL_3_3_v6 (q : R) : Fin 4 → R := ![(0), ((-q^4 + 2*q^2 - 1) / (q^5)), ((1) / (q^2)), ((q^4 - 2*q^2 + 1) / (q^7))]

theorem wAL_3_3_s6 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wAL_3_3_v5 q) = wAL_3_3_v6 q := by
  stepTac

@[simp] def wAL_3_3_v7 (q : R) : Fin 4 → R := ![(0), ((-q^4 + 2*q^2 - 1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^7)), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / (q^8))]

theorem wAL_3_3_s7 (q : R) (hq : q ≠ 0) :
    (g3_0 q).mulVec (wAL_3_3_v6 q) = wAL_3_3_v7 q := by
  stepTac

theorem wAL_3_3_entry (q : R) (hq : q ≠ 0) :
    word3 q wAL 3 3 = ((2*q^6 - 3*q^4 + 3*q^2 - 1) / (q^8)) := by
  rw [entry_eq_mulVec_single (word3 q wAL) 3 3]
  simp only [wAL, word3_mulVec_cons, word3_nil, Matrix.one_mulVec, gl3]
  rw [wAL_3_3_s0 q hq, wAL_3_3_s1 q hq, wAL_3_3_s2 q hq, wAL_3_3_s3 q hq, wAL_3_3_s4 q hq, wAL_3_3_s5 q hq, wAL_3_3_s6 q hq, wAL_3_3_s7 q hq]
  simp [wAL_3_3_v7]

@[simp] def wR_1_1_v0 (q : R) : Fin 4 → R := ![(1), (0), (0), (0)]

theorem wR_1_1_s0 (q : R) (hq : q ≠ 0) :
    (g1_0i q).mulVec (Pi.single 1 1) = wR_1_1_v0 q := by
  stepTac

@[simp] def wR_1_1_v1 (q : R) : Fin 4 → R := ![((1) / (q)), (0), (0), (0)]

theorem wR_1_1_s1 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_1_v0 q) = wR_1_1_v1 q := by
  stepTac

@[simp] def wR_1_1_v2 (q : R) : Fin 4 → R := ![((1) / (q^2)), (0), (0), (0)]

theorem wR_1_1_s2 (q : R) (hq : q ≠ 0) :
    (g1_2i q).mulVec (wR_1_1_v1 q) = wR_1_1_v2 q := by
  stepTac

@[simp] def wR_1_1_v3 (q : R) : Fin 4 → R := ![((1) / (q^3)), (0), (0), (0)]

theorem wR_1_1_s3 (q : R) (hq : q ≠ 0) :
    (g1_2i q).mulVec (wR_1_1_v2 q) = wR_1_1_v3 q := by
  stepTac

@[simp] def wR_1_1_v4 (q : R) : Fin 4 → R := ![((1) / (q^4)), (0), (0), (0)]

theorem wR_1_1_s4 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_1_v3 q) = wR_1_1_v4 q := by
  stepTac

@[simp] def wR_1_1_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((1) / (q^4)), (0), (0)]

theorem wR_1_1_s5 (q : R) (hq : q ≠ 0) :
    (g1_0i q).mulVec (wR_1_1_v4 q) = wR_1_1_v5 q := by
  stepTac

@[simp] def wR_1_1_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^6)), ((1 - q^2) / (q^5)), ((1) / (q^4)), (0)]

theorem wR_1_1_s6 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_1_v5 q) = wR_1_1_v6 q := by
  stepTac

@[simp] def wR_1_1_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((1 - q^2) / (q^4)), (0), ((1) / (q^4))]

theorem wR_1_1_s7 (q : R) (hq : q ≠ 0) :
    (g1_2 q).mulVec (wR_1_1_v6 q) = wR_1_1_v7 q := by
  stepTac

@[simp] def wR_1_1_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((1 - q^2) / (q^4)), ((1) / (q^5))]

theorem wR_1_1_s8 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_1_v7 q) = wR_1_1_v8 q := by
  stepTac

@[simp] def wR_1_1_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1) / (q^5)), ((-q^4 + 2*q^2 - 1) / (q^6))]

theorem wR_1_1_s9 (q : R) (hq : q ≠ 0) :
    (g1_2 q).mulVec (wR_1_1_v8 q) = wR_1_1_v9 q := by
  stepTac

@[simp] def wR_1_1_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^6)), ((-q^6 + 3*q^4 - 3*q^2 + 2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^7))]

theorem wR_1_1_s10 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_1_v9 q) = wR_1_1_v10 q := by
  stepTac

@[simp] def wR_1_1_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((-q^6 + 3*q^4 - 3*q^2 + 2) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^7)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^8))]

theorem wR_1_1_s11 (q : R) (hq : q ≠ 0) :
    (g1_2 q).mulVec (wR_1_1_v10 q) = wR_1_1_v11 q := by
  stepTac

theorem wR_1_1_entry (q : R) (hq : q ≠ 0) :
    word1 q wR 1 1 = ((-q^6 + 3*q^4 - 3*q^2 + 2) / (q^4)) := by
  rw [entry_eq_mulVec_single (word1 q wR) 1 1]
  simp only [wR, word1_mulVec_cons, word1_nil, Matrix.one_mulVec, gl1]
  rw [wR_1_1_s0 q hq, wR_1_1_s1 q hq, wR_1_1_s2 q hq, wR_1_1_s3 q hq, wR_1_1_s4 q hq, wR_1_1_s5 q hq, wR_1_1_s6 q hq, wR_1_1_s7 q hq, wR_1_1_s8 q hq, wR_1_1_s9 q hq, wR_1_1_s10 q hq, wR_1_1_s11 q hq]
  simp [wR_1_1_v11]

@[simp] def wR_1_2_v0 (q : R) : Fin 4 → R := ![(0), (0), ((1) / (q)), (0)]

theorem wR_1_2_s0 (q : R) (hq : q ≠ 0) :
    (g1_0i q).mulVec (Pi.single 2 1) = wR_1_2_v0 q := by
  stepTac

@[simp] def wR_1_2_v1 (q : R) : Fin 4 → R := ![(0), ((1) / (q)), (0), (0)]

theorem wR_1_2_s1 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_2_v0 q) = wR_1_2_v1 q := by
  stepTac

@[simp] def wR_1_2_v2 (q : R) : Fin 4 → R := ![(0), ((1) / (q^2)), (0), (0)]

theorem wR_1_2_s2 (q : R) (hq : q ≠ 0) :
    (g1_2i q).mulVec (wR_1_2_v1 q) = wR_1_2_v2 q := by
  stepTac

@[simp] def wR_1_2_v3 (q : R) : Fin 4 → R := ![(0), ((1) / (q^3)), (0), (0)]

theorem wR_1_2_s3 (q : R) (hq : q ≠ 0) :
    (g1_2i q).mulVec (wR_1_2_v2 q) = wR_1_2_v3 q := by
  stepTac

@[simp] def wR_1_2_v4 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / (q^4)), ((1) / (q^3)), (0)]

theorem wR_1_2_s4 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_2_v3 q) = wR_1_2_v4 q := by
  stepTac

@[simp] def wR_1_2_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), (0), ((1) / (q^4)), (0)]

theorem wR_1_2_s5 (q : R) (hq : q ≠ 0) :
    (g1_0i q).mulVec (wR_1_2_v4 q) = wR_1_2_v5 q := by
  stepTac

@[simp] def wR_1_2_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((1) / (q^4)), (0), (0)]

theorem wR_1_2_s6 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_2_v5 q) = wR_1_2_v6 q := by
  stepTac

@[simp] def wR_1_2_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((1) / (q^3)), (0), (0)]

theorem wR_1_2_s7 (q : R) (hq : q ≠ 0) :
    (g1_2 q).mulVec (wR_1_2_v6 q) = wR_1_2_v7 q := by
  stepTac

@[simp] def wR_1_2_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((1 - q^2) / (q^4)), ((1) / (q^3)), (0)]

theorem wR_1_2_s8 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_2_v7 q) = wR_1_2_v8 q := by
  stepTac

@[simp] def wR_1_2_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((1 - q^2) / (q^3)), (0), ((1) / (q^3))]

theorem wR_1_2_s9 (q : R) (hq : q ≠ 0) :
    (g1_2 q).mulVec (wR_1_2_v8 q) = wR_1_2_v9 q := by
  stepTac

@[simp] def wR_1_2_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), ((1) / (q^4))]

theorem wR_1_2_s10 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_2_v9 q) = wR_1_2_v10 q := by
  stepTac

@[simp] def wR_1_2_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^5))]

theorem wR_1_2_s11 (q : R) (hq : q ≠ 0) :
    (g1_2 q).mulVec (wR_1_2_v10 q) = wR_1_2_v11 q := by
  stepTac

theorem wR_1_2_entry (q : R) (hq : q ≠ 0) :
    word1 q wR 2 2 = ((1) / (q^4)) := by
  rw [entry_eq_mulVec_single (word1 q wR) 2 2]
  simp only [wR, word1_mulVec_cons, word1_nil, Matrix.one_mulVec, gl1]
  rw [wR_1_2_s0 q hq, wR_1_2_s1 q hq, wR_1_2_s2 q hq, wR_1_2_s3 q hq, wR_1_2_s4 q hq, wR_1_2_s5 q hq, wR_1_2_s6 q hq, wR_1_2_s7 q hq, wR_1_2_s8 q hq, wR_1_2_s9 q hq, wR_1_2_s10 q hq, wR_1_2_s11 q hq]
  simp [wR_1_2_v11]

@[simp] def wR_1_3_v0 (q : R) : Fin 4 → R := ![(0), (0), (0), ((1) / (q))]

theorem wR_1_3_s0 (q : R) (hq : q ≠ 0) :
    (g1_0i q).mulVec (Pi.single 3 1) = wR_1_3_v0 q := by
  stepTac

@[simp] def wR_1_3_v1 (q : R) : Fin 4 → R := ![(0), (0), (0), ((1) / (q^2))]

theorem wR_1_3_s1 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_3_v0 q) = wR_1_3_v1 q := by
  stepTac

@[simp] def wR_1_3_v2 (q : R) : Fin 4 → R := ![(0), (0), ((1) / (q^2)), (0)]

theorem wR_1_3_s2 (q : R) (hq : q ≠ 0) :
    (g1_2i q).mulVec (wR_1_3_v1 q) = wR_1_3_v2 q := by
  stepTac

@[simp] def wR_1_3_v3 (q : R) : Fin 4 → R := ![(0), (0), ((1 - q^2) / (q^3)), ((1) / (q^2))]

theorem wR_1_3_s3 (q : R) (hq : q ≠ 0) :
    (g1_2i q).mulVec (wR_1_3_v2 q) = wR_1_3_v3 q := by
  stepTac

@[simp] def wR_1_3_v4 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / (q^3)), (0), ((1) / (q^3))]

theorem wR_1_3_s4 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_3_v3 q) = wR_1_3_v4 q := by
  stepTac

@[simp] def wR_1_3_v5 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^3)), (0), (0), ((1) / (q^4))]

theorem wR_1_3_s5 (q : R) (hq : q ≠ 0) :
    (g1_0i q).mulVec (wR_1_3_v4 q) = wR_1_3_v5 q := by
  stepTac

@[simp] def wR_1_3_v6 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), (0), (0), ((1) / (q^5))]

theorem wR_1_3_s6 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_3_v5 q) = wR_1_3_v6 q := by
  stepTac

@[simp] def wR_1_3_v7 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^3)), (0), ((1) / (q^5)), ((q^2 - 1) / (q^6))]

theorem wR_1_3_s7 (q : R) (hq : q ≠ 0) :
    (g1_2 q).mulVec (wR_1_3_v6 q) = wR_1_3_v7 q := by
  stepTac

@[simp] def wR_1_3_v8 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((1) / (q^5)), (0), ((q^2 - 1) / (q^7))]

theorem wR_1_3_s8 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_3_v7 q) = wR_1_3_v8 q := by
  stepTac

@[simp] def wR_1_3_v9 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^3)), ((1) / (q^4)), ((q^2 - 1) / (q^7)), ((q^4 - 2*q^2 + 1) / (q^8))]

theorem wR_1_3_s9 (q : R) (hq : q ≠ 0) :
    (g1_2 q).mulVec (wR_1_3_v8 q) = wR_1_3_v9 q := by
  stepTac

@[simp] def wR_1_3_v10 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^7)), ((1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^9))]

theorem wR_1_3_s10 (q : R) (hq : q ≠ 0) :
    (g1_1i q).mulVec (wR_1_3_v9 q) = wR_1_3_v10 q := by
  stepTac

@[simp] def wR_1_3_v11 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^3)), ((-q^4 + 2*q^2 - 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^9)), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / (q^10))]

theorem wR_1_3_s11 (q : R) (hq : q ≠ 0) :
    (g1_2 q).mulVec (wR_1_3_v10 q) = wR_1_3_v11 q := by
  stepTac

theorem wR_1_3_entry (q : R) (hq : q ≠ 0) :
    word1 q wR 3 3 = ((2*q^6 - 3*q^4 + 3*q^2 - 1) / (q^10)) := by
  rw [entry_eq_mulVec_single (word1 q wR) 3 3]
  simp only [wR, word1_mulVec_cons, word1_nil, Matrix.one_mulVec, gl1]
  rw [wR_1_3_s0 q hq, wR_1_3_s1 q hq, wR_1_3_s2 q hq, wR_1_3_s3 q hq, wR_1_3_s4 q hq, wR_1_3_s5 q hq, wR_1_3_s6 q hq, wR_1_3_s7 q hq, wR_1_3_s8 q hq, wR_1_3_s9 q hq, wR_1_3_s10 q hq, wR_1_3_s11 q hq]
  simp [wR_1_3_v11]

@[simp] def wR_2_0_v0 (q : R) : Fin 6 → R := ![((1) / (q)), (0), (0), (0), (0), (0)]

theorem wR_2_0_s0 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (Pi.single 0 1) = wR_2_0_v0 q := by
  stepTac

@[simp] def wR_2_0_v1 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^2)), ((1) / (q)), (0), (0), (0), (0)]

theorem wR_2_0_s1 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_0_v0 q) = wR_2_0_v1 q := by
  stepTac

@[simp] def wR_2_0_v2 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^3)), ((1 - q^2) / (q^2)), ((1) / (q)), (0), (0), (0)]

theorem wR_2_0_s2 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_0_v1 q) = wR_2_0_v2 q := by
  stepTac

@[simp] def wR_2_0_v3 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^4)), ((q^4 - q^2 + 1) / (q^3)), ((1 - q^2) / (q^2)), (0), (0), (0)]

theorem wR_2_0_s3 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_0_v2 q) = wR_2_0_v3 q := by
  stepTac

@[simp] def wR_2_0_v4 (q : R) : Fin 6 → R := ![((q^6 - q^2 + 1) / (q^5)), ((1 - q^2) / (q^4)), ((1 - q^2) / (q^3)), (0), (0), (0)]

theorem wR_2_0_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_0_v3 q) = wR_2_0_v4 q := by
  stepTac

@[simp] def wR_2_0_v5 (q : R) : Fin 6 → R := ![((q^6 - q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^4)), ((1 - q^2) / (q^3)), (0)]

theorem wR_2_0_s5 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wR_2_0_v4 q) = wR_2_0_v5 q := by
  stepTac

@[simp] def wR_2_0_v6 (q : R) : Fin 6 → R := ![((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^7)), ((q^6 - q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((1 - q^2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3))]

theorem wR_2_0_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_0_v5 q) = wR_2_0_v6 q := by
  stepTac

@[simp] def wR_2_0_v7 (q : R) : Fin 6 → R := ![((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^4)), ((q^4 - 3*q^2 + 2) / (q^3)), ((1 - q^2) / (q^2))]

theorem wR_2_0_s7 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_0_v6 q) = wR_2_0_v7 q := by
  stepTac

@[simp] def wR_2_0_v8 (q : R) : Fin 6 → R := ![((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^7)), ((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^6)), ((2*q^4 - 3*q^2 + 2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^5)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^4)), ((q^4 - 3*q^2 + 2) / (q^3))]

theorem wR_2_0_s8 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_0_v7 q) = wR_2_0_v8 q := by
  stepTac

@[simp] def wR_2_0_v9 (q : R) : Fin 6 → R := ![((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^6)), ((2*q^4 - 3*q^2 + 2) / (q^5)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^6)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^4)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^5)), ((q^4 - 3*q^2 + 2) / (q^2))]

theorem wR_2_0_s9 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_0_v8 q) = wR_2_0_v9 q := by
  stepTac

@[simp] def wR_2_0_v10 (q : R) : Fin 6 → R := ![((-q^12 + 4*q^10 - 7*q^8 + 8*q^6 - 4*q^4 + 1) / (q^7)), ((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^6)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^7)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^5)), ((q^10 - 4*q^8 + 7*q^6 - 8*q^4 + 5*q^2 - 1) / (q^6)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^5))]

theorem wR_2_0_s10 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_0_v9 q) = wR_2_0_v10 q := by
  stepTac

@[simp] def wR_2_0_v11 (q : R) : Fin 6 → R := ![((-q^12 + 4*q^10 - 7*q^8 + 8*q^6 - 4*q^4 + 1) / (q^6)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^7)), ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 9*q^4 - 4*q^2 + 1) / (q^8)), ((q^10 - 4*q^8 + 7*q^6 - 8*q^4 + 5*q^2 - 1) / (q^6)), ((q^12 - 5*q^10 + 10*q^8 - 12*q^6 + 9*q^4 - 4*q^2 + 1) / (q^7)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^4))]

theorem wR_2_0_s11 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_0_v10 q) = wR_2_0_v11 q := by
  stepTac

theorem wR_2_0_entry (q : R) (hq : q ≠ 0) :
    word2 q wR 0 0 = ((-q^12 + 4*q^10 - 7*q^8 + 8*q^6 - 4*q^4 + 1) / (q^6)) := by
  rw [entry_eq_mulVec_single (word2 q wR) 0 0]
  simp only [wR, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wR_2_0_s0 q hq, wR_2_0_s1 q hq, wR_2_0_s2 q hq, wR_2_0_s3 q hq, wR_2_0_s4 q hq, wR_2_0_s5 q hq, wR_2_0_s6 q hq, wR_2_0_s7 q hq, wR_2_0_s8 q hq, wR_2_0_s9 q hq, wR_2_0_s10 q hq, wR_2_0_s11 q hq]
  simp [wR_2_0_v11]

@[simp] def wR_2_1_v0 (q : R) : Fin 6 → R := ![(0), ((1 - q^2) / (q)), (0), (1), (0), (0)]

theorem wR_2_1_s0 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (Pi.single 1 1) = wR_2_1_v0 q := by
  stepTac

@[simp] def wR_2_1_v1 (q : R) : Fin 6 → R := ![((1 - q^2) / (q)), (0), (0), ((1) / (q)), (0), (0)]

theorem wR_2_1_s1 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_1_v0 q) = wR_2_1_v1 q := by
  stepTac

@[simp] def wR_2_1_v2 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^2)), (0), (0), ((1 - q^2) / (q^2)), ((1) / (q)), (0)]

theorem wR_2_1_s2 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_1_v1 q) = wR_2_1_v2 q := by
  stepTac

@[simp] def wR_2_1_v3 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^3)), (0), (0), ((q^4 - q^2 + 1) / (q^3)), ((1 - q^2) / (q^2)), (0)]

theorem wR_2_1_s3 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_1_v2 q) = wR_2_1_v3 q := by
  stepTac

@[simp] def wR_2_1_v4 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), (0), ((q^4 - q^2 + 1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2))]

theorem wR_2_1_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_1_v3 q) = wR_2_1_v4 q := by
  stepTac

@[simp] def wR_2_1_v5 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^5)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^3)), (0), ((1 - q^2) / (q^3))]

theorem wR_2_1_s5 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wR_2_1_v4 q) = wR_2_1_v5 q := by
  stepTac

@[simp] def wR_2_1_v6 (q : R) : Fin 6 → R := ![((q^6 - q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^4)), ((1 - q^2) / (q^3)), (0)]

theorem wR_2_1_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_1_v5 q) = wR_2_1_v6 q := by
  stepTac

@[simp] def wR_2_1_v7 (q : R) : Fin 6 → R := ![((q^6 - q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^3)), ((1 - q^2) / (q^2)), (0)]

theorem wR_2_1_s7 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_1_v6 q) = wR_2_1_v7 q := by
  stepTac

@[simp] def wR_2_1_v8 (q : R) : Fin 6 → R := ![((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^6)), ((q^6 - q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2))]

theorem wR_2_1_s8 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_1_v7 q) = wR_2_1_v8 q := by
  stepTac

@[simp] def wR_2_1_v9 (q : R) : Fin 6 → R := ![((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((2*q^4 - 3*q^2 + 2) / (q^3)), ((q^4 - 2*q^2 + 1) / (q^3)), ((q^4 - 3*q^2 + 2) / (q^2)), ((1 - q^2) / (q))]

theorem wR_2_1_s9 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_1_v8 q) = wR_2_1_v9 q := by
  stepTac

@[simp] def wR_2_1_v10 (q : R) : Fin 6 → R := ![((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^6)), ((-q^8 + 2*q^6 - q^4 - q^2 + 1) / (q^5)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^4)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^3)), ((q^4 - 3*q^2 + 2) / (q^2))]

theorem wR_2_1_s10 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_1_v9 q) = wR_2_1_v10 q := by
  stepTac

@[simp] def wR_2_1_v11 (q : R) : Fin 6 → R := ![((q^10 - 3*q^8 + 4*q^6 - 2*q^4 - q^2 + 1) / (q^5)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^5)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^3)), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^4)), ((q^4 - 3*q^2 + 2) / (q))]

theorem wR_2_1_s11 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_1_v10 q) = wR_2_1_v11 q := by
  stepTac

theorem wR_2_1_entry (q : R) (hq : q ≠ 0) :
    word2 q wR 1 1 = ((2*q^4 - 3*q^2 + 2) / (q^4)) := by
  rw [entry_eq_mulVec_single (word2 q wR) 1 1]
  simp only [wR, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wR_2_1_s0 q hq, wR_2_1_s1 q hq, wR_2_1_s2 q hq, wR_2_1_s3 q hq, wR_2_1_s4 q hq, wR_2_1_s5 q hq, wR_2_1_s6 q hq, wR_2_1_s7 q hq, wR_2_1_s8 q hq, wR_2_1_s9 q hq, wR_2_1_s10 q hq, wR_2_1_s11 q hq]
  simp [wR_2_1_v11]

@[simp] def wR_2_2_v0 (q : R) : Fin 6 → R := ![(0), (0), ((1 - q^2) / (q)), (0), (1), (0)]

theorem wR_2_2_s0 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (Pi.single 2 1) = wR_2_2_v0 q := by
  stepTac

@[simp] def wR_2_2_v1 (q : R) : Fin 6 → R := ![(0), (0), ((1 - q^2) / (q^2)), (0), ((1 - q^2) / (q)), (1)]

theorem wR_2_2_s1 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_2_v0 q) = wR_2_2_v1 q := by
  stepTac

@[simp] def wR_2_2_v2 (q : R) : Fin 6 → R := ![(0), ((1 - q^2) / (q^2)), (0), ((1 - q^2) / (q)), (0), ((1) / (q))]

theorem wR_2_2_s2 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_2_v1 q) = wR_2_2_v2 q := by
  stepTac

@[simp] def wR_2_2_v3 (q : R) : Fin 6 → R := ![(0), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2)), ((q^4 - 2*q^2 + 1) / (q^2)), ((1 - q^2) / (q)), ((1) / (q^2))]

theorem wR_2_2_s3 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_2_v2 q) = wR_2_2_v3 q := by
  stepTac

@[simp] def wR_2_2_v4 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^3)), (0), ((1 - q^2) / (q^3)), ((q^4 - 2*q^2 + 1) / (q^3)), ((q^4 - 2*q^2 + 2) / (q^2)), ((1 - q^2) / (q))]

theorem wR_2_2_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_2_v3 q) = wR_2_2_v4 q := by
  stepTac

@[simp] def wR_2_2_v5 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((q^6 - q^4 + 1) / (q^4)), (0), ((1 - q^2) / (q^3)), ((1 - q^2) / (q^2))]

theorem wR_2_2_s5 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wR_2_2_v4 q) = wR_2_2_v5 q := by
  stepTac

@[simp] def wR_2_2_v6 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((q^6 - q^4 + 1) / (q^5)), (0), ((1 - q^2) / (q^4)), ((1 - q^2) / (q^3))]

theorem wR_2_2_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_2_v5 q) = wR_2_2_v6 q := by
  stepTac

@[simp] def wR_2_2_v7 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((q^6 - q^4 + 1) / (q^5)), ((q^8 - q^6 - q^4 + 2*q^2 - 1) / (q^6)), ((1 - q^2) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^5)), ((1 - q^2) / (q^2))]

theorem wR_2_2_s7 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_2_v6 q) = wR_2_2_v7 q := by
  stepTac

@[simp] def wR_2_2_v8 (q : R) : Fin 6 → R := ![((2*q^4 - 3*q^2 + 2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((q^8 - q^6 - q^4 + 2*q^2 - 1) / (q^7)), ((1 - q^2) / (q^5)), ((-2*q^4 + 3*q^2 - 1) / (q^6)), ((-q^4 + 2*q^2 - 1) / (q^5))]

theorem wR_2_2_s8 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_2_v7 q) = wR_2_2_v8 q := by
  stepTac

@[simp] def wR_2_2_v9 (q : R) : Fin 6 → R := ![((2*q^4 - 3*q^2 + 2) / (q^4)), ((q^8 - q^6 - q^4 + 2*q^2 - 1) / (q^7)), ((q^10 - q^8 - 2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^8)), ((-2*q^4 + 3*q^2 - 1) / (q^6)), ((-2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^7)), ((-q^4 + 2*q^2 - 1) / (q^4))]

theorem wR_2_2_s9 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_2_v8 q) = wR_2_2_v9 q := by
  stepTac

@[simp] def wR_2_2_v10 (q : R) : Fin 6 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^7)), ((2*q^4 - 3*q^2 + 2) / (q^4)), ((q^10 - q^8 - 2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^9)), ((-2*q^4 + 3*q^2 - 1) / (q^7)), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / (q^8)), ((-2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^7))]

theorem wR_2_2_s10 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_2_v9 q) = wR_2_2_v10 q := by
  stepTac

@[simp] def wR_2_2_v11 (q : R) : Fin 6 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^6)), ((q^10 - q^8 - 2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^9)), ((q^12 - 4*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^10)), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / (q^8)), ((q^10 - 5*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^9)), ((-2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6))]

theorem wR_2_2_s11 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_2_v10 q) = wR_2_2_v11 q := by
  stepTac

theorem wR_2_2_entry (q : R) (hq : q ≠ 0) :
    word2 q wR 2 2 = ((q^12 - 4*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^10)) := by
  rw [entry_eq_mulVec_single (word2 q wR) 2 2]
  simp only [wR, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wR_2_2_s0 q hq, wR_2_2_s1 q hq, wR_2_2_s2 q hq, wR_2_2_s3 q hq, wR_2_2_s4 q hq, wR_2_2_s5 q hq, wR_2_2_s6 q hq, wR_2_2_s7 q hq, wR_2_2_s8 q hq, wR_2_2_s9 q hq, wR_2_2_s10 q hq, wR_2_2_s11 q hq]
  simp [wR_2_2_v11]

@[simp] def wR_2_3_v0 (q : R) : Fin 6 → R := ![(0), (1), (0), (0), (0), (0)]

theorem wR_2_3_s0 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (Pi.single 3 1) = wR_2_3_v0 q := by
  stepTac

@[simp] def wR_2_3_v1 (q : R) : Fin 6 → R := ![(1), (0), (0), (0), (0), (0)]

theorem wR_2_3_s1 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_3_v0 q) = wR_2_3_v1 q := by
  stepTac

@[simp] def wR_2_3_v2 (q : R) : Fin 6 → R := ![((1) / (q)), (0), (0), (0), (0), (0)]

theorem wR_2_3_s2 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_3_v1 q) = wR_2_3_v2 q := by
  stepTac

@[simp] def wR_2_3_v3 (q : R) : Fin 6 → R := ![((1) / (q^2)), (0), (0), (0), (0), (0)]

theorem wR_2_3_s3 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_3_v2 q) = wR_2_3_v3 q := by
  stepTac

@[simp] def wR_2_3_v4 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^3)), ((1) / (q^2)), (0), (0), (0), (0)]

theorem wR_2_3_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_3_v3 q) = wR_2_3_v4 q := by
  stepTac

@[simp] def wR_2_3_v5 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^4)), ((1 - q^2) / (q^3)), (0), ((1) / (q^2)), (0), (0)]

theorem wR_2_3_s5 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wR_2_3_v4 q) = wR_2_3_v5 q := by
  stepTac

@[simp] def wR_2_3_v6 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^5)), ((1 - q^2) / (q^4)), (0), ((1) / (q^3)), (0), (0)]

theorem wR_2_3_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_3_v5 q) = wR_2_3_v6 q := by
  stepTac

@[simp] def wR_2_3_v7 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^4)), (0), ((1 - q^2) / (q^4)), (0), ((1) / (q^3)), (0)]

theorem wR_2_3_s7 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_3_v6 q) = wR_2_3_v7 q := by
  stepTac

@[simp] def wR_2_3_v8 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^5)), ((1 - q^2) / (q^4)), ((1 - q^2) / (q^5)), (0), ((1 - q^2) / (q^4)), ((1) / (q^3))]

theorem wR_2_3_s8 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_3_v7 q) = wR_2_3_v8 q := by
  stepTac

@[simp] def wR_2_3_v9 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^5)), ((-2*q^4 + 3*q^2 - 1) / (q^6)), ((1 - q^2) / (q^4)), ((-q^4 + 2*q^2 - 1) / (q^5)), ((1) / (q^2))]

theorem wR_2_3_s9 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_3_v8 q) = wR_2_3_v9 q := by
  stepTac

@[simp] def wR_2_3_v10 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((-2*q^4 + 3*q^2 - 1) / (q^7)), ((1 - q^2) / (q^5)), ((q^6 - 2*q^4 + 3*q^2 - 1) / (q^6)), ((-q^4 + 2*q^2 - 1) / (q^5))]

theorem wR_2_3_s10 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_3_v9 q) = wR_2_3_v10 q := by
  stepTac

@[simp] def wR_2_3_v11 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^4)), ((-2*q^4 + 3*q^2 - 1) / (q^7)), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / (q^8)), ((q^6 - 2*q^4 + 3*q^2 - 1) / (q^6)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^7)), ((-q^4 + 2*q^2 - 1) / (q^4))]

theorem wR_2_3_s11 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_3_v10 q) = wR_2_3_v11 q := by
  stepTac

theorem wR_2_3_entry (q : R) (hq : q ≠ 0) :
    word2 q wR 3 3 = ((q^6 - 2*q^4 + 3*q^2 - 1) / (q^6)) := by
  rw [entry_eq_mulVec_single (word2 q wR) 3 3]
  simp only [wR, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wR_2_3_s0 q hq, wR_2_3_s1 q hq, wR_2_3_s2 q hq, wR_2_3_s3 q hq, wR_2_3_s4 q hq, wR_2_3_s5 q hq, wR_2_3_s6 q hq, wR_2_3_s7 q hq, wR_2_3_s8 q hq, wR_2_3_s9 q hq, wR_2_3_s10 q hq, wR_2_3_s11 q hq]
  simp [wR_2_3_v11]

@[simp] def wR_2_4_v0 (q : R) : Fin 6 → R := ![(0), (0), (1), (0), (0), (0)]

theorem wR_2_4_s0 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (Pi.single 4 1) = wR_2_4_v0 q := by
  stepTac

@[simp] def wR_2_4_v1 (q : R) : Fin 6 → R := ![(0), (0), ((1) / (q)), (0), (0), (0)]

theorem wR_2_4_s1 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_4_v0 q) = wR_2_4_v1 q := by
  stepTac

@[simp] def wR_2_4_v2 (q : R) : Fin 6 → R := ![(0), ((1) / (q)), (0), (0), (0), (0)]

theorem wR_2_4_s2 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_4_v1 q) = wR_2_4_v2 q := by
  stepTac

@[simp] def wR_2_4_v3 (q : R) : Fin 6 → R := ![(0), ((1 - q^2) / (q^2)), ((1) / (q)), (0), (0), (0)]

theorem wR_2_4_s3 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_4_v2 q) = wR_2_4_v3 q := by
  stepTac

@[simp] def wR_2_4_v4 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^2)), (0), ((1) / (q^2)), (0), (0), (0)]

theorem wR_2_4_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_4_v3 q) = wR_2_4_v4 q := by
  stepTac

@[simp] def wR_2_4_v5 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^3)), (0), ((1 - q^2) / (q^3)), (0), ((1) / (q^2)), (0)]

theorem wR_2_4_s5 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wR_2_4_v4 q) = wR_2_4_v5 q := by
  stepTac

@[simp] def wR_2_4_v6 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), ((1 - q^2) / (q^4)), (0), ((1 - q^2) / (q^3)), ((1) / (q^2))]

theorem wR_2_4_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_4_v5 q) = wR_2_4_v6 q := by
  stepTac

@[simp] def wR_2_4_v7 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^4)), ((-2*q^4 + 3*q^2 - 1) / (q^5)), ((1 - q^2) / (q^3)), ((-q^4 + 2*q^2 - 1) / (q^4)), ((1) / (q))]

theorem wR_2_4_s7 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_4_v6 q) = wR_2_4_v7 q := by
  stepTac

@[simp] def wR_2_4_v8 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((-2*q^4 + 3*q^2 - 1) / (q^6)), ((1 - q^2) / (q^4)), ((q^6 - 2*q^4 + 3*q^2 - 1) / (q^5)), ((-q^4 + 2*q^2 - 1) / (q^4))]

theorem wR_2_4_s8 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_4_v7 q) = wR_2_4_v8 q := by
  stepTac

@[simp] def wR_2_4_v9 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^3)), ((-2*q^4 + 3*q^2 - 1) / (q^6)), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / (q^7)), ((q^6 - 2*q^4 + 3*q^2 - 1) / (q^5)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6)), ((-q^4 + 2*q^2 - 1) / (q^3))]

theorem wR_2_4_s9 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_4_v8 q) = wR_2_4_v9 q := by
  stepTac

@[simp] def wR_2_4_v10 (q : R) : Fin 6 → R := ![((q^10 - 4*q^8 + 7*q^6 - 8*q^4 + 5*q^2 - 1) / (q^6)), ((-q^6 + 3*q^4 - 4*q^2 + 2) / (q^3)), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / (q^8)), ((q^6 - 2*q^4 + 3*q^2 - 1) / (q^6)), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / (q^7)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6))]

theorem wR_2_4_s10 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_4_v9 q) = wR_2_4_v10 q := by
  stepTac

@[simp] def wR_2_4_v11 (q : R) : Fin 6 → R := ![((q^10 - 4*q^8 + 7*q^6 - 8*q^4 + 5*q^2 - 1) / (q^5)), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / (q^8)), ((-q^12 + 4*q^10 - 9*q^8 + 12*q^6 - 10*q^4 + 5*q^2 - 1) / (q^9)), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / (q^7)), ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / (q^8)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^5))]

theorem wR_2_4_s11 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_4_v10 q) = wR_2_4_v11 q := by
  stepTac

theorem wR_2_4_entry (q : R) (hq : q ≠ 0) :
    word2 q wR 4 4 = ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / (q^8)) := by
  rw [entry_eq_mulVec_single (word2 q wR) 4 4]
  simp only [wR, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wR_2_4_s0 q hq, wR_2_4_s1 q hq, wR_2_4_s2 q hq, wR_2_4_s3 q hq, wR_2_4_s4 q hq, wR_2_4_s5 q hq, wR_2_4_s6 q hq, wR_2_4_s7 q hq, wR_2_4_s8 q hq, wR_2_4_s9 q hq, wR_2_4_s10 q hq, wR_2_4_s11 q hq]
  simp [wR_2_4_v11]

@[simp] def wR_2_5_v0 (q : R) : Fin 6 → R := ![(0), (0), (0), (0), (0), ((1) / (q))]

theorem wR_2_5_s0 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (Pi.single 5 1) = wR_2_5_v0 q := by
  stepTac

@[simp] def wR_2_5_v1 (q : R) : Fin 6 → R := ![(0), (0), (0), (0), ((1) / (q)), (0)]

theorem wR_2_5_s1 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_5_v0 q) = wR_2_5_v1 q := by
  stepTac

@[simp] def wR_2_5_v2 (q : R) : Fin 6 → R := ![(0), (0), (0), ((1) / (q)), (0), (0)]

theorem wR_2_5_s2 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_5_v1 q) = wR_2_5_v2 q := by
  stepTac

@[simp] def wR_2_5_v3 (q : R) : Fin 6 → R := ![(0), (0), (0), ((1 - q^2) / (q^2)), ((1) / (q)), (0)]

theorem wR_2_5_s3 (q : R) (hq : q ≠ 0) :
    (g2_2i q).mulVec (wR_2_5_v2 q) = wR_2_5_v3 q := by
  stepTac

@[simp] def wR_2_5_v4 (q : R) : Fin 6 → R := ![(0), (0), (0), ((1 - q^2) / (q^3)), ((1 - q^2) / (q^2)), ((1) / (q))]

theorem wR_2_5_s4 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_5_v3 q) = wR_2_5_v4 q := by
  stepTac

@[simp] def wR_2_5_v5 (q : R) : Fin 6 → R := ![(0), ((1 - q^2) / (q^3)), ((1 - q^2) / (q^2)), (0), (0), ((1) / (q^2))]

theorem wR_2_5_s5 (q : R) (hq : q ≠ 0) :
    (g2_0i q).mulVec (wR_2_5_v4 q) = wR_2_5_v5 q := by
  stepTac

@[simp] def wR_2_5_v6 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^3)), (0), ((1 - q^2) / (q^3)), (0), ((1) / (q^2)), (0)]

theorem wR_2_5_s6 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_5_v5 q) = wR_2_5_v6 q := by
  stepTac

@[simp] def wR_2_5_v7 (q : R) : Fin 6 → R := ![((1 - q^2) / (q^2)), ((1 - q^2) / (q^3)), ((-q^4 + 2*q^2 - 1) / (q^4)), ((1) / (q^2)), ((q^2 - 1) / (q^3)), (0)]

theorem wR_2_5_s7 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_5_v6 q) = wR_2_5_v7 q := by
  stepTac

@[simp] def wR_2_5_v8 (q : R) : Fin 6 → R := ![((q^4 - 3*q^2 + 2) / (q^3)), ((1 - q^2) / (q^2)), ((-q^4 + 2*q^2 - 1) / (q^5)), ((1) / (q^3)), ((-q^4 + 2*q^2 - 1) / (q^4)), ((q^2 - 1) / (q^3))]

theorem wR_2_5_s8 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_5_v7 q) = wR_2_5_v8 q := by
  stepTac

@[simp] def wR_2_5_v9 (q : R) : Fin 6 → R := ![((q^4 - 3*q^2 + 2) / (q^2)), ((-q^4 + 2*q^2 - 1) / (q^5)), ((-2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6)), ((-q^4 + 2*q^2 - 1) / (q^4)), ((-q^6 + 3*q^4 - 2*q^2 + 1) / (q^5)), ((q^2 - 1) / (q^2))]

theorem wR_2_5_s9 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_5_v8 q) = wR_2_5_v9 q := by
  stepTac

@[simp] def wR_2_5_v10 (q : R) : Fin 6 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^5)), ((q^4 - 3*q^2 + 2) / (q^2)), ((-2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^7)), ((-q^4 + 2*q^2 - 1) / (q^5)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6)), ((-q^6 + 3*q^4 - 2*q^2 + 1) / (q^5))]

theorem wR_2_5_s10 (q : R) (hq : q ≠ 0) :
    (g2_1i q).mulVec (wR_2_5_v9 q) = wR_2_5_v10 q := by
  stepTac

@[simp] def wR_2_5_v11 (q : R) : Fin 6 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / (q^4)), ((-2*q^6 + 4*q^4 - 3*q^2 + 1) / (q^7)), ((q^10 - 5*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^8)), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6)), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / (q^7)), ((-q^6 + 3*q^4 - 2*q^2 + 1) / (q^4))]

theorem wR_2_5_s11 (q : R) (hq : q ≠ 0) :
    (g2_2 q).mulVec (wR_2_5_v10 q) = wR_2_5_v11 q := by
  stepTac

theorem wR_2_5_entry (q : R) (hq : q ≠ 0) :
    word2 q wR 5 5 = ((-q^6 + 3*q^4 - 2*q^2 + 1) / (q^4)) := by
  rw [entry_eq_mulVec_single (word2 q wR) 5 5]
  simp only [wR, word2_mulVec_cons, word2_nil, Matrix.one_mulVec, gl2]
  rw [wR_2_5_s0 q hq, wR_2_5_s1 q hq, wR_2_5_s2 q hq, wR_2_5_s3 q hq, wR_2_5_s4 q hq, wR_2_5_s5 q hq, wR_2_5_s6 q hq, wR_2_5_s7 q hq, wR_2_5_s8 q hq, wR_2_5_s9 q hq, wR_2_5_s10 q hq, wR_2_5_s11 q hq]
  simp [wR_2_5_v11]

@[simp] def wR_3_0_v0 (q : R) : Fin 4 → R := ![((1) / (q)), (0), (0), (0)]

theorem wR_3_0_s0 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (Pi.single 0 1) = wR_3_0_v0 q := by
  stepTac

@[simp] def wR_3_0_v1 (q : R) : Fin 4 → R := ![((1) / (q^2)), (0), (0), (0)]

theorem wR_3_0_s1 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_0_v0 q) = wR_3_0_v1 q := by
  stepTac

@[simp] def wR_3_0_v2 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^3)), ((1) / (q^2)), (0), (0)]

theorem wR_3_0_s2 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wR_3_0_v1 q) = wR_3_0_v2 q := by
  stepTac

@[simp] def wR_3_0_v3 (q : R) : Fin 4 → R := ![((q^4 - q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), (0), (0)]

theorem wR_3_0_s3 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wR_3_0_v2 q) = wR_3_0_v3 q := by
  stepTac

@[simp] def wR_3_0_v4 (q : R) : Fin 4 → R := ![((q^4 - q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3)), (0)]

theorem wR_3_0_s4 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_0_v3 q) = wR_3_0_v4 q := by
  stepTac

@[simp] def wR_3_0_v5 (q : R) : Fin 4 → R := ![((q^4 - q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3))]

theorem wR_3_0_s5 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (wR_3_0_v4 q) = wR_3_0_v5 q := by
  stepTac

@[simp] def wR_3_0_v6 (q : R) : Fin 4 → R := ![((q^4 - q^2 + 1) / (q^7)), ((q^4 - 2*q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 1) / (q^5)), ((1 - q^2) / (q^4))]

theorem wR_3_0_s6 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_0_v5 q) = wR_3_0_v6 q := by
  stepTac

@[simp] def wR_3_0_v7 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^6)), ((q^4 - 2*q^2 + 2) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^4)), ((1 - q^2) / (q^3))]

theorem wR_3_0_s7 (q : R) (hq : q ≠ 0) :
    (g3_2 q).mulVec (wR_3_0_v6 q) = wR_3_0_v7 q := by
  stepTac

@[simp] def wR_3_0_v8 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^7)), ((q^4 - 3*q^2 + 2) / (q^6)), ((q^4 - 2*q^2 + 2) / (q^5)), ((1 - q^2) / (q^4))]

theorem wR_3_0_s8 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_0_v7 q) = wR_3_0_v8 q := by
  stepTac

@[simp] def wR_3_0_v9 (q : R) : Fin 4 → R := ![((q^4 - 3*q^2 + 2) / (q^6)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^7)), ((q^4 - 2*q^2 + 2) / (q^4)), ((1 - q^2) / (q^3))]

theorem wR_3_0_s9 (q : R) (hq : q ≠ 0) :
    (g3_2 q).mulVec (wR_3_0_v8 q) = wR_3_0_v9 q := by
  stepTac

@[simp] def wR_3_0_v10 (q : R) : Fin 4 → R := ![((q^4 - 3*q^2 + 2) / (q^7)), ((2*q^6 - 4*q^4 + 4*q^2 - 1) / (q^8)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^7)), ((1 - q^2) / (q^4))]

theorem wR_3_0_s10 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_0_v9 q) = wR_3_0_v10 q := by
  stepTac

@[simp] def wR_3_0_v11 (q : R) : Fin 4 → R := ![((2*q^6 - 4*q^4 + 4*q^2 - 1) / (q^8)), ((2*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 1) / (q^9)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^6)), ((1 - q^2) / (q^3))]

theorem wR_3_0_s11 (q : R) (hq : q ≠ 0) :
    (g3_2 q).mulVec (wR_3_0_v10 q) = wR_3_0_v11 q := by
  stepTac

theorem wR_3_0_entry (q : R) (hq : q ≠ 0) :
    word3 q wR 0 0 = ((2*q^6 - 4*q^4 + 4*q^2 - 1) / (q^8)) := by
  rw [entry_eq_mulVec_single (word3 q wR) 0 0]
  simp only [wR, word3_mulVec_cons, word3_nil, Matrix.one_mulVec, gl3]
  rw [wR_3_0_s0 q hq, wR_3_0_s1 q hq, wR_3_0_s2 q hq, wR_3_0_s3 q hq, wR_3_0_s4 q hq, wR_3_0_s5 q hq, wR_3_0_s6 q hq, wR_3_0_s7 q hq, wR_3_0_s8 q hq, wR_3_0_s9 q hq, wR_3_0_s10 q hq, wR_3_0_s11 q hq]
  simp [wR_3_0_v11]

@[simp] def wR_3_1_v0 (q : R) : Fin 4 → R := ![(0), ((1) / (q)), (0), (0)]

theorem wR_3_1_s0 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (Pi.single 1 1) = wR_3_1_v0 q := by
  stepTac

@[simp] def wR_3_1_v1 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / (q^2)), ((1) / (q)), (0)]

theorem wR_3_1_s1 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_1_v0 q) = wR_3_1_v1 q := by
  stepTac

@[simp] def wR_3_1_v2 (q : R) : Fin 4 → R := ![((1 - q^2) / (q^2)), (0), ((1) / (q^2)), (0)]

theorem wR_3_1_s2 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wR_3_1_v1 q) = wR_3_1_v2 q := by
  stepTac

@[simp] def wR_3_1_v3 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2)), ((1) / (q^3)), (0)]

theorem wR_3_1_s3 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wR_3_1_v2 q) = wR_3_1_v3 q := by
  stepTac

@[simp] def wR_3_1_v4 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((q^4 - 2*q^2 + 2) / (q^3)), ((1 - q^2) / (q^2)), (0)]

theorem wR_3_1_s4 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_1_v3 q) = wR_3_1_v4 q := by
  stepTac

@[simp] def wR_3_1_v5 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2))]

theorem wR_3_1_s5 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (wR_3_1_v4 q) = wR_3_1_v5 q := by
  stepTac

@[simp] def wR_3_1_v6 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^6)), ((q^4 - 3*q^2 + 2) / (q^5)), ((q^4 - 2*q^2 + 2) / (q^4)), ((1 - q^2) / (q^3))]

theorem wR_3_1_s6 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_1_v5 q) = wR_3_1_v6 q := by
  stepTac

@[simp] def wR_3_1_v7 (q : R) : Fin 4 → R := ![((q^4 - 3*q^2 + 2) / (q^5)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^6)), ((q^4 - 2*q^2 + 2) / (q^3)), ((1 - q^2) / (q^2))]

theorem wR_3_1_s7 (q : R) (hq : q ≠ 0) :
    (g3_2 q).mulVec (wR_3_1_v6 q) = wR_3_1_v7 q := by
  stepTac

@[simp] def wR_3_1_v8 (q : R) : Fin 4 → R := ![((q^4 - 3*q^2 + 2) / (q^6)), ((2*q^6 - 4*q^4 + 4*q^2 - 1) / (q^7)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^6)), ((1 - q^2) / (q^3))]

theorem wR_3_1_s8 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_1_v7 q) = wR_3_1_v8 q := by
  stepTac

@[simp] def wR_3_1_v9 (q : R) : Fin 4 → R := ![((2*q^6 - 4*q^4 + 4*q^2 - 1) / (q^7)), ((2*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 1) / (q^8)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^5)), ((1 - q^2) / (q^2))]

theorem wR_3_1_s9 (q : R) (hq : q ≠ 0) :
    (g3_2 q).mulVec (wR_3_1_v8 q) = wR_3_1_v9 q := by
  stepTac

@[simp] def wR_3_1_v10 (q : R) : Fin 4 → R := ![((2*q^6 - 4*q^4 + 4*q^2 - 1) / (q^8)), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / (q^9)), ((2*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 1) / (q^8)), ((1 - q^2) / (q^3))]

theorem wR_3_1_s10 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_1_v9 q) = wR_3_1_v10 q := by
  stepTac

@[simp] def wR_3_1_v11 (q : R) : Fin 4 → R := ![((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / (q^9)), ((-q^12 + 5*q^10 - 9*q^8 + 10*q^6 - 7*q^4 + 4*q^2 - 1) / (q^10)), ((2*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 1) / (q^7)), ((1 - q^2) / (q^2))]

theorem wR_3_1_s11 (q : R) (hq : q ≠ 0) :
    (g3_2 q).mulVec (wR_3_1_v10 q) = wR_3_1_v11 q := by
  stepTac

theorem wR_3_1_entry (q : R) (hq : q ≠ 0) :
    word3 q wR 1 1 = ((-q^12 + 5*q^10 - 9*q^8 + 10*q^6 - 7*q^4 + 4*q^2 - 1) / (q^10)) := by
  rw [entry_eq_mulVec_single (word3 q wR) 1 1]
  simp only [wR, word3_mulVec_cons, word3_nil, Matrix.one_mulVec, gl3]
  rw [wR_3_1_s0 q hq, wR_3_1_s1 q hq, wR_3_1_s2 q hq, wR_3_1_s3 q hq, wR_3_1_s4 q hq, wR_3_1_s5 q hq, wR_3_1_s6 q hq, wR_3_1_s7 q hq, wR_3_1_s8 q hq, wR_3_1_s9 q hq, wR_3_1_s10 q hq, wR_3_1_s11 q hq]
  simp [wR_3_1_v11]

@[simp] def wR_3_2_v0 (q : R) : Fin 4 → R := ![(0), (0), ((1 - q^2) / (q)), (1)]

theorem wR_3_2_s0 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (Pi.single 2 1) = wR_3_2_v0 q := by
  stepTac

@[simp] def wR_3_2_v1 (q : R) : Fin 4 → R := ![(0), ((1 - q^2) / (q)), (0), ((1) / (q))]

theorem wR_3_2_s1 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_2_v0 q) = wR_3_2_v1 q := by
  stepTac

@[simp] def wR_3_2_v2 (q : R) : Fin 4 → R := ![((1 - q^2) / (q)), (0), (0), ((1) / (q^2))]

theorem wR_3_2_s2 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wR_3_2_v1 q) = wR_3_2_v2 q := by
  stepTac

@[simp] def wR_3_2_v3 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^2)), ((1 - q^2) / (q)), (0), ((1) / (q^3))]

theorem wR_3_2_s3 (q : R) (hq : q ≠ 0) :
    (g3_2i q).mulVec (wR_3_2_v2 q) = wR_3_2_v3 q := by
  stepTac

@[simp] def wR_3_2_v4 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^3)), ((q^4 - 2*q^2 + 1) / (q^2)), ((1 - q^2) / (q)), ((1) / (q^4))]

theorem wR_3_2_s4 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_2_v3 q) = wR_3_2_v4 q := by
  stepTac

@[simp] def wR_3_2_v5 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((q^6 - 2*q^4 + q^2 + 1) / (q^4)), ((1 - q^2) / (q))]

theorem wR_3_2_s5 (q : R) (hq : q ≠ 0) :
    (g3_0i q).mulVec (wR_3_2_v4 q) = wR_3_2_v5 q := by
  stepTac

@[simp] def wR_3_2_v6 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 1) / (q^5)), ((q^4 - 2*q^2 + 2) / (q^4)), ((q^4 - 2*q^2 + 1) / (q^3)), ((1 - q^2) / (q^2))]

theorem wR_3_2_s6 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_2_v5 q) = wR_3_2_v6 q := by
  stepTac

@[simp] def wR_3_2_v7 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 2) / (q^4)), ((q^6 - 2*q^4 + 2*q^2 - 1) / (q^5)), ((q^4 - 2*q^2 + 1) / (q^2)), ((1 - q^2) / (q))]

theorem wR_3_2_s7 (q : R) (hq : q ≠ 0) :
    (g3_2 q).mulVec (wR_3_2_v6 q) = wR_3_2_v7 q := by
  stepTac

@[simp] def wR_3_2_v8 (q : R) : Fin 4 → R := ![((q^4 - 2*q^2 + 2) / (q^5)), ((q^6 - 3*q^4 + 3*q^2 - 1) / (q^6)), ((q^6 - 2*q^4 + 2*q^2 - 1) / (q^5)), ((1 - q^2) / (q^2))]

theorem wR_3_2_s8 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_2_v7 q) = wR_3_2_v8 q := by
  stepTac

@[simp] def wR_3_2_v9 (q : R) : Fin 4 → R := ![((q^6 - 3*q^4 + 3*q^2 - 1) / (q^6)), ((q^8 - 3*q^6 + 4*q^4 - 2*q^2 + 1) / (q^7)), ((q^6 - 2*q^4 + 2*q^2 - 1) / (q^4)), ((1 - q^2) / (q))]

theorem wR_3_2_s9 (q : R) (hq : q ≠ 0) :
    (g3_2 q).mulVec (wR_3_2_v8 q) = wR_3_2_v9 q := by
  stepTac

@[simp] def wR_3_2_v10 (q : R) : Fin 4 → R := ![((q^6 - 3*q^4 + 3*q^2 - 1) / (q^7)), ((2*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 1) / (q^8)), ((q^8 - 3*q^6 + 4*q^4 - 2*q^2 + 1) / (q^7)), ((1 - q^2) / (q^2))]

theorem wR_3_2_s10 (q : R) (hq : q ≠ 0) :
    (g3_1i q).mulVec (wR_3_2_v9 q) = wR_3_2_v10 q := by
  stepTac

@[simp] def wR_3_2_v11 (q : R) : Fin 4 → R := ![((2*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 1) / (q^8)), ((2*q^10 - 6*q^8 + 7*q^6 - 5*q^4 + 3*q^2 - 1) / (q^9)), ((q^8 - 3*q^6 + 4*q^4 - 2*q^2 + 1) / (q^6)), ((1 - q^2) / (q))]

theorem wR_3_2_s11 (q : R) (hq : q ≠ 0) :
    (g3_2 q).mulVec (wR_3_2_v10 q) = wR_3_2_v11 q := by
  stepTac

theorem wR_3_2_entry (q : R) (hq : q ≠ 0) :
    word3 q wR 2 2 = ((q^8 - 3*q^6 + 4*q^4 - 2*q^2 + 1) / (q^6)) := by
  rw [entry_eq_mulVec_single (word3 q wR) 2 2]
  simp only [wR, word3_mulVec_cons, word3_nil, Matrix.one_mulVec, gl3]
  rw [wR_3_2_s0 q hq, wR_3_2_s1 q hq, wR_3_2_s2 q hq, wR_3_2_s3 q hq, wR_3_2_s4 q hq, wR_3_2_s5 q hq, wR_3_2_s6 q hq, wR_3_2_s7 q hq, wR_3_2_s8 q hq, wR_3_2_s9 q hq, wR_3_2_s10 q hq, wR_3_2_s11 q hq]
  simp [wR_3_2_v11]

theorem wL_tp (q : R) (hq : q ≠ 0) :
    tpL q (word1 q wL) (word3 q wL) (word2 q wL) = ((-q^16 + 3*q^14 - 3*q^12 + 7*q^10 - 6*q^8 + 7*q^6 - 3*q^4 + 3*q^2 - 1) / (q^10)) := by
  simp only [tpL, wL_2_0_entry q hq, wL_2_1_entry q hq, wL_2_3_entry q hq, wL_3_1_entry q hq, wL_3_2_entry q hq, wL_3_3_entry q hq]
  field_simp <;> ring

/-- The ruled split `ε = (tp − tn)/[2]⁴` on `wL`, using `left_ratio`. -/
theorem wL_eps (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (tpL q (word1 q wL) (word3 q wL) (word2 q wL) - tnL q (word1 q wL) (word3 q wL) (word2 q wL)) / (q + q⁻¹) ^ 4 = ((-q^18 + 4*q^16 - 6*q^14 + 10*q^12 - 13*q^10 + 13*q^8 - 10*q^6 + 6*q^4 - 4*q^2 + 1) / (q^8*(q^2 + 1)^4)) := by
  rw [left_ratio q hq h2, wL_tp q hq]
  have : q + q⁻¹ ≠ 0 := by
    intro h0
    apply h2
    have e : q * (q + q⁻¹) = q ^ 2 + 1 := by rw [mul_add, mul_inv_cancel₀ hq]; ring
    rw [← e, h0, mul_zero]
  field_simp <;> ring

theorem wAL_tp (q : R) (hq : q ≠ 0) :
    tpL q (word1 q wAL) (word3 q wAL) (word2 q wAL) = ((-q^16 + 3*q^14 - 4*q^12 + 8*q^10 - 6*q^8 + 8*q^6 - 4*q^4 + 3*q^2 - 1) / (q^8)) := by
  simp only [tpL, wAL_2_0_entry q hq, wAL_2_1_entry q hq, wAL_2_3_entry q hq, wAL_3_1_entry q hq, wAL_3_2_entry q hq, wAL_3_3_entry q hq]
  field_simp <;> ring

/-- The ruled split `ε = (tp − tn)/[2]⁴` on `wAL`, using `left_ratio`. -/
theorem wAL_eps (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (tpL q (word1 q wAL) (word3 q wAL) (word2 q wAL) - tnL q (word1 q wAL) (word3 q wAL) (word2 q wAL)) / (q + q⁻¹) ^ 4 = ((-q^18 + 4*q^16 - 7*q^14 + 12*q^12 - 14*q^10 + 14*q^8 - 12*q^6 + 7*q^4 - 4*q^2 + 1) / (q^6*(q^2 + 1)^4)) := by
  rw [left_ratio q hq h2, wAL_tp q hq]
  have : q + q⁻¹ ≠ 0 := by
    intro h0
    apply h2
    have e : q * (q + q⁻¹) = q ^ 2 + 1 := by rw [mul_add, mul_inv_cancel₀ hq]; ring
    rw [← e, h0, mul_zero]
  field_simp <;> ring

theorem wR_tp (q : R) (hq : q ≠ 0) :
    tpR q (word1 q wR) (word3 q wR) (word2 q wR) = ((-q^12 + 5*q^10 - 6*q^8 + 9*q^6 - 5*q^4 + 6*q^2 - 2) / (q^8)) := by
  simp only [tpR, wR_1_1_entry q hq, wR_1_2_entry q hq, wR_1_3_entry q hq, wR_2_0_entry q hq, wR_2_1_entry q hq, wR_2_2_entry q hq, wR_2_3_entry q hq, wR_2_4_entry q hq, wR_2_5_entry q hq, wR_3_0_entry q hq, wR_3_1_entry q hq, wR_3_2_entry q hq]
  field_simp <;> ring

theorem wR_tn (q : R) (hq : q ≠ 0) :
    tnR q (word1 q wR) (word3 q wR) (word2 q wR) = ((-q^18 + 4*q^16 - 6*q^14 + 9*q^12 - 8*q^10 + 7*q^8 - q^6 + q^4 + 2*q^2 - 1) / (q^12)) := by
  simp only [tnR, wR_1_1_entry q hq, wR_1_2_entry q hq, wR_1_3_entry q hq, wR_2_0_entry q hq, wR_2_1_entry q hq, wR_2_2_entry q hq, wR_2_3_entry q hq, wR_2_4_entry q hq, wR_2_5_entry q hq, wR_3_0_entry q hq, wR_3_1_entry q hq, wR_3_2_entry q hq]
  field_simp <;> ring

/-- **Right placement breaks the ratio:** the defect `E_n − q⁻²E_p`, of order `h²`. -/
theorem wR_defect (q : R) (hq : q ≠ 0) :
    tnR q (word1 q wR) (word3 q wR) (word2 q wR) - q⁻¹ ^ 2 * tpR q (word1 q wR) (word3 q wR) (word2 q wR) = ((-q^18 + 4*q^16 - 5*q^14 + 4*q^12 - 2*q^10 - 2*q^8 + 4*q^6 - 5*q^4 + 4*q^2 - 1) / (q^12)) := by
  rw [wR_tp q hq, wR_tn q hq]
  field_simp <;> ring

end QOU.QBeta.HydrogenFlavourSplit

#print axioms QOU.QBeta.HydrogenFlavourSplit.left_ratio
#print axioms QOU.QBeta.HydrogenFlavourSplit.wL_eps
#print axioms QOU.QBeta.HydrogenFlavourSplit.wAL_eps
#print axioms QOU.QBeta.HydrogenFlavourSplit.wR_defect
