---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-015-asymptotics
section_title: "Asymptotics"
section_number: null
pages: 14-15
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.719
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:Asymptotics label="sec:Asymptotics"}

It is immediate from [\[thm:dilog lemma\]](#thm:dilog lemma){reference-type="ref" reference="thm:dilog lemma"} that $\actq{D}{}$ converges pointwise on $\Omega_{D}$ to $\act{D}{}$ as $N\to
\infty$, which suggests we can approximate the state integrals $\stint{D, \mu, \beta}{k}$ of [\[eq:state integral again\]](#eq:state integral again){reference-type="eqref" reference="eq:state integral again"} by using a saddle-point approximation. @zbMATH06684922 gives a detailed explanation of the saddle point approximation in the context of the Volume Conjecture in [@zbMATH06684922 Section 3], which we summarize here.

Let $f$ be holomorphic on some domain in $\mathbb{C}^{\ell}$ containing an isolated critical point $\gamma$. A contour $\Gamma \colon [-1,1]^{\ell} \to \mathbb{C}^{\ell}$ with $\Gamma(0) = \gamma$ passes through $\gamma$ in if $\operatorname{Re}f(\Gamma(t)) < \operatorname{Re}f(\gamma)$ except for when $t = 0$ and it satisfies an additional orientation condition. The saddle point approximation says that $$\int_{\Gamma} e^{Nf(t)} \dif t
  =
  N^{-\ell/2}
  e^{Nf(\gamma)}
  [ \tau + \bigoh(N^{-1}) ]$$ for a constant $\tau$ related to the determinant of the Hessian of $f$ at $\gamma$. It can be refined to include higher-order terms in the exponent whose coefficients are related to derivatives of $f$. The idea is that near the critical point we can approximate $e^{N
f}$ by a Gaussian.

We can apply this approximation to study the asymptotics of $\qinv{K, \rho, u}$ for $K$ a hyperbolic knot. Suppose there is some diagram $D$ where $\rho$ is not pinched; as discussed in [\[sec:Gauge transformations and admissibility\]](#sec:Gauge transformations and admissibility){reference-type="ref" reference="sec:Gauge transformations and admissibility"} we can think of this as a nondegeneracy condition on $\rho$. If we could show that [\[step 2\]](#step 2){reference-type="ref" reference="step 2"} holds then we could replace the state integrals of [\[eq:state integral again\]](#eq:state integral again){reference-type="ref" reference="eq:state integral again"} with modified integrals $$\stintadj{D}{k} \mathrel{:=}
  \int_{\Gamma}
  \exp N\left( \act{D}{t} - \tu k \cdot t \right)
  \dif t$$ for some other contour $\Gamma$. The dependence on the initial representation $\rho$ drops out because $\beta/N\to 0$; this is one explanation for why the growth rate in [\[eq:asymptotics sign positive\]](#eq:asymptotics sign positive){reference-type="eqref" reference="eq:asymptotics sign positive"} is independent of $\rho$. Changing the contour $\Gamma$ is plausible because $\act{D}{}$ is a holomorphic function and we can use Stokes' Theorem (i.e. a higher-dimensional Cauchy theorem) but there are other issues discussed in [\[sec:Barriers to Step 2\]](#sec:Barriers to Step 2){reference-type="ref" reference="sec:Barriers to Step 2"}.

For now, suppose that it is valid to write $$\qinv{K, \rho, \mu}
  =
  N^{|E|/2 - 1/2}
  \sum_{k \in \mathbb{Z}^{E}}
  \stintadj{D}{k}
  +
  \bigoh(e^{N(\operatorname{Re}\varsigma_{K} - \delta)})$$ for some $\delta > 0$. Since we assumed $\rho$ was not pinched the complete hyperbolic structure $\rho_{\mathop{\mathrm{hyp}}}$ is also not pinched. By [\[thm:crit points are reps\]](#thm:crit points are reps){reference-type="ref" reference="thm:crit points are reps"} there is a generalized critical point $\gamma$ of $\act{D}{}$ with flattening vector $k_{0}$ corresponding to some normalized shadow coloring of $\rho_{\mathop{\mathrm{hyp}}}$ avoiding the unit circle.

We know that $\act{D}{\gamma} = \varsigma_{K}$ is the $\slg$ Chern-Simons invariant of $\rho_{\mathop{\mathrm{hyp}}}$ normalized as in [\[eq:asymptotics sign positive\]](#eq:asymptotics sign positive){reference-type="ref" reference="eq:asymptotics sign positive"} and that $\operatorname{Re}\varsigma_{K}$ is maximal among all generalized critical points. Suppose that $\Gamma$ passes through $\gamma$ in saddle point position (which is not quite right: see below). Then the saddle point approximation gives $$N^{|E|/2 - 1/2}
  \stintadj{D}{k_{0}}
  =
  \tau
  N^{-1/2}
  e^{N\varsigma_{K} + \bigoh(N^{-1})}$$ because $\Gamma$ is an $|E|$-dimensional contour. The terms of the sum with $k \ne k_{0}$ do not contribute at highest order to the asymptotics because the saddle point approximation also requires the imaginary part of the derivative of $\act{D}{}$ to vanish: if it does not the growth is suppressed by rapid oscillations in the phase of the integrand. The sum over $k$ in [\[eq:state intgral sum\]](#eq:state intgral sum){reference-type="eqref" reference="eq:state intgral sum"} naturally captures the extra choice of flattening used in the computation of $\varsigma_{K}$.

As noted above this analysis is incorrect. The problem is that $\gamma$ is *never* an isolated critical point because of gauge symmetry: the gauge transformations of [\[def:gauge transformation\]](#def:gauge transformation){reference-type="ref" reference="def:gauge transformation"} show that a given representation $\rho$ corresponds to a manifold of complex dimension $3$ lying in the space $\mathbb{C}^{E}$ of segment parameters. If we restrict to normalized shadow colorings we fix one degree of freedom, so $\act{D}{}$ is *constant* in two complex, hence four real coordinate directions near $\gamma$. This recovers an overall power of $N^{2}$, giving

::: conjecture
[]{#our volume conjecture label="our volume conjecture"} Let $K$ be a hyperbolic knot. Suppose that $\rho$ is a decorated representation of $D$ that is geometrically nondegenerate in the sense that $\rho$ is non-pinched for some open diagram $D$ of $K$. Then for some choices of log-meridian $\mu$ (see [\[sec:Barriers to Step 2\]](#sec:Barriers to Step 2){reference-type="ref" reference="sec:Barriers to Step 2"}) there is a constant $\tau$ so that $$\qinv{K, \rho, \mu}
    =
    N^{3/2}
    e^{N\varsigma_{K} }
    [\tau + \bigoh(N^{-1}) ]
    \qedhere$$
:::

Similar conjectures were made by @zbMATH05624995 [@zbMATH05624995].
