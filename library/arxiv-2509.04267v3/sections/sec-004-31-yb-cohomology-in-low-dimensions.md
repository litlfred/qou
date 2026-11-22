---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-004-31-yb-cohomology-in-low-dimensions
section_title: "YB cohomology in low dimensions"
section_number: 3.1
pages: 5-6
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.95
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
In this subsection we review YB cohomology theory from [@SZ-YBH] in low dimensions, as it is used in the several sections that follow.

The cochain groups are defined by $C^0_{\rm YB}(V,V)=0$ and $C^n_{\rm YB}(V,V)={\rm Hom} (V^{\otimes n},V^{\otimes n})$ for $n>0$. We define the differentials for $f \in C^1_{\rm YB}(V,V)$ and $\phi \in C^2_{\rm YB}(V,V)$ by $$\begin{aligned}
    \delta^1_{\rm YB} (f) 
    &=&
    R ( f \otimes {\mathbb 1}) + R ( {\mathbb 1} \otimes  f ) 
    -  ( f \otimes {\mathbb 1}) R - ( {\mathbb 1} \otimes  f )  R ,\\
    \delta^2_{\rm YB} (\phi) &=&
    (R \otimes {\mathbb 1} ) ( {\mathbb 1}  \otimes R ) ( \phi \otimes  {\mathbb 1} )
    + (R \otimes {\mathbb 1} ) ( {\mathbb 1}  \otimes \phi ) ( R \otimes  {\mathbb 1} )
    +  (\phi \otimes {\mathbb 1} ) ( {\mathbb 1}  \otimes R ) ( R \otimes  {\mathbb 1} ) \\
    & & -  ( {\mathbb 1}  \otimes R ) ( R \otimes  {\mathbb 1} ) ( {\mathbb 1}  \otimes \phi ) 
    - ( {\mathbb 1}  \otimes R ) ( \phi \otimes  {\mathbb 1} ) ( {\mathbb 1}  \otimes  R ) 
    - ( {\mathbb 1}  \otimes \phi ) ( R \otimes  {\mathbb 1} ) ( {\mathbb 1}  \otimes  R ) .
\end{aligned}$$

When the YBO $R$ needs to be specified, we also use the notation $\delta^n_{R}$ for $\delta^n_{\rm YB}$. The fact that these define homology theory is proved in the next section. The corresponding cocycle, coboundary, homology groups are denoted as usual using $Z, B, H$, respectively.

<figure id="YBdiff1">
<div class="center">
<img src="YBdiff1" style="width:2in" />
</div>
<figcaption></figcaption>
</figure>

<figure id="YBd2">
<div class="center">
<img src="YBd2" style="width:3in" />
</div>
<figcaption></figcaption>
</figure>

The expression for $\delta^1_{\rm YB} (f)$ is depicted in Figure [1](#YBdiff1){reference-type="ref" reference="YBdiff1"}, where YBOs are represented by crossings and 1-cocycles $f$ are represented by circles on edges. The expression for $\delta^2_{\rm YB} (\phi)$ is depicted in Figure [2](#YBd2){reference-type="ref" reference="YBd2"}, where 2-cocycles $\phi$ are represented by double circles. The first positive terms in the figure correspond to the left-hand side of the YBE, while the negative terms to the right-hand side. The three terms for each is obtained by replacing a crossing by a double circle at exactly one place.

We cite the following lemma that relates 2-cocycles to deformations.

::: lemma
[]{#lem:YB2toR label="lem:YB2toR"} Let $R: V \rightarrow V$ be a YBO. Let $\phi \in C^2_{\rm YB} (V,V)$ be a YB 2-cochain for $R$. Then, $\tilde R = R + \hbar \phi$ is a YBO on $\tilde V =  \mathbb k [[ \hbar ]] / (\hbar^2)  \otimes V$ if and only if $\phi \in Z^2_{\rm YB} (V,V)$.
:::

::: proof
*Proof.* One computes the YBE for $\tilde R$, and checks that the terms for $\hbar$ constitutes the YB 2-cocycle condition. ◻
:::

This YBO $\tilde R =  R + \hbar \phi$ on $\tilde V$ is called an *infinitesimal deformation* of $R$.
