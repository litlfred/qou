---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-003-3-invariants-of-colored-graphs
section_title: "Invariants of colored graphs"
section_number: 3
pages: 8-10
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
In this section, C is a pivotal k-category.
3.1. Colored graphs in surfaces. By a graph, we mean a ﬁnite graph without
isolated vertices. Every edge of a graph connects two (possibly co inciding) vertices
called the endpoints of the edge. We allow multiple edges with the same e ndpoints.
A graph G isC-colored, if each edge of G is oriented and endowed with an object
ofC called the color of the edge.
Let Σ be an oriented surface. By a graph in Σ, we mean a graph embedded
in Σ. A vertex v of aC-colored graph G in Σ determines a cyclic C- set (Ev,c v,ε v)
as follows: Ev is the set of half-edges of G incident to v with cyclic order induced
by the opposite orientation of Σ; the maps cv : Ev→ Ob(C) and εv : Ev→{ +,−}
assign to each half-edge e∈ Ev its color and sign (the sign is + if e is oriented
towardsv and− otherwise). Set Hv(G) = H(Ev) and
H(G) =⊗vHv(G),
where v runs over all vertices of G and⊗ =⊗k is the tensor product over k. To
stress the role of Σ, we shall sometimes write Hv(G; Σ) for Hv(G) and H(G; Σ)
for H(G).
For an n-valent vertex v of G, the k-module Hv(G) can be described as follows.
Let e1 <e 2 <··· <e n <e 1 be the half-edges of G incident to v with cyclic order
induced by the opposite orientation of Σ. Then Hv(G) = H((X1,ε 1),..., (Xn,ε n)),
whereXr =cv(er) and εr =εv(er) are the color and the sign of er forr = 1,...,n .
To simplify notation, we write H(X1ε1,...,X nεn) for this module. For exam-
ple, H(i+,j−,k +), H(j−,k +,i +), and H(k+,i +,j−) all stand for the module
associated to the trivalent vertexPSfrag replacements
i
j
k
Σ
.
Given twoC-colored graphs G andG′ in Σ, an isotopy ofG intoG′ is an isotopy
of G into G′ in the class of C-colored graphs in Σ preserving the vertices, the
edges, and the orientation and the color of the edges. An isotopy ι of G into G′
induces an isomorphism of cyclic C- sets Ev → Ev′ , where v is any vertex of G
and v′ =ι(v). This induces k-isomorphisms Hv(ι) :Hv(G)→Hv′ (G′) and H(ι) =
⊗vHv(ι) :H(G)→H(G′).
A duality between two vertices u, v of a C-colored graph G in Σ is a duality
between the cyclic C- sets Eu and Ev, see Section 2.3. Such a duality induces a
pairing ωu,v : Hu(G)⊗Hv(G)→ k and, when C is non-degenerate, a contraction
homomorphism∗u,v :Hu(G)⋆⊗Hv(G)⋆→ k.
AC-colored graph G⊂ Σ determines a C-colored graph Gop in−Σ obtained
by reversing orientation in all edges of G and in Σ while keeping the colors of the
edges. The cyclic C-sets determined by a vertex v of G and Gop are dual. If C is
non-degenerate, then we can conclude that
Hv(Gop;−Σ) = Hv(G; Σ) ⋆ and H(Gop;−Σ) = H(G; Σ) ⋆.
3.2. Invariants of graphs in R2. We always orient the plane R2 counterclockwise.
Let G be a C-colored graph in R2. For each vertex v of G, we choose a half-
edge ev∈ Ev and isotope G near v so that the half-edges incident to v lie above
v with respect to the second coordinate on R2 and ev is the leftmost of them.
Pick any αv∈ Hv(G) and replace v by a box colored with τ v
ev (αv) as depicted in
Figure 1, where τ v is the universal cone of Hv(G). This transforms G into a planar
diagram which determines, by the Penrose calculus, an element of En dC(1) = k
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 9PSfrag replacements
X
Y
Z
T
τ v
ev (αv)
ev
v
PSfrag replacements
X
Y
Z
T
τ v
ev (αv)
ev
v
PSfrag replacements
X
Y
Z
T
τ v
ev (αv)
ev
v
PSfrag replacements
X
Y
Z
T
τ v
ev (αv)
ev
v
PSfrag replacements
X
Y
Z
T τ v
ev (αv)
ev
v
.
Figure 1.
denoted FC(G)(⊗vαv). By linear extension, this procedure deﬁnes a vector FC(G)∈
H(G)⋆ = Hom k(H(G), k).
Lemma 3.1. The vector FC(G)∈ H(G)⋆ is a well-deﬁned isotopy invariant of a
C-colored graph G in R2. More precisely, for any isotopy ι between two C-colored
graphsG, G′ in R2, we have FC(G′)H(ι) = FC(G), where H(ι) :H(G)→H(G′) is
the isomorphism induced by ι.
Proof. Independence of FC(G) of the choice of the half-edges ev follows from the
deﬁnition of Hv(G). Invariance under isotopies follows from the pivotality of C. □
For example, if G = S1⊂ R2 is the unit circle with one vertex v = (1, 0) and
one edge oriented clockwise and colored with X∈ Ob(C), then Ev consists of two
elements labeled by ( X, +), (X,−) and H(G) = Hv(G)∼= HomC(1,X ∗⊗X). Here
FC(G)(α) = ev Xα∈ EndC(1) = k for all α∈H(G).
3.3. Invariants of graphs in S2. IfC is spherical, then the invariant FC gener-
alizes to graphs in the 2-sphere S2 = R2∪{∞} (the orientation of S2 extends the
counterclockwise orientation in R2). Let G be aC-colored graph in S2. Pushing, if
necessary,G away from∞, we obtain a C-colored graph G0 in R2. By Section 1.4,
FC(G) = FC(G0)∈H(G0)⋆ =H(G)⋆ does not depend on the way we push G in R2
and is an isotopy invariant of G.
We state a few properties of FC.
(i) If a C-colored graph G′⊂ S2 is obtained from a C-colored graph G⊂ S2
through the replacement of the color X of an edge by an isomorphic object
X ′, then any isomorphism X→ X ′ induces an isomorphism φ : H(G)→
H(G′) in the obvious way and φ⋆(FC(G′)) = FC(G). We call this property
of FC naturality.
(ii) If an edge e of aC-colored graph G⊂S2 is colored by 1 and the endpoints
of e are also endpoints of other edges of G, then FC(G) = FC(G\ Int(e)).
Indeed, in the Penrose calculus, e can be deleted without changing the
associated morphism.
(iii) If a C-colored graph G′⊂ S2 is obtained from a C-colored graph G⊂ S2
through the replacement of the color X of an edge e byX ∗ and the reversion
of the orientation of e, then the isomorphism ψX :X→X ∗∗ of Remark 1.5
induces an isomorphism ˆψ : H(G)→H(G′) and ( ˆψ)⋆(FC(G′)) = FC(G).
(iv) We have H(G∐G′) = H(G)⊗H(G′) and FC(G∐G′) = FC(G)⊗ FC(G′)
for any disjoint C-colored graphs G,G ′⊂S2.
Example 3.2. For an n-tuple S = ((X1,ε 1),..., (Xn,ε n)) of signed objects of C,
consider the following C- colored graph γ =γS in S2:
γ =
PSfrag replacements
X1
X2u v
Xn−1
Xn
.
10 V. TURAEV AND A. VIRELIZIER
The graph γ consists of n edges connecting the vertices u andv, the r-th edge being
colored with Xr and oriented towards v if εr = + and towards u otherwise (the
picture corresponds to ε1 =−,ε2 = +, εn =−). Then H(γ) = H(S∗)⊗H(S) and
FC(γ) = ωS : H(S∗)⊗H(S)→ k. The vertices u, v of γ are in duality induced by
the symmetry with respect to the vertical line and ωu,v =ωS = FC(γ).
Example 3.3. For any i,j,k,l,m,n ∈ Ob(C), consider the following C-colored
graph in S2:
Γ =
PSfrag replacements
i
jk
lm
nev
v
.
Here H(Γ) is the tensor product of the modules H(m+,i−,n−), H(j+,i +,k−),
H(n+,j−,l−), and H(l+,k +,m−). The vector FC(Γ)∈H(Γ) ⋆ and similar vectors
associated with other orientations of the edges of Γ form a family of 26 = 64 tensors
called 6j-symbols associated with i,j,k,l,m,n . For more on this, see Appendix.
