---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: page-008
section_title: "Page 8"
section_number: null
pages: 8-8
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
toc_source: undetermined
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where the ten- sor product need not be commutative."
---
8
JOHN W. BARRETT & BRUCE W. WESTBURY
The proof of the coherence theorem 1.9 now follows. It is only necessary to con-
sider reduced iterated natural transformations. A reduced iterated natural transfor-
mation is said to be directed if it is the product of instances which do not include
the inverses of (γ, τ, ν).
By the preceding lemma 1.15, each iterated functor is
equivalent to a reduced iterated functor, and hence to a standard iterated functor,
by a directed natural transformation.
By a standard argument (see [MacLane 1963]), it is suﬃcient to prove the co-
herence result for directed natural transformations between an iterated functor F
and a standard iterated functor S. According to lemma 1.11, any directed natural
transformation S →F can be written as a central iterate S →R followed by an
iterate of instances of (γ, τ, ν): R →F. By lemma 1.15, R and the second natural
transformation are unique, whilst the ﬁrst natural transformation is unique by the
coherence of central iterates.
Deﬁnition 1.16. If C is a category with duals then deﬁne the category PC to have
objects of the form (F, {a1, . . . , an}) where F is a standard iterated functor of mul-
tiplicity n and each ai is an object of C. The set of morphisms from (F, {a1, . . . , an})
to (G, {a1, . . . , am}) is the set of morphisms in C from F(a1, . . . , an) to G(a1, . . . , am).
There is a functor i: C →PC deﬁned on objects by a 7→(1, a). There is also
a functor π: PC →C deﬁned on objects by (F, {a1, . . . , an}) 7→F(a1, . . . , an). It
is trivial that the composite i ◦π is the identity functor of C. It is also clear that
there is a canonical natural transformation from π ◦i to the identity functor of PC.
Hence the categories PC and C are canonically equivalent.
The coherence theorem implies that the category PC is a strict monoidal cat-
egory with strict duals. The functor i has the universal property that if D is a
strict monoidal category with strict duals and F: C →D is a functor of monoidal
categories with duals then there is a unique functor G: PC →D of strict monoidal
categories with strict duals such that F = i ◦G.
2. Spherical categories
In this section we introduce spherical categories. A pivotal category is a category
with duals and with some additional structure and a spherical category is a pivotal
category in which the additional structure satisﬁes an extra condition.
Strict pivotal categories are discussed in [Freyd and Yetter 1989], where it is
shown that the category of oriented planar graphs up to isotopy with labelled
edges and with a distinguished edge at each vertex is a strict pivotal category.
If the sphere S2 is regarded as the plane with the point at inﬁnity attached, then
a closed graph in the plane can be regarded as a closed graph on the sphere. There
is an isotopy of the sphere which takes a closed graph of the form of Figure 1 to
the graph obtained by closing M in a loop to the left. This isotopy moves the loop
in Figure 1 past the point at inﬁnity. Taken together with planar isotopies, such
an operation on planar graphs generates all the isotopies on the sphere. It follows
that the evaluation in a spherical category of a closed graph with labelled edges and
with a distinguished edge at each vertex is invariant under isotopies of the sphere
S2.
