---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-071-93-the-commutative-tower
section_title: "The commutative tower"
section_number: 9.3
pages: 69-70
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.855
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:conj differentials label="sub:conj differentials"}

We conjecture that the differential $d_N$ in the Soergel category is closely related to the section $f=x^N$ of the tautological bundle on the flag Hilbert scheme. More precisely, we propose the following:

::: conjecture
[]{#conj:differentials label="conj:differentials"} There is a map $\iota_N : (\mathrm{SBim}_n,d_N) \to (Z_n(\mathbb{C}),s_N)$ in the sense of Definition [\[def:morphism\]](#def:morphism){reference-type="ref" reference="def:morphism"}. The corresponding functors fit into the commutative diagram: $$\label{eqn:conj differentials}
\includegraphics{9_3.png}$$ Furthermore, there is a tower of commuting squares connected with $\pi_N,\mathop{\mathrm{Tr}},I$ akin to [\[eq:tower\]](#eq:tower){reference-type="eqref" reference="eq:tower"}.
:::

::: remark
We expect that the general differential on $\mathrm{SBim}_n$ corresponding to the polynomial $p(x)$ in the right hand side, corresponds to replacing $s_N$ by $s_{p(x)}$ in the left hand side.
:::

The conjecture is true for $n=1$. Indeed, $\mathrm{FHilb}_1=\mathrm{FHilb}_1^\text{dg}= \mathbb{C}$, so: $$\mathrm{Tot}_{\mathrm{FHilb}_1^\text{dg}} (\mathcal{T}_n[1],s_N) = S_{\mathbb{C}[x]}^\bullet \left(\mathbb{C}[x] \stackrel{x^N}\longrightarrow \mathbb{C}[x] \right) \cong \mathrm{Spec}\ \mathbb{C}[x]/(x^N).$$ The Soergel category $\mathrm{SBim}_1$ has a unique $\mathbb{C}[x]$ bimodule, namely $\mathbf{1} = \mathbb{C}[x,y]/(x-y)$, and the corresponding object in the dg category $(\mathrm{SBim}_1,d_N)$ is given by: $$\mathbf{1} = \left[ \mathbb{C}[x,y]\xtofrom[x-y]{(W(x)-W(y))/(x-y)}\mathbb{C}[x,y] \right]$$ where $W(x)=\frac{x^{N+1}}{N+1}$. One can eliminate $y$ and rewrite the above $$\mathbf{1} = \left[ \mathbb{C}[x]\xrightarrow{W'(x)=x^N}\mathbb{C}[x] \right]$$ from where it is clear that the categories $\mathrm{Tot}_{\mathrm{FHilb}_1^\text{dg}} (\mathcal{T}_n[1],s_N)$ and $(\mathrm{SBim}_1,d_N)$ are equivalent.
