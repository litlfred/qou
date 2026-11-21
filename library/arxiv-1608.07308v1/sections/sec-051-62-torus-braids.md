---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-051-62-torus-braids
section_title: "Torus braids"
section_number: 6.2
pages: 49-50
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.936
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sec:n=3 torus label="sec:n=3 torus"}

In this section, we compare our conjectures to the ones of [@GORS; @ORS] for three-strand torus braids. The remainder of this Section provides explicit computations that follow from Conjectures [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"} and [\[conj:knots\]](#conj:knots){reference-type="ref" reference="conj:knots"}.

::: proposition
[]{#prop:3 strand label="prop:3 strand"}

The sheaves on $\mathrm{FHilb}_3$ associated to torus braids on 3 strands are: $$\label{eqn:3 strand}
\iota_{*}(\sigma_1\sigma_2)^{k} = \iota_{*}(\sigma_2\sigma_1)^{k} = 
\begin{cases}
\mathcal{L}_2^{m}\mathcal{L}_3^{m} & k=3m, \\
\mathcal{L}_2^{m}\mathcal{L}_3^{m}\otimes \mathcal{O}_{Z_2}& k=3m+1,\\
\mathcal{L}_2^{m+1}\mathcal{L}_3^{m}\otimes \mathcal{O}_{Z_2}& k=3m+2.\\
\end{cases}$$ Here $m$ (and hence $k$) is allowed to be either positive or negative.
:::

::: proof
*Proof.* Clearly, $(\sigma_1\sigma_2)^3=(\sigma_2\sigma_1)^3=\mathbf{FT}_3= \iota^*(\mathcal{L}_2\mathcal{L}_3)$, so in virtue of the projection formula [\[eqn:sk\]](#eqn:sk){reference-type="eqref" reference="eqn:sk"} it is sufficient to consider the cases $k=0,1,2$. For $k=0$, Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"} states that $\iota_*(\mathbf{1})=\mathcal{O}_{\mathrm{FHilb}_3}$, which is precisely the content of [\[eqn:3 strand\]](#eqn:3 strand){reference-type="eqref" reference="eqn:3 strand"}. For $k=1$, Conjecture [\[conj:knots\]](#conj:knots){reference-type="ref" reference="conj:knots"} implies $\iota_*(\sigma_1\sigma_2)=\mathcal{O}_{Z_2}$. Furthermore, for all $a, b \in \mathbb{N}$ one has: $$\label{eqn:equal traces}
\mathop{\mathrm{Tr}}(\sigma_2\sigma_1\mathcal{L}_2^{a}\mathcal{L}_3^{b})=\mathop{\mathrm{Tr}}(\sigma_1\sigma_2\mathcal{L}_2^{a}\mathcal{L}_3^{b}),$$ since $\sigma_1$ commutes with both $\mathcal{L}_2$ and $\mathcal{L}_3$, and the trace map enjows the property $\mathop{\mathrm{Tr}}(\sigma\sigma') = \mathop{\mathrm{Tr}}(\sigma'\sigma)$. By virtue of the definition [\[eqn:general 1\]](#eqn:general 1){reference-type="eqref" reference="eqn:general 1"} of the sheaves associated to the braids $\sigma_1\sigma_2$ and $\sigma_2\sigma_1$, formula [\[eqn:equal traces\]](#eqn:equal traces){reference-type="eqref" reference="eqn:equal traces"} implies that $\iota_*(\sigma_2\sigma_1) = \iota_*(\sigma_1\sigma_2)$. The case $k=2$ of [\[eqn:3 strand\]](#eqn:3 strand){reference-type="eqref" reference="eqn:3 strand"} follows analogously, because: $$(\sigma_1\sigma_2)^2=\mathcal{L}_2\sigma_2\sigma_1,\ (\sigma_2\sigma_1)^2=\sigma_1\sigma_2\mathcal{L}_2.$$ ◻
:::

To compute the Khovanov-Rozansky homology of torus braids, one needs to compute the homology of the resulting line bundles either on $\mathrm{FHilb}_3$, or on $Z_2=\mathrm{FHilb}_3(\mathrm{point})\times \mathbb{C}$. For simplicity, we will consider only the latter case, which corresponds to knots:

::: proposition
[]{#prop:3 strand torus label="prop:3 strand torus"}

The following equations hold: $\qquad H^{i}(\mathrm{FHilb}_3(\mathrm{point}),\mathcal{L}_2^{a}\mathcal{L}_3^{b}) =$ $$\label{eqn:3 strand torus}
= \begin{cases}
H^i(\mathbb{P}^1,\mathcal{O}(a)\otimes S^b(\mathcal{O}(2)\oplus qt\mathcal{O}(-1))& \text{if}\ b\ge 0,\\
0& \text{if}\ b=-1, \\
H^{i+1} \left(\mathbb{P}^1,\frac {\mathcal{O}(a-1)}{qt} \otimes S^{-b-2}\left(\mathcal{O}(-2) \oplus \frac {\mathcal{O}(1)}{qt} \right) \right)& \text{if}\ b\le -2.
\end{cases}$$
:::

::: proof
*Proof.* Let $\pi:\mathrm{FHilb}_3(\mathrm{point})\to \mathrm{FHilb}_2(\mathrm{point})=\mathbb{P}^1$ be the natural projection. By [\[eqn:z2\]](#eqn:z2){reference-type="eqref" reference="eqn:z2"} we have $\mathrm{FHilb}_3(\mathrm{point}) = \mathrm{Proj}\left( S^*_{\mathbb{P}^1} (\mathcal{O}(2)\oplus qt\mathcal{O}(-1)) \right)$. The following properties hold: $$R^{i}\pi_* \left( \mathcal{L}_3^{b} \right)=\begin{cases}
S^b(\mathcal{O}(2)\oplus qt\mathcal{O}(-1)) & \text{if} \ i=0 \text{ and } b\ge 0, \\
\frac {\mathcal{O}(-1)}{qt} \otimes S^{-b-2}\left(\mathcal{O}(-2) \oplus \frac {\mathcal{O}(1)}{qt} \right) &\text{if} \ i=1 \text{ and } b\le -2, \\
0 & \text{otherwise}
\end{cases}$$ Indeed, the second formula follows from the first and Serre duality. This completes the proof. ◻
:::

::: corollary
[]{#cor:3 strand torus label="cor:3 strand torus"} Putting together [\[eqn:3 strand\]](#eqn:3 strand){reference-type="eqref" reference="eqn:3 strand"}, [\[eqn:3 strand torus\]](#eqn:3 strand torus){reference-type="eqref" reference="eqn:3 strand torus"} and the well-known formula for the cohomology of line bundles on $\mathbb{P}^1$, we have the following formulas for all $m \geq 0$. $$\label{eqn:hhh 3 strand 1}
\mathop{\mathrm{HHH}}\left( (\sigma_1\sigma_2)^{3m+1} \right) = H^*(\mathrm{FHilb}_3(\mathrm{point}),\mathcal{L}_2^{m}\mathcal{L}_3^{m}) =$$ $$= H^0 \left(\mathbb{P}^1,  \bigoplus_{i=0}^m (qt)^i \mathcal{O}(3m-3i)\right) = \sum_{i=0}^m \sum_{j=0}^{3m-3i} q^{i+j} t^{3m-2i-j}$$ $$\label{eqn:hhh 3 strand 2}
\mathop{\mathrm{HHH}}\left( ( \sigma_1\sigma_2)^{3m+2} \right) = H^*(\mathrm{FHilb}_3(\mathrm{point}),\mathcal{L}_2^{m+1}\mathcal{L}_3^{m})=$$ $$= H^0 \left(\mathbb{P}^1,  \bigoplus_{i=0}^m (qt)^i \mathcal{O}(3m-3i+1)\right) = \sum_{i=0}^m \sum_{j=0}^{3m-3i+1} q^{i+j} t^{3m-2i-j+1}$$
:::

This agrees with the $a=0$ part of the Khovanov-Rozansky homology of $(3,3m+1)$ and of $(3,3m+2)$ torus knots, conjectured in [@GORS Section 5.2]. To recover the full $a$ dependence, we need to twist the right hand sides of [\[eqn:hhh 3 strand 1\]](#eqn:hhh 3 strand 1){reference-type="eqref" reference="eqn:hhh 3 strand 1"} and [\[eqn:hhh 3 strand 2\]](#eqn:hhh 3 strand 2){reference-type="eqref" reference="eqn:hhh 3 strand 2"} by the exterior power: $$\wedge^\bullet \mathcal{T}_3^\vee = \wedge^\bullet (\mathcal{L}_3 ``\oplus" \mathcal{L}_2 \oplus \mathcal{O})^\vee$$ where the symbol $``\oplus"$ refers to the fact that $\mathcal{T}_3$ is a non-trivial extension of $\mathcal{L}_2 \oplus \mathcal{O}$ by $\mathcal{L}_3$. Note that all of our computations can be easily extended to "twisted torus knots\" in the sense of [@CDW], which are presented by the braids $(\sigma_1\sigma_2)^{k}\otimes \iota^* (\mathcal{L}_2^{a} )$. We leave the corresponding computation to the interested reader.
