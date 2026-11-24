/-
# State-weighted reading 3: can the γγ selection tell the neutron from the proton?

Bean `qou-99qc` (Q_β derived, not chosen), `qou-ales` (γγ + reading-3 word selection).
Owner 2026-11-20: derive `n` and `p` as distinct γγ-selected elements instead of the
typed-crossing definition `Δ_S = 𝓑_n − 𝓑_p`.

The ruled reading 3 (`χ_λ(w) ≥ 0` on every block with `y_λ > 0`) takes no state argument,
so it selects the same word for every nucleon by definition. The only place a nucleon
label can enter is a **state-weighted** reading 3: positivity of `tr(Π^λ_s ρ_s(w))` on the
`H₃`-isotypic components of the nucleon's own weight space `s`. This file proves what that
reading can and cannot see.

## Part A — three strands (scope b)

`W_n` (basis `udd, dud, ddu`) and `W_p` (basis `duu, udu, uud`) are the `T³ = ∓½` weight
spaces of `V^{⊗3}` under the Jimbo `Ř` (the matrices of `IsospinRaisingRoundTrip.lean`,
#8632). The upper unitriangular `D = [[1, h, qh], [0, 1, h], [0, 0, 1]]`, `h = q − q⁻¹`,
intertwines them: `D σᵢ|_{W_n} = σᵢ|_{W_p} D` (`D_s1`, `D_s2`), it is invertible over any
commutative ring (`D_mul_Dinv`, `Dinv_mul_D`), and it carries the `(3)`-isotypic projector
of `W_n` to that of `W_p` (`D_Pi3`). Hence for **every** word in `σ₁^{±1}, σ₂^{±1}` the two
isotypic characters agree (`isoChar_eq`), and the state-weighted feasibility predicate is
the same for `n` and `p` (`feasible_iff`). This is the invariant behind #8616's
`trace_ρn_eq_trace_ρp`, extended from plain traces to isotypic traces.

## Part B — four strands, strand 4 a lepton line (named choice C-lep)

On the `T³ = 0` space of `V^{⊗4}`, `N = n ⊗ ν` (strand 4 = `u`) and `P = p ⊗ e` (strand
4 = `d`) are `H₃`-stable, with the Part-A matrices. The letter `σ₃` maps `N` to `P`; its
diagonal compressions are `diag(h, h, q)` on `N` and `diag(0, 0, q)` on `P`
(`compN3`, `compP3`; the compressions are computed and checked against the full 16-dim
`Ř`-action in `n2_state_weighted_selection_probe.py`, not derived in this file).
The γγ word `V₁V₂ = σ₁σ₂⁻¹·σ₂σ₃⁻¹ = σ₁σ₃⁻¹` has, on the two states, the isotypic characters
`charN3`, `charN21`, `charP3`, `charP21` below. They differ (`stateDiff_21`): the
isospin-`½` difference is `−(q²−1)(2q⁴+q²+1)/(q²(q⁴+q²+1))`, first order in `q − 1`.
Yet over an ordered field with `1 < q`, the `N` characters are positive, and the `P`
`(3)`-character is non-negative exactly when `q⁶ − q² − 1 ≤ 0` (`charP3_nonneg_iff`). So the
word is feasible for both states below `q* = √ρ` (`ρ` the plastic number), and for `n`
only above it. The proton pin `q₀ ≈ 1.10998` lies below `q* ≈ 1.15096`.

## Scope

Model statements. `C-lep` (strand 4 is a lepton doublet on the same `V`) and the
state-weighted reading are named choices, not rulings. Nothing empirical enters.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [humphreys1990] §7.4 (Hecke algebra; Wedderburn decomposition for generic q)
-- Ref: [jimbo1986] (the R-matrix of U_q(gl_2) and q-Schur–Weyl duality)
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.QuarkState.NucleonStateWeighted

open Matrix

local macro "mat3" : tactic =>
  `(tactic| (ext i j <;> fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> (try field_simp) <;> ring))

section Generic

variable {K : Type*} [Field K]

/-- `h = q − q⁻¹`. -/
def hh (q : K) : K := q - q⁻¹

/-- `σ₁` on `W_n` (basis `udd, dud, ddu`). -/
def sm1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, 0; 1, q - q⁻¹, 0; 0, 0, q]
/-- `σ₂` on `W_n`. -/
def sm2 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, 0, 1; 0, 1, q - q⁻¹]
/-- `σ₁` on `W_p` (basis `duu, udu, uud`). -/
def sp1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q - q⁻¹, 1, 0; 1, 0, 0; 0, 0, q]
/-- `σ₂` on `W_p`. -/
def sp2 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, q - q⁻¹, 1; 0, 1, 0]

/-- The intertwiner `W_n → W_p`: upper unitriangular. -/
def D (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![1, q - q⁻¹, q * (q - q⁻¹); 0, 1, q - q⁻¹; 0, 0, 1]
/-- Its inverse. -/
def Dinv (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![1, -(q - q⁻¹), (q - q⁻¹) ^ 2 - q * (q - q⁻¹); 0, 1, -(q - q⁻¹); 0, 0, 1]

/-- `(3)`-isotypic projector on `W_n`: `v vᵀ / (q⁴+q²+1)`, `v = (1, q, q²)`. -/
def Pi3N (q : K) : Matrix (Fin 3) (Fin 3) K :=
  (q ^ 4 + q ^ 2 + 1)⁻¹ • !![1, q, q ^ 2; q, q ^ 2, q ^ 3; q ^ 2, q ^ 3, q ^ 4]
/-- `(3)`-isotypic projector on `W_p`: `w wᵀ / (q⁴+q²+1)`, `w = (q², q, 1)`. -/
def Pi3P (q : K) : Matrix (Fin 3) (Fin 3) K :=
  (q ^ 4 + q ^ 2 + 1)⁻¹ • !![q ^ 4, q ^ 3, q ^ 2; q ^ 3, q ^ 2, q; q ^ 2, q, 1]

/-- The two isotypic blocks present in a nucleon weight space. -/
inductive Block | triv | half
  deriving DecidableEq

/-- Isotypic projector of a block on `W_n` / `W_p` (`(2,1)` is the complement of `(3)`). -/
def PiN (q : K) : Block → Matrix (Fin 3) (Fin 3) K
  | .triv => Pi3N q
  | .half => 1 - Pi3N q
/-- See `PiN`. -/
def PiP (q : K) : Block → Matrix (Fin 3) (Fin 3) K
  | .triv => Pi3P q
  | .half => 1 - Pi3P q

/-- A three-strand letter. -/
inductive Letter | s1 | s2 | s1i | s2i
  deriving DecidableEq

/-- The letter on `W_n` (`σ⁻¹ = σ − h`). -/
def onN (q : K) : Letter → Matrix (Fin 3) (Fin 3) K
  | .s1 => sm1 q
  | .s2 => sm2 q
  | .s1i => sm1 q - (q - q⁻¹) • 1
  | .s2i => sm2 q - (q - q⁻¹) • 1
/-- The letter on `W_p`. -/
def onP (q : K) : Letter → Matrix (Fin 3) (Fin 3) K
  | .s1 => sp1 q
  | .s2 => sp2 q
  | .s1i => sp1 q - (q - q⁻¹) • 1
  | .s2i => sp2 q - (q - q⁻¹) • 1

/-- A word acts on `W_n` / `W_p` as the ordered product of its letters. -/
def wordN (q : K) (w : List Letter) : Matrix (Fin 3) (Fin 3) K := (w.map (onN q)).prod
/-- See `wordN`. -/
def wordP (q : K) (w : List Letter) : Matrix (Fin 3) (Fin 3) K := (w.map (onP q)).prod

/-- State-weighted isotypic character `tr(Π^λ ρ(w))`. -/
def isoCharN (q : K) (b : Block) (w : List Letter) : K := trace (PiN q b * wordN q w)
/-- See `isoCharN`. -/
def isoCharP (q : K) (b : Block) (w : List Letter) : K := trace (PiP q b * wordP q w)

variable {q : K} (hq : q ≠ 0)
include hq

/-! ### Part A -/

theorem D_mul_Dinv : D q * Dinv q = 1 := by unfold D Dinv; mat3
theorem Dinv_mul_D : Dinv q * D q = 1 := by unfold D Dinv; mat3

/-- `D` intertwines `σ₁`. -/
theorem D_s1 : D q * sm1 q = sp1 q * D q := by unfold D sm1 sp1; mat3
/-- `D` intertwines `σ₂`. -/
theorem D_s2 : D q * sm2 q = sp2 q * D q := by unfold D sm2 sp2; mat3

/-- `D` intertwines every letter. -/
theorem D_letter (l : Letter) : D q * onN q l = onP q l * D q := by
  cases l
  · exact D_s1 hq
  · exact D_s2 hq
  · simp only [onN, onP, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_smul, Matrix.smul_mul,
      Matrix.mul_one, Matrix.one_mul, D_s1 hq]
  · simp only [onN, onP, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_smul, Matrix.smul_mul,
      Matrix.mul_one, Matrix.one_mul, D_s2 hq]

/-- `D` intertwines every word. -/
theorem D_word (w : List Letter) : D q * wordN q w = wordP q w * D q := by
  induction w with
  | nil => simp [wordN, wordP]
  | cons l w ih =>
    simp only [wordN, wordP, List.map_cons, List.prod_cons] at ih ⊢
    rw [← Matrix.mul_assoc, D_letter hq l, Matrix.mul_assoc, ih, Matrix.mul_assoc]

theorem D_Pi3 (hD : q ^ 4 + q ^ 2 + 1 ≠ 0) : D q * Pi3N q = Pi3P q * D q := by
  unfold D Pi3N Pi3P
  ext i j <;> fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem D_Pi (hD : q ^ 4 + q ^ 2 + 1 ≠ 0) (b : Block) : D q * PiN q b = PiP q b * D q := by
  cases b
  · exact D_Pi3 hq hD
  · simp only [PiN, PiP, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_one, Matrix.one_mul,
      D_Pi3 hq hD]

/-- **The state-weighted isotypic characters of every three-strand word are equal on the
neutron and the proton weight spaces.** -/
theorem isoChar_eq (hD : q ^ 4 + q ^ 2 + 1 ≠ 0) (b : Block) (w : List Letter) :
    isoCharN q b w = isoCharP q b w := by
  unfold isoCharN isoCharP
  have key : PiP q b * wordP q w = D q * (PiN q b * wordN q w) * Dinv q := by
    calc PiP q b * wordP q w = PiP q b * wordP q w * (D q * Dinv q) := by
          rw [D_mul_Dinv hq, Matrix.mul_one]
      _ = PiP q b * (wordP q w * D q) * Dinv q := by simp only [Matrix.mul_assoc]
      _ = PiP q b * (D q * wordN q w) * Dinv q := by rw [D_word hq w]
      _ = (PiP q b * D q) * wordN q w * Dinv q := by simp only [Matrix.mul_assoc]
      _ = D q * PiN q b * wordN q w * Dinv q := by rw [D_Pi hq hD b]
      _ = D q * (PiN q b * wordN q w) * Dinv q := by simp only [Matrix.mul_assoc]
  rw [key, Matrix.trace_mul_cycle, ← Matrix.mul_assoc, Dinv_mul_D hq, Matrix.one_mul]

/-! ### Part B: the four-strand quark–lepton letter `σ₃` -/

/-- Diagonal compression of `σ₃⁻¹ = σ₃ − h` to `N` (`σ₃|_N = diag(h, h, q)`). -/
def compN3i (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 0, 0; 0, 0, 0; 0, 0, q⁻¹]
/-- Diagonal compression of `σ₃⁻¹` to `P` (`σ₃|_P = diag(0, 0, q)`). -/
def compP3i (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![-(q - q⁻¹), 0, 0; 0, -(q - q⁻¹), 0; 0, 0, q⁻¹]

/-- `σ₃|_N − h = compN3i`. -/
theorem compN3 : !![q - q⁻¹, 0, 0; 0, q - q⁻¹, 0; 0, 0, q] - (q - q⁻¹) • (1 : Matrix (Fin 3) (Fin 3) K)
    = compN3i q := by unfold compN3i; mat3
/-- `σ₃|_P − h = compP3i`. -/
theorem compP3 : !![0, 0, 0; 0, 0, 0; 0, 0, q] - (q - q⁻¹) • (1 : Matrix (Fin 3) (Fin 3) K)
    = compP3i q := by unfold compP3i; mat3

/-- `V₁V₂ = σ₁σ₃⁻¹` compressed to `N` (σ₁ preserves `N`). -/
def wN (q : K) : Matrix (Fin 3) (Fin 3) K := sm1 q * compN3i q
/-- `V₁V₂ = σ₁σ₃⁻¹` compressed to `P`. -/
def wP (q : K) : Matrix (Fin 3) (Fin 3) K := sp1 q * compP3i q

variable (hD : q ^ 4 + q ^ 2 + 1 ≠ 0)
include hD

theorem charN3 : trace (Pi3N q * wN q) = q ^ 4 / (q ^ 4 + q ^ 2 + 1) := by
  simp [Matrix.trace_fin_three, Pi3N, wN, sm1, compN3i, Matrix.mul_apply, Fin.sum_univ_three, hD]
  have hD' : 1 + q ^ 2 + q ^ 4 ≠ 0 := by
    rwa [show (1 : K) + q ^ 2 + q ^ 4 = q ^ 4 + q ^ 2 + 1 by ring]
  field_simp <;> ring

theorem traceWN : trace (wN q) = 1 := by
  simp [Matrix.trace_fin_three, wN, sm1, compN3i, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp

theorem charN21 : trace ((1 - Pi3N q) * wN q) = (q ^ 2 + 1) / (q ^ 4 + q ^ 2 + 1) := by
  rw [Matrix.sub_mul, Matrix.one_mul, Matrix.trace_sub, traceWN hq hD, charN3 hq hD, one_sub_div hD]
  congr 1; ring

theorem charP3 : trace (Pi3P q * wP q) = -(q ^ 6 - q ^ 2 - 1) / (q ^ 4 + q ^ 2 + 1) := by
  simp [Matrix.trace_fin_three, Pi3P, wP, sp1, compP3i, Matrix.mul_apply, Fin.sum_univ_three, hD]
  have hD' : 1 + q ^ 2 + q ^ 4 ≠ 0 := by
    rwa [show (1 : K) + q ^ 2 + q ^ 4 = q ^ 4 + q ^ 2 + 1 by ring]
  field_simp <;> ring

theorem traceWP : trace (wP q) = (3 * q ^ 2 - q ^ 4 - 1) / q ^ 2 := by
  simp [Matrix.trace_fin_three, wP, sp1, compP3i, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; ring

theorem charP21 :
    trace ((1 - Pi3P q) * wP q) = (2 * q ^ 6 + q ^ 2 - 1) / (q ^ 2 * (q ^ 4 + q ^ 2 + 1)) := by
  rw [Matrix.sub_mul, Matrix.one_mul, Matrix.trace_sub, traceWP hq hD, charP3 hq hD,
    div_sub_div _ _ (pow_ne_zero 2 hq) hD,
    div_eq_div_iff (mul_ne_zero (pow_ne_zero 2 hq) hD) (mul_ne_zero (pow_ne_zero 2 hq) hD)]
  ring

/-- **The isospin-`½` state difference of the selected word**, first order in `q² − 1`. -/
theorem stateDiff_21 :
    trace ((1 - Pi3N q) * wN q) - trace ((1 - Pi3P q) * wP q)
      = -((q ^ 2 - 1) * (2 * q ^ 4 + q ^ 2 + 1)) / (q ^ 2 * (q ^ 4 + q ^ 2 + 1)) := by
  rw [charN21 hq hD, charP21 hq hD]; field_simp; ring

/-- The `(3)` state difference of the selected word. -/
theorem stateDiff_3 :
    trace (Pi3N q * wN q) - trace (Pi3P q * wP q)
      = (q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (q ^ 4 + q ^ 2 + 1) := by
  rw [charN3 hq hD, charP3 hq hD]; field_simp; ring

end Generic

/-! ### The feasibility threshold (ordered field) -/

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

theorem D4_pos (q : K) : 0 < q ^ 4 + q ^ 2 + 1 := by positivity

/-- **State-weighted feasibility of a three-strand word is the same for `n` and `p`.** -/
theorem feasible_iff {q : K} (hq : q ≠ 0) (w : List Letter) :
    (∀ b, 0 ≤ isoCharN q b w) ↔ (∀ b, 0 ≤ isoCharP q b w) := by
  have hD := (D4_pos q).ne'
  simp only [isoChar_eq hq hD]

/-- On `N` both characters of `σ₁σ₃⁻¹` are positive for every `q > 0`. -/
theorem charN_pos {q : K} (hq : 0 < q) :
    0 < trace (Pi3N q * wN q) ∧ 0 < trace ((1 - Pi3N q) * wN q) := by
  have hD := (D4_pos q).ne'
  rw [charN3 hq.ne' hD, charN21 hq.ne' hD]
  exact ⟨by positivity, by positivity⟩

/-- On `P` the `(3)`-character of `σ₁σ₃⁻¹` is non-negative exactly when `q⁶ ≤ q² + 1`. -/
theorem charP3_nonneg_iff {q : K} (hq : 0 < q) :
    0 ≤ trace (Pi3P q * wP q) ↔ q ^ 6 - q ^ 2 - 1 ≤ 0 := by
  have hD := D4_pos q
  rw [charP3 hq.ne' hD.ne', neg_div, neg_nonneg, div_nonpos_iff]
  constructor
  · rintro (⟨_, h⟩ | ⟨h1, h2⟩)
    · exact absurd h (not_le.mpr hD)
    · exact h1
  · intro h; exact Or.inr ⟨h, hD.le⟩

/-- On `P` the `(2,1)`-character of `σ₁σ₃⁻¹` is positive for `q ≥ 1`. -/
theorem charP21_pos {q : K} (hq : 1 ≤ q) : 0 < trace ((1 - Pi3P q) * wP q) := by
  have hq0 : 0 < q := lt_of_lt_of_le one_pos hq
  have hD := D4_pos q
  rw [charP21 hq0.ne' hD.ne']
  have : 0 < 2 * q ^ 6 + q ^ 2 - 1 := by
    have h1 : 1 ≤ q ^ 2 := one_le_pow₀ hq
    nlinarith [pow_pos hq0 6, one_le_pow₀ (n := 6) hq]
  exact div_pos this (by positivity)

end Ordered

end QOU.QuarkState.NucleonStateWeighted
