---
doc_id: arxiv-1011.1343v1
doc_title: "Chiral symmetry, nuclear forces and all that"
section_id: sec-006-43-the-nuclear-matter-problem
section_title: "The nuclear matter problem"
section_number: 4.3
pages: 10-11
source_pdf: 1011.1343v1.pdf
source_sha256: 7d50e5e28e695191
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 1.0
doc_brief: "Chiral symmetry, nuclear forces and all that — 11 sections: Front matter; The early days at Stony Brook; A first step: Studying pion-nucleo"
---
[]{#sec:nucmat label="sec:nucmat"}

Another important question in nuclear physics is to understand the saturation properties of nuclear matter - an idealized infinite system of nucleons in which all Coulomb effects are switched off. From the properties of heavy nuclei using some sophisticated mass formula, one can extrapolate to nuclear matter - and determine its saturation properties. The binding energy per nucleon $E/A$ is approximately $-16\,$ MeV at a Fermi momentum of about 1.3 fm$^{-1}$. So what does chiral EFT have to say? A first important step was taken by Norbert Kaiser, Wolfram Weise and collaborators at München, who calculated the contribution of pion exchange(s) to the energy density of nuclear matter and showed that the energy density of isospin symmetric nuclear matter can be extremely well approximated by the simple form $$E/A = \frac{3k_F^2}{10m} - \alpha \frac{k_F^3}{m^2} + \beta
\frac{k_F^4}{m^3}~.$$ They then calculated the coefficients $\alpha$ and $\beta$ from chiral dynamics. With some fine-tuning of the regulator, one finds an astonishingly good description of the energy density of nuclear matter [@Kaiser:2001jx]. This was later improved by including e.g. higher orders (sensitive again to the LECs $c_i$) and isobar degrees of freedom [@Fritsch:2004nx]. Interestingly, all this was based on a loop expansion with no explicit power counting - a power counting that indeed explained the success of these calculations was only set up much later, see [@Oller:2009zt]. Space forbids a discussion of this power counting and the resulting physics in detail - I only would like to mention that it could be shown that for many reactions the contributions from the multi-nucleon interactions cancel to leading order which is at the heart of the success of the Munich group calculations.

Here, I briefly pursue a more "conventional" approach to the nuclear matter problem based on more standard nuclear many-body theory. For decades, the method of choice to analyze nuclear matter has been the G-matrix of Brueckner and others - leading to the problem that for phase-shift equivalent NN potentials the resulting saturation properties lie on the Coester line that does not pass the empirical values. Recently, Siegfried Krewald and collaborators have recalculated the properties of nuclear matter based on the chiral NN and 3N forces (see the v2 version of Ref. [@Saviankou:2008tg]) utilizing the R-matrix as proposed by Baker in 1971 [@Baker:1971vm]. As can be seen from the left panel of Fig. [1](#fig:nucmat){reference-type="ref" reference="fig:nucmat"}, the NN interaction alone only binds for Fermi momenta larger than 1.7 fm$^{-1}$. However, including the 3NF with natural values for $D$ and $E$, one finds binding with the proper strength at the proper density. In the right panel, the sensitivity to the two cut-offs in the NN force as compared to phenomenological determinations is shown, it is of comparable size. The dependence on the 3-body LECs $D$ and $E$ is also weak, see Fig. 3 in Ref. [@Saviankou:2008tg]. It will be interesting to push these calculations to N$^3$LO and to include the $\Delta(1232)$ in the EFT.

<figure id="fig:nucmat">
<div class="center">
<p><embed src="ea103wsq.eps" style="width:6.75cm" /> <embed src="sat_ellipse2.eps" style="width:6.75cm" /></p>
</div>
<figcaption><span id="fig:nucmat" label="fig:nucmat"></span> Left panel: Binding energy per particle of nuclear matter as a function of the Fermi momentum <span class="math inline"><em>k</em><sub><em>F</em></sub></span> for the N<span class="math inline"><sup>2</sup></span>LO potential using a Lippman-Schwinger cut off <span class="math inline"><em>Λ</em> = 550</span> MeV and a spectral function cut off <span class="math inline"><em>Λ̃</em> = 600</span> MeV (solid line). The binding energies obtained in the absence of three-nucleon interactions are shown by the dashed line. The black square gives the empirical nuclear matter properties. Right panel: Saturation points of nuclear matter. Downward triangle, upward triangle and rectangle: various phenomenological approaches. Circles: chiral EFT at N<span class="math inline"><sup>2</sup></span>LO. </figcaption>
</figure>
