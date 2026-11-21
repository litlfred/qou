---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-043-82-reduced-case-version-of-the-auxiliary-lemma
section_title: "Reduced case version of the auxiliary lemma"
section_number: 8.2
pages: 45-46
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.938
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
Let us introduce $$\SymbolPrint{\calXr^{\circ}_2(G_{k\dots m})}=\frb\times G_{k\dots m} \times \frn^2,$$ $$\SymbolPrint{\calXr_3(G_n,G_{k\dots m})}:=\frb_n\times G_n\times G_{m-k+1}\times \frn_n.$$ Let us also define an embedding $\SymbolPrint{\bar{i}_{k\dots m}}:\calXr_3(G_n,G_{k\dots m})\to \calXr_3$ by $$\bar{i}_{k\dots m}(X,g_{12},g_{23},Y)=(X,g_{12},i_{k\dots m}(g_{23}),Y).$$ Using the last embedding we define the maps $\SymbolPrint{\bar{\pi}_{ij}}$ by restricting from the ambient $\calX_3$: $$\bar{\pi}_{12},\bar{\pi}_{13}: \calXr_3(G_n,G_{k\dots m})\to \calXr_2(G_n),\quad \bar{\pi}_{23}: \calXr_3(G_n,G_{k\dots m})\to \calXr_2(G_{k\dots m}).$$

Similarly, we define $\calXr_3(G_{k\dots m},G_n)$ together with the embedding $\bar{i}_{k\dots m}: \calXr_3(G_{k\dots m}, G_n)\to \calX_3$: $$\bar{i}_{k\dots m}(X,g_{12},g_{23},Y)=(X,i_{k\dots m}(g_{12}),g_{23},Y).$$ The same way as before we define the corresponding maps $\bar{\pi}_{ij}$.

The spaces $\calXr_3(G_{k\dots m},G_n)$ and $\calXr_3(G_n,G_{k\dots m})$ have natural $B_n\times B_{m-k+1}\times B_n$-equivariant structure. Moreover, the maps $\bar{\pi}_{ij}$ are $B_n^2$-equivariant but not $B_{m-k+1}$-equivariant. However, we can introduce the $B_n\times B_{m-k+1}\times B_n$-equivariant structure on the pull-back $(\bar{\pi}_{12}\times \bar{\pi}_{23})(\calF\otimes\calG)$ where $\calF,\calG$ are equivariant matrix factorizations from the appropriate spaces. More precisely, repeating the argument of the proposition [\[prop: Knorrer factor\]](#prop: Knorrer factor){reference-type="ref" reference="prop: Knorrer factor"} we obtain

::: proposition
[]{#prop: small prod 1 label="prop: small prod 1"} Let $$\calF\in \MF_{B_n^2}(\calXr_2(G_n),\Wr), \quad\calG\in \MF_{B_{m-k+1}^2}(\calXr_2(G_{m-k+1}),\Wr)$$ then there is a unique matrix factorization $$(\bar{\pi}_{12}\otimes_{B_{m-k+1}}\bar{\pi}_{23})^*(\calF\boxtimes \calG)\in \MF_{B_n\times B_{m-k+1}\times B_n}(\calXr_3(G_n,G_{m\dots k}),\bar{\pi}_{13}^*(\Wr)),$$ such that its $B_n^2$-equivariant specialization has properties: $$(\bar{\pi}_{12}\otimes_{B_{m-k+1}}\bar{\pi}_{23})^*(\calF\boxtimes \calG)^\sharp=(\bar{\pi}_{12}\times\bar{\pi}_{23})^*(\calF\boxtimes \calG),$$ and $$\CE_{\frn_{m-k+1}}(\pi_{13*}((\bar{\pi}_{12}\otimes_{B_{m-k+1}}\bar{\pi}_{23})^*(\calF\boxtimes \calG)))^{T_{m-k+1}^{(2)}}=\calF\bar{\star}\Indb_{k\dots m}(\calG).$$
:::

::: lemma
[]{#prop: small prod 2 label="prop: small prod 2"} Let $$\calF\in \MF_{B_{m-k+1}^2}(\calXr_2(G_{m-k+1}),\Wr),\quad\calG\in \MF_{B_{m-k+1}^2}(\calXr_2(G_n),\Wr)$$ then there is a unique matrix factorization $$(\bar{\pi}_{12}\otimes_{B_{m-k+1}}\bar{\pi}_{23})^*(\calF\boxtimes \calG)\in \MF_{B_n\times B_{m-k+1}\times B_n}(\calXr_3(G_{m\dots k},G_n),\bar{\pi}_{13}^*(\Wr)),$$ such that its $B_n^2$ limit has properties: $$(\bar{\pi}_{12}\otimes_{B_{m-k+1}}\bar{\pi}_{23})^*(\calF\boxtimes \calG)^\sharp=(\bar{\pi}_{12}\times\bar{\pi}_{23})^*(\calF\boxtimes \calG),$$ and $$\CE_{\frn_{m-k+1}}(\pi_{13*}((\bar{\pi}_{12}\otimes_{B_{m-k+1}}\bar{\pi}_{23})^*(\calF\boxtimes \calG)))^{T_{m-k+1}^{(2)}}=\Indb_{k\dots m}(\calF)\bar{\star}\calG.$$
:::
