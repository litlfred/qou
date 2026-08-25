---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-006-22-gluing
section_title: "Gluing"
section_number: 2.2
pages: 11-13
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
Any 3-manifold M with a combination of geodesic and cusp boundaries can be constructed
from a collection of ideal tetrahedra {∆i}N
i=1, by gluing together their faces one pair at a
time. Topologically, the geodesic boundary of M comes from faces of tetrahedra that remain
– 10 –
unglued. The torus or annular cusps of M, however, arise from assembling collections of small
truncated-vertex triangles, as in Figure7. Geometrically, it is clear that the geodesic boundary
of M will be endowed with a hyperbolic metric, since all the faces of ideal tetrahedra are
geodesic, hyperbolic surfaces. Similarly, the cusp boundaries become resolved into Euclidean
tori or annuli, triangulated by the Euclidean truncated vertices.
a) b)
Figure 7: Triangulations by Euclidean vertex triangles of (a) an annular cusp attached to a geodesic
boundary, and (b) a torus cusp.
In order for the hyperbolic metric on M resulting from such a gluing to be smooth, one
must impose that the total dihedral angle around every internal edge of the triangulation is
2π, and that the hyperbolic torsion vanishes. In other words, for every internal edge Ij, the
sum of complex edge parameters Zi,Z′
i,Z′′
i meeting this edge must equal exactly 2 πi. This
could be written formally as
CI≡
N∑
i=1
[
n(I,i )Zi +n′(I,i )Z′
i +n′′(I,i )Z′′
i
]
= 2πi (∀ internal edges I), (2.12)
where n(I,i )∈ {0, 1, 2} is the number of times the edge I in M coincides with an edge
parameter Zi of tetrahedron ∆i in the triangulation M =⋃N
i=1 ∆i.
Given individual phase spaces P∂∆i for each tetrahedron ∆ i,
I
z1
z3
z
￿
2
Figure 8: Illustration
of gluing at an internal
edge, with CI = Z1 +
Z′
2 +Z3.
one can construct a product phase space P{∂∆i} =∏N
i=1P∂∆i with
a product symplectic structure. The edge coordinates in this space
obey a Poisson algebra
{Zi,Z′
j} ={Z′
i,Z′′
j} ={Z′′
i,Zj} = ℏδij, (2.13)
with all other brackets vanishing. It is a wonderful fact that in the
product phase space all the “gluing constraints” CI deﬁned in (2.12)
commute with each other [14]. It turns out that the remaining linear
combinations of edge coordinates inP{∂∆i} that commute with (but
are independent of) the gluing constraints CI precisely parametrize
the remaining boundary phase space of the glued 3-manifoldM. This
includes both geodesic and cusp-like boundary components, and we
will momentarily give explicit examples of both.
– 11 –
Formally, the fact that all gluing constraints CI commute with each other and with the
coordinates of ﬂat connections on ∂M means that P∂M can be obtained as the symplectic
quotient of the product phase space P{∂∆i} by the ﬂows of the CI viewed as moment maps
[12],
P∂M =
( N∏
i=1
P∂∆i
)/ /(
CI = 2πi
)
, (2.14)
where I runs over all internal edges. The individual Lagrangian submanifolds L∆i can also
be carried through this symplectic reduction. One forms a product Lagrangian L{∆i} =∏N
i=1L∆i ⊂ P{∂∆i} cut out by N polynomial equations zi +z′
i
−1− 1 = 0; then algebraically
eliminates all variables in these equations that do not commute with the CI (projecting
L{∆i} along the ﬂows of theCI); and setsCI = 2πi in the equations that remain (intersecting
the projection with the moment map conditions). This leads to a Lagrangian submanifold
LM ⊂P ∂M . Subject to several technical caveats discussed in [ 12], it is precisely the desired
set of ﬂat connections on M.
