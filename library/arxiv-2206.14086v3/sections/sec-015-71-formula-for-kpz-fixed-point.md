---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-015-71-formula-for-kpz-fixed-point
section_title: "Formula for KPZ fixed point"
section_number: 7.1
pages: 9-10
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.72
latex_coverage_ratio: 0.981
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
Let $F_m$ be the $m$-point distribution of the KPZ fixed point with the narrow wedge initial condition. The result of [@Liu19] implies that $$\label{eq:KPZformula}
    F_m(\mathsf{h}; \gamma, \tau) 
    = \frac1{(2\pi \mathrm{i})^{m-1}} \oint \cdots \oint  \frac{\det( \mathsf{1}- \mathsf{K}_\zeta)}{\zeta_1(1-\zeta_1) \cdots \zeta_{m-1} (1-\zeta_{m-1})} \mathrm{d}\zeta_1 \cdots \mathrm{d}\zeta_{m-1}$$ where $\zeta=(\zeta_1, \cdots, \zeta_{m-1})$, and the contours are nested circles of radii less than $1$ centered at the origin. The operator $\mathsf{K}_\zeta$ acts on $L^2(\Sigma)$, where $\Sigma$ is the union of $4m-2$ contours in Figure [\[fig:KPZcontour\]](#fig:KPZcontour){reference-type="ref" reference="fig:KPZcontour"} that extend to infinity with angle $\pi/5$ from the $x$-axis. The kernel of $\mathsf{K}_\zeta$ can be written [@Baik-Prokhorov-Silva21] as a simple conjugation of the kernel $$\label{eq:kpzKkernel}
    \mathsf{K}^{\mathrm{conj}}_\zeta(u, v) = \frac{\mathsf{a}(u)^T \mathsf{D}(u)^T \mathsf{D}(v) \mathsf{b}( v)}{u-v}, \qquad u, v\in \Sigma,$$ which is zero for $u=v$. The $(m+1)\times (m+1)$ matrix $$\mathsf{D}(z)= \mathrm{diag}\big( e^{- \frac{1}{3} \tau_1 z^3+ \frac{1}{2} \gamma_1 z^2 + \mathsf{h}_1 z}, \cdots, e^{- \frac{1}{3} \tau_m z^3 + \frac{1}{2} \gamma_m z^2 + \mathsf{h}_m z}, 1 \big) .$$ The $(m+1)\times 1$ vectors $\mathsf{a}(z)$ and $\mathsf{b}(z)$ are simple and explicit, and they do not depend on $\mathsf{h}_i, \gamma_i, \tau_i$.

Note that the exponent $- \frac{1}{3} \tau_i z^3+ \frac{1}{2} \gamma_i z^2+ \mathsf{h}_i z$ in $\mathsf{D}(z)$ is unchanged if we rescale as [\[eq:rescale\]](#eq:rescale){reference-type="eqref" reference="eq:rescale"} and $z\mapsto \alpha^{-1} z$. This is consistent with the rescaling property of the KPZ fixed point.

<figure id="fig:periodicKPZset">

<figcaption>The space <span class="math inline">S</span> for periodic KPZ fixed when <span class="math inline"><em>m</em> = 3</span>.</figcaption>
</figure>
