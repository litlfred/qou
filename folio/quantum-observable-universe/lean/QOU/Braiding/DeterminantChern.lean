import QOU.Braiding.CrossingAdditiveWrithe
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.GeneralLinearGroup.Defs
import Mathlib.Algebra.BigOperators.Field

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

section MarkovAverage

variable {R : Type*} [Field R] {ι : Type*}

/-- **The eigenvalue split of a Hecke generator's trace.** If `σ` acts with
eigenvalue `q` on an `m₊`-dimensional subspace and `−q⁻¹` on an
`m₋`-dimensional one, its trace is `f·(q − q⁻¹)/2 + c₁·(q + q⁻¹)/2` with
`f = m₊ + m₋` (the dimension) and `c₁ = m₊ − m₋` (the determinant exponent).
This is the crossing-energy split `E = ℓ·b + w·a`, with `ℓ ↔ f` and `w ↔ c₁`. -/
theorem eigen_trace_split (h2 : (2 : R) ≠ 0) (q mp mm : R) :
    mp * q + mm * (-q⁻¹)
      = (mp + mm) * ((q - q⁻¹) / 2) + (mp - mm) * ((q + q⁻¹) / 2) := by
  field_simp
  ring

/-- **The Markov average of `c₁`.** Let a trace decompose as `Σ_k y_k χ_k` with
`Σ_k y_k f_k = tr(1) = 1` and `Σ_k y_k χ_k(σ) = tr(σ) = z`, and let each
`χ_k(σ) = f_k·h/2 + c_k·[2]/2`. Then `Σ_k y_k c_k = (2z − h)/[2]`.
The inputs are the Markov normalisations, which hold for every `n`; so the
average does not depend on `n`. At `z = q³/(q²+1)` this is `(q⁴+1)/(q²+1)²`. -/
theorem markov_average_c1 (s : Finset ι) (y f c χ : ι → R) (h two z : R)
    (h2 : (2 : R) ≠ 0) (htwo : two ≠ 0)
    (hχ : ∀ k ∈ s, χ k = f k * (h / 2) + c k * (two / 2))
    (h1 : ∑ k ∈ s, y k * f k = 1) (hz : ∑ k ∈ s, y k * χ k = z) :
    ∑ k ∈ s, y k * c k = (2 * z - h) / two := by
  have hsplit : ∑ k ∈ s, y k * χ k
      = (h / 2) * ∑ k ∈ s, y k * f k + (two / 2) * ∑ k ∈ s, y k * c k := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun k hk => ?_
    rw [hχ k hk]; ring
  rw [hsplit, h1] at hz
  rw [eq_div_iff htwo]
  field_simp at hz
  linear_combination hz

/-- The short `Q_β` element `Δ_S = (h²/2)·1 − (h/2)(σ₁ + σ₂)` has trace
`−(h/2)(2z − h)` under any trace with `tr(1) = 1`, `tr(σᵢ) = z`. So the ratio of
its traces at two Markov parameters is the ratio of `(2z − h)`; between `z_D`
and the augmentation `z = q` that ratio is `(2z_D − h)/[2]`, the Markov
average of `c₁` above. -/
theorem trace_deltaS (h z : R) :
    h ^ 2 / 2 * 1 - h / 2 * (z + z) = -(h / 2) * (2 * z - h) := by
  ring

end MarkovAverage

end QOU.Braiding.DeterminantChern
