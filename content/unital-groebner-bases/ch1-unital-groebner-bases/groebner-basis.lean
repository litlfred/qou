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

The paper's Definition 5.1 (Gröbner basis) corresponds to
`IsGrobnerShirshovBasis`, which requires:
- `overlap_resolves` — all overlap compositions reduce to zero
- `inclusion_resolves` — all inclusion compositions reduce to zero

The **unital condition** (Definition 5.2) is the additional
requirement that leading coefficients of generators (and their
two-sided multiples) are units of R. Over a field, this is
automatic.

Key results from the lean-archive:
- `composition_lemma` — proved (CompositionLemma.lean)
- `retraction_property` — proved (CompositionLemma.lean)
- `normal_form_unique` — axiom (Bergman 1978)

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
    See `QOU.GrobnerShirshov.IsGrobnerShirshovBasis`.

    The composition_lemma (proved in CompositionLemma.lean) and
    retraction_property (proved) are consequences.

    The unital condition adds: LC(g_γ) ∈ R× for all generators. -/
structure IsGSBasis (G : Type*) (k : Type*) [Ring k] where
  /-- All overlap S-polynomials reduce to zero. -/
  overlap_resolves : True  -- see lean-archive for full statement
  /-- All inclusion S-polynomials reduce to zero. -/
  inclusion_resolves : True  -- see lean-archive for full statement

/-- The **unital condition**: leading coefficients are units.
    Over a field, every Gröbner basis is unital. -/
def IsGSBasis.isUnital {G : Type*} {k : Type*} [Ring k]
    (_gs : IsGSBasis G k) : Prop :=
  True  -- see lean-archive for full statement with IsUnit

end QOU.GrobnerShirshov.ContentBlock
