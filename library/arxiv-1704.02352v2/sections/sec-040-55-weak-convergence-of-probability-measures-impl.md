---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-040-55-weak-convergence-of-probability-measures-impl
section_title: "Weak convergence of probability measures implies uniform convergence of densities"
section_number: 5.5
pages: 38-39
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.966
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
For $\epsilon>0$ and $u_0\in\mathbb{R}$ let $\phi_\epsilon\colon \mathbb{R}\to\mathbb{R}_+$ be a function on the real line such that $\phi_\epsilon$ is supported on an $\epsilon$-neighborhood of $u_0$ and $\int \phi_\epsilon(u) \dif u = 1$. Since $\mathbb{E}f_{\Lambda_n}$ is Lipschitz with constant $1$, it follows that $$\begin{gathered}
\label{eq:Lipschitz-is-good}
\left| \mathbb{E}f_{\Lambda_n}(u_0) - \int\ \phi_\epsilon(u)\ \dif \mathbb{E}P_{\Lambda_n}(u) \right| =\\
\left| \int \phi_\epsilon(u)\ \left( \mathbb{E}f_{\Lambda_n} (u_0) - \mathbb{E}f_{\Lambda_n}(u)\right)  \dif u \right| \leq 
\\ 
\int \phi_\epsilon(u)\ \left|\mathbb{E}f_{\Lambda_n} (u_0) - \mathbb{E}f_{\Lambda_n}(u)\right|\  \dif u\leq \epsilon.
\end{gathered}$$ By weak convergence of probability measures, the integral on the left-hand side converges, as $n\to\infty$, to $\int\ \phi_\epsilon(u)\ \dif P_{\Lambda_\infty}(u)$. By passing to the limit, the above inequality implies therefore that $$\limsup_{n\to\infty}
\left| \mathbb{E}f_{\Lambda_n}(u_0) - \int\ \phi_\epsilon(u)\ \dif P_{\Lambda_\infty}(u) \right| 
\leq \epsilon.$$ Since this inequality holds true for arbitrary $\epsilon>0$, it follows that the sequence $\mathbb{E}f_{\Lambda_n}(u_0)$ is a Cauchy sequence, hence it converges to a finite limit which will be denoted by $f_{\Lambda_\infty}(u_0)$. In other words, we have proved that the functions $\mathbb{E}f_{\Lambda_n}$ converge pointwise to the function $f_{\Lambda_\infty}$; since all functions $\mathbb{E}f_{\Lambda_n}$ are Lipschitz with the same constant, *the convergence is uniform on a compact set $K=[-R,R]$ for arbitrary value of $R$*.

On the other hand, inequalities [\[eq:bounds-on-density\]](#eq:bounds-on-density){reference-type="eqref" reference="eq:bounds-on-density"} show that the distance between $\mathbb{E}f_{\Lambda_n}$ and $f_{\Lambda_\infty}$ with respect to the supremum norm on the set $K^c=\mathbb{R}\setminus K$ is bounded by $$\label{eq:sup-bound}
\left\| \mathbb{E}f_{\Lambda_n} - f_{\Lambda_\infty} \right\|_{L^{\infty}[K^c]} \leq
\frac{2}{\sqrt{R^2+4}+|R|}.$$ Since the right-hand side converges to zero as $R\to\infty$, it follows that *the sequence of functions $\mathbb{E}f_{\Lambda_n}$ converges to $f_{\Lambda_\infty}$ uniformly on the whole real line $\mathbb{R}$*.

To conclude, we proved the following theorem which might be of independent interest.

::: theorem
Let $(\Lambda_n)$ be a sequence of random anisotropic Young diagrams, each with the unit area. Let $(P_{\Lambda_n})$ be the corresponding sequence of random probability measures on $\mathbb{R}$ with densities $(f_{\Lambda_n})$ as in [\[subsec:MeasureAssociatedWithYoung\]](#subsec:MeasureAssociatedWithYoung){reference-type="ref" reference="subsec:MeasureAssociatedWithYoung"}. Assume that the sequence of probability measures $(\mathbb{E}P_{\Lambda_n})$ converges to some limit in the weak topology.

Then there exists a function $f_{\Lambda_\infty}$ such that $\mathbb{E}f_{\Lambda_n} \to
f_{\Lambda_\infty}$ uniformly on $\mathbb{R}$.
:::
