---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
State sum models with defects
based on spherical fusion categories
Catherine Meusburger
Department Mathematik
Friedrich-Alexander-Universität Erlangen-Nürnberg
Cauerstraße 11, 91058 Erlangen, Germany
Email: catherine.meusburger@math.uni-erlangen.de
May 13, 2022
Abstract
We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface,
line and point defects. Surface defects are oriented embedded 2d PL submanifolds and are labeled with
bimodule categories over spherical fusion categories with bimodule traces. Line and point defects form
directed graphs on these surfaces and labeled with bimodule functors and bimodule natural transformations.
The state sum is based on generalised 6j symbols that encode the coherence isomorphisms of the defect
data. We prove the triangulation independence of the state sum and show that it can be computed in
terms of polygon diagrams that satisfy the cutting and gluing identities for polygon presentations of
oriented surfaces. By computing state sums with defect surfaces, we show that they detect the genus of
a defect surface and are sensitive to its embedding. We show that defect lines on defect surfaces with
trivial defect data define ribbon invariants for the centre of the underlying spherical fusion category.
Introduction
Turaev-Viro-Barrett-Westbury state sums were introduced in [TV92, BW96] and define invariants of 3-
manifolds and topological quantum field theories (TQFTs). They are also of interest from the physics
perspective, since they arise in the quantisation of Chern-Simons and BF theories and have applications in
topological quantum computing. In particular, it was established by Balsam and Kirillov in [BK12, Kr11]
that they are closely related to two condensed matter physics models for topological quantum computers,
namely Kitaev’s quantum double model [Ki03] and Levin-Wen models [LW05].
Introducing defects in these models is natural in this physics context. Early work on specific line and point
defects in Turaev-Viro-Barrett-Westbury state sums by Karowski and Schrader [KS93] and by Barrett et
al. [BMG07] was motivated by the wish to introduce observables. In models from condensed matter physics
it is also natural to study codimension one defects as domain walls. Introducing defects in these models
amounts to labeling distinguished submanifolds with higher categorical data that relates the categorical data
outside the defects. The general algebraic data for defects of all codimensions in Levin-Wen models was
identified by Kitaev and Kong [KK12] and coincides largely with the defect data in this article.
From the mathematics perspective the introduction of defects in Turaev-Viro-Barrett-Westbury state sums is
of interest as a concrete model for defect TQFTs, in which the usual cobordism category is replaced with a
decorated cobordism category that involves distinguished submanifolds of various codimensions. A general
formalism and concrete examples of defect TQFTs were developed by Carqueville et al. [CRS18, CRS19,
CMS20]. However, these are not constructed as state sum models, but from a cobordism category.
State sum models that extend Turaev-Viro TQFTs and involve defect lines decorated by the centre of a
spherical fusion category were defined by Turaev and Virelizier [TV10, TV17] and by Balsam and Kirillov
in [KB10, B10]. More recently, Fuchs et al. [FSS19] gave a state sum construction for a modular functor
with bimodule categories over finite tensor categories and Lee and Yetter [LY20] defined a triangulation
independent state sum with defect surfaces. However, the categorical defect data in [LY20] differs from the
data in the other publications and should be thought of as additional structure, as pointed out in [LY20].
Thus, a Turaev-Viro-Barrett-Westbury style state sum model with defects of all codimensions labeled by
bimodule categories, functors and natural transformations is still missing. In this article we define such a
state sum model and prove its triangulation independence. The model generalises the usual Turaev-Viro-
Barrett-Westbury state sum, which is obtained by choosing trivial defect data.
1
arXiv:2205.06874v2  [math.QA]  15 Jun 2023
State sum model with defects
We consider three-dimensional PL manifolds M, possibly with boundary. Defect surfaces are embedded
oriented PL surfaces with compact boundary contained in ∂M. Defect lines and points form directed graphs
on these surfaces, whose edges may end on ∂M.
Regions outside the defects are assigned spherical fusion categories. Oriented defect surfaces are assigned
finite semisimple bimodule categories with bimodule traces, oriented defect lines bimodule functors and defect
vertices bimodule natural transformations.
Bimodule traces were introduced by Schaumann in [S13, S15], where it was shown that for fixed spherical fusion
categories, bimodule categories with bimodule traces, bimodule functors and bimodule natural transformations
form a pivotal 2-category. The restriction to finite semisimple bimodule categories with bimodule traces
is motivated by the fact that semisimplicity, summation over simple objects and the existence of traces
are essential ingredients in the usual Turaev-Viro-Barrett-Westbury state sum. Although the latter can be
generalised to pivotal fusion categories, see [TV10, TV17], we stick with the original formulation in terms of
spherical fusion categories and 6j symbols and hence require bimodule traces.
The state sum is based on a triangulation of M, which is required at first to intersect defect surfaces, defect
lines and defect vertices transversally and generically. This means each tetrahedron can intersect at most one
defect surface, either in a triangle, whose vertices lie on three edges incident at a common vertex, or in a
quadrilateral, whose vertices lie on two pairs of opposite edges. Defect vertices must be in the interior of
tetrahedra and defect edges must intersect their faces transversally in the interior.
To define the state sum, one labels the edges of the triangulation with simple objects, either in a spherical
fusion category, if the edge does not intersect any defect surface, or in the bimodule category at its intersection
point with a defect surface. This assigns to each labeled tetrahedron a generalised 6j symbol that is the 6j
symbol for a spherical fusion category for a tetrahedron without defects. The state sum is then obtained by
taking the product of the generalised 6j symbols of all tetrahedra and the dimensions of the simple objects at
the internal edges, summing over all assignments of simple objects and over bases of the morphism spaces for
its triangles and rescaling by the dimensions of the spherical fusion categories at the vertices.
Generalised 6j symbols
The generalised 6j symbol for a tetrahedron depends on the simple objects assigned to its edges and the
bimodule functors and natural transformation in its interior. By combining the latter with the morphisms
assigned to its boundary triangles one obtains an endomorphism of a simple object in a bimodule category.
The generalised 6j symbol is the trace of this endomorphism. It generalises the usual 6j symbols or F-matrices
for spherical fusion categories and has a similar algebraic and geometric interpretation.
Just as the 6j symbols for a spherical fusion category encode its associator on its simple objects, the 6j symbols
for a bimodule category encode the natural isomorphisms that describe its bimodule category structure. If a
tetrahedron also contains defect lines or defect vertices, these coherence isomorphisms are combined with
the coherence isomorphisms for the bimodule functors at the defect lines and with the bimodule natural
transformations at the defect points.
The 6j symbols for a spherical fusion category relate the geometry of a tetrahedron to the diagrammatic
calculus for a spherical fusion category. Their diagrams are obtained by taking the dual graph on the surface
of the tetrahedron and labeling its edges and vertices with objects and morphisms in a spherical fusion
category. The properties of a spherical fusion category imply that it has the symmetries of a tetrahedron.
Similarly, generalised 6j symbols for defect tetrahedra relate the geometry of a tetrahedron with defects to a
diagrammatic calculus for bimodule categories, functors and natural transformations. Their diagrams are
obtained by projecting the duals of those edges and triangles that do not intersect the defect surface on the
defect surface. This yields a polygon with lines and vertices in its interior labeled by bimodule functors and
natural transformations as well as objects and morphisms in spherical fusion categories. The diagrams also
involve crossings labeled by coherence isomorphisms of bimodule categories and bimodule functors.
We develop a diagrammatic calculus for such polygon diagrams and define their evaluation. For a diagram
obtained from a tetrahedron with defects, this is the generalised 6j symbol of the tetrahedron. As the presence
of defects reduces the symmetries of a tetrahedron, generalised 6j symbols exhibit fewer symmetries than
the 6j symbols of a spherical fusion category. Nevertheless, the associated polygon diagrams can be cut and
glued by summing over simple objects and bases of the morphism spaces at their boundary.
2
Theorem 1: (Theorem 3.1) Evaluations of polygon diagrams are invariant under rotations of the polygon.
They satisfy the usual cutting and gluing identities for polygon presentations of oriented surfaces and an
