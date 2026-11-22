---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-020-52-error-term-for-balanced-young-diagrams
section_title: "Error term for balanced Young diagrams"
section_number: 5.2
pages: 16-17
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.899
latex_coverage_ratio: 0.946
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
Biane [@Biane1998] proved that if the permutation $\pi$ is fixed, its non-trivial cycle lengths are equal to $k_1,\dots,k_r\geq 2$, and the Young diagram $\lambda$ is balanced (i.e. $r(\lambda),c(\lambda)=O(\sqrt{n})$) then $$\chi^\lambda(\pi) = \frac{1}{(n)_{|\mathop{\mathrm{supp}}(\pi)|}}
\prod_{i=1}^r R_{k_i+1}(\lambda) + O\left(n^{-\frac{|\pi|+2}{2}}\right).$$

The following theorem gives a uniform estimate for the error term in Biane's formula (note that if $\pi$ is fixed and the Young diagram balanced, with $\varepsilon = \frac{C}{ \sqrt{ n } }$ and $A=D\ \sqrt{ n }$ we recover the result of Biane).

::: theorem
[]{#theo:equiv-cumulants label="theo:equiv-cumulants"} There exists a constant $a$ such that, for any $0 < \varepsilon < 1$, any Young diagram $\lambda$ of size $n$ and any permutation $\pi \in S_n$ such that $|\mathop{\mathrm{supp}}(\pi)|^2 \leq \varepsilon A$ and $r(\lambda),c(\lambda)\leq A\leq n$ we have:

$$\left|\chi^\lambda(\pi) - \frac{1}{(n)_{|\mathop{\mathrm{supp}}(\pi)|}}
\prod_{i=1}^r R_{k_i+1}(\lambda)\right| \leq 

\left(\varepsilon^2 +
\frac{A}{n} \varepsilon \right) \left(\frac{a A}{n}\right)^{|\pi|},$$

where the $k_i$ are the lengths of the non-trivial cycles of $\pi$.
:::

::: proof
*Proof.* We can assume that $\pi\in S_l$ has no fixpoints. Using Theorem [\[theo:character-sniady\]](#theo:character-sniady){reference-type="ref" reference="theo:character-sniady"} and Theorem [\[theo:cumulants\]](#theo:cumulants){reference-type="ref" reference="theo:cumulants"} together with the fact that any minimal factorisation of $\pi$ is a product of minimal factorisations of its cycles, we can write: $$\Sigma^\lambda(\pi) - \prod_{i=1}^r R_{k_i+1}^\lambda =
\sum_{\substack{\sigma_1,\sigma_2 \in S_l \\ \sigma_1 \sigma_2 = \pi \\
|\sigma_1| + |\sigma_2| > |\pi|}} (-1)^{|\sigma_1|}
N^\lambda(\sigma_1,\sigma_2).$$

To such a pair $(\sigma_1,\sigma_2)$ of permutations we can associate one of the pairs of permutations $(\sigma'_1,\sigma'_2)$ given by Lemma [\[lem:feray\]](#lem:feray){reference-type="ref" reference="lem:feray"} with $|\sigma'_1| \geq 1$.

Consider separately the case $|\sigma'_1|=1$. Then $\mathop{\mathrm{orbits}}(\sigma_1,\sigma_2)=
\mathop{\mathrm{orbits}}(\sigma'_1,\sigma'_2) \geq |C(\pi)|-1$ and the first inequality in [\[eq:swider\]](#eq:swider){reference-type="eqref" reference="eq:swider"} shows that $$N^\lambda(\sigma_1,\sigma_2)  \leq 
A^{|C(\sigma_1)|+|C(\sigma_2)|}\left(\frac{n}{A^2}\right)^{|C(\pi)|-1}$$

therefore the estimate given by

Proposition [\[prop:bipartite-graphs\]](#prop:bipartite-graphs){reference-type="ref" reference="prop:bipartite-graphs"} can be improved to the following one: $$N^\lambda(\sigma_1,\sigma_2) \leq A^{l-|C(\pi)|}n^{|C(\pi)|} \frac{1}{n}.$$

Clearly $A\geq l$ therefore by the same argument as in the proof of Theorem [\[theo:rough\]](#theo:rough){reference-type="ref" reference="theo:rough"}, we obtain the inequality $$\left|\Sigma^\lambda(\pi) - \prod_{i=1}^r R_{k_i+1}(\lambda) \right| \leq 4^l
A^{l-r} n^r \left(\frac{l^2}{n} + \sum_{i \geq 2} \frac{l^{2i}}{A^i
i!}\right).$$ The proof is now finished thanks to the remarks of the previous subsection and the inequality $\exp(z)-1-z \leq z^2$ for $0<z<1$. ◻
:::
