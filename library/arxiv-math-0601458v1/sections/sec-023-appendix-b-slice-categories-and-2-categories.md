---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-023-appendix-b-slice-categories-and-2-categories
section_title: "Appendix B. Slice Categories and 2-Categories"
section_number: null
pages: 62-62
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
We saw that in the special case where the groupoid Zo of colourings was a set,
the category of groupoid-coloured sets had objects which were maps from sets S'
into Zp, and morphisms were commuting diagrams like this:

(76) s—>s'
Zo
commutes.

This is an example of an “over category”. These are categories of objects “over”
some given object. In general, an over category can be constructed from any cat-
egories C and object c € C by taking objects to be maps f : a > c (for a € C)
and morphisms to be commuting triangles. We will encounter this sort of construc-
tion again when we define M-sets and M-stuff types for a monoid M. This sort
of construction is often called a “slice category”. We will prefer the slightly more
illustrative terminology “over category”. For more details, see e.g. [13] or [14].

In general, however, groupoid-coloured sets have colours taken from a groupoid,
which is not an object in Set, so we have something somewhat weaker. One way
to say it is that we only have a forgetful functor from Zo-Set to Set where Zo-sets
are taken to the underlying set, and morphisms are taken to their underlying set
bijections. It is worth pointing out the relationship between this and the change of
perspective between our original way of defining structure types as functions from
underlying sets to the “bundle” viewpoint, with structured sets lying “over” their
underlying sets.

Another way to say what we have with Zo-Set is that it is a weak over 2-category,
when we think of the sets S and S’ as trivial groupoids, hence o, c and c’ functors.
These are defined like over categories, but instead of morphisms amounting to
commuting triangles, morphisms consist of natural isomorphisms a with:

(77) S—ss'

ia

Zo

This is exactly the definition we gave above, where the morphisms coming from
a give the labels on the strands of o.

The formulation of over 2-categories is particularly relevant to stuff types, as we
shall see. First, however, we need to fill in some more infrastructure.
