---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-009-9-the-state-sum-tqft
section_title: "The state-sum TQFT"
section_number: 9
pages: 26-31
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
We construct in this section the state sum TQFT associated with any spherical
fusion category with invertible dimension.
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 27
9.1. Preliminaries on TQFTs. For convenience of the reader, we outline a def-
inition of a 3-dimensional Topological Quantum Field Theory (TQFT) re ferring
for details to [Tu]. We ﬁrst deﬁne a category of 3-dimensional cobor disms Cob 3.
Objects of Cob 3 are closed oriented surfaces. A morphism Σ 0 → Σ 1 in Cob 3
is represented by a pair ( M,h ), where M is a compact oriented 3-manifold and
h is an orientation-preserving homeomorphism ( −Σ 0)⊔ Σ 1 ≃ ∂M . Two such
pairs (M,h : (−Σ 0)⊔ Σ 1→ ∂M ) and ( M ′,h ′ : (−Σ 0)⊔ Σ 1→ ∂M ′) represent the
same morphism Σ 0 → Σ 1 if there is an orientation-preserving homeomorphism
F : M → M ′ such that h′ = Fh . The identity morphism of a surface Σ is rep-
resented by the cylinder Σ × [0, 1] with the product orientation and the tauto-
logical identiﬁcation of the boundary with ( −Σ)⊔ Σ. Composition of morphisms
in Cob 3 is deﬁned through gluing of cobordisms: the composition of morphism s
(M0,h 0) : Σ 0 → Σ 1 and (M1,h 1) : Σ 1 → Σ 2 is represented by the pair ( M,h ),
where M is the result of gluing M0 to M1 along h1h−1
0 : h0(Σ 1)→ h1(Σ 1) and
h =h0|Σ 0⊔h1|Σ 2 : (−Σ 0)⊔ Σ 2≃∂M . The category Cob 3 is a symmetric monoidal
category with tensor product given by disjoint union. The unit obje ct of Cob 3 is
the empty surface ∅ (which by convention has a unique orientation).
Denote vect k the category whose objects are ﬁnitely generated projective k-
modules and whose morphisms are k-homomorphisms of modules. We view vect k
as a symmetric monoidal category with standard tensor product a nd unit object
k. A 3-dimensional TQFT is a symmetric monoidal functor Z : Cob 3→ vectk. In
particular, Z(∅) = k, Z(Σ⊔ Σ ′) = Z(Σ)⊗Z(Σ ′) for any closed oriented surfaces
Σ, Σ ′, and similarly for morphisms.
Each compact oriented 3-manifold M determines two morphisms ∅→ ∂M and
−∂M →∅ in Cob 3. The associated homomorphisms Z(∅) = k → Z(∂M ) and
Z(−∂M )→ Z(∅) = k are denoted Z(M,∅,∂M ) and Z(M,−∂M,∅), respectively.
If ∂M =∅, then Z(M,∅,∂M ) = Z(M,−∂M,∅) : k→ k is multiplication by an
element of k denoted Z(M ).
The category Cob 3 includes as a subcategory the category of closed oriented sur-
faces and (isotopy classes of) orientation-preserving homeomor phisms of surfaces.
Indeed, any such homeomorphism f : Σ → Σ ′ determines a morphism Σ → Σ ′
in Cob 3 represented by the pair ( C = Σ ′× [0, 1],h : (−Σ) ⊔ Σ ′ ≃ ∂C ), where
h(x) = ( f (x), 0) for x∈ Σ and h(x′) = ( x′, 1) for x′∈ Σ ′. Restricting a TQFT
Z : Cob 3→ vectk to this subcategory, we obtain the action of homeomorphisms
induced by Z.
An isomorphism of 3-dimensional TQFTs Z1→ Z2 is a natural monoidal iso-
morphism of functors. Such an isomorphism is a system of k-isomorphismsZ1(Σ)≃
Z2(Σ), where Σ runs over all closed oriented surfaces. These k-isomorphisms should
be multiplicative with respect to disjoint unions of surfaces and comm ute with the
action of cobordisms (and in particular, of homeomorphisms). For Σ =∅, the iso-
morphism Z1(Σ) ≃Z2(Σ) should be the identity map k→ k. This implies that if
two TQFTs Z1, Z2 are isomorphic, then Z1(M ) = Z2(M ) for any closed oriented
3-manifold M .
9.2. Invariants of I-colored graphs. Fix up to the end of Section 9 a spherical
fusion category C over k such that dim(C) is invertible in k. Fix a representative
set I of simple objects of C. We shall derive from C and I a 3-dimensional TQFT.
By an I-colored graph in a surface, we mean a C-colored graph such that the
colors of all edges belong to I and all vertices have valence ≥ 2. For any compact
oriented 3-manifold M and any I-colored graph G in ∂M , we deﬁne a topological
invariant|M,G|∈ k as follows. Pick a skeleton P⊂M of the pair ( M,G ). Pick a
map c : Reg(P )→I extending the coloring of G in the sense that for every edge a
of G, the value of c on the region of P adjacent to a is theC-color of a. For every
28 V. TURAEV AND A. VIRELIZIER
oriented edge e of P , consider the k-module Hc(e) = H(Pe), where Pe is the set
of branches of P at e turned into a cyclic C- set as in Section 5.2. Let E0 be the
set of oriented edges of P with both endpoints in Int( M ), and let E∂ be the set
of edges of P with exactly one endpoint in ∂M oriented towards this endpoint.
Note that every vertex v of G is incident to a unique edge ev belonging to E∂ and
Hc(ev) = Hv(Gop;−∂M ), where the orientation of ∂M is induced by that of M .
Therefore
⊗e∈E∂ Hc(e)⋆ =⊗vHv(Gop;−∂M )⋆ =H(Gop;−∂M )⋆.
For e∈ E0, the equality Peop = (Pe)op induces a duality between the modules
Hc(e), Hc(eop) and a contraction Hc(e)⋆⊗Hc(eop)⋆→ k. This contraction does
not depend on the orientation of e up to permutation of the factors. Applying these
contractions, we obtain a homomorphism
∗P : ⊗e∈E0∪E∂ Hc(e)⋆−→⊗ e∈E∂ Hc(e)⋆ =H(Gop;−∂M )⋆.
As in Section 6.2, any vertex x ofP lying in Int(M ) determines an oriented graph Γ x
on S2, and the mapping c turns Γ x into an I-colored graph. Section 3.3 yields a
tensor FC(Γ x)∈ Hc(Γ x)∗. Here Hc(Γ x) = ⊗eHc(e), where e runs over all edges
of P incident to x and oriented away from x. The tensor product ⊗x FC(Γ x) over
all vertices x of P lying in Int(M ) is a vector in ⊗e∈E0∪E∂ Hc(e)⋆.
Theorem 9.1. For a skeleton P of (M,G ), set
|M,G| = (dim(C))−|P |∑
c

 ∏
r∈Reg(P )
(dimc(r))χ(r)

∗P (⊗x FC(Γ x)),
where|P| is the number of components of M\P ,c runs over all maps Reg(P )→I
extending the coloring of G, and χ is the Euler characteristic. Then |M,G| ∈
H(Gop;−∂M )⋆ does not depend on the choice of P .
Proof. Since any two skeletons of ( M,G ) are related by primary moves, we need
only to verify the invariance of |M,G| under these moves. This invariance is a local
property veriﬁed exactly as in the proof of Theorem 6.1. □
Though there is a canonical isomorphism H(Gop;−∂M )⋆≃H(G;∂M ) (see the
last remark of Section 3.1), we view |M,G| as an element of H(Gop;−∂M )⋆.
TakingG =∅, we obtain a scalar topological invariant |M|C =|M,∅|∈ H(∅)⋆ =
k of M . This generalizes the invariant deﬁned above for closed M .
9.3. Invariants of 3-cobordisms. A 3-cobordism is a triple ( M, Σ 0, Σ 1), where
M is a compact oriented 3-manifold and Σ 0, Σ 1 are disjoint closed oriented surfaces
contained in ∂M such that ∂M = (−Σ 0)⊔ Σ 1 in the category of oriented manifolds.
We call Σ 0 and Σ 1 the bottom base and the top base of M , respectively.
Consider a 3-cobordism (M, Σ 0, Σ 1) and an I-colored graph Gi⊂ Σ i fori = 0, 1.
Theorem 9.1 yields a vector
|M,G op
0 ∪G1|∈ H(G0∪Gop
1 ,−∂M )⋆ =H(G0, Σ 0)⋆⊗H(Gop
1 ,−Σ 1)⋆.
The isomorphism H(Gop
1 ,−Σ 1)⋆ ≃ H(G1, Σ 1) given by the last remark of Sec-
tion 3.1 induces an isomorphism
Υ : H(G0, Σ 0)⋆⊗H(Gop
1 ,−Σ 1)⋆→ Homk
(
H(G0, Σ 0),H (G1, Σ 1)
)
.
Set
|M, Σ 0,G 0, Σ 1,G 1| = (dim(C))|G1|
dim(G1) Υ
(
|M,G op
0 ∪G1|
)
: H(G0; Σ 0)→H(G1; Σ 1),
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 29
where for an I-colored graph G in a surface Σ, the symbol |G| denotes the num-
ber of components of Σ \G and dim(G) denotes the product of the dimensions of
the objects of C associated with the edges of G. To compute the homomorphism
|M, Σ 0,G 0, Σ 1,G 1|, let Ω ∈H(G1, Σ 1)⊗H(Gop
1 ,−Σ 1) be the inverse of the canon-
ical pairing H(Gop
1 ,−Σ 1)⊗H(G1, Σ 1)→ k. Pick any expansion Ω = ∑
αaα⊗bα,
where aα∈H(G1, Σ 1) and bα∈H(Gop
1 ,−Σ 1). Then for any h∈H(G0, Σ 0),
|M, Σ 0,G 0, Σ 1,G 1|(h) = (dim(C))|G1|
dim(G1)
∑
α
|M,G op
0 ∪G1|(h⊗bα)aα.
By skeleton of a closed surface Σ we mean an oriented graph G⊂ Σ such that
all vertices of G have valence≥ 2 and all components of Σ \G are open disks. For
example, the vertices and the edges of a triangulation t of Σ (with an arbitrary
orientation of the edges) form a skeleton of Σ. For a graph G, denote by col(G) the
set of all maps from the set of edges of G to I.
Lemma 9.2. Let (M0, Σ 0, Σ 1), (M1, Σ 1, Σ 2) be two 3-cobordisms and (M, Σ 0, Σ 2)
be the 3-cobordism obtained by gluing M0 and M1 along Σ 1. For any I-colored
graphsG0⊂ Σ 0, G2⊂ Σ 2 and any skeleton G of Σ 1,
|M, Σ 0,G 0, Σ 2,G 2| =
∑
c∈col(G)
|M1, Σ 1, (G,c ), Σ 2,G 2|◦| M0, Σ 0,G 0, Σ 1, (G,c )|.
Proof. This is a direct consequence of the deﬁnitions since the union of a ske leton of
(M0,G op
0 ∪G) with a skeleton of ( M1,G op∪G2) is a skeleton of ( M,G op
0 ∪G2). □
9.4. The state-sum TQFT. For a skeleton G of a closed oriented surface Σ, set
|G; Σ|◦ =⊕c∈col(G)H((G,c ); Σ).
Given a 3-cobordism (M, Σ 0, Σ 1), we deﬁne for any skeletons G0⊂ Σ 0 andG1⊂ Σ 1
a homomorphism
|M, Σ 0,G 0, Σ 1,G 1|◦ :|G0; Σ 0|◦→|G1; Σ 1|◦
by
(13) |M, Σ 0,G 0, Σ 1,G 1|◦ =
∑
c0∈col(G0)
c1∈col(G1)
|M, Σ 0, (G0,c 0), Σ 1, (G1,c 1)|,
where|M, Σ 0, (G0,c 0), Σ 1, (G1,c 1)| : H((G0,c 0); Σ 0)→H((G1,c 1); Σ 1). Lemma 9.2
implies that for any cobordisms M0,M 1,M as in this lemma and for any skeletons
Gi⊂ Σ i with i = 0, 1, 2,
(14) |M, Σ 0,G 0, Σ 2,G 2|◦ =|M, Σ 1,G 1, Σ 2,G 2|◦◦|M, Σ 0,G 0, Σ 1,G 1|◦.
These constructions assign a ﬁnitely generated free module to eve ry closed oriented
surface with distinguished skeleton and a homomorphism of these mo dules to ev-
ery 3-cobordism whose bases are endowed with skeletons. This dat a satisﬁes an
appropriate version of axioms of a TQFT except one: the homomorp hism associ-
ated with the cylinder over a surface, generally speaking, is not the identity. There
is a standard procedure which transforms such a “pseudo-TQFT” into a genuine
TQFT and gets rid of the skeletons of surfaces at the same time. Th is procedure
is described in detail in a similar setting in [Tu], Section VII.3. The idea is th at if
G0,G 1 are two skeletons of a closed oriented surface Σ, then the cylinder cobordism
M = Σ × [0, 1] gives a homomorphism
p(G0,G 1) =|M, Σ×{ 0},G 0×{ 0}, Σ×{ 1},G 1×{ 1}|◦ :|G0; Σ|◦→|G1; Σ|◦.
Formula (14) implies that p(G0,G 2) = p(G1,G 2)p(G0,G 1) for any skeletons G0,
G1,G2 of Σ. Taking G0 =G1 =G2 we obtain that p(G0,G 0) is a projector onto a
30 V. TURAEV AND A. VIRELIZIER
direct summand |G0; Σ| of|G0; Σ|◦. Moreover, p(G0,G 1) maps |G0; Σ| isomorphi-
cally onto |G1; Σ|. The ﬁnitely generated projective k-modules{|G; Σ|}G, where
G runs over all skeletons of Σ, and the homomorphisms {p(G0,G 1)}G0,G1 form a
projective system. The projective limit of this system is a k-module,|Σ|, indepen-
dent of the choice of a skeleton of Σ. For each skeleton G of Σ, we have a “cone
isomorphism” of k-modules|G; Σ|∼=|Σ|. By convention, the empty surface ∅ has a
unique (empty) skeleton and |∅| = k.
Any 3-cobordism (M, Σ 0, Σ 1) splits as a product of a 3-cobordism with a cylin-
der over Σ 1. Using this splitting and Formula (14), we obtain that the homomor-
phism (13) carries |Σ 0|∼=|G0; Σ 0|⊂| G0; Σ 0|◦ into|Σ 1|∼=|G1; Σ 1|⊂| G1; Σ 1|◦
for any skeletons G0,G 1 of Σ 0, Σ 1, respectively. This gives a homomorphism
|M, Σ 0, Σ 1| :|Σ 0|→| Σ 1| independent of the choice of G0, G1.
An orientation preserving homeomorphism of closed oriented surfa cesf : Σ → Σ ′
induces an isomorphism |f| :|Σ|→| Σ ′| as follows. Pick a skeleton G of Σ. Then
G′ =f (G) is a skeleton of Σ ′, and|f| is the composition of the isomorphisms
|Σ|∼=|G; Σ|∼=|G′; Σ ′|∼=|Σ ′|.
Here the ﬁrst and the third isomorphisms are the cone isomorphisms and the middle
isomorphism is induced by the homeomorphism of pairs f : (Σ ,G )→ (Σ ′,G ′). It is
easy to check that |f| does not depend on the choice of G.
To accomplish the construction of the 3-dimensional TQFT |·| , we need only to
associate with every morphism ϕ : Σ 0→ Σ 1 in Cob 3 the induced homomorphism
|ϕ| :|Σ 0|→| Σ 1|. Represent ϕ by a pair ( M,h : (−Σ 0)⊔ Σ 1≃ ∂M ) as above. For
i = 0, 1 denote by Σ ′
i the surfaceh(Σ i)⊂∂M with orientation induced by the one in
Σ i. The 3-cobordism ( M, Σ ′
0, Σ ′
1) yields a homomorphism |M, Σ ′
0, Σ ′
1| :|Σ ′
0|→| Σ ′
1|.
The homeomorphism h : Σ i→ Σ ′
i induces an isomorphism |Σ i|∼=|Σ ′
i| for i = 0, 1.
Composing these three homomorphisms we obtain the homomorphism |ϕ| :|Σ 0|→
|Σ 1|. This homomorphism does not depend on the choice of the represen tative
pair (M,h ). It follows from the deﬁnitions and Lemma 9.2 that the assignment
Σ↦→|Σ|, ϕ↦→|ϕ| satisﬁes all the axioms of a TQFT. To stress the dependance of
C, we shall denote this TQFT by |·| C. Considered up to isomorphism, the TQFT
|·| C does not depend on the choice of the representative set I of simple objects of
C. For any closed oriented 3-manifold M , the invariant|M|C∈ k produced by this
TQFT coincides with the invariant of Sections 5 and 6.
9.5. Computation of |S2|C. To illustrate our deﬁnitions, we compute the k-
module|S2|C. A circle G⊂ R2⊂ R2∪{∞} = S2 oriented counterclockwise and
viewed as a graph with one vertex x and one edge e is a skeleton of S2. Assigning
i∈ I to e, we turn G into an I-colored graph Gi. By deﬁnition, the k-module
|S2|C is isomorphic to the image of the endomorphism p(G,G ) = ∑
i,j∈Ipj
i of
|G;S2|◦ =⊕i∈IH(Gi), where
pj
i =|Σ× [0, 1], Σ×{ 0},G i×{ 0}, Σ×{ 1},G j×{ 1}|C : H(Gi)→H(Gj).
To computepj
i , consider the 2-polyhedron P = (G×[0, 1])∪(S2×{ 1
2}) in S2×[0, 1].
We stratify P by taking as edges the arcs x× [0, 1
2 ], x× [ 1
2, 1], and e×{t} for
t∈{ 0, 1
2, 1}. The polyhedron P has 3 vertices x×{t} with t∈{ 0, 1
2, 1} and 4
disk regions. We orient the two regions adjacent to the boundary s o that P is a
skeleton of the pair ( S2× [0, 1], (Gop×{ 0})∪ (G×{ 1})) and endow the two regions
contained in S2×{ 1
2} with orientation induced by that of S2. Clearly,|P| = 4. Set
Gj
i = (Gop
i ×{ 0})∪ (Gj×{ 1})⊂∂(S2× [0, 1]).
The maps Reg( P )→ I extending the coloring of Gj
i are numerated by the colors
z,w ∈ I of the region contained in S2×{ 1
2}. The link of the vertex ( x, 1
2 ) of P
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 31
determines aC-colored graph Γ z,w inS2:
P =PSfrag replacements
i
j
z w , Γ z,w =
PSfrag replacements
i
j
z
w
i i
j j
z
w
.
Let u,v be the bottom and the top vertices of Γ z,w, respectively. Then
|S2× [0, 1],G j
i|C = dim(i) dim(j)
dim(C)4
∑
z,w∈I
dim(z) dim(w)µz,w
i,j
with
µz,w
i,j =∗P (FC(Γ z,w )) = FC


PSfrag replacements
i i
j j
z
w

∈Hu(Γ z,w )∗⊗Hv(Γ z,w)∗,
where the dotted line represents the tensor contraction. Note t hat Hu(Γ z) =
H(Gi) and Hv(Γ z) = H(Gop
j ). Set ai = τ −1
i (~coevi)∈ H(Gi) where τi : H(Gi)→
HomC(1,i ∗⊗i) is the cone isomorphism. Then the vector ai forms a basis of H(Gi).
Since H(Gop
j ) = H(Gj), Ω = (dim( j))−1aj⊗aj∈H(Gj)⊗H(Gop
j ) is the inverse
of the canonical pairing H(Gop
j )⊗H(Gj )→ k. Now
µz,w
i,j (ai⊗aj) = FC


PSfrag replacements
i
j
z
w

 =N 1
j∗⊗z∗⊗i⊗w
Therefore
pj
i (ai) = dim(C)2
dim(j)2|S2× [0, 1],G j
i|C(ai⊗aj)aj
= dim(i)
dim(j) dim(C)2
∑
z,w∈I
dim(z) dim(w)N 1
j∗ ⊗z∗⊗i⊗waj
= dim(i)2
dim(C) aj by the ﬁrst formula of Lemma 4.3.
We conclude that the image of p(G,G ) is generated by v =∑
j∈Iaj∈|G;S2|◦, and
so that|S2|C≃ k.
