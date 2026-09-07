---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-016-4-coordinates-on-generically-decorated-represent
section_title: "Coordinates on generically-decorated representations"
section_number: 4
pages: 15-23
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
Here we review decorations of representations and deﬁne F ock–Goncharov coordinate structures .
For a representation ρ and a chosen triangulation, a decoration of ρ is a collection of ﬂags for each simplex
in the triangulation. These ﬂags can recreate ρ, and have a canonical form that admits generalized minor
coordinates. Fock–Goncharov coordinate structures will d escribe coordinates on these decorations.
15
These decorations apply to surfaces, but also to 3-manifolds with ﬁxed ideal triangulations. We follow
[FG06b] for the surface case and [Zic19] for the 3-manifold case.
4.1. Conﬁgurations and gluings.
Deﬁnition 4.1. LetG be a Lie group over C, with suﬃcient choices to deﬁne G0 as in Deﬁnition 2.11. Let
K be a subgroup of G (we will ultimately use N+). A tuple of cosets (g0K,g 1K,...,g mK) is suﬃciently
generic if each g−1
i gj ∈w0G0.
Such a tuple corresponds to a labeling of edges in an oriented m-simplex by elements of w0G0, as in
Figure 10, with the edge from i to j (assuming j >i) labeled by g−1
i gj.
The variety of such suﬃciently generic (m + 1) -tuples is the conﬁguration space Conf m+1(G/K).
Identifying elements which diﬀer by left-multiplication o f G yields the variety Conf ∗
m+1(G/K).
g0Kg1K
g2K
g−1
0 g1
g−1
0 g2g−1
1 g2
g0K
g1K
g2K
g3K
g−1
0 g1
g−1
1 g2
g−1
2 g3
Figure 10. Oriented 2- and 3-simplices labeled by elements of Conf ∗
3(G/K) and
Conf ∗
4(G/K).
Deﬁnition 4.2. Let M be a compact manifold (possibly with boundary) and G a Lie group over C, with
K a subgroup of G. A subgroup L of π1(M ) is peripheral if there is a boundary component D of M such
that L is induced by the inclusion of D; that is ι∗(π1(D)) = L.
A representation ρ : π1(M ) → G is a (G,K )-representation if, for every peripheral subgroup L, the
image ρ(L) is a conjugate of K. In the case K =N+, the term boundary-unipotent is used. If K =B+,
then ρ is boundary-borel.
Lemma 4.3 ([Zic19, Lemma 5.8, Proposition 5.9]) . There is an isomorphism of varieties
Conf ∗
3(G/N+) ∼=H 3 ×H (N− ∩w0G0).
The ﬁber product ×H means that for (h1,h 2,h 3,u ) ∈ Conf ∗
3(G/N+)), we have
[w0−1u]0 = (w0(h3h1)h2)−1.
Thus we will often write (h1,h 2,h 3,u ) forα, which has one representative (N+,w0h1N+,uw 0(h1)h2sGN+).
We refer to these as canonical forms for Conf ∗
3(G/N+).
Deﬁnition 4.4. By expanding N+ to B+ above, we obtain that α ∈ Conf ∗
3(G/B+) can be given as
(B+,w0B+,uB +). Choose the unique ux such that, for all k, the minor ∆ wkω1,ω1(ux) = 1 . This element ux
is the canonical form for α.
For an arbitrary (B+,w0B+,uB +), by expanding Deﬁnition 2.16 there is a unique (up to the cent er of G)
elementh such that huh−1 is the canonical form ux. When G is centerless, we denote this element by n(u).
Proposition 4.5. This summarizes [Zic19, Proposition 5.10]. Let α ∈ Conf ∗
3(G/N+) be given by α =
(h1,h 2,h 3,u ). Recall Φ and Ψ of Deﬁnition 2.25. The map
rot : Conf ∗
3(G/N+) → Conf ∗
3(G/N+), (g0N+,g 1N+,g 2N+) ↦→(g2N+,g 0N+,g 1N+)
is given, in this form, via
rot : (h1,h 2,h 3,u ) ↦→(h3,h 1,h 2,h −1
2 (w0(h1))−1(ΦΨΦΨ)( u)(w0(h1))h2).
16
Deﬁnition 4.6. This summarizes [Zic19, Section 2.2.1]. We deﬁne and Conf ∗
3(G/N+) ×sG
13 Conf ∗
3(G/N+) by
gluing copies of Conf ∗
3(G/N+) along matching copies of Conf ∗
2(G/N+). Speciﬁcally,
Conf ∗
3(G/N+) ×sG
02 Conf ∗
3(G/N+) =
{
(g0sGN+,g1N+,g2N+),
(g0N+,g2N+,g3N+) : (g0N+,g 1N+,g 2N+,g 3N+) ∈ Conf ∗
4(G/N+)
}
Conf ∗
3(G/N+) ×sG
13 Conf ∗
3(G/N+) =
{
(g1N+,g2N+,g3N+),
(g0N+,g1sGN+,g3N+) : (g0N+,g 1N+,g 2N+,g 3N+) ∈ Conf ∗
4(G/N+)
}
We also deﬁne the following maps from Conf ∗
4(G/N+) to Conf ∗
3(G/N+) ×sG
jk Conf ∗
3(G/N+) for jk = 02, 13:
Ψ 02 : (g0N+,g 1N+,g 2N+,g 3N+) ↦→(g0sGN+,g1N+,g2N+),
(g0N+,g2N+,g3N+)
Ψ 13 : (g0N+,g 1N+,g 2N+,g 3N+) ↦→ (g1N+,g2N+,g3N+),
(g0N+,g1sGN+,g3N+)
See part of Figure 15 for a graphical depiction.
In the surface case, these correspond to the two diﬀerent way s of triangulating a quadrilateral. The act
of retriangulating a single quadrilateral this way is calle d a “ﬂip”. In the 3-manifold case, these correspond
to decomposing a tetrahedron’s vertices into the two triang les’ worth.
Remark 4.7. The element sG is in the center of G, so is only relevant for N+-cosets. Its purpose is to
allow the quiver amalgamation (see Deﬁnition 4.14 ahead) to agree with the identiﬁcation of elements of
Conf ∗
3(G/N+) along a copy of Conf ∗
2(G/N+).
To see this, note that Figure 13 a shows identifying a 0– 2 edge with a 0– 1 edge, and Figure 13 b identifes a
0– 2 edge with a 1– 2 edge. Since the associated elements of Conf ∗
2(G/N+) are oriented via the cyclic ordering
on (0, 1, 2), this quiver amalgamation corresponds to identifying elem ents of Conf ∗
2(G/N+) “backwards”.
This use of sG is why AG,Σ is the moduli space of twisted, decorated representations from π1(Σ) intoG.
See [FG06b, Section 8.6] and [Zic19, Section 2.3] for more de tails.
4.2. T riangular quivers and F ock–Goncharov coordinate structu res. We want a variety that is
independent of the choice of triangulation. Therefore, we w ill need coordinate change maps corresponding
to changes in triangulation (the rotation of individual tri angles, or the quadrilateral ﬂip).
Here we deﬁne the outputs of the algorithm of Section 5. These are triangular quivers (see Deﬁni-
tion 4.13), which have vertices on edges and in the interior. If, moreover, these quivers admit a rotation and
a ﬂip as quiver mutations, they have triangulation-compatible symmetry (see Deﬁnition 4.15). And
if we can then associate the A- and X -coordinates to coordinates on Conf ∗
3(G/N+) and Conf ∗
3(G/B+), we
have a F ock–Goncharov coordinate structure (see Deﬁnition 4.16).
Deﬁnition 4.8. LetD be a Dynkin diagram, with associated Cartan matrix
[ aij
]
. A quiver Q is of Dynkin
type D if |ǫ(i,j )| = −aji (for i ⁄=j) and σ(i,j ) takes values only in { −1, 0, +1 }. The undirected graph of
Q carries the adjacency information of D, and the vertex weights carry the edge details.
Q is of half-Dynkin type D if 2Q, the quiver obtained by multiplying all edge weights by 2, is of Dynkin
type D.
Deﬁnition 4.9. Let D be a quiver of Dynkin type (with no oriented cycles). We can ob tain a particular
Coxeter element c by requiring that sαi appear before sαj in c if σ(i,j )> 0 in D. Such a c is induced by
the quiver D.
Deﬁnition 4.10. A quiver of Dynkin type is tree-like if, as an unoriented graph, it is a tree, and the
directed edges always point away from the root. In this case, there is a partition of vertices {T0,T 1,...,T m }
such that the vertices in Ti are of distance i (in the unoriented graph) from the root vertex.
Note that Coxeter elements induced by tree-like Dynkin quiv ers always take the form
c =
(∏
α∈T0
sα
)(∏
α∈T1
sα
)
· · ·
( ∏
α∈Tm
sα
)
.
Deﬁnition 4.11. The involution σG acts on quivers of Dynkin type in the same way that it would act on
the Dynkin diagram as in Remark 2.7. A tree-like quiver Q of Dynkin type D is well-rooted if this action
of σG preserves all Ti partitions. See Figure 11.
17
Figure 11. A non-well-rooted quiver (left) and a well-rooted quiver (r ight) for E6.
Remark 4.12. In the most cases, the quiver obtained by applying a naïve “le ft-to-right” ordering to the
common presentation of the Dynkin diagram is well-rooted. T he pathological case is E6.
Deﬁnition 4.13. A quiver Q is triangular if, for a standard 2-simplex σ with vertices 0, 1, 2, each vertex
in Q is associated to the interior of some sub-simplex σ′ of σ. dσ′ (Q) is deﬁned to be the sub-quiver of Q
obtained by deleting all vertices except those that lie on th e interior of σ. See Figure 12.
In other words, a triangular quiver Q is one that can be split into sub-quivers:
• d(0,1)(Q), d(1,2)(Q), and d(0,2)(Q): the vertices on the edges of the triangle.
• d(0,1,2)(Q): the vertices in the interior of the triangle.
We label the vertices on the d(0,1) edge’s vertices by Ai, those on the d(1,2) edge by Bi, and those on the
d(0,2) edge by Ci.
An isomorphism ϕ of triangular quivers must preserve these classiﬁcations: d∆ (ϕ(Q)) = ϕ(d∆ (Q)).
0
2
1 A1A2
v11
v21
B1
B2 C2
C1
A• = d (0,1)(Q)
d(0,2)(Q) = C•B• = d (1,2)(Q)
d(0,1,2)(Q)
Figure 12. A triangular quiver (this one is associated to a Lie group of t ype C2).
Deﬁnition 4.14. Let Q be a triangular quiver such that the edge sub-quivers are iso morphic as sets of
vertices. That is, ﬁx isomorphisms ϕ : d (0,1)(Q) ∼= d(0,2)(Q) and ψ : d (0,2)(Q) ∼= d(1,2)(Q). Then we deﬁne
• Q0– 2 as the quiver obtained by identifying two copies of Q along ϕ, and
• Q1– 3 as the quiver obtained by identifying two copies of Q along ψ.
In performing the identiﬁcation of vertices, edge weights a re added. They need not agree, and in particular
might cancel; see Figures 13 a and 13 b.
This is a special case of amalgamation as deﬁned in [FG06a, §2.2].
Deﬁnition 4.15. A quiver has triangulation-compatible symmetry if
(1) It is triangular by Deﬁnition 4.13,
(2) There is a quiver mutation µrot which is an isomorphism of triangular quivers between Q and Q′,
where Q′ is obtained from Q by permuting simplex indices from (0, 1, 2) to (2, 0, 1).
(3) There is a quiver mutation µﬂip which transforms Q0– 2 to Q1– 3.
18
0
1
2
0
1
2
ϕ
0
1
2
3
(a) Construction of Q0– 2 (for G of type C2).
0
1
2
0
1 2
ψ
0
1
2
3
(b) Construction of Q1– 3 (for G of type C2).
Figure 13. Amalgamating triangular quivers.
If T is an oriented triangulation of a surface, and T ′ is an orientation-preserving retriangulation of T ,
then inscribing Q in each simplex of T and T ′ and amalgamating along edges results in two quivers that
diﬀer by some sequence of µrot and µﬂip . Therefore, if the cluster variables of Q are coordinates for the
representation variety, the existence of µrot andµﬂip will (eventually) show the variety to be independent of
the speciﬁc choice of triangulation.
Deﬁnition 4.16. Fix a semisimple Lie group G over C with a ﬁxed maximal torus H and a maximal
unipotent subgroup N+, with B+ =HN +. A quiver Q carries a F ock–Goncharov coordinate structure
for G if
(1) Q has triangulation-compatible symmetry as in Deﬁnition 4.1 5.
(2) Each of the edge sub-quivers of Q are of half-Dynkin type for G, as by Deﬁnition 4.8, and the
isomorphisms ϕ and ψ of Deﬁnition 4.14 identify vertices that come from the same n odes in the
Dynkin diagram.
(3) There exists a map M : Conf ∗
3(G/N+) →T A
Q , which is a birational equivalence.
(4) Moreover, M respects the rotation. That is, the following diagrams comm ute:
Conf ∗
3(G/N+) T A
Q Conf ∗
3(G/B+) T X
Q
Conf ∗
3(G/N+) T A
µrot(Q) Conf ∗
3(G/B+) T X
µrot(Q)
M
rot µ∗
rot
M
rot µ∗
rot
M M
with rot : (g0K,g 1K,g 2K) ↦→(g2K,g 0K,g 1K) (see also Figure 14).
(5) Moreover, M respects the ﬂip. That is, the following diagrams commute:
Conf ∗
3(G/N+) ×sG
02 Conf ∗
3(G/N+) T A
Q0– 2 Conf ∗
3(G/B+) ×sG
02 Conf ∗
3(G/B+) T X
Q0– 2
Conf ∗
3(G/N+) ×sG
13 Conf ∗
3(G/N+) T A
Q1– 3 Conf ∗
3(G/B+) ×sG
13 Conf ∗
3(G/B+) T X
Q1– 3
M
Ψ 13◦Ψ −1
02 µ∗
ﬂip
M
Ψ 13◦Ψ −1
02 µ∗
ﬂip
M M
where Ψ jk are deﬁned as in Deﬁnition 4.6 (see also Figure 15).
19
Remark 4.17. By the map p of Deﬁnition 2.32, M provides a map to T X
Q . In fact, this map factors through
Conf ∗
3(G/B+). By abuse of notation, we also refer to this map as M in Items 4 and 5.
Example 4.18. Figures 14 and 15 illustrate the last two demands: to move bac k and forth between
Conf ∗
3(G/N+) and T A
Q , or Conf ∗
4(G/N+) and T A
Q0– 2 in terms of coordinates and quiver mutations.
g1N+
g2N+
g0N+
g0N+
g1N+
g2N+
01
2
B1
B2
A2 A1
C1
C2
v11
v21
1
2
0
B1
B2
A2 A1
C1
C2
v′
11
v′
21
0
1
2
B1
B2A2
A1
C1C2
v′
11
v′
21
M
M
rot
µrot
∼=
Figure 14. Quiver for type C2, illustrating µ∗
rot ◦ M = M ◦ rot, with T A
Q depicted by a
graph for Q.
g0N+
g1N+
g2N+
g3N+
g0sGN+
g1N+
g2N+
g0N+
g3N+
g2N+
g1N+
g2N+
g3N+
g0N+
g1sGN+ g3N+
0
1
2
3
0
1
2
3
Ψ 02
Ψ 13
M
M
Ψ 13 ◦ Ψ −1
02 µflip
Figure 15. Quiver for type C2, illustrating µ∗
ﬂip ◦ M = M ◦ Ψ 13 ◦ Ψ −1
02 . The tetrahedron
shows the use of the ﬂip in the 3-manifold context.
We can now restate Theorem 1.1 as the following
20
Theorem 4.19. For a split semisimple simply-connected (or centerless) alg ebraic group G over Q, a quiver
with a Fock–Goncharov structure exists.
We will mostly focus on the simple case. The semisimple case f ollows quickly as described in Section 8.
The construction for Theorem 4.19 is given in Section 5.
4.3. F rom coordinates to representations. The Fock–Goncharov program for deﬁning AG,Σ and XG,Σ
works for any compact, oriented Σ with boundary components. In the case that the boundary cons ists
of punctures, we can describe reconstructing a representat ion from a point in the moduli space. We start
with the A-coordinate version due to complications in technicalitie s, referring to [FG06b, Section 8], [Zic19,
Section 6] for more details.
We start with an ideal triangulation T of Σ , together with a quiver Q and seed torus T A
Q for each triangle
in T , amalgamated together.
First, we truncate the triangulation, as in Figure 16 a. We will associate an element of G to each directed
edge: elements on the long edges will be called αij, and elements on short edges will be called βijk . The
local labeling of vertices by 0, 1, and 2 is determined by triangularity (see Deﬁnition 4.13) of the q uiverQ.
01
2
α01
α20α12
β012
β120
β201
(a) A truncated simplex. “Long” edges are in
black, “short” edges are in blue.
01
2
α01
α20α12
β012
β120
β201
γ210
γ120
(b) A doubly-truncated simplex. “Long” edges
are in black, “middle” edges are in blue, “short”
edges are in red.
Figure 16. Truncations of T . The left is used for A-coordinates, the right for X -
coordinates.
To compute ρ(γ), we homotope γ to follow these edges, then multiply together the elements i n the order
given by γ. When the orientation of γ disagrees with the orientation of the edge, we use the invers e of the
attached element.
All that remains is to give a formula for the αij and βijk .
• We start with an element in T A
Q ; the A-coordinates of Q.
• Since we have a Fock–Goncharov coordinate structure, we may apply (M)−1. This gives an explicit
element of Conf ∗
3(G/N+). It is most conveniently expressed as (h1,h 2,h 3,u ).
• Set
α01 =w0h1 u0 =u β 201 = (w0(h1)h2)−1 (ΨΦΨ)( u0) (w0(h1)h2)
α12 =w0h2 u1 = (w0(h1)h2)−1 (ΦΨ) 2(u0) (w0(h1)h2) β120 = (w0(h2)h3)−1 (ΨΦΨ)( u1) (w0(h2)h3)
α20 =w0h3 u2 = (w0(h1)h2)−1 (ΦΨ) 2(u1) (w0(h1)h2) β012 = (w0(h3)h1)−1 (ΨΦΨ)( u2) (w0(h3)h1).
Remark 4.20. Since all βijk are assigned elements of N+, and any peripheral γ can be homotoped to follow
only short edges, any ρ constructed this way is boundary-unipotent.
Also, given a point in X +
G,Σ , we can reconstruct a boundary-borel representation ρ (up to conjugation) as
follows. We refer to [FG06b, Section 6], [GGZ15, Section 9] f or more details.
Again, we start with an ideal triangulation T of Σ , together with a quiver Q and seed torus T X
Q for each
triangle in T . Instead of triangulating, however, we doubly triangulate , as in Figure 16 b. To compute ρ(γ),
we homotope γ to follow the edges, then multiply αij, βijk , or γijk (or their inverses) as appropriate.
• We start with elements of T X
Q .
21
• Taking (M)−1 gives elements of Conf ∗
3(G/B+) for each triangle. To compute edges at a particular
triangle, assume its ﬂags are (g0B+,g 1B+,g 2B+) = ( B+,w0B+,u xB+), and that the neighboring
triangles have vertices (0, 1, 3), (1, 2, 4), and (2, 0, 5) (with cosets g3B+, g4B+, and g5B+).
• Recall n(u) of Deﬁnition 4.4. The element assignments are
α01 =w0 α12 =w0 α20 =w0
β012 = Φ −1(ux) β120 =w0−1u−1
x w0 β201 =
(
Φ −1(u−1
x )
)−1
γ012 =n(g3) γ120 =n([w0u−1
x g4]−) γ201 =n([w0[w0
−1u−1
x ]−1
− w0
−1u−1
x g5]−]−)
γ102 = (n([w0g3]−))−1 γ210 =
(
n(u−1
x g4)
)−1
γ021 =
(
n([w0[w0
−1ux]−w0
−1g5]−)
)−1
Remark 4.21. All middle edges are assigned elements of N+, and all short edges are assigned elements of H.
Therefore any peripheral loop lies in B+ and ρ is boundary-borel.
Remark 4.22. Sincen(u) may require taking square roots, the ﬁeld over which the X -coordinates are deﬁned
may need to be extended in order to deﬁne ρ.
Since we can now explicitly interpret points in these moduli spaces as representations, we describe the
positivity conditions of higher Teichmüller spaces.
Deﬁnition 4.23. Let N+ be a maximal unipotent subgroup of G. Then Deﬁnition 2.23 gives coordinate
charts on N+ for each presentation of w0. These charts are the positive structure on N+. The elements
of N+ which have coordinates entirely in R>0 for all these charts are the positive part of N+.
The maps χωk of Deﬁnition 2.8 are also a positive structure on the maximal torus H ofG. Again, the
positive part consists of the elements which have coordinates in R>0 by the positive structure.
By [FG06b, Section 8.1], together with the canonical form of Lemma 4.3, these provide a positive
structure, and a positive part , of Conf ∗
3(G/N+). There is also a completely analogous positive structure
on Conf ∗
3(G/B+) following [FG06b, Section 5.5].
Remark 4.24. Generalized minors are compatible with these positive stru ctures, as from [FG06b, Theo-
rem 5.1]. Therefore, positive points in the ﬂag varieties Conf ∗
3(G/K) are exactly those points for which all
A- and X -coordinates in the cluster ensemble are in R>0.
Deﬁnition 4.25. The space T +(Σ) is Teichmüller space, together with choices of orientation for non-cuspidal
boundary components. For a surface Σ with n ≥ 0 boundary circles b1,...,b n, deﬁne
T +(Σ) = { (p,ǫ 1,...,ǫ n) : p ∈ T (S),ǫ i = ±1 },
where ǫi is positive to denote that the chosen orientation of bi agrees with that naturally induced by Σ .
Remark 4.26. When Σ has only cuspidal boundary components, T +(Σ) = T (Σ) .
Deﬁnition 4.27. WhenG is centerless, we may repeat the above construction, but tak e the X -coordinates
of the cluster ensemble. This gives the moduli space XG,Σ of framed, G-local systems on Σ by [FG06b,
Section 2.1]. The R>0 points also give X +
G,Σ . This space is identiﬁed with T +(Σ) .
That T +(Σ) appears instead of T (Σ) is rather a technicality. Restricting our attention to orde rings
of ideal triangulations that agree with the surface’s natur al orientation restrictrs T +(Σ) to a set we can
canonically identify with T (Σ) .
Deﬁnition 4.28. When G is simply connected, choose an ordered, oriented triangula tion of Σ . Associate
a copy of Q to each triangle, and amalgamate all the quivers together by identifying shared edge vertices
between triangles. The A-coordinates of the cluster ensemble form the moduli space AG,Σ .
By [FG06b, Section 8.6] the C-points of this moduli space parameterize twisted, decorated repre-
sentations into G. The R>0-points give A+
G,Σ , a higher T eichmüller space . These correspond to ﬂag
varieties such that all generalized minors are strictly pos itive.
These moduli spaces have further interpretations and prope rties, explored in [FG06b], [FG06a], [FG09a],
[GS18], etc.
22
