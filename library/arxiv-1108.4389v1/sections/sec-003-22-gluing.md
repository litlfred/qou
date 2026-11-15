---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-003-22-gluing
section_title: "Gluing"
section_number: 2.2
pages: 11-13
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 1.0
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:geomglue label="sec:geomglue"}

Any 3-manifold $M$ with a combination of geodesic and cusp boundaries can be constructed from a collection of ideal tetrahedra $\{\Delta_i\}_{i=1}^N$, by gluing together their faces one pair at a time. Topologically, the geodesic boundary of $M$ comes from faces of tetrahedra that remain unglued. The torus or annular cusps of $M$, however, arise from assembling collections of small truncated-vertex triangles, as in Figure [1](#fig:gluingtet){reference-type="ref" reference="fig:gluingtet"}. Geometrically, it is clear that the geodesic boundary of $M$ will be endowed with a hyperbolic metric, since all the faces of ideal tetrahedra are geodesic, hyperbolic surfaces. Similarly, the cusp boundaries become resolved into Euclidean tori or annuli, triangulated by the Euclidean truncated vertices.

![Triangulations by Euclidean vertex triangles of (a) an annular cusp attached to a geodesic boundary, and (b) a torus cusp.](gluingtetC){#fig:gluingtet width="5in"}

In order for the hyperbolic metric on $M$ resulting from such a gluing to be smooth, one must impose that the total dihedral angle around every internal edge of the triangulation is $2\pi$, and that the hyperbolic torsion vanishes. In other words, for every internal edge $I_j$, the sum of complex edge parameters $Z_i,Z_i',Z_i''$ meeting this edge must equal exactly $2\pi i$. This could be written formally as

$$C_I \equiv \sum_{i=1}^N \Big[n(I,i)Z_i+n'(I,i) Z_i'+n''(I,i)Z_i''\Big] = 2\pi i\qquad (\forall\;\text{internal edges $I$})\,, \label{defCj}$$

where $n(I,i) \in \{0,1,2\}$ is the number of times the edge $I$ in $M$ coincides with an edge parameter $Z_i$ of tetrahedron $\Delta_i$ in the triangulation $M= \bigcup_{i=1}^N\Delta_i$.

Given individual phase spaces $\mathcal{P}_{\partial\Delta_i}$ for each tetrahedron $\Delta_i$, one can construct a product phase space $\mathcal{P}_{\{\partial\Delta_i\}}=\prod_{i=1}^N \mathcal{P}_{\partial\Delta_i}$ with a product symplectic structure. The edge coordinates in this space obey a Poisson algebra

$$\{Z_i,Z_j'\} = \{Z_i',Z_j''\}= \{Z_i'',Z_j\} = \hbar\,\delta_{ij}\,,$$

with all other brackets vanishing. It is a wonderful fact that in the product phase space all the "gluing constraints" $C_I$ defined in [\[defCj\]](#defCj){reference-type="eqref" reference="defCj"} commute with each other [@NZ]. It turns out that the remaining linear combinations of edge coordinates in $\mathcal{P}_{\{\partial\Delta_i\}}$ that commute with (but are independent of) the gluing constraints $C_I$ precisely parametrize the remaining boundary phase space of the glued 3-manifold $M$. This includes both geodesic and cusp-like boundary components, and we will momentarily give explicit examples of both.

Formally, the fact that all gluing constraints $C_I$ commute with each other and with the coordinates of flat connections on $\partial M$ means that $\mathcal{P}_{\partial M}$ can be obtained as the symplectic quotient of the product phase space $\mathcal{P}_{\{\partial\Delta_i\}}$ by the flows of the $C_I$ viewed as *moment maps* [@Dimofte-QRS],

$$\mathcal{P}_{\partial M}\,=\, \bigg(\prod_{i=1}^N \mathcal{P}_{\partial\Delta_i}\bigg)\Big/\!\!\!\Big/\big(C_I=2\pi i\,\big) \,,$$

where $I$ runs over all internal edges. The individual Lagrangian submanifolds $\mathcal{L}_{\Delta_i}$ can also be carried through this symplectic reduction. One forms a product Lagrangian $\mathcal{L}_{\{\Delta_i\}}=\prod_{i=1}^N\mathcal{L}_{\Delta_i}\;\subset\;\mathcal{P}_{\{\partial\Delta_i\}}$ cut out by $N$ polynomial equations $z_i+z_i'{}^{-1}-1=0$; then algebraically eliminates all variables in these equations that do not commute with the $C_I$ (projecting $\mathcal{L}_{\{\Delta_i\}}$ along the flows of the $C_I$); and sets $C_I=2\pi i$ in the equations that remain (intersecting the projection with the moment map conditions). This leads to a Lagrangian submanifold $\mathcal{L}_M\,\subset\,\mathcal{P}_{\partial M}$. Subject to several technical caveats discussed in [@Dimofte-QRS], it is precisely the desired set of flat connections on $M$.
