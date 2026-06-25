import Mathlib.Data.List.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.Ring.Basic

/-!
# Monomials, monomial bases, and leading terms

Content block for `def:monomial-basis`.

The authoritative formalization lives in
`content/unital-groebner-bases/lean/QOU/GrobnerShirshov/Basic.lean`, which defines:
- `QOU.GrobnerShirshov.Monomial G` — words in generators (abbrev for `List G`)
- `QOU.GrobnerShirshov.AlgElement G k` — finitely supported linear
  combinations of monomials over a ring `k`
- `QOU.GrobnerShirshov.leadingMonomial` — the greatest monomial in
  the support w.r.t. an admissible order

The paper's Definition 3.1–3.3 corresponds to these declarations.

## References

- [leitnerpawloski2004] https://arxiv.org/abs/math/0409565, Definition 3
- content/unital-groebner-bases/lean/QOU/GrobnerShirshov/Basic.lean §§1–2
-/

-- Re-export the relevant types for documentation purposes.
-- In the Lean build these are imported via QOU.GrobnerShirshov.


namespace QOU.GrobnerShirshov.ContentBlock

/-- A **monomial** in a free associative algebra on generators `G`.
    Represented as a finite word (list) of generators.
    See `QOU.GrobnerShirshov.Monomial`. -/
abbrev Monomial (G : Type*) := List G

/-- An element of the free algebra `k⟨G⟩`, represented as a
    finitely-supported linear combination of monomials.
    See `QOU.GrobnerShirshov.AlgElement`. -/
structure AlgElement (G : Type*) (k : Type*) [Ring k] where
  coeff : Monomial G → k
  support : Finset (Monomial G)
  support_spec : ∀ m, m ∉ support → coeff m = 0

/-- The zero element has empty support.
    Proved (not sorry). -/
def AlgElement.zero {G : Type*} {k : Type*} [Ring k] : AlgElement G k where
  coeff := fun _ => 0
  support := ∅
  support_spec := fun _ _ => rfl

/-- An element is zero iff its support is empty.
    Proved (not sorry). -/
def AlgElement.isZero {G : Type*} {k : Type*} [Ring k]
    (f : AlgElement G k) : Prop :=
  f.support = ∅

end QOU.GrobnerShirshov.ContentBlock
