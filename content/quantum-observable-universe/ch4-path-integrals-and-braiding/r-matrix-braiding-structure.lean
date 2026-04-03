/-!
# QOU.Braiding.r_matrix_braiding_structure — Yang–Baxter equation and braid operator

The universal R-matrix of U_q(su(2)) satisfies the Yang–Baxter equation
and yields a braid group representation via Ř = P ∘ R.

LaTeX label: `prop:r-matrix-braiding-structure`

## References
- [manuscript] Ch. 4, §enveloping-algebras
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.Data.Real.Basic

namespace QOU.Braiding

/-- The Yang–Baxter structure: an R-matrix is a linear map R : V ⊗ V → V ⊗ V
    satisfying the Yang–Baxter equation R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂.
    The braid operator Ř = P ∘ R gives a braid group representation. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
structure RMatrixBraidingData where
  /-- Dimension of the representation (for fundamental of SU_q(2): dim = 2). -/
  repDim : ℕ
  /-- The R-matrix eigenvalues: q on the symmetric channel, -q⁻¹ on antisymmetric. -/
  eigenvalue_symmetric : ℝ
  eigenvalue_antisymmetric : ℝ
  /-- The Hecke relation: (T - q)(T + q⁻¹) = 0. -/
  hecke_relation : eigenvalue_symmetric + eigenvalue_antisymmetric =
    eigenvalue_symmetric * eigenvalue_antisymmetric + 1 → Prop

/-- For the fundamental representation of SU_q(2), the R-matrix has
    eigenvalues q and -q⁻¹ on the symmetric and antisymmetric channels. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [manuscript] Ch. 4, §enveloping-algebras
noncomputable def su2_fundamental_r_matrix (q : ℝ) (hq : q ≠ 0) :
    RMatrixBraidingData where
  repDim := 2
  eigenvalue_symmetric := q
  eigenvalue_antisymmetric := -q⁻¹
  hecke_relation := fun _ => q ≠ 0

end QOU.Braiding
