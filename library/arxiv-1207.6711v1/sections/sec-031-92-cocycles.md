---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-031-92-cocycles
section_title: "Cocycles"
section_number: 9.2
pages: 29-29
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
9.2. Cocycles. Let G be a group and let X be any space with a polyhedral decomposition.
Deﬁnition 9.3. A G-cocycle on X is an assignment of elements in G to the oriented edges
of X such that the product around each face is 1 ∈G and such that reversing the orientation
of an edge replaces the labeling by its inverse.
Deﬁnition 9.4. Let τ be a G-valued 0-cochain on X, i.e. a function from the vertices to G.
The coboundary of τ is the G-cocycle
(9.1)
δτ(⟨v0, v1⟩) = (τ v0)−1τ v1,
where ⟨v0, v1⟩is the edge from v0 to v1 and τ vi is the value of τ at vi. The coboundary action
of τ on G-cocycles is given by taking σ to the cocycle
(9.2)
τσ: ⟨v0, v1⟩7→(τ v0)−1σ(⟨v0, v1⟩)τ v1.
Given a simplex ∆, let ∆and ∆denote the corresponding truncated, and doubly truncated
simplices.
Deﬁnition 9.5. Let H ⊂G be groups. A (G, H)-cocycle on ∆is a G-cocycle where short
edges are labed by elements in H.
Deﬁnition 9.6. Let K ⊂H ⊂G be groups. A (G, H, K)-cocycle on ∆is a G-cocycle where
short edges are labeled by elements in K, and middle edges by elements in H.
Remark 9.7. Note that every (G, H)-cocycle on ∆can be obtained from a unique (G, H, {e})-
cocycle on ∆by collapsing the short edges. We shall thus always regard a cocycle on ∆as
a cocycle on ∆.
9.2.1. Labeling conventions. We index the vertices of ∆by ordered pairs of distinct vertices
of ∆, v0v1 being the vertex near v0 on the edge to v1. We index the vertices of ∆by ordered
triples of distinct vertices of ∆, v0v1v2 being the vertex, whose closest vertex in ∆is v0,
closest edge v0v1, and closest face v0v1v2. Given a cocycle on ∆, we use α’s to denote the
labeling of long edges, β’s for the middle edges, and γ’s for the short edges. Note that an
edge of each type is uniquely determined by its initial vertex. This gives a unique labeling
scheme, e.g. the long edge from v0v1v2 to v1v0v2 is labeled by βv0v1v2. Similarly, if τ is a
0-cochain, the value at v0v1v2 is denoted by τ v0v1v2. We shall not need a labeling scheme
for cocycles on truncated simplices. By Remark 9.7 we can regard these as cocycles on the
corresponding doubly truncated simplices.
