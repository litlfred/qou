---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-012-12-state-sum-invariants-of-links-in-3-manifolds
section_title: "State sum invariants of links in 3-manifolds"
section_number: 12
pages: 35-55
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
Fix a spherical fusion category C over an algebraically closed ﬁeld k such that
dimC⁄= 0. In this section, we extend the state-sum invariant of 3-cobor disms|·| C
to 3-cobordisms with Z(C)-colored links inside.
36 V. TURAEV AND A. VIRELIZIER
12.1. Knotted graphs in S2. By a knotted graph in S2, we mean a graph im-
mersed in S2 such that the multiple points of the immersion are double transversa l
crossings of edges, and at each crossing, one of the two intersec ting edges is distin-
guished and said to be “lower” or “under-passing”, the second edg e being “upper”
or “over-passing”. Note that some of the crossings may be self-c rossings of edges.
A knotted graph may have only a ﬁnite number of crossings, and the y all lie away
from the vertices of the graph.
A knotted graph G in S2 isC-colored if all its edges are oriented and endowed
with an object of C orZ(C) (called the color of the edge) so that, at each crossing,
the color of the over-passing edge is an object of Z(C). In other words, the color of
an edge e ofG is an object of Z(C) if e passes at least once over other edges or over
itself and is an object of Z(C) or C otherwise. By the quasi-color of e, we mean
the color of e if it is in Ob( C) and the underlying object of the color of e if it is in
Ob(Z(C)). In all cases, the quasi-color of e is in Ob(C). For example, the C-colored
graphs in S2 as in Section 3.1 are C-colored knotted graphs with no crossings.
Given twoC-colored knotted graphs G and G′ in S2, an isotopy of G intoG′ is
an isotopy of G into G′ in the class of C-colored knotted graphs in S2 preserving
the vertices, the edges, the crossings, and the orientation and t he color of the edges.
A vertex v of a C-colored knotted graph G in S2 determines a cyclic C- set
(Ev,c v,ε v) as in Section 3.1 with the only diﬀerence that the map cv : Ev→ Ob(C)
assigns to each half-edge e∈Ev its quasi-color. As in Section 3.1, we set Hv(G) =
H(Ev) and H(G) =⊗vHv(G), where v runs over all vertices of G.
The invariant FC of Section 3.3 extends to C-colored knotted graphs in S2 as
follows. Let G be a C-colored knotted graph in S2. Pushing, if necessary, G away
from∞, we obtain a C-colored knotted graph in R2, also denoted by G. For each
vertex v of G, we choose a half-edge ev ∈ Ev and isotope G near v so that the
half-edges incident to v lie above v with respect to the second coordinate on R2
and ev is the leftmost of them. Pick any αv ∈ Hv(G) and replace v by a box
colored with τ v
ev (αv), where τ v is the universal cone of Hv(G) (see Figure 1). For
each crossing c of G, isotope G near c so that both strands of G meeting at c
are oriented downwards. If ( A,σ ) is the color of the over-passing strand and X
the quasi-color of the under-passing strand, then we replace c by a box labeled
by σX provided the over-passing strand goes from top-right to bottom -left and
by σ−1
X provided the over-passing strand goes from top-left to bottom- right. This
transforms G into a planar diagram which determines, by the Penrose calculus,
an element of End C(1) = k. This element is denoted FC(G)(⊗vαv). By linear
extension, our procedure deﬁnes a vector FC(G)∈H(G)⋆ = Hom k(H(G), k).
Consider the local moves on C-colored knotted graphs in S2 shown in Figure 8.
It is understood that all strands are oriented (in an arbitrary way ), and the orienta-
tions of the strands are the same before and after the moves. Th e colors of all edges
are objects of C andZ(C) preserved under the moves. As above, the colors of all
over-passing edges are objects of Z(C). For example, the second move of Figure 8
is allowed only when the color of the left strand is in Z(C).
Lemma 12.1. The vector FC(G)∈H(G)⋆ is a well-deﬁned isotopy invariant of G
preserved under the moves in Figure 8.
Proof. Independence of FC(G) of the choice of the half-edges ev follows from the
deﬁnition of Hv(G). Invariance of FC(G) under isotopies of G follows from the
sphericity ofC.
We claim that, as in Section 3.3, if a C-colored knotted graph G′⊂S2 is obtained
from a C-colored knotted graph G⊂ S2 through replacement of the color of an
edge e by its dual and simultaneous reversion of the orientation of e, then the
isomorphism ψX : X→ X ∗∗ of Remark 1.5 (where X∈ Ob(C) is the quasi-color
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 37
, ,
Figure 8.
of e) induces an isomorphism ˆψ :H(G)→H(G′) such that ( ˆψ)⋆(FC(G′)) = FC(G).
This claim is veriﬁed by comparing the contributions of the vertices an d crossings
of G, G′ to FC(G), FC(G′) respectively. Indeed, without loss of generality, we can
assume that G⊂ R2 = S2\{∞} and G is generic with respect to the second
coordinate on R2. Consider a crossing x ofG with over-passing edge eo and under-
passing edge eu. Applying if necessary an isotopy to G in a neighborhood of x, we
can assume that eo is directed from top-left to bottom-right. Let ( A,σ )∈Z (C)
be the color of eo and X∈ Ob(C) be the quasi-color of eu. There are four cases
to consider depending on the orientation of eu at x (downwards or upwards) and
depending on whether we reverse the orientation of eo or eu. Assume that eu is
directed downwards at x, so that the contribution of x to FC(G) isPSfrag replacements
(A,σ )X X
X
A
A
σ−1
X .
If G′ is obtained by reversing eu and replacing its color with the dual object, then
the contribution of x to FC(G′) is
PSfrag replacements
(A,σ ) (A,σ )
≃ =
X
XX ∗ X ∗ X ∗
X ∗
X ∗
X ∗A
A
A
A
σ−1
XσX ∗
ψX
ψ−1
X
.
The last equality follows from the deﬁnition of ψX and the formula
σ−1
X = (~evX⊗ idA⊗X )(idX⊗σX ∗⊗ idX )(idX⊗A⊗ ~coevX ).
The latter formula can be easily deduced from the naturality of σ and Formula (15).
Similarly, if G′ is obtained by reversing eu and replacing its color with the dual
object, then the contributions of x to FC(G) and FC(G′) are obtained from each
other through conjugation by ψA (to see this, one should use the expression for
the dual of a half braiding given in Section 10.2). The case where eu is directed
upwards is treated similarly. Combining these local computations, we obtain the
required claim.
Consider the second move in Figure 8. Applying if necessary the prop erty of
FC obtained in the previous paragraph, we can reduce ourselves to th e case where
both strands are oriented downward. In this case the required ide ntity follows
38 V. TURAEV AND A. VIRELIZIER
from the deﬁnition of FC(G). Similarly, to prove the invariance of FC(G) under the
fourth move, it suﬃces to consider the case where all edges inciden t to the vertex
are oriented to the left. The required identity follows from the deﬁn itions and
the properties of σ. The invariance of FC(G) under the third move can be proved
similarly treating the crossing point of the two lower branches as a ve rtex. Finally,
the ﬁrst move expands as a composition of the other moves throug h pushing the
over-passing branch to the left across the rest of the diagram an d across the point
∞∈ S2. □
Note that Lemma 4.2 extends mutatis mutandis to C-colored knotted graphs
in S2.
12.2. Link diagrams. Let M be a compact oriented 3-manifold. Given a s-
skeletonP ofM , that is, a s-skeleton of the pair ( M,∅) in the sense of Section 8.1,
we can present links in M by diagrams in P , see [Tu, Chapter IX]. (Similar presen-
tations can be deﬁned on arbitrary skeletons of M , but s-skeletons will be suﬃcient
for our aims.) A link diagram in P is a ﬁnite set of loops in P such that:
(i) the loops do not meet the vertices of P and meet the edges of P transversely;
(ii) the loops have only double transversal crossings and self-cros sings lying in
Int(P ) = P\P (1);
(iii) at each crossing point of the loops one of the two intersecting br anches is
distinguished and said to be “lower”, the second branch being “uppe r”.
The underlying 4-valent graph of a link diagram is formed by the loops of the
diagram with over/under-crossing data forgotten. By abuse of n otation, we shall
usually denote a link diagram and its underlying graph by the same symb ol.
Each link diagram d inP determines a link ℓd⊂M as follows. The orientations
of M and P determine a distinguished normal direction on Int( P ) in M . Pushing
slightly all upper branches of d in M\P in this direction, we transform d intoℓd.
The underlying loops of d have a well-deﬁned normal line bundle bP (d) in P ; this
bundle is deﬁned in the points of d∩P (1) since, in a neighborhood of any such point,
d traverses two regions of P locally forming a 2-disk. The bundle bP (d) induces a
line subbundle bd of the (2-dimensional) normal bundle of ℓd in M .
An enriched link diagram in P is a link diagram in P whose loops are equipped
with half-integers called pre-twists. The pre-twist of a loop L is required to belong to
Z if the normal line bundle of L inP is trivial and to 1
2 +Z otherwise. The pre-twists
determine a framing of ℓd⊂M as follows. Twist bd around each component of ℓd
as many times as the pre-twist of the corresponding loop. (The pos itive direction
of the twist is determined by the orientation of M . For instance, a pre-twist of 1
2
gives rise to a positive half-twist of bd.) This produces a trivial normal line bundle
on ℓd. Its non-zero sections yield a framing of ℓd.
It is easy to see that every framed link in M may be represented by an enriched
link diagram in P . Consider the moves Ω 1,..., Ω 8 on enriched link diagrams shown
in Figure 9 where the orientation of M corresponds to the right-handed orientation
in R3. The moves Ω 1, Ω 2, Ω 3 proceed in Int(P ), and Ω 4,..., Ω 8 proceed in a neigh-
borhood of P (1). In Figure 9 the link diagrams on P are drawn in red bold in order
to distinguish them from the edges of P . The move Ω 1 decreases the pre-twist by 1
and Ω 4 increases the pre-twist by 1
2 ; the other moves do not change the pre-twists.
The move Ω 6 has four versions; in the one in Figure 9 we assume that the orienta-
tions of the horizontal regions are compatible, i.e., are induced by an orientation of
the horizontal plane. If these orientations are incompatible, then the picture must
be modiﬁed: the overcrossing on the left (or on the right) should be replaced with
an undercrossing. The third and fourth versions of Ω 6 are obtained from the ﬁrst
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 39
PSfrag replacements
Ω 1
−1
,PSfrag replacements
Ω 1
−1
Ω 2
,
PSfrag replacements
Ω 1
−1
Ω 2
Ω 3
,
PSfrag replacements
Ω 1
−1
Ω 2
Ω 3
Ω 4
1
2
PSfrag replacements
Ω 1
−1
Ω 2
Ω 3
Ω 4
1
2
Ω 5
PSfrag replacements
Ω 1
−1
Ω 2
Ω 3
Ω 4
1
2
Ω 5
Ω 6
PSfrag replacements
Ω 1
−1
Ω 2
Ω 3
Ω 4
1
2
Ω 5
Ω 6
Ω 8PSfrag replacements
Ω 1
−1
Ω 2
Ω 3
Ω 4
1
2
Ω 5
Ω 6
Ω 8
Ω 7.1
PSfrag replacements
Ω 1
−1
Ω 2
Ω 3
Ω 4
1
2
Ω 5
Ω 6
Ω 8
Ω 7.1
Ω 7.2
Figure 9. Moves Ω 1− Ω 8 on link diagrams
two by changing both overcrossings to undercrossings. The move Ω 7 has two ver-
sions; both apply only when the left horizontal region is oriented cou nterclockwise.
By [Tu], two enriched link diagrams in P represent isotopic framed links if and only
if these diagrams may be related by a ﬁnite sequence of moves Ω ±1
1 ,..., Ω ±1
8 and
ambient isotopies in P .
Oriented framed links in M can be similarly presented by oriented link diagrams
in P . These are the (enriched) link diagrams as above formed by oriente d loops.
Two such diagrams present isotopic oriented framed links if and only if they may
be related by the moves in Figure 9 where all strands are oriented (t he orientations
of the strands must be the same before and after the moves).
12.3. Invariants of links. A component K of a link L in a 3-manifold M is said
to be trivial if there is an embedded 2-disk D⊂ M such that K = ∂D = D∩L.
Consider a pair (M,L ), where M is a compact oriented 3-manifold and L⊂ Int(M )
is an oriented framed link whose all components are non-trivial and c olored by
simple objects of Z(C). We deﬁne an invariant |M,L|C ∈ k as follows. Fix a
(ﬁnite) representative set I of simple objects of C. Pick a s-skeleton P of M and
an oriented enriched link diagram d in P representing L. The set ~d = P (1)∪d is
a graph embedded in P with edges contained either in P (1) or in d and vertices of
three types: the vertices of P (1), the points of P (1)∩d, and the crossings of d. The
assumption that all components of L are non-trivial ensures that every component
of ~d contains at least one vertex, so that ~d is a graph in the sense of Section 3.1.
Cutting out P along ~d, we obtain a compact oriented surface whose components
40 V. TURAEV AND A. VIRELIZIER
are disks and disks with holes. These components are called the regions of d. The
set of regions of d is denoted by Reg( d).
Pick a map c : Reg(d)→I. For any oriented edge e of the graph ~d, we deﬁne a
k-module Hc(e). If e⊂P (1), then Hc(e) = H(Pe) as in Section 6.3. If e⊂d, then
there are two regions r−,r +∈ Reg(d) adjacent to e. We choose notation so that
the orientation of r+ (resp. r−) induces on e the orientation compatible with that
of e (resp. opposite to that of e):
PSfrag replacements
A
r+ r−
e
.
Let A∈ Ob(C) be the quasi-color of the component of L containing e. We turn
the 3-element set Pe ={r−,e,r +} into a cyclicC-set by providing it with the cyclic
order r− < e < r+ < r− and with the map to Ob( C)×{ +,−} carrying r± to
(c(r±),±) and e to (A,ε ), where ε = + if the orientations of e andd are compatible
and ε =− otherwise. Set
Hc(e) = H(Pe)∼= HomC(1,c (r−)∗⊗Aε⊗c(r+)).
It is clear that in both cases Peop = (Pe)op. This induces a duality between the
modules Hc(e), Hc(eop) and a contraction ∗e : Hc(e)⋆⊗Hc(eop)⋆→ k.
We now associate to every vertex x of ~d a certain vector |x|c. We distinguish
three cases. If x is a vertex of P (1), then as in Section 6.3, the link of x determines
aC-colored graph Γ x⊂S2. Set |x|c = FC(Γ x)∈Hc(Γ x)∗.
If x is a crossing of d, then a neighborhood of x in P looks as follows:
PSfrag replacements
i
j
k
J J ′
l
Here J and J ′ are the colors of the strands of d meeting at x, and i,j,k,l ∈ I
are the c-colors of the regions in Reg( d) adjacent to x. Let Γ x be the following
C-colored knotted graph in R2⊂S2:
Γ x =
PSfrag replacements
i
j
k
J J ′ l
The orientation (not shown in the picture) of the diagonals is induced by that of d.
Section 12.1 yields a tensor |x|c = FC(Γ x)∈Hc(Γ x)∗.
The deﬁnition of|x|c in the remaining case x∈P (1)∩d uses the assumption that
the colors of the components of L are simple objects. Since k is an algebraically
closed ﬁeld, we can choose for each component of L a square root νJ ∈ k of the
twist scalar vJ∈ k of the color J of this component, see Section 10.1. (At the end,
the invariant|M,L|C∈ k will be independent of this choice.) A neighborhood of
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 41
x∈P (1)∩d inP looks as follows (as usual, the orientation of M is right-handed):
PSfrag replacements
r−
r+
r
i
j
k
M
J
lx
m .
The skeleton P has 3 regions (possibly coinciding) adjacent to x. We denote them
r,r −,r + so that the strand of d at x goes from r− to r+. Let J be the color of
this strand. The diagram d has 5 regions adjacent to x. We denote their c-colors
by i,j,k,l,m as in the picture. Let e0 be a tangent vector at x directed inside r
and let ( e±
1,e ±
2 ) be a positive (i.e., positively oriented) basis of the tangent space
of r± at x. Consider the basis ( e0,e ±
1,e ±
2 ) of the tangent space of M at x. Set
ε±
x = 1 if this basis is positive and ε±
x =−1 if it is negative. Let Γ x be the following
C-colored knotted graph in R2⊂S2:
Γ x =
PSfrag replacements
i
j
k
l
m
J
J ′
1 2
where
PSfrag replacements
i
j
k
l
m
J
J ′
1
2
=



PSfrag replacements
ij
klmJJ ′
12
if ε−
x =−1,
PSfrag replacements
ij
klmJJ ′
12
if ε−
x = 1,
PSfrag replacements
i
j
k
l
m
J
J ′
1
2 =



PSfrag replacements
ij
klmJJ ′
12
if ε+
x =−1,
PSfrag replacements
ij
klmJJ ′
12
if ε+
x = 1.
The latter pictures determine the orientations of the edges of Γ x colored by i,j,k,l .
The edge of Γ x colored by m is directed downward if the orientation of r followed
by that of d at x yields the positive orientation of M and upward otherwise. Set
εx = ε−
x−ε+
x
2 ∈{− 1, 0, 1} and |x|c =νεx
J FC(Γ x)∈Hc(Γ x)⋆.
For any vertex x of ~d, we have Hc(Γ x) =⊗eHc(e), where e runs over the edges
of ~d incident to x and oriented away from x. The tensor product ⊗x|x|c over all
vertices x of ~d is a vector in ⊗eHc(e)⋆, where e runs over all oriented edges of ~d.
Set∗P =⊗e∗e : ⊗e Hc(e)⋆→ k.
Let L1,...,L N be the components of L. Let Jq∈ Ob(Z(C)) be the color of Lq.
Recall the distinguished square root νJq ∈ k of the twist scalar vJq of Jq. Let
nq∈ 1
2 Z be the pre-twist of the loop of d representingLq, where q = 1,...,N . Set
|M,L|C = (dim(C))−|P |
N∏
q=1
ν2nq
Jq
∑
c

 ∏
r∈Reg(d)
(dimc(r))χ(r)

∗P (⊗x|x|c)∈ k,
42 V. TURAEV AND A. VIRELIZIER
where|P| is the number of components of M\P ,c runs over all maps Reg( d)→I,
and χ(r) is the Euler characteristic of r.
Lemma 12.2. |M,L|C is a topological invariant of the pair (M,L ) independent of
the choice of I and of the choice of square roots of the twist scalars.
Proof. The independence of I follows from the naturality of FC and of the contrac-
tion homomorphisms. We prove the independence of the choice of νJq . The term
of|M,L|C determined by a map Reg( d)→I is a product of an expression indepen-
dent of νJq and ν2nq+sq
Jq for sq =∑
xεx, where x runs over the intersections of the
q-th component of d with P (1). It suﬃces to show that 2 nq +sq∈ 2Z. Observe
that εx = 0 if the orientations of the regions r− and r+ at x are compatible, and
εx =±1 otherwise. Therefore sq∈ 2Z if and only if the normal bundle of the i-th
component of d inP is trivial. By the deﬁnition of a pre-twist, the latter condition
holds if and only if nq∈ Z. Therefore, 2 nq +sq∈ 2Z in all cases.
Recall that any two s-skeletons of M can be related by a sequence of Matveev-
Piergallini moves. Using Ω ±1
5 , Ω 6, and Ω 8 we can deform any diagram of L on P
away from the place where an MP-move is performed on P . Then the same ar-
guments as in the proof of Theorems 5.1 and 6.1 show that |M,L|C is invariant
under the MP-move in question. Therefore we need only to verify th at|M,L|C is
invariant under the moves Ω 1,..., Ω 8.
Without loss of generality, we can assume that in the pictures of Ω 1, Ω 2, Ω 3 the
orientation of the ambient region corresponds to the countercloc kwise orientation
of the plane of the picture. For any orientation of the red-bold str and, colored by
a simple object J ofZ(C),
PSfrag replacements
J
J z
i j
∑
z∈I
dim(z)
PSfrag replacements
J
J
zi
j
j
=
PSfrag replacements
J
J
zi j = vJ
PSfrag replacements
J
J
zi j .
The arrow indicates that we compute the contribution of the pictur e (the curl) to
the state sum. The dotted arc indicates the tensor contraction o f the vector spaces
corresponding to the endpoints of the arc. The equalities follow res pectively from
Lemma 4.2.c and the deﬁnition of the twist scalar vJ (if the red-bold strand is
oriented upward, one should also use the equality vJ ∗ =vJ ). Taking into account
the normalization factor ∏
qν2nq
q and the additional pre-twist−1 introduced by Ω 1,
we conclude that |M,L|C is invariant under Ω 1.
For any orientations of the red-bold strands (colored by simple obj ects ofZ(C)),
PSfrag replacements
J
J ′
zi j
k
l
∑
z∈I
dim(z)
PSfrag replacements
J
J ′
z
z
i
i
j
j
k
l
=
∑
z∈I
dim(z)
PSfrag replacements
J
J ′
z
i
i
j
k
l
=
PSfrag replacements
J
J ′
zi j
k
l
=
PSfrag replacements
J
J ′
z
i j
k
l
= δk,l
PSfrag replacements
J
J ′
z
i
j
k
l k
PSfrag replacements
J
J ′
z
i
j
k
l
kk j
PSfrag replacements
J
J ′
z
i
j
k
l
k
k ji .
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 43
The ﬁrst two equalities follow respectively from Claims (d) and (c) of L emma 4.2.
The third equality follows from Lemma 12.1. We conclude that |M,L|C is invariant
under Ω 2. The invariance under Ω 3 is veriﬁed similarly.
Below we verify the invariance of |M,L|C under the moves Ω 4,... Ω 8 for a cer-
tain orientation of the link diagram. The proof of the invariance for t he opposite
orientation of a component of the diagram can be obtained by repea ting exactly
the same arguments but using everywhere the opposite orientatio n of the relevant
edges of the C-colored knotted graphs. In particular, the tensors associated with
all vertices are represented by the same graphs with opposite orie ntation of the
appropriate red-bold edges. For the tensors associated with the crossings, this fol-
lows directly from the deﬁnitions. For the tensors associated with t he vertices of
P (1)∩d, we use that
PSfrag replacements
J
=
PSfrag replacements
J
= ν−2
J
PSfrag replacements
J
.
and
PSfrag replacements
J
=
PSfrag replacements
J
= ν2
J
PSfrag replacements
J
.
For example, we have
PSfrag replacements
J i
j
k
l
m ν
−1−1
2
J
PSfrag replacements
J
i
j
k
l
m
and
PSfrag replacements
J
JJ ν
1+1
2
J
= ν−1
J
i
i
i
j
j
j
k
k
k
l
l
l
m
m
m .
The last graph diﬀers from the graph obtained in the previous pictur e only by the
orientation of the red-bold edge.
Let us now verify the invariance of |M,L|C under the moves Ω 4− Ω 8 for a certain
orientation of the s-skeleton and of the link diagram. We begin with Ω 4, Ω 5, and
Ω 8. In these computations, the (unique) red-bold strand is colored w ith a simple
object J ofZ(C). We have
44 V. TURAEV AND A. VIRELIZIER
PSfrag replacements
J
z
i
j
k
l
m
ν
−1−1
2
J ν
1−1
2
J
∑
z∈I
dim(z)
PSfrag replacements
J
z
zi
j
jk
k
l
m
m
= ν−1
J
∑
z∈I
dim(z)
PSfrag replacements
J
z zi j j
k k
l
m
m
= ν−1
J
∑
z∈I
dim(z)
PSfrag replacements
J
z zi j j
k k
l
m
m
= ν−1
J
PSfrag replacements
J
z
i
j
k
l
m
= ν−1
J
PSfrag replacements
J
z
i
j
k
l
m
All these equalities except the penultimate one follow from Lemma 12.1 ; the penul-
timate equality follows from Lemma 4.2. By deﬁnition,
PSfrag replacements
J
z
i
j
k
l
m ν
−1+1
2
J
PSfrag replacements
J
z
i
j
k
l
m
.
Taking into account the normalization factor ∏
qν2nq
q and the additional pre-twist
1
2 introduced by Ω 4, we conclude that |M,L|C is invariant under Ω 4.
Next, we have
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 45
PSfrag replacements
J
z
i
j
k l
m
ν
1−1
2
J ν
1−1
2
J
∑
z∈I
dim(z)
PSfrag replacements
J z
z
i
j
j
k
l
l
m
m
=
PSfrag replacements
J
z
i
j
k
lm
=
PSfrag replacements
J
z i
j
k
lm = δi,k
PSfrag replacements
J
z
iijk lm .
The right-hand side is the contribution to the state sum of the follow ing piece of
the diagram:
PSfrag replacements
J
z
i
j
k
l
m .
Therefore the state sum is invariant under Ω 5.
Next, we have
M
PSfrag replacements
z
i
j
kl
m
n
p
q
46 V. TURAEV AND A. VIRELIZIER
ν
1−1
2
J ν
1−1
2
J
∑
z∈I
dim(z)
PSfrag replacements
z
z
z
i
i
jk
k
l
m
m
n
n
p qq
=
PSfrag replacements
z
i
j
k
l
m
n
p
q
=
PSfrag replacements
z
i
j
k
l
m
n
p
q
=ν
1−1
2
J
PSfrag replacements
z
i
j
j
k
l
l
m
n
p
p q
M
PSfrag replacements
z
i
j
kl
m
n
p
q
Therefore the state sum is invariant under Ω 8.
Consider now the moves Ω 6 and Ω 7. We assume that the two red-bold strands
are colored with simple objects J,J ′ ofZ(C). We have
PSfrag replacements
J
J ′z
i
j
k
l
m
n
p
ν
1−1
2
J ν
1−1
2
J ′
∑
z∈I
dim(z)
PSfrag replacements
J
J ′
z
z
z
i
i
j
k
k
l
m
m
n
p
p
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 47
=
PSfrag replacements
J
J ′
z i
j
k
l
m
n
p =
PSfrag replacements
J
J ′
z i
j
k
l
m
n
p
=ν
1−1
2
J ν
1−1
2
J ′
∑
z∈I
dim(z)
PSfrag replacements
J
J ′
z
z
z
i
j
j
k
l
l
m
n
n
p
p
PSfrag replacements
J
J ′ z
i
j
k
l
m
n
p
.
Therefore the state sum is invariant under Ω 6.
We verify the invariance for Ω 7.1 (the case of Ω 7.2 is similar). We have
PSfrag replacements
J J ′
z
i
j
k
l
m
n
p
q
ν
−1+1
2
J ν
1−1
2
J ′
∑
z∈I
dim(z)
PSfrag replacements
J
J ′
z
z
z
i
i
j
k
k
l
m
m
n
p
p
q
48 V. TURAEV AND A. VIRELIZIER
=
∑
z∈I
dim(z)
PSfrag replacements
J
J ′
z
z
z
i
i
j
k
k
l
m
m
n
p
p
q
=
PSfrag replacements
J
J ′
z
i
j
k
l
m
n
p
q
=
PSfrag replacements
J
J ′
z
i
j
k
l
m
n
p
q
=
PSfrag replacements
J
J ′
z
i
j
j
k
l
l
m
n
n
p
q
=ν
−1+1
2
J ν
1−1
2
J ′
PSfrag replacements
J
J ′
z
i
j
j
k
l
l
m
n
n
p
q
PSfrag replacements
J
J ′
z
i
j
k
l
m
n
p
q
Therefore the state sum is invariant under Ω 7.
The invariance of |M,L|C under the moves Ω 4− Ω 8 with other orientations of
the s-skeleton can be veriﬁed similarly. As above, this veriﬁcation is e asy for Ω 5
and Ω 6 but longer for the other moves. However, having veriﬁed this invar iance for
Ω 5 and Ω 6, we can prove that |M,L|C does not depend on the orientation of the
s-skeletonP . Then the invariance for the other moves follows from the special c ases
considered above. To prove our claim, it is enough to prove the invar iance of|M,L|C
under reversion of the orientation in an arbitrary region, X, of P . Applying bubble
movesT
′′
4 (see Figure 4) at the boundary of X, then using Ω 5 to push the newly
attached disks near the crossings and using Ω 6 to pull the crossings into these disks,
we can reduce the claim to the case where X contains no crossings of the diagram
(note that all these transformations keep |M,L|C). Then X meets the link diagram
in several disjoint embedded arcs. Similarly, applying bubble moves T
′′
4 and then
lune movesL±1 (see Figure 7) to push the newly attached disks between the arcs
of the diagram in X, we can reduce the claim to the case where the diagram meets
the disk X along a single embedded arc. Finally, applying the moves ( T 2,1)−1 (see
Figure 6) to P outside the diagram, we can reduce the claim to the case where X
has only two vertices in P as in the picture below. There are two cases to consider,
depending on whether or not this arc arrives and leaves in the same d irection:
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 49
and
Let us check that the two orientations of the disk do contribute sim ilarly to the
state sum. In the ﬁrst case, we have
PSfrag replacements
J
x
i
j
y
ν
ε −
x +1
2
J ν
−1−ε +
y
2
J
∑
i,j∈I
dim(i) dim(j)
PSfrag replacements
J
x
i
i
i
j
j
j
y
=ν
ε −x −ε +y
2
J
PSfrag replacements
J
x
i
j
y
=ν
ε −
x −1
2
J ν
+1−ε +y
2
J
∑
i,j∈I
dim(i) dim(j)
PSfrag replacements
J
x
i
i
i
j
j
j
y
50 V. TURAEV AND A. VIRELIZIER
PSfrag replacements
J
x
i
j
y
In the second case, we have
PSfrag replacements
J
x
i
j
y
ν
ε −
x +1
2
J ν
1−ε +
y
2
J
∑
i,j∈I
dim(i) dim(j)
PSfrag replacements
J
x
i
i
i
j
j
j
y
=ν
1+
ε −x −ε +y
2
J
∑
i,j∈I
dim(i) dim(j)
PSfrag replacements
J
x
i
i j
j
y
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 51
=ν
1+
ε −x −ε +y
2
J
∑
i,j∈I
dim(i) dim(j)PSfrag replacements
J
x
i
j
y
=ν
1+
ε −x −ε +y
2
J
∑
j∈I
dim(j)PSfrag replacements
J
x
i
j
y
=ν
1+
ε −x −ε +y
2
J
PSfrag replacements
J
x
i
j
y
=ν
−1+
ε −x −ε +y
2
J
PSfrag replacements
J
x
i
j
y
=ν
−1+
ε −
x −ε +
y
2
J
∑
i,j∈I
dim(i) dim(j)
PSfrag replacements
J
x
i
j
y
52 V. TURAEV AND A. VIRELIZIER
=ν
−1+
ε −
x −ε +
y
2
J
∑
i,j∈I
dim(i) dim(j)
PSfrag replacements
J
x
i
i
i
j
j
j
y
=ν
ε −x −1
2
J ν
−1−ε +y
2
J
∑
i,j∈I
dim(i) dim(j)
PSfrag replacements
J
x
i
i
i
j
j
j
y
PSfrag replacements
J
x
i
j
y
This concludes the proof of Lemma 12.2. □
12.4. The case of arbitrary links. We extend the invariant |M,L|C of links
without trivial components in a compact oriented 3-manifold M (see Lemma 12.2)
to arbitrary links in M . Consider an oriented framed link L ⊂ Int(M ) whose
components are colored by simple objects of Z(C). Let L1,...,L k be the trivial
components of L, and let ~L be the sublink of L formed by all the other components.
For i = 1,...,k , let Ji be the object of Z(C) coloring Li and let fi∈ Z be the
framing number of Li (deﬁned as in the standard case of knots in the 3-sphere).
Set
|M,L|C =|M,~L|C
k∏
i=1
vfi
Ji dim(Ji)∈ k.
Theorem 12.3. |M,L|C is a topological invariant of the pair (M,L ).
This theorem directly follows from Lemma 12.2.
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 53
The invariant|M,L|C can be computed via the same formula as in Section 12.3
applied to an arbitrary s-skeleton P of M and an oriented enriched link diagram
d in P representingL such that every component of d has a self-crossing or meets
the 1-skeleton of P .
12.5. Remarks. (1) Since all objects of Z(C) are direct sums of simple objects, the
invariant|M,L|C extends by linearity to arbitrary colors of the components of L.
(2) Theorem 11.1 directly extends to 3- manifolds with links, see Form ula (18)
in Section 13.5.
12.6. A special case. It is obvious that for L =∅, we have |M,L|C =|M|C,
where|M|C∈ k is the invariant deﬁned for closed M in Section 5 and generalized
to compact M in Section 9.2. We obtain a similar formula for any Z(C)-colored
framed oriented link L lying in a 3-ball in M . Denote by L′ theZ(C)-colored
framed oriented link in S3 obtained by cutting out the ball containing L from M
and embedding this ball - with L inside - in S3. The embedding in question should
be orientation-preserving.
Lemma 12.4. |M,L|C =|M|CFZ(C)(L′).
Proof. Pick an s-skeleton P of M and a diagram d of L contained in a region r
of P . Inserting if necessary small curls in d, we can assume that d has at least
one self-crossing and all pre-twists of d are equal to zero. Denote the underlying
(4-valent) graph of d byd. Applying if necessary Ω 2 to d in r, we can ensure that
d is connected and all its edges have distinct endpoints. Then all regio ns of d are
disks except the “exterior region” r0 of d in r, which is an annulus. Let R1 be the
set of the disk regions of d contained in r andR2 be the set of all other disk regions
of d. Thus, Reg( d) = R1∐R2∐{r0}.
SinceP (1)∩d =∅, the scalar∗P (⊗x|x|c)∈ k in the deﬁnition of |M,L|C expands
as a product of two scalars tc
1,t c
2∈ k. The scalar tc
1 (resp. tc
2) is obtained from the
tensor associated with the vertices of P (1) (resp.d) through the tensor contraction
associated with the edges of P (1) (resp. d). Each tc
k is determined by i =c(r0)∈I
and the map ck =c|Rk : Rk→I. We therefore denote tc
k byti,ck . We have
|M,L|C = (dim(C))−|P |∑
i∈I
∑
c : Reg( d)→I
c(r0)=i
( ∏
r∈R1∪R2
dimc(r)
)
tc
1tc
2
= (dim(C))−|P |∑
i∈I
∑
c1 : R1→I
( ∏
r∈R1
dimc1(r)
)
ti,c1
∑
c2 : R2→I
( ∏
r∈R2
dimc2(r)
)
ti,c2.
Below we prove that for all i∈I,
(16)
∑
c : R1→I
( ∏
r∈R1
dimc(r)
)
ti,c = dim(i)FZ(C)(L′).
Substituting this in the expression for |M,L|C above, we obtain that
|M,L|C = (dim(C))−|P |∑
i∈I
∑
c : R2→I
( ∏
r∈R2
dimc(r)
)
ti,c2 dim(i)FZ(C)(L′)
=|M|CFZ(C)(L′).
To prove (16), we need to study the graph d in more detail. Let N≥ 1 be the
number of vertices of d (i.e., the number of crossings of d). Since the graph d is
4-valent, it has 2 N edges. A computation of the Euler characteristic of r shows
that d splits r into N + 1 disk regions and the exterior region r0. The diagram d
54 V. TURAEV AND A. VIRELIZIER
also determines a graph d∗⊂r as follows. Fix a point in each region of d inr called
the center of the region. These N + 2 points are the vertices of d∗. Every edge e
of d determines a dual edge e∗ of d∗ which connects the centers of the two regions
adjacent to e, meets the interior of e transversely in one point, and is disjoint from
d otherwise. Note that the two regions adjacent to e are always distinct so that
the edges of d∗ are not loops. We choose the edges of d∗ so that they meet only in
common vertices. The vertex of d∗ represented by the center of r0 is denoted O.
By a subgraph of a graph G we mean a graph formed by some vertices and edges
of G. A subgraph F of G is full if all vertices of G are vertices of F . A maximal
tree in G is a full subgraph of G which is a tree. Each subgraph F of d determines
a full subgraph F ∗ ofd∗ whose edges are dual to the edges of d not belonging to F .
Clearly,F∩F ∗ =∅. If F is a maximal tree in d, then F ∗ is a maximal tree in d∗.
Indeed, since every component of r\F ∗ contains a vertex of d and any two vertices
of d can be related by a path in F⊂r\F ∗, the set r\F ∗ is connected. Hence F ∗
is a forest with N + 2 vertices and 2 N− (N− 1) = N + 1 edges. Such a forest is
necessarily a tree.
Let e1,...,e 2N be the edges of d enumerated so that the following conditions
are met. For k = 1,..., 2N , set Fk =∪k
l=1el⊂ d and observe that F ∗
k is the full
subgraph of d∗ with edges e∗
k+1,...,e ∗
2N . We require that (a) the graph FN −1 is
a maximal tree in d and (b) for all k =N,..., 2N , the graph F ∗
k−1 has a 1-valent
vertex distinct from O and incident to e∗
k. It is easy to choose e1,...,e N −1 to
ensure (a). We explain now how to choose ek with k ≥ N to ensure (b). For
k =N , pick a 1-valent vertex vN of the maximal tree F ∗
N −1⊂d∗ distinct from O.
(Such a vertex exists because a tree having at least one edge nece ssarily has ≥ 2
vertices of valency 1.) Let eN be the edge of d such that e∗
N is the edge of F ∗
N −1
adjacent to vN . The graph F ∗
N is obtained from F ∗
N −1 by removing e∗
N (keeping all
the vertices). Clearly, F ∗
N is a disjoint union of the isolated vertex vN and a tree
with N + 1 vertices. We choose eN +1 so that e∗
N +1 is the edge of the latter tree
adjacent to a 1-valent vertex vN +1⁄= O. Continuing by induction we obtain that
the graph F ∗
k constructed at the k-th step consists of isolated vertices vN,...,v k
and a tree with 2 N + 1−k vertices. We choose ek+1 so that e∗
k+1 is the edge of the
latter tree adjacent to a 1-valent vertex vk+1⁄= O. This process stops at k = 2N
because the graph F ∗
2N has only isolated vertices.
We can now prove (16). Recall that the term ti,c is obtained by placing a small
colored tetrahedron-type graph in every crossing of d, taking the tensor product
of the associated FZ(C)-invariants, and tensor contracting this product along the
edges of d. The colors of the edges of these tetrahedron-type graphs are determined
byi,c , and the given coloring of the link components. We shall perform the tensor
contraction at one edge at a time following the order of the edges e1,...,e 2N ﬁxed
above. Condition (a) shows that for k = 1,...,N − 1, the k-th tensor contraction
involves two diﬀerent pieces of the diagram so that we can apply Claim ( d) of
Lemma 4.2. At each of these N− 1 steps, the tensor contraction of the tensor
product of two FZ(C)-invariants yields the FZ(C)-invariant of a “fused” diagram. For
k≥N , the endpoint vk ofe∗
k is the center of a disk region, Vk⊂r, of d adjacent to
the edge ek. Note that all other sides of Vk (i.e., all other edges of d adjacent to Vk)
must have appeared at the previous steps among e1,...,e k−1. This follows from the
fact that neither of the edges e∗
k+1,...,e ∗
2N is adjacent to vk. Therefore the fusions
corresponding to all sides of Vk exceptek have been done before the k-th step. The
tetrahedron-type graph associated with a vertex of Vk has a side in Vk; under the
fusions in question, these sides are united into a single arc labeled with c(Vk). This
shows that the k-th tensor contraction involves two vertices of the same connect ed
piece of the diagram. We apply Claim (c) of Lemma 4.2 where the roles of i,u,v
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 55
are played respectively by c(Vk) and the endpoints of ek (here we use that all edges
of d have distinct endpoints). After fusion along ek our diagram will contain an
embedded c(Vk)-colored circle. Lemma 4.2.c says that to preserve the state sum
under the fusion we must delete this circle, the summation over c(Vk)∈I, and the
factor dim c(Vk). The rest of the diagram is the “fused diagram” obtained at the
k-th step. Continuing by induction, we obtain that the left-hand side of (16) is
equal to the FZ(C)-invariant of the fused diagram obtained at the last step k = 2N .
This diagram consists of a diagram of L′ surrounded by a big circle colored with i.
The FZ(C)-invariant of this fused diagram is equal to dim( i)FZ(C)(L′). This proves
our claim. □
Applying Lemma 12.4 to M = S3 and using the equality |S3|C = (dim(C))−1
(see Section 6.3), we obtain that for any Z(C)-colored framed oriented link L⊂S3,
(17) |S3,L|C = (dim(C))−1FZ(C)(L).
