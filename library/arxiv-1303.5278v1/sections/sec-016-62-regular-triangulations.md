---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-016-62-regular-triangulations
section_title: "Regular triangulations"
section_number: 6.2
pages: 34-41
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
6.2. Regular triangulations.The concept of a regular triangulation comes from the study
of triangulations of convex polytopes inRn. Here we are not dealing with topological trian-
gulations, where tetrahedra may have self-identiﬁcations or two vertices may have multiple
edges connecting them. Rather, the vertices are concrete points inRn, the edges are straight
line segments in Rn and so on. In this context, a triangulation of a convex polytope is a
subdivision of the polytope into concrete Euclidean simplices. Roughly speaking, a triangu-
lation of a polytope inRn is regular if it is isomorphic to the lower faces of a convex polytope
in Rn+1. The following series of deﬁnitions make this idea precise.
Deﬁnition 6.7.An aﬃne combinationof a set of points(pj)j∈C in Rn is a sum∑
j∈Cλjpj
where ∑
j∈Cλj = 1. A set of points is aﬃnely independent if none of them is an aﬃne
combination of the others. Ak–simplexis the convex hull of an aﬃnely independent set of
k + 1 points.
Deﬁnition 6.8.Apoint conﬁgurationis a ﬁnite set of labelled points inRn. Let A = (pj)j∈J
be a point conﬁguration with label setJ. ForC⊂J, theaﬃne span ofC in A is the set of
aﬃne combinations of the set of points labelled byC. The dimension ofC is the dimension
of the aﬃne span ofC. The convex hull ofC in A is the convex hull inRn of the set of
points labelled byC.
convA(C) :=
{∑
j∈C
λjpj|λj≥ 0 for allj∈C, and
∑
j∈C
λj = 1
}
The relative interior ofC in A is the interior of the convex hull in its aﬃne span.
relintA(C) :=
{∑
j∈C
λjpj|λj > 0 for allj∈C, and
∑
j∈C
λj = 1
}
Deﬁnition 6.9.With the above notation, ifψ∈ (Rn)∗ is a linear functional, then theface
of C in directionψ is the subset ofC given by
faceA(C,ψ ) :=
{
j∈C|ψ(pj) = max
b∈C
(ψ(pb))
}
If F is a face ofC, we writeF≤A C and if in additionF⁄=C we writeF <A C.
Deﬁnition 6.10.With the above notation, a collectionS of subsets ofJ is a polyhedral
subdivision of A if it satisﬁes the following conditions. (The elements ofS are calledcells.)
(1) IfC∈ S and F≤C then F∈ S.
(2)∪C∈SconvA(C)⊃ convA(J).
(3) IfC⁄=C′ are two cells inS then relintA(C)∩relintA(C′) =∅.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 35
Remark 6.11. The ﬁrst condition says that if some cell is in our subdivision then all faces
of it are also. The second condition says that it is a subdivision of the whole convex hull of
the points inA. The third condition says that the cells can only overlap with each other on
their faces, not their interiors.
Deﬁnition 6.12.With the above notation, atriangulation of A is a polyhedral subdivision
of A such that every cell is a simplex.
Deﬁnition 6.13.Let A = (pj)j∈J be a point conﬁguration with label setJ. Suppose that
ω : A→ R is any map. Thelifted point conﬁgurationin Rn+1 is the point conﬁguration
Aω = (pω
j )j∈J := (pj,ω (pj))j∈J
(again with label setJ) given by adjoining to each vector ann + 1th coordinate given by
the value ofω at that point. Consider the set of faces of convAω(J). A lower face of this
convex hull is a face that is “visible from below”. That is, faceAω(J,ψ ) is a lower face ifψ is
negative on the last coordinate.
Deﬁnition 6.14.The regular polyhedral subdivision ofA produced byω, denoted S(A,ω ),
is the set of lower faces of the point conﬁgurationAω.
Note that a face in these deﬁnitions is a set of labels for the point conﬁguration. So the
set of faces making up the polyhedral subdivision ofA is deﬁned in terms ofAω, but this
works because the same set of labels is used for the two point conﬁgurations. Lemma 2.3.11
of [DLRS10] shows thatS(A,ω ) is indeed a polyhedral subdivision ofA, for everyω.
Deﬁnition 6.15.A regular triangulation ofA is a regular polyhedral subdivision ofA that
is a triangulation ofA.
Proposition 2.2.4 of [DLRS10] shows that every point conﬁguration has a regular trian-
gulation. The connection between regular triangulations of point conﬁgurations and our
situation can be made via the Klein model ofH3. In this model, geodesics are represented
as straight lines in Euclidean space,E3. A convex ideal hyperbolic polyhedron is represented
as a convex Euclidean polyhedron whose vertices lie on a sphere. Such a Euclidean polyhe-
dron can be seen as a point conﬁguration, with the points consisting of the vertices of the
polyhedron. Note that this is a more restrictive situation than the full generality discussed
in [DLRS10] – since all the vertices lie on a sphere, there can be no internal points, and no
three points can lie on a line. These observations imply that the set of subdivisions of a
convex ideal hyperbolic polyhedron into (strictly positive) volume ideal hyperbolic tetrahe-
dra is in one-to-one correspondence with the set of triangulations of the convex Euclidean
polyhedron, in the sense of Deﬁnition 6.12. The bijective map between the two sets preserves
the combinatorial structure of the triangulations.
Deﬁnition 6.16.Given the above discussion, we deﬁne aregular ideal triangulationof a
convex ideal hyperbolic polyhedron to be an ideal triangulation of the polyhedron whose
corresponding Euclidean triangulation of the corresponding convex Euclidean polyhedron is
regular.3
3Note that this deﬁnition has no relation to the deﬁnition of a regular ideal hyperbolic tetrahedron, in
the sense of a tetrahedron with all dihedral angles beingπ/3.
36 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
We are now in a position to be able to deﬁne our class of triangulationsXEP
M .
Deﬁnition 6.17.LetM be a cusped hyperbolic 3–manifold. LetP be the PPP–cellulation
ofM derived from the Epstein–Penner decomposition ofM (choosing equal volumes for the
cuspsifthereismorethanone)byinsertingpolygonalpillowsbetweenanytwonon-triangular
faces of the decomposition. The class of triangulations XEP
M consists of all triangulations
constructed via the following method:
(1) Insert a regular ideal triangulation of each polyhedronP of P intoP.
(2) Each polygonal pillowQ has two (not necessarily distinct) polyhedraP− and P+
glued to it. The regular ideal triangulations ofP− and P+ induce triangulationst−
and t+ of the two polygonal faces ofQ. Insert intoQ a layered triangulation ofQ,
bridging betweent− and t+.
Note that although there are only ﬁnitely many regular ideal triangulations of a given
convex ideal polyhedron, there may be inﬁnitely many triangulations inXEP
M , since the
layered triangulations can be arbitrarily long.
Remark 6.18. From the geometric construction, every triangulation ofXEP
M has a natural
semi-angle structure, as in Remark 6.6, so they are all 1-eﬃcient by Theorem 1.5.
Deﬁnition 6.19.The corank of ad–dimensional point conﬁguration withn points is the
numbern−d− 1.
A point conﬁguration has corankzero if and only if it is aﬃnely independent. A point
conﬁguration has corankone if and only if it has a unique aﬃne dependence relation. This
means that there is a unique solution to
∑
j∈J
λjpj = 0 with
∑
j∈J
λj = 0, where at least oneλj⁄= 0.
Uniqueness is up to scaling allλ’s by the same factor. The aﬃne dependence dividesJ into
three subsets:
J+ :={j∈J|λj > 0}, J 0 :={j∈J|λj = 0}, J − :={j∈J|λj < 0}.
(Which is which ofJ+ andJ− is not well deﬁned since we can multiply all of the coeﬃcients
by−1 to swap them.) Then relintA(J+)∩relintA(J−) is a single point, given by
∑
j∈J+
λjpj =
∑
j∈J−
−λjpj,
where we have normalised theλ’s so that
∑
j∈J+
λj =
∑
j∈J−
−λj = 1.
Deﬁnition 6.20.Let A = (pj)j∈J be a point conﬁguration with label setJ. A subset ofJ
is called acircuit,Z, if it is a minimal aﬃnely dependent set (i.e. it is dependent, but every
proper subset is independent).
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 37
In the above discussion,Z = J+∪J−, andZ is partitioned into the two sets,Z+ = J+
and Z− = J− since if λj = 0 in the aﬃne dependence then it could be removed fromZ,
contradicting minimality.
In R3, ﬁve points in general position are a circuit, but there may be circuits with fewer
points. Four points are a circuit if they lie in a plane, three if they lie on a line, and two
if they are coincident. However, for our purposes the points are the vertices of a convex
Euclidean polyhedron, so we may assume that there are no repeated points. Moreover, the
points lie on a sphere, so no three lie on a line. Therefore, the only two possibilities are ﬁve
points in general position, or four points that lie on a plane, as shown in Figure 16.
−
+
−
+
+
+
+
−
−
Figure 16. Circuits with 4 and 5 elements.
Remark 6.21. For us then, the only possible corank one conﬁgurations are
(1) ﬁve points in general position, or
(2) four points in a plane, or
(3) four points in a plane plus one point not in that plane.
Deﬁnition 6.22.Let S be a polyhedral subdivision that is not a triangulation. ThenS is
an almost–triangulationif
(1) all of the cells ofS have corank at most one, and
(2) all of the cells ofS of corank one contain the same circuit.
Lemma 6.23. In our case, the 3–cells of an almost–triangulation are all simplices apart
from one or two 3–cells. These 3–cells can have the following forms:
(1) The convex hull of ﬁve points on a sphere, in general position, as in the upper diagram
of Figure 17.
(2) A 4–sided pyramid, with the base of the pyramid on a boundary face of the polyhedron,
as in the upper diagram of Figure 18a.
(3) Two 4–sided pyramids whose bases are coincident, as in the upper diagram of Figure
18b.
Proof. This follows immediately from Deﬁnition 6.22 and Remark 6.21. □
Deﬁnition 6.24.Let S and S′ be two polyhedral subdivisions of a point conﬁgurationA.
Then S is a reﬁnement ofS′ if for eachC∈ S, there is aC′∈ S′ with C⊂C′.
38 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
reﬁnement reﬁnement
ﬂip
Figure 17. The almost–triangulation in case (1) of Lemma 6.23, and its
two reﬁnements to triangulations. Note that although the top and lower left
pictures are identical, the top is to be interpreted as a single 3–cell, while
the lower left shows two tetrahedra meeting in a triangle. The associated ﬂip
between the two triangulations is a 2–3 ﬂip.
Lemma 6.25 (Corollary 2.4.6 of [DLRS10]). Every almost–triangulation has exactly two
proper reﬁnements, which are both triangulations.
Deﬁnition 6.26.Two triangulations of the same point conﬁguration areconnected by a ﬂip
supported on the almost–triangulationS if they are the only two triangulations reﬁningS.
Deﬁnition 6.27.We call the ﬂips associated to the three possible almost–triangulation
types listed in Lemma 6.23 the2-3 ﬂip, external 2–2 ﬂip, andinternal 2–2 ﬂiprespectively.
See Figures 17 and 18.
Deﬁnition 6.28.The ﬂip graphof the point conﬁgurationA is the graph whose vertices
are the triangulations ofA and whose edges are triangulations connected by ﬂips.
We use the following result, due to Gelfand, Kapranov and Zelevinsky, and given as
Corollary 5.3.14 in [DLRS10].
Theorem 6.29(Gelfand, Kapranov and Zelevinsky [GKZ94]). Let A be a point conﬁgura-
tion. The subgraph of the ﬂip graph induced by all regular triangulations ofA that use the
same vertices is connected.
In our case, since the vertices lie on a sphere, all vertices are used in every triangulation,
so this says that we can get from any regular triangulation of the polyhedron to any other
by performing ﬂips.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 39
reﬁnement reﬁnement
ﬂip
v1
v2
v3
v4
(a) The almost–triangulation in
case (2) of Lemma 6.23, and its two
reﬁnements to triangulations.
reﬁnement reﬁnement
ﬂip
v1
v2
v3
v4
(b) The almost–triangulation in
case (3) of Lemma 6.23, and its two
reﬁnements to triangulations.
Figure 18. Almost–triangulations in cases (2) and (3) of Lemma 6.23, and
the associated 2–2 ﬂips. In all diagrams, verticesv1 through v4 are coplanar.
Remark 6.30. Our strategy for connecting two triangulations T1, T2 ∈ XEP
M is as follows.
Both triangulations consist of regular triangulations of the polyhedra of the PPP–cellulation,
together with layered triangulations in the polygonal pillows between them.
(1) UseTheorem6.29oneachpolyhedron, tochangethetriangulationofeachpolyhedron
in T1 into the corresponding triangulation of the polyhedron inT2. This step may
alter the triangulations of the polygonal pillows as well.
(2) Change the triangulation in each polygonal pillow of the resulting triangulation so
that it matches with the corresponding triangulation inT2. This step does not alter
the triangulations of the polyhedra.
6.3. Interpreting ﬂip moves using 2–3 moves.In order to carry out step (1) of our plan
in Remark 6.30, we will interpret the ﬂip moves in terms of the 2–3 and 3–2 moves allowed
in Theorem 1.1.
(1) First, consider a 2–3 ﬂip in one polyhedron. This is simply a 2–3 move. Since the
triangulations on either side of the move are inXEP
M , they are both 1–eﬃcient by
Remark 6.18. Therefore the triangulations have the same index by Theorem 1.1.
(2) Second, consider an external 2–2 ﬂip. See Figure 19a. The base of the pyramid is on
a face of the polyhedron that is glued to a polygonal pillow. The two triangles on
the base of the pyramid are glued to either a single tetrahedron in the pillow, or two
tetrahedra in either the polygonal pillow or the polyhedron on the other side of the
polygonal pillow.
• If the two triangles are glued to a single tetrahedron then we are in the situation
shown in the top diagram of Figure 19a, and we can perform a 3–2 move, which
40 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
performs the ﬂip to the polyhedron, and removes the single tetrahedron from
the layered triangulation of the polygonal pillow.
• Otherwise, we perform a 2–3 move, which performs the ﬂip to the polyhedron,
and adds a ﬂat tetrahedron to the layered triangulation of the polygonal pillow.
(Note that we could use only this move, even in the previous case; the diﬀerence
between the two options is a 0–2 move.)
Once again, the triangulations on either side of the move are inXEP
M , so they are both
1–eﬃcient and the triangulations have the same index.
(3) Lastly, consider an internal 2–2 ﬂip. See Figure 19b. We can perform a 2–3 move
followed by a 3–2 move, which together perform the ﬂip. Since the four vertices in
the circuit are coplanar, at the intermediate step we introduce a ﬂat tetrahedron.
The intermediate triangulation is not inXEP
M , since it includes a ﬂat tetrahedron in a
polyhedron, and so the polyhedron does not have a regular triangulation. However,
the intermediate triangulation still has a natural semi–angle structure in the obvious
way, and so it is 1–eﬃcient, and again the three triangulations involved all have the
same index.
3–2
2–3
v1
v2
v3
v4
v1
v2
v3
v4
(a) Two possible ways to perform
an external 2–2 move, depending
on whether or not there is a suit-
able ﬂat tetrahedron in the polygo-
nal pillow that the base of the pyra-
mid is glued to.
2–2
2–3 3–2
v1
v2
v3
v4
(b) An internal 2–2 ﬂip, obtained
by performing a 2–3 move followed
by a 3–2 move. At the intermediate
step we get a ﬂat tetrahedron with
verticesv1 through v4.
Figure 19. The possible 2–2 moves on a triangulation of a point conﬁgura-
tion, realised using 2–3 and 3–2 moves. Again in each case, verticesv1 through
v4 are coplanar.
The arguments so far show that we can achieve step (1) of Remark 6.30. Now we need to
deal with step (2).
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 41
