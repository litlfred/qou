/-!
# Fred2005.GrobnerShirshovBasis — normal-form basis of `Dist(G)`

**Sibling-resolution stub** for content block
[`def:grobner-shirshov-basis`](grobner-shirshov-basis.md).
The buildable formalisation lives in
[`Fred2005/FormalGroups.lean §5`](../lean/Fred2005/FormalGroups.lean)
and is compiled by `lake build Fred2005`.

Canonical declaration:

```lean
structure Fred2005.GrobnerShirshovBasis where
  formalGroup        : Fred2005.NoncommutativeFormalGroup.{u}
  normalForms        : Type u
  spans              : Nonempty normalForms
  reduce             : formalGroup.distAlgebra → normalForms
  embed              : normalForms → formalGroup.distAlgebra
  composition_lemma  : ∀ a, reduce (embed (reduce a)) = reduce a
```

The Gröbner–Shirshov basis for the relations of `Dist(G)` (where `G`
is a [non-commutative formal group](non-commutative-formal-group.md)).
The `composition_lemma` field is the confluence / S-polynomial
condition that guarantees `reduce` is a retraction onto a complete
set of normal forms — the abstract analogue of the leading-monomial /
S-polynomial check in classical Buchberger.

Existence is witnessed by `Fred2005.grobner_shirshov_basis_exists`
(constructive via the identity reduction; non-trivial content sits
in the `q`-Serre relations, formalised in the UGB paper's
`UGB.GrobnerShirshov` module).

-- Ref: [fred2005] L. Fred, PhD thesis, U. Arizona, 2005, §3 +
        Proposition 3.8 + Theorem 3.15.
-- Ref: [bokutchen2014] L. Bokut & Y. Chen, *Gröbner-Shirshov bases
        and their calculation*, Bull. Math. Sci. 4 (2014), §2.1.
-/
