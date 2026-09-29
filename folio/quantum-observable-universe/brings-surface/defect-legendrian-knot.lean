import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic


/-!
# QOU.AlgebraicSubstrate.defect_legendrian_knot

The unit particle defect is a Legendrian knot: its support in the
contact manifold (A, θ) satisfies θ|_{supp(Li_q)} = 0, making it
maximally tangent to the contact distribution.

LaTeX label: `prop:defect-legendrian-knot`

## References

- [manuscript] Ch 8 §2, The unit particle as a cohomological defect
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

open CategoryTheory

universe u v

variable {C : Type u} [CategoryTheory.Category.{v} C]
  [CategoryTheory.MonoidalCategory C]

/- The unit particle defect is Legendrian: the contact form θ
    vanishes on the support of the unit particle state Li_q(z).

    In a 3-dimensional torsion leaf L_q, Legendrian curves are knots,
    The unit particle inherits a knot type from its embedding.
    The Legendrian condition (θ = 0 on supp) means the defect carries
    no transverse angular momentum. -/
-- Ref: [manuscript] Ch 8 §2
/-- The Legendrian condition on the unit-particle defect, as a **predicate**
    on the categorical data: the contact form `θ`, post-composed with the
    defect support `supp`, agrees with the (given) `zero` morphism composed
    with `supp` — i.e. `θ` vanishes on `supp` in the categorical sense
    `θ ≫ supp = zero ≫ supp`.

    Named (§3b), not asserted: the previous `(h_contact : P) : P := h_contact`
    was self-assuming and stated nothing. The full geometric content — that
    `supp(Li_q)` is Legendrian in the contact 3-manifold `L_q` — requires the
    q-torsion leaf structure from the Reeb derivation, not available at this
    level of abstraction, so this names the condition rather than proving it. -/
def defect_legendrian_knot
    (A : C)
    (θ : A ⟶ A)
    (supp : A ⟶ A)
    (zero : A ⟶ A) : Prop :=
  θ ≫ supp = zero ≫ supp

end QOU.AlgebraicSubstrate
