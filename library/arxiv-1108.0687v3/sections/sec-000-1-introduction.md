---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-2
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.967
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
[]{#sec:intro label="sec:intro"}

Our goal in this paper is to prove concentration inequalities for Lipschitz functions of certain collections of negatively dependent binary-valued random variables. To illustrate our general methods we state our main result in a special case that was motivated by a question of E. Mossel (personal communication).

::: thm
[]{#th:sp tree label="th:sp tree"} Let $G = (V,E)$ be a finite connected graph, let ${\mathbb P}$ be the uniform measure on the spanning trees of $G$, and for $e \in E$ let $X_e$ be the indicator function of the event that $e$ is in the chosen spanning tree. Let $f : \{ 0 , 1 \}^E \to \mathbb{R}$ be any function with Lipschitz constant 1. Then $${\mathbb P}(f - {\mathbb E}f \geq a) \leq \exp \left ( - \frac{a^2}{8 \, |V|}
   \right ) \, .$$
:::

For example we might take $f$ to be one half the number of vertices whose degree in the random tree is odd. This result is a consequence of more general results stated in Section [\[sec:results\]](#sec:results){reference-type="ref" reference="sec:results"} and Section [\[sec:examples\]](#sec:examples){reference-type="ref" reference="sec:examples"}.
