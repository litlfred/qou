---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-070-92-sections-and-schemes
section_title: "Sections and schemes"
section_number: 9.2
pages: 68-69
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.871
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:sections schemes label="sub:sections schemes"}

On the geometric side, we have a remarkable family of dg schemes closely related to $\mathrm{FHilb}^\text{dg}_n = \mathrm{FHilb}_n^\text{dg}(\mathbb{C})$. Namely, let $s$ be an arbitrary section of the tautological bundle $\mathcal{T}_n$. It defines a contraction map: $$\label{eqn:contraction}
d_s:\wedge^{\bullet}\mathcal{T}_n^{\vee}\to \wedge^{\bullet-1}\mathcal{T}_n^{\vee}$$ Recall the construction [\[eqn:iota wedge\]](#eqn:iota wedge){reference-type="eqref" reference="eqn:iota wedge"}: $$\widetilde{\iota}_*(\sigma) = \iota_*(\sigma) \otimes \wedge^\bullet \mathcal{T}_n^\vee$$ which is naturally a sheaf of dg modules on $\mathrm{Tot}_{\mathrm{FHilb}_n^\text{dg}} \mathcal{T}_n[1]$. If we endow the exterior power with the differential [\[eqn:contraction\]](#eqn:contraction){reference-type="eqref" reference="eqn:contraction"}, we obtain: $$\left( \widetilde{\iota}_*(\sigma), d_s \right)$$ which is naturally a sheaf of dg modules on the dg scheme: $$\mathrm{Tot}_{\mathrm{FHilb}_n^\text{dg}} (\mathcal{T}_n[1],s) := \text{the sheaf of dg algebras } \left( \wedge^\bullet \mathcal{T}_n^\vee, d_s \right) \text{ on }\mathrm{FHilb}_n^\text{dg}.$$ To construct sections $s$ of the tautological bundle $\mathcal{T}_n$, recall that its fibers are given by: $$\mathcal{T}_n|_{I_n\subset \ldots\subset \mathbb{C}[x,y]} = \mathbb{C}[x,y]/I_n.$$ Therefore every polynomial $f\in \mathbb{C}[x,y]$ defines a section $s_f \in \Gamma(\mathrm{FHilb}_n, \mathcal{T}_n)$ for all $n$, and these sections are all compatible with each other: $$\includegraphics{before_9_3a.png}$$ The morphism $\mathrm{FHilb}_{n} \stackrel{\pi}\longrightarrow \mathrm{FHilb}_{n-1} \times \mathbb{C}$ therefore induces a map: $$\mathrm{Tot}_{\mathrm{FHilb}_n^\text{dg}} (\mathcal{T}_n[1],s_f) \stackrel{\pi_f}\longrightarrow \mathrm{Tot}_{\mathrm{FHilb}_{n-1}^\text{dg}\times \mathbb{C}} (\mathcal{T}_{n-1}[1],s_f)$$ and so one has a commutative diagram of maps of dg schemes: $$\includegraphics{before_9_3b.png}$$ where the vertical maps are simply induced by the map of dg algebras $\wedge^\bullet \mathcal{T}_n^\vee \rightarrow \left( \wedge^\bullet \mathcal{T}_n^\vee, d_s \right)$. Note that the dg scheme $\mathrm{Tot}_{\mathrm{FHilb}_n^\text{dg}} (\mathcal{T}_n[1],s_f)$ is $\mathbb{C}^{*} \times \mathbb{C}^*$ equivariant if and only if $f$ is an equivariant section of $\mathcal{T}_n$. It is not hard to see that the only such equivariant sections are $f(x,y) = x^Ny^M$ for some $(N,M) \in \mathbb{N}_0 \times \mathbb{N}_0$. We denote the corresponding section by $s_{N|M}$.

::: remark
In [@GORS Section 7], the differentials were parametrized by copies of the defining representation of $S_n$ in the rational Cherednik algebra, which can be considered as a noncommutative deformation of $\mathbb{C}[x_1,\ldots,x_n,y_1,\ldots,y_n]$. One can check that such a copy naturally corresponds to a section of $\mathcal{T}_n$, in particular, $f\in \mathbb{C}[x,y]$ corresponds to the subspace $\mathop{\mathrm{Span}}(f(x_i,y_i))_{1\leq i \leq n}$.
:::
