---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-009-23-natural-cocycles
section_title: "Natural cocycles"
section_number: 2.3
pages: 7-7
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 1.0
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:NaturalCocycle label="sec:NaturalCocycle"} The triangulation $\mathcal T$ of $M$ induces a decomposition $\overline \mathcal T$ of $M$ by truncated simplices.

::: definition
[]{#def:NaturalCocycle label="def:NaturalCocycle"} A *natural cocycle* on a truncated simplex $\overline\Delta$ is a labeling of the oriented edges by elements in $\mathop{\mathrm{SL}}(2,\mathbb C)$ such that

1.  []{#itm:1 label="itm:1"} The product around each face (triangular and hexagonal) is $I$, the identity matrix.

2.  []{#itm:3 label="itm:3"} Short edges are labeled by elements $\beta_{ij}^k$ in $P$.

3.  []{#itm:4 label="itm:4"} Long edges are labeled by counter diagonal elements $\alpha_{ij}$.

4.  []{#itm:2 label="itm:2"} Flipping the orientation replaces a labeling by its inverse, i.e. $\alpha_{ij}\alpha_{ji}=I=\beta_{ij}^k\beta_{ji}^k$.

The indexing is such that $\alpha_{ij}$ is the labeling of the long edge from vertex $i$ to $j$, and $\beta_{ij}^k$ is the labeling of the short edge near vertex $k$ parallel to the edge from $i$ to $j$; see Figure [\[fig:FundamentalCorrespondence\]](#fig:FundamentalCorrespondence){reference-type="ref" reference="fig:FundamentalCorrespondence"}.
:::

::: definition
A natural cocycle on $\overline \mathcal T$ is a natural cocycle on each truncated simplex such that the labelings of identified edges agree.
:::

::: remark
Decorations, $(G,H)$-representations, and natural cocycles are also defined for $G=\mathop{\mathrm{PSL}}(2,\mathbb C)$. The analogue of Corollary [\[cor:Freedom\]](#cor:Freedom){reference-type="ref" reference="cor:Freedom"} holds as well.
:::
