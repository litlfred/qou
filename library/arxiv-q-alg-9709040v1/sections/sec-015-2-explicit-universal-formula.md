---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-015-2-explicit-universal-formula
section_title: "Explicit universal formula"
section_number: 2
pages: 4-7
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
Here we propose a formula for the star-product for arbitrary Poisson structure α in an open domain
of the standard coordinate space Rd. Terms of our formula modulo O(¯h3) are the same as in the previous
section, plus a gauge-trivial term of order O(¯h2), symmetric in f and g. Terms of the formula are certain
universal polydiﬀerential operators applied to coeﬃcient s of the bi-vector ﬁeld α and to functions f,g . All
indices corresponding to coordinates in the formula appear once as lower indices and once as upper indices,
i.e. the formula is invariant under aﬃne transformations of Rd.
In order to describe terms proportional to ¯ hn for any integer n≥ 0, we introduce a special class Gn of
oriented labeled graphs.
4
Deﬁnition. An (oriented) graph Γ is a pair (VΓ,E Γ ) of two ﬁnite sets such that EΓ is a subset of VΓ×VΓ .
Elements of VΓ are vertices of Γ, elements of EΓ are edges of Γ. If e = (v1,v 2)∈ EΓ ⊆ VΓ ×VΓ is an
edge then we say that e starts at v1 and ends at v2.
In the usual deﬁnition of graphs one admits inﬁnite graphs, a nd also graphs with multiple edges. Here
we will not meet such structures and use a simpliﬁed terminol ogy.
We say that a labeled graph Γ belongs to Gn if
1) Γ has n + 2 vertices and 2 n edges,
2) the set vertices VΓ is{1,...,n }⊔{ L,R}, where L,R are just two symbols (capital roman letters,
mean Left and Right),
3) edges of Γ are labeled by symbols e1
1,e 2
1,e 1
2,e 2
2,...,e 1
n,e 2
n,
4) for every k∈{ 1,...,n } edges labeled by e1
k and e2
k start at the vertex k,
5) for any v∈VΓ the ordered pair ( v,v ) is not an edge of Γ.
The set Gn is ﬁnite, it has
(
n(n + 1)
) n
elements for n≥ 1 and 1 element for n = 0.
To each labeled graph Γ ∈Gn we associate a bidiﬀerential operator
BΓ ,α :A×A−→A, A =C∞(V), V is an open domain in Rd
which depends on bi-vector ﬁeld α∈ Γ(V,∧2TV ), not necessarily a Poisson one. We show one example, from
which the general rule should be clear. Here n = 3 and the list of edges is
(
e1
1,e 2
1,e 1
2,e 2
2,e 1
3,e 2
3
)
=
(
(1,L ), (1,R ), (2,R ), (2, 3), (3,L ), (3,R )
)
.
. .
.
2
3
L R
1
 1
2
3
5
.
.
6i
i i
i
i
4i
In the picture of Γ we put independent indices 1 ≤ i1,...,i 6≤d on edges, instead of labels e∗
∗. The
operator BΓ ,α corresponding to this graph is
(f,g )↦→
∑
i1,...,i 6
αi1i2αi3i4∂i4 (αi5i6 )∂i1∂i5 (f )∂i2∂i3∂i6 (g) .
The general formula for the operator BΓ ,α is
BΓ ,α (f,g ) :=
∑
I:EΓ−→{1,...,d }


n∏
k=1

 ∏
e∈EΓ , e =(∗,k )
∂I(e)

αI(e1
k)I(e2
k)

×
×

 ∏
e∈EΓ , e =(∗,L )
∂I(e)

f×

 ∏
e∈EΓ , e =(∗,R )
∂I(e)

g .
5
In the next step we associate a weight WΓ ∈ R with each graph Γ ∈Gn. In order to deﬁne it we need
an elementary construction from hyperbolic geometry.
Let p,q, p⁄= q be two points on the standard upper half-plane H ={z∈ C| Im(z) > 0} endowed
with the Lobachevsky metric. We denote by φh(p,q )∈ R/2πZ the angle at p formed by two lines, l(p,q )
and l(p,∞) passing through p and q, and through p and the point ∞ on the absolute. The direction of the
measurement of the angle is counterclockwise from l(p,∞) to l(p,q ). In the notation φh(p,q ) letter h is for
harmonic.
φ
pq
8
. .
An easy planimetry shows that one can express angle φh(p,q ) in terms of complex numbers:
φh(p,q ) = Arg((q−p)/(q−p)) = 1
2iLog
( (q−p)(q−p)
(q−p)(q−p)
)
.
Functionφh(p,q ) can be deﬁned by continuity also in the case p,q∈H⊔ R, p⁄=q.
Denote byHn the space of conﬁgurations of n numbered pairwise distinct points on H:
Hn ={(p1,...,p n)|pk∈H, pk⁄=pl for k⁄=l} .
Hn⊂ Cn is a non-compact smooth 2 n-dimensional manifold. We introduce orientation on Hn using the
natural complex structure on it.
If Γ ∈Gn is a graph as above, and ( p1,...,p n)∈H n is a conﬁguration of points, then we draw a copy
of Γ on the plane R2≃ C by assigning point pk∈H to the vertex k, 1≤ k≤n, point 0 ∈ R⊂ C to the
vertexL, and point 1 ∈ R⊂ C to the vertex R. Each edge should be drawn as a line interval in hyperbolic
geometry. Every edge e of the graph Γ deﬁnes an ordered pair ( p,q ) of points on H⊔ R, thus an angle
φh
e :=φh(p,q ). If points pi move around, we get a function φh
e onHn with values in R/2πZ.
We deﬁne the weight of Γ as
wΓ := 1
n!(2π)2n
∫
Hn
n⋀
i=1
(dφh
e1
k
∧dφh
e2
k
) .
Lemma. The integral in the deﬁnition of wΓ is absolutely convergent.
This lemma is a particular case of a more general statement pr oven in section 6.
Theorem. Let α be a Poisson bi-vector ﬁeld in a domain of Rd. The formula
f ⋆g :=
∞∑
n=0
¯hn ∑
Γ∈Gn
wΓBΓ ,α (f,g )
6
deﬁnes an associative product. If we change coordinates, we obtain a gauge equivalent star-product.
The proof of this theorem is elementary, it uses only the Stok es formula. Again, this theorem is a
corollary of a more general statement proven in section 6.
