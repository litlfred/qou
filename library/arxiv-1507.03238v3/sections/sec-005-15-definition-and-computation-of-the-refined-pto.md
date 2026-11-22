---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-005-15-definition-and-computation-of-the-refined-pto
section_title: "Definition and computation of the refined Ptolemy varieties - an overview"
section_number: 1.5
pages: 4-5
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.994
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:Algorithm label="sec:Algorithm"} We consider only $\overline P(\mathcal T)$ here. The modified variants are defined and computed in a similar way. As mentioned earlier, a decorated representation defines Ptolemy coordinates, and thus gives rise to a distinguished set of edges, namely those having Ptolemy coordinate zero. The idea is to consider all possible such sets. It turns out that they have to satisfy a transitivity property.

::: definition
A *transitive edge set* is a set $E$ of edges of $\mathcal T$ satisfying that if any two edges of a face are in $E$, so is the third. The edges in a transitive edge set are called *zero-edges*. We sometimes denote $E$ by $(\mathcal T,E)$ to stress the significance of the triangulation.
:::

There are always at least two transitive edge sets: the *non-degenerate* edge set with no zero-edges, and the *totally degenerate* edge set where all edges are zero-edges. In Section [\[sec:InvariantPtolemy\]](#sec:InvariantPtolemy){reference-type="ref" reference="sec:InvariantPtolemy"} we define for all transitive edge sets $E$ (except the totally degenerate one) a Ptolemy variety $P(\mathcal T,E)$, parametrizing decorated representations whose Ptolemy coordinates are zero exactly at the edges in $E$. The triangulation independent Ptolemy variety $\overline P(\mathcal T)$ is then defined as the union of all the $P(\mathcal T,E)$ (see Definition [\[def:InvariantPtolemy\]](#def:InvariantPtolemy){reference-type="ref" reference="def:InvariantPtolemy"}). For the non-degenerate edge set $P(\mathcal T,E)$ is simply $P(\mathcal T)$. If each face has at most one zero-edge (the *edge-degenerate* case; see Definition [\[def:PartitionType\]](#def:PartitionType){reference-type="ref" reference="def:PartitionType"}), $P(\mathcal T,E)$ is defined by the usual Ptolemy relations together with an *edge relation* [\[eq:EdgeRelations\]](#eq:EdgeRelations){reference-type="eqref" reference="eq:EdgeRelations"} for each zero-edge. If one or more faces consists entirely of zero-edges, one can reduce to the edge-degenerate case by considering an auxilary triangulation $\mathcal T'$ obtained from $\mathcal T$ by performing an explicit sequence of 2-3 moves.

### Algorithm

We describe an algorithm that is guaranteed to find all boundary-unipotent irreducible representations of a manifold, no matter what triangulation $\mathcal T_0$ is used as input. The steps involve triangulations obtained from $\mathcal T_0$ by performing 2-3 moves, but these are purely auxiliary.

A simplex is *degenerate* if all six edges are zero. A face is *degenerate* if all 3 edges are zero.

-   Compute all transitive edge sets $(\mathcal T_0,E_0)$ ignoring the totally degenerate one.

-   If $(\mathcal T,E)$ has a degenerate simplex, replace it by a descendant (Definition [\[def:Descendant\]](#def:Descendant){reference-type="ref" reference="def:Descendant"}) $(\mathcal T',E')$ after performing a 2-3 move at a face adjacent to a non-degenerate and a degenerate simplex. This procedure reduces the number of degenerate simplices by one. Repeat until all simplices are non-degenerate.

-   If $(\mathcal T,E)$ has a degenerate face, replace it by the set of descendants $(\mathcal T',E')$ where $\mathcal T'$ is the triangulation obtained from $\mathcal T$ by performing a 2-3 move on each degenerate face. No descendants have degenerate faces.

-   For each $(\mathcal T,E)$ from step 2 compute the primary decomposition of the reduced Ptolemy variety $P(\mathcal T,E)_{\mathop{\mathrm{red}}}$.

-   For each zero dimensional component of $P(\mathcal T,E)_{\mathop{\mathrm{red}}}$, compute the corresponding boundary-unipotent $\mathop{\mathrm{SL}}(2,\mathbb C)$-representations via the Bruhat cocycle (Section [\[sec:BruhatCocycle\]](#sec:BruhatCocycle){reference-type="ref" reference="sec:BruhatCocycle"}). The output is a matrix of exact algebraic expressions for each generator of $\pi_1(M)$ in the face pairing presentation.

::: remark
If a Ptolemy variety contains a higher dimensional component $C$, one can compute the tautological representation $\pi_1(M)\to \mathop{\mathrm{SL}}(2,F(C))$, where $F(C)$ is the function field of $C$. See Section [\[sub:TautologicalRep\]](#sub:TautologicalRep){reference-type="ref" reference="sub:TautologicalRep"} for an example.
:::

::: remark
Among the 61911 manifolds in the SnapPy census `OrientableCuspedCensus` there is no manifold with more than 53 transitive edge sets (average 16). Most of these edge sets are only edge-degenerate (72%), so steps 1 and 2 above are rarely needed.
:::

::: remark
In case there are only two transitive edge sets it follows immediately from the definition that $\overline P(\mathcal T)=P(\mathcal T)$, so in this case the standard Ptolemy variety is guaranteed to detect all boundary-unipotent representations. Unfortunately, the only manifolds in the SnapPy census `OrientableCuspedCensus` with only two transitive edge sets are: `m003`, `m004`, `m015`, `m016`, `m017`, `m019`, `m118`, `m119`, `m180`, `m185`.
:::
