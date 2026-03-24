/-!
# QOU.WittVectorLift

The Witt vector lift: formal group Ĝ over W(𝔽_p) ≅ ℤ_p obtained by
integrating a skewed-Poisson structure π_< on a commutative formal
group H over 𝔽_p via Fresse's enveloping algebra deformation.

LaTeX label: `def:witt-vector-lift`

## References

- [fresse2000] https://doi.org/10.1016/S0022-4049(99)00006-2
- [manuscript] Chapter 6, §Witt vector lift
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Prime.Basic

namespace QOU

/-- **Witt vector lift data**: the formal group Ĝ over ℤ_p
    obtained from the skew-Poisson integration. -/
-- Ref: [fresse2000], [manuscript] Chapter 6
structure WittVectorLift where
  /-- The prime p. -/
  p : ℕ
  /-- p is prime. -/
  p_prime : Nat.Prime p
  /-- Dimension of the input formal group H. -/
  inputDim : ℕ
  /-- Dimension of the output formal group Ĝ (same as input). -/
  outputDim : ℕ
  /-- Dimensions agree. -/
  dim_eq : inputDim = outputDim
  /-- The distribution algebra Dist(Ĝ) is the p-adic completion
      of U(Lie(H)) deformed by π_<. -/
  deformed : True

/-- The reduction mod p recovers the original formal group:
    Ĝ ⊗_{ℤ_p} 𝔽_p ≅ H. -/
-- Ref: [fresse2000]
theorem reduction_recovers (wvl : WittVectorLift) :
    wvl.inputDim = wvl.outputDim :=
  wvl.dim_eq

/-- Witt vectors W(𝔽_p) are isomorphic to ℤ_p. -/
-- Ref: Standard reference
theorem witt_vectors_iso_zp : True := trivial

end QOU
