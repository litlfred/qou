---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1406.7337v4.pdf
source_sha256: 5bae8237742733b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.95
doc_brief: "Semi-Adequate Closed Braids and Volume — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and below in terms of the twist number, the number of"
---
One of the current aims of knot theory is to strengthen the relationships among the hyperbolic volume of the link complement, the colored Jones polynomial, and data extracted from link diagrams. In a recent monograph, Futer, Kalfagianni, and Purcell ([@Guts], or see [@Survey] for a survey of results) showed that, for sufficiently twisted negative braid closures and for certain Montesinos links, the volume of the link complement can be bounded above and below in terms of the twist number of an A-adequate link diagram. The results for Montesinos links were recently generalized by Purcell and Finlinson in [@Montesinos]. Similar results for alternating links were previously given by Lackenby in [@Lackenby], with the lower bounds improved upon by Agol, Storm, and W. Thurston in [@AgolStorm] and the upper bounds improved upon by Agol and D. Thurston in the appendix of [@Lackenby] and more recently improved upon by Dasbach and Tsvietkova in [@Refined]. In a previous paper ([@Me]), the author showed that the volumes for a large family of A-adequate link complements can be bounded in terms of two diagrammatic quantities: the twist number and the number of certain alternating tangles in a given A-adequate diagram.

In this paper, we show that the volumes for a family of A-adequate closed $n$-braids can be bounded above and below in terms of the twist number $t(D)$, the number $t^{+}(D)$ of positive twist regions, the number $t^{-}(D)$ of negative twist regions, the number $n$ of braid strings, and the number $m$ of special types of state circles (called *non-essential wandering circles*) that arise from a given closed braid diagram. Let $v_{8}=3.6638\ldots$ denote the volume of a regular ideal octahedron and let $v_{3}=1.0149\ldots$ denote the volume of a regular ideal tetrahedron. The main results of this paper, where the words "certain" and "more general" will be made precise later, are stated below.

::: theorem
[]{#introthm label="introthm"} For $D(K)$ a certain A-adequate closed $n$-braid diagram, the complement of $K$ satisfies the volume bounds $$\frac{v_{8}}{2}\cdot(t(D)-2(n+m-2)) \leq v_{8}\cdot(t^{-}(D)-(n+m-2)) \leq \mathrm{vol}(S^{3}\backslash K) < 10v_{3}\cdot(t(D)-1).$$ For $D(K)$ a more general A-adequate closed $n$-braid diagram, the complement of $K$ satisfies the volume bounds $$v_{8}\cdot(t^{-}(D)-t^{+}(D)-(n+m-2)) \leq \mathrm{vol}(S^{3}\backslash K) < 10v_{3}\cdot(t(D)-1) = 10v_{3}\cdot(t^{-}(D)+t^{+}(D)-1).$$
:::

By restricting to a family of A-adequate closed $3$-braids, we show that the volumes can also be bounded in terms of the parameter $s$ from the Schreier normal form of the $3$-braid. It should be noted that the lower bound provided in this paper, which relies on the more recent machinery of [@Guts], is often an improvement over the one given in [@Cusp].

::: theorem
[]{#sthm label="sthm"} For $D(K)$ a certain A-adequate closed $3$-braid diagram, the complement of $K$ satisfies the volume bounds $$v_{8}\cdot(s-1) \leq \mathrm{vol}(S^{3}\backslash K) < 4v_{8}\cdot s.$$
:::

In addition to providing diagrammatic volume bounds, we also show that, for the same family of A-adequate closed 3-braids, the parameters $k$ and $s$ from the Schreier normal form can actually be read off of the original 3-braid diagram.

The volumes for many families of link complements have also been expressed in terms of coefficients of the colored Jones polynomial ([@Volumish], [@Refined], [@Guts], [@Filling], [@Symmetric], [@Cusp], [@Stoimenow]). Denote the *$j^{th}$ colored Jones polynomial* of a link $K$ by $$J_{K}^{j}(t)=\alpha_{j}t^{m_{j}}+\beta_{j}t^{m_{j}-1}+\cdots+\beta_{j}'t^{r_{j}+1}+\alpha_{j}'t^{r_{j}},$$ where $j \in \mathbb{N}$ and where the degree of each monomial summand decreases from left to right. We will show that, for fixed $n$, the volumes for many of the closed $n$-braids considered in this paper can be bounded in terms of the stable penultimate coefficient $\beta_{K}':=\beta_{j}'$ (where $j \geq 2$) of the colored Jones polynomial. A result of this nature shows that the given collection of closed $n$-braids satisfies a Coarse Volume Conjecture ([@Guts], Section 10.4). This result, which is stated below, can be viewed as a corollary of Theorem [\[introthm\]](#introthm){reference-type="ref" reference="introthm"}.

::: corollary
[]{#newcor label="newcor"} For $D(K)$ a certain A-adequate closed $n$-braid diagram, the complement of $K$ satisfies the volume bounds $$v_{8}\cdot(\left|\beta_{K}'\right|-1) \leq \mathrm{vol}(S^{3}\backslash K) < 20v_{3}\cdot\left(\left|\beta_{K}'\right|+n+m-\dfrac{7}{2}\right).$$
:::

# Acknowledgments

I would like to thank Efstratia Kalfagianni for helpful conversations that led to this project. I would also like to thank the anonymous referee for helpful comments that led to an improvement in the quality of exposition in this paper.
