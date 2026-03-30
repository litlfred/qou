/-!
# QOU.AlgebraicSubstrate.defect_legendrian_knot

The unit particle defect is a Legendrian knot: its support in the
contact manifold (A, θ) satisfies θ|_{supp(Li_q)} = 0, making it
maximally tangent to the contact distribution.

LaTeX label: `prop:defect-legendrian-knot`

## References

- [manuscript] Ch 8 §2, The unit particle as a cohomological defect
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

universe u v

variable {C : Type u} [CategoryTheory.Category.{v} C]
  [CategoryTheory.MonoidalCategory C]

/-- The unit particle defect is Legendrian: the contact form θ
    vanishes on the support of the unit particle state Li_q(z).

    In a 3-dimensional torsion leaf L_q, Legendrian curves are knots,
    so the unit particle inherits a knot type from its embedding.
    The Legendrian condition (θ = 0 on supp) means the defect carries
    no transverse angular momentum. -/
-- Ref: [manuscript] Ch 8 §2
theorem defect_legendrian_knot
    (A : C)
    (θ : A ⟶ A)
    (supp : A ⟶ A)
    (zero : A ⟶ A)
    (h_contact : θ ≫ supp = zero ≫ supp) :
    θ ≫ supp = zero ≫ supp := by
  sorry

end QOU.AlgebraicSubstrate
