---
doc_id: arxiv-2510.21576v1
doc_title: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation"
section_id: sec-002-electron-nucleus-scattering-cross-section
section_title: "Electron-nucleus scattering cross section"
section_number: null
pages: 2-3
source_pdf: 2510.21576v1.pdf
source_sha256: 17a79b59d590c8da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 1.0
doc_brief: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation — 16 sections: Relativistic corrections for lepto; Introduction; Electron-nucleus scattering cross"
---
[]{#sec:xsec label="sec:xsec"}

The inclusive double-differential cross section for electron scattering from a nucleus is written in terms of the longitudinal, $R_L$, and transverse, $R_T$, response functions as: $$\begin{aligned}
\label{eq:diff_cross_section}
    \begin{split}
       \left(\frac{d^2\sigma}{d\varepsilon^\prime d\Omega}\right)_e=&\left(\frac{d\sigma}{d\Omega}\right)_M\left[\left(\frac{Q^2}{{q}^2}\right)^2R_L(q,\omega)\right.
        \\
        &\left.+\left(\tan^2{\frac{\theta}{2}}+\frac{1}{2}\frac{Q^2}{{q}^2}\right) R_T({q},\omega) \right],
    \end{split}
\end{aligned}$$ where $\varepsilon'$ is the electron's final energy and $\Omega$ is the scattering solid angle. The Mott cross section is given by $$\left(\frac{d\sigma}{d\Omega}\right)_M = \left[\frac{\alpha \cos \left(\theta / 2\right)}{2 \varepsilon^{\prime} \sin ^{2}\left(\theta / 2\right)}\right]^{2} \, ,$$ where $\boldsymbol{q}=\boldsymbol{p}_e-\boldsymbol{p}^\prime_e$ and $q$ denote the three-momentum transfer and its magnitude, respectively, and $\boldsymbol{p}_e$ ($\boldsymbol{p}^\prime_e$) is the momentum of the incoming (outgoing) electron. The energy transfer is denoted by $\omega=\varepsilon -\varepsilon^\prime$, while $Q^2=q^2-\omega^2$, and $\theta$ is the electron scattering angle. The longitudinal and transverse response functions of Eq. ([\[eq:diff_cross_section\]](#eq:diff_cross_section){reference-type="ref" reference="eq:diff_cross_section"}) describe the transition from an initial, $| \Psi_0 \rangle$, to a final nuclear state, $| \Psi_f \rangle$, of a nucleus with mass number $A$ and initial (final) energy $E_0$ ($E_f$). Specifically, $$\label{eq:R_L}
R_L(q,\omega) = R^{00}(q,\omega) \, ,$$ and $$\label{eq:R_T}
R_T(q,\omega) = R^{xx}(q,\omega)+R^{yy}(q,\omega) \, ,$$ where $$\begin{aligned}
\label{eq:hardonictensor}
    \begin{split}
        R^{\mu\nu}(\boldsymbol{q},\omega)=&\sum_f\langle \Psi_0 |J^{\mu\dagger}(\boldsymbol{q},\omega)| \Psi_f \rangle\langle \Psi_f |J^\nu(\boldsymbol{q},\omega)| \Psi_0 \rangle
        \\
        &\times\delta(E_0+\omega-E_f)\, ,
    \end{split}
\end{aligned}$$ and the sum runs on all possible final hadronic states, both bound and in the continuum.

The current $J^\mu(\boldsymbol{q},\omega)$ describes the interaction between the probe and the nucleus and it is expanded as a sum of many-nucleon operators as $$J^\mu=\sum_i j^\mu_i+\sum_{i<j} j^\mu_{ij}+\ldots \, ,$$ where $j^\mu_i$ is a one-body operator acting on the $i$-th nucleon and the sum runs over all the nucleons in the system. The two-body component, $j^\mu_{ij}$, acts on nucleon correlated pairs, $ij$, and the corresponding sum goes over all pairs in the system. As in conventional calculations, we neglect terms that act on more than two nucleons and choose $\ensuremath{\boldsymbol{q}}$ to be along the $z$-axis.

The focus of this work is on an improved treatment of the one-body current operators at high values of momentum transfer $q$. For two-body currents, we employ the most recent formulation described at length in Refs. [@Carlson:2014vla; @Bacca:2014tla; @Marcucci:2005zc; @Pastore:2019urn; @Andreoli:2024ovl] and references therein. These will not be discussed further here; interested readers are referred to those sources for more details.

The computational methods used in this work are described in Refs. [@Pastore:2019urn; @Andreoli:2024ovl]. Our calculations employ a nuclear Hamiltonian consisting of the Argonne $v_{18}$ two-nucleon interaction [@Wiringa:1994wb] together with the Urbana IX three-nucleon interaction [@Pudliner:1995wk]. The ground state wave function includes two- and three-body correlations induced by the Hamiltonian.
