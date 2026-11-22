---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-030-6-induction-functors
section_title: "Induction functors"
section_number: 6
pages: 31-31
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.935
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#sec: inc label="sec: inc"}

The main goal of this section is to construct induction functors: $$\SymbolPrint{\ind_k}: \MF_{B_k^2}(\calX_2^\circ(G_k),W)\times \MF_{B_{n-k}^2}(\calX^\circ_2(G_{n-k}),W)\to \MF_{B_n^2}(\calX_2^\circ(G_n),W),$$ $$\SymbolPrint{\indb_k}: \MF_{B_k^2}(\calXr_2(G_k),\Wr)\times \MF_{B_{n-k}^2}(\calXr_2(G_{n-k}),\Wr)\to \MF_{B_n^2}(\calXr_2 (G_n),\Wr).$$ and to show that these functors are intertwined by the Knorrer functors.

::: proposition
[]{#prop: ind phi label="prop: ind phi"} We have $$\ind_k\circ (\Phi_k\times \Phi_{n-k} ) =\Phi_n\circ \ind_k.$$
:::

We also show that the induction functor is the convolution algebra homomorphism.

::: proposition
[]{#prop: ind homo label="prop: ind homo"} For any $$\calF_1,\calG_1\in \MF_{B_k^2}(\calX^\circ_2(G_k),W), \quad \calF_2,\calG_2\in \MF_{B_{n-k}^2}(\calX^\circ_2(G_{n-k}),W).$$ We have $$\ind_k(\calF_1,\calF_2)\star\ind_{k}(\calG_1,\calG_2)=\ind_k(\calF_1\star\calG_1,\calG_1\star\calG_2).$$
:::

Finally, we define the generators of the braid group on two strands and using the induction functor explain how we construct the generators for the braid group on arbitrary number of strands.
