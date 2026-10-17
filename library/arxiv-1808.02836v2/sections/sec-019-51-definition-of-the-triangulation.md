---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-019-51-definition-of-the-triangulation
section_title: "Definition of the triangulation"
section_number: 5.1
pages: 28-29
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.991
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
[]{#sec:mit label="sec:mit"}

Monodromy ideal triangulations were studied in Lackenby [@Lackenby-canonical-2003] and Gueritaud [@Gueritaud-canonical-2006], and we refer the reader to these references for details.

The monodromy ideal triangulations all have the property that they are ideal triangulations for which all edges are of even degree and there is a single ideal vertex. As we are only interested in the case of hyperbolic 3-manifolds amongst once punctured torus bundles, we restrict to monodromy as a map $A \in SL(2,\mathbb{Z})$ having trace different from $0,\pm 1, \pm 2.$

Each tetrahedron in the monodromy ideal triangulation is *layered* on a once punctured triangulated torus with two ideal triangles. In particular, two sets of opposite edges of each tetrahedron are identified in pairs so that the top and bottom pairs of faces form such triangulated once punctured tori. Each tetrahedron induces a diagonal flip on the triangulation of the once punctured torus, and tracing the sequence of flips gives rise to a conjugate of $\pm A.$ Indeed, each flip corresponds to one of the standard transvection matrices $$R = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} 
\quad \text{and} \quad 
L = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix},$$ and hence one obtains a factorisation of a conjugate of $\pm A$ in terms of positive powers of $L$ and $R.$

A key property of these triangulations is that the normal quadrilateral discs are of two types---called *horizontal* and *vertical*. A horizontal quadrilateral has vertices on the two pairs of opposite edges which are glued together. A vertical quadrilateral has two vertices on such a pair of edges and two vertices on the two edges which are not glued together.

A crucial fact about normal surfaces in these triangulations is that the Euler characteristic is exactly the negative of the total number of horizontal quadrilaterals, see Lemma [\[lem:chiofS\]](#lem:chiofS){reference-type="ref" reference="lem:chiofS"}. In particular no normal triangle and no vertical quadrilateral contributes to the Euler characteristic.

In Sections [\[subsec:Reduction using coverings\]](#subsec:Reduction using coverings){reference-type="ref" reference="subsec:Reduction using coverings"} and [\[ssec:closedonesided\]](#ssec:closedonesided){reference-type="ref" reference="ssec:closedonesided"} we prove the following result, first stated in the introduction.

::: reptheorem
thm:torusbundles Monodromy ideal triangulations of once-punctured torus bundles are minimal.
:::
