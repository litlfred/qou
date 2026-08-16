---
doc_id: 0307092v2
doc_title: "Published: 14 February 2004"
section_id: sec-004-5-developing-map
section_title: "Developing map"
section_number: 5
pages: 18-23
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class Walter D Neumann — We deﬁne an extended Bloch group and show it is naturally isom orphic to H3(PSL(2, C)δ; Z)."
---
H
3
which is helpful for visualizing the ﬂattening con-
dition. It is used to prove some preliminary lemmas. Section 6 proves a con-
sequence of the ﬁve term relations, a general “cycle relatio n” which is used
frequently later.
Section 9 proves Theorem 4.5, the existence of a strong ﬂatte ning of K . The
argument of this section is combinatorial and depends heavi ly on [13].
The combinatorial argument is continued at the beginning of the next section
(Section 10) to show that the resulting element of ˆP(C) is independent of the
choice of strong ﬂattening and lies in ˆB(C). It then remains to show that the
element of ˆB(C) only depends on the homology class α ∈ H3(G; Z) and not on
the G–labeled ordered 3–cycle K used to represent it. In the rest of Section
10 we ﬁrst show that this element of ˆB(C) is unchanged if the G–labeling of
K is changed by a coboundary (so it just depends on the ﬂat G–bundle and
not on the 1–cocycle used to represent it) and next that it is i nvariant under
alteration of the triangulation of |K| by Pachner moves. Thus, by the end of
this section we know that we have an element of ˆB(C) that only depends on
the space |K| and the ﬂat G–bundle over it.
This section uses a strong ﬂattening of K and, moreover, it needs to assume
that K is a simplicial rather than quasi-simplicial complex and th at the vertex
orderings of its simplices are induced by a global ordering o f the 0–simplices
of K . These assumptions will be removed one by one in the next sect ion, so
Theorem 4.6 eventually applies to ﬂattenings that are not ne cessarily strong,
and also to quasi-simplicial complexes for which the vertex orderings of the
simplices need not be globally induced.
Section 11 completes the proof of Theorem 4.6. First it is sho wn that the singu-
larities of |K| can be “resolved” to make |K| into a manifold. Since H3(G; Z)
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 431
can be represented as the bordism group of 3–manifolds with ﬂ at G–bundles,
the proof is completed by showing that the element of ˆB(C) is unchanged by ele-
mentary bordisms (ie, surgery). Flattenings and strong ﬂat tenings are the same
thing when K is a manifold, so the requirement of strong ﬂattenings disso lves,
while retriangulation using Pachner moves is used to relax t he requirements
on K to require only that it be a quasi-simplicial complex with ve rtex-ordered
simplices.
Finally, the main Theorem 2.6, stating that λ : H3(PSL(2, C); Z) → ˆB(C) is an
isomorphism and that Cheeger–Chern–Simons class is given b y Rogers dilog-
arithm, is proved in section 12. At this point it follows easi ly, using work of
Dupont.
Section 13 describes the weaker conclusions obtained if ord erings of simplices
are not used, conﬁrming a conjecture in [13].
The next two sections then apply the results to invariants of 3–manifolds, and
a very brief ﬁnal section describes what happens if C is replaced by a number-
ﬁeld.
5 Developing map
Suppose we have a G–labeled 3–cycle K . Choose a generic point z ∈ ∂
H
3
as
in the deﬁnition of ﬂattenings (Deﬁnition 4.4). Then each si mplex ∆ i of K
corresponds to a non-degenerate ideal simplex ⟨g(i)
0 z, g(i)
1 z, g(i)
2 z, g(i)
3 z⟩ in H
3
.
This simplex is determined up to isometry, since ( g(i)
0 , . . . , g(i)
3 ) is well deﬁned
up to left multiplication by elements of G = PSL(2 , C) = Isom +(H3). This
associates a geometry as an ideal simplex to each simplex of K , and hence, by
lifting, also to each simplex of the universal cover ˜K .
We would like to use this geometry to construct a developing map | ˜K| →
H
3
. The next lemma says that this is possible. Note that the idea l simplex
corresponding to a 3–simplex of K inherits an orientation from H3 that will not
in general agree with the orientation of the simplex in the ma nifold |K − K (0)|,
so the developing map may be “folded” in that some simplices m ay be mapped
reversing orientation. In particular, adjacent simplices will map to the same
side of a common 2–face whenever the ideal simplex orientati on of one of the
simplices agrees with its orientation in |K| and for the other simplex it diﬀers.
Lemma 5.1 There is a map D : | ˜K| → H
3
(unique up to isometries of H3 )
which maps each simplex of the universal cover ˜K of K isometrically and
Geometry & Topology, Volume 8 (2004)
432 Walter D Neumann
preserving orientation with respect to its ideal simplex sh ape just described.
We call it the “developing map.” The map is equivariant with r espect to an
action of π1(K) on H
3
.
Proof Consider the corresponding 1–cocyle σ (subsection 4.1.2) whose value
on an unordered 1–simplex ⟨v1, v2⟩ with label ( g1, g2) is σ(⟨v1, v2⟩) = g−1
1 g2 .
Any edge path ⟨v0, v1⟩⟨v1, v2⟩. . . ⟨vk−1, vk⟩ determines an element
σ(⟨v0, v1⟩)σ(⟨v1, v2⟩) . . . σ(⟨vk−1, vk⟩) ∈ G
and this gives a homomorphism φK from the groupoid of edge paths to G. In
particular, it restricts to a group homomorphism π1(K, v0) → G. We thus get
an action of π1(K, v0) on H
3
.
Choose a 0–simplex ˜ v0 as a basepoint in the universal cover ˜K of K . We
can then G–label the vertices of ˜K by labeling vertex ˜v by the element φK (γ)
where γ is the image of any edge path from ˜ v0 to ˜v in ˜K . This gives us a lift
of the G–labeling of K to a labeling of ˜K in which labels are absolute rather
than just well deﬁned up to left multiplication by G. Using this labeling, the
desired mapping of | ˜K| to H
3
maps a simplex of ˜K with labels ( g1, . . . , g4) to
the ideal simplex ⟨g1z, . . . , g4z⟩.
To show the equivariance of this map it helps to describe it mo re explicitly. For
any two 0–simplices w1, w2 ∈ ˜K , let φ[w1, w2] be φK of the image in K of a
simplicial path [ w1, w2] from w1 to w2 in ˜K . φ[w1, w2] only depends on w1
and w2 since any two paths from w1 to w2 are homotopic. With this notation
the developing map is
D(w) = φ[˜v0, w]z for any w ∈ ˜K (0).
The action of π1(K, v0) by covering transformations is such that the lift of a
closed path representing γ ∈ π1(K, v0) is a path [˜ v0, γ˜v0].
Thus for any w ∈ ˜K (0) and γ ∈ π1(K, v0) we have
φK(γ)D(w) = φK (γ)φ[˜v0, w]z = φ[˜v0, γ˜v0]φ[v0, w]z =
=φ[˜v0, γ˜v0]φ[γv0, γw]z = φ[v0, γw]z = D(γw)
This proves the equivariance.
The developing map gives a convenient way to visualize what i t means to satisfy
the ﬂattening condition in the star neighborhood N of a 0–simplex v of K .
Since N is contractible, it lifts homeomorphically to the star ˜N of a lift ˜v of
v in ˜K . Use the upper half-space model of H3 and choose the developing map
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 433
−π/3
π
3π/2
π/3 −π/4 2π/3
0
3π/2 −π/4
7π/4
π/3 −2π/3
π/3
4π/3 −2π/3
−2π/3
Figure 3: Three triangles in developing image of N in C showing rotation levels of
edges and resulting adjusted angles. One triangle is from a “folded” simplex.
D : | ˜K| → H
3
so D(˜v) = ∞. Thus for each 3–simplex of the closure of ˜N ,
the other three vertices of the simplex map to points in C ⊂ C ∪ {∞} = ∂H
3
,
and thus determine a triangle in C. Each 2–simplex incident to v determines
a 1–simplex in Lv and hence a line segment in C. For each such segment S ,
the angle of this line segment from horizontal is well deﬁned in R/πZ; choose a
speciﬁc lift a(S) of this number in R and call it the rotation level for S . Then
diﬀerences of rotation levels for segments corresponding to adjacent 2–faces of a
3–simplex determine a ﬂattening in the star neighborhood of N (see Figure 3).
Speciﬁcally:
Suppose we have two adjacent 2–faces incident to v of a 3–simplex ∆ i of N .
Geometry & Topology, Volume 8 (2004)
434 Walter D Neumann
Let S1 and S2 be the corresponding segments in the plane C, taken in the
order speciﬁed by the orientation ∆ i inherits from K (so S1 and S2 are in
clockwise order around the triangle in C determined by ∆ if the developing
map D preserves orientation of ∆ and anticlockwise order otherwi se). Specify
the adjusted angle between these 2–faces of ∆ i to be ǫi(a(S2) − a(S1)) (where,
as usual, ǫi = ±1 is determined by vertex-order of ∆ i ).
This clearly speciﬁes a ﬂattening for the 3–simplices of N and the ﬂattening
conditions are satisﬁed at v . Conversely, such a ﬂattening for N plus a rotation
level a(S) for one of the line segments determines a(S) for every segment, so
the ﬂattening determines the rotation level function a up to a multiple of π .
We will use the developing map to prove a preliminary proposi tion towards
Theorem 4.5. That theorem says a strong ﬂattening of K exists. Since changing
ﬂattenings changes log parameters by multiples of πi , it must be true that if
we make an arbitrary choice of ﬂattenings of the individual ideal simplices then
the sum of log parameters along any normal path in the star of a 0–simplex is
a multiple of πi . We will show, in fact:
Proposition 5.2 Notation as in Deﬁnition 4.4. If we use ﬂattenings ℓ(xi; 0, 0)
for the simplices of K then the log parameter along any normal path in the
star of a 0–simplex is a multiple of 2πi .
The proof of this will involve the following related proposi tion, which we prove
ﬁrst.
Proposition 5.3 Notation as in Deﬁnition 4.4. If we use ﬂattenings ℓ(xi; 0, 0)
for the simplices of K then the parity along any normal path in K is zero.
Proof As we follow a normal path the contribution to the parity as we pass
an edge of a simplex is 0 if the edge is the 01, 03, 12, or 23 edge o f the simplex
and the contribution is ±1 if it is the 02 or 13 edge. Consider the orientations
of the triangular faces we cross as we follow the path, where t he orientation is
the one induced by the ordering of its vertices. As we pass a 02 or 13 edge this
orientation changes while for the other edges it does not. Si nce K is oriented,
we must have an even number of orientation changes as we trave rse the normal
path, proving the claim.
Proof of Proposition 5.2 Consider a normal path γ in the star N of a 0–
simplex v of K . As above, use the upper half-space model of H3 and choose
the developing map D : | ˜K| → H
3
so D(˜v) = ∞, where ˜v is a lift of v .
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 435
Denote the lift of γ to ˜N by ˜γ . The path D ◦ ˜γ has a “shadow” in C. As γ
passes an edge of a 3–simplex of ˜N , the shadow passes the corresponding vertex
of the corresponding triangle in C, entering at one edge of the triangle and
exiting at another. The cross-ratio parameter correspondi ng to the 3–simplex
edge (or its inverse, depending on vertex ordering and how we are passing the
edge) is the derivative of the linear map of C that takes the entering edge
of the triangle to the exiting edge, ﬁxing the common vertex. Since the path
D ◦ ˜γ ends up where it started, the product of these cross-ratio pa rameters
(each raised to an appropriate power ±1) is 1, so the appropriately signed
sum of their logs is a multiple of 2 πi . This sum is precisely the log-parameter
along the path, except for the adjustments by multiples of πi that are involved
in forming the log-parameters from the logarithms of cross- ratio parameters.
These adjustments add up to an even multiple of πi since the parity along the
path γ to be zero by Proposition 5.3.
The following corollary of Propositions 5.2 and 5.3 is usefu l. It is immediate
from the deﬁnition of parity.
Corollary 5.4 For a normal path in the star of a vertex, if the ﬂattening
condition for log-parameters is satisﬁed, then so is the par ity condition.
