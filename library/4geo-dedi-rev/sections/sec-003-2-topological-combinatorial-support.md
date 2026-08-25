---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-003-2-topological-combinatorial-support
section_title: "Topological-combinatorial support"
section_number: 2
pages: 7-8
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
doc_brief: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds — 27 sections: ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE"
---
We ﬁx a compact closed oriented smooth surfaceS0 of genusg, and a subset P ={p1,...,p r}⊂ S0
of r≥ 1 marked points. We denote by S the punctured surface S 0\P . We assume that
m :=−χ(S) = (2g− 2) +r> 0.
A diﬀeomorphism φ0 : S0 → S0 such that φ0(pj) = pj for every j induces a diﬀeomorphism
φ :S→S. Consider the cylinder C0 := S0× [0, 1] with the product orientation. Denote by M0 the
mapping torus of φ0 with the induced orientation. That is, M0 :=C0/∼φ0, where (x, 0)∼φ0 (y, 1) if
y =φ0(x), x,y∈S0. Let ˆM0 be the space obtained by collapsing to one point xj the image in M0 of
each line pj× [0, 1] in C0. Then ˆM0 is a pseudo-manifold; X ={x1,...,x r} is the set of singular (ie.
non manifold) points of ˆM0. Every singular point xj has a conical neighbourhood homeomorphic to
the quotient of T 2
j× [0, 1] by the equivalence relation identifying T 2
j×{ 0} to a point, where T 2
j is a
2-torus. The point xj corresponds to the coset of T 2
j ×{ 0}, and T 2
j ×{ 1} is called the link of xj in
ˆM0. So M = ˆM0\X is the interior of a compact manifold ¯M with boundary formed by r tori. In
fact M is the mapping torus Mφ =C/∼φ, where C =S× [0, 1]. From now on, we denote by Mφ the
manifold M endowed with this ﬁbration over the circle S1, and by Cφ the mapping cylinder of φ.
Layered triangulations of Mφ can be constructed as follows (see for instance [10], where one can
ﬁnd also a proof of the well known fact that two ideal triangulations of S are connected by a ﬁnite
chain of diagonal exchanges). Consider the set of triangulations λ ofS0 whose sets of vertices coincide
with P . By removing P , such a triangulation λ is also said an ideal triangulation of S; it has 3 m
edges and 2m triangles. Denote by λ′ =φ0(λ) the image ideal triangulation of S. Let us ﬁx a chain
of diagonal exchanges connecting λ to λ′:
λ =λ0→λ1→···→ λk =λ′.
Possibly by performing some additional diagonal exchanges followed by their inverses, we can assume
that this chain is “full”, in the sense that every edge of λ supports some diagonal exchange in the
chain. Then the chain induces a 3-dimensional triangulation T of ˆM0, whose tetrahedra are obtained
by “superposing”, for everyj, the two squares ofλj,λj+1 involved in the diagonal exchangeλj→λj+1
(see Figure 1). The set of vertices of T coincides with X. The ideal triangulation T\X is called a
layered triangulation of Mφ. It lifts to a layered triangulation TCφ of the cylinder Cφ.
For each tetrahedron of T , we call abstract tetrahedron its underlying simplicial set considered
independently of the face pairings in T . Similarly we call abstract edge or face of T any edge or face
of an abstract tetrahedra of T . Given any edge e ofT , we write E→e to mean that an abstract edge
E is identiﬁed to e in the triangulation T .
From now on we assume that the diﬀeomorphismφ ofS is pseudo-Anosov, so thatMφ is a hyperbolic
manifold with r cusps.
By construction every (ideally triangulated) surface ( S,λj) is embedded in T and TCφ. The union
of the surfaces (S,λj) forms the 2-skeletons of T and TCφ. Every surface ( S,λj) divides Mφ locally,
and the given orientations of S and Mφ determines the (local) positive side of S in M. In terms
of TCφ, the positive side of ( S,λ ) = ( S,λ 0) lifts to a collar of S×{ 0}, while the negative side of
(S,λ′) = (S,λk) lifts to a collar of S×{ 1}.
The triangulation T is naturally endowed with a taut pre-branching ω. Let us recall brieﬂy this
notion (see [6], [10]). A taut pre-branching is a choice of transverse co-orientation for each 2-face
of T , so that for every tetrahedron, exactly two of its 2-face co-orientations point inward/outward;
moreover, it is required that there are exactly two abstract diagonal edges E→ e for every edge e
of T . Here, we call diagonal edges the two edges of an abstract tetrahedron whose adjacent 2-face
co-orientations point both inward or both outward. The taut pre-branching ω of T is deﬁned by the
system of transverse 2-face co-orientations dual to the orientation of the embedded surfaces ( S,λj).
We ﬁx also aweak branching ˜b compatible withω (see [5]). Recall that ˜b is a choice of vertex ordering
b for each abstract tetrahedron of T , called (local) branching, satisfying the following constraint. The
ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS 7
abstract 2-faces of the tetrahedron have an orientation induced byb, given by their vertex orderings up
to even permutations. Then, it is required that these orientations match, under the 2-face pairings,
with the orientations dual to ω (note that we do not require that the abstract vertex orderings
match: this deﬁnes the stronger notion of global branching). Similarly, ˜b gives an orientation to every
tetrahedron; without loss of generality, we can assume that it agrees with the orientation of M. A
weak branching ˜bj is also deﬁned on every surface triangulation λj, by giving every triangle τ in λj
the branching induced by the tetrahedron lying on the positive side of τ.
In Figure 1 we show a typical local conﬁguration occurring in T or TCφ, that is, a tetrahedron ∆,
represented under an orientation preserving embedding in R3, built by gluing squares Q,Q′ along the
boundary, carrying triangulations λ, λ′ related by a diagonal exchange. The orientation of ∆ agrees
with the standard orientation of R3, and the 2-face co-orientations that deﬁne the pre-branching ω
are dual to the counter-clockwise orientation of the four faces of ∆. We have chosen one branching
b of ∆ (any edge being oriented from the lowest to the biggest endpoint) among the two which are
compatible with ω and induce the given orientation of ∆. The 2-faces are ordered as the opposite
vertices are, accordingly with b.
We advertize that Figure 1 will be used to support all computations. In such a situation we will
denote by e0 the edge [v0,v 1], by e1 the edge [v1,v 2], and by e2 the edge [v0,v 2].
Q Q’
∆
0
32
1
3
1
2
0
Figure 1.
