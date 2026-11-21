---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-006-221-mayer-vietoris
section_title: "Mayer-Vietoris"
section_number: 2.2.1
pages: 8-8
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 1.0
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
Let $K$ be a CW-complex, with subcomplexes $K_1,\ K_2\subset K$ so that $K=K_1\cup K_2$. Let $\rho\colon\pi_1K\to \mathrm{SL}_n(F)$ be a representation. Consider the diagram of inclusions $$\xymatrix{
K_1\cap K_2
\ar[d]^{i_2}
\ar[r]^{i_1} & K_1 \ar[d]^{j_1} \\ 
K_2 \ar[r]^{j_2}  & K.
}$$ There is a Mayer-Vietoris exact sequence in homology with twisted coefficients, if the representations on $\pi_1K_1$, $\pi_1K_ 2$ and $\pi_1L$ are the restrictions: $$\begin{gathered}
 \label{eqn:MV}
  \cdots  \to \bigoplus_L H_i(L;\rho) \xrightarrow{i_{1*}\oplus i_{2*}}  
H_i(K_1;\rho)\oplus H_i( K_2;\rho)
  \xrightarrow{j_{1*}-j_{2*}}  H_i(K;\rho)  \\
 \to \bigoplus_L  H_{i-1}(L;\rho)\to\cdots
 
\end{gathered}$$ where $L$ runs on the connected components of $K_1\cap K_2$. Notice that different choices of base-points yield canonical isomorphisms between the homology groups, hence we can consider $K_1\cap K_2$ not connected,

Choose a basis for each of these cohomology groups $h_*$ for $H_*(K;\rho)$, $h_{1*}$ for $H_*(K_1;\rho)$, $h_{2*}$ for $H_*(K_2;\rho)$, and $h_{L*}$ for $H_*(L ;\rho)$. The long exact sequence [\[eqn:MV\]](#eqn:MV){reference-type="eqref" reference="eqn:MV"} is viewed as a complex. Its torsion is denoted by $\operatorname{tor}
(\mathcal H, h_{**})$.

::: prop
[]{#prop:MV label="prop:MV"} Let $K$ be a CW-complex, with subcomplexes $K_1\cap K_2$ so that $K=K_1\cup 
K_2$. Let $\rho\colon\pi_1K\to \mathrm{SL}_n(F)$ be a representation and choose basis in homology. Then $$\operatorname{tor}(K, h_*;\rho)=\frac{\operatorname{tor}(K_1,h_{1*};\rho)\operatorname{tor}(K_2,h_{2*};\rho) 
}{\prod\limits_L\operatorname{tor}(L,h_{L*};\rho) \operatorname{tor}(\mathcal H, h_{**}) }$$ where $L$ runs on the connected components of $K_1\cap K_2$.
:::

This is used in surgery formulas (e.g. Proposition [\[prop:SF\]](#prop:SF){reference-type="ref" reference="prop:SF"}) or for the mapping torus (Proposition [\[prop:MapTorus\]](#prop:MapTorus){reference-type="ref" reference="prop:MapTorus"}). The proof can be found in [@Milnor66] or in [@Memoirs Section 0.4].
