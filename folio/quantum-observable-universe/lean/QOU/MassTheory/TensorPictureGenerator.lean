import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# The tensor-picture Hecke generator is a transposition plus a diagonal part

Bean `qou-qqm4`. Probes: `computations/probes/tensor_picture_markov_trace_probe.py`,
`computations/probes/c2_diagonal_insertion_expansion_probe.py`.

On `ℂ² ⊗ ℂ²` with basis `(e₁₁, e₁₂, e₂₁, e₂₂)` the `U_q(sl₂)` R-matrix in Hecke
normalisation is

    Ř(q) = ⎡ q  0  0  0 ⎤
           ⎢ 0  0  1  0 ⎥        h = q − q⁻¹
           ⎢ 0  1  h  0 ⎥
           ⎣ 0  0  0  q ⎦

Three facts about it carry the whole insertion-expansion derivation of the
trace coefficients `c₀, c₁, c₂, …`:

1. **`Ř = s + D(q)`** with `s` the swap and `D(q) = diag(q−1, 0, h, q−1)`
   diagonal and vanishing at `q = 1` (`rHecke_eq_swap_add_diag`,
   `diagPart_one`). This is what makes the trace of a braid word, at every
   order in `ε = q − 1`, a fixed-point count over sub-words.
2. **The Hecke relation** `(Ř − q)(Ř + q⁻¹) = 0` (`rHecke_hecke_relation`), so
   `Ř` represents the generator `σ_i` of `H_n(q)` in the corpus's convention
   (§7a: eigenvalues `q` and `−q⁻¹`).
3. **The quantum trace of one generator is the convention-D loop value:**
   `Tr(K Ř) = q³(1 + q²)` with `K = diag(1, q², q², q⁴)`, so
   `Tr(K Ř)/(1+q²)² = q³/(q²+1) = z_D` (`qtrace_rHecke`, `qtrace_rHecke_div`).
   This pins the R-matrix normalisation to the Markov trace the corpus uses
   without any reference to the seminormal form.

Also recorded: the swap squares to the identity, and the first- and
second-order coefficients of `D(1+ε)` are the `Y = diag(0, −1, 1, 0)` and
`W = diag(0, 0, −1, 0)` the probes read off — here as exact identities in
`ε` rather than as series.

Everything is over a generic field `K` (§7c); no `ℝ`, no numerics.

-- Ref: [leitner2026] bean qou-qqm4
-/

namespace QOU.MassTheory

open Matrix

variable {K : Type*} [Field K]

/-- The swap on `ℂ² ⊗ ℂ²` in the basis `(e₁₁, e₁₂, e₂₁, e₂₂)`. -/
def swap4 : Matrix (Fin 4) (Fin 4) K :=
  !![1, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, 0, 0;
     0, 0, 0, 1]

/-- The diagonal part `D(q) = diag(q−1, 0, q−q⁻¹, q−1)`. -/
def diagPart (q : K) : Matrix (Fin 4) (Fin 4) K :=
  diagonal ![q - 1, 0, q - q⁻¹, q - 1]

/-- The R-matrix in Hecke normalisation. -/
def rHecke (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, q - q⁻¹, 0;
     0, 0, 0, q]

/-- The pivotal weight `K = diag(1, q², q², q⁴)` on the pair. -/
def pivotal (q : K) : Matrix (Fin 4) (Fin 4) K :=
  diagonal ![1, q ^ 2, q ^ 2, q ^ 4]

/-- **Fact 1.** `Ř = s + D(q)`. -/
theorem rHecke_eq_swap_add_diag (q : K) : rHecke q = swap4 + diagPart q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rHecke, swap4, diagPart]

/-- The diagonal part vanishes at `q = 1`. -/
theorem diagPart_one : diagPart (1 : K) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [diagPart]

/-- The swap is an involution. -/
theorem swap4_mul_swap4 : (swap4 : Matrix (Fin 4) (Fin 4) K) * swap4 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [swap4, Matrix.mul_apply, Fin.sum_univ_four]

/-- **Fact 2.** The Hecke relation `(Ř − q)(Ř + q⁻¹) = 0`. -/
theorem rHecke_hecke_relation (q : K) (hq : q ≠ 0) :
    (rHecke q - q • (1 : Matrix (Fin 4) (Fin 4) K)) * (rHecke q + q⁻¹ • 1) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rHecke, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;>
    field_simp <;> ring

/-- **Fact 3.** `Tr(K Ř) = q³(1 + q²)`. -/
theorem qtrace_rHecke (q : K) (hq : q ≠ 0) :
    trace (pivotal q * rHecke q) = q ^ 3 * (1 + q ^ 2) := by
  simp [trace, pivotal, rHecke, Matrix.mul_apply, Fin.sum_univ_four, diagonal_apply]
  field_simp
  ring

/-- Hence the quantum trace of one generator, normalised by `Tr K = (1+q²)²`,
is the convention-D loop value `z_D = q³/(q²+1)`. -/
theorem qtrace_rHecke_div (q : K) (hq : q ≠ 0) (h1 : 1 + q ^ 2 ≠ 0) :
    trace (pivotal q * rHecke q) / (1 + q ^ 2) ^ 2 = q ^ 3 / (1 + q ^ 2) := by
  rw [qtrace_rHecke q hq, sq (1 + q ^ 2), mul_div_mul_right _ _ h1]

/-- `Tr K = (1 + q²)²`: the two-site normaliser. -/
theorem trace_pivotal (q : K) : trace (pivotal q) = (1 + q ^ 2) ^ 2 := by
  simp [trace, pivotal, Fin.sum_univ_four]
  ring

/-! ### The first two orders of `D(1 + ε)`, as exact identities -/

/-- `q − 1 = ε` and `q − q⁻¹ = 2ε − ε² + ε³/(1+ε)`: the diagonal part at
`q = 1 + ε` is `ε·diag(1, 0, 2, 1) + ε²·diag(0, 0, −1, 0) + ε³·diag(0, 0, 1/(1+ε), 0)`.
So `X = 1 + Y` with `Y = diag(0, −1, 1, 0)` and `W = diag(0, 0, −1, 0)`, exactly. -/
theorem diagPart_one_add (ε : K) (hε : 1 + ε ≠ 0) :
    diagPart (1 + ε)
      = ε • diagonal ![1, 0, 2, 1] + ε ^ 2 • diagonal ![0, 0, -1, 0]
        + ε ^ 3 • diagonal ![0, 0, (1 + ε)⁻¹, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [diagPart]
  field_simp
  ring

/-- The first-order term minus the identity is `Y = diag(0, −1, 1, 0)`, and `Y`
anticommutes with the swap — the concrete instance of
`LeadingOrderTraceCoefficient.hecke_first_order_anticommutes`. -/
theorem swap4_mul_Y_anticomm :
    (swap4 : Matrix (Fin 4) (Fin 4) K) * diagonal ![0, -1, 1, 0]
      = -(diagonal ![0, -1, 1, 0] * swap4) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [swap4, Matrix.mul_apply, diagonal_apply]

/-- `Y` is traceless against the pivotal weight at `q = 1` — the two-site form of
`Tr(Y·P) = 0`, which the probes use for every permutation. -/
theorem trace_Y : trace (diagonal ![0, -1, 1, 0] : Matrix (Fin 4) (Fin 4) K) = 0 := by
  simp [trace, Fin.sum_univ_four]

end QOU.MassTheory
