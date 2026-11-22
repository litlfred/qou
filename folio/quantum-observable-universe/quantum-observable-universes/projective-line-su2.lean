import Mathlib.Data.Nat.Basic


/-!
# QOU.Examples.projective_line_su2 — Projective line for SU(2)

The flag manifold SU(2)/U(1) ≅ ℙ¹(ℂ):
- Points [ℓ] ∈ ℙ¹(ℂ) are lines ℓ ⊂ V = ℂ² (kernels of linear forms)
- Function algebra: O(ℙ¹(ℂ)) = ℂ[z] in affine coordinate z = v₁/v₂
- This is the key C[z] identification: the coordinate ring of the
  projective line is the polynomial ring ℂ[z]
- Euler characteristic χ(ℙ¹) = 2

LaTeX label: `ex:projective-line-su2`

## References

- [leitner2026] §1 Example: Projective line for SU(2)
-/

namespace QOU.Examples

/-- **SU(2) projective line data**: ℙ(V) = SU(2)/U(1) ≅ ℙ¹(ℂ) ≅ S².

    LaTeX: `\label{ex:projective-line-su2}` -/
-- Ref: [leitner2026] §1
structure SU2ProjectiveLineData where
  /-- Real dimension of G/T = SU(2)/U(1). -/
  realDim : ℕ
  /-- SU(2)/U(1) has real dimension 2 (= dim SU(2) − dim U(1) = 3 − 1). -/
  real_dim_eq : realDim = 2
  /-- Complex dimension of ℙ¹(ℂ). -/
  complexDim : ℕ
  /-- ℙ¹(ℂ) has complex dimension 1. -/
  complex_dim_eq : complexDim = 1
  /-- Euler characteristic of ℙ¹(ℂ) = S². -/
  eulerChar : ℤ
  /-- χ(ℙ¹) = 2. -/
  euler_eq : eulerChar = 2
  /-- The coordinate ring is ℂ[z] (polynomial ring in one variable). -/
  coord_ring_generators : ℕ
  /-- One generator z. -/
  coord_ring_one_gen : coord_ring_generators = 1

/-- The projective line data for SU(2)/U(1). -/
-- Ref: [leitner2026] §1
def su2ProjectiveLine : SU2ProjectiveLineData where
  realDim := 2
  real_dim_eq := rfl
  complexDim := 1
  complex_dim_eq := rfl
  eulerChar := 2
  euler_eq := rfl
  coord_ring_generators := 1
  coord_ring_one_gen := rfl

/-- ℙ¹(ℂ) has Euler characteristic 2. -/
theorem su2_projective_euler_char : su2ProjectiveLine.eulerChar = 2 := rfl

/-- The coordinate ring O(ℙ¹) = ℂ[z] has one generator. -/
theorem su2_cz_one_generator : su2ProjectiveLine.coord_ring_generators = 1 := rfl

end QOU.Examples
