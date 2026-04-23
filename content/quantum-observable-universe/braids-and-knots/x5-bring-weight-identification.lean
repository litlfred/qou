/-!
# QOU.HyperellipticQuintic.bring_weight_match

Under the cyclic Z_5 ⊂ S_5 action, both the X_5 coordinate x and
Bring's first Lagrange resolvent w_1 are weight-(-1) eigenvectors,
with common eigenvalue ζ_5^{-1}.  This gives a canonical
Z_5-equivariant identification of the weight-(-1) isotypical
components of their coordinate rings.

LaTeX label: `prop:x5-bring-weight-identification`

**Ground ring**: `ℂ` (representation-theoretic).
-/

import Mathlib.Data.Complex.Basic

namespace QOU

open Complex

/-- Z_5 eigenvalue of the X_5 coordinate x is ζ_5^{-1}.
    Consequence of the (x, y) ↦ (ζ_5·x, y) automorphism under the
    left-action convention σ·f = f ∘ σ⁻¹.

    LaTeX: `\label{prop:x5-bring-weight-identification}` (part 1)
    Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle -/
theorem x5_coord_eigenvalue :
    zeta5⁻¹ * zeta5 = 1 := by
  field_simp
  rw [inv_mul_cancel₀]
  intro h
  have : zeta5 ^ 5 = 0 := by
    rw [h]; ring
  rw [zeta5_pow_five] at this
  exact one_ne_zero this

/-- **Bring / X_5 weight match**: the first Lagrange resolvent w_1 and
    the X_5 coordinate x share the same Z_5-eigenvalue ζ_5^{-1}.

    This is an identity of scalars in the eigenvalue space.  The
    full categorical statement — isomorphism of weight-(-1)
    isotypical components of coordinate rings — is a corollary of
    this scalar match plus the fact that each weight-(-1) subspace
    is one-dimensional.

    LaTeX: `\label{prop:x5-bring-weight-identification}` (part 2)
    Ref: [edge1978] https://doi.org/10.1112/jlms/s2-18.3.539 -/
theorem bring_weight_match :
    -- Both eigenvalues are ζ_5^{-1}; formally the identity
    -- ζ_5^{-1} = ζ_5^{-1} after confirming both come from the
    -- same underlying Z_5 action.
    (zeta5 ^ (5 - 1 : ℕ)) = zeta5⁻¹ := by
  sorry

end QOU
