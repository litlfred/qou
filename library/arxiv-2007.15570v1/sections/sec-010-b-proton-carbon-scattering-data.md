---
doc_id: arxiv-2007.15570v1
doc_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_id: sec-010-b-proton-carbon-scattering-data
section_title: "B Proton-carbon Scattering Data"
section_number: null
pages: 7-8
source_pdf: 2007.15570v1.pdf
source_sha256: 6e46f4346a29fd83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.997
doc_brief: "A quantum Monte Carlo based approach to intranuclear cascades — 16 sections: Front matter; A quantum Monte Carlo based approa; I Introduction"
---
Reproducing the proton-nucleus cross section measurements is an important test of the accuracy of the INC model. Proton-nucleus scattering probes the nucleon-nucleon cross section which is typically divided into two pieces, the reaction and the elastic cross sections, $$\sigma_{\rm tot} = \sigma_R + \sigma_{\rm el}.$$ In the elastic part, no energy is transferred into nuclear excitation and the nucleus remains unbroken, that is $n+A \rightarrow n+A$. The reaction cross section includes transition to nuclear excited states, $n+A \rightarrow n+A^*$, as well as inelastic reactions $n+A \rightarrow X$.

Several experiments have been carried out to determine the total reaction cross section, see for example Refs. [@Dicello:1970mx; @Bobchenko:1979hp; @Bauhoff:1986gcb; @Kox:1987qw; @Sihver:1993pc; @Carlson:1996ofz]. The latter is typically obtained by measuring the total cross section from the change in intensity of a calibrated proton beam traversing a carbon target and then subtracting the calculated elastic cross section.

<figure id="fig:pC_xsec">
<p><embed src="figures/xsec.pdf" /><br />
<embed src="figures/xsec_zoom.pdf" /><br />
</p>
<figcaption>Proton-carbon scattering total cross section as a function of the incoming proton kinetic energy. In the upper panel the entire energy range for which experimental data are available is shown. In the lower panel the low energy region is magnified. The red and blue curves correspond to the cylinder algorithm where the mean field (MF) and quantum Monte Carlo (QMC) configurations have been used, respectively. The green and orange curves are the same but for the Gaussian interaction probability. The results displayed in purple refers to the mean free path (MFP) calculations. The solid and dashed curves corresponds to the use of the <code>GEANT4</code> <span class="citation" data-cites="Agostinelli:2002hh"></span> and NASA <span class="citation" data-cites="Norbury:2008"></span> parametrization of the cross section in the interaction probability, respectively. The data points are from Ref. <span class="citation" data-cites="Carlson:1996ofz"></span> <span id="fig:pC_xsec" label="fig:pC_xsec"></span></figcaption>
</figure>

We compute $\sigma_R$ neglecting Coulomb interactions, as they are expected to contribute mostly to $\sigma_{\rm el}$. We obtain the proton-carbon scattering cross section by the following simulation (with a different setup from the proposed algorithm of Fig. [\[fig:algorithm\]](#fig:algorithm){reference-type="ref" reference="fig:algorithm"}). We define a beam of protons with energy $E$, uniformly distributed over an area $A$ (orthogonal to the proton momenta). Note that $A\gg \pi R^2$, where $R$ is the radius of the carbon nucleus. The carbon nucleus is situated in the center of the beam. We propagate each proton in time and check for scattering at each step. The Monte Carlo reaction cross section is then defined as the area of the beam times the fraction of scattered events, namely, $$\sigma_{\rm MC}=A \frac{N_{\rm scat}}{N_{\rm tot}}.$$ This is not exactly the experimentally measured reaction cross section. Angular and/or momentum acceptances for the attenuated beam are finite, and we do not include these effects in our calculation. Nevertheless, we do not expect such effects to change our results significantly, and thus $\sigma_{\rm MC}$ should be a good approximation of the reaction cross section. Moreover, imposing Pauli blocking on both outgoing nucleons will effectively suppress the contribution of elastic transitions.

The two panels of Fig. [1](#fig:pC_xsec){reference-type="ref" reference="fig:pC_xsec"} display the proton-carbon scattering cross sections as a function of the proton kinetic energy. In the upper panel our Monte Carlo simulations are compared with experimental data in the entire energy region in which data are available [@Carlson:1996ofz], while the lower panel focuses on proton kinetic energies below 200 MeV. The curves correspond to different implementations of the INC. These implementations are composed of three ingredients, namely,

1.  Nuclear configuration: quantum Monte Carlo (QMC) or mean field (MF);

2.  Interaction model: cylinder (cyl), Gaussian (Gauss), or mean free path (MFP);

3.  Nucleon-nucleon cross section: elastic (El) or total (Tot).

Note that the interaction model MFP does not use any configuration, but rather the local density.

The solid lines have been obtained using the nucleon-nucleon cross sections from the SAID database [@SAID], obtained using `GEANT4` [@Agostinelli:2002hh], in which only the elastic contribution is retained. The dashed lines used the NASA parameterization [@Norbury:2008], which includes inelasticities. The inelastic contribution leads to an enhancement of the cross section which is necessary to reproduce the data correctly for intermediate to large proton kinetic energies. The NASA parameterization allows us to approximate the effects of including pions in the cascade. Results obtained with these two nucleon-nucleon cross sections are indicated in Fig. [1](#fig:pC_xsec){reference-type="ref" reference="fig:pC_xsec"} by "El" for elastic cross section and "Tot" for the total cross section. As expected, the $p$-carbon cross section obtained using only the elastic nucleon-nucleon cross section is consistently lower than the one obtained using the total nucleon-nucleon cross section. The effect is large for $T_p>50$ MeV, where pion production becomes relevant. In a future work, we will explicitly include pion degrees of freedom in our INC as these are known to play a crucial role in this region. Additionally, the present results neglect modifications to the nucleon-nucleon cross section arising from the nuclear medium itself. Such modifications have been considered in the literature  [@Pandharipande:1992zz]. We also leave these considerations for a future work.

The dependence of the results on the functional form of the interaction probability and on the nuclear model adopted to generate nuclear configurations has also been investigated. The blue and red lines are obtained from the cylinder probability of Eq. [\[prob:cyl\]](#prob:cyl){reference-type="eqref" reference="prob:cyl"} and sampling the initial nucleon configurations from the quantum Monte Carlo (QMC) and mean field (MF) distributions, respectively. To obtain the orange and green curves, QMC and MF configurations were used together with the Gaussian probability of Eq. [\[prob:gauss\]](#prob:gauss){reference-type="eqref" reference="prob:gauss"}. We observe that in both cases, the QMC and MF curves are almost superimposed, indicating that this observable does not depend strongly on correlation effects among the nucleons. A more detailed discussion of their impact on particle propagation distances will be discussed in Sec. [\[sec:corr:eff\]](#sec:corr:eff){reference-type="ref" reference="sec:corr:eff"}.

The purple lines refer to mean free path (MFP) calculations which present conceptual differences with respect to the cylinder and Gaussian cases and yield large discrepancies in the results. The predictions for the $p$-carbon cross section obtained from the MFP approach underestimate the experimental data and are significantly lower with respect to the other curves obtained with more refined techniques.

In the lower panel of Fig. [1](#fig:pC_xsec){reference-type="ref" reference="fig:pC_xsec"} we focus on the comparison between the different MC simulations and the data in the low energy region, i.e., proton kinetic energies below $200$ MeV. The results obtained using the Gaussian and cylinder algorithm are in fair agreement with the experimental data: the curves display the correct behaviour although the position of the peak is not exactly reproduced. We note that Pauli blocking plays a fundamental role for these kinematics, significantly quenching the results. More sophisticated techniques aimed at consistently orthogonalizing the nuclear wave function in the final state are discussed in Ref. [@Gonzalez-Jimenez:2019qhq]. Their implementation in our INC will be the subject of a future work.

The functional forms adopted to determine the probability distribution (Gaussian vs. cylinder) yield predictions which differ by $\sim15\%$ in the low energy region (compare, for instance, the green and red lines in Fig. [1](#fig:pC_xsec){reference-type="ref" reference="fig:pC_xsec"}). For intermediate proton kinetic energies $T_p$ the curves converge to the same result and reproduce the data. At low $T_p$, the predicted cross sections for the MFP method are $\sim50\%$ smaller than those of the Gaussian and cylinder methods. As these differences are also present in nuclear transparency, we will discuss their origins in the next section.
