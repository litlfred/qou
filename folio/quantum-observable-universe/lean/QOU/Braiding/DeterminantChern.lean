import QOU.Braiding.CrossingAdditiveWrithe
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.GeneralLinearGroup.Defs

/-!
# The first Chern class of a braid representation is its determinant exponent

For a representation of the braid group with conjugate generators, every
abelian character — in particular the determinant — factors through the writhe:
`χ(β) = χ(σ)^{w(β)}`. So `log_q |det ρ(β)| = c₁(ρ) · w(β)` with
`det ρ(σ) = ± q^{c₁(ρ)}`. This is the crossing-additive `c · w` form that
`CrossingAdditiveWrithe` shows every additive braid invariant has.

For the adjoint `X ↦ g X g⁻¹`, written as the Kronecker matrix `g ⊗ (g⁻¹)ᵀ`,
the determinant is `1` for every invertible `g`. So `c₁(Ad ρ) = 0` holds for
every representation and constrains nothing. This replaces the withdrawn
QUO-3a of `prop:vertex-algebra-relations`, which used a trace instead.

Checked against exact seminormal representations of `H_n(q)`, `n = 2..5`, where
`c₁(V_λ) = χ^λ(transposition)` (project file `qou-crossing-energy/result-c1.md`).
That identification is computed, not proved here. Bean `qou-078y`.
-/

namespace QOU.Braiding.DeterminantChern

open QOU.Braiding.CrossingAdditive

section Words

variable {G : Type*} [Group G] {n : ℕ}

/-- Evaluate a signed braid word with generator images `g`. -/
def evalWord (g : Fin n → G) (w : List (Letter n)) : G :=
  (w.map fun l => if l.2 then g l.1 else (g l.1)⁻¹).prod

/-- **An abelian character of a braid representation is `D ^ writhe`** when every
generator has the same character value `D` (as for conjugate generators). -/
theorem character_evalWord {M : Type*} [CommGroup M] (χ : G →* M) (g : Fin n → G)
    (D : M) (hD : ∀ i, χ (g i) = D) (w : List (Letter n)) :
    χ (evalWord g w) = D ^ writhe w := by
  induction w with
  | nil => simp [evalWord, writhe]
  | cons l w ih =>
    obtain ⟨i, b⟩ := l
    have h1 : evalWord g ((i, b) :: w)
        = (if b then g i else (g i)⁻¹) * evalWord g w := by simp [evalWord]
    have h2 : writhe ((i, b) :: w) = (if b then (1 : ℤ) else -1) + writhe w := by
      simp [writhe]
    rw [h1, h2, map_mul, ih, zpow_add]
    cases b <;> simp [hD]

/-- The determinant case: `det ρ(β) = det ρ(σ)^{w(β)}`. -/
theorem det_evalWord {m R : Type*} [Fintype m] [DecidableEq m] [CommRing R]
    (g : Fin n → GL m R) (D : Rˣ) (hD : ∀ i, Matrix.GeneralLinearGroup.det (g i) = D)
    (w : List (Letter n)) :
    Matrix.GeneralLinearGroup.det (evalWord g w) = D ^ writhe w :=
  character_evalWord _ g D hD w

end Words

section Adjoint

variable {m K : Type*} [Fintype m] [DecidableEq m] [Field K]

/-- **`c₁(Ad) = 0`.** The conjugation `X ↦ A X A⁻¹`, as the Kronecker matrix
`A ⊗ (A⁻¹)ᵀ`, has determinant `1` for every invertible `A`. -/
theorem det_kronecker_inv_transpose (A : Matrix m m K) (hA : A.det ≠ 0) :
    (Matrix.kroneckerMap (· * ·) A (A⁻¹).transpose).det = 1 := by
  rw [Matrix.det_kronecker, Matrix.det_transpose, Matrix.det_nonsing_inv,
    Ring.inverse_eq_inv', ← mul_pow, mul_inv_cancel₀ hA, one_pow]

end Adjoint

end QOU.Braiding.DeterminantChern
