---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-033-43-estimates-on-some-classes-of-permutations
section_title: "Estimates on some classes of permutations"
section_number: 4.3
pages: 31-32
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.962
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
Recall that for a permutation $\pi$ we denote by $C(\pi)$ the set of its cycles. The length $$\|\pi\|:=l - |C(\pi)|$$ of a permutation $\pi\in\mathfrak{S}(l)$ is defined as the minimal number of factors necessary to write $\pi$ as a product of transpositions.

::: lemma
[]{#lem:not-many-permutations label="lem:not-many-permutations"} For all integers $r\geq 0$ and $l\geq 1$ $$\#\Big\{ \pi\in\mathfrak{S}(l) : \| \pi\| = r \Big\} \leq \frac{l^{2r}}{r!}.$$
:::

::: proof
*Proof.* We claim that for each permutation $\pi\in\mathfrak{S}(l)$ such that $\|\pi\|=r$ there exist at least $r$ transpositions $\tau$ with the property that the permutation $\pi':= \pi \tau$ fulfills $\| \pi'\|=\|\pi\|-1$. Indeed, each such a transposition is of the form $\tau=(a,b)$ with $a\neq b$ being elements of the same cycle of $\pi$; it follows that the number of such transpositions is equal to $$\sum_{c\in C(\pi)} \binom{|c|}{2} \geq \sum_{c\in C(\pi)} \big( |c|-1  \big) = \|\pi\|.$$

By repeating inductively the same argument for the collection of permutations $(\pi')$ obtained above, it follows that the permutation $\pi$ can be written in at least $r!$ different ways as a product of $r$ transpositions. Since there are $\binom{l}{2}<l^2$ transpositions in $\mathfrak{S}(l)$, this concludes the proof. ◻
:::

We revisit [\[sec:top-degree-by-Sniady\]](#sec:top-degree-by-Sniady){reference-type="ref" reference="sec:top-degree-by-Sniady"}. In the following we will need a convenient way of parametrizing the equivalence classes in $\mathcal{X}_l/\sim$; for this purpose we note that in each equivalence class one can choose a representative (which is not necessarily unique) $(\sigma_1,\sigma_2)$ with the property that the permutation $\sigma_2$ has a particularly simple cycle structure, namely $$\sigma_2=(1,2,\dots,i_1)(i_1+1,i_1+2,\dots,i_2) \cdots (i_{\ell-1}+1,i_{\ell-1}+2,\dots,i_\ell)$$ for some increasing sequence $1\leq i_1<i_2<\cdots<i_\ell=l$. Note that for a fixed $\ell=|C(\sigma_2)|$ $$\begin{gathered}
\label{eq:takietam}
\text{the number of permutations } \sigma_2 \text{ of the above form}\\
\text{is given by } \binom{l}{\ell-1} \leq l^{\ell-1}.
\end{gathered}$$
