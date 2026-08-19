---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-029-91-truncated-and-doubly-truncated-simplices
section_title: "Truncated and doubly truncated simplices"
section_number: 9.1
pages: 28-31
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
Deﬁnition 9.1. A truncated simplex is a polyhedron obtained from a simplex by truncating
its vertices. A doubly truncated simplex is a polyhedron obtained from a simplex by ﬁrst
truncating the vertices and then truncating the edges.
We refer to the edges of a truncated simplex as long and short edges, and the edges of a
doubly truncated simplex as long, middle, and short edges.
Note that a triangulation of M induces a decomposition of M into truncated simplices, as
well as a decomposition of M into doubly truncated simplices and prisms. An ordering of a
simplex induces an orientation of the edges of the corresponding truncated simplex. Similarly,
an orientation of a simplex induces orientations of the edges of the corresponding doubly
truncated simplex. Note that an ordering is required to obtain natural edge orientations on
a truncated simplex.
0
1
3
2
0
1
3
2
β132
α123
γ123
Figure 17. A truncated
simplex. Edge orienta-
tions induced by the ver-
tex ordering.
Figure 18. A doubly
truncated simplex. Edge
orientations induced by
the orientation.
Figure 19. A prism.
Remark 9.2. We can view a doubly truncated simplex as the permutohedron of S4. We
can embed it in a standard simplex ∆ 3
1 as the convex hull of 1
11∆3
11({0, 1, 3, 7}), the set
1
11∆3
11({0, 1, 3, 7}) being the vertex set. With this embedding, the long edges are twice as
long as the middle edges, which are again twice as long as the short edges (which have length√
2
11 ). Similarly, we may view a truncated simplex as the convex hull of 1
5∆3
5({0, 1, 4}).
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 29
9.2. Cocycles. LetG be a group and let X be any space with a polyhedral decomposition.
Deﬁnition 9.3. A G-cocycle on X is an assignment of elements in G to the oriented edges
ofX such that the product around each face is 1∈G and such that reversing the orientation
of an edge replaces the labeling by its inverse.
Deﬁnition 9.4. Letτ be a G-valued 0-cochain onX, i.e. a function from the vertices to G.
The coboundary of τ is the G-cocycle
(9.1) δτ (⟨v0,v 1⟩) = (τv0)−1τv1,
where⟨v0,v 1⟩ is the edge from v0 tov1 andτvi is the value ofτ atvi. The coboundary action
of τ on G-cocycles is given by taking σ to the cocycle
(9.2) τσ :⟨v0,v 1⟩↦→ (τv0)−1σ(⟨v0,v 1⟩)τv1.
Given a simplex ∆, let∆ and ∆ denote the corresponding truncated, and doubly truncated
simplices.
Deﬁnition 9.5. Let H⊂G be groups. A ( G,H )-cocycle on ∆ is a G-cocycle where short
edges are labed by elements in H.
Deﬁnition 9.6. LetK⊂H⊂G be groups. A (G,H,K )-cocycle on ∆ is aG-cocycle where
short edges are labeled by elements in K, and middle edges by elements in H.
Remark 9.7. Note that every (G,H )-cocycle on ∆ can be obtained from a unique (G,H,{e})-
cocycle on ∆ by collapsing the short edges. We shall thus always regard a cocycle on ∆ as
a cocycle on ∆.
9.2.1. Labeling conventions. We index the vertices of ∆ by ordered pairs of distinct vertices
of ∆, v0v1 being the vertex near v0 on the edge to v1. We index the vertices of ∆ by ordered
triples of distinct vertices of ∆, v0v1v2 being the vertex, whose closest vertex in ∆ is v0,
closest edge v0v1, and closest face v0v1v2. Given a cocycle on ∆, we use α’s to denote the
labeling of long edges, β’s for the middle edges, and γ’s for the short edges. Note that an
edge of each type is uniquely determined by its initial vertex. This gives a unique labeling
scheme, e.g. the long edge from v0v1v2 to v1v0v2 is labeled by βv0v1v2. Similarly, if τ is a
0-cochain, the value at v0v1v2 is denoted by τv0v1v2. We shall not need a labeling scheme
for cocycles on truncated simplices. By Remark 9.7 we can regard these as cocycles on the
corresponding doubly truncated simplices.
9.3. The natural cocycle of a generic decoration. We now show that suﬃciently generic
decorations naturally give rise to cocycles on M.
Deﬁnition 9.8. A pair (g0N,g 1N) of N-cosets in SL(n, C) is suﬃciently generic if there
exists a (necessarily unique) g∈ SL(n, C) such that
(9.3) ( g0N,g 1N) =g(N,qN ), with q counter-diagonal.
A tuple is suﬃciently generic if it is pairwise suﬃciently generic.
Let N− denote the lower triangular matrices in SL(n, C) with 1’s on the diagonal.
30 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
Deﬁnition 9.9. An element n∈ B is normalized if the last column vector consists of 1’s.
An element n−∈N− in normalized if the ﬁrst column vector consists of 1’s.
Deﬁnition 9.10. A triple (g0B,g 1B,g 2B) of B-cosets in PGL(n, C) is suﬃciently generic
if there exists a (necessarily unique) g∈ PGL(n, C) such that
(9.4) ( g0B,g 1B,g 2B) =g(B,q 1B,n−B), with n−∈N− normalized.
A tuple is suﬃciently generic if each triple is suﬃciently generic.
Remark 9.11. A simple exercise in linear algebra shows that generic (as in Deﬁnition 8.6)
implies suﬃciently generic.
Deﬁnition 9.12. Let (g0N,g 1N,g 2N,g 3N) be a generic SL(n, C)/N-decoration on ∆3
n. The
natural (SL(n, C),N )-cocycle on ∆3
n is the coboundary of the unique 0-cochain τ satisfying
(9.5) ( gv0N,gv1N) =τv0v1(N,qN ) with q counter diagonal.
This deﬁnes the map Lαβ in (1.5). It follows immediately from the deﬁnition that the
natural cocycle labels short edges by elements in N and long edges by counter diagonal
elements. Let q1 denote the counter diagonal matrix whose non-zero entries are all 1. Note
that q1 =q−1
1 .
Deﬁnition 9.13. Let (g0B,g 1B,g 2B,g 3B) be a generic decoration on a simplex. The natural
(PGL(n, C),B,H )-cocycle on ∆3
n is the coboundary of the unique 0-cochain τ satisfying
(9.6) ( gv0B,gv1B,gv2B) =τv0v1v2(B,q 1B,n−B) with n−∈N− normalized.
This deﬁnes the mapLαβγ in (1.5).
Remark 9.14. Note that a (G,H )-cocycle σ on ∆ determines a G/H-decoration D on ∆.
We say thatD is compatible withσ. To see this note that σ is the coboundary of a 0-cochain
τ on ∆, which is unique up to left multiplication by an element in G. The value of τ at the
vertices near a vertex of ∆ are all in the same H-coset. Hence, we have a decoration on ∆.
Similarly, a (G,B,H )-cocycle on ∆ determines a G/B-decoration on ∆. It follows that the
mapsLαβ andLαβγ are bijective with explicit inverses.
Lemma 9.15. Let D = (g0B,g 1B,g 2B,g 3B) be a generic decoration on a simplex. The
natural (PGL(n, C),B,H )-cocycle is the unique cocycle, which is compatible with the dec-
oration and satisﬁes
(i) Short edges are labeled by elements in H.
(ii) Middle edges are labeled by normalized elements in B.
(iii) Long edges are labeled by q1.
Proof. We ﬁrst show that the natural cocycle satisﬁes the three conditions. It is enough to
prove this for a single edge of each type. We may assume that D = (B,q 1,B,n −B,m−B)
where n−,m− ∈ N− and n− is normalized. Then τ 012 = 1, so for each edge starting
at 012, we only need to compute the value of τ at the end point. Since ( q1B,B,n −B) =
q1(B,q 1B,q 1n−B), and the ﬁrst column vector ofq1n− consists of 1’s, it follows thatτ 102 =q1,
proving the result for the long edges. Since the stabilizer of B isB, it follows that τ 021∈B,
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 31
proving the result for the middle edges. Finally, τ 013 is the unique element in H such that
hm−h−1 is normalized, proving the result for the short edges.
Let σ1 and σ2 be two cocycles satisfying the required conditions. Since any two cocycles
diﬀer by the coboundary action, σ2 = ησ1 for some coboundary η. Since long edges are
labeled by q1 and since the cocycles determine the same decoration, we may assume that
η takes values in H. It is now elementary to check that if η is not the identity, either (ii)
or (iii) fails. □
Remark 9.16. Note that for a generic decoration on a triangulation of M, the natural
cocycles on each simplex ﬁt together to form a natural cocycle on M.
