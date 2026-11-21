---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-013-6-ring-domain
section_title: "Ring domain"
section_number: 6
pages: 8-9
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.993
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
[]{#sec:ring label="sec:ring"}

Consider the TASEP on the integer ring $\mathbb{Z}_L=\mathbb{Z}/L\mathbb{Z}=\{0, 1, \cdots, L-1\}$ where we identify sites $L$ and $0$. An equivalent model is the TASEP on $\mathbb{Z}$ that is spatially periodic, which we may call the periodic TASEP.

We call $L$ the size of the ring or the period of the periodic TASEP.

<figure id="fig:Ringmaro">

<figcaption>Hydrodynamic limits of periodic height function when <span class="math inline"><em>t</em> = <em>O</em>(<em>t</em>)</span></figcaption>
</figure>

The number $N$ of particles in the TASEP on the ring is preserved.

We assume the step initial condition shown in Figure [\[fig:Ring\]](#fig:Ring){reference-type="ref" reference="fig:Ring"}. For the convenience of presentation, we assume that $L$ is an even integer and $N=L/2$ so that the particle density $\rho=N/L=1/2$. The initial height function of the periodic TASEP is the bottom curve in Figure [1](#fig:Ringmaro){reference-type="ref" reference="fig:Ringmaro"}. The other curves are the hydrodynamic limits, as time $t$ and period $L$ tend to infinity proportionally when $t/L=0.5n$ for $n=1,2, \cdots, 6$.

Consider two cases, one that $t\to\infty$ with $L$ fixed and the other that $L\to\infty$ with $t$ fixed. If $t\to\infty$ with $L$ fixed, the periodic corner growth model becomes essentially a one-dimensional growth model, and we expect that the height scales as $t^{1/2}$ and converges to the Gaussian distribution. On the other hand, if $L\to \infty$ with $t$ fixed, then the periodic TASEP becomes the usual TASEP on $\mathbb{Z}$. Thus, the height scales as $t^{1/3}$ if we let $t\to\infty$ after taking $L\to \infty$. An interesting intermediate regime is when $L, t\to\infty$ simultaneously such that $$\label{eq:relax}
    t=O(L^{3/2}).$$ Since the spatial scale for KPZ limit theorems on infinite spaces is $t^{2/3}$, we expect that the height functions at all positions on the ring of size $L$ are correlated non-trivially.

If [\[eq:relax\]](#eq:relax){reference-type="eqref" reference="eq:relax"} holds, we say that we are in the relaxation time regime.

There were some results on transition probabilities and the spectral gap of the generator in the relaxation time regime, such as [@Gwa-SpohnBethe]. However, KPZ limit theorems were obtained only recently. The paper [@Prolhac16], which is a non-completely rigorous physics paper, and [@Baik-Liu18] obtained a one-point KPZ limit theorem almost at the same time independently. This result was further extended to 2d multi-point distributions in [@Baik-Liu19; @Baik-Liu21].

::: theorem
[]{#thm:PTASEP label="thm:PTASEP"} Consider the TASEP on a ring of size $L$ with the step initial condition and extend it to the periodic TASEP.

Assume that $L$ is even and $\rho=N/L= 1/2$ for the convenience of presentation. Set $$T=L^{3/2}.$$ For $i=1, \cdots, m$, let

$(\gamma_i,  \tau_i, \mathsf{h}_i) \in \mathbb{R}\times  \mathbb{R}_+\times \mathbb{R}$ and assume that $\tau_1<\cdots< \tau_m$. Then, $$\lim_{T\to \infty} \mathrm{P}\Big( \bigcap_{i=1}^m  \big\{  \frac{\mathbf{h}(\gamma_i T^{2/3}, 2 \tau_i T) - \tau_i T}{-T^{1/3}} \le \mathsf{h}_i   \big\} \Big) 
    =   F^{\mathrm{pKPZ}}_m(\mathsf{h}; \gamma, \tau)$$ for an $m$-point distribution function $F^{\mathrm{pKPZ}}_m$ described in the next section.
:::

Like the infinite space case, we expect that the height field of the periodic models in the relaxation time regime converges to a universal field, which we may call the periodic KPZ fixed point. The function $F^{\mathrm{pKPZ}}_m$ should be the $m$-point distribution of this conjectured periodic KPZ fixed point with the (periodic) narrow wedge initial condition. It is naturally periodic with respect to $\gamma_i\mapsto \gamma_i+1$. However, unlike the KPZ fixed point, $F^{\mathrm{pKPZ}}_m$ is not invariant under the rescaling [\[eq:rescale\]](#eq:rescale){reference-type="eqref" reference="eq:rescale"}. Indeed, we conjecture that $F^{\mathrm{pKPZ}}_m$ interpolates the KPZ fixed point and one-dimensional Brownian motion. Concretely, we expect that $$\lim_{\epsilon\to 0} F^{\mathrm{pKPZ}}_m(\mathsf{h}^\epsilon; \gamma^\epsilon, \tau^\epsilon) =  F_m(\mathsf{h}; \gamma, \tau) 
     \qquad \text{where $(\mathsf{h}_i^\epsilon, \gamma_i^\epsilon, \tau_i^\epsilon) = ( (\tau_i \epsilon)^{1/3}\mathsf{h}_i, (\tau_i \epsilon)^{2/3} \gamma_i,  \tau_i \epsilon)$}$$ and $F_m$ is the $m$-point distribution of the KPZ fixed point, and that $$\lim_{s\to \infty} F^{\mathrm{pKPZ}}_m ( \mathsf{h}^s; \gamma,  \tau^s  )  = G_m(\mathsf{h}; \tau) 
    \qquad \text{where $( \mathsf{h}_i^s, \tau^s) = ( - s \tau_i + \frac{s^{1/2} \pi^{1/4} }{\sqrt{2}} \mathsf{h}_i, s \tau_i)$ }$$ and $G_m$ is the $m$-point distribution of a Brownian motion at times $\tau_1, \cdots, \tau_m$. These conjectures were proved for $m=1$ in [@Baik-Liu-Silva20], assuming $\gamma_1=0$ for the $\epsilon\to 0$ case.

Theorem [\[thm:PTASEP\]](#thm:PTASEP){reference-type="ref" reference="thm:PTASEP"} is also proved for the discrete-time TASEP on a ring [@Liao21]. However, extending the result to other integrable models is at the moment a challenge.
