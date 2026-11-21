---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-018-51-unfolding
section_title: "Unfolding"
section_number: 5.1
pages: 31-32
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.985
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
[]{#unfolding label="unfolding"}

In order to compare eigenvalues of any physical system with RMT results, it is necessary first to "unfold" the empirical spectrum (see e.g. Ref. [@Bohi84a]). The spacing $\Delta$ of the eigenvalues is related to the spectral density by $$\Delta(E)=1/\rho(E)\:.$$ Unfolding is a local rescaling of the energy scale so that the mean level spacing of the unfolded eigenvalues is equal to unity throughout the spectrum. This is achieved by splitting the spectral density in an average density, $\bar \rho(E)$, and a fluctuating piece, $$\rho(E) = \bar \rho(E) + \rho_{\rm fl}(E)\:.$$ The average spectral density can be obtained in different ways. In some cases, it can be computed analytically using semiclassical arguments. However, in most cases $\bar \rho(E)$ is obtained by averaging over many level spacings. There are two essentially different procedures to do this, spectral averaging and ensemble averaging. Spectral averaging is appropriate if only one or a few spectra are available. The average level spacing at $E$ is then obtained by averaging over many level spacings around $E$. Ensemble averaging is appropriate if there is a large ensemble of spectra all drawn from the same statistical distribution. In this case, the average spacing can be obtained by averaging the spacing at $E$ over each member of the ensemble. In both cases, the separation of the spectral density into an average and a fluctuating piece requires a separation of scales that is typically achieved only in the thermodynamic limit or in the semiclassical limit. The unfolded spectrum, $\{x_n\}$, is then obtained from the average spectral density (equal to the inverse average level spacing) by $$x_n=\int_{-\infty}^{E_n}\bar\rho(\lambda) d\lambda\:,$$ where $\{E_n\}$ is the original sequence of eigenvalues. The difference between the two procedures is that spectral averaging yields $\bar\rho(E)$ separately for each spectrum whereas ensemble averaging yields a single $\bar\rho(E)$ for all spectra. In both cases, the average spectral density of the unfolded spectrum becomes $\bar\rho(x)=1$, so that the sequence $\{x_n\}$ has an average level spacing equal to unity. The correlations of the levels are always calculated for the unfolded spectrum.

The two procedures to calculate the average spectral density do not necessarily give the same spectral correlations at long distances. The equivalence of the two is known as spectral ergodicity. This property has been shown analytically for several random matrix ensembles [@Pandey; @Weide-recent]. In general, ensemble averaging results in stronger level fluctuations than does spectral averaging [@French-connection; @Guhr99; @Ande99]. In practice a mixture of both methods is often useful. For example, one may calculate the average spectral density by ensemble averaging but, in order to get better statistics, calculate the correlation functions by both ensemble averaging and spectral averaging. Spectral averaging requires that the statistical properties of the eigenvalues be stationary over the spectrum, which is not the case for many systems and has to be checked each time.
