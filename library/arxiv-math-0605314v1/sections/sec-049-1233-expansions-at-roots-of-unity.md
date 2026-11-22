---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-049-1233-expansions-at-roots-of-unity
section_title: "Expansions at roots of unity"
section_number: 12.3.3
pages: 42-42
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 1.0
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:expansions-at-roots label="sec:expansions-at-roots"}

For every root of unity $\zeta$, $\iota _\zeta (J_M)\in \modZ [\zeta ][[q-\zeta ]]$ may be considered as a generalization of the Ohtsuki series $\tau ^O(M)=\iota _1(J_M)$. Define $\lambda _{\zeta ,k}(M)\in \modZ [\zeta ]$, $k\ge 0$, by $$\iota _\zeta (J_M)=\sum_{k\ge 0}\lambda _{\zeta ,k}(M)(q-\zeta )^k.$$

::: question
[]{#r41 label="r41"} Recall that the Ohtsuki series is considered to be related to the perturbative expansion of the Chern-Simons path integral. Are there any "physical" interpretation of the other power series $\iota _\zeta (J_M)$?
:::

Let us consider the case $\zeta =-1$. We have $$\label{e75}
  \iota _{-1}(J_M)=\sum_{k\ge 0}\lambda _{-1,k}(M)(q+1)^k
  \in \modZ [[q+1]]$$ where $\lambda _{-1,k}(M)\in \modZ$. It follows from Lemma [\[r47\]](#r47){reference-type="ref" reference="r47"} that $\lambda _{-1,0}(M)=1$. Thus the first interesting coefficient is $\lambda _{-1,1}(M)\in \modZ$, which is additive under connected sum, and satisfies $\lambda _{-1,1}(-M)=-\lambda _{-1,1}(M)$ by Proposition [\[thm:43\]](#thm:43){reference-type="ref" reference="thm:43"}. Some computations show that $\lambda _{-1,1}$ is nontrivial (i.e., non-vanishing for some $M$), and linearly independent over $\modQ$ to the Casson invariant $\lambda (M)=\frac{1}{6}\lambda _1(M)$ of $M$. (However, there is a congruence relation between them, see Remark [\[r63\]](#r63){reference-type="ref" reference="r63"} below.) See Remarks [\[r61\]](#r61){reference-type="ref" reference="r61"} and [\[r63\]](#r63){reference-type="ref" reference="r63"} for some other properties of $\lambda _{-1,k}(M)$. An interesting problem is to identify the topological information carried by $\lambda _{-1,1}(M)$.
