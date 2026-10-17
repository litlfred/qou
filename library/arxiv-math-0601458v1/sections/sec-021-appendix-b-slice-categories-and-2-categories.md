---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-021-appendix-b-slice-categories-and-2-categories
section_title: "Appendix B. Slice Categories and 2-Categories"
section_number: null
pages: 62-62
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
---
We saw that in the special case where the groupoid Z0 of colourings was a set,
the category of groupoid-coloured sets had objects which were maps from sets S
into Z0, and morphisms were commuting diagrams like this:
(76)
S
c

σ
/ S′
c′
~}}}}}}}}
Z0
commutes.
This is an example of an “over category”. These are categories of objects “over”
some given object. In general, an over category can be constructed from any cat-
egories C and object c ∈C by taking objects to be maps f : a →c (for a ∈C)
and morphisms to be commuting triangles. We will encounter this sort of construc-
tion again when we deﬁne M-sets and M-stuﬀtypes for a monoid M. This sort
of construction is often called a “slice category”. We will prefer the slightly more
illustrative terminology “over category”. For more details, see e.g. [13] or [14].
In general, however, groupoid-coloured sets have colours taken from a groupoid,
which is not an object in Set, so we have something somewhat weaker. One way
to say it is that we only have a forgetful functor from Z0-Set to Set where Z0-sets
are taken to the underlying set, and morphisms are taken to their underlying set
bijections. It is worth pointing out the relationship between this and the change of
perspective between our original way of deﬁning structure types as functions from
underlying sets to the “bundle” viewpoint, with structured sets lying “over” their
underlying sets.
Another way to say what we have with Z0-Set is that it is a weak over 2-category,
when we think of the sets S and S′ as trivial groupoids, hence σ, c and c′ functors.
These are deﬁned like over categories, but instead of morphisms amounting to
commuting triangles, morphisms consist of natural isomorphisms α with:
(77)
S
c

σ
/ S′
c′
~}}}}}}}}
Z0
rz
α
l
l
l
l
l
l
l
l
l
l
l
l
l
l
This is exactly the deﬁnition we gave above, where the morphisms coming from
α give the labels on the strands of σ.
The formulation of over 2-categories is particularly relevant to stuﬀtypes, as we
shall see. First, however, we need to ﬁll in some more infrastructure.
