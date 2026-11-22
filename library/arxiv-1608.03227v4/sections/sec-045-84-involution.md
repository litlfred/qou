---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-045-84-involution
section_title: "Involution"
section_number: 8.4
pages: 47-47
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.96
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
Let $w_0\in G_n$ be the longest element of the Coxeter group $S_n$: $(w_0)_{i,j}=\delta_{i+j,n+1}$. The involution $\SymbolPrint{\mathrm{D}}: G\to G$ defined by $\mathrm{D}(g)=w_0 (g^{-1})^t w_0$ preserves $B$ and the Lie version of involution $\mathrm{D}(X)=-w_0 X^t w_0$, $X\in \frg=\textup{Lie}(G)$ preserves $\frb\subset \frg$. Moreover, since $Tr(\mathrm{D}(X))=-Tr(X)$ the have automorphism of category $$\mathrm{D}:\quad \MF_{B^2}(\calX_2(G),W)\to \MF_{B^2}(\calX_2(G),W),$$ $$\mathrm{D}:\quad \MF_{B^2}(\calXr_2(G),\Wr)\to \MF_{B^2}(\calXr_2(G),\Wr).$$ The following proposition is almost tautological

::: proposition
Automorphism $\mathrm{D}$ respects convolution product: $$\mathrm{D}(\calF)\star \mathrm{D}(\calG)=\mathrm{D}(\calF\star\calG),\quad \mathrm{D}(\calF)\bar{\star} \mathrm{D}(\calG)=\mathrm{D}(\calF\bar{\star}\calG),$$ and $$\mathrm{D}(\calC^{(i)}_{\pm})=\calC^{(n-i)}_{\pm},\quad \mathrm{D}(\bcalC^{(i)}_{\pm})=\bcalC^{(n-i)}_{\pm}.$$
:::

::: proof
*Proof.* Let us show that $\mathrm{D}$ induces an automorphism of the category of matrix factorizations. We define the action on the objects as $$\calF=(M,\tilde{D},\partial_l,\partial_r)\mapsto (M,\mathrm{D}\circ \tilde{D}\circ \mathrm{ D},
    \mathrm{D}\circ \partial_l\circ \mathrm{D},\mathrm{D}\circ\partial_r\circ \mathrm{D}).$$ Since $W\circ \mathrm{D}=W$ the last formula sends objects of $\MF_{B^2}(\calX_2(G),W)$ to the objects of $\MF_{B^2}(\calX_2(G),W\circ\mathrm{D})=
  \MF_{B^2}(\calX_2(G),W)$. The action on the space of morphisms is also defined by conjugation with $\mathrm{D}$: $$Hom(\calF,\calF') \owns \Psi\mapsto \mathrm{D}\circ \Psi\circ \mathrm{D}.$$ Thus is constructed an automorphism of the category.

The induction functors $\Ind_{k,m},\ind_{k,m}$ are defined with pull-backs and push-forwards along the maps $p_{k,m},i_{k,m}$ Hence the rest of the proposition follows from the observation that $\mathrm{D}\circ i_{k,m}= i_{k',m'}\circ \mathrm{D}$, $\mathrm{D}\circ p_{k,m}= p_{k',m'}\circ \mathrm{D}$, $k'=n+1-k,m'=n+1-m$. ◻
:::
