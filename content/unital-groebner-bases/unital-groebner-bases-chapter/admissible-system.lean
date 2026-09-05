import Mathlib.Order.WellFounded
import Mathlib.Data.List.Basic


/-!
# Monomial ordering and admissible system

Content block for `def:admissible-system`.

The authoritative formalization lives in
`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/Basic.lean`, which defines:
- `QOU.GrobnerShirshov.AdmissibleOrder G` — a well-order on monomials
  compatible with left and right concatenation

The paper's Definition 3.4–3.6 corresponds to `AdmissibleOrder`.

Key properties (all proved, no sorry):
- `trichotomy` — linear order on monomials
- `wf` — well-foundedness
- `left_compat` — a < b → c++a < c++b
- `right_compat` — a < b → a++d < b++d

Additionally, `NormalForms.lean` provides concrete instances:
- `degLexLt` — degree-lexicographic order (proved well-founded)
- `degLexLt_trichotomy` — trichotomy (proved)
- `degLexLt_left_compat`, `degLexLt_right_compat` — compatibility (proved)
- `degLexOrder` — the full `AdmissibleOrder` instance (proved)

## References

- [leitnerpawloski2004] https://arxiv.org/abs/math/0409565, Definition 3.4–3.6
- content/unital-groebner-bases/lean/UGB/GrobnerShirshov/Basic.lean §1
- content/unital-groebner-bases/lean/UGB/GrobnerShirshov/NormalForms.lean (concrete order)
-/

namespace QOU.GrobnerShirshov.ContentBlock

/-- An **admissible order** on monomials: a well-order compatible
    with concatenation (two-sided multiplication).
    See `QOU.GrobnerShirshov.AdmissibleOrder`.

    All fields are proved in the Lean formalization for the deg-lex order. -/
structure AdmissibleOrder (G : Type*) where
  lt : List G → List G → Prop
  trichotomy : ∀ (a b : List G), lt a b ∨ a = b ∨ lt b a
  wf : WellFounded lt
  left_compat : ∀ (a b c : List G), lt a b → lt (c ++ a) (c ++ b)
  right_compat : ∀ (a b d : List G), lt a b → lt (a ++ d) (b ++ d)

end QOU.GrobnerShirshov.ContentBlock
