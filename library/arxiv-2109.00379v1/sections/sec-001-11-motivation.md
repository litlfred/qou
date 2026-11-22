---
doc_id: arxiv-2109.00379v1
doc_title: "TWISTED NEUMANN–ZAGIER MATRICES"
section_id: sec-001-11-motivation
section_title: "Motivation"
section_number: 1.1
pages: 1-2
source_pdf: 2109.00379v1.pdf
source_sha256: f0c9bd89312a761c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.908
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
---
[]{#sub.motivation label="sub.motivation"}

Ideal triangulations of 3-manifolds with torus boundary components were introduced by Thurston [@Thurston] as a convenient way to describe and effectively compute [@snappy] complete hyperbolic structures on 3-manifolds. To do so, one assigns a complex number different from 0 or 1 to each tetrahedron and a polynomial equation around each edge of the triangulation. These so-called gluing equations have special shape that can be described by two matrices $\mathbf{A}$ and $\mathbf{B}$ (with rows and columns indexed by the edges and by the tetrahedra, respectively) whose entries describe the number of times (but *not* the order by which) tetrahedra wind around an edge. One of the main discoveries of Neumann--Zagier is that the matrix $(\mathbf{A} | \mathbf{B})$ becomes, after some minor modifications, the upper part of a symplectic matrix with integer entries [@NZ]. The symplectic property of the NZ matrices and of the corresponding gluing equations define a linear symplectic structure on a vector space whose quantization leads to a plethora of quantum invariants that include the loop invariants of Dimofte and the first author [@DG1; @DG2], the 3D-index in both the original formulation of Dimofte-Gaiotto-Gukov [@DGG1; @DGG2] as well as the state-integral formulation of Kashaev and the first author [@GK:meromorphic] and Kashaev--Luo--Vartanov state-integral [@KLV; @AGK:KLV]. All of those invariants are defined using the NZ matrices of a suitable ideal triangulation, and their topological invariance follows by proving that they are unchanged under Pachner 2--3 moves.

Our original motivation was to study the behavior of the loop invariants of [@DG1] under cyclic covers. Since the latter are defined in terms of NZ data of an ideal triangulation, we were led to study the behavior of the NZ matrices under cyclic covers. By elementary topology, each tetrahedron of an ideal triangulation lifts to $n$ tetrahedra in the $n$-fold cyclic cover, and lifting all the way to the infinite cyclic cover leads to the notion of NZ matrices which we can call *equivariant* or *twisted* (as is common in algebraic and geometric topology) or *$t$-deformed* (as is common in physics). We will use the term "twisted", and keep in mind that the variable $t$ below encodes topological information of cyclic covers.

Said differently, as the triangulation of the cyclic cover unfolds, so do its edges and the tetrahedra that wind around them. This is the content of the twisted NZ matrices. How can this elementary idea be nontrivial or interesting?

It turns out that the twisted NZ matrices have twisted symplectic properties which come from topology and using them one can give twisted versions of the above mentioned invariants, i.e., of the loop invariants [@DG1; @DG2], the 3D-index in [@DGG1; @DGG2] and [@GK:meromorphic] and KLV state-integral [@KLV; @AGK:KLV]. A key property of such a twisted invariant is that it determines the corresponding (untwisted) invariant of all cyclic covers. For example, the twisted 1-loop invariant of a knot complement defined below satisfies this property.

Our goal is to define the twisted NZ matrices, describe their properties and show how to compute them in terms of the methods developed by `SnapPy` [@snappy]. Having done so, we can use the twisted NZ matrices to define a twisted version of the 1-loop invariant, prove its topological invariance and conjecture that it equals to the adjoint twisted Alexander polynomial. It is interesting to note that the twisted 1-loop invariant depends only on the combinatorics of the NZ matrices of the infinite cyclic cover (which is abelian information) whereas the adjoint twisted Alexander polynomial depends on the complete hyperbolic structure given as a representation of the fundamental group.

Further applications of twisted NZ matrices will be given in forthcoming work.
