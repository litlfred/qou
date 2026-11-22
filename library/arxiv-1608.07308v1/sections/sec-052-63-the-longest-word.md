---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-052-63-the-longest-word
section_title: "The longest word"
section_number: 6.3
pages: 50-50
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.851
latex_coverage_ratio: 0.952
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:longest label="sub:longest"}

Let us describe the sheaf for the positive lift $\sigma_1\sigma_2\sigma_1$ of the longest word in $S_3$. Remark that the following equation holds for all $a$ and $b$: $$\label{eqn:conj for 121}
\mathop{\mathrm{Tr}}(\sigma_1\sigma_2\sigma_1\mathcal{L}_2^{a}\mathcal{L}_3^{b})=\mathop{\mathrm{Tr}}(\sigma_2\sigma_1\sigma_1\mathcal{L}_2^{a}\mathcal{L}_3^{b}),$$ since $\sigma_1$ commutes both with $\mathcal{L}_2$ and $\mathcal{L}_3$ and the trace satisfies $\mathop{\mathrm{Tr}}(\sigma \sigma') = \mathop{\mathrm{Tr}}(\sigma'\sigma)$. By Corollary [\[cor:trace twisted identity\]](#cor:trace twisted identity){reference-type="ref" reference="cor:trace twisted identity"}, these traces are isomorphic up to a twist by a permutation $(1\ 2)$. In particular, the left hand side of [\[eqn:conj for 121\]](#eqn:conj for 121){reference-type="eqref" reference="eqn:conj for 121"} is supported on $\{x_1=x_3\}$, while the right hand side is supported on $\{x_2=x_3\}$. Furthermore, $$\iota_*(\sigma_2\sigma_1\sigma_1) = L_2\otimes \iota_*(\sigma_2)=L_2\otimes \mathcal{O}_{\mathrm{FHilb}(2\sim 3)}.$$ Note that in the notations of Section [\[sec:n=3\]](#sec:n=3){reference-type="ref" reference="sec:n=3"}, $\mathrm{FHilb}(2\sim 3)=Z_2\cup Z_5$. There is a natural involution $j_{12}$ on $\mathrm{FHilb}_3$ which exchanges $x_1$ and $x_2$ in $Z_1$, acts trivially on $Z_2$ and $Z_3$ and permutes $Z_4$ and $Z_5$. We arrive at the following conjecture:

::: conjecture
One has $\iota_*(\sigma_1\sigma_2\sigma_1)=j_{12}^{*}(L_2\otimes \mathcal{O}_{Z_2\cup Z_5}).$
:::
