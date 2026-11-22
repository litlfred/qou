---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE"
section_id: sec-008-31-statement-of-the-volume-conjecture
section_title: "Statement of the Volume Conjecture"
section_number: 3.1
pages: 16-18
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
toc_source: outline
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.963
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE — This is an introduction to the Volume Conjecture and its gener- alizations for nonexperts."
---
In [@Kashaev:MODPLA95] Kashaev introduced a link invariant $\langle L\rangle_N\in\mathbb{C}$ for an integer $N$ greater than one and a link $L$ by using the quantum dilogarithm. Then he observed in [@Kashaev:LETMP97] that the limit $2\pi\lim_{N\to\infty}\log|\langle K\rangle_N|/N$ is equal to the hyperbolic volume of the knot complement if a knot $K$ is hyperbolic. Here a knot in the three-sphere $S^3$ is called hyperbolic if its complement possesses a complete hyperbolic structure with finite volume. He also conjectured this would also hold for any hyperbolic knot.

In [@Murakami/Murakami:ACTAM12001] J. Murakami and I proved that Kashaev's invariant equals the $N$-dimensional colored Jones polynomial evaluated at the $N$-th root of unity, that is, $\langle L\rangle_N=J_N(L;\exp(2\pi\sqrt{-1}/N))$ and proposed that Kashaev's conjecture would hold for any knot by using the simplicial volume.

::: conjecture
[]{#conj:VC label="conj:VC"} The following equality would hold for any knot $K$. $$2\pi\lim_{N\to\infty}\frac{\log|J_N(K;\exp(2\pi\sqrt{-1}/N))|}{N}
  =\operatorname{Vol}(S^3\setminus{K}).$$
:::

To define the simplicial volume (or Gromov norm), we introduce the Jaco--Shalen--Johannson (JSJ) decomposition (or the torus decomposition) of a knot complement.

::: definition
Let $K$ be a knot. Then its complement $S^3\setminus{K}$ can be uniquely decomposed into hyperbolic pieces and Seifert fibered pieces by a system of tori: $$S^3\setminus{K}
  =
  \left(\bigsqcup H_i\right)\sqcup\left(\bigsqcup E_j\right)$$ with $H_i$ hyperbolic and $E_j$ Seifert-fibered.
:::

Then the simplicial volume of the knot complement is defined to be the sum of the hyperbolic volumes of the hyperbolic pieces.

::: definition
If a knot complement $S^3\setminus{K}$ is decomposed as above, then its simplicial volume $\operatorname{Vol}(S^3\setminus{K})$ is defined as $$\operatorname{Vol}(S^3\setminus{K})
  :=
  \sum_{H_i:\text{hyperbolic piece}}\text{Hyperbolic Volume of $H_i$}.$$
:::

::: example
Let us consider the $(2,1)$-cable of the figure-eight knot as shown in figure [1](#fig:2_1_fig_8){reference-type="ref" reference="fig:2_1_fig_8"}.

![$(2,1)$-cable of the figure-eight knot](2_1_cable_small.eps){#fig:2_1_fig_8}

Then its complement can be decomposed by a torus into two pieces (Figure [2](#fig:2_1_fig_8_JSJ){reference-type="ref" reference="fig:2_1_fig_8_JSJ"}), one hyperbolic and one Seifert fibered.

<figure id="fig:2_1_fig_8_JSJ">
<p><embed src="complement_2_1_cable_small.eps" /> <span class="math inline">$\underset{\text{\raisebox{-2mm}{hyperbolic}}}
    {\includegraphics[scale=0.3]{complement_fig8_small.eps}}$</span></p>
<figcaption>The JSJ decomposition of the <span class="math inline">(2,1)</span>-cable of the figure-eight knot</figcaption>
</figure>

Therefore we have $$\operatorname{Vol}
  \left(
    \raisebox{-14mm}{\includegraphics[scale=0.3]{complement_2_1_cable_small.eps}}
  \right)
  =
  \operatorname{Vol}
  \left(
    \raisebox{-14mm}{\includegraphics[scale=0.3]{complement_fig8_small.eps}}
  \right).$$
:::
