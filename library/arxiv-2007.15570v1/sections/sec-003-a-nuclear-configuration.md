---
doc_id: arxiv-2007.15570v1
doc_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_id: sec-003-a-nuclear-configuration
section_title: "A Nuclear configuration"
section_number: null
pages: 2-4
source_pdf: 2007.15570v1.pdf
source_sha256: 6e46f4346a29fd83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.732
doc_brief: "A quantum Monte Carlo based approach to intranuclear cascades — 16 sections: Front matter; A quantum Monte Carlo based approa; I Introduction"
---
[]{#sec:nuclear-configuration label="sec:nuclear-configuration"}

Nuclei are complicated many-body systems of fermions, whose structure and dynamics emerge from individual interactions among the constituent protons and neutrons. To a remarkably large extent, the latter can be modeled by the non-relativistic Hamiltonian $$H=\sum_{i}\frac{{\bf p}_i^2}{2m_N}+\sum_{i<j} v_{ij}+ \sum_{i<j<k}V_{ijk}\,,
\label{NMBT:ham}$$ where ${\bf p}_i$ denotes the momentum of the $i$-th nucleon with mass $m_N$, while $v_{ij}$ and $V_{ijk}$ are the nucleon-nucleon ($N\!N$) and three-nucleon ($3N$) potentials, respectively. We employ the highly-realistic Argonne $v_{18}$ (AV18) $N\!N$ interaction [@Wiringa:1994wb] that includes spin, isospin, tensor, spin-orbit and quadratic momentum-dependent terms as well as isospin-symmetry-breaking corrections and reproduces the Nijmegen nucleon-nucleon database with a $\chi^2$/datum $\simeq 1$. For the $3N$ interaction, we use the Illinois-7 (IL7) potential [@Pieper:2008], which consists of the dominant standard Fujita-Miyazawa two-pion exchange and smaller multi-pion-exchange components resulting from the excitation of intermediate $\Delta$ resonances. The IL7 potential also contains phenomenological isospin-dependent central terms. The parameters characterizing this three-body potential have been determined by fitting the low-lying spectra of nuclei in the mass range $A$=3--10. The overall AV18+IL7 Hamiltonian then leads to predictions of $\approx 100$ ground- and excited-state energies up to $A$=12, including the $^{12}$C ground- and Hoyle-state energies, in good agreement with the corresponding empirical values [@Carlson:2014vla].

Over the last decades significant progress has been made in the development of ab initio nuclear methods, which solve the many-body Schrödinger equation associated with the Hamiltonian of Eq. [\[NMBT:ham\]](#NMBT:ham){reference-type="eqref" reference="NMBT:ham"} with controlled approximations [@Bogner:2009bt; @Barrett:2013nh; @Hagen:2013nca; @Barbieri:2016uib]. For light nuclei, quantum Monte Carlo (QMC) and, in particular, Green's function Monte Carlo (GFMC) methods have been exploited to carry out calculations of nuclear properties, based on realistic $N\!N$ and $3N$ potentials, and consistent one- and two-body meson-exchange currents [@Carlson:2014vla]. GFMC begins with the construction of a trial wave function $\Psi_T$ that is a symmetrized product of two- and three-body correlation operators acting on an antisymmetric $A$-body single-particle wave function that has the proper quantum numbers for the state of interest. The variational parameters in $\Psi_T$ are found by minimizing the energy expectation value $$E_0 \leq E_T = \frac{\langle \Psi_T | H | \Psi_T \rangle} {\langle \Psi_T | \Psi_T \rangle}\, ,$$ where $E_0$ is the true ground-state energy of the system. The calculation of $E_T$ requires the numerical solution of a multidimensional integral that is carried out employing standard Metropolis Monte Carlo sampling in configuration space.

GFMC then projects out the lowest eigenstate $\Psi_0$ of the given quantum numbers starting from $\Psi_T$ by performing a propagation in imaginary time $\tau$ $$|\Psi_0\rangle = \lim_{\tau \rightarrow \infty} {\rm exp}[-(H-E_0)\tau] |\Psi_T\rangle.$$ The propagation $|\Psi(\tau)\rangle = {\rm exp}[-(H-E_0)\tau] |\Psi_T\rangle$ is carried out as a series of many small imaginary-time steps $\Delta\tau$. Expectation values of operators are evaluated as mixed matrix elements $O(\tau) = \langle \Psi_T | O | \Psi(\tau)\rangle$, and the behavior as a function of $\tau$ analyzed to obtain converged results. Because $H$ and ${\rm exp}[-(H-E_0)\tau]$ commute, the mixed estimate is the exact expectation of $\langle \Psi(\tau/2) | O | \Psi(\tau/2)\rangle$ but linear extrapolations are used to evaluate other quantities.

In addition to binding energies the GFMC provides detailed information on the distribution of nucleons in a nucleus in both coordinate and momentum space, which are interesting in multiple experimental settings. For example, the mixed-estimate of the single-nucleon density is calculated as $$\begin{aligned}
    \rho_{N}(r) &=\frac{1}{4\pi r^2}\big\langle\Psi_T \big|\sum_i \mathcal \delta(r-|\mathbf{r}_i|)P_{N}\big|\Psi(\tau)\big\rangle\,, 
    \label{eq:rho_N}
\end{aligned}$$ where $N=p,n$; $P_{N_i}=\frac{1\pm\tau_{z_i}}{2}$ is the neutron or proton projector operator; and, $\rho_N$ integrates to the number of protons or neutrons. The two-body density distribution, yielding the probability of finding two nucleons with separation $r$, is defined as $$\begin{aligned}
    \rho_{NN}(r) &=\frac{1}{4\pi r^2}\big\langle\Psi_T \big|\sum_{i<j} \mathcal \delta(r-|\mathbf{r}_{ij}|)P_{N_i} P_{N_j} \big|\Psi(\tau)\big\rangle\,.
    \label{eq:rho_NN}
\end{aligned}$$

The positions of the constituents protons and neutrons utilized in the nuclear cascade algorithm are sampled from $36000$ GFMC configurations. We employ the so-called constrained-path approximation [@Wiringa:2000gb] to make sure that their Monte Carlo weights remain positive, thereby facilitating their usage in the cascade algorithm. As a consequence, the single-proton distribution displayed by the blue solid circles of Fig. [1](#fig:density_1b){reference-type="ref" reference="fig:density_1b"} is slightly different from the results reported in Ref. [@Lovato:2013cua], which have been obtained performing fully unconstrained imaginary-time propagations. Since we neglect the charge-symmetry breaking terms in the Hamiltonian, and since $^{12}$C is isospin symmetric, the single-neutron distribution is identical to that of the proton.

For benchmark purposes, we also sample $36000$ mean-field (MF) configurations from the single-proton distribution. The corresponding single-proton densities coincide by construction with the GFMC one, as shown in Fig. [1](#fig:density_1b){reference-type="ref" reference="fig:density_1b"}. However, the differences between GFMC and MF configurations become apparent when comparing the corresponding two-body density distributions represented in Fig. [2](#fig:density_12b){reference-type="ref" reference="fig:density_12b"}. The short-range repulsive core of the $NN$ interaction prevents two nucleons from being close to each other. As a consequence, the $pp$ and $np$ GFMC density distributions are small at short separation distances. Furthermore, the difference between the GFMC $pp$ and $np$ density distributions around $r=1$ fm can be attributed to the strong tensor correlations induced by the one-pion-exchange part of the $NN$ interaction, which is further enhanced by the two-pion-exchange part of the $3N$ potential. Note that the short-range behavior of $\rho_{NN}$, which is largely nucleus independent, does depend strongly on the $NN$ interaction model [@Cruz-Torres:2019fum]. On the other hand, the MF ones do not exhibit this rich behavior as the correlations among nucleons are entirely disregarded.

![Nucleon density in carbon from Green's function Monte Carlo (red) and mean field (blue) configurations. []{#fig:density_1b label="fig:density_1b"}](figures/density_p.pdf){#fig:density_1b width=".53\\textwidth"}

<figure id="fig:density_12b">
<p><embed src="figures/density_pp.pdf" /> <embed src="figures/density_np.pdf" /></p>
<figcaption>Proton-proton (top panel) and proton-neutron (bottom panel) correlation functions in carbon from Green’s function Monte Carlo (red) and mean field (blue) configurations. <span id="fig:density_12b" label="fig:density_12b"></span></figcaption>
</figure>
