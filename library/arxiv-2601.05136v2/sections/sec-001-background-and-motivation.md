---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-001-background-and-motivation
section_title: "Background and motivation"
section_number: null
pages: 2-3
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.865
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:Background and motivation label="sec:Background and motivation"}

Kashaev's [@Kashaev1997] proposes a striking connection between the geometry of hyperbolic knots and their quantum invariants. This conjecture appears to be related to quantum $\slg$ Chern-Simons theory, a TQFT arising as a complexification [@Gukov2005] or analytic continuation [@Witten2010] of the more familiar quantum $\operatorname{SU}(2)$ Chern-Simons theory [@zbMATH04092352]. A number of authors [@Baseilhac2004; @Bonahon2021; @Kashaev2005; @McPhailSnyderVolume] have constructed geometric quantum invariants that can be interpreted as candidates for a mathematical realization of $\slg$ Chern-Simons theory.

We discuss some typical features of a candidate mathematical realization. For concreteness let $K$ be a hyperbolic knot in $S^{3}$, although some versions are additionally or instead defined for closed $3$-manifolds or related objects. A realization is a family of functions $$\mathcal{Z}_{N} \colon \mathsf{X}(K) \to \mathbb{C}$$ for $N$ a positive integer related to the level and $\mathsf{X}(K)$ a space parametrizing hyperbolic structures on $\comp{K}$; it is usually a version of the $\slg$ character variety of $\comp{K}$. Let $\varsigma_{K} \in \mathbb{C}/ 2 \pi \ii \mathbb{Z}$ be the $\slg$ Chern-Simons invariant of the canonical structure $\rho_{\mathop{\mathrm{hyp}}}$ of $K$, normalized so $2 \pi \operatorname{Re}\varsigma_{K}$ is the hyperbolic volume of $K$. A volume conjecture is the statement that (up to normalization and some other details) $$\label{eq:asymptotics sign positive}
  \lim_{N\to \infty}
  \frac{
    \log \mathcal{Z}_{N}(K, \rho)
  }{
    N
  }
  =
  \varsigma_{K}$$ for some $\rho \in \mathsf{X}(K)$ that is not necessarily $\rho_{\mathop{\mathrm{hyp}}}$. We think of $N\to \infty$ as the semiclassical limit. The surprising observation is that this holds for $\rho$ other than $\rho_{\mathop{\mathrm{hyp}}}$; Kashaev's original conjecture [@Kashaev1997] is that it happens for the trivial hyperbolic structure $1$. In this case $\mathcal{Z}_{N}(K,1)$ can be identified with a value of the $N$th colored Jones polynomial of $K$ [@Murakami2001]. There is a standard ansatz (successful in some special cases) for proving these conjectures that uses two steps.

::: step
[]{#step 1 label="step 1"} Show that the invariant is equivalent (perhaps asymptotically) to a , a contour integral $$\mathcal{Z}_{N}(K, \rho) \sim
    \int_{\Gamma} e^{N\mathcal{S}(\mathbf{t})} \dif \mathbf{t}$$ where $\mathcal{S}$ is a holomorphic function that can be identified with the Chern-Simons functional. Sometimes instead one must consider a sum of such integrals.
:::

In more detail, given a combinatorial description $\mathcal{T}$ of $\comp{K}$ the domain of $\mathcal{S}$ is a space $\Omega_{\mathcal{T}}$ parametrizing hyperbolic structures on the individual pieces of $\mathcal{T}$. Critical points of $\mathcal{S}$ are choices that combine together to give a coherent structure on all of $\comp{K}$ and the critical value is the $\slg$ Chern-Simons invariant. For example, if $\mathcal{T}$ is an ideal triangulation then $\Omega_{\mathcal{T}}$ parametrizes shapes of the tetrahedra and critical points of $\mathcal{S}$ are solutions of Thurston's gluing equations.

::: step
[]{#step 2 label="step 2"} Show that $$\int_{\Gamma} e^{N\mathcal{S}(\mathbf{t})} \dif \mathbf{t}
    \sim
    \int_{\Gamma'} e^{N\mathcal{S}(\mathbf{t})} \dif \mathbf{t}$$ where $\Gamma'$ is a contour in saddle point position for a critical point corresponding to $\rho_{\mathop{\mathrm{hyp}}}$.
:::

The maximum critical value of $\operatorname{Re}\mathcal{S}$ is $\operatorname{Re}\varsigma_{K}$. It occurs at a saddle point of $\operatorname{Re}\mathcal{S}$ because $\mathcal{S}$ is a holomorphic function. If $\Gamma'$ is a contour passing through this saddle point in the right way a standard by a Gaussian integral gives the desired asymptotics [\[eq:asymptotics
sign positive\]](#eq:asymptotics
sign positive){reference-type="eqref" reference="eq:asymptotics
sign positive"}.

In general both steps require hard computations; a detailed discussion of the analytic issues is given by @zbMATH06684922 [@zbMATH06684922]. [\[step 1\]](#step 1){reference-type="ref" reference="step 1"} requires re-writing a discrete sum as a (sum of) integrals, typically by using the Poisson summation formula. Ensuring that this is valid requires careful estimates on the size of $\mathcal{S}$ and related functions.

Previous work of the author [@McPhailSnyderVolume] uses the holonomy $R$-matrices defined in joint work with N. Reshetikhin [@McPhailSnyderAlgebra] to define a candidate mathematical realization $\qinv{}$ of complex Chern-Simons theory as described above. In this paper we show that $\qinv{}$ is equal to a sum of state integrals. Our method does not require checking any inequalities and works for any representation satisfying a natural, algebraic nondegeneracy condition. To my knowledge this is the first example of an exact (not asymptotic) state integral presentation of a cyclic type invariant. Such integral presentations automatically occur for principal type invariants, an inequivalent but related mathematical realization of complex Chern-Simons theory ([\[sec:negative type\]](#sec:negative type){reference-type="ref" reference="sec:negative type"}). Our results may clarify the relationship between these two branches.
