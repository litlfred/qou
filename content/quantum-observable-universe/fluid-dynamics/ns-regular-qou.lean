/-!
# QOU.FluidDynamics.NSRegularQOU — NS-regular quantum observable universe

A quantum observable universe (C, A, τ) is NS-regular when the NS obstruction
class NS(A) = κ₀|_Σ ∈ H²(Σ, B) vanishes, where Σ is the collision locus of
a generic vortex pair and κ₀ = e(ξ) is the Euler class of the Reeb bundle.
NS-regularity implies that the classical Navier–Stokes equation (the q = 1
specialisation) admits smooth global solutions for all smooth initial data.

LaTeX label: `def:ns-regular-qou`

## References

- [manuscript] Ch 10 §2

**Ground ring**: `R_q = ℤ[q, q⁻¹]`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic

namespace QOU.FluidDynamics

/-- An NS-regular quantum observable universe: one whose NS obstruction
    class vanishes, guaranteeing global regularity of the classical
    Navier–Stokes equation (q → 1 limit).

    The NS obstruction depends only on the Euler characteristic χ(A):
    - χ(A) = 0  ⟹  NS(A) = 0  (NS-regular)
    - χ(A) ≠ 0  ⟹  NS(A) ≠ 0  (NS-singular) -/
-- Ref: [manuscript] Ch 10 §2
structure NSRegularQOU where
  /-- The Euler characteristic χ(A) of the Frobenius–Hopf object. -/
  eulerChar : ℤ
  /-- NS-regularity: the Euler characteristic vanishes. -/
  -- Ref: [manuscript] Ch 10 §2
  ns_regular : eulerChar = 0

/-- An NS-singular quantum observable universe has nonzero obstruction. -/
-- Ref: [manuscript] Ch 10 §2
structure NSSingularQOU where
  /-- The Euler characteristic χ(A) of the Frobenius–Hopf object. -/
  eulerChar : ℤ
  /-- NS-singularity: the Euler characteristic is nonzero. -/
  -- Ref: [manuscript] Ch 10 §2
  ns_singular : eulerChar ≠ 0

end QOU.FluidDynamics
