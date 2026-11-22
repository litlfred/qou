---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-005-24-hydrodynamic-limit-and-kpz-limit
section_title: "Hydrodynamic limit and KPZ limit"
section_number: 2.4
pages: 4-5
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.876
latex_coverage_ratio: 1.0
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
The hydrodynamic limit of TASEP is about $\mathbf{h}(x,t)$ when $x$ and $t$ are proportional. For the step initial condition, $\mathbf{h}(x,0)=|x|$, Rost [@Rost81] showed in 1981 that $$\frac{\mathbf{h}(xT, tT)}{T}  \to \bar{\mathbf{h}}(x,t)$$ almost surely as $T\to \infty$, where $\bar{\mathbf{h}}(x,t) = \frac{t^2+x^2}{2t}$ for $|x|\le t$ and $\bar{\mathbf{h}}(x,t) = |x|$ for $|x|\ge t$. See Figure [1](#fig:hbar){reference-type="ref" reference="fig:hbar"} for the graph. The hydrodynamic limit $\bar{\mathbf{h}}$ is deterministic, and it solves Burger's equation [@Liggett85; @Liggett99].

The KPZ limit is about the next term, $\mathbf{h}(xT, tT)- \bar{\mathbf{h}}(x,t)T$. Setting $x=0$ for convenience and following the 1:2:3 scale, the KPZ universality conjecture suggests that $$\frac{\mathbf{h}(\gamma T^{2/3}, \tau T)- \bar{\mathbf{h}}(0,\tau)T}{T^{1/3}}$$ converges to a 2d random field. If we do not set $x=0$, then we should consider $\mathbf{h}(xT+ \gamma T^{2/3}, \tau T)- \bar{\mathbf{h}}(x,\tau)T$ in the numerator. The limiting 2d field, the KPZ fixed point, depends on the initial condition. The step initial condition for the TASEP becomes the so-called narrow wedge initial condition for the KPZ fixed point.

![$y= \bar{\mathbf{h}}(x, t)$ for a few values of $t$](Growth.pdf){#fig:hbar}

TASEP has interpretations as an interacting particle system, a random growth process, and a last passage percolation model. Each of these interpretations has natural extensions and generalizations. The KPZ universality conjecture is that a large class of models in these generalizations has a universal limit. The exact class is not known, but for random growth models, three key features seem to be the locality of growth, some smoothing mechanism, and lateral growths. For directed last passage percolation, the universality is expected for all random variables $w_s$ with enough moments and without a large atom at the top of the support of the distribution. The last condition is to prevent the situation that there is always a path connecting $(1,1)$ and $(m,n)$ using only the top value, making the last passage time too concentrated.
