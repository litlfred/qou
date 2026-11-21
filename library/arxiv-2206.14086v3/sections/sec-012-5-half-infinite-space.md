---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-012-5-half-infinite-space
section_title: "Half-infinite space"
section_number: 5
pages: 7-8
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.932
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
[]{#sec:half label="sec:half"}

We discussed so far models on infinite spaces. For example, the TASEP was defined on $\mathbb{Z}$. In this and the following sections, we consider different domains and their effects on the limit.

Consider the TASEP on the half-infinite space $\mathbb{Z}_+\cup\{0\}$. We introduce a parameter $\alpha>0$ representing the injection rate at site $0$: if the origin is empty, a new particle is injected with rate $\alpha$. Once injected, particles follow the usual TASEP rule. Suppose that we start with the empty configuration. If we could inject particles freely without being blocked by existing particles in the domain, then the height function at the origin would satisfy $\mathbf{h}(0,T)/T\to 2\alpha$ in probability as $T\to \infty$.

However, due to the particles already in the domain, the height grows at a slower rate, and the hydrodynamic limit at the origin turns out to be $$\frac{\mathbf{h}(0, T)}{T} \to \max \big\{ 2\alpha(1-\alpha), \frac{1}{2} \big\},$$ showing that the effective injection rate is $\max\{ \alpha(1-\alpha), 1/4\}$. The formula changes at $\alpha=1/2$.

The papers [@Baik-Rains01a; @Baik-Rains01] obtained a one-point KPZ limit theorem at the origin for the Poisson PNG and discrete-time TASEP models. The height scales as $T^{1/3}$ for $\alpha\ge 1/2$ and as $T^{1/2}$ for $\alpha<1/2$. The limiting distribution is a variation of the Tracy-Widom distribution for $\alpha>1/2$, another variation for $\alpha=1/2$, and the Gaussian distribution for $\alpha<1/2$. The result is extended to general positions and equal-time, multi-position distributions in [@Sasamoto-Imamura04; @Baik-Barraquand-Corwin-Suidan18] for the Poisson PNG and the discrete and continuous-time TASEP.

The one-point distribution result was also extended to other models recently. The ASEP was analyzed in [@Barraquand-Borodin-Corwin-Wheeler18] for a particular value of the boundary condition. The paper [@Imamura-Mucciconi-Sasamoto22] established one-point distribution results for log-Gamma directed polymer, q-PushTASEP, and multiplicative stochastic heat equation, for general values of the boundary condition. However, multi-time limit theorems are still yet to be established
