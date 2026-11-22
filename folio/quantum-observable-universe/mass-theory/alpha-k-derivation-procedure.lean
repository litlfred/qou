import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# QOU.BraidKnot.alpha_k_derivation_procedure

Linear-system procedure for Jones–Markov block-weights `y_λ` at
`H_n(R, q)`.  At generic `q` the Markov-trace property
`tr_M(x · T_n) = z · tr_M(x)` fixes `tr_M(w_μ) = z^{n - len μ}` for
every cycle-type representative `w_μ`, giving a `p(n) × p(n)` linear
system

  `Σ_λ χ_λ(w_μ) · y_λ  =  z^{n - len μ}`,   `A · y = b`,

with `A_{μ,λ} = χ_λ(w_μ)`.  At generic `q` the character matrix `A`
is invertible (Schur–Weyl–Hecke duality / cycle-type representatives
form a class-function basis), so the system has a **unique** solution
`y_λ`.

**2026-11-20 (W8b, gap 1 of bean `qou-w8cg`).** The invertibility of `A`
was a bare hypothesis. It is now **proved at `n = 3`**: the `H₃(q)`
character matrix on the representatives `1, σ₀, σ₀σ₁` has determinant
`−[2]_q · [3]_q` (`det_heckeCharMatrixH3`), so it is invertible exactly when
`[2]_q [3]_q ≠ 0`, i.e. away from the roots of unity of order 4, 3 and 6 —
which is what "generic `q`" means here (`alpha_k_derivation_procedure_h3`).
The table is the one stated and used in
`QOU.BraidsAndKnots.MarkovTraceTLUniqueness`. **General `n` is still carried
as a hypothesis**: it follows from semisimplicity of `H_n(q)` at generic `q`
and Tits deformation [geckpfeiffer2000, tits1969], which this file does not
formalise. The ground ring is now a generic field (§7c); it was `ℝ`.

The core mathematical content of the proposition is exactly this:
*for an invertible square matrix `A` and any right-hand side `b`, the
linear system `A · y = b` has a unique solution.*  The Lean statement
below isolates that content over a generic field `R`; the existence witness
is `A⁻¹ · b`, and uniqueness follows from injectivity of `v ↦ A · v`
for invertible `A`.

LaTeX label: `conj:alpha-k-derivation-procedure`

## References

- [leitner2026] Ch. Braids and Knots, §α_k derivation procedure
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidKnot

open Matrix

/-- **Proposition (linear-system characterisation of `y_λ`)**.

    At generic `q` the character matrix `A = [χ_λ(w_μ)]` is invertible
    (Schur–Weyl–Hecke duality), so the Jones–Markov linear system
    `A *ᵥ y = b` (with `b_μ = z^{n - len μ}`) has a **unique** solution
    `y`.  This is the abstract content: for an invertible square matrix
    `A` over a field and any `b`, `A *ᵥ y = b` has a unique solution,
    namely `y = A⁻¹ *ᵥ b`. -/
-- Ref: [leitner2026] Ch. Braids and Knots, §α_k derivation procedure
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem alpha_k_derivation_procedure {R : Type*} [Field R] {p : ℕ}
    (A : Matrix (Fin p) (Fin p) R) [Invertible A] (b : Fin p → R) :
    ∃! y : Fin p → R, A *ᵥ y = b := by
  refine ⟨A⁻¹ *ᵥ b, ?_, ?_⟩
  · -- existence: `A *ᵥ (A⁻¹ *ᵥ b) = (A * A⁻¹) *ᵥ b = 1 *ᵥ b = b`
    show A *ᵥ (A⁻¹ *ᵥ b) = b
    rw [Matrix.mulVec_mulVec, Matrix.mul_inv_of_invertible, Matrix.one_mulVec]
  · -- uniqueness: multiply by A⁻¹ on the left to show injectivity
    intro y hy
    have h1 : A⁻¹ *ᵥ (A *ᵥ y) = A⁻¹ *ᵥ b := by rw [hy]
    rw [Matrix.mulVec_mulVec] at h1
    rw [Matrix.inv_mul_of_invertible] at h1
    rw [Matrix.one_mulVec] at h1
    -- Ref: [leitner2026] conj:alpha-k-derivation-procedure
    exact h1

/-- The `H₃(q)` character matrix `A_{μ,λ} = χ_λ(w_μ)`: rows are the
representatives `w_μ = 1, σ₀, σ₀σ₁` (cycle types `(1³), (2,1), (3)`), columns
the partitions `λ = (3), (2,1), (1³)`. Values as in
`QOU.BraidsAndKnots.MarkovTraceTLUniqueness`. -/
def heckeCharMatrixH3 {R : Type*} [Field R] (q : R) : Matrix (Fin 3) (Fin 3) R :=
  !![1, 2, 1;
     q, q - q⁻¹, -q⁻¹;
     q ^ 2, -1, q⁻¹ ^ 2]

/-- `det A = −[2]_q · [3]_q`, with `[2]_q = q + q⁻¹` and `[3]_q = q² + 1 + q⁻²`. -/
theorem det_heckeCharMatrixH3 {R : Type*} [Field R] {q : R} (hq : q ≠ 0) :
    (heckeCharMatrixH3 q).det = -((q + q⁻¹) * (q ^ 2 + 1 + q⁻¹ ^ 2)) := by
  rw [heckeCharMatrixH3, Matrix.det_fin_three]
  simp
  field_simp
  ring

/-- **The `n = 3` case, proved.** At generic `q` (`q ≠ 0`, `[2]_q ≠ 0`,
`[3]_q ≠ 0`) the `H₃(q)` Jones–Markov system `A *ᵥ y = b` has a unique
solution for every right-hand side `b`. -/
theorem alpha_k_derivation_procedure_h3 {R : Type*} [Field R] {q : R} (hq : q ≠ 0)
    (h2 : q + q⁻¹ ≠ 0) (h3 : q ^ 2 + 1 + q⁻¹ ^ 2 ≠ 0) (b : Fin 3 → R) :
    ∃! y : Fin 3 → R, heckeCharMatrixH3 q *ᵥ y = b := by
  have hdet : IsUnit (heckeCharMatrixH3 q).det := by
    rw [det_heckeCharMatrixH3 hq]
    exact (neg_ne_zero.mpr (mul_ne_zero h2 h3)).isUnit
  haveI := (heckeCharMatrixH3 q).invertibleOfIsUnitDet hdet
  exact alpha_k_derivation_procedure _ b

end QOU.BraidKnot
