---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-032-11-examples
section_title: "Examples"
section_number: 11
pages: 21-22
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.864
latex_coverage_ratio: 0.926
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:Examples label="sec:Examples"} Let $M$ be the manifold `m009` from the SnapPy census [@SnapPy]. The census triangulation $\mathcal T$ of $M$ is shown in Figure [1](#fig:Trigm009){reference-type="ref" reference="fig:Trigm009"}.

<figure id="fig:Trigm009">

<figcaption>Census triangulation of <code>m009</code>. The signs on the faces indicate the obstruction cocycle <span class="math inline"><em>σ</em><sup>3</sup></span>.</figcaption>
</figure>

We refer to the three edges as *edge 1*, *edge 2*, and *edge 3*, according to the number of arrow heads. By inspecting the figure, one checks that there are four transitive edge sets: The non-degenerate edge set where all edges are nonzero, the edge-degenerate edge set where only edge 1 is zero, the edge-degenerate edge set where only edge 2 is zero, and the totally degenerate edge set (which we ignore, see Section [\[sec:TotallyDegenerate\]](#sec:TotallyDegenerate){reference-type="ref" reference="sec:TotallyDegenerate"}). The edge relation around edge 1 is given by $$\label{eq:EdgeOneRelation}
\frac{c_{23,0}}{c_{21,0}c_{13,0}}+\frac{c_{01,1}}{c_{03,1}c_{31,1}}+\frac{c_{10,0}}{c_{12,0}c_{20,0}}+\frac{c_{01,2}}{c_{03,2}c_{31,2}}+\frac{c_{23,1}}{c_{21,1}c_{13,1}}+\frac{c_{32,2}}{c_{30,2}c_{02,2}}=0$$ and the edge relation around edge 2 is given by $$\label{eq:EdgeTwoRelation}
\frac{c_{02,0}}{c_{01,0}c_{12,0}}+\frac{c_{30,1}}{c_{31,1}c_{10,1}}+\frac{c_{20,2}}{c_{23,2}c_{30,2}}+\frac{c_{12,1}}{c_{13,1}c_{32,1}}=0.$$ Since there is no transitive edge set where edge 3 is zero (except the totally degenerate edge set), Theorem [\[thm:Reduced\]](#thm:Reduced){reference-type="ref" reference="thm:Reduced"} implies that the reduced Ptolemy variety (all variants) is given by setting the Ptolemy coordinate of edge 3 equal to $1$.
