---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-006-resurgence-in-3d-mathcal-n2-theories
section_title: "Resurgence in 3d ${\mathcal N}=2$ theories"
section_number: null
pages: 12-14
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.914
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
The phenomenon of non-abelian contributions being distributed among the abelian ones can be translated entirely into the language of 3d ${\mathcal N}=2$ field theories. In fact, this phenomenon is not limited to theories $T[M_3]$ associated with 3-manifolds and should be regarded more broadly, as a decomposition of BPS quantities in gapless (conformal) theories into BPS spectra of its massive deformations.

Thanks to supersymmetric localization, partition functions of 3d ${\mathcal N}=2$ theories on $D^2\times_q S^1$ can be reduced to finite-dimensional integrals, which in the limit $q = e^{\hbar} \to 1$ have the form $$Z (D^2\times_q S^1) \; = \; \int dz \, \Delta (z) \, \exp \left( \frac{1}{\hbar} \widetilde{\mathcal W}(z) + \ldots \right)
\label{generalZvortex}.$$ The multi-variable $z = (z_1 , \ldots, z_r)$ typically comes from gauge factors, and $\widetilde{\mathcal W}(z)$ can be interpreted as a twisted superpotential of the 3d theory on a circle. Its critical points are the vacua of the 2d ${\mathcal N}=(2,2)$ effective field theory, which for a finite-size circle come in infinite towers. Indeed, when the 3d theory is compactified on a circle of finite radius, the variables $z_i$ are ${\mathbb C}^*$-valued and the equations for vacua also have the exponentiated form: $$\exp \left( \frac{\partial \widetilde{\mathcal W}}{\partial \log z_i} \right) \; = \; 1.$$ For this reason, each vacuum comes in an infinite family, much like saddle points of Chern-Simons functional. Also, as in Chern-Simons theory, the critical points of $\widetilde{\mathcal W}$ have the leading order behavior $$\hbar^{n/2} e^{\frac{1}{\hbar} \widetilde{\mathcal W}(z_*)} \cdot (\text{power series in}~\hbar)$$ where the critical exponent $n$ is the degree of degeneracy of the critical point $z = z_*$; the larger the value of $n$ the more singular the critical point is (see [@appetizer] for a careful treatment of such factors).

![Critical points of $\widetilde{\mathcal W}$ in 3d ${\mathcal N}=2$ theories come in infinite towers because, as in complex Chern-Simons theory, the space of fields is not simply-connected. Moreover, a generic theory has degenerate, non-Morse critical points, which arise, *e.g.*, when the fields at the critical point have a large stabilizer. In localization integrals, such critical points "absorb" the contributions of regular, Morse critical points as trans-series.](critpts){#fig:critpts width="3.0in"}

Therefore, in the context of completely general 3d ${\mathcal N}=2$ theories we find two key elements of the resurgent analysis [@Gukov:2016njj]: the critical points come in infinite ${\mathbb Z}$-towers and they may have different degree of degeneracy signalled by powers of $\hbar = \log q$. Hence, applying the resurgent analysis of [@Gukov:2016njj] to the integral [\[generalZvortex\]](#generalZvortex){reference-type="eqref" reference="generalZvortex"}, we conclude that contributions of critical points with smaller values of the exponent $n$ will be "distributed" among critical points with larger values of $n$.

In order to see this phenomenon in physically-motivated 3d ${\mathcal N}=2$ theories, such as 3d SQED or SQCD, we simply need to look at examples with non-trivial range of values of $n$.
