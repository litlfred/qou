---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-025-52-properties-of-the-knorrer-functor
section_title: "Properties of the Knorrer functor"
section_number: 5.2
pages: 25-26
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.969
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
As in the previous proof, $CC$ denotes the correction complex $$CC:= \begin{bmatrix} (\tilde{X}_{1--} )& (Y_{1}-\Ad_{g_{12}}(Y_2)_{++})\end{bmatrix}$$ Let us explain the equivariant structure of this matrix factorization. Since $B_{(2)}$-action does not change entries of the complex $\SymbolPrint{CC}$, the $B_{(2)}$ equivariant structure of $B_{(2)}$ is trivial.

To describe $B_{(1)}$ equivariant structure, let us write the differential of $CC$ as $$\SymbolPrint{D^{kn}}=D^{kn}_++D^{kn}_-, \quad D^{kn}_+=\sum_{k>l}(\tilde{X}_{1,--})_{kl}\theta_{kl},$$ $$D^{kn}_-=\sum_{k>l}

 (Y_{1}-\Ad_{g_{12}}(Y_2)_{++})_{lk}
\frac{\partial}{\partial \theta_{kl}},$$ where $\theta_{ij}$ are odd variables. The equivariant structure is defined by the action on $\theta_{kl}$: $$E_{ij}\cdot \theta_{kl}=\sum_{k>i}\theta_{ki}-\sum_{j>l}\theta_{jl}$$

The differential $D^{kn}$ is not $\frn_{(2)}$ invariant: $$E_{ij}\cdot D^{kn}_+=0,\quad E_{ij}\cdot D^{kn}_-=\sum_{j>l} [\Ad_{g_{12}}(Y_2)_-]_{il}\frac{\partial}{\partial\theta_{jl}}-\sum_{k>i} [\Ad_{g_{12}}(Y_2)_-]_{ik}\frac{\partial}{\partial\theta_{ki}}.$$ Thus the correction differentials are non-trivial in $\Phi(\calF)$ but the correction differentials are not arbitrary and below we emphasize properties of the correction differentials that are needed for the proofs that follow.

::: proposition
Let $\calF=(M,D,\partial_l,\partial_r)\in \MF_{B^2}(\calXr_2,\Wr)$, $M=V_{\mathrm{m}}\otimes \CC[\calXr_2]$, $V_{\mathrm{m}}\in \Mod^{filt}_{\frn^2}$ The matrix factorization $\Phi(\calF)\in \MF_{B^2}(\calX_2,W)$ is the equivariant matrix factorization $$(V_{\mathrm{m}}\otimes \CC[\calX_2], D+D^{kn}, \tilde{\partial}_l,\tilde{\partial}_r)$$ where $\tilde{\partial}_r=\partial_r$.
:::

::: proof
*Proof.* The only part that requires a discussion is the fact that the differential $\Phi(\calF)^{\sharp}$ has differential $D+D^{kn}$: a priori our construction of the push forward $j^x_*(\pi_y^*(\calF))$ relies on the extension lemma [\[lem: ext MF+\]](#lem: ext MF+){reference-type="ref" reference="lem: ext MF+"} and involves choice of an extension $\tilde{D}$ of $D$ from variety $\widetilde{\calX}_2$ to $\calX_2$ and completion of $\tilde{D}+D^{kn}_+$ to the differential $\tilde{D}+D^{kn}_++d^-$ such that $(\tilde{D}+D^{kn}_++d^-)^2=W$.

However, in our case map $j^x$ is actually a section of the (non-equivariant) map: $$\pi_x:\calX_2\to \widetilde{\calX}_2,\quad \pi_x(X,g_1,Y_1,g_2,Y_2)=(\Ad_{g_1}^{-1}(X)_+,g_1^{-1}g_2,Y_2).$$ Thus according to the remark [\[rem: section\]](#rem: section){reference-type="ref" reference="rem: section"} we can choose $\tilde{D}$ to be $D=\bar{\pi}^*(D)=\pi_x^*(\pi_y^*(D))$. Moreover, $d^-=D_-^{kn}$ because $(D+D^{kn})^2=W$ and the completion of the differential is unique up to an isomorphism. ◻
:::
