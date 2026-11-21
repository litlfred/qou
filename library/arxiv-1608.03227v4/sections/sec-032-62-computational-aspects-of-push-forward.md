---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-032-62-computational-aspects-of-push-forward
section_title: "Computational aspects of push-forward"
section_number: 6.2
pages: 32-33
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.99
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#ssec: comp ins label="ssec: comp ins"} In our general construction of the push forward $i_{k*}(\calF)$, $\calF=(M,D,d_l,d_r)$ we make a choice of the extension $\tilde{D}$ of the differential $D$ from sub-variety $\calX^\circ_2(P_k)$ to $\calX^\circ_2(G_n)$. However in our case we have a canonical choice of the extension because we could use the projection map $\Lie(G_n)\to \Lie(P_{k})$ to construct such an extension and use the remark [\[rem: section\]](#rem: section){reference-type="ref" reference="rem: section"}, the details are provided below. Morally, we would like to interpret $i_{k}$ as a section of some map and it is possible if we enlarge our space slightly.

In this subsection we use notation $\adj(A)$ for the adjoint of matrix $A$. Let us introduce space $\SymbolPrint{\calX^\circ_2(G_n)^\flat}:=\frg_n\times \Lie(G_n) \times \frn_n^{2}$. There is a natural embedding $$j_n: \calX_2^\circ(G_n)\to \calX_2^\circ(G_n)^\flat$$ induced by the embedding $G_n\to \mathfrak{gl}_n$. If we define $$W^\flat(X,g,Y_1,Y_2)=
\Tr(X( Y_1\det- gY_2\adj(g))),\quad \det=\det(g)$$ then we have $j^*_n(W\cdot\det)=W^\flat$ and the map $$j^*_n: \MF_{B^2_n}(\calX_2^\circ(G_n)^\flat,W^\flat)\to \MF_{B^2_n}(\calX_2^\circ(G_n)^\flat,W'),$$ where $W'=W\cdot\det$, is well defined.

Similarly, we define $\calX^\circ_2(P_k)^\flat$ and $\calXr^\circ_2(P_k)^\flat$. The natural map $$\SymbolPrint{j^k_n}: \calX^\circ_2(P_k)\to \calX^\circ_2(P_k)^\flat$$ induces the pull back map $$j^{k*}_{n}: \MF_{B^2}(\calX^\circ_2(P_k)^\flat,W^\flat)\to \MF_{B^2}(\calX^\circ_2(P_k),W').$$

Since $W'$ and $W$ differ by the non-vanishing factor $\det$, there is an embedding of categories $\det: \MF_{B^2}(\calX^{\circ}_2,W)\rightarrow\MF_{B^2}(\calX^{\circ}_2,W')$: $$\det: [M_0\xrightarrow{D_0} M_1\xrightarrow{D_1} M_1]\mapsto [M_0\xrightarrow{D_0\cdot \det} M_1\xrightarrow{D_1}M_0].$$ We the inverse functor we denote by $\det^{-1}$ and we use the same notation for the functors between the categories related to the parabolic versions of the categories.

There is no natural map between $\calX^\circ_2(G_n)$ and $\calX^\circ_2(P_k)$ but there is a natural linear projection $\SymbolPrint{\rho_k}: \calX^\circ_2(G_n)^\flat\to
\calX_2^\circ(P_k)^\flat$ and there is a pull back map $$\rho_k^*: \MF(\calX_2^\circ(P_k)^\flat,W^\flat)\to \MF(\calX_2^\circ(G_n)^\flat,\rho_k^*(W^\flat)).$$

There is also a natural inclusion map $i_k: \calX^\circ_2(P_k)^\flat\to \calX^\circ_2(G_n)^\flat$ which is a section of the projection $\rho_k$: $\rho_k\circ i_{k}=id$.

Hence there is $\calF'\in \MF_{B^2_n}(\calX^\circ_2(P_k)^\flat,W^\flat)$ such that $j^{k*}_n(\calF')=\det(\calF)$ and we define $$\tilde{\calF}=(\tilde{M},\tilde{D},\tilde{\partial}_l,\tilde{\partial}):=\mathrm{det}^{-1}\circ j^{*}_n\circ \rho_k^*(\calF')\in \MF(\calX^\circ_2(G_n),j_n^{*}\circ{\rho}_{k}^*(W^\flat)\cdot\mathrm{det}^{-1}).$$

By construction we have $\tilde{\calF}|_{\calX^\circ_2(P_k)}=\calF$. Thus the matrix factorization $\tilde{\calF}$ provides the first step of the construction of the push forward $i_{k*}(\calF)$ from section [\[ssec: eq push f\]](#ssec: eq push f){reference-type="ref" reference="ssec: eq push f"}. By completing the second step of the construction from the section [\[ssec: eq push f\]](#ssec: eq push f){reference-type="ref" reference="ssec: eq push f"} we obtain the matrix factorization:

$$i_{k*}(\calF)=(\tilde{M},d_K+\tilde{D}+d^-,\partial_l,\partial_r),$$ where $d_K: \tilde{M}\otimes \Lambda^{\bullet} V\to \tilde{M}\otimes \Lambda^{\bullet-1} V$ is the Koszul differential for the defining ideal of $\calX_2^\circ(P_k)\subset \calX_2^\circ(G_n)$ and $d^-=\sum_{i<j} d^-_{ij}$, $d^-_{ij}:\tilde{M}\otimes\Lambda^i V\to \tilde{M}\otimes \Lambda^{j} V$ is the complementary differential: $(d_k+\tilde{D}+d^-)^2=\Wr$

Note that because of our choice of extension $\tilde{\calF}$ the differentials $d^-_{ij}$ vanish unless $j=i+1$, we give more details below. Define a linear operator operator $\Pi^k_{+}:\frg_n\to \mathfrak{p}_k$ which is a natural projection. Respectively, we have $\Pi_{--}^k(A)=A-\Pi_+^{k}(A)$. The difference $\delta_kW:=W-j_n^*\circ\rho_n^{k*}(W^\flat)\cdot \det^{-1}$ could be written as sum of two terms: $$\delta_kW_1:=\Tr(\Pi_{--}^k(X)\cdot \Pi_{++}^k(Y_1-\Ad_{g_{12}}(Y_2))),$$ $$\delta_kW_2:=\Tr(\Pi_+^k(X)\cdot
\Pi^k_{-}(\Ad_{g_{12}}(Y_2)-\rho_k(g_{12})(Y_2)\adj(\rho_k(g_{12}))\det(g_{12})^{-1}  ),$$ where we use convention $\mathrm{Id}=\Pi^k_{-}+\Pi^k_{++}$.

Since $\delta_k W_1\in (\Pi^k_{--}(X))$ and $\delta_kW_2\in (\Pi^k_{--}(g_{12}))$ we have $$i_{k*}(\calF)^\sharp=\tilde{\calF}\otimes [\Pi_{--}^k(X), \Pi_{++}^k(Y_1-\Ad_{g_{12}}(Y_2))]\otimes  \mathrm{K}^{\delta_k W_2} (\Pi_{--}^{k}(g_{12})).$$ That is the differentials $d_{ij}^-$ are the negative differentials of the Koszul matrix factorization and hence have above mentioned property.
