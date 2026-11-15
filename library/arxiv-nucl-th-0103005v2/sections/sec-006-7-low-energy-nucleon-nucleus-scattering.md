---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "arXiv:nucl-th/0103005v2 6 Mar 2001"
section_id: sec-006-7-low-energy-nucleon-nucleus-scattering
section_title: "LOW-ENERGY NUCLEON-NUCLEUS SCATTERING"
section_number: 7
pages: 35-36
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.974
doc_brief: "arXiv:nucl-th/0103005v2 6 Mar 2001 — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear Hamiltonians that"
---
[]{#sec:scat label="sec:scat"}

The calculations presented so far have treated resonant nuclear states as if they were particle stable; that is the VMC trial wave functions decay exponentially at large distances and the GFMC propagation does not impose a scattering-state boundary condition. As was shown in Fig. [\[fig:8be-e_of_tau\]](#fig:8be-e_of_tau){reference-type="ref" reference="fig:8be-e_of_tau"}, this GFMC propagation converges for unstable states that are narrow, but for wide states, such as $^8$Be(4$^+$), the $E(\tau)$ keeps decreasing for increasing $\tau$. Such states should be computed using scattering-wave boundary conditions.

The $^5$He($\case{1}{2}^-$, $\case{3}{2}^-$) states have been studied in VMC [@csk87] and GFMC [@cs94] using scattering-wave boundary conditions. The VMC calculations use a trial function that is a straight-forward generalization of the $\Psi_V$ given in Sec. 3. In it the $\Psi_J$ contains one p-wave single-particle function that goes to zero at a specified (large) radius, $R_n$. The variational energy is minimized subject to this boundary condition. The phase shift at the resulting scattering energy, $E_s=E(^5\mbox{He}(R_n))-E(^4\mbox{He})$ is then obtained from $$\tan(\delta_l) = \frac{j_l(k R_n)}{n_l(k R_n)},$$ where $k = (2 \mu E_s)^{1/2} / \hbar$, $\mu$ is the $\alpha$+$n$ reduced mass, and $j_l$ and $n_l$ are the spherical Bessel functions (in this case $l=1$). It is possible to generalize this formulation by specifying a logarithmic-derivative at $R_n$, rather than having the wave function go to zero there. This method requires the computation of the energy difference, $E_s$. If this is done with two different VMC calculations, one for $^5$He with the specified boundary condition, and one for $^4$He, then the statistical errors of these two calculations must be added in quadrature. Instead one can directly evaluate the energy difference in a VMC random walk that is controlled by the $^5$He wave function. In practice this gives $E_s$ with a smaller statistical error than either of the separate statistical errors [@csk87]. The GFMC calculations start with the scattering-state trial function and use a modified propagator that preserves the boundary condition [@cs94]. Both methods result in a phase shift and energy corresponding to a given boundary condition. By repeating the calculations for different boundary conditions, the phase shift as a function of energy can be mapped out.

The VMC calculations of Ref. [@csk87] used older two- and three-nucleon potentials than have been used for the other calculations reported in this review. They reproduced the qualitative features of the experimental $\alpha$+$n$ $\case{1}{2}^-$ and $\case{3}{2}^-$ phase shifts, but, in particular, gave a spin-orbit splitting about 1 MeV too small. The GFMC calculations [@cs94] used a different, but still somewhat old Hamiltonian and obtained values that are closer to experiment. These calculations need to be repeated with the modern Hamiltonians described in this review, and for other systems such as $\alpha$+$d$, $^6$He+$n$, and $\alpha$+$\alpha$.
