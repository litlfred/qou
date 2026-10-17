---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-005-3-from-planar-diagrams-to-ideal-triangulations
section_title: "From planar diagrams to ideal triangulations"
section_number: 3
pages: 9-9
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
toc_source: outline
text_source: latex
latex_prose_ratio: 0.691
latex_coverage_ratio: 0.986
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
[]{#sec.octa label="sec.octa"}

In this section we recall a well-known connection between planar projections of (hyperbolic) knots and their ideal triangulations. The history of the subject predates quantum topology, and the sought algorithm takes as input a planar projection $D$ of a knot $K$, produces as an intermediate stage an octahedral cell decomposition of its complement minus two points, and eventually produces an ideal triangulation of its complement $S^3 \setminus K$. This algorithm due to Thurston appears in the code of `SnapPy` in the original version due to Weeks [@snappy]. It is described in detail in [@Weeks], and forms the core method of `SnapPy` for computing numerically (or exactly) the complete hyperbolic structure of a hyperbolic knot (or more generally, link) complement.

Years after its discovery and its use in hyperbolic geometry, it was realized that the above algorithm has applications to quantum topology, and more precisely to the volume conjecture. The reason being obvious syntactical similarities between the octahedral decomposition of a planar projection of a knot and the state-sum formula for its Kashaev invariant, where the shapes of 4 tetrahedra around a crossing of the knot match with the quantum factorials in Kashaev's $R$-matrix of his invariant. This connection was discussed by D. Thurston in relation to the Kashaev invariant and its asymptotics [@Thu99], and later by Yokota [@Yokota02], see also [@GL:asy Sec.8.2].

The algorithm consists of two steps $$\label{2steps}
\mathring{D}\mathrel{\leadsto}(\mathcal O_D,s) \mathrel{\leadsto}\mathcal T_{\mathring{D}}$$ which we next discuss in detail.
