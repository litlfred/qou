---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-015-the-partial-permutation-algebra-of-yang-mills-th
section_title: "The Partial Permutation Algebra of Yang-Mills Theory"
section_number: null
pages: 19-20
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
We have shown that the correlators of chiral Yang-Mills theory may be written as a sum over Hurwitz theory correlators of all degrees with insertions specified by operators in the algebra $\mathcal{C}_d$ of conjugacy classes of degree $d$.

This observation suggests that the appropriate structure to deal with the right-hand side of equation [\[dSumDictionary\]](#dSumDictionary){reference-type="eqref" reference="dSumDictionary"} is one that accommodates each degree $d$ operator algebra $\mathcal{C}_d$. The further requirement that this algebraic structure be that of a quantum field theory, and thus be an operator algebra, necessitates that a product be defined between operators of different degrees.

Hence, one is naturally led to introduce an algebra of partial permutations $\mathcal{A}_{\infty}$ to interpret equation [\[dSumDictionary\]](#dSumDictionary){reference-type="eqref" reference="dSumDictionary"}. The required field theory is obtained by deforming the extended field theory introduced in section [\[ExtendedHurwitz\]](#ExtendedHurwitz){reference-type="ref" reference="ExtendedHurwitz"}.

Thus far, we have only defined deformations of theories at fixed-degree -- see equations [\[TransDeformation\]](#TransDeformation){reference-type="eqref" reference="TransDeformation"} and [\[OmegaDeformation\]](#OmegaDeformation){reference-type="eqref" reference="OmegaDeformation"}. Extending such deformations to theories that capture all covering degrees at once requires care. In particular, one needs to define a partial permutation that behaves as the exponential distance operator $\Omega_{u}$ does inside any fixed-degree correlator. We define the appropriate operator $$\Tilde{\Omega}_u:=\sum_{r\ \text{minimal}} u^{\lvert r \rvert} A_{r}\, ,$$ where $\lvert r \rvert := \lvert d_r \rvert - \ell(r)$ is the charge of the partial permutation $r$, and the sum is taken over all minimal partial permutations $r$, namely the partial permutations with no inert entries. This includes the neutral element of the partial permutation algebra $A_{\empty}$ [@IvanovKerov]. The partial permutation $\tilde{\Omega}_u$ is defined with no reference to a specific value of the degree $d$ and indeed satisfies $$\langle \Tilde{\Omega}_{u} \cdot (\dots) \rangle_d =  \langle \Omega_{u} \cdot (\dots) \rangle_d\, ,$$ for all values of the degree.

The following deformation of the extended theory thus reproduces the partition functions [\[dSumDictionary\]](#dSumDictionary){reference-type="eqref" reference="dSumDictionary"} of chiral Yang-Mills theory in the absence of boundaries: $$\mathcal{L}\to \mathcal{L}- g_s t\, A_2 + \log \Tilde{\Omega}_{g_s u}^{2-2G} \, ,
    \label{ppDeformation}$$ where $A_2$ is the orbit of transpositions. As for the deformed Hurwitz theory, the observables are renormalized as $\hat{A}_r:=\tilde{\Omega}_{u}^{-1} A_r$ and the correlation functions of the theory are defined by summing over all degrees and covering surface genera. We introduce the vertex operators $\hat{\mathsf{A}}_{r}:=g_s^{\lvert d_r \rvert} \hat{A}_{r}$ and write $$\langle \hat{\mathsf{A}}_{r_1}\cdots \hat{\mathsf{A}}_{r_k}\rangle^{\text{def}} := \sum_{g} g_{s}^{2g-2} \sum_d q^d \langle g_s^{\ell(r_1)}\hat{A}_{r_1}\cdots g_s^{\ell(r_k)}\hat{A}_{r_k} \rangle_{g,d}^{\text{def}}\, ,$$ where the deformed correlator equals $\langle\, (\, \dots)\, \cdot\,  \rangle_{g,d}^{\text{def}}:=\langle \,(\, \dots)\, \cdot\, \tilde{\Omega}_u^{2-2G\,} e^{-tA_2} \rangle_{g,d}$.
