---
doc_id: arxiv-1307.6697v2
doc_title: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS"
section_id: sec-004-5-holonomy-of-a-decoration
section_title: "Holonomy of a decoration"
section_number: 5
pages: 9-12
source_pdf: 1307.6697v2.pdf
source_sha256: a3afaefdaebe0292
toc_source: outline
doc_brief: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS — In this paper we are interested in computing representations of the funda- mental group of a 3-manifold into PGL(3, C) (in particular in PGL(2"
---
In this section we recall how to compute the holonomy of a decoration described above
(see [2] for more details). A decoration of a triangulation of a manifold M gives rise to a
representation (called holonomy representation)
ρ : π1(M, p0) →PGL(3, C).
The base point is not important if we study representations up to conjugation. In fact, each
solution of the consistency equations gives a conjugacy class of representations but a special
choice of base point and side pairings is needed in explicit computations. The idea is to
10
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
follow a path in the fundamental group from face to face keeping track of changes using a
coordinate system adapted to the faces.
In order to compute holonomies we ﬁrst ﬁx a face (with ordered vertices) of one of the
tetrahedra and a base point on the face. We then follow paths representing the generators
of the fundamental group of the manifold which we decompose into arcs contained in each
tetrahedron and which are transverse to their sides. For each arc we write the contribution
to the holonomy as is explained in the following.
Given a tetrahedron (ijkl), the arc going from face (ijk) to face (ijl) can be represented
by a "left turn" arc around the edge (ij). We will also consider permutations of a face as
for example, the permutation (ijk) →(jki).
To follow the change in the holonomy along these arcs we associate to each face, that is, to
a conﬁguration of 3 generic ﬂags ([xi], [fi])1≤i≤3 with triple ratio X, a projective coordinate
system of CP2: take the one where the point x1 = [1 : 0 : 0]t, f1 = [0 : 0 : 1], x2 = [0 : 0 : 1]t,
f2 = [1 : 0 : 0], the point x3 has coordinates [1 : −1 : 1]t and f3 = [X : X + 1 : 1].
The cyclic permutation of the ﬂags (ijk) →(jki) with triple ratio X induces the coordi-
nate change given by the matrix
T (X) =


X
X + 1
1
−X
−X
0
X
0
0

.
It is also useful to consider the transposition (ijk) →(jik) which is given by the matrix
I =


0
0
1
0
1
0
1
0
0

.
Remark then that
T ( 1
X ) = I ◦T −1(X) ◦I.
If we have a tetrahedron of ﬂags (ijkl) with its z-coordinates, then the basis related to the
triple (ijl) is obtained in the coordinate system related to the triple (ijk) by the coordinate
change given by the matrix
(ijk) →(ijl) =




1
zji
0
0
0
1
0
0
0
zij



.
5.1. Representation of the fundamental group. We obtain the change of coordinate
matrix of a path in the triangulation by decomposing it in the two elementary steps described
in the previous section and multiplying the change of coordinate matrices for each step from
left to right. Finally, to obtain the representation of the fundamental group we take the
inverse of the coordinate change matrix for each path representative of an element of the
fundamental group.
One has to be careful if we want to obtain a representation in PU(2, 1). In general we
need to conjugate the above representation by an element so that the group preserves a
chosen hermitian form.
11
Let (i0j0k0) (an ordered triple of points in a face of tetrahedron T0) be the base point and
Z0 = zi0j0k0(T0) be its 3-ratio. We consider the transformation A =


−1+Z0
Z0
0
0
0
−1
0
0
0
1


such that A·


1
1+Z0
1
1

=


1
−1
1

. The hermitian form J is preserved if we conjugate the group
elements by A, or equivalently the group preserves the hermitian form J0 = tA
−1JA−1 with
eigenvalues 1, 1/ |1 + Z0| , −1/ |1 + Z0|. We will show computations in a speciﬁc example in
a future section.
5.2. Boundary holonomy. If we follow a path in a boundary torus of a triangulated
manifold we will obtain, applying the procedure above, a coordinate change. We obtain
then a representation of the fundamental group of the boundary in PGL(3, C). Each torus
is associated to a vertex and therefore the representation of its fundamental group ﬁxes a
ﬂag. Choosing the ﬂag properly up to conjugation, we can arrange it so that the boundary
representation is upper triangular. Given two generators of a torus group represented by
paths a and b one can compute easily the eigenvalues of the holonomy along them.
We suppose a path is contained in the link of the vertex and is transverse to the edges of
the triangulation induced by the tetrahedra. Consider a path segment at the link of vertex i
which is turning left around the edge ij, that is (ijk) →(ijl). Then, as before, the holonomy
change of coordinate matrix is


1
zji
0
0
0
1
0
0
0
zij

.
Consider the path segment at the link of vertex i which is turning right around the edge ij,
that is
(ilj) →(ikj).
Then the holonomy change of coordinate matrix is




zklzlk
zij
−
zkl
zijzlj −
1
zki
−zil
zki
0
1
zil
0
0
1
zij



.
Both matrices being upper diagonal, to ﬁnd the eigenvalues we need only to multiply
the diagonal terms. The eigenvalues of the boundary holonomy are the diagonal elements
obtained as above. We will note A∗and A the two eigenvalues (the ﬁrst and the third with
the normalization as above so that the second eigenvalue be one) of the path a and B∗and
B the two eigenvalues of the path b.
5.3. Boundary unipotent holonomy equations. The boundary holonomy gives a rep-
resentation of the fundamental group of the boundary tori into PGL(3, C). If t is the number
of boundary tori, we note
ρb : (Z ⊕Z)t →PGL(3, C).
12
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
For knots we can deﬁne canonical generators of the boundary torus called meridian and
longitude. But, for simplicity, we will refer to generators of boundary tori for other manifolds
as well as meridians and longitudes, denoted m and l. The abelian group generated by the
image of ρb is called the peripheral group. It turns out that an important information on the
representations is the rank of the peripheral group. For instance, examples of uniformizable
CR manifolds were obtained precisely when the rank of the peripheral group is one (see
[21, 8, 19]).
We say the representation is unipotent if the boundary holonomy is unipotent. That is, if
the boundary holonomy representation can be given by matrices (up to scalar multiplication)
of the form


1
⋆
⋆
0
1
⋆
0
0
1

.
That is, all eigenvalues are equal.
In the following we will ﬁnd unipotent representations associated to parabolic decora-
tions. That means that for each boundary torus we compute the eigenvalues A∗, A, B∗, B
corresponding to generators a and b at each torus and impose the equations
A∗= A = B∗= B = 1.
We remark that each eigenvalue is a rational function of the cross-ratio coordinates.
