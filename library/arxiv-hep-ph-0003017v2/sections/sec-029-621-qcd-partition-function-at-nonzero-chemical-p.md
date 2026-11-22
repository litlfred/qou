---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-029-621-qcd-partition-function-at-nonzero-chemical-p
section_title: "QCD PARTITION FUNCTION AT NONZERO CHEMICAL POTENTIAL"
section_number: 6.2.1
pages: 41-41
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.988
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
The QCD partition function at nonzero temperature $T$ and chemical potential $\mu$ is given by [@phase] $$Z(m,\mu,T) =\Tr e^{-\frac{H_{\rm QCD} -\mu N}T}
  =\sum_\alpha e^{-\frac{E_\alpha-\mu N_\alpha}{T}}\:,$$ where $H_{\rm QCD}$ is the Hamiltonian of QCD with eigenvalues $E_\alpha$ and $N$ is the quark number operator. At zero temperature, only the states with $E_\alpha/N_{\alpha} < \mu$ contribute to the partition function. We thus expect that the partition function is independent of $\mu$ below a critical chemical potential $\mu_c$ given by the lightest baryon mass per unit quark number. Therefore, for $\mu < \mu_c \approx m_N/3$ (where $m_N$ is the nucleon mass), the baryon density remains zero and the chiral condensate is constant.

The quark chemical potential appears in the Lagrangian in the form $\mu\psi^\dagger\psi=\bar\psi(\mu\gamma_0)\psi$ and is therefore introduced in the Dirac operator by the substitution $$\partial_0 \rightarrow \partial_0 + \mu\:.$$ This substitution destroys the Hermiticity properties of the QCD Dirac operator, and the resulting complex phase of the fermion determinant makes Monte Carlo simulations impossible. Because of the success of the quenched approximation in lattice QCD simulations at $\mu=0$, it is tempting to ignore the fermion determinant in this case. However, it was shown [@everybody; @maria] that the critical chemical potential for quenched simulations is determined by the pion mass rather than the nucleon mass. Obviously, the basic physics of the problem is not visible in the quenched approximation. An analytical understanding of this problem was first obtained by means of a random matrix model for the Dirac operator of QCD at finite density [@Misha].
