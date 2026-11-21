/-!
# Fred2005.CommutativeFormalGroup

Sibling stub for content block
[`def:commutative-formal-group`](commutative-formal-group.md). The declaration is

```lean
abbrev Fred2005.CommutativeFormalGroup (R : Type*) [CommRing R] (ι : Type*) [Finite ι] :=
  {G : QOU.FormalGroups.FormalGroupLaw R ι // G.IsComm}
```

in [`Fred2005/FormalGroups.lean`](../lean/Fred2005/FormalGroups.lean), built on the
`qou` package's `QOU.FormalGroups.FormalGroupLaw` (n-dimensional formal group laws
over any commutative ring).

-- Ref: [hazewinkel1978] M. Hazewinkel, *Formal Groups and Applications*, 1978, Ch. I.
-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, §2.
-/
