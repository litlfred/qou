import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# QOU.BraidKnot.KnotOperatorRecurrence — knot operators give recurrences via the Gram form

The algebraic content of the observation that a **knot operator** which is a power of a
fixed braiding element gives a **linear recurrence** for the associated knot invariants,
with the **Gram matrix of the Markov pairing** the tool that diagonalises it.

Setting: the two-strand Temperley–Lieb module `TL₂ = span{1, e}` (`e² = δ·e`, `δ` the loop
value), on which the Kauffman braiding acts as `σ = A·1 + A⁻¹·e`. The twist region of a
**twist knot** is `σ²` — a `2×2` operator. Two structural facts, proved sorry-free over a
generic commutative ring:

* **Cayley–Hamilton (`charpoly_two`)** — every `2×2` matrix `M` satisfies
  `M·M = (tr M)·M − (det M)·1`. Hence (`pow_two_step`) the powers obey the two-term
  recurrence `Mⁿ⁺² = t·Mⁿ⁺¹ − d·Mⁿ` whenever `M·M = t·M − d·1`, and applying the Markov
  trace / closure — a *linear* functional — carries it to the knot invariants
  (`trace_two_step`): `tr(Mⁿ⁺²) = t·tr(Mⁿ⁺¹) − d·tr(Mⁿ)`. This is the twist-knot
  Jones-polynomial recurrence in its cleanest generic form; the coefficients `t = tr M`,
  `d = det M` are the elementary symmetric functions of the two operator eigen-channels.
* **Gram self-adjointness (`twist_gram_selfAdjoint`)** — with the Markov-pairing Gram
  matrix `G = !![δ, 1; 1, δ]` (`⟨a,b⟩ = tr_M(ab)` on `{1,e}`), the twist operator is
  `G`-self-adjoint (`G · σ² = (G · σ²)ᵀ`). This is exactly why the recurrence diagonalises:
  the knot operator is self-adjoint in the Gram inner product, so `G⁻¹` builds the dual /
  Jones–Wenzl projector basis on which `σ²` is diagonal (eigen-channels `A²`, `A⁻⁶`).

Consequence (recorded in the companion audit, not Lean): a finite-dimensional module ⇒
Cayley–Hamilton ⇒ a `q`-holonomic recurrence — the **quantum A-polynomial / AJ** structure.
The knot-operator + Gram-inverse machinery therefore *computes* the even/geometric-channel
`q`-holonomic recurrences; the bar-odd `Q_β` D-ladder's proven **non-**`q`-holonomicity
(KC22) is precisely the statement that it escapes this machinery.

Generic `CommRing` (§7c); `A`, `δ` are formal ring elements (no archimedean input).
-/

namespace QOU.BraidKnot.KnotOperatorRecurrence

open Matrix

variable {R : Type*} [CommRing R]

/-- **2×2 Cayley–Hamilton.** Every `2×2` matrix satisfies its characteristic polynomial:
`M·M = (M₀₀+M₁₁)·M − (M₀₀M₁₁ − M₀₁M₁₀)·1` — trace and determinant as the recurrence
coefficients. -/
theorem charpoly_two (M : Matrix (Fin 2) (Fin 2) R) :
    M * M = (M 0 0 + M 1 1) • M - (M 0 0 * M 1 1 - M 0 1 * M 1 0) • (1 : Matrix (Fin 2) (Fin 2) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.sub_apply,
      Matrix.smul_apply] <;> ring

/-- **Power recurrence.** If a knot operator `M` satisfies the quadratic relation
`M·M = t·M − d·1` (its `2×2` Cayley–Hamilton), then its powers obey the two-term linear
recurrence `Mⁿ⁺² = t·Mⁿ⁺¹ − d·Mⁿ`. -/
theorem pow_two_step {M : Matrix (Fin 2) (Fin 2) R} {t d : R}
    (h : M * M = t • M - d • (1 : Matrix (Fin 2) (Fin 2) R)) (n : ℕ) :
    M ^ (n + 2) = t • M ^ (n + 1) - d • M ^ n := by
  have hp : M ^ (n + 2) = M ^ n * (M * M) := by
    rw [pow_add, pow_two]
  rw [hp, h, mul_sub, mul_smul_comm, mul_smul_comm, mul_one, ← pow_succ]

/-- **Closure / Markov-trace recurrence.** Applying the (linear) trace — the closure of the
tangle, i.e. the knot invariant — to `pow_two_step` gives the invariant's two-term
recurrence: `tr(Mⁿ⁺²) = t·tr(Mⁿ⁺¹) − d·tr(Mⁿ)`. This is the twist-knot Jones-polynomial
recurrence. -/
theorem trace_two_step {M : Matrix (Fin 2) (Fin 2) R} {t d : R}
    (h : M * M = t • M - d • (1 : Matrix (Fin 2) (Fin 2) R)) (n : ℕ) :
    (M ^ (n + 2)).trace = t * (M ^ (n + 1)).trace - d * (M ^ n).trace := by
  rw [pow_two_step h, Matrix.trace_sub, Matrix.trace_smul, Matrix.trace_smul,
    smul_eq_mul, smul_eq_mul]

section Twist

variable (A δ : R)

/-- The Temperley–Lieb cup-cap generator `e` on `{1, e}` (left multiplication), `e² = δe`. -/
def eGen : Matrix (Fin 2) (Fin 2) R := !![0, 0; 1, δ]

/-- The Kauffman braiding `σ = A·1 + u·e` (here the inverse strand weight is the ring
element `u`, so the statement stays over a generic commutative ring rather than a field). -/
def braid (u : R) : Matrix (Fin 2) (Fin 2) R := A • (1 : Matrix (Fin 2) (Fin 2) R) + u • eGen δ

/-- The **twist operator** `σ²` — one full clasp twist, the knot operator of the twist-knot
family. -/
def twist (u : R) : Matrix (Fin 2) (Fin 2) R := braid A δ u * braid A δ u

/-- The Markov-pairing **Gram matrix** on `{1, e}`: `G = !![δ, 1; 1, δ]`
(`⟨1,1⟩ = tr_M 1 = δ`, `⟨1,e⟩ = tr_M e = 1`, `⟨e,e⟩ = tr_M(δe) = δ`). Symmetric. -/
def gram : Matrix (Fin 2) (Fin 2) R := !![δ, 1; 1, δ]

/-- **The twist knot operator is Gram-self-adjoint.** `G · σ²` is symmetric — its two
off-diagonal entries agree, `(G·σ²)₀₁ = (G·σ²)₁₀` — so `σ²` is self-adjoint in the Markov
inner product. This is the fact that makes the recurrence diagonalise: `G⁻¹` builds the
dual / Jones–Wenzl projector basis on which `σ²` is diagonal. -/
theorem twist_gram_selfAdjoint (u : R) :
    (gram δ * twist A δ u) 0 1 = (gram δ * twist A δ u) 1 0 := by
  simp [gram, twist, braid, eGen, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply,
    Matrix.add_apply, Matrix.smul_apply]
  ring

end Twist

end QOU.BraidKnot.KnotOperatorRecurrence
