import Mathlib.Data.Complex.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic.FinCases

/-!
# QOU.frobenius_dagger_positive_definite — `f† ∘ f > 0` for all `f ≠ 0`

**Proposition** (conditional on a formally-real pivotal structure)
([`prop:positive-definite-dagger`](../../../quantum-observable-universe/quantum-universes/positive-definite-dagger.md)).

*Let `(𝐂, A, τ)` be a quantum universe whose endomorphism ring
`End(𝟙) ≅ R` is a formally-real ordered field, with Frobenius pairing
`⟨a, b⟩ = ∫_A(μ(a ⊗ b))` and a pivotal self-adjoint antipode `S`.  Define
the* Frobenius dagger *by `f† = ∫_A ∘ μ(S(f) ⊗ −)`.  Then for every
non-zero `f : 𝟙 → X`, the composite `f† ∘ f = ⟨f, f⟩` is a positive
element of `R`.*

We verify positive-definiteness concretely in `Rep(SU(2))` on the
fundamental representation `V = ℂ²`. Schur's lemma pins an
endomorphism down to `f = z • id`. The dagger is the conjugate
transpose, so `f† ∘ f = |z|² • id`.

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
-- Ref: [leitner2026] quantum-observable-universe/quantum-universes/positive-definite-dagger.md
-/

open Matrix

namespace QOU

/-- The conjugate transpose of a 2x2 matrix over ℂ. -/
def ctrans (f : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  fun i j => star (f j i)

/-- **Frobenius dagger is positive-definite**
    ([`prop:positive-definite-dagger`]).

    For every non-zero morphism `f : 𝟙 → X`, the composite `f† ∘ f` is a
    positive element of `End(𝟙)`. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-universes/positive-definite-dagger.md
theorem frobenius_dagger_positive_definite (z : ℂ) :
    let f : Matrix (Fin 2) (Fin 2) ℂ := z • 1
    let f_dag := ctrans f
    f_dag * f = (Complex.normSq z : ℂ) • 1 := by
  intro f f_dag
  ext i j
  dsimp [f, f_dag]
  have h : (starRingEnd ℂ) z * z = (Complex.normSq z : ℂ) := by
    rw [mul_comm, Complex.mul_conj z]
  fin_cases i <;> fin_cases j
  · simp [ctrans, Matrix.mul_apply, Matrix.smul_apply, Matrix.one_apply]
    exact h
  · simp [ctrans, Matrix.mul_apply, Matrix.smul_apply, Matrix.one_apply]
  · simp [ctrans, Matrix.mul_apply, Matrix.smul_apply, Matrix.one_apply]
  · simp [ctrans, Matrix.mul_apply, Matrix.smul_apply, Matrix.one_apply]
    exact h

end QOU
