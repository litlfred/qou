/-!
# QOU.HyperellipticQuintic.bring_weight_match

Under the cyclic Z_5 ⊂ S_5 action, both the X_5 coordinate x and
Bring's first Lagrange resolvent w_1 are weight-(-1) eigenvectors,
with common eigenvalue ζ_5^{-1}.  This gives a canonical
Z_5-equivariant identification of the weight-(-1) isotypical
components of their coordinate rings.

LaTeX label: `prop:x5-bring-weight-identification`

**Ground ring**: `ℂ` (representation-theoretic).

Self-contained: re-defines `zeta5` locally, matching the block-level
convention.
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU.X5BringWeight

open Complex

/-- Primitive fifth root of unity (local copy). -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
noncomputable def zeta5 : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / 5)

/-- ζ₅^5 = 1 (local copy; sorry pending env validation). -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
theorem zeta5_pow_five : zeta5 ^ 5 = 1 := by
  sorry

/-- **Bring / X_5 weight match**: ζ₅⁴ = ζ₅⁻¹.

    Expresses that the Z_5-eigenvalue of the first Lagrange resolvent
    w_1 on Bring (computed as ζ₅^{-1} via the DFT action
    σ(w_k) = ζ₅^{-k} w_k) coincides with the Z_5-eigenvalue of the
    X_5 coordinate x under the automorphism (x, y) ↦ (ζ₅·x, y).

    The full categorical statement — isomorphism of weight-(-1)
    isotypical components of coordinate rings — is a corollary of
    this scalar match plus the fact that each weight-(-1) subspace
    is one-dimensional.

    LaTeX: `\label{prop:x5-bring-weight-identification}`
    Ref: [edge1978] https://doi.org/10.1112/jlms/s2-18.3.539 -/
theorem bring_weight_match : zeta5 ^ (4 : ℕ) = zeta5⁻¹ := by
  -- Intended proof: from zeta5^5 = 1 and zeta5 ≠ 0 (Complex.exp
  -- never vanishes), conclude zeta5^4 = zeta5^{-1}.
  -- Ref: [edge1978] https://doi.org/10.1112/jlms/s2-18.3.539
  sorry

end QOU.X5BringWeight
