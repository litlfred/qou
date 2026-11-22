---
doc_id: arxiv-1208.3475v2
doc_title: "Poisson - Random Matrix transition in the QCD Dirac spectrum"
section_id: sec-007-41-localization-length
section_title: "Localization length"
section_number: 4.1
pages: 6-7
source_pdf: 1208.3475v2.pdf
source_sha256: d53fc4eefa070ba3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 1.0
doc_brief: "Poisson - Random Matrix transition in the QCD Dirac spectrum — 12 sections: Front matter; Introduction; Simulation details"
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
