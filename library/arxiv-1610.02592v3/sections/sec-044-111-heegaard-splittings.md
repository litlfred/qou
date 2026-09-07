---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-044-111-heegaard-splittings
section_title: "Heegaard splittings"
section_number: 11.1
pages: 351-353
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
surgery, and with product manifoldsΣ× [−1, 1] we getsurface bundles. We
introduce here all these topological constructions.
We end this chapter by showing that every prime three-manifold has a
canonical decomposition along disjoint embedded tori, called thegeometric
decomposition – the reason for adopting this name will be evident in the next
chapters.
11.1. Heegaard splittings
A Heegard splittingis a decomposition of a closed three-manifold in two
manifolds of the simple kinds, the handlebodies.
11.1.1. Deﬁnition.The following proposition is quite surprising, because
it shows that every closed orientable three-manifold decomposes into two
pieces of a very simple type.
Proposition11.1.1. Everyclosedorientable3-manifold M decomposesinto
two handlebodies of some genusg.
Proof. The 3-manifoldM has a handle decomposition with 0-, 1-, 2-, and
3-handles. The 0- and 1-handles altogether form a handlebody. The 2- and
3-handles may be turned upside down to form a handle decomposition into 0-
and 1-handles, so another handlebody. □
343
344 11. CONSTRUCTIONS OF THREE-MANIFOLDS
H
H'
S
Figure 11.1. A stabilisation of a Heegaard splitting.
A decomposition ofM into two handlebodies is called aHeegaard splitting.
Thetwohandlebodieshavenecessarilythesamegenus g, sincetheirboundaries
are glued together and are hence diﬀeomorphic surfaces.
Deﬁnition 11.1.2. TheHeegaard genusg(M) of a closed orientableM is
the minimum genus of a Heegaard splitting forM.
11.1.2. Examples. The manifolds of genus zero and one are perfectly
understood.
Proposition 11.1.3.The 3-sphere has genus zero, lens spaces (exceptS3)
have genus one, and all the other closed orientable three-manifolds have genus
at least two.
Proof. By gluing two discs we get a 3-sphere, and by deﬁnition by gluing
two solid tori we get a lens space. □
Classifying closed manifolds of genus two is a much harder task. We limit
ourselves to a class of examples.
Exercise11.1.4. EverySeifertmanifold
(
S2, (p1,q 1), (p2,q 2), (p3,q 3)
)
with
p1,p 2,p 3> 2 has genus two.
Hint. Pick two singular ﬁbres and connect them with a horizontal arc. A
regular neighbourhood of this graph is a genus-two handlebody: prove that its
complement is also a handlebody. □
11.1.3. Stabilisation. The same manifold may have various non isotopic
Heegaard splittings: for instance there is a simple move that modiﬁes a Hee-
gaard splitting by increasing its genus in a somehow trivial way.
A stabilisation is a move as in Figure 11.1 that transforms a Heegaard
splitting M = H∪S H′ of genus g into one of genus g + 1 of the same
manifold M. We add an unknotted handle to the surfaceS =∂H =∂H′, so
that bothH andH′ are transformed into handlebodies of genusg + 1.
Example 11.1.5. The complement of a standardly embedded genus-g han-
dlebody inS3 as in Figure 9.6 is another handlebody, and together they form
