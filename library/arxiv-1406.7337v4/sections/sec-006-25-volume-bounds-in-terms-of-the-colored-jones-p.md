---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume"
section_id: sec-006-25-volume-bounds-in-terms-of-the-colored-jones-p
section_title: "Volume bounds in terms of the colored Jones polynomial"
section_number: 2.5
pages: 11-12
source_pdf: 1406.7337v4.pdf
source_sha256: 5bae8237742733b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.971
doc_brief: "Semi-Adequate Closed Braids and Volume — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and below in terms of the twist number, the number of"
---
We now continue our study of volume bounds for hyperbolic A-adequate closed braids by translating our diagrammatic volume bounds from earlier to volume bounds in terms of the stable penultimate coefficient $\beta_{K}'$ of the colored Jones polynomial. Recall from the introduction that we denote the *$j^{th}$ colored Jones polynomial* of a link $K$ by $$J_{K}^{j}(t)=\alpha_{j}t^{m_{j}}+\beta_{j}t^{m_{j}-1}+\cdots+\beta_{j}'t^{r_{j}+1}+\alpha_{j}'t^{r_{j}},$$ where $j \in \mathbb{N}$ and where the degree of each monomial summand decreases from left to right. The following corollary of Theorem [\[mytheorem\]](#mytheorem){reference-type="ref" reference="mytheorem"} is a more precise version of Corollary [\[newcor\]](#newcor){reference-type="ref" reference="newcor"} from the introduction.

::: corollary
[]{#newestsetup label="newestsetup"} Let $D(K)=\widehat{\beta}$ denote the closure of a nice $n$-braid $\beta \in B_{n}$ that satisfies the assumptions of Lemma [\[setup\]](#setup){reference-type="ref" reference="setup"}. In the case that $n=3$ and in the case that $n \geq 4$ when the only positive syllables of $\beta$ possibly occur in the generators $\sigma_{1}$ and $\sigma_{n-1}$, we have the volume bounds $$v_{8}\cdot(\left|\beta_{K}'\right|-1) \leq \mathrm{vol}(S^{3}\backslash K) < 20v_{3}\cdot\left(\left|\beta_{K}'\right|+n+m-\dfrac{7}{2}\right).$$
:::

::: proof
*Proof.* Since $D(K)$ is a connected, A-adequate link diagram, then Theorem 3.1 of [@HeadTail] implies that the absolute value $$\left|\beta_{K}'\right|:=\left|\beta_{j}'\right|=1-\chi(\mathbb{G}_{A}')$$ is independent of $j \geq 2$. By combining this result with Theorem [\[Cor\]](#Cor){reference-type="ref" reference="Cor"} and Theorem [\[mytheorem\]](#mytheorem){reference-type="ref" reference="mytheorem"}, we get the desired result. ◻
:::
