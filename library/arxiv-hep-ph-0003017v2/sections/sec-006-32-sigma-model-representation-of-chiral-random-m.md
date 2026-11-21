---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-006-32-sigma-model-representation-of-chiral-random-m
section_title: "Sigma Model Representation of Chiral Random Matrix Models"
section_number: 3.2
pages: 17-19
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.967
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
The chiral random matrix partition function can be evaluated using standard random matrix methods. For simplicity, let us consider the case $\beta=2$. The fermion determinant can be written as a Grassmann integral, and averaging over the Gaussian distribution function results in a four-fermion interaction. Because of the underlying unitary invariance ([\[inv\]](#inv){reference-type="ref" reference="inv"}) of the chRMT, the fermionic variables only appear in invariant combinations of the form $\sigma^{fg} \sim \bar\psi^f_i \psi^g_i$, and the partition function can be rewritten identically in terms of these variables as [@Shur93; @HVeff] $$Z_{\nu}(m) = \int D \sigma \: e^{-{n\Sigma^2} \Tr
  \sigma \sigma^\dagger}{\det}^{\nu} (\sigma+m{\bf 1} ){\det}^{n}
  [(\sigma+m{\bf 1} )(\sigma^\dagger +m{\bf 1})]\:,
  \label{z2sigma}$$ where the quark masses have been taken real and degenerate for simplicity. The integration is over the real and imaginary parts of the $N_f \times N_f$ arbitrary complex matrix $\sigma$. For $m = 0$ this integral is invariant under $\sigma \rightarrow U \sigma V^{-1}$ with $U$ and $V\in{\rm SU}(N_f)$. Let us calculate the integrals by a saddle-point approximation. The saddle-point equation reads (notice that $\nu \ll n$) $$\Sigma^2 (\sigma^\dagger+m) \sigma = 1\:.$$ The condensate at the saddle point is given by $$|\langle\bar\psi\psi\rangle| = \frac 1{2nN_f} \partial_m \log Z = 
  \frac {\Sigma^2}{2N_f}\langle {\rm Tr}(\sigma +\sigma^\dagger)\rangle \:,$$ where the expectation value is with respect to the partition function ([\[z2sigma\]](#z2sigma){reference-type="ref" reference="z2sigma"}). The solution of the saddle-point equation, $\bar\sigma$, is proportional to the identity matrix. In the chiral limit, we then find $\bar \sigma = 1/\Sigma$, and we can identify $\Sigma$ as the chiral condensate.

The fluctuations about the saddle point can be separated into massive modes with a curvature of order $n$ and Goldstone modes with a curvature of order $mn$. In the limit $n\rightarrow \infty$, the partition function ([\[z2sigma\]](#z2sigma){reference-type="ref" reference="z2sigma"}) can be simplified by keeping the integrals over the Goldstone manifold and performing the remaining integrals by a saddle-point integration. This results in the partition function $$\label{Znum}
  Z_{\nu}( m) = \int_{U \in {\rm U}(N_f)} DU\: {\det}^\nu U\:
  e^{ n\Sigma  \Tr (MU + M^\dagger U^{-1})}\:,$$ which is the familiar finite volume partition function to be discussed in Sec. [\[Finite-Volume\]](#Finite-Volume){reference-type="ref" reference="Finite-Volume"}.

## $\theta$-Dependence of the Partition Function

The $\theta$-dependence of the partition function is obtained by summing over all topological sectors of the partition function according to Eq. ([\[Ztheta\]](#Ztheta){reference-type="ref" reference="Ztheta"}), which applies to full QCD where the partition function is obtained by integrating over the gauge fields. The terms $Z_\nu$ in this equation reflect the probability of encountering gauge fields with topological charge $\nu$.

For the effective theory, the partition function in the topological sector $\nu$ is given in Eq. ([\[Znum\]](#Znum){reference-type="ref" reference="Znum"}). However, this $\nu$-dependence is only due to the fermion determinant. In the sum over $\nu$, we should therefore add weight factors $P(\nu)$ that take into account the distribution of topological charge of the quenched gauge fields (i.e. gauge fields generated without the fermion determinant). This yields $$Z^{\rm eff}(\theta,m) = \sum_{\nu}P(\nu) e^{i\nu \theta} Z^{\rm
  eff}_\nu(m)\:. 
\label{ztheta}$$ Below, we argue that the weight factors can be ignored for light quarks but that they are necessary when one considers the quenched theory (which corresponds to $N_f=0$ or, equivalently, to the limit of very heavy quarks).

Our starting point is that the topological susceptibility of the quenched gauge fields is nonvanishing, i.e. $$\frac { \langle \nu^2 \rangle_q} V \ne 0\:.$$ Invoking the central limit theorem, we assume that $P(\nu)$ is Gaussian, $$P(\nu) = \frac 1{\sqrt{2 \pi \langle \nu^2 \rangle_q}}\:
  e^{-\frac{\nu^2}{2 \langle \nu^2 \rangle_q }}\:,$$ which has been verified by quenched lattice QCD simulations.

We analyze the partition function ([\[ztheta\]](#ztheta){reference-type="ref" reference="ztheta"}) for $Z_{\nu}^{\rm eff}(m)$ given by the finite-volume partition function in Eq. ([\[Znum\]](#Znum){reference-type="ref" reference="Znum"}). Replacing the sum over $\nu$ by an integral, we obtain after integration $$Z^{\rm eff}(\theta,m)=\int_{U\in{\rm U}(N_f)} DU
  e^{-\frac{ \langle \nu^2 \rangle_q}2
    (\theta -i\Tr\log U )^2 +  \frac12\Sigma V \Tr (MU + M^\dagger
     U^{-1})}\:. 
\label{zlargen}$$ The exponent in the integrand corresponds to the effective static potential of QCD with a large number of colors [@Witten], and therefore the chRMT partition function reproduces all identities that have been derived from this effective potential [@Shur93; @janu1]. For example, the topological charge is screened by light quarks. For a careful analysis of the periodicity requirements of the $\theta$-dependence of the effective partition function ([\[zlargen\]](#zlargen){reference-type="ref" reference="zlargen"}), see Ref. [@Zhit].

Let us illustrate the screening of topological charge for $N_f = 1$ and real $m$, for which $$Z^{\rm eff}(\theta,m) = \int d \phi \: e^{-\frac{\langle \nu^2 \rangle_q}2
    (\theta -\phi )^2 + \Sigma Vm \cos \phi}\:.$$ The integral over $\phi$ can be performed by a saddle-point approximation resulting in [@Leut92] $$\label{Zmtheta}
  Z^{\rm eff}(\theta,m) = e^{mV\Sigma \cos\theta}.$$ The topological susceptibility is given by $$\langle \nu^2\rangle = -\frac{\partial^2}{\partial{\theta^2}}
  \log Z =  m V\Sigma \qquad ({\rm for}\;\theta=0)
  \label{susm}$$ so that the topological charge is completely screened in the chiral limit. This also shows that the results are insensitive to our choice of the distribution function $P(\nu)$. For example, in an instanton liquid interpretation of the chiral random matrix model, the natural choice for $P(\nu)$ is the binomial distribution $B(N-\nu,\nu)$, resulting in the same effective potential [@Shur93].

In fact, it can be concluded from Eq. ([\[susm\]](#susm){reference-type="ref" reference="susm"}) that for light quarks the distribution $P(\nu)$ can be ignored altogether. Let us again illustrate this for $N_f =1$, for which the integral in Eq. ([\[Znum\]](#Znum){reference-type="ref" reference="Znum"}) results in the finite volume partition function $$Z^{\rm eff}_\nu(m) = I_\nu(mV\Sigma)\:,$$ where $I_\nu$ is a modified Bessel function. Summing over $\nu$ according to Eq. ([\[Ztheta\]](#Ztheta){reference-type="ref" reference="Ztheta"}), i.e. without the weight factors $P(\nu)$, we obtain [@Damtop] $$Z^{\rm eff}(\theta, m) =\sum_{\nu}
  e^{i\nu \theta} I_\nu(mV\Sigma) = e^{mV \Sigma \cos \theta}\:,$$ where we have used a summation formula for modified Bessel functions. This is exactly the same result as in Eq. ([\[Zmtheta\]](#Zmtheta){reference-type="ref" reference="Zmtheta"}). For an extension of these results to more than one flavor, see Ref. [@Damtop].
