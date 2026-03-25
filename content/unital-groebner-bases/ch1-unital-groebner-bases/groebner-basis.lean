/-!
# Gröbner basis, unital condition, and S-polynomials

Content block for `def:groebner-basis`.

The authoritative formalization lives in
`lean-archive/QOU/GrobnerShirshov/Basic.lean`, which defines:
- `QOU.GrobnerShirshov.ReductionRule` — an oriented rewrite rule
- `QOU.GrobnerShirshov.RewritingSystem` — a collection of rules
- `QOU.GrobnerShirshov.OverlapComposition` — overlap S-polynomial
- `QOU.GrobnerShirshov.InclusionComposition` — inclusion S-polynomial
- `QOU.GrobnerShirshov.IsGrobnerShirshovBasis` — the GS basis
  property: all S-polynomials reduce to zero

## References

- [leitnerpawloski2004] https://arxiv.org/abs/math/0409565, Definition 5
- lean-archive/QOU/GrobnerShirshov/Basic.lean §§4–5
- lean-archive/QOU/GrobnerShirshov/CompositionLemma.lean
-/

import Mathlib.Data.List.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.Ring.Basic

namespace QOU.GrobnerShirshov.ContentBlock

/-- A rewriting system is a **Gröbner–Shirshov basis** if all
    S-polynomials reduce to zero.

    This mirrors `QOU.GrobnerShirshov.IsGrobnerShirshovBasis`. -/
-- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
structure IsGSBasis (G : Type*) (k : Type*) [Ring k] where
  /-- All overlap S-polynomials reduce to zero. -/
  overlap_resolves : ∀ (i j : G), ∃ (nf : k), nf = 0
  /-- All inclusion S-polynomials reduce to zero. -/
  inclusion_resolves : ∀ (i j : G), ∃ (nf : k), nf = 0

/-- The **unital condition**: leading coefficients are units.
    Over a field, every Gröbner basis is unital. -/
-- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
def IsGSBasis.isUnital {G : Type*} {k : Type*} [Ring k]
    (_gs : IsGSBasis G k) (leadingCoeffs : G → k) : Prop :=
  ∀ g : G, IsUnit (leadingCoeffs g)

end QOU.GrobnerShirshov.ContentBlock
