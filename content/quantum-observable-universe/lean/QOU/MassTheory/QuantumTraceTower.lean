/-
# QOU.MassTheory.QuantumTraceTower — the ∀n weighted quantum trace (qou-v7ro, instance brick 2)

Brick 1 (`QOU.MassTheory.TemperleyLiebSpinHalf`) gave the concrete 2-strand TL relations. This
brick supplies the two **dimension-general** facts about the weighted quantum trace that identity
(I) of the ∀A Milnor deficit proof rests on:

* **Kronecker multiplicativity** `qtr_{D₁⊗D₂}(X₁⊗X₂) = qtr_{D₁}(X₁)·qtr_{D₂}(X₂)` — the algebraic
  content of "disjoint strand blocks factor", and what makes `qtr(W e W⁻¹) = qtr(e)` and the
  juxtaposition terms work at every strand count.
* **The loop tower** `qtr(1) = [2]^n` on `n` strands — the free-strand factor `[2]^{n}` / `[2]^{n-1}`
  in identity (I).

The quantum trace is `qtr D X = tr(D·X)` with `D` the μ-weight (`μ = diag(q, 1/q)`). Two models:
the abstract Kronecker model (any index types) for multiplicativity, and the explicit
`Fin n → Fin 2` spin-configuration model (diagonal weight) for the `[2]^n` tower, which avoids a
reindexed Kronecker power. Everything is over a generic field (§7c); sorry-free.

Scope: this is brick 2. The Brunnian word `ρ(w_n)` as a concrete operator, the `e_{n-1}` embedding
`qtr(e_{n-1}) = [2]^{n-1}`, and the composing induction are brick 3+ (Mathlib has no knot theory).
-/
import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace

namespace QOU.MassTheory.QuantumTraceTower

open Matrix
open scoped Kronecker

variable {K : Type*} [Field K]

/-- Weighted quantum trace `qtr D X = tr(D · X)`; `D` is the diagonal μ-weight. -/
def qtr {a : Type*} [Fintype a] [DecidableEq a] (D X : Matrix a a K) : K := (D * X).trace

/-- `qtr D 1 = tr D`. -/
theorem qtr_one {a : Type*} [Fintype a] [DecidableEq a] (D : Matrix a a K) :
    qtr D 1 = D.trace := by
  simp [qtr]

/-- **Kronecker multiplicativity of the quantum trace.** Disjoint strand blocks factor:
`qtr_{D₁⊗D₂}(X₁⊗X₂) = qtr_{D₁}(X₁)·qtr_{D₂}(X₂)`. -/
theorem qtr_kron {a b : Type*} [Fintype a] [DecidableEq a] [Fintype b] [DecidableEq b]
    (D₁ X₁ : Matrix a a K) (D₂ X₂ : Matrix b b K) :
    qtr (D₁ ⊗ₖ D₂) (X₁ ⊗ₖ X₂) = qtr D₁ X₁ * qtr D₂ X₂ := by
  unfold qtr
  rw [← Matrix.mul_kronecker_mul, Matrix.trace_kronecker]

/-- The weight factorises on the identity: `qtr_{D₁⊗D₂}(1) = qtr_{D₁}(1)·qtr_{D₂}(1)`. -/
theorem qtr_kron_one {a b : Type*} [Fintype a] [DecidableEq a] [Fintype b] [DecidableEq b]
    (D₁ : Matrix a a K) (D₂ : Matrix b b K) :
    qtr (D₁ ⊗ₖ D₂) 1 = qtr D₁ 1 * qtr D₂ 1 := by
  rw [← Matrix.one_kronecker_one (α := K), qtr_kron]

/-- The diagonal μ-weight on one strand: `μ = diag(q, 1/q)` as a function `Fin 2 → K`. -/
def muDiag (q : K) : Fin 2 → K := ![q, 1/q]

/-- The sum of the μ-weights over one strand is `[2] = q + 1/q`. -/
theorem sum_muDiag (q : K) : (∑ b : Fin 2, muDiag q b) = q + 1/q := by
  rw [Fin.sum_univ_two]; simp [muDiag]

/-- Diagonal quantum trace on `n` strands: `qtrDiag X = ∑_f (∏ i μ(f i))·X_{f,f}`, indexed by the
spin configurations `f : Fin n → Fin 2`. -/
def qtrDiag (q : K) {n : ℕ} (X : Matrix (Fin n → Fin 2) (Fin n → Fin 2) K) : K :=
  ∑ f : Fin n → Fin 2, (∏ i, muDiag q (f i)) * X f f

/-- **The loop tower: `qtr(1) = [2]^n`.** The free-strand factor at every `n`. -/
theorem qtrDiag_one (q : K) (n : ℕ) :
    qtrDiag q (1 : Matrix (Fin n → Fin 2) (Fin n → Fin 2) K) = (q + 1/q) ^ n := by
  unfold qtrDiag
  simp only [Matrix.one_apply_eq, mul_one]
  have h : (∑ f : Fin n → Fin 2, ∏ i, muDiag q (f i))
      = ∏ _i : Fin n, (∑ b : Fin 2, muDiag q b) := by
    rw [Finset.prod_univ_sum, Fintype.piFinset_univ]
  rw [h, Finset.prod_const, Finset.card_univ, Fintype.card_fin, sum_muDiag]

end QOU.MassTheory.QuantumTraceTower
