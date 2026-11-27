/-!
# Fred2005.NoncommutativeFormalGroup

Sibling stub for content block
[`def:non-commutative-formal-group`](non-commutative-formal-group.md). The declaration is

```lean
abbrev Fred2005.NoncommutativeFormalGroup (R : Type*) [CommRing R] (ι : Type*) [Finite ι] :=
  QOU.FormalGroups.FormalGroupLaw R ι
```

in [`Fred2005/FormalGroups.lean`](../lean/Fred2005/FormalGroups.lean). The distribution
algebra with its convolution product is `QOU.FormalGroups.Dist`, `conv`, `one` in the
`qou` package (`QOU/FormalGroups/Distributions.lean`; associativity `conv_assoc` and the
unit laws `one_conv`, `conv_one` are proved). The comultiplication and the multiplicative
basis of Lemma/Def. 2.2 are not formalised.

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, §2.
-/
