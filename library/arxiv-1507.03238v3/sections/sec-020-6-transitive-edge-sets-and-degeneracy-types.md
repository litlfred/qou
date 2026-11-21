---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-020-6-transitive-edge-sets-and-degeneracy-types
section_title: "Transitive edge sets and degeneracy types"
section_number: 6
pages: 14-15
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.844
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:TransitiveEdgeSets label="sec:TransitiveEdgeSets"} Note that a decoration $D$ determines a distinguished subset of the edge set of $\mathcal T$, namely those whose Ptolemy coordinates are zero. We refer to this subset as the *zero-set* of $D$.

::: definition
[]{#def:TransitiveEdgeSubset label="def:TransitiveEdgeSubset"} A *transitive edge set* is a subset $E$ of the edges of $\mathcal T$ such that if two edges on a face are in $E$, so is the third. The set of transitive edge sets is denoted by $\mathop{\mathrm{T}}(\mathcal T)$. Given $E\in\mathop{\mathrm{T}}(\mathcal T)$, we refer to the edges in $E$ as *zero-edges*. To stress the dependence on $\mathcal T$ we sometimes denote a transitive edge set as $(\mathcal T,E)$ instead of $E$.
:::

::: lemma
[]{#lemma:TransitiveDec label="lemma:TransitiveDec"} The zero-set of a decoration is transitive.
:::

::: proof
*Proof.* If $g_0P$, $g_1P$ and $g_2P$ are the cosets assigned to the vertices of a face, the Ptolemy coordinates are given by $c_{ij}=\det(v_i,v_j)$, where $v_i=g_i\left(\begin{smallmatrix}1\\0\end{smallmatrix}\right)$. Hence, a Ptolemy coordinate $c_{ij}$ is zero if and only if $v_i$ and $v_j$ are linearly dependent. The result now follows from the fact that linear dependence of vectors is transitive. ◻
:::

::: definition
Let $E\in\mathop{\mathrm{T}}(\mathcal T)$ be a transitive edge set. A face of $\mathcal T$ is *degenerate* if all its three edges are zero-edges. A simplex of $\mathcal T$ is degenerate if all of its six edges are zero-edges.
:::

::: definition
[]{#def:PartitionType label="def:PartitionType"} We divide the transitive edge sets into the following types: $$\begin{aligned}
\textbf{Non-degenerate:}& \text{ No zero-edges (there is a unique such).}\\
\textbf{Edge-degenerate:}& \text{ Some zero-edges, but no degenerate faces.}\\
\textbf{Face-degenerate:}& \text{ Some degenerate faces, but no degenerate simplices.}\\
\textbf{Simplex-degenerate:}& \text{ Some, but not all, simplices are degenerate.}\\
\textbf{Totally degenerate:}& \text{ All simplices are degenerate (there is a unique such).}
\end{aligned}$$
:::

Clearly, any $E\in\mathop{\mathrm{T}}(\mathcal T)$ falls into exactly one of these types.
