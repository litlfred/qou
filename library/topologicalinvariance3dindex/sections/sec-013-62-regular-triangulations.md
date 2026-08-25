---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-013-62-regular-triangulations
section_title: "Regular triangulations"
section_number: 6.2
pages: 34-43
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
gurations, following [DLRS10].
6.2. Regular triangulations. The concept of a regular triangulation comes from the study
of triangulations of convex polytopes in Rn. Here we are not dealing with topological trian-
gulations, where tetrahedra may have self-identi
cations or two vertices may have multiple
edges connecting them. Rather, the vertices are concrete points in Rn, the edges are straight
line segments in Rn and so on. In this context, a triangulation of a convex polytope is a
subdivision of the polytope into concrete Euclidean simplices. Roughly speaking, a triangu-
lation of a polytope in Rn is regular if it is isomorphic to the lower faces of a convex polytope
in Rn+1. The following series of de
nitions make this idea precise.
De
nition 6.7. An a
ne combination of a set of points (pj)j∈C in Rn is a sum ∑
j∈Cλjpj
where ∑
j∈Cλj = 1. A set of points is a
nely independent if none of them is an a
ne
combination of the others. A ksimplex is the convex hull of an a
nely independent set of
k + 1 points.
De
nition 6.8. A point con
guration is a 
nite set of labelled points in Rn. Let A = (pj)j∈J
be a point con
guration with label set J. For C⊂J, the a
ne span of C in A is the set of
a
ne combinations of the set of points labelled by C. The dimension of C is the dimension
of the a
ne span of C. The convex hull of C in A is the convex hull in Rn of the set of
points labelled by C.
conv A(C) :=
{∑
j∈C
λjpj|λj≥ 0 for all j∈C, and
∑
j∈C
λj = 1
}
The relative interior of C in A is the interior of the convex hull in its a
ne span.
relint A(C) :=
{∑
j∈C
λjpj|λj > 0 for all j∈C, and
∑
j∈C
λj = 1
}
De
nition 6.9. With the above notation, if ψ∈ (Rn)∗ is a linear functional, then the face
of C in direction ψ is the subset of C given by
face A(C,ψ ) :=
{
j∈C|ψ(pj) = max
b∈C
(ψ(pb))
}
If F is a face of C, we write F≤A C and if in addition F⁄=C we write F <A C.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 35
De
nition 6.10. With the above notation, a collection S of subsets of J is a polyhedral
subdivision of A if it satis
es the following conditions. (The elements of S are called cells .)
(1) If C∈ S and F≤C then F∈ S.
(2) ∪C∈Sconv A(C)⊃ conv A(J).
(3) If C⁄=C′ are two cells in S then relint A(C)∩ relint A(C′) =∅.
Remark 6.11 . The 
rst condition says that if some cell is in our subdivision then all faces
of it are also. The second condition says that it is a subdivision of the whole convex hull of
the points in A. The third condition says that the cells can only overlap with each other on
their faces, not their interiors.
De
nition 6.12. With the above notation, a triangulation of A is a polyhedral subdivision
of A such that every cell is a simplex.
De
nition 6.13. Let A = (pj)j∈J be a point con
guration with label set J. Suppose that
ω : A→ R is any map. The lifted point con
guration in Rn+1 is the point con
guration
Aω = (pω
j )j∈J := (pj,ω (pj))j∈J
(again with label set J) given by adjoining to each vector an n + 1th coordinate given by
the value of ω at that point. Consider the set of faces of conv Aω(J). A lower face of this
convex hull is a face that is visible from below. That is, face Aω(J,ψ ) is a lower face if ψ is
negative on the last coordinate.
De
nition 6.14. The regular polyhedral subdivision of A produced by ω, denoted S(A,ω ),
is the set of lower faces of the point con
guration Aω.
Note that a face in these de
nitions is a set of labels for the point con
guration. So the
set of faces making up the polyhedral subdivision of A is de
ned in terms of Aω, but this
works because the same set of labels is used for the two point con
gurations. Lemma 2.3.11
of [DLRS10] shows that S(A,ω ) is indeed a polyhedral subdivision of A, for every ω.
De
nition 6.15. A regular triangulation of A is a regular polyhedral subdivision of A that
is a triangulation of A.
Proposition 2.2.4 of [DLRS10] shows that every point con
guration has a regular trian-
gulation. The connection between regular triangulations of point con
gurations and our
situation can be made via the Klein model of H3. In this model, geodesics are represented
as straight lines in Euclidean space, E3. A convex ideal hyperbolic polyhedron is represented
as a convex Euclidean polyhedron whose vertices lie on a sphere. Such a Euclidean polyhe-
dron can be seen as a point con
guration, with the points consisting of the vertices of the
polyhedron. Note that this is a more restrictive situation than the full generality discussed
in [DLRS10]  since all the vertices lie on a sphere, there can be no internal points, and no
three points can lie on a line. These observations imply that the set of subdivisions of a
convex ideal hyperbolic polyhedron into (strictly positive) volume ideal hyperbolic tetrahe-
dra is in one-to-one correspondence with the set of triangulations of the convex Euclidean
polyhedron, in the sense of De
nition 6.12. The bijective map between the two sets preserves
the combinatorial structure of the triangulations.
36 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
De
nition 6.16. Given the above discussion, we de
ne a regular ideal triangulation of a
convex ideal hyperbolic polyhedron to be an ideal triangulation of the polyhedron whose
corresponding Euclidean triangulation of the corresponding convex Euclidean polyhedron is
regular. 4
We are now in a position to be able to de
ne our class of triangulations XEP
M .
De
nition 6.17. Let M be a cusped hyperbolic 3manifold. Let P be the PPPcellulation
of M derived from the EpsteinPenner decomposition of M (choosing equal volumes for the
cusps if there is more than one) by inserting polygonal pillows between any two non-triangular
faces of the decomposition. The class of triangulations XEP
M consists of all triangulations
constructed via the following method:
(1) Insert a regular ideal triangulation of each polyhedron P of P into P .
(2) Each polygonal pillow Q has two (not necessarily distinct) polyhedra P− and P+
glued to it. The regular ideal triangulations of P− and P+ induce triangulations t−
and t+ of the two polygonal faces of Q. Insert into Q a layered triangulation of Q,
bridging between t− and t+.
Note that although there are only 
nitely many regular ideal triangulations of a given
convex ideal polyhedron, there may be in
nitely many triangulations in XEP
M , since the
layered triangulations can be arbitrarily long.
Remark 6.18 . From the geometric construction, every triangulation of XEP
M has a natural
semi-angle structure, as in Remark 6.6, so they are all 1-e
cient by Theorem 1.5.
De
nition 6.19. The corank of a ddimensional point con
guration with n points is the
number n−d− 1.
A point con
guration has corank zero if and only if it is a
nely independent. A point
con
guration has corank one if and only if it has a unique a
ne dependence relation. This
means that there is a unique solution to ∑
j∈J
λjpj = 0 with
∑
j∈J
λj = 0, where at least one λj⁄= 0.
Uniqueness is up to scaling all λ's by the same factor. The a
ne dependence divides J into
three subsets:
J+ :={j∈J|λj > 0}, J 0 :={j∈J|λj = 0}, J − :={j∈J|λj < 0}.
(Which is which of J+ and J− is not well de
ned since we can multiply all of the coe
cients
by −1 to swap them.) Then relint A(J+)∩ relint A(J−) is a single point, given by
∑
j∈J+
λjpj =
∑
j∈J−
−λjpj,
where we have normalised the λ's so that∑
j∈J+
λj =
∑
j∈J−
−λj = 1.
4 Note that this de
nition has no relation to the de
nition of a regular ideal hyperbolic tetrahedron, in
the sense of a tetrahedron with all dihedral angles being π/3.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 37
De
nition 6.20. Let A = (pj)j∈J be a point con
guration with label set J. A subset of J
is called a circuit , Z, if it is a minimal a
nely dependent set (i.e. it is dependent, but every
proper subset is independent).
In the above discussion, Z = J+∪J−, and Z is partitioned into the two sets, Z+ = J+
and Z− = J− since if λj = 0 in the a
ne dependence then it could be removed from Z,
contradicting minimality.
In R3, 
ve points in general position are a circuit, but there may be circuits with fewer
points. Four points are a circuit if they lie in a plane, three if they lie on a line, and two
if they are coincident. However, for our purposes the points are the vertices of a convex
Euclidean polyhedron, so we may assume that there are no repeated points. Moreover, the
points lie on a sphere, so no three lie on a line. Therefore, the only two possibilities are 
ve
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
Remark 6.21 . For us then, the only possible corank one con
gurations are
(1) 
ve points in general position, or
(2) four points in a plane, or
(3) four points in a plane plus one point not in that plane.
De
nition 6.22. Let S be a polyhedral subdivision that is not a triangulation. Then S is
an almosttriangulation if
(1) all of the cells of S have corank at most one, and
(2) all of the cells of S of corank one contain the same circuit.
Lemma 6.23. In our case, the 3cells of an almosttriangulation are all simplices apart
from one or two 3cells. These 3cells can have the following forms:
(1) The convex hull of 
ve points on a sphere, in general position, as in the upper diagram
of Figure 17.
(2) A 4sided pyramid, with the base of the pyramid on a boundary face of the polyhedron,
as in the upper diagram of Figure 18a.
(3) Two 4sided pyramids whose bases are coincident, as in the upper diagram of Figure
18b.
38 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Proof. This follows immediately from De
nition 6.22 and Remark 6.21. □
re
nement re
nement

ip
Figure 17. The almosttriangulation in case (1) of Lemma 6.23, and its
two re
nements to triangulations. Note that although the top and lower left
pictures are identical, the top is to be interpreted as a single 3cell, while
the lower left shows two tetrahedra meeting in a triangle. The associated 
ip
between the two triangulations is a 23 
ip.
De
nition 6.24. Let S and S′ be two polyhedral subdivisions of a point con
guration A.
Then S is a re
nement of S′ if for each C∈ S, there is a C′∈ S′ with C⊂C′.
Lemma 6.25 (Corollary 2.4.6 of [DLRS10]) . Every almosttriangulation has exactly two
proper re
nements, which are both triangulations.
De
nition 6.26. Two triangulations of the same point con
guration are connected by a 
ip
supported on the almosttriangulation S if they are the only two triangulations re
ning S.
De
nition 6.27. We call the 
ips associated to the three possible almosttriangulation
types listed in Lemma 6.23 the 2-3 
ip , external 22 
ip , and internal 22 
ip respectively.
See Figures 17 and 18.
Remark 6.28 . The internal 2-2 
ip acts on the triangulation by a move sometimes called the
4-4 move , as it removes four tetrahedra and replaces them with four others. However, here
we stick with the notation derived from the bistellar 
ip terminology.
De
nition 6.29. The 
ip graph of the point con
guration A is the graph whose vertices
are the triangulations of A and whose edges are triangulations connected by 
ips.
We use the following result, due to Gelfand, Kapranov and Zelevinsky, and given as
Corollary 5.3.14 in [DLRS10].
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 39
re
nement re
nement

ip
v1
v2
v3
v4
(a) The almosttriangulation in
case (2) of Lemma 6.23, and its two
re
nements to triangulations.
re
nement re
nement

ip
v1
v2
v3
v4
(b) The almosttriangulation in
case (3) of Lemma 6.23, and its two
re
nements to triangulations.
Figure 18. Almosttriangulations in cases (2) and (3) of Lemma 6.23, and
the associated 22 
ips. In all diagrams, vertices v1 through v4 are coplanar.
Theorem 6.30 (Gelfand, Kapranov and Zelevinsky [GKZ94]) . Let A be a point con
gura-
tion. The subgraph of the 
ip graph induced by all regular triangulations of A that use the
same vertices is connected.
In our case, since the vertices lie on a sphere, all vertices are used in every triangulation,
so this says that we can get from any regular triangulation of the polyhedron to any other
by performing 
ips.
Remark 6.31 . Our strategy for connecting two triangulations T1, T2 ∈ XEP
M is as follows.
Both triangulations consist of regular triangulations of the polyhedra of the PPPcellulation,
together with layered triangulations in the polygonal pillows between them.
(1) Use Theorem 6.30 on each polyhedron, to change the triangulation of each polyhedron
in T1 into the corresponding triangulation of the polyhedron in T2. This step may
alter the triangulations of the polygonal pillows as well.
(2) Change the triangulation in each polygonal pillow of the resulting triangulation so
that it matches with the corresponding triangulation in T2. This step does not alter
the triangulations of the polyhedra.
6.3. Interpreting 
ip moves using 23 moves. In order to carry out step (1) of our plan
in Remark 6.31, we will interpret the 
ip moves in terms of the 23 and 32 moves allowed
in Theorem 1.1.
40 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
(1) First, consider a 23 
ip in one polyhedron. This is simply a 23 move. Since the
triangulations on either side of the move are in XEP
M , they are both 1e
cient by
Remark 6.18. Therefore the triangulations have the same index by Theorem 1.1.
(2) Second, consider an external 22 
ip. See Figure 19a. The base of the pyramid is on
a face of the polyhedron that is glued to a polygonal pillow. The two triangles on
the base of the pyramid are glued to either a single tetrahedron in the pillow, or two
tetrahedra in either the polygonal pillow or the polyhedron on the other side of the
polygonal pillow.
• If the two triangles are glued to a single tetrahedron then we are in the situation
shown in the top diagram of Figure 19a, and we can perform a 32 move, which
performs the 
ip to the polyhedron, and removes the single tetrahedron from
the layered triangulation of the polygonal pillow.
• Otherwise, we perform a 23 move, which performs the 
ip to the polyhedron,
and adds a 
at tetrahedron to the layered triangulation of the polygonal pillow.
(Note that we could use only this move, even in the previous case; the dierence
between the two options is a 02 move.)
Once again, the triangulations on either side of the move are in XEP
M , so they are both
1e
cient and the triangulations have the same index.
(3) Lastly, consider an internal 22 
ip. See Figure 19b. We can perform a 23 move
followed by a 32 move, which together perform the 
ip. Since the four vertices in
the circuit are coplanar, at the intermediate step we introduce a 
at tetrahedron.
The intermediate triangulation is not in XEP
M , since it includes a 
at tetrahedron in a
polyhedron, and so the polyhedron does not have a regular triangulation. However,
the intermediate triangulation still has a natural semiangle structure in the obvious
way, and so it is 1e
cient, and again the three triangulations involved all have the
same index.
The arguments so far show that we can achieve step (1) of Remark 6.31. Now we need to
deal with step (2).
6.4. Moving paths in the 1skeleton of the associahedron using 23 and 02
moves. In order to carry out step (2) of our plan in Remark 6.31, we need to modify the
layered triangulations in the polygonal pillows. We will do this using the 23, 32, 02 and
20 moves allowed in Theorems 1.1 and 5.1.
Having completed step (1), we have two triangulations, T1 and T2, which agree on the
polyhedra but may dier in the polygonal pillows. Let Q be a polygonal pillow. Since T1
and T2 agree on the polyhedra glued to either side of Q, they agree on the triangulations of
the polygonal faces Q+ and Q−. Call these triangulations t+ and t−.
The next well-known theorem concerns the identi
cation of the set of triangulations of
an n-gon with the vertices of the associahedron Kn−2, and the set of geometric bistellar

ips with the edges of Kn−2. The associahedron Kn−2 was introduced by Stashe [Sta63].
An identi
cation of Kn−2 with a convex polytope in Euclidean space was given in the ap-
pendix to [Sta97]. The cellular decomposition of the polytope Kn−2 (and in particular, its
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 41
32
23
v1
v2
v3
v4
v1
v2
v3
v4
(a) Two possible ways to perform
an external 22 move, depending
on whether or not there is a suit-
able 
at tetrahedron in the polygo-
nal pillow that the base of the pyra-
mid is glued to.
22
23 32
v1
v2
v3
v4
(b) An internal 22 
ip, obtained
by performing a 23 move followed
by a 32 move. At the intermediate
step we get a 
at tetrahedron with
vertices v1 through v4.
Figure 19. The possible 22 moves on a triangulation of a point con
gura-
tion, realised using 23 and 32 moves. Again in each case, vertices v1 through
v4 are coplanar.
2-skeleton) is discussed at length in the above references and also in [Lod04]. The fact that
the 2-dimensional faces of the associahedron are squares and pentagons also follows from
MacLane's coherence theorem [Mac71]. A vast generalization of regular triangulations of
point con
gurations was studied by Gelfand-Kapranov-Zelevinsky, and in [GKZ94, Sec.7.3]
it is explained how to identify the secondary polytope of 2-dimensional con
gurations with
the associahedron.
Theorem 6.32. The set of triangulations of an ngon and the set of diagonal 
ips connecting
them correspond to the vertices and edges of a convex polytope called the associahedron . The
set of 2cells of the associahedron consists of squares and pentagons. Each square corresponds
to two commuting diagonal 
ips (as in De
nition 6.4) on two 4-gons whose interiors are
disjoint. Each pentagon corresponds to a pentagon relation between the 
ve triangulations
of a pentagon. See Figure 20.
Our two layered triangulations of the polygonal pillow Q can be represented as two paths
p1 and p2 in the 1skeleton of the associahedron that both start at the vertex corresponding to
t− and end at the vertex corresponding to t+. Since the fundamental group of the 2skeleton
X(2) of a CW complex X satis
es π1(X(2)) = π1(X), it follows that the 2skeleton of a
convex polytope is simply connected, and every loop along the 1-skeleton can be trivialized
by moving pieces of it across the 2-cells. It follows that the 2skeleton of the associahedron
is simply connected, and so we can homotope p1 to p2, 
xing endpoints, by moving the path
42 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
(a) A square 2cell of the asso-
ciahedron.
(b) A pentagon 2cell of the associahedron.
Figure 20. The 2cells of the associahedron.
across some 
nite sequence of the 2cells. To be precise, we can homotope p1 to p2 with a
combination of the following moves and their inverses.
(1) Remove a backtracking , that is, replace a segment of a path of the form ...,t 1,t 2,t 1,...
with ...,t 1,... , where t1 and t2 are related by a diagonal 
ip.
(2) Move a path that follows two consecutive sides of a square 2cell to follow the other
two sides.
(3) Move a path that follows three consecutive sides of a square 2cell to follow the other
side.
(4) Delete a part of a path that goes around all four sides of a square 2cell.
(5) Move a path that follows three consecutive sides of a pentagon 2cell to follow the
other two sides.
(6) Move a path that follows four consecutive sides of a pentagon 2cell to follow the
other side.
(7) Delete a part of a path that goes around all 
ve sides of a pentagonal 2cell.
These moves can be achieved as follows.
• Move (1) corresponds to performing a 20 move on the triangulation. Since the two
triangulations are both in XEP
M , they are both 1e
cient by Remark 6.18. Therefore
the two triangulations have the same index by Theorem 5.1.
• Move (2) does not change the layered triangulation at all, it only swaps the order in
which we add two non-overlapping 
at tetrahedra to the layering.
• Move (3) can be made by applying move (2) followed by move (1).
• Move (4) can be made by applying move (2) followed by move (1) twice.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 43
• Move (5) corresponds to performing a 32 move on the triangulation. As before,
since the two triangulations are both in XEP
M , they are both 1e
cient by Remark
6.18. Therefore the two triangulations have the same index by Theorem 1.1(b).
• Move (6) can be made by applying move (5) followed by move (1).
• Move (7) can be made by applying move (5) followed by move (1) twice.
Proof of Theorem 1.8. We have shown in this section that given any two triangulations in
XEP
M , the steps in Remark 6.31 can be made using 23, 32, 02 and 20 moves which preserve
the index. Thus the entire class of triangulations has the same index. Since XEP
M depends
only on the topology of M , we can take the index of any of these triangulations for the value
of the index for the manifold, and this depends only on the topology of M . □
Proof of Theorem 1.9. Fix a cusped hyperbolic manifold M and T ∈ XEP
M . T consists of
two types of tetrahedra: the ones that subdivide the ideal hyperbolic cells of the Epstein-
Penner cell decomposition of M , and the ones that are parts of the pillows. The former
have geometric shapes (i.e., shapes that are in the upper half plane), and the latter have
real non-degenerate shapes. By construction, the shapes ZT satisfy the gluing equations of
T, proving part (a). Their arguments also satisfy the gluing equations, proving part (c).
Also by construction, the shapes ZT and ZT′ are related by 23, 32, 02 and 20 moves
if the corresponding triangulations T and T′ are related by the same moves. □
