---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-012-26-quivers
section_title: "Quivers"
section_number: 2.6
pages: 11-12
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
of geometric type), studied in [FZ02], [FZ03], and [BFZ05]. The quiver interpretation, ﬁrst discussed in
[MRZ03], is given a complete introduction in [Mar13], which we follow. The only departure we need from
Marsh’s deﬁnition is to allow some edge weights to be in 1
2 Z instead of Z. We also give a name to the
symmetrized edge weights σ(v,w ), and encode the symmetrizability of edge weights into verte x weights dv.
Deﬁnition 2.26. A quiver is a directed graph with no 1- or 2-cycles or multiple edges, with weights on
edges and vertices. Vertex weights are in N>0, and edge weights are in 1
2 Z. The edge weights are denoted
σ(v,w ), and the vertex weights dv. Also deﬁned is the auxiliary quantity ǫ(v,w ), by
ǫ(v,w ) = dw
gcd(dv,d w)σ(v,w ).
Vertices are either frozen or non-frozen, and edge weights are integral unless the edge is between two
frozen vertices, in which case they are half-integral.
01
2
B1
B2
A2 A1
C1
C2
v11
v21
Figure 7. A quiver. Larger vertices are of weight 2, and dotted edges correspond to
σ(i,j ) = 1
2 .
11
Remark 2.27. Almost all of the time, σ(i,j ) will lie in { −1, 0, +1 }. In this case, the edge weights σ(i,j ) are
just the incidence matrix of the graph underlying the quiver .
Remark 2.28. The term quiver occurs in other areas of literature as a multi-digraph. We us e it here
as a edge-weighted digraph with skew-symmetrizable adjace ncy matrix, encoding the exchange matrix of
Fomin–Zelevinsky’s cluster algebras.
Deﬁnition 2.29. For each non-frozen v, a quiver µv(Q) is deﬁned. This is the mutation of Q atv. Edges
in µv(Q) are deﬁned by ǫ′(·, ·), with
ǫ′(x,y ) =



ǫ(x,y ) if ǫ(x,v )ǫ(v,y ) ≤ 0,v /∈ {x,y }
−ǫ(x,y ) if v ∈ {x,y }
ǫ(x,y ) + |ǫ(x,v )|ǫ(v,y ) if ǫ(x,v )ǫ(v,y )> 0,v /∈ {x,y }.
Customarily, the vertex v is renamed in µv(Q), e.g. to v′. This is because µv induces a map on the seed
torus of Q which changes the coordinate associated to v (see Deﬁnition 2.32). For very long sequences, we
will usually ignore the renamings for readability and think of v as a vertex in a graph, not as a coordinate
function.
Notation 2.30. Sequences of mutations are performed left to right: that is µv,w =µw ◦µv. When subscripts
would be awkward, we will also write mutation sequences as µ {v1,v 2,... }. We shall also employ ∏
v∈Iµv
to mean mutating at all vertices in I, in the order given by I.
Remark 2.31. When depicting quivers, we shall assume that all black edges have weight σ = 1 , and gray,
dashed edges have weight σ = 1
2 .
Vertex weights will be depicted by the relative size of circl es; we will only use weights 1, 2, and (only in
the case of G2) 3. Frozen vertices will be colored blue, but this will also b e described in the text if at all
relevant.
01
2
B1
B2
A2 A1
C1
C2
v11
v21 µ{v11}
01
2
B1
B2
A2 A1
C1
C2
v′
11
v21
Figure 8. Mutating the quiver of Figure 7 at v11.
