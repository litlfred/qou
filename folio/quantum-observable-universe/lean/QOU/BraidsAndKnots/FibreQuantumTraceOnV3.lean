/-
# The quantum trace of the two-dimensional fibre action on `V^{⊗3}`, computed

Bean `qou-n1dj`. `FibreCategoricalTraceForcesJones` reduces the D-vs-C question
for the mass channel to one named premise, `MassTraceIsFibreCategorical`: *the
mass-channel trace is the categorical trace of the fibre action on `V^{⊗3}`*.
That file never constructs such a trace; its witness `fibreCategoricalJones`
**posits** the Jones weights `(1 − 2t², t², 0)` and checks them against the
Markov equations.

This file **builds the trace** and derives the weights from it, with no posited
weight vector:

* `rCheck` — the braiding `Ř` on `V ⊗ V`, `V = R²`, in the paper's §7a
  normalisation (eigenvalues `q` and `−q⁻¹`). `rCheck_hecke`: it satisfies the
  Hecke relation `Ř² = (q − q⁻¹)Ř + 1`.
* `sigma1 = Ř ⊗ 1`, `sigma2 = 1 ⊗ Ř` on `V^{⊗3}` (`Fin 2 × Fin 2 × Fin 2`).
  `sigma_braid`: the braid relation `σ₁σ₂σ₁ = σ₂σ₁σ₂`, and `sigma1_hecke` /
  `sigma2_hecke`: the Hecke relation — so this is a genuine representation of
  `H₃(q)` on the fibre cube.
* `fibreTrace` — the quantum (pivotal) trace `τ(M) = [2]_q⁻³ · Tr(K^{⊗3} M)`,
  pivot `K = diag(q⁻¹, q)`. `pivot_comm_sigma1/2` and `fibreTrace_mul_comm`: on
  the commutant of `K^{⊗3}` (which contains the image of `H₃(q)`) `τ` is a trace.
* `fibreTrace_one`, `fibreTrace_sigma1`, `fibreTrace_sigma1_sigma2`: computed
  values `1`, `z`, `z²` with `z = q − t = q²t`, `t = [2]_q⁻¹`.
* `fibreTrace_weights_eq_jones`: **any** Frobenius weight vector
  `(y₃, y₂₁, y₁₃)` reproducing those three values against the `H₃(q)`
  `q`-character table on `1, σ₁, σ₁σ₂` has `y₁₃ = 0`, `[2]_q² y₂₁ = 1`,
  `y₃ = 1 − 2y₂₁` — i.e. it is the Jones / convention-D vector. The vanishing of
  the alternating weight is **computed from the fibre action**, not taken from
  the row cap.
* `exists_unique_fibreTrace_categorical`: packaged — there is a
  `MassTraceIsFibreCategorical R 2` whose weights reproduce the fibre quantum
  trace, and every weight vector that does so equals its weights.

## What this does NOT establish (read before citing)

* **It does not identify the mass channel's trace with `fibreTrace`.** The class
  `MassTraceIsFibreCategorical` has no field referring to any particular trace,
  so no instance of it can certify "this is the mass trace"; it is in fact
  inhabited by constants. What remains open in `qou-n1dj` is the
  *identification* "mass-channel trace = quantum trace of the fundamental
  `U_q(𝔰𝔩₂)` action on `V^{⊗3}`" — which the corpus states as a definition
  (`feynman-markov-identification`) rather than proves. This file discharges
  the premise **for `fibreTrace`**, not for the mass channel.
* **Weights are matched on the three class representatives only.** That `τ ∘ ρ`
  is a linear combination of the irreducible characters of `H₃(q)` (split
  semisimplicity) is not formalised here; the theorem is: *if* a weight vector
  reproduces `τ` on `1, σ₁, σ₁σ₂`, it is the Jones vector — and that such a
  vector exists.
* Non-degeneracy hypothesis `(q + qi)² − 1 ≠ 0`, i.e. `[3]_q ≠ 0` — the root of
  unity at which `TL₃` degenerates; inherited from
  `threeRow_eq_zero_of_jones_ocneanu`.

## Base ring (§7c)

Generic `{R : Type*} [CommRing R]`, `[IsDomain R]` only for the weight
uniqueness. `q⁻¹` and `[2]_q⁻¹` are carried as elements `qi`, `t` constrained by
`q * qi = 1`, `(q + qi) * t = 1`; everything is division-free. No `ℝ`, no
ordering, no numerical `q₀`.
-/
import Mathlib.Data.Fin.VecNotation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination
import QOU.BraidsAndKnots.FibreCategoricalTraceForcesJones
import QOU.BraidsAndKnots.FibreDimensionForcesTL

namespace QOU.BraidsAndKnots.FibreQuantumTraceOnV3

open Matrix

variable {R : Type*} [CommRing R]

/-- Entries `Ř_{(a,b),(c,d)}` of the braiding on `V ⊗ V` (row `(a,b)`, column
`(c,d)`): `Ř e₀e₀ = q e₀e₀`, `Ř e₀e₁ = (q − q⁻¹) e₀e₁ + e₁e₀`, `Ř e₁e₀ = e₀e₁`,
`Ř e₁e₁ = q e₁e₁`. -/
def rEnt (q qi : R) : Fin 2 → Fin 2 → Fin 2 → Fin 2 → R :=
  ![![![![q, 0], ![0, 0]], ![![0, q - qi], ![1, 0]]],
    ![![![0, 1], ![0, 0]], ![![0, 0], ![0, q]]]]

/-- The braiding `Ř` on `V ⊗ V`, `V = R²`. -/
def rCheck (q qi : R) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R :=
  Matrix.of fun x y => rEnt q qi x.1 x.2 y.1 y.2

/-- `Ř` satisfies the Hecke relation `(Ř − q)(Ř + q⁻¹) = 0`. -/
theorem rCheck_hecke (q qi : R) (hqi : q * qi = 1) :
    rCheck q qi * rCheck q qi = (q - qi) • rCheck q qi + 1 := by
  ext ⟨a, b⟩ ⟨c, d⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [rCheck, rEnt, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two] <;>
    first | ring1 | linear_combination hqi


/-- `σ₁ = Ř ⊗ 1` on `V^{⊗3}`. -/
def sigma1 (q qi : R) : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  Matrix.of fun x y => rEnt q qi x.1 x.2.1 y.1 y.2.1 * (if x.2.2 = y.2.2 then 1 else 0)

/-- `σ₂ = 1 ⊗ Ř` on `V^{⊗3}`. -/
def sigma2 (q qi : R) : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  Matrix.of fun x y => (if x.1 = y.1 then 1 else 0) * rEnt q qi x.2.1 x.2.2 y.2.1 y.2.2

/-- Pivotal element on one tensor factor: `K = diag(q⁻¹, q)`. -/
def kappa (q qi : R) : Fin 2 → R := ![qi, q]

/-- The pivot `K^{⊗3}` on `V^{⊗3}`, as a diagonal matrix. -/
def pivot (q qi : R) : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  Matrix.diagonal fun x => kappa q qi x.1 * kappa q qi x.2.1 * kappa q qi x.2.2

/-- The normalised quantum trace on `V^{⊗3}`: `τ(M) = t³ · Tr(K^{⊗3} M)`, with
`t = [2]_q⁻¹` so that `τ(1) = 1`. -/
def fibreTrace (q qi t : R)
    (M : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R) : R :=
  t ^ 3 * Matrix.trace (pivot q qi * M)

/-- `τ(1) = 1`. -/
theorem fibreTrace_one (q qi t : R) (h2 : (q + qi) * t = 1) :
    fibreTrace q qi t 1 = 1 := by
  unfold fibreTrace
  simp [pivot, kappa, Matrix.trace, Fintype.sum_prod_type, Fin.sum_univ_two]
  linear_combination (((q + qi) * t) ^ 2 + (q + qi) * t + 1) * h2

/-- `τ(σ₁) = z` with `z = q − t` (equivalently `z·[2]_q = q²`, convention D). -/
theorem fibreTrace_sigma1 (q qi t : R) (hqi : q * qi = 1) (h2 : (q + qi) * t = 1) :
    fibreTrace q qi t (sigma1 q qi) = q - t := by
  unfold fibreTrace
  simp [pivot, kappa, sigma1, rEnt, Matrix.trace, Fintype.sum_prod_type, Fin.sum_univ_two]
  linear_combination t * (q ^ 2 * t ^ 2 + q * qi * t ^ 2 - q * t - 1) * hqi
    + q * (q ^ 2 * t ^ 2 + q * t + t ^ 2 + 1) * h2

/-- `τ(σ₁σ₂) = z²` — the Markov property, computed. -/
theorem fibreTrace_sigma1_sigma2 (q qi t : R) (hqi : q * qi = 1) (h2 : (q + qi) * t = 1) :
    fibreTrace q qi t (sigma1 q qi * sigma2 q qi) = (q - t) ^ 2 := by
  unfold fibreTrace
  simp [pivot, kappa, sigma1, sigma2, rEnt, Matrix.trace, Matrix.mul_apply,
    Fintype.sum_prod_type, Fin.sum_univ_two]
  linear_combination (-t * (q ^ 2 * t + q - t)) * hqi
    + q * (q ^ 3 * t ^ 2 + q ^ 2 * t + q - t) * h2


-- 64 explicit entry cases of an 8 × 8 matrix identity; evaluation only, no search.
set_option maxHeartbeats 4000000 in
/-- The braid relation `σ₁σ₂σ₁ = σ₂σ₁σ₂` on `V^{⊗3}`. -/
theorem sigma_braid (q qi : R) (hqi : q * qi = 1) :
    sigma1 q qi * sigma2 q qi * sigma1 q qi = sigma2 q qi * sigma1 q qi * sigma2 q qi := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;>
    fin_cases c' <;>
    simp [sigma1, sigma2, rEnt, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two] <;>
    first | ring1 | linear_combination (q - qi) * hqi | linear_combination -(q - qi) * hqi

-- 64 explicit entry cases of an 8 × 8 matrix identity; evaluation only, no search.
set_option maxHeartbeats 4000000 in
/-- The Hecke relation for `σ₁` on `V^{⊗3}`. -/
theorem sigma1_hecke (q qi : R) (hqi : q * qi = 1) :
    sigma1 q qi * sigma1 q qi = (q - qi) • sigma1 q qi + 1 := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;>
    fin_cases c' <;>
    simp [sigma1, rEnt, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two] <;>
    first | ring1 | linear_combination hqi

-- 64 explicit entry cases of an 8 × 8 matrix identity; evaluation only, no search.
set_option maxHeartbeats 4000000 in
/-- The Hecke relation for `σ₂` on `V^{⊗3}`. -/
theorem sigma2_hecke (q qi : R) (hqi : q * qi = 1) :
    sigma2 q qi * sigma2 q qi = (q - qi) • sigma2 q qi + 1 := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;>
    fin_cases c' <;>
    simp [sigma2, rEnt, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two] <;>
    first | ring1 | linear_combination hqi

/-- `σ₁` preserves weight, so it commutes with the pivot. -/
theorem pivot_comm_sigma1 (q qi : R) :
    pivot q qi * sigma1 q qi = sigma1 q qi * pivot q qi := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;>
    fin_cases c' <;>
    simp [pivot, sigma1, rEnt, kappa, Matrix.diagonal_mul, Matrix.mul_diagonal] <;> ring1

/-- `σ₂` preserves weight, so it commutes with the pivot. -/
theorem pivot_comm_sigma2 (q qi : R) :
    pivot q qi * sigma2 q qi = sigma2 q qi * pivot q qi := by
  ext ⟨a, b, c⟩ ⟨a', b', c'⟩
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases a' <;> fin_cases b' <;>
    fin_cases c' <;>
    simp [pivot, sigma2, rEnt, kappa, Matrix.diagonal_mul, Matrix.mul_diagonal] <;> ring1

/-- **`τ` is a trace on the commutant of the pivot** — in particular on the
image of `H₃(q)` (generated by `σ₁, σ₂`, both in the commutant). -/
theorem fibreTrace_mul_comm (q qi t : R)
    (M N : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R)
    (hM : pivot q qi * M = M * pivot q qi) :
    fibreTrace q qi t (M * N) = fibreTrace q qi t (N * M) := by
  unfold fibreTrace
  congr 1
  calc Matrix.trace (pivot q qi * (M * N))
      = Matrix.trace ((M * pivot q qi) * N) := by rw [← Matrix.mul_assoc, hM]
    _ = Matrix.trace (M * (pivot q qi * N)) := by rw [Matrix.mul_assoc]
    _ = Matrix.trace ((pivot q qi * N) * M) := Matrix.trace_mul_comm _ _
    _ = Matrix.trace (pivot q qi * (N * M)) := by rw [Matrix.mul_assoc]


/-- **The Frobenius weights of the fibre quantum trace are the Jones weights.**

Any `(y₃, y₂₁, y₁₃)` whose pairing with the `H₃(q)` `q`-character table on
`1, σ₁, σ₁σ₂` reproduces `τ` there has `y₁₃ = 0`, `[2]_q² y₂₁ = 1`,
`y₃ = 1 − 2 y₂₁`. The vanishing of the alternating weight is derived from the
computed values of `τ` (via `threeRow_eq_zero_of_jones_ocneanu`), not assumed. -/
theorem fibreTrace_weights_eq_jones [IsDomain R] (q qi t y₃ y₂₁ y₁₃ : R)
    (hqi : q * qi = 1) (h2 : (q + qi) * t = 1)
    (h3ne : (q + qi) ^ 2 - 1 ≠ 0)
    (h0 : y₃ + 2 * y₂₁ + y₁₃ = fibreTrace q qi t 1)
    (h1 : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = fibreTrace q qi t (sigma1 q qi))
    (h12 : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ =
      fibreTrace q qi t (sigma1 q qi * sigma2 q qi)) :
    y₁₃ = 0 ∧ (q + qi) ^ 2 * y₂₁ = 1 ∧ y₃ = 1 - 2 * y₂₁ := by
  rw [fibreTrace_one q qi t h2] at h0
  rw [fibreTrace_sigma1 q qi t hqi h2] at h1
  rw [fibreTrace_sigma1_sigma2 q qi t hqi h2] at h12
  have hb2ne : q + qi ≠ 0 := by
    intro h
    rw [h, zero_mul] at h2
    exact zero_ne_one h2
  have hzD : (q - t) * (q + qi) = q ^ 2 := by linear_combination hqi - h2
  have hA : y₁₃ = 0 :=
    threeRow_eq_zero_of_jones_ocneanu q qi (q - t) y₃ y₂₁ y₁₃ hqi h0 h1 h12 hzD hb2ne h3ne
  refine ⟨hA, ?_, ?_⟩
  · linear_combination (q + qi) * (q * h0 - h1) - (q + qi) ^ 2 * hA + h2
  · linear_combination h0 - hA

/-- The Jones-weight witness `fibreCategoricalJones` reproduces the fibre quantum
trace on the three class representatives. -/
theorem fibreCategoricalJones_moments_eq_fibreTrace [Nontrivial R] (q qi t : R)
    (hqi : q * qi = 1) (h2 : (q + qi) * t = 1) :
    (fibreCategoricalJones q qi t hqi h2).weightSym
        + 2 * (fibreCategoricalJones q qi t hqi h2).weightMixed
        + (fibreCategoricalJones q qi t hqi h2).weightAlt = fibreTrace q qi t 1
      ∧ q * (fibreCategoricalJones q qi t hqi h2).weightSym
          + (q - qi) * (fibreCategoricalJones q qi t hqi h2).weightMixed
          + (-qi) * (fibreCategoricalJones q qi t hqi h2).weightAlt
          = fibreTrace q qi t (sigma1 q qi)
      ∧ q ^ 2 * (fibreCategoricalJones q qi t hqi h2).weightSym
          + (-1) * (fibreCategoricalJones q qi t hqi h2).weightMixed
          + qi ^ 2 * (fibreCategoricalJones q qi t hqi h2).weightAlt
          = fibreTrace q qi t (sigma1 q qi * sigma2 q qi) := by
  rw [fibreTrace_one q qi t h2, fibreTrace_sigma1 q qi t hqi h2,
    fibreTrace_sigma1_sigma2 q qi t hqi h2]
  refine ⟨?_, ?_, ?_⟩
  · show (1 - 2 * t ^ 2) + 2 * t ^ 2 + (0 : R) = 1
    ring
  · show q * (1 - 2 * t ^ 2) + (q - qi) * t ^ 2 + (-qi) * (0 : R) = q - t
    linear_combination (-t) * h2
  · show q ^ 2 * (1 - 2 * t ^ 2) + (-1) * t ^ 2 + qi ^ 2 * (0 : R) = (q - t) ^ 2
    linear_combination (-2 * q * t) * h2 + 2 * t ^ 2 * hqi

/-- **The premise holds for the fibre quantum trace, with uniquely determined
weights.** There is a `MassTraceIsFibreCategorical R 2` whose Frobenius weights
reproduce `fibreTrace` on `1, σ₁, σ₁σ₂`, and any weight vector that reproduces
`fibreTrace` there equals its weights.

Scope: this is a statement about `fibreTrace`, the quantum trace of the
two-dimensional fibre action. That the **mass channel's** trace is `fibreTrace`
is not proved here (bean `qou-n1dj`). -/
theorem exists_unique_fibreTrace_categorical [IsDomain R] (q qi t : R)
    (hqi : q * qi = 1) (h2 : (q + qi) * t = 1) (h3ne : (q + qi) ^ 2 - 1 ≠ 0) :
    ∃ ctx : MassTraceIsFibreCategorical R 2,
      (ctx.weightSym + 2 * ctx.weightMixed + ctx.weightAlt = fibreTrace q qi t 1
        ∧ q * ctx.weightSym + (q - qi) * ctx.weightMixed + (-qi) * ctx.weightAlt
            = fibreTrace q qi t (sigma1 q qi)
        ∧ q ^ 2 * ctx.weightSym + (-1) * ctx.weightMixed + qi ^ 2 * ctx.weightAlt
            = fibreTrace q qi t (sigma1 q qi * sigma2 q qi))
      ∧ ∀ y₃ y₂₁ y₁₃ : R,
          y₃ + 2 * y₂₁ + y₁₃ = fibreTrace q qi t 1 →
          q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = fibreTrace q qi t (sigma1 q qi) →
          q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃
              = fibreTrace q qi t (sigma1 q qi * sigma2 q qi) →
          y₃ = ctx.weightSym ∧ y₂₁ = ctx.weightMixed ∧ y₁₃ = ctx.weightAlt := by
  refine ⟨fibreCategoricalJones q qi t hqi h2,
    fibreCategoricalJones_moments_eq_fibreTrace q qi t hqi h2, ?_⟩
  intro y₃ y₂₁ y₁₃ h0 h1 h12
  obtain ⟨hA, hM, hS⟩ := fibreTrace_weights_eq_jones q qi t y₃ y₂₁ y₁₃ hqi h2 h3ne h0 h1 h12
  have hM' : y₂₁ = t ^ 2 := by
    linear_combination t ^ 2 * hM - ((q + qi) * t + 1) * y₂₁ * h2
  refine ⟨?_, hM', hA⟩
  show y₃ = 1 - 2 * t ^ 2
  rw [hS, hM']

end QOU.BraidsAndKnots.FibreQuantumTraceOnV3
