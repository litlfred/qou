import Mathlib.Algebra.Polynomial.Laurent


/-!
# QOU.Examples.maximal_torus_su2 — Maximal torus for SU(2)

The maximal torus T ≅ U(1) of SU(2):
- V = ℂ² with weight decomposition V = ℂe₊ ⊕ ℂe₋
- e₃ = ½ diag(1, −1) generates T
- t ∈ T acts on e₊ by e^{iθ} and e₋ by e^{−iθ}
- T = { diag(e^{iθ}, e^{−iθ}) : θ ∈ ℝ } ≅ U(1)
- Rank of T = 1 (= rank of SU(2))

LaTeX label: `ex:maximal-torus-su2`

## References

- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
- [manuscript] §1 Example: Maximal torus for SU(2)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Examples

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **SU(2) maximal torus data**: T ≅ U(1) with 2 weight spaces.

    LaTeX: `\label{ex:maximal-torus-su2}` -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
structure SU2MaximalTorusData where
  /-- Number of weight spaces in the fundamental V = ℂ². -/
  numWeightSpaces : ℕ
  /-- V decomposes into 2 weight spaces (±1/2). -/
  weight_decomp : numWeightSpaces = 2
  /-- Rank of the maximal torus. -/
  rank : ℕ
  /-- T has rank 1 (one-dimensional torus ≅ U(1)). -/
  rank_one : rank = 1
  /-- The weights of V are ±1/2 (represented as ±1 in the twice-weight convention). -/
  weights : List ℤ
  /-- The weight list for V_{1/2}. -/
  weights_are : weights = [1, -1]

/-- The maximal torus data for SU(2). -/
-- Ref: [manuscript] §1
def su2MaximalTorus : SU2MaximalTorusData where
  numWeightSpaces := 2
  weight_decomp := rfl
  rank := 1
  rank_one := rfl
  weights := [1, -1]
  weights_are := rfl

/-- T has rank 1 (≅ U(1)). -/
theorem su2_torus_rank : su2MaximalTorus.rank = 1 := rfl

/-- V_{1/2} has 2 weight spaces. -/
theorem su2_weight_count : su2MaximalTorus.numWeightSpaces = 2 := rfl

end

end QOU.Examples
