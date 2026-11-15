---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-042-61-adjunction
section_title: "Adjunction"
section_number: 6.1
pages: 37-38
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.957
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
[]{#adjunction label="adjunction"} Until now we have spoken about "adjoint" morphisms without really saying what the adjunction is.

::: lem
If $M$ and $N$ are two Bott-Samelson bimodules, the following map is an isomorphism of graded right $R$-modules $$\begin{aligned}
\mathrm{Hom}(B_sM,N)&\rightarrow \mathrm{Hom}(M,B_sN)\\
f&\mapsto (\mathrm{id}_{B_s}\otimes f)\circ ((j_s^a\circ m_s^a)\otimes \mathrm{id}_M)
\end{aligned}$$
:::

It is an exercice to prove this (one just needs to find explicitly the inverse map). In any case, a detailed proof can be found in [@Li0 Lemme 2.4]. This adjunction might seem complicated but in pictures, it is just this map

<figure>
<div class="center">
<img src="adjuncion.png" />
</div>
<figcaption>Adjunction map</figcaption>
</figure>

It is an easy exercice to prove that $j_s^a$ is the adjoint of $j_s$ in this sense as it is $m_s^a$ of $m_s$. Before we can consrtuct the light leaves we need
