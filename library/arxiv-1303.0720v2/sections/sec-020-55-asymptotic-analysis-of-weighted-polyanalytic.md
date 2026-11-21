---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-020-55-asymptotic-analysis-of-weighted-polyanalytic
section_title: "Asymptotic analysis of weighted polyanalytic Bergman kernels"
section_number: 5.5
pages: 12-13
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.986
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
It is our aim is to supply an algorithm to compute a near-diagonal asymptotic expansion of the weighted polyanalytic Bergman kernel $K_{q,m}$ as $m$ tends to infinity. Under suitable assumptions on the potential $Q$, the kernel has -- up to an error term -- the (local) expansion $$K_{q,m}(z,w)\sim
\big\{ m^{q} \Lfun^q_{0}(z, w) + m^{q-1}\Lfun^q_{1}(z, w)+\dots
+ m^{q-k}\Lfun^q_{k}(z,w) \big\} 
\mathrm{e}^{2mQ(z,w)},$$ where near the diagonal $z=w$, the coefficient functions $\Lfun^q_{j}(z,w)$ are $q$-analytic in each of the variables $z$ and $\bar w$. As before, $Q(z,w)$ is a polarization of $Q(z)$. The control of the error term is of order $\mathrm{O}(m^{q-k-1})$ in the parameter $m$. We work this out in detail in the bianalytic case $q=2$, and obtain explicit formulae for $\Lfun^2_j$ when $j=0,1,2$ (see Remark [\[rem-AA\]](#rem-AA){reference-type="ref" reference="rem-AA"}). Note that we may use the formula $\delta K_{q,m}:=K_{q,m}-K_{q-1,m}$ to asymptotically express the reproducing kernel $\delta K_{q,m}$ associated with the orthogonal difference space $\delta\mathrm{PA}^2_{q,m}$.

We base our approach is based on the recent work of Berman, Berndtsson, and Sjöstrand [@bbs], where they give an elementary algorithm to compute the coefficients $\Lfun_{j}=\Lfun^1_{j}$ of the asymptotic expansion of the weighted Bergman kernel.

We now extend their method to polyanalytic functions of one variable. We explain our results in detail in the case $q=2$ and compute the first two terms of the asymptotic expansion. We supply some hints on how to the approach applies for bigger values of $q$. The actual computations become unwieldy and for this reason they are not presented. Our asymptotic analysis leads to the following blow-up result.

::: thm
[]{#blowupthm label="blowupthm"} $(q=2)$ Let $\Omega$ be a domain in ${\mathbb C}$, and suppose $Q:\Omega\to{\mathbb R}$ is $C^4$-smooth

with $\varDelta Q>0$ on $\Omega$ and $$\sup_{\Omega}\frac{1}{\varDelta Q}\varDelta\log\frac{1}{\varDelta Q}<+\infty.$$ Suppose, in addition, that $Q$ is real-analytically smooth in a neighborhood of a point $z_0\in\Omega$, and introduce the rescaled coordinates $\xi':=[2m\varDelta Q(z_0)]^{-1/2}\xi$ and $\eta':=[2m\varDelta Q(z_0)]^{-1/2}\eta$. Then there exists a positive $m_0$ such that, for all $m \geq m_0$, we have $$\frac{1}{2m \varDelta Q(z_0)}\vert K_{2,m}(z_0+
\xi',z_0+\eta')\vert\mathrm{e}^{- mQ( z_0+\xi')-mQ (z_0+\eta')}
=\frac{|2-|\xi-\eta|^2|}{\pi}\,\mathrm{e}^{-\frac12|\xi-\eta|^2}+\mathrm{O}(m^{-1/2}),
\label{eq-univ1}$$ where the constant in the error term is uniform in compact subsets of $(\xi,\eta)\in{\mathbb C}^2$.
:::

We remark that since the limiting kernel on the right-hand side of [\[eq-univ1\]](#eq-univ1){reference-type="eqref" reference="eq-univ1"} does not depend on the particular weight $Q$, we may view the above theorem as a universality result; for more on universality, see, e.g., [@deift]. The probabilistic interpretation is that in the large $m$ limit, the determinantal point process (for a definition, see [@hkpv]) defined by the kernel $K_{2,m}$ obeys local statistics (after the appropriate local blow-up) given by the kernel $\pi^{-1}(2-|\xi-\eta|^2)\mathrm{e}^{-|\xi-\eta|^2/2}$. This local blow-up kernel appeared earlier in our previous paper [@hh] which was concerned with the quadratic potential $Q(z)=\vert z\vert^2$. In that paper, we analyzed a system of noninteracting fermions described by the Landau Hamiltonian of Subsection [\[subsec-landau\]](#subsec-landau){reference-type="ref" reference="subsec-landau"}, so that each of the $q$ first Landau levels was filled with $n$ particles. As $n$ tends to infinity and the magnetic field is rescaled by $m$, with $m=n+\mathrm{O}(1)$, the particles accumulate on the closed unit disk (which equals the spectral droplet in this instance) with uniform density, and the Laguerre polynomial kernel $\pi^{-1}L^{(1)}_{q-1}(|\xi-\eta|^2)\mathrm{e}^{-|\xi-\eta|^2/2}$ describes the local blow-up statistics in the limit in this polynomial case for general values of $q$. Here, $L^{(\alpha)}_r$ stands for the generalized Laguerre polynomial of degree $r$ with parameter $\alpha$; note that $L^{(1)}_1(x)=2-x$, which explains the expression in Theorem [\[blowupthm\]](#blowupthm){reference-type="ref" reference="blowupthm"}.

To be more precise, this system of free fermions is a determinantal point process given by the reproducing kernels of the spaces $$\mathrm{Pol}_{q,m, n} := \mathrm{span} \{ \bar z^r z^j \mid 0 \leq r 
\leq q-1, 0 \leq j \leq n-1 \} \subset L^2( {\mathbb C},\mathrm{e}^{-2m|z|^2}).$$ In later work, we intend to replace the weight $\mathrm{e}^{-2m|z|^2}$ by a more general weight $\mathrm{e}^{-2mQ(z)}$ and apply the methods developed here to obtain the asymptotic analysis of the corresponding stochastic processes. On a more general complex manifold, this should correspond to studying sections on line bundles $\bar L^{\otimes q} \otimes L^{\otimes n}$.

Finally, we suggest that it is probably possible to extend our results to the several complex variables setting and in a second step, to more general complex manifolds. Moreover, we would expect that asymptotic expansion results could be obtained for reproducing kernels associated with differential operators more general than $\bar \partial^q$.
