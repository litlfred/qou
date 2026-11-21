---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-011-21-constructing-quantum-invariants
section_title: "Constructing quantum invariants"
section_number: 2.1
pages: 5-6
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.961
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
[]{#sect-construct label="sect-construct"} Let $\mathcal{B}$ be a ribbon autonomous category ($\mathcal{B}$ is not necessarily linear). Assume that $\mathcal{B}$ admits a coend: $$C=\int^{Y \in \mathcal{B}} \leftidx{^\vee}{\!Y}{} \otimes Y,$$ with universal coaction $\delta_Y \colon Y \to Y \otimes C$ (see Section [\[sect-coend-cat\]](#sect-coend-cat){reference-type="ref" reference="sect-coend-cat"}). In particular, using the general theory of coends, we have the following universal property: for any natural transformation $\xi=\{\xi_{Y_1,\dots,Y_n} \colon Y_1 \otimes \cdots \otimes Y_n \to Y_1 \otimes \cdots \otimes Y_n \otimes M\}_{Y_1,\dots,Y_n
\in \mathrm{Ob}(\mathcal{B})}$, where $M$ is an object of $\mathcal{B}$, there exists a unique morphism $r\colon C^{\otimes n} \to M$ such that: $$\psfrag{X}[Bl][Bl]{\scalebox{.8}{$Y_1$}}
 \psfrag{Y}[Bl][Bl]{\scalebox{.8}{$Y_n$}}
 \psfrag{M}[Bl][Bl]{\scalebox{.8}{$M$}}
 \psfrag{H}[cc][cc]{\scalebox{.8}{$\delta_{Y_1}$}}
 \psfrag{K}[cc][cc]{\scalebox{.8}{$\delta_{Y_n}$}}
 \psfrag{C}[cc][cc]{\scalebox{.8}{$C$}}
 \psfrag{B}[cc][cc]{\scalebox{1}{$r$}}
 \psfrag{R}[cc][cc]{\scalebox{1}{$\xi_{Y_1,\dots,Y_n}$}}
 \raisebox{-.5\height}{\includegraphics[scale=.8]{fact-coend3.eps}} \quad = \quad \raisebox{-.5\height}{\includegraphics[scale=.8]{fact-coend4.eps}}$$ for all objects $Y_1, \dots , Y_n$ of $\mathcal{B}$.

Now let $T$ be a ribbon $n$-string link with $n$ a non-negative integer. Recall $T$ is a ribbon $(n,n)$-tangle consisting of $n$ arc components, without any closed component, such that the $k$th arc ($1\leq k \leq n$) joins the $k$th bottom endpoint to the $k$th top endpoint. We orient $T$ from bottom to top. By virtue of the universality of the category of colored ribbon tangles, coloring the $n$ components of $T$ with objects $Y_1, \dots, Y_n$ of $\mathcal{B}$ yields a morphism $T_{Y_1, \cdots, Y_n}
\colon Y_1 \otimes \cdots \otimes Y_n \to Y_1 \otimes \cdots \otimes Y_n$, that is, $$T_{Y_1, \cdots,Y_n}= \psfrag{X}[cl][cl]{\scalebox{.8}{$Y_1$}} \psfrag{Y}[cl][cl]{\scalebox{.8}{$Y_n$}}
\psfrag{H}[cc][cc]{\scalebox{.8}{$\delta_{Y_1}$}} \psfrag{K}[cc][cc]{\scalebox{.8}{$\delta_{Y_n}$}}
 \psfrag{C}[cc][cc]{\scalebox{.8}{$C$}}  \psfrag{B}[cc][cc]{\scalebox{.8}{$\phi_T$}}
 \raisebox{-.5\height}{\includegraphics[scale=.8]{fact-coend1.eps}}\, .$$ Moreover $T_{Y_1, \cdots, Y_n}$ is natural in each variable $Y_k$ and so, by universality of the coaction of the coend $C$, there exists a unique morphism: $$\phi_T \colon C^{\otimes n} \to \mathbb{1}$$ such that: $$T_{Y_1, \cdots,Y_n}= \psfrag{X}[cl][cl]{\scalebox{.8}{$Y_1$}} \psfrag{Y}[cl][cl]{\scalebox{.8}{$Y_n$}}
\psfrag{H}[cc][cc]{\scalebox{.8}{$\delta_{Y_1}$}} \psfrag{K}[cc][cc]{\scalebox{.8}{$\delta_{Y_n}$}}
 \psfrag{C}[cc][cc]{\scalebox{.8}{$C$}}  \psfrag{B}[cc][cc]{\scalebox{.8}{$\phi_T$}}
 \;\raisebox{-.5\height}{\includegraphics[scale=.8]{fact-coend2.eps}} \, .$$

Two natural questions arise in this context:

-   How to evaluate the forms $\phi_T$ to get invariants of framed links[^1] and, further, of 3-manifolds?

-   How to compute the forms $\phi_T$ which are defined by universal property?

We address the first question in Section [\[sect-kirby\]](#sect-kirby){reference-type="ref" reference="sect-kirby"} and the second one in Section [\[sect-Hdiag\]](#sect-Hdiag){reference-type="ref" reference="sect-Hdiag"}.

[^1]: A framed link with $n$ components is always the closure of some ribbon $n$-string link.
