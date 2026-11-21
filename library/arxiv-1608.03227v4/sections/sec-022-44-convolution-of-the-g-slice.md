---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-022-44-convolution-of-the-g-slice
section_title: "Convolution of the G-slice"
section_number: 4.4
pages: 22-23
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.982
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#ssec: Gslice label="ssec: Gslice"} As we mentioned earlier, $\MF_{B^2}(\calX_2,W)^G$ signifies $B^2$-equivariant matrix factorizations from $\MFs_{B^2}(\calX_2,W)$ that $G$-invariant. This description becomes simpler when

we introduce a smaller space $\SymbolPrint{\calX_2^\circ}:=\frg\times G\times \frb^2$ and the map $\SymbolPrint{p_\circ}: \calX_2\to \calX_2^\circ$ defined by $$p_\circ(X,g_1,Y_1,g_2,Y_2)=(\Ad_{g_1}^{-1}(X),g_{12},Y_1,\Ad_{g_{12}}(Y_2)_{++}).$$ This map is $G$-equivariant with the trivial $G$-action on the target. The space $\calX_2^\circ$ is a slice to $G$-action on $\calX_2$.

If we define the function $W$ on $\calX^\circ_2$ by $$W(X,g,Y_1,Y_2)=\Tr(X(Y_1-\Ad_g(Y_2)))$$ Then the pull back $(p_\circ)^*:\MF_{B^2}(\calX_2^\circ,W)\to \MFs_{B^2}(\calX_2,W)^G$ provides an equivalence of categories.

Indeed, we have an $G\times B^2$-equivariant isomorphism $\SymbolPrint{\Psi_G}:\calX_2\to G\times \calX_2^\circ$: $$\Psi_G(X,g_1,Y_1,g_2,Y_2)=(g_1,p_\circ(X,g_1,Y_1,g_2,Y_2)).$$ The group $G$-acts on the first factor of $G\times\calX_2^\circ$ by left multiplication and acts trivially on the second factor hence the pull-back functor $pr_2^*: \MF_{B^2}(G\times\calX_2^\circ,W)^G\to \MF_{B^2}(\calX_2^\circ,W)$ is an isomorphism. Thus the equivalence follows because $p_\circ=\Psi_G\circ pr_2$. Thus we can work with the category $\MF_{B^2}(\calX_2^\circ,W)$ instead of $\MF_{B^2}(\calX_2,W)^{G}$.

Define $\calX_3^\circ:=\frg\times G^2\times \frn^3$. The convolution for the objects of $\MFBt(\calX^\circ_2,W)$ is defined with modified maps $\SymbolPrint{\pi_{ij}^\circ}:\calX_3^\circ\to\calX_2^\circ$: $$\pi^\circ_{12}(X,g_{12},g_{23},Y_1,Y_2,Y_3)=(X,g_{12},Y_1,Y_2),$$ $$\pi^\circ_{23}(X,g_{12},g_{23},Y_1,Y_2,Y_3)=(\Ad_{g_{12}}^{-1}(X),g_{23},Y_2,Y_3),$$ $$\pi^\circ_{13}(X,g_{12},g_{23},Y_1,Y_2,Y_3)=(\Ad_{g_{13}}^{-1}(X),g_{13},Y_1,Y_3),$$ where $g_{13}=g_{12} g_{23}$. The convolution is then defined by $$\calG\star \calF=\pi^\circ_{13*}(\CE_{\frn^{(2)}}( \pi^{\circ,*}_{12}(\calF)\otimes_B\pi^{\circ,*}_{23}(\calG)))^{T^{(2)}}.$$ Obviously, the pull-back map $p_\circ^*$ is an isomorphism of the convolution algebras.
