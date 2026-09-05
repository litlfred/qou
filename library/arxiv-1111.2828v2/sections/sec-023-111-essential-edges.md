---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-023-111-essential-edges
section_title: "Essential edges"
section_number: 11.1
pages: 40-41
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
---
Deﬁnition 11.4. An edge of K is essential if the lifts to L have distinct end points.
Note that an edge may be essential even though it is homotopic ally trivial in K. Let L(0) denote
the zero skeleton of L.
Lemma 11.5. Let ρ be a representation in SL(2, C) or PSL(2, C). A decoration of ρ determines a
ρ-equivariant map
(11.9) D : L(0) → ∂H
3
= C ∪ {∞}, e i ↦→gi∞.
Every such map comes from a decoration, and the decoration is generic if and only if the vertices
of each simplex of L map to distinct points in C ∪ {∞}.
Proof. Equivariance of ( 11.9) follows from the deﬁnition of a decoration. A ρ-equivariant map
D : L(0) → C ∪ {∞} is uniquely determined by its image of lifts ~ei ∈ L of the zero cells ei of K.
Picking gi such that gi∞ = D(~ei), we deﬁne a decoration by assigning the coset giN to~ei. The last
statement follows from the fact that det(g1e1, g2e1) = 0 if and only if g1∞ = g2∞. □
In the following we assume that the interior of M is a cusped hyperbolic 3-manifold H3/Γ with
ﬁnite volume.
Proposition 11.6. If all edges of K are essential, the geometric representation has a generic
decoration.
Proof. We identify π1(M ) with Γ ⊂ PSL(2, C). Each vertex of L corresponds to either a cusp
of M or an interior point of M . Accordingly, we have L(0) = L(0)
cusp ∪ L(0)
int. Each point in L(0)
cusp
determines a parabolic subgroup of PSL(2, C) stabilizing a unique point in C ∪ {∞}. We thus have
an equivariant map D : L(0)
cusp → C ∪ {∞} taking a point to its stabilizer. Let e1 and e2 be points
in L(0)
cusp connected by an edge. Since all edges of K are essential, e1 ⁄= e2. It is well known that
the point stabilizers of diﬀerent cusps are distinct. Hence , D(e1) ⁄= D(e2) if e1 and e2 correspond
to diﬀerent cusps. If e1 and e2 correspond to the same cusp, there exists an element in Γ taking e1
to e2. Since only peripheral elements (i.e. cusp stabilizers) ha ve ﬁxed points in C ∪ {∞}, it follows
that D(e1) ⁄= D(e2). We extend D to L(0) by choosing any equivariant map L(0)
int → C ∪ {∞}. Since
such map is uniquely determined by ﬁnitely many values (whic h may be chosen freely), we can pick
the extension so that the vertices of each simplex map to dist inct points. This proves the result. □
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 41
Theorem 11.7. Suppose all edges of K are essential. The representation φn ◦ ρgeo is detected by
Pn(K) if n is odd, and by P σgeo
n (K) if n is even.
Proof. By Proposition 11.6, P σgeo
2 (K) detects ρgeo. The result now follows from Corollary 11.2. □
Remark 11.8. The census triangulations all have essential edges.
