---
doc_id: arxiv-1208.3475v2
doc_title: "Poisson - Random Matrix transition in the QCD Dirac spectrum"
section_id: sec-004-41-localization-length
section_title: "Localization length"
section_number: 4.1
pages: 6-8
source_pdf: 1208.3475v2.pdf
source_sha256: d53fc4eefa070ba3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.993
---
To get a rough estimate of the localization scale we can consider the inverse participation ratio (IPR) defined by Eq. [\[eq:IPR\]](#eq:IPR){reference-type="ref" reference="eq:IPR"}. Since the IPR scales like the inverse four-volume of the region where the given mode is spread out a good measure of the localization scale is provided by the quantity

$$l = a \cdot \langle \mbox{IPR}^{-\frac{1}{4}} \rangle,
   \label{eq:l}$$

where the average is understood over all the eigenmodes in a given region of the spectrum. In principle $l$ varies through the spectrum but it does not change too much within the region of localized modes. To illustrate that, in Fig. [1](#fig:lvslambda){reference-type="ref" reference="fig:lvslambda"} we show in two representative cases how $l$ changes through the spectrum. As can be seen in the Figure for the lowest part of the spectrum the localization length is almost constant and is independent of the spatial volume. In this region there might be a small dip in $l$. The dip is generally more pronounced at lower temperatures and/or on finer lattices but on our ensembles the total variation of $l$ in the localized regime never exceeds 20%. At some point in the spectrum $l$ starts to increase sharply and becomes strongly volume dependent. This is the beginning of the transition to delocalized states.

<figure id="fig:lvslambda">
<div class="center">
<embed src="lvslambda.eps" />
</div>
<figcaption><span id="fig:lvslambda" label="fig:lvslambda"></span> The localization length (Eq. <a href="#eq:l" data-reference-type="ref" data-reference="eq:l">[eq:l]</a>) of eigenmodes along the spectrum for ensembles D1 and D2 differing only in their spatial volumes. Both <span class="math inline"><em>l</em></span> and the location in the spectrum, <span class="math inline"><em>λ</em></span> are given in lattice units. Statistical errors are not shown as they are smaller than the size of the symbols.</figcaption>
</figure>

In what follows we define the localization length of localized modes with the following simple procedure. The localized eigenmodes all have $l$'s between the bottom of the dip and the $l$ of the very lowest eigenmodes. This interval for ensembles D1 and D2 is indicated by the two dashed horizontal lines in Fig. [1](#fig:lvslambda){reference-type="ref" reference="fig:lvslambda"}. The central value we quote for $l$ is always the center of this band and the uncertainty is half the width of the band. Compared to that, statistical errors are always negligible.

Having a well defined measure of the localization length for localized modes we can now look at how it depends on the lattice spacing. Since, as we will see, $l$ also depends on the temperature, we choose to compare ensembles C, D and E which are almost exactly at the same physical temperature of about 400 MeV. Since $l$ does not depend on the spatial volume we omit the numbers from the ensemble labels here. In Fig. [2](#fig:lvsa){reference-type="ref" reference="fig:lvsa"} we plot the localization length as a function of the lattice spacing for these three ensembles.

<figure id="fig:lvsa">
<div class="center">
<embed src="lvsa.eps" />
</div>
<figcaption><span id="fig:lvsa" label="fig:lvsa"></span> The localization length of the localized modes as a function of the lattice spacing. The three points correspond to the same physical temperature of about 400MeV (ensembles C, D and E).</figcaption>
</figure>

To guide the eye we also included a linear fit to the data. Even if the quality of our data does not allow a proper continuum extrapolation it can be safely concluded that the localization length measured in physical units does not increase in the continuum limit and it is not larger than a few tenth of a Fermi at this temperature.

It is also instructive to see how the localization length compares to the most important length scale in the problem, the inverse temperature or in other words the temporal size of the box. In Fig. [3](#fig:lvsT){reference-type="ref" reference="fig:lvsT"} we plot the localization length in units of the inverse temperature for all the ensembles. Different symbols represent data sets corresponding to different values of the lattice spacing. There is a slight trend of the finer lattices producing more localized low modes as can be seen also in Fig. [2](#fig:lvsa){reference-type="ref" reference="fig:lvsa"}. The important point is that the lowest modes always appear to be localized on or below the scale of the inverse temperature in the whole range of temperatures studied here.

<figure id="fig:lvsT">
<div class="center">
<embed src="lvsT.eps" />
</div>
<figcaption><span id="fig:lvsT" label="fig:lvsT"></span> The localization length in units of the inverse temperature as a function of the physical temperature. The different symbols represent data obtained at different values of the lattice spacing.</figcaption>
</figure>

## Renormalization and temperature dependence of $\lambda_c$

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

Data sets C, D and E where we have data at the same temperature for all three lattice spacings indicate that the lattice spacing dependence in the quantity $\frac{\lambda\ensuremath _{\mbox{\scriptsize c}}}{m\ensuremath _{\mbox{\scriptsize ud}}}$ is comparable to its uncertainty at a given lattice spacing. Therefore in Fig. [4](#fig:lcpmvsT){reference-type="ref" reference="fig:lcpmvsT"} we plot the temperature dependence of this quantity for all lattice spacings in the same figure. The different types of symbols, corresponding to data obtained from lattices of different coarseness, all lie on a smooth curve confirming that scaling violations in this quantity are small. The lowest order polynomial fit to all the data that yields an acceptable chi-squared ($\chi^2=1.3$) is second order and extrapolates to $T=$<!-- -->170MeV at $\frac{\lambda\ensuremath _{\mbox{\scriptsize c}}}{m\ensuremath _{\mbox{\scriptsize ud}}}=0$. This value is consistent with the known location of the finite temperature cross-over in QCD [@Borsanyi:2010bp; @Bazavov:2011nk] below which chiral symmetry is broken and no localized modes are expected to be present. This provides a further consistency check of our results.

<figure id="fig:locnum">
<div class="center">
<embed src="locnum.eps" />
</div>
<figcaption><span id="fig:locnum" label="fig:locnum"></span> The number of localized (below <span class="math inline">$\lambda\ensuremath _{\mbox{\scriptsize c}}$</span>) eigenmodes per cubic Fermi as a function of the temperature. Different symbols refer to simulations at different values of the lattice spacing.</figcaption>
</figure>

Another physically interesting quantity is the number density of localized modes. This quantity is also practically important if one aims at detecting localization from spectral statistics. In order to be able to observe Poisson statistics in the level spacing distribution the volume of the system has to be large enough to accommodate several localized eigenmodes per configuration. To see what that means practically in Fig. [5](#fig:locnum){reference-type="ref" reference="fig:locnum"} we plotted the average density of eigenmodes below $\lambda\ensuremath _{\mbox{\scriptsize c}}$ as a function of the temperature. Again we collect data obtained at different values of the lattice spacing in the same Figure. Apparently the number density of localized modes decreases sharply as the transition temperature is approached from above. In practical terms that means that in order to have for instance about twenty localized modes per configuration the aspect ratio of the boxes has to be kept between 4-6 in the temperature range considered here.

Finally we would like to point out a potential technical difficulty in studying the level spacing distribution. It is caused by the pairing of staggered Dirac eigenvalues affecting the lowest part of the spectrum when the spatial volume is small. It comes about because in the continuum limit staggered fermions describe four fermion flavors and the spectrum is expected to become fourfold degenerate. Therefore approaching the continuum limit this degeneracy starts to be formed and peculiar correlations will appear among members of the would-be continuum quartets.

It turns out that already at the lattice spacings we used here the stout smearing of gauge fields coupled to the fermions bring the spectrum close enough to the continuum behavior that such extra correlations for the lowest eigenvalues can be detected. This is first manifested in pairwise attraction between consecutive eigenvalues which distorts the Poisson statistics [@Kovacs:2011km]. The splitting between members of the doublets, however, does not depend appreciably on the volume while the separation of the doublets (eventually quartets) should be inversely proportional to the spectral density and thus to the volume. Therefore this distortion of the level spacing statistics is a finite volume effect (c.f. also [@Halasz:1996sb]). Moreover it only affects the lowest part of the spectrum where the spectral density is very small. Since the spatial volumes we used are large enough the results we presented here are not affected by the staggered degeneracy. On the other hand, a more systematic study of the level spacing statistics of the very lowest staggered Dirac modes might reveal interesting facts about how the expected degeneracy is formed in the continuum limit.
