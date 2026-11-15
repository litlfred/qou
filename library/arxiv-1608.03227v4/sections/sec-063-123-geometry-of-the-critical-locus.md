---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-063-123-geometry-of-the-critical-locus
section_title: "Geometry of the critical locus"
section_number: 12.3
pages: 68-69
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.961
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
Before we describe the last step of our construction of the knot invariant let us discuss the structure of the scheme $\SymbolPrint{\calX^{crit}_\ell}:=\Spec(R_\ell)$. First, we describe a particular set of generators of the ideal $\Icr_\ell$. Let us notice that we can rewrite the intermediate potential $W_{i,i+1}$ as follows $$\label{eq: two forms of crit}
\SymbolPrint{W_{i,i+1}}= \Tr(\Ad^{-1}_{g_i}(X)Y_i-\Ad^{-1}_{g_{i+1}}(X)Y_{i+1})$$

As we explain in the section [\[sec: Knor\]](#sec: Knor){reference-type="ref" reference="sec: Knor"} the potential $W_{i,i+1}$ could be rewritten as follows: $$\Tr(\tilde{X}_{i,+}\Ad_{g_{i,i+1}}(Y_{i+1}))-\Tr(\tilde{X}_{i,--}(Y_{i}-\Ad_{g_{i,i+1}}(Y_{i+1})_{++})).$$

Here and everywhere below the notations are consistent with the notations of section [\[sec: Knor\]](#sec: Knor){reference-type="ref" reference="sec: Knor"}, that is $M_+$ ($M_-$) is the upper-triangular (lower-triangular) part of a matrix $M$ and $M_{++}$ ($M_{--}$) is the strictly upper-triangular (lower-triangular) part of $M$ and $$g_{i,i+1}=g_{i}^{-1}g_{i+1},\quad \tilde{X}_{i}=\Ad_{g_{i}}^{-1}(X).$$ Taking partial derivatives of the last function with respect to the coordinates $Y_{i+1}$, $\tilde{X}_{i,+}$, $g$, $Y_{i}-\Ad_{g_{i,i+1}}(Y_{i+1})_{++},\tilde{X}_{i,--}$ we obtain equations: $$\begin{gathered}
\label{eq: part ders}
\Ad^{-1}_{g_{i,i+1}}(\tilde{X}_{i})_{--}=0,\\
\Ad_{g_{i,i+1}}(Y_{i+1})_{-}=0,\label{eq: Y neg}\\
 [\Ad_{g_{i,i+1}}(Y_{i+1}),\tilde{X}_{i,+}]=0,\\
 \tilde{X}_{i,--}=0,\\
  Y_{i}=\Ad_{g_{i,i+1}}(Y_{i+1})_{++}.\label{eq: Yi Yi+1}
 
\end{gathered}$$ Let us notice that the last equations the first and the second lines actually imply: $$\label{eq: flag comm}
  [Y_{i},\tilde{X}_{i,+}]=0,$$ since $[\Ad_{g_{i,i+1}}(Y_{i+1}),\tilde{X}_{i,+}]=[\Ad_{g_{i,i+1}}(Y_{i+1})_{++},\tilde{X}_{i,+}]+[\Ad_{g_{i,i+1}}(Y_{i+1})_{-},\tilde{X}_{i,+}]$.

On the other hand if we compute the partial derivatives by $X$ of the LHS of ([\[eq: two forms of crit\]](#eq: two forms of crit){reference-type="ref" reference="eq: two forms of crit"}) we get $$\label{eq: AdAd}
 \Ad_{g_i}(Y_i)=\Ad_{g_{i+1}}( Y_{i+1})$$

Finally let us notice that the ([\[eq: part ders\]](#eq: part ders){reference-type="ref" reference="eq: part ders"}) and ([\[eq: flag comm\]](#eq: flag comm){reference-type="ref" reference="eq: flag comm"}) imply that $[Y_{i+1},\tilde{X}_{i+1}]=0$ and hence $$\label{eq: comm}
 [\Ad_{g_i}Y_i,X]=0.$$ Let us notice that because of the previous observation ([\[eq: AdAd\]](#eq: AdAd){reference-type="ref" reference="eq: AdAd"}), the last equations ([\[eq: comm\]](#eq: comm){reference-type="ref" reference="eq: comm"}) are equivalent for different values of $i$.

Thus we see that the $G\times B^{\ell}$ equivariant scheme $\calX_\ell^{crit}$ comes equipped with the following maps: $$pr_{i}: \calX_\ell^{crit}\to \mathcal{CV}_{\frb\times\frn}, \quad pr_i(g_\bullet,X,Y_\bullet)=(Y_i,\tilde{X}_{i,+}),$$ this map is $B$-equivariant; $$pr:\calX_\ell^{crit}\to \mathcal{CV}_{\frg\times\frg}, \quad pr(g_\bullet,X,Y_\bullet)=(\Ad_{g_i}(Y_i),X),$$ this map is $G$-equivariant. The varieties $\mathcal{CV}_B$ and $\mathcal{CV}_G$ are the commuting sub varieties of $\frn\times\frb$ and $\frg\times\frg$ respectively.

::: proposition
The critical locus $\calX^{crit}_\ell$ consists of elements $(X,g_1,Y_1,\dots,g_\ell,Y_\ell)$ satisfying $$\begin{gathered}
 \Ad_{g_i}(Y_i)=\Ad_{g_{i+1}}(Y_{i+1})\\
 \Ad_{g_i}^{-1}(X)_{--}=0\\
 [X,\Ad_{g_1}(Y_1)]=0.
 
\end{gathered}$$
:::
