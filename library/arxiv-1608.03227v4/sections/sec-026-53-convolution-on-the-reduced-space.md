---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-026-53-convolution-on-the-reduced-space
section_title: "Convolution on the reduced space"
section_number: 5.3
pages: 26-26
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.943
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
In order to define the convolution on the smaller space $\calXr_2$, consider

the space $\SymbolPrint{\calXr_3}:=\frb\times G^2\times\frn$ with the following $B^3$-action $$(b_1,b_2,b_3)\cdot (X,g_{12},g_{23},Y)=(\Ad_{b_1}(X),b_1 g_{12} b_2^{-1}, b_2 g_{23} b_3^{-1}, \Ad_{b_3}(Y)).$$ There are the following

maps $\SymbolPrint{\bar{\pi}_{ij}}:\calXr_3\to\calXr_2$: $$\bar{\pi}_{12}(X,g_{12},g_{13},Y)=(X,g_{12},\Ad_{g_{23}}(Y)_{++}),$$ $$\bar{\pi}_{23}(X,g_{12},g_{13},Y)=(\Ad_{g_{12}}^{-1}(X)_+,g_{23},Y),$$ $$\bar{\pi}_{13}(X,g_{12},g_{13},Y)=(X,g_{12}g_{23},Y).$$

::: proposition
$\bar{\pi}_{12}^*(\Wr)+\bar{\pi}_{23}^*(\Wr)=\bar{\pi}_{13}^*(\Wr)$.
:::

::: proof
*Proof.* Indeed we have $$\begin{gathered}
\bar{\pi}_{12}^*(\Wr)+\bar{\pi}_{23}^*(\Wr)=\Tr(X\Ad_{g_{12}}(\Ad_{g_{23}}(Y)_{++}))+\Tr(\Ad_{g_{12}}^{-1}(X)_+\Ad_{g_{23}}(Y))=\\
\Tr(\Ad^{-1}_{g_{12}}(X)\Ad_{g_{23}}(Y)_{++})+\Tr(\Ad^{-1}_{g_{12}}(X)_+\Ad_{g_{23}}(Y)).
\end{gathered}$$ Thus the statement follows is implied by $$\begin{gathered}
 \Tr(A B_{++})+\Tr(A_+B)=\Tr(AB)-\Tr(AB_-)+\Tr(A_+B_-)\\
  =\Tr(AB)+\Tr(A_-B_-)=\Tr(AB).
\end{gathered}$$ ◻
:::

For given $\calF,\calG\in \MF_{B\times B}(\calXr_2,W)$ it is tempting to define $$\label{eq: red convolution prelim}
\calF\SymbolPrint{\bar{\star}}\calG:=\bar{\pi}_{13*}(\CE_{\frn^{(2)}}( \bar{\pi}_{12}^*(\calF)\otimes\bar{\pi}_{23}^*(\calG))))^{T^{(2)}},$$ where $\frn^{(2)}$, $T^{(2)}$ are the subalgebras of the middle factor in $\frb^3$ acting on $\calXr_3$. The only issue with this definition is that the maps $\bar{\pi}_{12}$ and $\bar{\pi}_{23}$ are not $B^3$ equivariant. Thus we have to define the $B^3$-equivariant structure on the pull back $\bar{\pi}_{12}^*(\calF)\otimes\bar{\pi}_{23}^*(\calG)$ and we do it below.
