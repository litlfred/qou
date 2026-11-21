---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-001-11-many-sums-and-products
section_title: "Many sums and products"
section_number: 1.1
pages: 2-3
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.947
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
Erdős [@Er77] also made the stronger conjecture that, for any $k\geq 2$ and $\epsilon>0$, $$\max(\mathopen{}\left| kA\mathclose{}\right|,\lvert A^{(k)}\rvert) \gg_{k,\epsilon}\mathopen{}\left| A\mathclose{}\right|^{k-\epsilon},$$ where $kA$ and $A^{(k)}$ denote the $k$-fold sum set and $k$-fold product set, respectively. (Once again this was for $A\subset \mathbb{Z}$ originally, but Erdős and Szemerédi [@ErSz83] asked it also for $A\subset \mathbb{R}$). Our methods provide a strong counterexample to this conjecture for large $k$.

::: theorem
[]{#th-mainmult label="th-mainmult"} There exists an absolute constant $C>0$ such that for any fixed $k\geq 3$ there exist arbitrarily large $A\subset \mathbb{R}$ with $$\max(\mathopen{}\left| kA\mathclose{}\right|,\lvert A^{(k)}\rvert)\leq \mathopen{}\left| A\mathclose{}\right|^{C\frac{\log k}{\log\log k}}.$$ Furthermore, for any fixed $\epsilon\in (0,1)$, there exist arbitrarily large $A\subset \mathbb{R}$ such that $$\max(\mathopen{}\left| kA\mathclose{}\right|,\lvert A^{(k)}\rvert)\leq \mathopen{}\left| A\mathclose{}\right|^{C^{1/\epsilon}+\epsilon \log k}\textrm{ for all }k\geq 3.$$
:::

This is likely the best possible dependence on $k$ in the exponent (at least for $k$ fixed and $\mathopen{}\left| A\mathclose{}\right|\to \infty$). It follows from work of Mudgal [@Mu24] and the recent resolution of the weak polynomial Freiman--Ruzsa conjecture by Gowers, Green, Manners, and Tao [@GGMT25] that, for any $A\subset \mathbb{R}$, for all $k\geq 3$, $$\max(\mathopen{}\left| kA\mathclose{}\right|,\lvert A^{(k)}\rvert)\geq\mathopen{}\left| A\mathclose{}\right|^{(\log k)^c}$$ for some absolute constant $c>0$. With sufficiently improved bounds on the number of solutions to linear equations in multiplicative groups (as discussed in Section [\[sec-linear\]](#sec-linear){reference-type="ref" reference="sec-linear"}) this exponent can likely be improved to $\frac{\log k}{\log\log k}$. This exact quantitative dependence was achieved for $A\subset \mathbb{Z}$ by Pálvölgyi and Zhelezov [@PaZh21]. In a similar vein, Konyagin [@Ko14] proved that if $A\subset \mathbb{C}$ is a finite set such that $\mathopen{}\left| AA\mathclose{}\right|\leq \mathopen{}\left| A\mathclose{}\right|^{1+O(1/k)}$ then $\mathopen{}\left| kA\mathclose{}\right|\geq \mathopen{}\left| A\mathclose{}\right|^{c\log k}$ for some constant $c>0$.
