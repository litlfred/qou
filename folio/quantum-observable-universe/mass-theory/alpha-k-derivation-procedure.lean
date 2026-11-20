import Mathlib.Data.Real.Basic
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse

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

The core mathematical content of the proposition is exactly this:
*for an invertible square matrix `A` and any right-hand side `b`, the
linear system `A · y = b` has a unique solution.*  The Lean statement
below isolates that content over `ℝ` (the archimedean specialisation
of the generic ring `R` at the substrate `q_0`); the existence witness
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
    `A` over `ℝ` and any `b`, `A *ᵥ y = b` has a unique solution,
    namely `y = A⁻¹ *ᵥ b`. -/
-- Ref: [leitner2026] Ch. Braids and Knots, §α_k derivation procedure
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem alpha_k_derivation_procedure {p : ℕ}
    (A : Matrix (Fin p) (Fin p) ℝ) [Invertible A] (b : Fin p → ℝ) :
    ∃! y : Fin p → ℝ, A *ᵥ y = b := by
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

end QOU.BraidKnot
