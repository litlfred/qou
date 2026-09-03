---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-019-triangulated-3-manifolds-with-defects
section_title: "Triangulated 3-manifolds with defects"
section_number: null
pages: 28-29
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
We consider a compact oriented 3d PL manifoldM with (possibly empty) boundary∂M. Defect structures
are assigned to a compact oriented embedded 2d PL submanifoldD⊂M with boundary∂D⊂∂M that is a
finite sum of circles. The submanifoldD is equipped with a (finite, possibly empty) embedded PL graph
D1 with vertex setD0 such thatD1∩∂D⊂D0 contains only univalent vertices. Connected components of
M\D are calledregions of M, connected components ofD defect surfaces, connected components of
D\D1 defect areas, connected components ofD1\D0 defect lines, elements ofD0\∂D defect vertices.
We equip each defect line and defect surface with an orientation. In pictures we indicate the orientation of a
defect surface by a positive normal vector to the surface and the orientation of a defect line by an arrow on
the line. Regions and defect areas, lines and vertices are labeled with categorical data as follows, see Figure 2
for an illustration:
• Regions ofM are assigned spherical fusion categories.
• Each oriented defect area is assigned a pair(M,θ ) of a (C,D)-bimodule categoryM and a (C,D)-
bimodule traceθ onM, whereC andD are the spherical fusion categories for the regions at the tip
and the tail of the surface’s normal vector.
Reversing the orientation of a defect area amounts to replacingM by the opposite bimodule category
M# from Example 1.6.
• Each oriented defect line is assigned a(C,D)-bimodule functorF :M→N , whereM andN are the
(C,D)-bimodule categories to the left and to the right of the defect line, viewed in the direction of its
orientation and fromC.
Reversing the orientation of a defect line corresponds to replacingF :M→N by its left adjoint
Fl :N→M . Reversing the orientation of the adjacent defect areas and the orientation of the line
corresponds to replacingM,N byM#,N # and F byF # :M#→N # from Example 1.10, 7.
• A defect vertex whose incident defect lines are labeled by(C,D)-bimodule functors is assigned a cyclic
equivalence class of(C,D)-bimodule natural transformations between them, whose sources and targets
are determined by the orientation and the cyclic ordering of the incident defect lines.
Defect areas between two regions labeled both withC may be labeled withC as a bimodule category over itself
and with its trace as a bimodule trace. Such defect areas are calledtrivial defect areas. Similarly, a defect
line between two defect areas labeled with(M,θ ) may be labeled with the identity functorF = idM :M→M
as a (C,D)-bimodule functor. Such defect lines are calledtrivial defect lines. A defect vertex labeled with
idF or with a counitϵF, ϵ′F or unitηF,η′F of the adjunctionFl⊢F is called atrivial defect vertex.
A compact oriented 3d PL manifoldM, possibly with boundary, together with defectsD0⊂D1⊂D is called
a defect 3-manifold. A defect 3-manifold together with a labeling of the defects with categorical data is
called a3-manifold with defect data.
To define a state sum model for a 3-manifold with defect data, we require a triangulation ofM. It must be
sufficiently refined to resolve all defect surfaces and must intersect the defect surfaces generically.
Definition 4.1. LetM be a defect 3-manifold andT a triangulation ofM.
1. A triangle inT is calledtransversal, if
• each of its sides contains at most one point on a defect surface,
• its intersection with each defect surface is empty or a line with endpoints on its sides,
28
and generic if
• none of its vertices is on a defect surface,
• none of its sides intersects a defect line,
• it does not contain a defect vertex.
2. A tetrahedron inT is transversal, if all of its faces are transversal and its intersection with each de-
fect surface is either empty or a polygon with vertices on its edges. It is generic, if all its faces are generic.
3. The triangulationT is transversal or generic if all of its tetrahedra are transversal or generic.
It follows directly that a generic transversal tetrahedron either intersects a single defect surface in three edges
incident at a common vertex, as in Figure 2 (a), intersects a defect surface in two pairs of opposite edges, as
in Figure 2 (b), or does not intersect any defect surface at all.
Any transversal triangulation can be deformed into a generic one by slightly perturbing the defect surfaces
and the defect graphs. By taking derived subdivisions, see Rourke and Sanderson [RS, Ch. 2], and perturbing
defect surfaces and defect graphs one can transform any triangulation into one that is both transversal and
generic. In particular, one can achieve that the defect manifold is a subcomplex of a first derived subdivision.
We orient the edges of a generic transversal triangulation in such a way that
(i) edges in each triangle do not form a cycle,
(ii) in each tetrahedron, the edges that intersect a defect surface are oriented parallel to its positive normal
vector.
This does not restrict generality. Condition (i) can be achieved by numbering the vertices of the triangulation
and orienting each edge in such a way that it points from the vertex with the smaller number to the vertex
with the bigger number. This is possible because any PL triangulation is determined by an underlying
combinatorial simplicial complex, see for instance [RS, Th. 2.11].
Given a generic transversal triangulation that satisfies (i), reverse the orientation of each edge that intersects
a defect surface and is oriented against its positive normal vector. Each triangle that intersects a defect
surface intersects it in exactly two edges. After this orientation reversal these two edges are either both
incoming or outgoing at a common vertex and hence cannot be part of a cycle. The resulting triangulation
satisfies (i) and (ii).
A defect 3-manifold together with an oriented triangulation is called atriangulated defect 3-manifold. A
3-manifold with defect data together with an oriented triangulation is called atriangulated 3-manifold
with defect data. They are calledtransversal or generic if the triangulation is transversal or generic.
