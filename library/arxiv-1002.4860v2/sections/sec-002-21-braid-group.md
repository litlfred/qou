---
doc_id: arxiv-1002.4860v2
doc_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_id: sec-002-21-braid-group
section_title: "Braid group"
section_number: 2.1
pages: 2-2
source_pdf: 1002.4860v2.pdf
source_sha256: a2cfe924f7a9f5a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 1.0
doc_brief: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL — We develop a diagrammatic formalism for calculating the Alexander polynomial of the closure of a braid as a state-sum."
---
Fix $n \geq 1$. Let $\Sigma_n = \{ \sigma_1, \ldots, \sigma_{n-1} \}$ be the set of braid generators, and let $\Sigma_n^\bullet$ denote the set of words in the symbols $\Sigma_n \sqcup \Sigma_n^{-1}$. Let $B_n$ be the braid group on $n$ strands, that is, the quotient of the free group on $\Sigma_n$ by the relations $$\begin{aligned}
    \sigma_r \sigma_{r+1} \sigma_r &=& \sigma_{r+1} \sigma_r \sigma_{r+1} \text { for each } 1 \le r \le n-2, \\
    \sigma_r \sigma_s &=& \sigma_s \sigma_r \text { when } |r - s| > 1.
\end{aligned}$$ Let $\mathcal{L}$ be the set of isotopy classes of smooth links in $S^3$. For each $n$, there is a canonical map $\Sigma_n^\bullet \twoheadrightarrow B_n$. Also there is a map $B_n \rightarrow \mathcal{L}$ defined by closing a braid into a link. The map $B_n \to \mathbb{Z}$, $\sigma_r \mapsto 1$ induces an isomorphism of groups $B_n / [B_n, B_n] \to \mathbb{Z}$. The image of $w \in \Sigma_n^\bullet$ under the composition $\Sigma_n^\bullet \twoheadrightarrow B_n \to \mathbb{Z}$ is called the *exponent sum* of $w$.
