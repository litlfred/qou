---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-019-51-upper-bound-for-characters-proof-of-theorem
section_title: "Upper bound for characters: proof of Theorem ??"
section_number: 5.1
pages: 15-16
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.883
latex_coverage_ratio: 0.945
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
::: proof
*Proof of Theorem [\[theo:rough\]](#theo:rough){reference-type="ref" reference="theo:rough"}.* Let $k_1,\dots,k_r\geq 2$ be the lengths of the non-trivial cycles in the cycle decomposition of $\pi\in S_n$. It follows that $l:=k_1+\cdots+k_r=|\mathop{\mathrm{supp}}\pi|$ and in the following we will regard $\pi$ as an element of $S_l$. We denote $A=\max(l,r(\lambda),c(\lambda))$.

We consider a map which to a pair $(\sigma_1,\sigma_2)$ associates any pair $(\sigma_1',\sigma_2')$ as prescribed by Lemma [\[lem:feray\]](#lem:feray){reference-type="ref" reference="lem:feray"}. For any fixed $\sigma_2'$ the permutations $\sigma_2$ such that $|\sigma_2'|= |\sigma_2'\sigma_2^{-1} |+|\sigma_2|$ can be identified with non-crossing partitions of the cycles of $\sigma_2'$ (see [@Biane1997 Section 1.3]). It follows that the number of such permutations $\sigma_2$ is equal to the product of appropriate Catalan numbers and, hence, this product is bounded from above by $4^{l}$. Therefore Theorem [\[theo:character-sniady\]](#theo:character-sniady){reference-type="ref" reference="theo:character-sniady"} and Proposition [\[prop:bipartite-graphs\]](#prop:bipartite-graphs){reference-type="ref" reference="prop:bipartite-graphs"} show that $$\begin{gathered}

|\Sigma^{\lambda}(\pi) | \leq
\sum_{\substack{\sigma_1,\sigma_2\in S_l,\\ \sigma_1 \sigma_2=\pi}} A^{l-r} n^r \left(\frac{1}{A}\right)^{o(\sigma_1,\sigma_2)} \leq
4^l \sum_{\substack{\sigma_1',\sigma_2'\in S_l, \\ \sigma'_1 \sigma'_2=\pi}} A^{l-r} n^r \left(\frac{1}{A}\right)^{|\sigma'_1|}\\
\leq 4^l A^{l-r} n^r \sum_{\sigma'_1\in S_l} \left(\frac{1}{A}\right)^{|\sigma'_1|} \leq
4^l A^{l-r} n^r \sum_{i \geq 0} \frac{l^{2i}}{A^i i!},
\end{gathered}$$ where the last inequality follows from Lemma [\[lem:nie-za-duzo\]](#lem:nie-za-duzo){reference-type="ref" reference="lem:nie-za-duzo"}. It follows that $$|\Sigma^{\lambda}(\pi) | \leq  4^l A^{l-r} n^r e^{\frac{l^2}{A}} \leq (4e)^l A^{l-r} n^r.$$ After dividing by $(n)_l \geq \left(\frac{n}{e}\right)^l$, we obtain $|\chi^{\lambda}(\pi) | \leq (4 e^2)^l (A/n)^{l-r}$, which finishes the proof because $l=|\mathop{\mathrm{supp}}\pi| \leq 2|\pi|$ and $l-r=|\pi|$. ◻
:::
