---
doc_id: arxiv-1208.3475v2
doc_title: "Poisson - Random Matrix transition in the QCD Dirac spectrum"
section_id: sec-008-42-renormalization-and-temperature-dependence-of
section_title: "Renormalization and temperature dependence of $\lambda_c$"
section_number: 4.2
pages: 7-8
source_pdf: 1208.3475v2.pdf
source_sha256: d53fc4eefa070ba3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.991
doc_brief: "Poisson - Random Matrix transition in the QCD Dirac spectrum — 12 sections: Front matter; Introduction; Simulation details"
---
We have seen that the lowest eigenmodes spread out only to a distance scale below the inverse temperature. Therefore these modes cannot contribute to quark propagation on length scales larger than that. As far as hadronic correlators are considered above that distance scale the system behaves as if it had a gap of order $\lambda_c$. The influence of this effective gap on the physics depends on how $\lambda_c$, the critical point in the spectrum, scales in the continuum limit.

In Subsection [\[ssec:smulsd\]](#ssec:smulsd){reference-type="ref" reference="ssec:smulsd"} we showed how to determine the critical point using the second moment of the unfolded level spacing distribution. This procedure yields the critical point $\lambda_c a$ in dimensionless lattice units for each temperature and lattice spacing. In what follows we give a proposal for defining the continuum limit of this quantity. Since the critical point is effectively a gap for quark modes capable of propagating to long distances it plays a role similar to the quark mass that also introduces a gap. For this reason we expect $\lambda_c$ to be renormalized in exactly the same way as the quark mass and the ratio of $\lambda_c a$ to the bare light quark mass $m\ensuremath _{\mbox{\scriptsize ud}} a$ should have a proper continuum limit. Moreover this quantity measures the relative size of the effective gap for delocalized modes and the gap for all modes provided by the quark mass.

Another, perhaps more formal, argument showing that $\lambda_c/m\ensuremath _{\mbox{\scriptsize ud}}$ has a well-defined continuum limit is as follows. On the one hand, the pseudoscalar meson correlator $\langle P(x) P(0) \rangle$ is proportional to the matrix elements of the square of the Dirac propagator, $[(D^\dagger+m)(D+m)]^{-1}$. On the other hand, for asymptotically large temporal separations $t$

$$\frac{1}{V\ensuremath _{\mbox{\scriptsize s}}} \sum_{\vec{x}} \langle P(t,\vec{x}) P(0) \rangle =
    C\ensuremath _{\mbox{\scriptsize PP}} \mbox{e}^{m_\pi t},$$

where $V\ensuremath _{\mbox{\scriptsize s}}$ is the spatial volume and $C\ensuremath _{\mbox{\scriptsize PP}}$ is related to the pion decay constant, $f_\pi$, as [@Aubin:2004fs]

$$C\ensuremath _{\mbox{\scriptsize PP}} m\ensuremath _{\mbox{\scriptsize ud}}^2 = \frac{f_\pi^2}{V\ensuremath _{\mbox{\scriptsize s}}} m_\pi^3.$$

The right-hand side of this equation is a well-defined physical quantity and thus so is the left-hand side. Since $C\ensuremath _{\mbox{\scriptsize PP}}$ is proportional to the inverse quark propagator squared, it is also proportional to the inverse of the Dirac eigenvalues squared. Thus

$$m\ensuremath _{\mbox{\scriptsize ud}}^2 \lambda\ensuremath _{\mbox{\scriptsize c}}^{-2} \propto C\ensuremath _{\mbox{\scriptsize PP}} m\ensuremath _{\mbox{\scriptsize ud}}^2$$

also has a well defined continuum limit. For a more general discussion of similar issues with Wilson fermions see also [@DelDebbio:2005qa] and [@Giusti:2008vb].

<figure id="fig:lcpmvsT">
<div class="center">
<embed src="lcpmvsT.eps" />
</div>
<figcaption><span id="fig:lcpmvsT" label="fig:lcpmvsT"></span> The temperature dependence of the renormalized critical point <span class="math inline">$\frac{\lambda\ensuremath _{\mbox{\scriptsize c}}}{m\ensuremath _{\mbox{\scriptsize ud}}}$</span>. The continuous line is a quadratic polynomial fit to all the data. The different symbols correspond to data obtained using lattices of different coarseness.</figcaption>
</figure>

Data sets C, D and E where we have data at the same temperature for all three lattice spacings indicate that the lattice spacing dependence in the quantity $\frac{\lambda\ensuremath _{\mbox{\scriptsize c}}}{m\ensuremath _{\mbox{\scriptsize ud}}}$ is comparable to its uncertainty at a given lattice spacing. Therefore in Fig. [1](#fig:lcpmvsT){reference-type="ref" reference="fig:lcpmvsT"} we plot the temperature dependence of this quantity for all lattice spacings in the same figure. The different types of symbols, corresponding to data obtained from lattices of different coarseness, all lie on a smooth curve confirming that scaling violations in this quantity are small. The lowest order polynomial fit to all the data that yields an acceptable chi-squared ($\chi^2=1.3$) is second order and extrapolates to $T=$<!-- -->170MeV at $\frac{\lambda\ensuremath _{\mbox{\scriptsize c}}}{m\ensuremath _{\mbox{\scriptsize ud}}}=0$. This value is consistent with the known location of the finite temperature cross-over in QCD [@Borsanyi:2010bp; @Bazavov:2011nk] below which chiral symmetry is broken and no localized modes are expected to be present. This provides a further consistency check of our results.

<figure id="fig:locnum">
<div class="center">
<embed src="locnum.eps" />
</div>
<figcaption><span id="fig:locnum" label="fig:locnum"></span> The number of localized (below <span class="math inline">$\lambda\ensuremath _{\mbox{\scriptsize c}}$</span>) eigenmodes per cubic Fermi as a function of the temperature. Different symbols refer to simulations at different values of the lattice spacing.</figcaption>
</figure>

Another physically interesting quantity is the number density of localized modes. This quantity is also practically important if one aims at detecting localization from spectral statistics. In order to be able to observe Poisson statistics in the level spacing distribution the volume of the system has to be large enough to accommodate several localized eigenmodes per configuration. To see what that means practically in Fig. [2](#fig:locnum){reference-type="ref" reference="fig:locnum"} we plotted the average density of eigenmodes below $\lambda\ensuremath _{\mbox{\scriptsize c}}$ as a function of the temperature. Again we collect data obtained at different values of the lattice spacing in the same Figure. Apparently the number density of localized modes decreases sharply as the transition temperature is approached from above. In practical terms that means that in order to have for instance about twenty localized modes per configuration the aspect ratio of the boxes has to be kept between 4-6 in the temperature range considered here.

Finally we would like to point out a potential technical difficulty in studying the level spacing distribution. It is caused by the pairing of staggered Dirac eigenvalues affecting the lowest part of the spectrum when the spatial volume is small. It comes about because in the continuum limit staggered fermions describe four fermion flavors and the spectrum is expected to become fourfold degenerate. Therefore approaching the continuum limit this degeneracy starts to be formed and peculiar correlations will appear among members of the would-be continuum quartets.

It turns out that already at the lattice spacings we used here the stout smearing of gauge fields coupled to the fermions bring the spectrum close enough to the continuum behavior that such extra correlations for the lowest eigenvalues can be detected. This is first manifested in pairwise attraction between consecutive eigenvalues which distorts the Poisson statistics [@Kovacs:2011km]. The splitting between members of the doublets, however, does not depend appreciably on the volume while the separation of the doublets (eventually quartets) should be inversely proportional to the spectral density and thus to the volume. Therefore this distortion of the level spacing statistics is a finite volume effect (c.f. also [@Halasz:1996sb]). Moreover it only affects the lowest part of the spectrum where the spectral density is very small. Since the spatial volumes we used are large enough the results we presented here are not affected by the staggered degeneracy. On the other hand, a more systematic study of the level spacing statistics of the very lowest staggered Dirac modes might reveal interesting facts about how the expected degeneracy is formed in the continuum limit.
