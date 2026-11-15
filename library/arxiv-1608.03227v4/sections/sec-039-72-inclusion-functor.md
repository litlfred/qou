---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-039-72-inclusion-functor
section_title: "Inclusion functor"
section_number: 7.2
pages: 40-41
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.844
latex_coverage_ratio: 0.929
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
In the proof of proposition [\[prop: ind trans\]](#prop: ind trans){reference-type="ref" reference="prop: ind trans"} we constructed the functor $\ind_{k,m}$ and we can use this functor to define the functor: $$\SymbolPrint{\Ind_{k\dots m}}: \MF_{ B_{m-k+1}^2}(\calX_2(G_{m-k+1}),W)\to \MF_{ B_n^2}(\calX_2(G_n),W),$$ by $\SymbolPrint{\Ind_{k\dots m}}(\calF):=\ind_{k,m}(\calC_{\parallel}\boxtimes\calF\boxtimes\calC_{\parallel})$. Using Knorrer functor we also define the reduced version of the inclusion functor: $$\SymbolPrint{\Indb_{k\dots m}}: \MF_{B_{m-k+1}^2}(\calXr_2(G_{m-k+1}),\Wr)\to \MF_{B_n^2}(\calXr_2(G_n),\Wr),$$

The results of the previous section the properties of the unit immediately imply the following corollaries

::: corollary
[]{#cor: ind label="cor: ind"} The functors $\Indb_{k\dots m}$ and $\Ind_{k\dots m}$ are homomorphism of the convolution algebras.
:::

::: corollary
[]{#cor: commute non red label="cor: commute non red"}For any $k,m,k',m'$ such that $k<m<k'<m'$ and $$\calF\in \MF_{B_{m-k+1}^2}(\calX_2(G_{m-k+1}),W),$$ $$\calG\in \MF_{ B_{m'-k'+1}^2}(\calX_2(G_{m'-k'+1}),W)$$ we have $$\Ind_{k\dots m} (\calF)\star\Ind_{k'\dots m'} (\calG)=\Ind_{k'\dots m'} (\calG)\star\Ind_{k\dots m} (\calF).$$
:::

::: corollary
[]{#cor: commute label="cor: commute"}For any $k,m,k',m'$ such that $k<m<k'<m'$ and $$\calF\in \MF_{ B_{m-k+1}^2}(\calXr_2(G_{m-k+1}),\Wr),\quad
\calG\in \MF_{ B_{m'-k'+1}^2}(\calXr_2(G_{m'-k'+1}),\Wr)$$ we have $$\Indb_{k\dots m} (\calF)\bar{\star}\Indb_{k'\dots m'} (\calG)=\Indb_{k'\dots m'} (\calG)\bar{\star}\Indb_{k\dots m} (\calF).$$
:::
