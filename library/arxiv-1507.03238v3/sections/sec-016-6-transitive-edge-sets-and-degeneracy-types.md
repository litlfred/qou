---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-016-6-transitive-edge-sets-and-degeneracy-types
section_title: "Transitive edge sets and degeneracy types"
section_number: 6
pages: 14-15
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
text_source: latex
latex_prose_ratio: 0.611
latex_coverage_ratio: 0.827
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
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
[]{#def:PartitionType label="def:PartitionType"} We divide the transitive edge sets into the following types: $$\begin{align*}
\textbf{Non-degenerate:}& \text{ No zero-edges (there is a unique such).}\\
\textbf{Edge-degenerate:}& \text{ Some zero-edges, but no degenerate faces.}\\
\textbf{Face-degenerate:}& \text{ Some degenerate faces, but no degenerate simplices.}\\
\textbf{Simplex-degenerate:}& \text{ Some, but not all, simplices are degenerate.}\\
\textbf{Totally degenerate:}& \text{ All simplices are degenerate (there is a unique such).}
\end{align*}$$
:::

Clearly, any $E\in\mathop{\mathrm{T}}(\mathcal T)$ falls into exactly one of these types.

## Decorations, Ptolemy assignments and Bruhat cocycles

::: definition
Let $E\in\mathop{\mathrm{T}}(\mathcal T)$. A decoration is of *type $E$* if its zero-edges agree with $E$. A Bruhat cocycle $\tau$ has *type $E$* if the set of long edges that are diagonal agrees with the zero-edges of $E$. A Ptolemy assignment has type $E$ if the set of edges whose Ptolemy coordinate is zero agrees with the zero-edges of $E$.
:::

Note that the one-to-one-correspondence in Theorem [\[thm:OneToOneGeneral\]](#thm:OneToOneGeneral){reference-type="ref" reference="thm:OneToOneGeneral"} preserves the type. We stress that the type depends on the triangulation.

::: remark
Decorations of type $E$ may not exist. For example, if there is an edge loop where all but one edge is zero, the argument in the proof of Lemma [\[lemma:TransitiveDec\]](#lemma:TransitiveDec){reference-type="ref" reference="lemma:TransitiveDec"} shows that $E$ cannot be the zero-set of a decoration.
:::

## The totally degenerate edge set {#sec:TotallyDegenerate}

::: proposition
[]{#prop:TotallyDegenerate label="prop:TotallyDegenerate"} If a decoration of a representation $\rho$ is totally degenerate, then $\rho$ is reducible.
:::

::: proof
*Proof.* If all Ptolemy coordinates are zero, the decoration must take all ideal vertices of $\widetilde M$ to the same $B$-coset. This is only possible if $\rho$ is reducible. ◻
:::

::: proposition
[]{#prop:ReducibleDegenerate label="prop:ReducibleDegenerate"} If a decoration of a reducible representation $\rho$ is not totally degenerate, then $\rho$ is boundary-degenerate.
:::

::: proof
*Proof.* A reducible representation has a totally degenerate decoration. The only way it can also have a decoration which is not totally degenerate is if a boundary component is a sphere or collapsed. ◻
:::
