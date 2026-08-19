---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-015-61-subdivisions-of-the-epsteinpenner-decompositi
section_title: "Subdivisions of the Epstein–Penner decomposition"
section_number: 6.1
pages: 32-34
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
bolic 3–manifoldM, the Epstein–Penner decomposition (see [EP88]) dividesM into a ﬁnite
number of ideal hyperbolic polyhedra. This subdivision is canonical, depending only on the
topology of the manifold, ifM has a single cusp. IfM has r≥ 1 cusps, then the Epstein-
Penner cell decomposition is canonical up to the choice of a scale vector(t1,...,t r) with
t1,t 2,...,t r > 0 giving the relative size of the cusps. The scale vector is well-deﬁned up to
multiplication by a positive real number. For the purposes of deﬁning our canonical set, we
can choose allti to be the same.
Very often, the cells of the decomposition are all ideal tetrahedra, but other polyhedra
can occur. For many applications, including the use in this paper, we need a subdivision
of M into ideal tetrahedra only. It is well known that every cusped 3–manifold has a
decomposition into ideal tetrahedra, but one often needs more than a purely topological
structure on the tetrahedra. The Epstein–Penner decomposition, coming as it does with
a geometric structure, provides all of the nice geometric properties one could want. So,
in the cases when the cells of the decomposition are not themselves tetrahedra, we would
like to further subdivide the polyhedra into tetrahedra. However, there is no canonical
way to subdivide, and it is not even clear if one can subdivide the various polyhedra in
a consistent way, so that the triangulations induced on the faces of the polyhedra match
when the polyhedra are glued to each other. In particular, it is still unknown whether every
cusped hyperbolic 3–manifold admits ageometric triangulation (that is, a subdivision into
positive volume ideal hyperbolic tetrahedra), either constructed by further subdividing the
Epstein–Penner decomposition or otherwise.
However, one can use the Epstein–Penner decomposition to produce an ideal triangulation
by subdividing the ideal polyhedra, if we also allow ﬂat tetrahedra inserted between faces of
the polyhedra to bridge between incompatible triangulations of those faces. Such an ideal
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 33
triangulation has anatural semi-angle structure(see Remark 6.6), and so by Theorem 1.5
all of these triangulations are 1–eﬃcient.
To describe our triangulations more precisely, we use the same notation as in [HRS12].
Deﬁnition 6.1.In this paper, the termpolyhedron will mean a combinatorial object ob-
tained by removing all of the vertices from a 3-cell with a given combinatorial cell decom-
position of its boundary. We further require that this can be realised as a positive volume
convex ideal polyhedron in hyperbolic 3-spaceH3.
Deﬁnition 6.2.An (ideal) polygonal pillow or n-gonal pillow is a combinatorial object
obtained by removing all of the vertices from a 3-cell with a combinatorial cell decomposition
of its boundary that has precisely two faces. The two faces are copies of ann-gon identiﬁed
along corresponding edges.
Deﬁnition 6.3.Suppose that P is a cellulation of a 3-manifold consisting of polyhedra
and polygonal pillows with the property that polyhedra are glued to either polyhedra or
polygonal pillows, but polygonal pillows are only glued to polyhedra. Then we call P a
polyhedron and polygonal pillow cellulation, or for short, aPPP-cellulation.
Deﬁnition 6.4.Let t be a triangulation of a polygon. Adiagonal ﬂipmove changest as
follows. First we remove an internal edge oft, producing a four sided polygon, one of whose
diagonals is the removed edge. Second, we add in the other diagonal, cutting the polygon
into two triangles and giving a new triangulation of the polygon.
Deﬁnition 6.5.Let Q be a polygonal pillow, with triangulationst− and t+ given on its
two polygonal facesQ− and Q+. By a layered triangulation ofQ, bridging betweent− and
t+, we mean a triangulation produced as follows. We are given a sequence of diagonal ﬂips
which convertt− into t+. This gives a sequence of triangulationst− =L1,L 2,...,L k =t+,
where consecutive triangulations are related by a diagonal ﬂip. Starting fromQ− with the
triangulation t− = L1, we glue a tetrahedron onto the triangulationL1 so that two of its
faces cover the faces ofL1 involved in the ﬁrst diagonal ﬂip. The other two faces together
with the rest ofL1 produce the triangulationL2. We continue in this fashion, adding one
tetrahedron for each diagonal ﬂip until we reachLk =t+, which we identify withQ+.
Our class of triangulations XEP
M of M consists of triangulations that are subdivisions
of PPP-cellulations. Our PPP-cellulation will have polyhedra being the polyhedra of the
Epstein-Penner decomposition. It also has a polygonal pillow inserted between all pairs of
identiﬁed faces that have at least 4 sides. We will form our triangulations by ﬁrst sub-
dividing the ideal hyperbolic polyhedra into positive volume ideal hyperbolic tetrahedra.
Secondly, for each polygonal pillow, we insert any layered triangulation that bridges between
the induced triangulations of the two boundary polygons of the polyhedra to each side.
Remark 6.6. Any triangulation produced in the way described above has anatural semi–
angle structure. This comes from the shapes of the tetrahedra as ideal hyperbolic tetrahedra.
The dihedral angles of the positive volume ideal hyperbolic tetrahedra, together with 0 and
π angles for the ﬂat tetrahedra in the layered triangulations in the polygonal pillows satisfy
all of the rules for a generalised angle structure, and all angles are in[0,π ].
34 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
The natural semi–angle structure together with Theorem 1.5 show that each triangulation
in our class is 1-eﬃcient. However, we also need to show that our class is connected under
2–3, 3–2, 0–2 and 2–0 moves, and for this we will need some extra machinery. The main tool
