---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-015-41-cocycles-and-the-action-by-coboundaries
section_title: "Cocycles, and the action by coboundaries"
section_number: 4.1
pages: 10-11
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.944
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
Let $G=\mathop{\mathrm{SL}}(2,\mathbb C)$. Recall that the triangulation $\mathcal T$ induces a decomposition $\overline\mathcal T$ of $M$ by truncated simplices.

::: definition
A *$G$-cocycle* on $M$ is a labeling of the oriented edges of $M$ satisfying [\[itm:1\]](#itm:1){reference-type="ref" reference="itm:1"} and [\[itm:2\]](#itm:2){reference-type="ref" reference="itm:2"} of Definition [\[def:NaturalCocycle\]](#def:NaturalCocycle){reference-type="ref" reference="def:NaturalCocycle"}. A $G$-cocycle satisfying [\[itm:3\]](#itm:3){reference-type="ref" reference="itm:3"} as well is called a $(G,P)$-cocycle.
:::

A $G$-cocycle $\tau$ determines (up to conjugation) a representation $\pi_1(M)\to G$ by taking products along edge paths. Note that if $\tau$ is a $(G,P)$-cocycle this representation is boundary-unipotent and is canonically decorated. Hence, a $(G,P)$-cocycle determines a decoration.

::: definition
If $D$ is a decoration and $\tau$ a $(G,P)$-cocycle, we say that $\tau$ is compatible with $D$ if the decoration determined by $\tau$ equals $D$.
:::

Let $V(\overline\mathcal T)$ denote the set of vertices of $\overline\mathcal T$. Given an oriented edge $e$ of $\overline\mathcal T$, let $e_0,e_1\in V(\overline\mathcal T)$, denote the starting and ending vertex of $e$, respectively.

::: definition
A *zero-cochain* is a map $\eta\colon V(\overline\mathcal T)\to G$. The *coboundary* of a zero-cochain $\eta$ is the $G$-cocycle labeling an oriented edge $e$ by $\eta(e_0)^{-1}\eta(e_1)$.
:::

::: definition
The *coboundary action* of a *$P$-valued* zero-cochain $\eta\colon V(\overline\mathcal T)\to P$ on a $(G,P)$-cocycle $\tau$ replaces $\tau$ by $\eta\tau$, the cocycle defined by $$\eta\tau(e)=\eta(e_0)^{-1}\tau(e)\eta(e_1).$$
:::

Note that the coboundary action does not change the decorated representation.
