---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-027-74-simplex-degenerate-edge-sets
section_title: "Simplex-degenerate edge sets"
section_number: 7.4
pages: 19-20
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.859
latex_coverage_ratio: 0.932
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
Given a simplex-degenerate edge set $E\in \mathop{\mathrm{T}}(\mathcal T)$. Let $d(E)$ denote the number of degenerate simplices.

::: lemma
Let $E\in \mathop{\mathrm{T}}(\mathcal T)$ be simplex-degenerate and let $\mathcal T'$ be a triangulation obtained from $\mathcal T$ be performing a 2-3 move at a face between a degenerate and a non-degenerate simplex. Then $E$ has a unique descendant $E'\in \mathop{\mathrm{T}}(\mathcal T)$. Furthermore $d(E')=d(E)-1$.
:::

::: proof
*Proof.* Transitivity holds if and only if the new edge is non-zero. Hence, none of the new simplices are degenerate (see Figure [\[fig:WildDescendant\]](#fig:WildDescendant){reference-type="ref" reference="fig:WildDescendant"}). This proves the result. ◻
:::

::: corollary
[]{#cor:RemoveDegeneracy label="cor:RemoveDegeneracy"} Let $E\in \mathop{\mathrm{T}}(\mathcal T)$ be simplex-degenerate. There exists a triangulation $\mathcal T'$ obtained from $\mathcal T$ by performing 2-3 moves such that $E$ has a unique descendant $E'\in \mathop{\mathrm{T}}(\mathcal T')$, which is face-degenerate.
:::

::: proof
*Proof.* Repeatedly perform 2-3 moves at a face between a degenerate and a non-degenerate simplex until there are no more degenerate simplices. ◻
:::

::: definition
[]{#def:PtolemyWild label="def:PtolemyWild"} Let $E\in \mathop{\mathrm{T}}(\mathcal T)$ be simplex-degenerate and let $E'$ and $\mathcal T'$ be as in Corollary [\[cor:RemoveDegeneracy\]](#cor:RemoveDegeneracy){reference-type="ref" reference="cor:RemoveDegeneracy"}. Define $$P(\mathcal T,E)=P(\mathcal T',E')$$ and define $P^\sigma(\mathcal T,E)$ and $\mathcal EP(\mathcal T,E)$ similarly.
:::

Note that as a subset of $A(V(M))$ the definition is independent of the choice of $\mathcal T'$.

::: theorem
[]{#thm:OneOneWild label="thm:OneOneWild"} The one-to-one correspondences [\[eq:OneOneMild\]](#eq:OneOneMild){reference-type="eqref" reference="eq:OneOneMild"}, [\[eq:OneOneMildSigma\]](#eq:OneOneMildSigma){reference-type="eqref" reference="eq:OneOneMildSigma"}, and [\[eq:OneOneMildEnhanced\]](#eq:OneOneMildEnhanced){reference-type="eqref" reference="eq:OneOneMildEnhanced"} hold for all transitive edges sets $E$ that are not totally degenerate.
:::

::: proof
*Proof.* This follows from Theorem [\[thm:OneOneModerate\]](#thm:OneOneModerate){reference-type="ref" reference="thm:OneOneModerate"} and Corollary [\[cor:RemoveDegeneracy\]](#cor:RemoveDegeneracy){reference-type="ref" reference="cor:RemoveDegeneracy"}. ◻
:::
