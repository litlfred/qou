---
doc_id: arxiv-2007.15570v1
doc_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_id: sec-008-iii-results-and-model-validation
section_title: "III Results and Model Validation"
section_number: null
pages: 6-6
source_pdf: 2007.15570v1.pdf
source_sha256: 6e46f4346a29fd83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.64
latex_coverage_ratio: 0.979
doc_brief: "A quantum Monte Carlo based approach to intranuclear cascades — 16 sections: Front matter; A quantum Monte Carlo based approa; I Introduction"
---
In this Section, we present the validation tests we performed and the results we obtained within our INC model. For comparison purposes, we also implement a version of the nucleon-nucleon interaction algorithm that we dub *mean free path* (MFP). This approach is routinely used in event generators. Within this algorithm, the system is not evolved in time steps but rather in constant position steps that we indicate as $\lambda_{\rm max}$. At each step of the loop the mean free path of the propagating particle reads $$\tilde{\lambda}=1/\Big(\rho_{p}(r)\sigma_{Np}+\rho_{n}(r)\sigma_{Nn}\Big)$$ where $N=n,p$ refers to the isospin of the propagating particle and $r$ its distance from the centre of the nucleus. Note that in the limit of constant density, $\rho_{p(n)}(r)=\bar{\rho}$, we would recover $\tilde{\lambda}=\lambda_{\rm mfp}$. (see also Sec. [\[ssec:mean_free_path\]](#ssec:mean_free_path){reference-type="ref" reference="ssec:mean_free_path"} below). The probability that the struck particle traveled a distance $\lambda$ without interacting can be written as $P(\lambda)=e^{-\lambda/\tilde{\lambda}}$. We can then sample $\lambda =-\tilde{\lambda}\cdot \ln({\rm rand}[0,1])$ and say that an interaction took place if $\lambda < \lambda_{\rm max}$. Note that $\lambda_{\rm max}$ has to be chosen small enough in order to satisfy the assumption of a constant density.

<figure id="fig:mfp">
<p><embed src="figures/mean_free_path.pdf" /><br />
</p>
<figcaption>Distribution of distance traveled (blue histogram) by 500 MeV test nucleons traveling through a <span class="math inline">0.16</span> nucleons/fm<span class="math inline"><sup>3</sup></span> background density of nucleons at rest, fixed interaction cross-section of 50 mb, and using the Gaussian interaction probability. The black and orange lines are the expected distributions for the fitted (1.23 fm) and expected (1.25 fm) values of the mean free path, respectively. <span id="fig:mfp" label="fig:mfp"></span></figcaption>
</figure>

## Mean free path []{#ssec:mean_free_path label="ssec:mean_free_path"}

The simplest validation consists of calculating the mean free path of a nucleon travelling through a medium of uniformly distributed nucleons, with fixed interaction cross sections. Our goal is to obtain $$\label{eq:mfp}
    \lambda_{\rm mfp} = \frac{1}{\sigma \rho},$$ where $\sigma$ is the nucleon-nucleon cross section, and $\rho$ is the number density of nucleons. We simulate a background of static, randomly and uniformly distributed protons and neutrons at rest. For an event, we insert into the medium a test particle with a fixed energy and propagate it through the medium. When the first interaction happens, we record the length the test particle has traveled. Figure [1](#fig:mfp){reference-type="ref" reference="fig:mfp"} shows the distribution of lengths traveled for a 500 MeV test proton in a $0.16$ nucleons/fm$^3$ background density of nucleons, assuming a fixed interaction cross section of 50 mb, and using the Gaussian interaction probability. The expected distributions, according to Eq. [\[eq:mfp\]](#eq:mfp){reference-type="eqref" reference="eq:mfp"}, are also shown for the fitted (black line) and the expected (orange line) values of the mean free path. The nuclear density and interaction cross section were chosen arbitrarily. Adjusting these values does not change the agreement between the expected mean free path and the calculated mean free path. While not shown here, using the cylinder interaction probability does not change the results either. As we can see, our code correctly reproduces the expected behavior for the mean free path, allowing us to proceed to more complex tests of our INC.
