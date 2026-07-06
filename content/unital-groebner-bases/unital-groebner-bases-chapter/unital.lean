import Mathlib.Data.List.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Units.Basic

/-!
# Unital subset

Content block for `def:unital`.

Split out of `def:groebner-basis`. A subset `G ⊆ A` is **unital** when
every leading coefficient is a unit of the ground ring (and the same
holds after admissible left/right multiplication). Over a field this is
automatic; if `B` is multiplicatively closed, condition (b) follows from
condition (a).

The authoritative formalization lives in
`content/unital-groebner-bases/lean/QOU/GrobnerShirshov/Basic.lean`.

## References

- [leitnerpawloski2004] https://arxiv.org/abs/math/0409565, Definition 5
- content/unital-groebner-bases/lean/QOU/GrobnerShirshov/Basic.lean §§4–5
-/

namespace QOU.GrobnerShirshov.ContentBlock

/-- The **unital condition** for a family of generators with leading
    coefficients `leadingCoeffs : G → k`: every leading coefficient is a
    unit of the ground ring.

    Over a field this is automatic; this mirrors the `isUnital`
    predicate of `QOU.GrobnerShirshov.IsGrobnerShirshovBasis`. -/
-- Ref: [leitnerpawloski2004] Leitner & Pawloski, "Unital Gröbner Bases over Arbitrary Commutative Ground Rings," arXiv:math/0409565
def isUnital {G : Type*} {k : Type*} [Ring k]
    (leadingCoeffs : G → k) : Prop :=
  ∀ g : G, IsUnit (leadingCoeffs g)

end QOU.GrobnerShirshov.ContentBlock
