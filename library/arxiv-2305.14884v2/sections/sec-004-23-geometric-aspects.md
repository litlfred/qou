---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-004-23-geometric-aspects
section_title: "Geometric aspects"
section_number: 2.3
pages: 8-9
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further choices)"
---
related to the choice of the shapes z in a Neumann–Zagier datum. Let us ﬁx an ideal
triangulation T . A solution z ∈ ( /BV \ {0, 1})N to the Neumann–Zagier equations gives rise,
via a developing map, to a representation ρz :π1(M) → PSL2( /BV ). For a detailed discussion,
see the appendix of [ 6]. However, not every representation ρ :π1(M) → PSL2( /BV ) is “seen”
by T , that is, is in the image of the map z → ρz. What’s more, if ρ is in the image of the
above map and we do a 2–3 Pachner move on the triangulation, it may n o longer be in the
image of the map corresponding to the new triangulation. The reaso n is that the shapes
of the two triangulations are related by a rational map, which may se nd a complex number
diﬀerent from 0 and 1 to 0, 1 or ∞. To phrase the problem diﬀerently, every two ideal
triangulations (each with at least two tetrahedra, as we will always a ssume) of a 3-manifold
with non-empty boundary are related by a sequence of 2–3 Pachne r moves [ 28, 32]. However,
it is not known that the set of ideal triangulations that see the discr ete faithful representation
ρgeom : π1(M) → PSL2( /BV ) is connected under 2–3 Pachner moves, nor is it known whether
the set of nondegenerate NZ data is connected under 2–3 Pachne r moves.
A solution to these issues was found in [ 11], and this was used to prove the topological
invariance of the 1-loop function, and was also used in [ 18] to prove the topological invariance
of the 3D-index. Let us recall the geometric details here. Every cu sped hyperbolic 3-
manifold M (complete, ﬁnite volume) has a canonical ideal cell decomposition wh ose cells
are 3-dimensional convex ideal polytopes given by Epstein–Penner [13]. It is easy to see that
every convex ideal polyhedron can be triangulated into ideal tetra hedra by connecting an
ideal vertex to all other ideal vertices (thus reducing the problem to the ideal cone of an
ideal polygon), and then triangulating further the ideal polygon int o ideal triangles. Doing
so, the triangulation of the common faces of the 3-dimensional con vex ideal polytopes may
not match, in which case one can pass from one triangulation of a poly gonal face to another
by adding ﬂat tetrahedra.
The question is whether every two such triangulations are related b y a sequence of 2–3
moves. This is a combinatorial problem of convex geometry, which we summarize below.
For a detailed discussion, the reader may consult the book [ 9] and references therein.
Fix a convex polytope P in /CA
d. One can consider the set of triangulations of P . When
d = 2, P is a polygon and it is known that every two triangulations are related b y a sequence
of ﬂips. For general d, ﬂips are replaced by geometric bistellar moves . When d ≥ 5, it is
known that the graph of triangulations (with edges given by geomet ric bistellar ﬂips) is
not connected, and has isolated vertices. For d = 3, it is not known whether the graph is
connected.
The situation is much better when one considers regular triangulations ofP . In that case,
the corresponding graph of regular triangulations is connected an d, in fact, it is the edge
set of the secondary polytope of P . When d = 3 and P is convex and in general position,
then the only geometric bistellar move is the 2–3 move where the adde d edge that appears
in the move is an edge that connects two vertices of P . When d = 3 and P is not in general
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 9
position, the same conclusion holds as long as one allows for tetrahed ra that are ﬂat, i.e., lie
on a 2-dimensional plane.
Returning to the Epstein-Penner ideal cell decomposition, let T EP denote a regular ideal
triangulations of the canonical ideal cell decomposition of M. (For a detailed discussion of
this set, see also [ 18, Sec.6]). The set {T EP} of regular ideal triangulations is connected
by 2–3 Pachner moves. Moreover, such triangulations see ρgeom since by the geometric
construction, the shapes are always nondegenerate, i.e., not equ al to 0 or 1 and in fact
always have nonnegative (though sometimes zero) imaginary part.
Finally, we need to show that det(Λ) is nonzero. This follows from the fact that
det(B) det(Λ) = det( −A +Bdiag(1/(1 −zj)) equals (up to multiplication by a monomial in
z andz′′) to the 1-loop invariant of [ 11, Sec.1.3]. The nonvanishing of the latter follows from
Thurston’s hyperbolic Dehn surgery theorem [ 34], which implies that ρgeom ∈X geom
M ∪PM is
an isolated smooth point of the geometric component X geom
M of the PSL 2( /BV )-character variety
of M, intersected with the locus PM of boundary-parabolic PSL 2( /BV )-representations, i.e.,
representations ρ satisfying tr(ρ(γ))2 = 4 for all peripheral elements γ ∈ π1(M). Since the
1-loop invariant is the determinant of the Hessian of the deﬁning NZ e quations of ρgeom, it
follows that the 1-loop invariant is nonzero.
