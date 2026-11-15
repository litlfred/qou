---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-030-9-the-reduced-ptolemy-varieties
section_title: "The reduced Ptolemy varieties"
section_number: 9
pages: 21-21
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 1.0
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
The diagonal action on decorations, Ptolemy assignments, and natural cocycles extends canonically to the case where some of the Ptolemy coordinates are zero and some of the long edges are diagonal instead of counterdiagonal. We define the reduced Ptolemy variety $\overline P_{\mathop{\mathrm{red}}}(\mathcal T)$ to be the quotient of $\overline P(\mathcal T)$ by the diagonal action. In [@PtolemyField] we showed that the reduced Ptolemy variety $P(\mathcal T)_{\mathop{\mathrm{red}}}$ can be computed by setting appropriately chosen Ptolemy coordinates equal to $1$:

::: theorem
[]{#thm:SetEdgesToOne label="thm:SetEdgesToOne"} Let $G$ be a connected graph in the one-skeleton of $\widehat M$, which has fundamental group $\mathbb Z$ and contains all vertices. The reduced Ptolemy variety $P(\mathcal T)_{\mathop{\mathrm{red}}}$ is isomorphic to the subvariety of $P(\mathcal T)$ where the Ptolemy coordinates of all edges in $G$ are $1$. The same result holds for $P^\sigma(\mathcal T)_{\mathop{\mathrm{red}}}$.
:::

::: remark
In [@PtolemyField] this is only proved when $G$ is a so-called "maximal tree with $1$- or $3$-cycle", but the proof can be trivially extended to any graph with fundamental group $\mathbb Z$ containing all vertices.
:::

::: theorem
[]{#thm:Reduced label="thm:Reduced"} Let $E\in \mathop{\mathrm{T}}(\mathcal T)$ be edge-degenerate. Then, there exists a graph $G$ of nonzero edges which has fundamental group $\mathbb Z$ and contains all vertices. The reduced Ptolemy variety $P(\mathcal T,E)_{\mathop{\mathrm{red}}}$ is isomorphic to the subvariety of $P(\mathcal T,E)$ where the Ptolemy coordinates of all edges in $G$ are $1$. The same result holds for $P^\sigma(\mathcal T,E)_{\mathop{\mathrm{red}}}$ and $\mathcal EP(\mathcal T,E)_{\mathop{\mathrm{red}}}$.
:::

::: proof
*Proof.* Since $E$ is edge-degenerate, the set of nonzero edges connects all vertices of $\mathcal T$ and contains cycles. Thus, we can choose a graph $G$ with the above properties. Hence, the result follows from Theorem [\[thm:SetEdgesToOne\]](#thm:SetEdgesToOne){reference-type="ref" reference="thm:SetEdgesToOne"}. The proofs trivially extend to the case of $\mathcal EP(\mathcal T,E)_{\mathop{\mathrm{red}}}$. ◻
:::
