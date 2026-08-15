---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-022-12-notes-on-connectedness-of-the-1-efficient-pac
section_title: "Notes on connectedness of the 1-efficient Pachner Graph"
section_number: 12
pages: 39-41
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
In this section we study thePachner graph for a compact orientable 3-manifoldM with
non-empty boundary consisting of tori. This is a graph where each vertex corresponds to
an ideal triangulation (up to the equivalence of relabelling) of the manifoldM, with an
edge connecting two vertices if their corresponding triangulations can be obtained from one
another via 2-3 or 3-2 Pachner moves (as shown in Figures 11 and 12.) We give some general
results, then describe a census of all ideal triangulations with at most 6 tetrahedra which
provides a number of examples with interesting properties.
Figure 11. A 2-3 move on labelled tetrahedra. As the black square indicates,
edges A12 and B13 are identiﬁed withC23
Throughout the section, we will use Burton’s isomorphism signature notation [Bur11] to
identify triangulations. Interested readers can replicate the results of this section by inputing
these signatures into Regina to construct the relevant triangulations. Readers new to this
concept will ﬁnd it helpful to know that if the ﬁrst letter of the signature (of those used
in this paper) is then-th letter of the alphabet, then the corresponding triangulation is
comprised ofn− 1 tetrahedra.
As mentioned in the introduction, the the Pachner graph of a3-manifold with non-empty
boundary is connected, and so it is interesting to consider basic properties of subgraphs
of this graph: number of vertices, connectedness, etc. For example, we say thegeometric
Pachner graph is the subgraph of “geometric” triangulations such that Thurston’s gluing
equations have a solution where each tetrahedral shape has positive imaginary part.
40 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Figure 12. The eﬀect of the 2-3 move on the boundary triangles.
It has been recently shown that the ﬁgure eight knot complement admits inﬁnitely many
geometric triangulations, however the geometric subgraph of the Pachner graph is discon-
nected (see [DD, Theorem 1.1 and Remark 3.3]).
One can also deﬁne the1-eﬃcient Pachner graphas the subgraph of the Pachner graph
containing only 1-eﬃcient triangulations and the edges between them.
Before discussing the 1-eﬃcient Pachner graph, we mention that our notation (used here
and in the accompanying code) for Seifert ﬁbred spaces with non-empty boundary, is con-
sistent with Hatcher [Hat]. Namely, a Seifert ﬁbre space over the surfaceF with exceptional
ﬁbres given by the parameters{(ai,bi)}k
i=1 (with ai > bi > 0 if F is punctured) will be
denoted bySFS [F (a1,b 1)...(ak,bk)].
First, we point out that for many 3-manifolds the 1-eﬃcient Pachner graph is inﬁnite.
Although this is presumably known to the experts, we include it for the sake of completeness.
Proposition 12.1. Let M be an cusped irreducible, atoroidal orientable 3-manifold other
then the solid torusS1×D2. ThenM admits inﬁnitely many 1-eﬃcient triangulations.
The key idea for this proof is to exhibit ideal triangulations that support ataut angle
structure, i.e. a semi-angle structure where all angles are either 0 or π. (A semi-angle
structure is an assignment of non-negative angles to the edges in the ideal tetrahedra, so
that the angle sum at each ideal vertex in such a tetrahedron isπ.) Also, in [Lac00, Theorem
1], Lackenby shows that an-annular cusped manifolds admit taut ideal triangulations, which
give such a taut angle structure. Given the hypotheses of the Proposition, we point out
that an-annular is shorthand for Seifert ﬁbre spaces over the disk over thanS1×D2 or
SFS [D(2, 1)(2, 1)], and hyperbolic manifolds.
Proof. If M is hyperbolic or a Seifert ﬁbre space over the disk (other thanS1× D2 or
SFS [D(2, 1)(2, 1)]), then by [Lac00, Theorem 1],M admits a taut ideal triangulation, say
with n tetrahedra. In this triangulation, about any edge we can ﬁnd two faces of the
triangulation incident to that edge which (in an open neighbourhood of the edge) separate
the two angles labelled byπ. Performing a 0-2 move along these two faces produces a new
triangulation with n + 2 tetrahedra. To see that this triangulation supports a taut angle
structure, label each edge in the new edge class of degree 2 byπ, the opposite edges in the
THE 3D-INDEX AND NORMAL SURF ACES 41
tetrahedron byπ, and the remaining edges0. As this is a semi-angle structure, this new
triangulation is 1-eﬃcient sinceM is atoroidal (see [KR05, Theorem 2.6]).
IfM is Seifert ﬁbred over an annulus with exactly one exceptional ﬁbre, thenM is ﬁbred
over the circle with ﬁbre a surface of negative Euler characteristic. Therefore,M admits a
layered triangulation obtained from expressing the monodromy of its ﬁbration in terms of
edge ﬂips on an ideal triangulation of the ﬁbre (see for example [Lac00, Section 2]). Using
this ideal layered triangulation, we again obtain a taut angle structure and complete the
proof in the same manner as above. □
The following remark uses a dual notion to 1-eﬃciency, introduced by Garoufalidis [Gar15],
to obtain a similar result. LetT be an ideal triangulation withn tetrahedra andΛ ={λi}3n
i=1
a set of 3n generalised angle structures. Then Λ is a index structure on T if for eachQ =
(Q1,...,Q n) where Qj is a choice of quadrilateral type in tetrahedronj, there existλi such
that for allj the edges oppositeQj in T have positive angles inλi. This is an obstruction
to having embedded surfaces of non-negative Euler characteristic, and in fact it is known to
be equivalent toT being 1-eﬃcient by [GHRS15, Theorem 1.2].
Remark 12.2. An ideal triangulation of a solid torus will not admit a taut angle structure
(by [KR05], the existence of an embedded generalised normal torus in a solid torus is an
obstruction to existence of a taut angle structure). Nevertheless, an analogous method can
be used to obtain inﬁnitely many 1-eﬃcient triangulations of the solid torus. For example,
the triangulation ‘dLQacccbnbb’ has a gluing matrix:

1 0 0 0 0 0 0 0 0
1 2 2 1 2 2 1 2 2
0 0 0 1 0 0 1 0 0


and so{(2π,β 0,−π−β0,π,β 1,−β1,π,β 2,−β2)| β0,β 1,β 2∈ R} is a subset of the gener-
alised angle structures on ‘dLQacccbnbb’. Furthermore, one has the freedom to adjust these
parameters to ﬁnd an index structure. In fact, after performing a 0-2 move along the two
faces incident to the degree two edge, we see that a new index structure is obtained since we
can obtain new generalised angle structures by just introducing two new tetrahedra subject
to same constraint as the last two tetrahedra above, i.e. the angles are(π,βj,−βj). Fur-
thermore, one can then perform 0-2 moves along the faces incident to any degree 2 edge in
the resulting triangulations to obtain more 1-eﬃcient triangulations, and so by an inductive
argument there are inﬁnitely many 1-eﬃcient triangulations of the solid torus.
