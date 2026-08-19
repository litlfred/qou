---
doc_id: angled-survey
doc_title: "Contemporary Mathematics From angled triangulations to hyperbolic structures"
section_id: sec-008-14-acknowledgements-the-proof-of-theorem-12-was
section_title: "Acknowledgements. The proof of Theorem 1.2 was developed while"
section_number: 1.4
pages: 4-6
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "Contemporary Mathematics From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on"
---
the two authors were preparing to give a mini-course at Osaka University in Jan-
uary 2006. This argument was then tested and reﬁned in front of three workshop
audiences containing many graduate students: at Osaka University in 2006, at Zhe-
jiang University in 2007, and at Columbia University in 2009. We thank all the
participants of those workshops for their suggestions. We are also grateful to the
organizers of the Columbia workshop, “Interactions Between Hyperbolic Geometry,
Quantum Topology and Number Theory,” for their encouragement to write up this
material for the workshop proceedings. Finally, this paper beneﬁted from a num-
ber of conversations with Marc Culler, Feng Luo, Igor Rivin, Makoto Sakuma, and
Louis Theran.
2. Gluing equations
For the length of this paper,M will typically denote a compact, connected,
orientable 3–manifold whose boundary consists of tori. For example, such a mani-
fold can be obtained fromS
3 by removing an open tubular neighborhood of a knot
or link. Anideal triangulationτ is a subdivision ofM/integerdivide∂Minto ideal tetrahedra,
glued in pairs along their faces. One way to recover the compact manifoldM is
to truncate all the vertices of the tetrahedra: then, the triangles created by the
truncation will ﬁt together to tile∂M.
As discussed in the Introduction, our eventual goal is to ﬁnd a complete hy-
perbolic metric onM by gluing together metric tetrahedra. The metric models for
the tetrahedra inM come from ideal tetrahedra inH
3:
Definition 2.1. A hyperbolic ideal tetrahedronT is the convex hull inH3 of
four distinct points on∂H3. The four points on∂H3 are calledideal verticesof T,
and are not part of the tetrahedron. The tetrahedronT is called degenerate if it
lies in a single plane, andnon-degenerate otherwise.
Recall that an isometry ofH3 is completely determined by its action on three
points on ∂H3. Thus we may assume, for concreteness, that three vertices ofT
lie at 0,1,∞ in the upper half-space model. IfT is non-degenerate, we may also
162
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES 5
α
α
γ
γ
β
β
01
∞
z
Figure 1. Left: the shape of an ideal tetrahedron is deﬁned by
three dihedral angles. Right: the gluing of tetrahedra, seen from
an ideal vertex.
assume that the fourth vertex lies atz ∈ C,w i t hI m (z) > 0. This number z ∈ C
determines T up to isometry.
Suppose we moveT by an orientation–preserving isometry ofH3, so that three
vertices again lie at 0,1,∞, the fourth vertex again lies in the upper half-plane,
and edgee is mapped to the edge 0∞. Then the fourth vertex ofT will be sent to
one of
(2.1) z, z ′= z −1
z or z′′= 1
1−z.
The corresponding numberz, z′,o rz′′is called theshape parameterof e. Notice
that opposite edges ofT have the same shape parameter, and thatzz′z′′= −1.
The arguments
argz> 0, argz′> 0, argz′′> 0
represent the dihedral angles of T, or equivalently the angles of the Euclidean
triangle with vertices 0,1,z. If one of the vertices ofT is truncated by a horosphere,
the intersection will be a Euclidean triangle in precisely this similarity class. This
Euclidean triangle of intersection betweenT and a horosphere is called aboundary
triangle of T. See Figure 1, left.
The tiling of∂M by boundary triangles of the tetrahedra provides a way to
understand what conditions are required to glue the tetrahedra coherently.
Definition 2.2. Let C be an oriented surface with a speciﬁed triangulation
(for example, a boundary torus ofM with the tessellation by boundary triangles).
A segment in C is an embedded arc in one triangle, which is disjoint from the
vertices of C, and whose endpoints lie in distinct edges ofC.A normal closed
curve σ ⊂ C is an immersed closed curve that is transverse to the edges ofC,s u c h
that the intersection betweenσ and a triangle is a union of segments.
Definition 2.3. Let τ be an ideal triangulation ofM, and letC be one torus
component of ∂M.T h e nτ induces a tessellation ofC by boundary triangles. If
each tetrahedron of τ is assigned a hyperbolic shape, then every corner of each
boundary triangle can be labeled with the corresponding shape parameter.
Let σ be an oriented normal closed curve inC.T h e ne v e r y s e g m e n to fσ in
a triangle of C cuts oﬀ a single vertex of a triangle, labeled with a single shape
163
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
