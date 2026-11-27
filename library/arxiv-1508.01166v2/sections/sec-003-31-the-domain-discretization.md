---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-003-31-the-domain-discretization
section_title: "The domain discretization"
section_number: 3.1
pages: 7-8
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
Let Ω be the physical domain of dimension N = 2 or 3. The domain Ω is
approximated by the simplicial complex K. Following the notation in [15, 17], a
domain simplex σ of dimension k is denoted by σk∈ K. A k-simplexσk is de-
ﬁned by the nodes forming it asσk = [v0,..., vk], where the subscripts represent the
nodes indices. The order of the nodes deﬁning a simplex implies its orientation.
The top dimensional simplicesσN are assumed to have been oriented consistently,
whereas the orientation of the lower dimensional simplices is arbitrary. An exam-
ple 2D mesh is shown in Fig. 1. The number of k-simplices in the discrete mesh
is denoted by Nk. Therefore for the mesh in Fig. 1, N2 = 8, N1 = 15, and N0 = 8.
Associated with the primal simplicial complex K is a dual complex ⋆K con-
sisting of cells. For a primal k-simplexσk∈ K, its dual is an (N− k)-cell denoted
by⋆σk∈ ⋆K. The dual mesh considered here is the circumcentric dual, shown
in Fig. 1 in red color. For a 2D mesh, the dual of a triangle is its circumcenter,
the dual of a primal edge is the dual edge connecting the circumcenters of the
two triangles sharing the primal edge, and the dual of a primal node is the 2-cell
(polygon) formed by the duals of the edges connected to this primal node. For
the case of a triangular mesh representing a curved surface, the dual edges can be
kinked lines and the dual cells can be non planar. In 2D, the positive orientation of
both primal 2-simplices (triangles) and dual 2-cells (polygons) is assumed to be
7
counterclockwise. The orientation of the primal 1-simplices (edges) is arbitrary,
however their orientations induce the dual edges orientations. The dual edges can
be oriented simply by rotating the primal edge orientation 90 degrees along the
triangles orientation (i.e. counterclockwise), as shown in Fig. 1. In the 3D case,
the orientations of the primal edges and faces (i.e. triangles) are arbitrary, how-
ever, their orientations induce the orientations of their duals through the right hand
rule.
The simplicial meshes considered here are Delaunay meshes, with an extra
requirement only for the N-simplices with a face on ∂Ω, the domain boundary.
Previous investigation [20] showed that in order to correctly represent the discrete
Hodge star operator, the mesh interior N-simplices have to be pairwise Delaunay,
while the N-simplicial elements with a face on the domain boundary have to be
one-sided (i.e., with respect to the face of the N-simplex on the domain boundary,
both the simplex circumcenter and its apex have to be on the same side). Such
Delaunay meshes can easily be generated using commercial or open source mesh
generators.
