---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-044-83-reduced-convolution-with-rank-1-matrix-factor
section_title: "Reduced convolution with rank 1 matrix factorizations"
section_number: 8.3
pages: 46-47
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.955
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#ssec: conv rk 1 label="ssec: conv rk 1"} The most important case of these theorems is the case $m=k+1$, that is when one of the matrix factorizations in $\bar{\star}$ product is lifted from the space $\calXr_2(G_2)$, we call such matrix factorization rank $1$ matrix factorization. In this case the pull back functor $(\bar{\pi}_{12}\times_{B_{m-k+1}}\bar{\pi}_{23})^*$ could be made very explicit. We do not provide the details of the computation, we essentially just follow the method of proposition [\[prop: Knorrer factor\]](#prop: Knorrer factor){reference-type="ref" reference="prop: Knorrer factor"}.

Let us fix notations. Let $\calF=(M_1,D_1,\partial'_l,\partial'_r)\in \MF_{B_n\times B_2}(\calXr_2(G_n),\Wr)$, $\calG=(M_2,D_2,\partial''_l,\partial''_r)\in \MF_{B_2\times B_n}(\calXr_2(G_2),\Wr)$, $B_2$ in both cases is the image of the embedding $i_{k,k+1}: B_2\to B_n$. Since the Lie algebra $\frn_2$ is one-dimensional $\frn_2=\langle e \rangle$ the corresponding $\frn_2$-equivariant structure is given by the maps the even maps $$\partial'_r\in Hom_{\CC[\calXr_2(G_n)]}(M_1, M_1), \partial''_l\in Hom_{\CC[\calXr_2(G_2)]}(M_2, M_2).$$ Respectively $$\label{eq: pi12Bpi23 1}
 (\bar{\pi}_{12}\otimes_{B_{m-k+1}}\bar{\pi}_{23})^*(\calF\boxtimes \calG)=(\bar{\pi}_{12}^*(M_1)\otimes\bar{\pi}_{23}^*(M_2),D_1+D_2;\partial'_l,\partial'_r+\partial''_l+\partial_{rl},\partial'_r),$$ where the differential $\partial_{rl}$ is given by the formula $$\label{eq: pi12Bpi23 2}
\partial_{rl}=\bar{\pi}_{12}^*\left(\frac{\partial D_1}{\partial Y_{k,k+1}}\right)(\tilde{Y}^2_{k+1,k+1}-\tilde{Y}^2_{k,k})+ \bar{\pi}_{23}^*\left(\frac{\partial D_2}{\partial X_{kk}}-\frac{\partial D_2}{\partial X_{k+1,k+1}}\right) \tilde{X}^2_{k+1,k},$$ where $\tilde{X}^2=\Ad_{g_{12}}^{-1}(X)$ and $\tilde{Y}^2=\Ad_{g_{12}}(Y)$.

In the other case $$\calF=(M_1,D_1,\partial'_l,\partial'_r)\in \MF_{B_n\times B_2}(\calXr_2(G_2),\Wr),$$ $$\calG=(M_2,D_2,\partial''_l,\partial''_r)\in \MF_{B_2\times B_n}(\calXr_2(G_n),\Wr)$$ and the expressions for $(\bar{\pi}_{12}\times_{B_{m-k+1}}\bar{\pi}_{23})^*(\calF\boxtimes \calG)$ is given by the same formulas ([\[eq: pi12Bpi23 1\]](#eq: pi12Bpi23 1){reference-type="ref" reference="eq: pi12Bpi23 1"}), ([\[eq: pi12Bpi23 2\]](#eq: pi12Bpi23 2){reference-type="ref" reference="eq: pi12Bpi23 2"}).

::: remark
As one can see, if we work with $B_2$-equivariant matrix factorizations on $Z$ with $B_2$-invariant potential then all the technicalities that are discussed in the first few sections are unnecessary since $\MFs_{B_2}^{str}(Z,F)=\MF_{B_2}(Z,F)$.
:::
