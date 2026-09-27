import Mathlib.Data.List.Basic
import Mathlib.Data.List.Infix
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.Ring.Defs


/-!
# Remainder modules O(I) and Õ(I)

Content block for `def:remainder-module`.

The authoritative formalization lives in
`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/Basic.lean`, which defines:
- `QOU.GrobnerShirshov.isNormalForm` — an element is in normal form
  iff no rule's leading monomial divides any monomial in its support

The remainder module Õ(I) is the span of normal-form monomials:
those basis elements not appearing as leading monomials of any
element of I. This corresponds to `isNormalForm` applied to
single monomials.

## References

- [leitnerpawloski2004] https://arxiv.org/abs/math/0409565, Definition 4
- content/unital-groebner-bases/lean/UGB/GrobnerShirshov/Basic.lean §3 (isNormalForm)
-/

namespace QOU.GrobnerShirshov.ContentBlock

/-- An element is in **normal form** w.r.t. a rewriting system if no
    rule's leading monomial appears as a subword of any monomial in
    the element's support. This characterizes elements of Õ(I).
    See `QOU.GrobnerShirshov.isNormalForm` (proved, no sorry). -/
def isNormalForm {G : Type*} {k : Type*} [Ring k]
    (rules : List (List G))  -- leading monomials of rules
    (support : Finset (List G)) : Prop :=
  ∀ r ∈ rules, ∀ m ∈ support, ¬ r <:+: m

end QOU.GrobnerShirshov.ContentBlock
