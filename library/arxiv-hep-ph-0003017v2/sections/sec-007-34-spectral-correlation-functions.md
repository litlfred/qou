---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-007-34-spectral-correlation-functions
section_title: "Spectral Correlation Functions"
section_number: 3.4
pages: 19-20
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.832
latex_coverage_ratio: 0.979
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
[]{#sec3.1 label="sec3.1"}

In this section, we discuss the spectral correlation functions and the microscopic spectral density corresponding to the chRMT partition function. The global spectral density is a semicircle. It is not universal and we do not expect to find it in realistic physical systems. The universal quantities are local or microscopic spectral correlation functions. In general, a $k$-point spectral correlation function is defined by [@Dyso62] $$\label{kpoint}
  R_k(\lambda_1,\ldots,\lambda_k)=\left\langle\sum_{\scriptsize
      \matrix{j_1\cdots j_k=1\cr j_p\ne j_q}}^N
    \delta(\lambda_1-E_{j_1})\cdots\delta(\lambda_k-E_{j_k})\right\rangle\:,$$ where the $E_{j_p}$ are eigenvalues. The quantity $R_k$ represents the probability density to find $k$ eigenvalues, regardless of labeling, at $\lambda_1,\ldots,\lambda_k$. In particular, $R_1(\lambda)=\rho(\lambda)$. By "local" we mean that the energy differences $|\lambda_p-\lambda_q|$ are of the order of a few mean level spacings.

Because of the $\rm U_A(1)$ symmetry of QCD, all nonzero eigenvalues come in pairs $\pm i\lambda_n$ (see Sec. [\[topology\]](#topology){reference-type="ref" reference="topology"}). This implies that the origin, $\lambda=0$, is a special point of the spectrum and that we have to consider the $R_k$ separately in the bulk of the spectrum and near $\lambda=0$. The latter is called the microscopic region or the "hard edge" of the spectrum.[^1] In addition, there is the tail or "soft edge" of the spectrum, which we do not discuss. The bulk of the spectrum is the middle region, far from either edge.

Because the random matrix partition function is known in terms of an integral over the eigenvalues of the Dirac operator, see Eq. ([\[zeig\]](#zeig){reference-type="ref" reference="zeig"}), it is possible to obtain the spectral density and all spectral $k$-point correlation functions by integration over $N-k$ eigenvalues. In the present case, the integrals can be performed most conveniently by the orthogonal polynomial method. We mention only the most important results in the sections below.

[^1]: The reason for this nomenclature is that in a Fermi-gas formulation of RMT, where the eigenvalues are interpreted as the positions of particles, this symmetry corresponds to choosing a potential that is infinite for negative values of the eigenvalues. In this picture, the soft edge corresponds to a potential with a finite slope.
