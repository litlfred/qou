---
doc_id: arxiv-1912.13486v2
doc_title: "Index for a Model of 3d-3d Correspondence for Plumbed 3-Manifolds"
section_id: sec-003-22-analysis-on-homological-block-and-index-of-le
section_title: "Analysis on homological block and index of lens space theory"
section_number: 2.2
pages: 9-10
source_pdf: 1912.13486v2.pdf
source_sha256: 9a8dbc1a143f7448
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.975
doc_brief: "Index for a Model of 3d-3d Correspondence for Plumbed 3-Manifolds — We consider the S2 ×q S1 supersymmetric index of a 3d N = 2 theory T[M3] when M3 is a plumbed 3-manifold."
---
When the 3-manifold is a lens space $M_3 = L(p,1) \simeq S^3/\mathbb{Z}_p$, the corresponding 3d $\mathcal{N}=2$ theory $T[L(p,1)]$ has been discussed in [@Gadde-Gukov-Putrov-4manifold; @Chung-Dimofte-Gukov-Sulkowski; @Gukov-Pei] and more recently in [@Gukov-Putrov-Vafa; @Gukov-Pei-Putrov-Vafa] in the context of homological blocks. Since our analysis for the plumbed 3-manifolds can be regarded as an extrapolation of this example, we study the homological block and the index of the lens space theory in detail.\
The 3d $\mathcal{N}=2$ theory $T[L(p,1), U(N)]$ (resp. $T[L(p,1), SU(N)]$) corresponding to the lens space $M_3=L(p,1)$ is given by a 3d $\mathcal{N}=2$ vector multiplet for $G=U(N)$ (resp. $SU(N)$), an adjoint chiral multiplet with $R$-charge 2 which is charged $+1$ under $U(1)_t$ global symmetry, and there is a Chern-Simons term with a level $p$.

The homological blocks for the lens space when the gauge group is $G=U(N)$ was obtained in [@Gukov-Putrov-Vafa] from the WRT invariant [@Marino2004], and it is given by $$\begin{aligned}
\widehat{Z}_b(t,q) = \frac{1}{|\mathcal{W}_b|} \frac{1}{(tq;q)_\infty^N} \oint_{|s_j|=1} \prod_{j=1}^N \frac{ds_j}{2 \pi i s_j} \prod_{1 \leq i \neq j \leq N} \frac{(s_i s_j^{-1};q)_\infty}{(s_i s_j^{-1} q t;q)_\infty} \, \Theta_b^{p \cdot \text{Id}_N}(s;q)   \label{hb-lens}
\end{aligned}$$ where $\Theta_b^{ p \cdot \text{Id}_N}(s;q)$ is the theta function for a lattice $\mathbb{Z}_N$ with a quadratic form $p \cdot \text{Id}_N$ $$\begin{aligned}
\Theta_b^{ p \cdot \text{Id}_N}(s;q) = \sum_{n \in p \mathbb{Z}^N + b} q^{\sum_{j=1}^N \frac{n_i^2}{2p}} \prod_{j=1}^N s_i^{n_i}    \,  .
\end{aligned}$$ The homological block [\[hb-lens\]](#hb-lens){reference-type="eqref" reference="hb-lens"} as the $D^2 \times_q S^1$ partition function can be obtained from the vector multiplet $V_N$ with the Neumann boundary condition [\[vec-loc1\]](#vec-loc1){reference-type="eqref" reference="vec-loc1"} and the adjoint chiral multiplet $\Phi_{R=2,N}^+$ whose $R$ charge is 2 and $U(1)_t$ charge is $+1$ also with the Neumann boundary condition [\[adj-loc-N\]](#adj-loc-N){reference-type="eqref" reference="adj-loc-N"}. $\Theta_a^{ p \cdot \text{Id}_N}(s;q)$ is interpreted as the contribution from the boundary degrees of freedom that cancel the anomaly inflow from the CS term whose level is $p$, which we don't know how to derive from the Lagrangian description of the $\mathcal{N}=(0,2)$ boundary theory. Also, there would be an extra factor $\prod_{1 \leq i,j \leq N} \theta((-q^{\frac{1}{2}})^{1-R} v^{-1})^{1/2}$ in the calculation, which captures information of the background CS contributions for $U(1)_t$ symmetry and $U(1)_R$ symmetry at the level of the index. If we would like to cancel the background CS contributions, this theta function (or an equivalent term up to theta function ambiguity) needs to be included in [\[hb-lens\]](#hb-lens){reference-type="eqref" reference="hb-lens"} because $q$-Pochhammer symbols have $-\frac{1}{2}$ background CS levels. But we may ignore this contribution in the calculation of homological block because it gives just an overall factor. Then we obtain [\[hb-lens\]](#hb-lens){reference-type="eqref" reference="hb-lens"}.

The unrefined limit $t=1$ of the homological block [\[hb-lens\]](#hb-lens){reference-type="eqref" reference="hb-lens"} is $$\begin{aligned}
\widehat{Z}_b(q) = \frac{\widehat{Z}_b(t,q)}{(tq;q)_\infty^N} \bigg|_{t \rightarrow 1} = \frac{1}{|\mathcal{W}_b|} \oint_{|s_i|=1} \prod_{j=1}^N \frac{d s_j}{2 \pi i z_j} \prod_{1 \leq i \neq j \leq N} (1-s_i s_j^{-1}) \, \Theta_b^{p \cdot \text{Id}_N}(s;q)   \,  .
\end{aligned}$$\

The index of $T[L(p,1), U(N)]$ is $$\begin{aligned}
\begin{split}
\mathcal{I}_{U(N)} = &\sum_{m_1 \geq \cdots \geq m_N \in \mathbb{Z}} \frac{1}{|\mathcal{W}_{\mathbf{m}}|} \oint_{|z_i|=1} \prod_{j=1}^N \frac{d z_j}{2 \pi i z_j} \,
I_{\text{CS}} \, I_{\text{vect}}(z,m,q) \, I_{\text{adj}}(z,m,t,R,q)
\end{split} \\
\begin{split}
&=\sum_{m_1 \geq \cdots \geq m_N \in \mathbb{Z}} \frac{1}{|\mathcal{W}_{\mathbf{m}}|} \oint_{|z_i|=1} \prod_{j=1}^N \frac{d z_j}{2 \pi i z_j}
\prod_{j=1}^N z_i^{pm_j}        \\
&\hspace{5mm} \times \prod_{1 \leq i \neq j \leq N} t^{-|m_i-m_j|/2} (-1)^{|m_i-m_j|/2} q^{-R |m_i-m_j|/4} ( 1 - q^{|m_i - m_j |/2} z_i z_j^{-1} )  \\
&\hspace{5mm} \times \prod_{1 \leq i \neq j \leq N} \frac{(z_i^{-1} z_j t^{-1} q^{|m_i-m_j|/2+1-R/2};q)_\infty}{(z_i z_j^{-1} t q^{|m_i-m_j|/2+R/2};q)_\infty}
\bigg( \frac{(t^{-1}q^{1-R/2};q)_\infty}{(t q^{R/2};q)_\infty} \bigg)^N \,  ,
\end{split}
\end{aligned}$$ which is obtained from [\[sci-vect\]](#sci-vect){reference-type="eqref" reference="sci-vect"} and [\[sci-adj\]](#sci-adj){reference-type="eqref" reference="sci-adj"} with $R=2$. When $G=SU(N)$, $\sum_{j=1}^N m_j=0$ and $\prod_{j=1}^N z_j=1$ are imposed and the contribution from the Cartan part of the adjoint chiral multiplet is $\big( (t^{-1}q^{1-R/2};q)_\infty / (t q^{R/2};q)_\infty \big)^{N-1}$. In particular, when $G=SU(2)$, we have $$\begin{aligned}
\begin{split}
\mathcal{I}_{SU(2)} &= \frac{1}{2} \sum_{m \in \mathbb{Z}}\oint_{|z|=1} \frac{dz}{2 \pi i z} z^{2pm} 
t^{-|2m|} q^{-|2m|} ( 1 - q^{|m|} z^2 ) ( 1 - q^{|m|} z^{-2} )  \\  
&\hspace{10mm} \times \frac{(z^2 t^{-1} q^{|m|+1-R/2};q)_\infty}{(z^2 t q^{|m|+R/2};q)_\infty} \frac{(z^{-2} t^{-1} q^{|m|+1-R/2};q)_\infty}{(z^{-2} t q^{|m|+R/2};q)_\infty}
\bigg( \frac{(t^{-1}q^{1-R/2};q)_\infty}{(t q^{R/2};q)_\infty} \bigg)   \label{lens-sci-su2}
\end{split}
\end{aligned}$$ with $R=2$. The $G=SU(2)$ case was studied in the context of homological block in [@Gukov-Pei-Putrov-Vafa]. More specifically, it was checked that $\mathcal{I}_{SU(2)} = \sum_{b} |\mathcal{W}_b| \widehat{Z}_b(q,v) \widehat{Z}_b(\tilde{q},v^{-1})$ where $\tilde{q}=q^{-1}$, $v=t$, and $\tilde{v}=t^{-1}$ as before. The index [\[lens-sci-su2\]](#lens-sci-su2){reference-type="eqref" reference="lens-sci-su2"} can also be obtained via [\[id-fusion\]](#id-fusion){reference-type="eqref" reference="id-fusion"}. From these calculations we see that the CS contribution to the index comes only from the theta function $\Theta_b^{p \cdot \text{Id}_N}(s;q)$.
