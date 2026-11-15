---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-009-342-microscopic-correlations
section_title: "MICROSCOPIC CORRELATIONS"
section_number: 3.4.2
pages: 21-22
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.988
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
In the context of QCD, the small eigenvalues are more interesting than those in the bulk because of their relation to spontaneous chiral symmetry breaking via the Banks-Casher relation. The local spectral correlation functions at the hard edge of the spectrum are characterized by $\lambda_p\sim{\cal O}(1/N)$ and $|\lambda_p-\lambda_q|\sim{\cal O}(1/N)$. Unfolding in the microscopic region is easy; the eigenvalues are simply rescaled by the mean level spacing at $\lambda=0$, which is given by Eq. ([\[spacing\]](#spacing){reference-type="ref" reference="spacing"}). By convention, we define the unfolded variables by $x_p=\lambda_p V\Sigma$, i.e. the factor of $\pi$ is omitted. Note that $V\propto N$. Thus, in the unfolded variables we have $x_p\sim{\cal O}(1)$ and $|x_p-x_q|\sim{\cal O}(1)$. As advertised above, the functional form of the $R_k$ is different in the microscopic region. The $R_k$ are still given by the determinant of a kernel according to Eq. ([\[det\]](#det){reference-type="ref" reference="det"}), but the sine kernel is now replaced by the Bessel kernel [@Verb93], $$\label{Bessel}
  K(x,y)=\sqrt{xy}\:\frac{xJ_{\alpha+1}(x)J_\alpha(y)
    -yJ_\alpha(x)J_{\alpha+1}(y)}{x^2-y^2}\:,$$ where $J_\alpha$ denotes Bessel functions and $\alpha=N_f+|\nu|$, with $N_f$ the number of massless flavors and $\nu$ the topological charge. A mathematical discussion of the Bessel kernel can be found in Ref. [@Tracy].

The RMT results for the chOE and the chSE are more complicated [@Verb94; @Naga95; @Brez96; @Altland]. Note that, in contrast to the situation in the bulk, the microscopic correlations depend on $N_f$ and $\nu$.

The one-point function is universal in the microscopic region. For the chUE, the microscopic spectral density, defined above in Eq. ([\[micro\]](#micro){reference-type="ref" reference="micro"}), is related to the kernel by $\rho_s(z)=K(z,z)$ and can be expressed as [@Verb93; @Verb94c] $$\rho_s(z)  = \frac {z}{2} \left[J^2_{N_f+|\nu|}(z) -J_{N_f+|\nu|+1}(z)
  J_{N_f+|\nu|-1}(z)\right]\:.
  \label{micro2}$$ It is also the generating function for the Leutwyler-Smilga sum rules, which are essentially inverse moments of $\rho_s$ (or of higher-order spectral correlation functions). They are discussed below. The results ([\[Bessel\]](#Bessel){reference-type="ref" reference="Bessel"}) and ([\[micro2\]](#micro2){reference-type="ref" reference="micro2"}) were first derived using chiral RMT. In the meantime, Eq. ([\[micro2\]](#micro2){reference-type="ref" reference="micro2"}) has been confirmed by an explicit calculation starting from a partially quenched chiral Lagrangian [@OTV; @Damg99], which is discussed in the next section. The microscopic spectral density and the two-point correlation function for the case $N_f+|\nu|=0$ have also been derived by means of the supersymmetric method of RMT [@Andreev].

There is a very interesting connection between the Bessel kernel and the effective partition function. In addition to the partition function $Z^{(N_f)}$ for $N_f$ massless sea quarks, one can also compute the partition function $Z^{(N_f+2)}$ for $N_f$ massless quarks and two additional flavors with imaginary masses. One then finds the relation [@Damg98a] $$\label{massiveK}
  K(x,y)=\frac{1}{2}(xy)^{N_f+1/2}\:\frac{Z^{(N_f+2)}(ix,iy)}{Z^{(N_f)}}\:,$$ which can also be generalized to massive sea quarks. Thus, to obtain the $R_k$ for $N_f$ flavors, one needs to know the partition function for two additional flavors with imaginary masses. This result has a natural interpretation in terms of the effective spectral partition function (discussed below in Sec. [\[sec:effective\]](#sec:effective){reference-type="ref" reference="sec:effective"}). The two additional flavors are the spectral quark and its bosonic superpartner [@OTV]. The relation ([\[massiveK\]](#massiveK){reference-type="ref" reference="massiveK"}) once again demonstrates the equivalence of the random matrix formulation and the effective field theory in the zero mode domain. Additional consistency conditions for the finite volume partition function are discussed in Ref. [@Akeconsist].
