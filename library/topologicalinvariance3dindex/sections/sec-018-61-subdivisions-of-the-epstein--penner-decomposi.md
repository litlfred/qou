---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-018-61-subdivisions-of-the-epstein--penner-decomposi
section_title: "Subdivisions of the Epstein--Penner decomposition"
section_number: 6.1
pages: 32-34
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
bolic 3manifold M, the EpsteinPenner decomposition (see [EP88]) divides M into a 
nite
number of ideal hyperbolic polyhedra. This subdivision is canonical, depending only on the
topology of the manifold, if M has a single cusp. If M has r ≥1 cusps, then the Epstein-
Penner cell decomposition is canonical up to the choice of a scale vector (t1, . . . , tr) with
t1, t2, . . . , tr > 0 giving the relative size of the cusps. The scale vector is well-de
ned up to
multiplication by a positive real number. For the purposes of de
ning our canonical set, we
can choose all ti to be the same.
Very often, the cells of the decomposition are all ideal tetrahedra, but other polyhedra
can occur. For many applications, including the use in this paper, we need a subdivision
of M into ideal tetrahedra only.
It is well known that every cusped 3manifold has a
decomposition into ideal tetrahedra, but one often needs more than a purely topological
structure on the tetrahedra. The EpsteinPenner decomposition, coming as it does with
a geometric structure, provides all of the nice geometric properties one could want. So,
in the cases when the cells of the decomposition are not themselves tetrahedra, we would
like to further subdivide the polyhedra into tetrahedra.
However, there is no canonical
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
33
way to subdivide, and it is not even clear if one can subdivide the various polyhedra in
a consistent way, so that the triangulations induced on the faces of the polyhedra match
when the polyhedra are glued to each other. In particular, it is still unknown whether every
cusped hyperbolic 3manifold admits a geometric triangulation (that is, a subdivision into
positive volume ideal hyperbolic tetrahedra), either constructed by further subdividing the
EpsteinPenner decomposition or otherwise.
However, one can use the EpsteinPenner decomposition to produce an ideal triangulation
by subdividing the ideal polyhedra, if we also allow 
at tetrahedra inserted between faces of
the polyhedra to bridge between incompatible triangulations of those faces. Such an ideal
triangulation has a natural semi-angle structure (see Remark 6.6), and so by Theorem 1.5
all of these triangulations are 1e
cient.
To describe our triangulations more precisely, we use the same notation as in [HRS12].
De
nition 6.1. In this paper, the term polyhedron will mean a combinatorial object ob-
tained by removing all of the vertices from a 3-cell with a given combinatorial cell decom-
position of its boundary. We further require that this can be realised as a positive volume
convex ideal polyhedron in hyperbolic 3-space H3.
De
nition 6.2. An (ideal) polygonal pillow or n-gonal pillow is a combinatorial object
obtained by removing all of the vertices from a 3-cell with a combinatorial cell decomposition
of its boundary that has precisely two faces. The two faces are copies of an n-gon identi
ed
along corresponding edges.
De
nition 6.3. Suppose that P is a cellulation of a 3-manifold consisting of polyhedra
and polygonal pillows with the property that polyhedra are glued to either polyhedra or
polygonal pillows, but polygonal pillows are only glued to polyhedra. Then we call P a
polyhedron and polygonal pillow cellulation, or for short, a PPP-cellulation.
De
nition 6.4. Let t be a triangulation of a polygon. A diagonal 
ip move changes t as
follows. First we remove an internal edge of t, producing a four sided polygon, one of whose
diagonals is the removed edge. Second, we add in the other diagonal, cutting the polygon
into two triangles and giving a new triangulation of the polygon.
De
nition 6.5. Let Q be a polygonal pillow, with triangulations t−and t+ given on its
two polygonal faces Q−and Q+. By a layered triangulation of Q, bridging between t−and
t+, we mean a triangulation produced as follows. We are given a sequence of diagonal 
ips
which convert t−into t+. This gives a sequence of triangulations t−= L1, L2, . . . , Lk = t+,
where consecutive triangulations are related by a diagonal 
ip. Starting from Q−with the
triangulation t−= L1, we glue a tetrahedron onto the triangulation L1 so that two of its
faces cover the faces of L1 involved in the 
rst diagonal 
ip. The other two faces together
with the rest of L1 produce the triangulation L2. We continue in this fashion, adding one
tetrahedron for each diagonal 
ip until we reach Lk = t+, which we identify with Q+.
Our class of triangulations XEP
M
of M consists of triangulations that are subdivisions
of PPP-cellulations. Our PPP-cellulation will have polyhedra being the polyhedra of the
Epstein-Penner decomposition. It also has a polygonal pillow inserted between all pairs of
identi
ed faces that have at least 4 sides.
We will form our triangulations by 
rst sub-
dividing the ideal hyperbolic polyhedra into positive volume ideal hyperbolic tetrahedra.
34 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Secondly, for each polygonal pillow, we insert any layered triangulation that bridges between
the induced triangulations of the two boundary polygons of the polyhedra to each side.
Remark 6.6. Any triangulation produced in the way described above has a natural semi
angle structure. This comes from the shapes of the tetrahedra as ideal hyperbolic tetrahedra.
The dihedral angles of the positive volume ideal hyperbolic tetrahedra, together with 0 and
π angles for the 
at tetrahedra in the layered triangulations in the polygonal pillows satisfy
all of the rules for a generalised angle structure, and all angles are in [0, π].
The natural semiangle structure together with Theorem 1.5 show that each triangulation
in our class is 1-e
cient. However, we also need to show that our class is connected under
23, 32, 02 and 20 moves, and for this we will need some extra machinery. The main tool
