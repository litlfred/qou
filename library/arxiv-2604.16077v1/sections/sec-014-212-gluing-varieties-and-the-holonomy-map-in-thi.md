---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-014-212-gluing-varieties-and-the-holonomy-map-in-thi
section_title: "Gluing varieties and the holonomy map. In this section we explain how the structures"
section_number: 2.1.2
pages: 10-12
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
carried by quantum 3-simplices can be globalized on ideal tr iangulations.
Let M be a cusped manifold, i.e. an oriented non-compact 3-manifo ld admitting a complete
hyperbolic metric of ﬁnite volume. We denote by ¯M the compact manifold with interior M ;
∂ ¯M is a union of p tori.
Let T be an ideal triangulation of M , i.e. a gluing by simplicial face pairings of tetrahedra
with truncated (“ideal”) vertices, homeomorphic to M .
Denote by ∆ 1,..., ∆n the tetrahedra of T , with the orientation induced from M . We call
abstract tetrahedra and abstract edges of T the tetrahedra ∆ i and their edges before their
gluings in T . Give each tetrahedron ∆ i a branching bi, as deﬁned in Section 2.1.1. Denote by
b the collection of these local branchings bi. We do not ask that they match along common
edges (so we can choose each bi so that ∗bi(∆i) = 1). We note however that for such global
branchings b, when they exist (like for ( T,b ) in Figure 1), the QHI state sums have the
simplest form ([7]).
Deﬁnition 2.1. The quantum gluing variety GN (T,b ) is the set of tuples w := (w1,..., wn) ∈
C3n, where wi = ( wi
0, wi
1, wi
2) is a triple of quantum shape parameters on (∆ i,bi), i =
1,...,n , as in Section 2.1.1, satisfying the following edge relation at each edge e of T :
(9)
∏
E→e
w(E)∗E (∆) =e− 2πi
N .
Here the product is over all the abstract edges E identiﬁed to e in T (which is denoted
E → e), w(E) is the quantum shape parameter of E in the corresponding tetrahedron ∆ i,
and ∗E(∆) is its branching sign.
Note that the branching b enters the deﬁnition of GN (T,b ) only in that it speciﬁes a concrete
model of the space in C3n. Diﬀerent branchings yield isomorphic spaces. In [7, Sectio n 3B
and 4C] the space GN (T,b ) was denoted G0(T,b,c )N .
ForN = 1, G(T,b ) := G1(T,b ) is Thurston’s gluing variety associated to T , since in this case
wi = wi is a triple of shape parameters ( wi
0,wi
1,wi
2) for the tetrahedron ∆ i, satisfying the
edge relations ∏
E→ew(E)∗E (∆) = 1 (with the notations of (9)).
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 11
It is a well-known fact that G(T,b ) ⁄= ∅ if all the edges e of T are essential, i.e., e ∩ ¯M is
not homotopic to an arc in ∂ ¯M by a homotopy ﬁxing the endpoints. In that case we have
GN (T,b ) ⁄= ∅ (see Theorem 2.7). Moreover, denote by ˜M the universal cover of M . By
“straightening” the tetrahedra of T by means of an isometry ˜M → H3, one can see that if
G(T,b ) ⁄= ∅, then the character ρhyp of the discrete faithful representations of π1(M ) into
PSL (2, C) is encoded by a point of G(T,b ).
More generally, when G(T,b ) is non-empty it is related to the variety X(M ) of PSL (2, C)-
characters of M as follows (see e.g. [49, 14, 44]). Recall that X(M ) is the aﬃne algebraic set
consisting of representations π1(M ) → PSL (2, C) up to the equivalence relation of having
the same trace on each element of π1(M ). Denote by ˜M the universal cover of M . Any
point w ∈ G(T,b ) determines a pseudo-developing map Dw : ˜M → H3, unique up to post-
composition with an isometry, which sends a lift ˜∆i of the tetrahedron ∆ i to a hyperbolic
ideal tetrahedron with shape parameters ( wi
0,wi
1,wi
2). A pseudo-developing map Dw deﬁnes
a representation ρw : π1(M ) → PSL (2, C) by Dw(γ.x) = ρw(γ)Dw(x) for all γ ∈ π1(M ),
x ∈ ˜M . Diﬀerent choices of developing maps Dw yield conjugate representations ρw. The
resulting holonomy map (denoting again by ρw the character of a representation ρw)
(10) hol : G(T,b ) − → X(M )
w ↦− →ρw
is regular, and generically 2 : 1. More will be said about it in Section 2.2.2. For the moment,
let us note that in general hol is not surjective (for instance, by the construction of pseu do-
developing maps it is not hard to see that the image of hol cannot contain any character of
reducible representations).
The Thurston gluing variety G(T,b ) and the map hol have good properties when T is a
geometric triangulation, in the following sense.
Deﬁnition 2.2. We say that T is a geometric triangulation of M when:
• either the edges of T are isotopic to geodesics in the complete hyperbolic struct ure
of M , and these geodesics triangulate M into tetrahedra with non zero volume and
disjoint interiors;
• orT is obtained by subdividing the Epstein-Penner canonical po lyhedral decomposi-
tion of M (then some tetrahedra may be ﬂat, i.e., of zero volume).
In the former case we say that T is a positive triangulation, as it can be isotoped to a gluing
of positively oriented hyperbolic ideal tetrahedra corres ponding to the ∆ i, with classical
shape parameters satisfying I(whyp(E)∗E (∆)) > 0 for every abstract edge E of T . Such
triangulations are produced, e.g., by the software program SnapPy [24]. In general, when T
is geometric there exists a point whyp ∈G(T,b ) such that
hol(whyp) = ρhyp, and I(whyp(E)∗E (∆)) ≥ 0 for every abstract edge E of T.
For a geometric triangulation T the following facts hold true (see [49], [14, Chapter E.6 and
Proposition 7.7], [53] and [52, Proposition 3.5-3.6], [22] and [44, Proposition 15.3.4]):
(i) dim C(G(T,b )) = p, the number of cusps of M (this is also the dimension of the
geometric component Xhyp(M ) of X(M ), see Section 2.2.2);
(ii) there is a unique point whyp as above, it is a smooth point of G(T,b ), and a neigh-
borhood of whyp parametrizes a space of (non complete) hyperbolic structur es on
M .
Now let w := (w1,...,w n) ∈G(T,b ), where wi := (wi
0,wi
1,wi
2) as usual.
