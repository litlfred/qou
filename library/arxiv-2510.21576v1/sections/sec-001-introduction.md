---
doc_id: arxiv-2510.21576v1
doc_title: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 2510.21576v1.pdf
source_sha256: 17a79b59d590c8da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.982
---
[]{#sec:intro label="sec:intro"} In recent years, significant progress has been made in calculating inclusive cross sections for lepton scattering from nuclei [@Rocco:2020jlx; @Bacca:2014tla] using the microscopic, or *ab initio*, approach [@10.3389/fphy.2020.00379]. This framework allows for the inclusion of many-nucleon correlations and electroweak currents, which are essential for delivering theoretical predictions that explain the available experimental data. Specifically, nuclear wave functions are determined by solving the many-nucleon Hamiltonian, which typically includes a kinetic term arising from the sum of the kinetic energies of individual nucleons, as well as two- and three-body potentials that describe the correlations between nucleons in pairs and triplets. The interaction with external electroweak probes, such as electrons and neutrinos, is expressed by one- and two-nucleon current operators, which describe the coupling of the probe with individual nucleons and pairs of correlated nucleons.

Due to the increasing computational cost associated with a larger number of nucleons, the *ab initio* method has primarily been applied to light nuclei [@Carlson:1997qn; @Bacca:2014tla; @Carlson:2001mp; @Carlson:1992ga; @Lovato:2015oea; @Lovato:2016gkq; @Lovato:2017cux; @Lovato:2020kba; @Efros:1994iq; @Bacca:2009vp; @Orlandini:2013eya]. Only recently have calculations for systems with a mass number $A=40$ appeared in the literature [@Sobczyk:2023sxh; @Sobczyk:2021dwm]. These studies have highlighted the importance of many-nucleon effects in accurately explaining the available experimental data.

Despite these advancements, there are two key limitations within this approach. First, traditional methods are generally limited to studying inclusive processes. Specifically, these methods rely on integral properties of the nuclear electroweak response functions, which are extracted by unfolding the integral transforms. For example, QMC calculations, specifically Green's Function Monte Carlo (GFMC) calculations, exploit the Euclidean transform [@Carlson:2001mp; @Carlson:1992ga; @Lovato:2015oea; @Lovato:2016gkq; @Lovato:2017cux; @Lovato:2020kba], while the coupled-cluster (CC) approach uses the Lorentz integral transform (LIT) method [@Efros:1994iq; @Bacca:2009vp; @Orlandini:2013eya].

Second, the *ab initio* framework is inherently nonrelativistic, as it solves the many-body Schrödinger equation. Relativistic effects in the electroweak currents are typically treated perturbatively by expanding the covariant single-nucleon currents in powers of $q/m$, where $q$ is the momentum transferred by the external electroweak probe and $m$ is the nucleon mass. Relativistic effects may also be phenomenologically included in two-nucleon correlations. In fact, the two-nucleon interactions typically adopted in QMC calculations, *i.e.*, the Argonne $v_{18}$ [@Wiringa:1994wb], contain parameters that are fitted to nucleon-nucleon scattering data, including data that involve center-of-mass energy up to around $300$ MeV, and reproduce the phase shifts up to $\sim 1$ GeV where relativistic effects may become significant.

Despite the *approximated* inclusions of relativistic effects, this approach fails to agree with the data at high values of momentum transfer. The importance of a proper relativistic treatment of the electroweak currents has recently been highlighted in the context of electron scattering from trinucleon systems [@Andreoli:2021cxo], where QMC-based calculations -- namely the GFMC and the Short-Time-Approximation (STA) -- of cross sections were compared with those obtained with the Spectral Function method [@Benhar:1994hw; @Rocco:2015cil; @Rocco:2018mwt]. The latter adopts fully covariant single nucleon currents and accounts for relativistic kinematics in the final-state energies, thus correctly reproducing the experimental data at high $q$ values, while QMC calculations were in agreement with data up to values of $q\simeq 600$ MeV$/c$.

To address these limitations, two approaches have been explored for incorporating relativistic effects in nonrelativistic *ab initio* QMC calculations. One relies on boost transformations [@PhysRevC.72.011002]. This approach has been applied, for example, in combination with nuclear electroweak responses obtained from GFMC calculations, leading to improvements in the description of scattering at higher momentum transfers [@Rocco:2018tes; @Nikolakopoulos:2023zse].

The second approach, which is the focus of this work, is based on the Short-Time Approximation (STA) [@Pastore:2019urn] factorization scheme, where the external probe interacts only with pairs of correlated nucleons. This enables us to extend the *ab initio* approach for nuclear electroweak responses and cross sections to larger nuclei without losing essential two-nucleon dynamics. The STA has been validated through comparisons with exact theoretical results and experimental data of electron scattering from light nuclei with mass numbers $A=3,\, 4$ and $12$ [@Pastore:2019urn; @Andreoli:2021cxo; @Andreoli:2024ovl; @King:2024zbv], showing good agreement with the data up to values of momentum transfer $q\sim 600$ MeV$/c$. The STA factorization scheme consistently incorporates two-nucleon correlations and currents while isolating the interaction vertex, thus allowing for a direct treatment of relativistic effects.

Specifically, relativistic effects are included in the single-nucleon current operator and in the treatment of the two-nucleon final state kinematics. The nonrelativistic reduction of the covariant single-nucleon electromagnetic current is carried out using an expansion scheme where the momentum transfer $q$ is no longer considered as a small perturbative scale, as in traditional calculations [@Carlson:1997qn; @Pastore:2008ui; @Pastore:2009is; @Pastore:2011ip]. Instead, it assumes that the momentum $q$ carried by the probe can be large and transferred to the scattered nucleon, while only the momentum of the struck nucleon inside the nucleus is small and is treated perturbatively. This approach allows for a more accurate theoretical description of relativistic effects ensuring better agreement with experimental data at high $q$-values. We note that a similar approach has been developed, *e.g.*, in Ref. [@Jeschonnek:1997dm] to study single nucleon electron scattering and $^2$H$(e,e^\prime p)n$ reactions. We will discuss some of the differences in the relevant section.

The theoretical framework developed in this work is directly relevant for current and future experimental programs in neutrino-nucleus scattering [@DUNE:2016hlj; @DUNE:2022aul] and can be extended beyond the light nuclei studied here. Electron scattering provides a valuable testing ground for nuclear models applicable to neutrino physics, due to the wealth of experimental data and the absence of complications related to leptonic energy reconstruction [@Ankowski:2014]. Although the STA has been validated for nuclei up to $A=12$ within the Variational Monte Carlo (VMC) approach, its algorithm can be exported to computational methods utilized to study heavier systems. For the Deep Underground Neutrino Experiment (DUNE), which uses a $^{40}$Ar target, future developments of the STA approach in combination with the Auxiliary Field Diffusion Monte Carlo [@Carlson:2014vla] many-body computational method, will allow for lepton-nucleus studies toward medium-mass nuclei contributing to a better modeling of neutrino-nucleus interactions at the few-GeV energy scale. Continued development of theoretical approaches that properly account for relativistic effects and two-nucleon currents and correlations in nuclear systems beyond the light mass region are required to reduce uncertainties in neutrino energy reconstruction that are crucial for DUNE's oscillation measurements.

Similarly, this framework allows us to address observables measured in ongoing and future electron scattering experiments at Jefferson Lab [@Arrington:2021alx; @Accardi:2023chb]. Extension of the STA framework to compute the cross section measured in short-range correlation experiments [@Arrington:2022sov] as well as Primakoff production of pseudoscalar mesons [@PrimEx:2010fvg] are also possible and will be considered in future works. The development of the *ab-initio* technique such as the STA is crucial to understanding and describing the experiments with light nuclei at Jefferson JLab and in the future at EIC [@AbdulKhalek:2021gbh].

The inclusion of relativistic effects at the vertex within the framework of the STA is the focus of this paper. The paper is organized as follows. Section [1](#sec:xsec){reference-type="ref" reference="sec:xsec"} describes nuclear response functions and inclusive cross sections. In Section [2](#sec:currents){reference-type="ref" reference="sec:currents"}, we discuss the covariant single-nucleon electromagnetic current and its nonrelativistic reduction suitable for large $q$-values. Section [\[sec:STA\]](#sec:STA){reference-type="ref" reference="sec:STA"} outlines the STA method. The relativistic treatment of two-nucleon final state kinematics is discussed in Section [\[sec:relativistic_kinematics\]](#sec:relativistic_kinematics){reference-type="ref" reference="sec:relativistic_kinematics"}. Results and comparisons with experimental data for inclusive electron scattering are provided in Section [\[sec:results\]](#sec:results){reference-type="ref" reference="sec:results"}, while in Section [\[sec:conclusion\]](#sec:conclusion){reference-type="ref" reference="sec:conclusion"} we summarize our conclusions and outline the next stage in this program of extending the kinematic reach of the STA.

# Electron-nucleus scattering cross section {#sec:xsec}

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

# One-Body Electromagnetic Current {#sec:currents}

The covariant relativistic expression for the one-body electromagnetic current operator is given by [@Carlson:1997qn] $$\begin{aligned}
\label{eq:relvector}
    j^\mu=\bar{u}(\boldsymbol{p}^\prime s')\left[{F}_1\gamma^\mu+i\sigma^{\mu\nu}q_\nu\frac{{F}_2}{2m}\right]u(\boldsymbol{p}s),
\end{aligned}$$ where $\boldsymbol{p}$ ($\boldsymbol{p}^\prime$) is the initial (final) nucleon momentum with mass $m$ and spin $s$ ($s'$) and we omit, here and in the following, the index that specifies the $i$-th nucleon. The Dirac spinors and gamma matrices are denoted by $u$ and $\gamma^\mu$, respectively, with $\bar{u}=u^\dagger \gamma^0$ and $\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu]$. The $4$-vector energy-momentum transfer is given by $q^\nu=(\omega,\ensuremath{\boldsymbol{q}})$.

The Dirac and Pauli form factors [@Hyde-Wright:2004], ${F}_1(Q^2)$ and $F_2(Q^2)$, characterize the electromagnetic structure of the nucleon and are expressed in terms of the electric and magnetic Sachs form factors $G_{E/M}^{p,n}(Q^2)$ [@Ernst:1960] of the proton and neutron, $$\begin{aligned}
\label{eq:sachs}
    F_1^{p,n}=\frac{G_E^{p,n}+\tau G_M^{p,n}}{1+\tau},\quad F_2^{p,n}=\frac{G_M^{p,n}-G_E^{p,n}}{1+\tau},
\end{aligned}$$ where $\tau=Q^2/4m^2$ is a kinematic factor. The nucleon's identity -- whether it is a proton ($p$) or a neutron ($n$) -- is specified by the nucleon isopsin projection operator $(1\pm\tau_z)/2$, with $\tau_z$ denoting the third component of the nucleon isospin operator. In what follows, for ease of reading, we omit the $p/n$ superscript and implicitly assume the appropriate isospin projection operator acting on the nucleon.

## Low-momentum transfer nonrelativistic reduction

Traditional many-body calculations [@Carlson:1997qn; @Bacca:2014tla] adopt a nonrelativistic reduction of the single-nucleon covariant current given in Eq. ([\[eq:relvector\]](#eq:relvector){reference-type="ref" reference="eq:relvector"}). The expansion is based on the assumption that both $p$ and $p'$ (and thus $q$) are small compared to the nucleon mass. At leading order (LO), this approach leads to the following expressions in coordinate space for the charge, $\rho=j^0$, and current, $\boldsymbol{j}_\perp$, operators: $$\begin{aligned}
 \label{eq:charge_NR_LO}
    \rho=&{G_E} e^{i\boldsymbol{q}\cdot\boldsymbol{r}} \, ,
\end{aligned}$$ $$\begin{aligned}
 \label{eq:transverse_NR_LO}
\boldsymbol{j}_\perp=&e^{i\boldsymbol{q}\cdot\boldsymbol{r}}\left[\frac{G_E}{m}\boldsymbol{p}^\perp-i\frac{G_M}{2m}(\boldsymbol{q}\times\boldsymbol{\sigma})\right] \, ,
\end{aligned}$$ where $\ensuremath{\boldsymbol{O}}^\perp = \ensuremath{\boldsymbol{O}}-(\ensuremath{\boldsymbol{O}}\cdot\hat{\ensuremath{\boldsymbol{q}}}) \hat{\ensuremath{\boldsymbol{q}}}$ is the component of the operator $\ensuremath{\boldsymbol{O}}$ perpendicular to the momentum transfer $\ensuremath{\boldsymbol{q}}$, and $\boldsymbol{r}$ is its spatial coordinate. Additionally, in coordinate space $\ensuremath{\boldsymbol{p}} = -i \nabla$ and acts directly on the wave function (for sub-leading terms involving powers of $\ensuremath{\boldsymbol{p}}$, particular care must be taken when performing the Fourier transform from momentum to coordinate space).

Typically, in addition to the LO term given above, the single-nucleon charge operator includes the Darwin-Foldy and spin-orbit terms, also accounting for relativistic effects [@Carlson:1997qn]: $$\begin{aligned}
\label{eq:charge_DF}
    \rho=&\left[\frac{G_E}{\sqrt{1+Q^2/4m^2}}
    -i\frac{2G_M-G_E}{4m^2}\boldsymbol{q}\cdot(\boldsymbol{\sigma}\times\boldsymbol{p})\right] e^{i\boldsymbol{q}\cdot\boldsymbol{r}}   \, .
\end{aligned}$$

Using the expansion parameter discussed above, that is $q/m \sim p/m \sim p'/m \ll 1$, subleading terms of the one-body charge and current operators, beyond LO, have been derived, *e.g.*, in Refs. [@Pastore:2009is; @Pastore:2011ip]. However, the expansion is limited to low-momentum-transfer kinematics and consequently fails to accurately describe processes at high energy. An appropriate expansion scheme for these regimes is described in the next subsection.

## High-momentum transfer nonrelativistic reduction {#sec:relativistic_current}

For momentum transfer $q \sim m$ or greater, relativistic effects become important in two main ways. First, the electromagnetic current operators require a proper nonrelativistic reduction. Second, the final states, which play a significant role in the nuclear response functions, may include high-momentum knocked-out nucleons, whose kinetic energies should be calculated relativistically for accurate results. In this section, we focus on determining the nonrelativistic reduction of the electromagnetic currents at high-momentum transfer. The results obtained here are general and applicable in any microscopic modeling of the nucleus. The treatment of final states' relativistic kinematics within the STA framework is discussed separately in Sec. [\[sec:relativistic_kinematics\]](#sec:relativistic_kinematics){reference-type="ref" reference="sec:relativistic_kinematics"}.

Our starting point is the covariant expression of the one-body current operator given in Eq. ([\[eq:relvector\]](#eq:relvector){reference-type="ref" reference="eq:relvector"}). At low-momentum transfer $q$, its nonrelativistic reduction at leading order is given in Eqs. [\[eq:charge_NR_LO\]](#eq:charge_NR_LO){reference-type="eqref" reference="eq:charge_NR_LO"} and [\[eq:transverse_NR_LO\]](#eq:transverse_NR_LO){reference-type="eqref" reference="eq:transverse_NR_LO"} which are accurate for $q\ll m$. Sub-leading terms extend the currents' validity up to moderate $q$, but the expansion breaks down at larger momenta since it assumes $q/m\ll1$. Even the inclusion of sub-leading terms fails to overcome this limitation. To address this, we adopt a different strategy -- introduced in Ref. [@Jeschonnek:1997dm] -- in which only the initial nucleon momentum $p$ is assumed to be small. This is justified in the quasi-elastic kinematic regime where the struck nucleon is initially at low momentum but receives a momentum $q$ from the probing lepton, which can be large. Thus, we avoid the assumption that the nucleon final momentum $p^\prime$ is small and expand the covariant current only in $p/m$. The resulting expressions are then valid for any value of momentum transfer $q$ provided that $p/m\ll1$.

To carry out this nonrelativistic reduction we begin by defining the spinors and their normalizations $$\label{eq:spinor}
u(\ensuremath{\boldsymbol{p}}s) = N(p) \begin{pmatrix}
           1 \\
           \frac{\ensuremath{\boldsymbol{\sigma}}\cdot \ensuremath{\boldsymbol{p}}}{E+m} 
         \end{pmatrix}
\chi_s \, ,$$ where $\chi_s$ and $E=\sqrt{p^2+m^2}$ are the nucleon spin state and energy, respectively, while $N$ is a normalization factor chosen so that $u^\dagger u = 1$. Specifically, for a nucleon with momentum $p$ and energy $E$, the normalization factor reads: $$\label{eq:N_p}
N(p) = \sqrt{\frac{E+m}{2E}}  \, .$$ An expansion of the normalization factor in $p/m$ yields $N(p) \rightarrow 1$ at leading order.

For the final state, where $\ensuremath{\boldsymbol{p'}}=\ensuremath{\boldsymbol{p}}+\ensuremath{\boldsymbol{q}}$, we make no assumption on the size of $p^\prime$ and $q$. Thus, at leading order the normalization factor of the final nucleon spinor reads: $$\label{eq:N_p'}
N(p^\prime)=\sqrt{\frac{E^\prime+m}{2E^\prime}} \rightarrow  \sqrt{\frac{\sqrt{q^2+m^2}+m}{2\sqrt{q^2+m^2}}} \equiv \alpha(q) \, .$$ Sub-leading corrections arise from further expanding in $p/m$.

This expansion scheme is also applied to the factors $(E+m)^{-1}$ and $(E'+m)^{-1}$ entering the spinors, and to the energy transfer $\omega$ defined as: $$\label{eq:omega}
\omega=E'-E = \sqrt{p'^2+m^2}-\sqrt{p^2+m^2} \, .$$ We note that this formulation assumes that both the initial and final nucleons are on-shell. While different conventions exist, the impact of off-shell corrections near the quasi-elastic peak is expected to be minimal [@DeForest:1983].

The nucleon form factors ${F}_1(Q^2)$ and $F_2(Q^2)$ appearing in the covariant expression of the electromagnetic current -- Eq. ([\[eq:relvector\]](#eq:relvector){reference-type="ref" reference="eq:relvector"}) -- must also be treated consistently since they depend on the nucleon momentum through $Q^2$. At leading order in $p/m$, this effectively corresponds to evaluating the form factors at the quasi-elastic peak, that is at $p=0$, or equivalently at $Q^2=Q_{qe}^2$ with $$Q^2_{qe}=2m\left(\sqrt{q^2+m^2}-m\right) \, .$$ Then the form factor expressions become: $$G_E(Q^2_{qe}) = F_1(Q^2_{qe})-\tau_{qe} F_2(Q^2_{qe}) \, ,$$ $$G_M(Q^2_{qe})=F_1(Q^2_{qe})+F_2(Q^2_{qe}) \, ,$$ with $$\tau_{qe}= \frac{Q^2_{qe}}{4m^2} =
\frac{\sqrt{q^2+m^2}-m}{2m}  \, .$$

By expanding the covariant electromagnetic current in $p/m$ while treating the momentum transfer $q$ exactly, we obtain the following expressions at leading order (LO), $\sim (p/m)^0$: $$\begin{aligned}
\label{eq:rho_p0}
\rho^{(0)} &=& \alpha(q) G_E(Q^2_{qe})e^{i\boldsymbol{q}\cdot\boldsymbol{r}}\, ,\\
\label{eq:current_p0}
\ensuremath{\boldsymbol{j}}_\perp^{(0)}  &=&
\frac{2m\tau_{qe}}{q^2} G_M(Q^2_{qe}) \alpha(q)   i  (\ensuremath{\boldsymbol{\sigma}} \times \ensuremath{\boldsymbol{q}}) e^{i\boldsymbol{q}\cdot\boldsymbol{r}}\, .
\end{aligned}$$

The next-to-leading-order (NLO) expressions include terms of the order $\sim(p/m)^1$ and are given by:

::: widetext
$$\begin{aligned}
\label{eq:rho_p1}
\rho^{(1)} & = & \frac{\alpha(q) \tau_{qe}}{m^2(2\tau_{qe}+1)^2(\tau_{qe}+1)} \left[
(2\tau_{qe}+1) G_M   - \tau_{qe}G_E  \right] \ensuremath{\boldsymbol{q}}\cdot \ensuremath{\boldsymbol{p}}
-
\frac{\alpha(q)}{(\tau_{qe}+1)} \frac{2G_M - G_E}{4m^2} 
i\ensuremath{\boldsymbol{q}}\cdot(\ensuremath{\boldsymbol{\sigma}}\times\ensuremath{\boldsymbol{p}})\, ,     \\
\ensuremath{\boldsymbol{j}}^{(1)}_\perp &= &
 \left\{ 
 \frac{\alpha(q)}{m(\tau_{qe}+1)} \left[  G_E
+ \frac{\tau_{qe}  }{2} G_M \right]
\right\} \ensuremath{\boldsymbol{p}}^\perp
+
 \left\{ 
  \frac{\alpha(q) \tau_{qe}}{m(\tau_{qe}+1)} 
  \left[ \frac{1}{2}G_E - G_M \right]
\right\}   i(\ensuremath{\boldsymbol{\sigma}} \times \ensuremath{\boldsymbol{p}})^\perp
 \nonumber \\ &+&
\left\{ 
\frac{\alpha(q)}{4m^3(\tau_{qe}+1)^2 (2\tau_{qe}+1)^2} \left[
 - G_E \frac{1}{2}(2\tau_{qe} +1)^2 
+G_M (2\tau_{qe}^2-1)
\right]
\right\} \left(\ensuremath{\boldsymbol{p}}\cdot\ensuremath{\boldsymbol{q}}\right)(i\ensuremath{\boldsymbol{\sigma}}\times\ensuremath{\boldsymbol{q}}) 
\nonumber \\ &+&
\left\{ 
 \frac{\alpha(q)}{8m^3(\tau_{qe}+1)^2}
(G_M-G_E)
\right\} ( \ensuremath{\boldsymbol{\sigma}}\cdot\ensuremath{\boldsymbol{q}})(i\ensuremath{\boldsymbol{q}}\times\ensuremath{\boldsymbol{p}}) \, ,
\label{eq:current_p1}
\end{aligned}$$
:::

where we dropped the overall $e^{i\boldsymbol{q}\cdot\boldsymbol{r}}$ factor for ease of reading. Note that also at NLO the Sachs form factors are evaluated at the quasielastic peak, so in the equations above $G_{E/M}\equiv G_{E/M}(Q_{qe}^2)$. Corrections beyond this approximation will appear at the next order.

The nucleonic form factors $G_{E/M}$ are described by empirical functions, typically constrained through fits to experimental data. In principle, their expansion around the quasielastic peak introduces terms that should be included for consistency. For example, terms linear in $p$, when combined with the operator structures of Eqs. [\[eq:rho_p0\]](#eq:rho_p0){reference-type="eqref" reference="eq:rho_p0"} and [\[eq:current_p0\]](#eq:current_p0){reference-type="eqref" reference="eq:current_p0"}, would contribute at NLO. While these contributions could be determined explicitly for a given parameterization, this lies beyond the scope of this work.

The expansion presented here closely follows the approach developed in Ref. [@Jeschonnek:1997dm], but for some differences arising from the use of different conventions. In particular, we adopt the normalization condition $u^\dagger u =1$, which leads to the normalization factor given in Eq. [\[eq:N_p\]](#eq:N_p){reference-type="eqref" reference="eq:N_p"}. The same convention is effectively used, for example, in Ref. [@Krebs:2019aka] (see Eqs. (2.2), (2.3), and (2.5) therein). This convention is consistent with the definition of cross section given in Eq. [\[eq:diff_cross_section\]](#eq:diff_cross_section){reference-type="eqref" reference="eq:diff_cross_section"}. Ref. [@Jeschonnek:1997dm], on the other hand, uses the normalization factor $N=\sqrt{(E+m)/(2m)}$, a convention also adopted in Ref. [@Amaro:1995kk] (see Eq. (A.6) in that reference). As a result, their corresponding expression for the cross section includes additional kinematics factors compared with the definition given in Eq. [\[eq:diff_cross_section\]](#eq:diff_cross_section){reference-type="eqref" reference="eq:diff_cross_section"}.

While the different conventions lead to distinct expressions in the response functions and currents, they do not affect the cross sections at LO in $p/m$. For example, Ref. [@Jeschonnek:1997dm] reports an increase in the longitudinal response function (relative to the longitudinal response calculated with the LO charge operator of Eq. [\[eq:charge_NR_LO\]](#eq:charge_NR_LO){reference-type="eqref" reference="eq:charge_NR_LO"} obtained by expanding in $q/m$), whereas we find a decrease. Despite this, the corresponding cross sections agree at this order. Another difference that affects the formal expressions at NLO and beyond is related to the treatment of the energy transfer $\omega$ given in Eq. [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"}, which we expand to allow for a more efficient implementation in QMC calculations.

As a consistency check, we have verified that our conventions for both the spinor normalization and the cross-section reproduce the well-known Rosenbluth cross section in the limit of a single nucleon at rest in the initial state. This verification is detailed in App. [\[sec:ros_cross_section\]](#sec:ros_cross_section){reference-type="ref" reference="sec:ros_cross_section"}

Here, we have focused exclusively on the one-body current operator. A similar treatment should be in principle applied to two-body currents. However, within the low-momentum transfer expansion scheme, the two-body vector and charge currents scale as $p/m$ [@Pastore:2011ip; @Krebs:2019aka], therefore, corrections to their standard formulations are expected to be small overall. For an expansion of two-body meson exchange currents see, *e.g.*, Ref. [@Amaro:1998ta].

## Comparing low- and high-momentum transfer nonrelativistic reductions {#sec:comparing}

In this section, we compare the low-momentum transfer nonrelativistic reduction at LO of the single nucleon charge and current operators -- given in Eqs. [\[eq:charge_NR_LO\]](#eq:charge_NR_LO){reference-type="eqref" reference="eq:charge_NR_LO"} and [\[eq:transverse_NR_LO\]](#eq:transverse_NR_LO){reference-type="eqref" reference="eq:transverse_NR_LO"} -- with the corresponding expressions obtained in the high-momentum transfer regime -- Eqs. [\[eq:rho_p0\]](#eq:rho_p0){reference-type="eqref" reference="eq:rho_p0"} and [\[eq:current_p0\]](#eq:current_p0){reference-type="eqref" reference="eq:current_p0"}.

We start with the charge operator. Here, the main difference is the additional factor $\alpha(q)$ in the LO high-$q$ result of Eq. [\[eq:rho_p0\]](#eq:rho_p0){reference-type="eqref" reference="eq:rho_p0"}. Since $\alpha(q) \rightarrow 1$ for $q\rightarrow 0$, the two results coincide for $q\ll m$. However, $\alpha(q)<1$ for all values of $q$, and its deviation from unity increases with increasing $q$, leading to a suppression in the longitudinal response at LO. Specifically, the longitudinal response -- which involves a current-current correlator -- scales as $\alpha(q)^2$ in the high-$q$ expansion scheme, whereas in the low-$q$ reduction the scaling prefactor is simply one. The ratio of the longitudinal responses obtained in the two different schemes, namely $$\frac{R_L^{\rm high-q}}{R_L^{\rm low-q}}\propto \alpha(q)^2 \, ,$$ is plotted in Fig. [1](#fig:R_L_factors){reference-type="ref" reference="fig:R_L_factors"} as a function of $q$. The reduction becomes increasingly pronounced at high $q$. For example, $\alpha^2=0.9$ for $q=700$ MeV$/c$, and $\alpha^2=0.77$ for $q=1500$ MeV/$c$, and, in the limit of $q\gg m$, $\alpha^2\rightarrow 1/2$.

We can also compare the low-$q$ result at LO with the Darwin-Foldy contribution to the charge operator, given by the first term in Eq. [\[eq:charge_DF\]](#eq:charge_DF){reference-type="eqref" reference="eq:charge_DF"}. In this case, the resulting ratio of longitudinal responses is proportional to $$\frac{R_L^{\rm DF}}{R_L^{\rm low-q}}\propto \frac{1}{(1+Q_{qe}^2/4m^2)}\, ,$$ and it is also plotted in Fig. [1](#fig:R_L_factors){reference-type="ref" reference="fig:R_L_factors"} for comparison. The LO high-$q$ expression (solid blue line) and the Darwin-Foldy (orange dashed line) term agree well up to moderate values of momentum transfer. Differences arise at $q\gtrsim 500$ MeV/$c$. In this regime, the Darwin-Foldy prefactor decreases more rapidly than $\alpha(q)$, resulting in a stronger suppression in the longitudinal response. Consequently, the high-$q$ nonrelativistic reduction leads to comparatively larger longitudinal response functions. For example, at $q=1500$ MeV$/c$ there is a $\sim10\%$ enhancement. Moreover, in the limit of $q\gg m$, the Darwin-Foldy term goes to zero, unlike $\alpha^2(q)$, leading to significant differences.

<figure id="fig:R_L_factors">
<div class="center">
<embed src="figures/R_L_factors.pdf" />
</div>
<figcaption><span id="fig:R_L_factors" label="fig:R_L_factors"></span> Ratio of the longitudinal responses obtained using: <span><em>i</em></span>) the high- and low-<span class="math inline"><em>q</em></span> expansion schemes for the one-body charge orator at LO (blue solid line); and <span><em>ii</em></span>) the Darwin-Foldy correction to the charge operator and the low-<span class="math inline"><em>q</em></span> expansion at LO (orange dashed line). See text for explanation.</figcaption>
</figure>

We now turn our attention to the transverse current operator and compare its LO low-momentum transfer expression, Eq. [\[eq:transverse_NR_LO\]](#eq:transverse_NR_LO){reference-type="eqref" reference="eq:transverse_NR_LO"}, with the LO high-momentum result, Eq. [\[eq:current_p0\]](#eq:current_p0){reference-type="eqref" reference="eq:current_p0"}. In the limit of $q\rightarrow 0$, the factor $(2m\tau_{qe})/q^2\rightarrow 1/2m$, and the expression in Eq. [\[eq:current_p0\]](#eq:current_p0){reference-type="eqref" reference="eq:current_p0"} reduces to the second term in Eq. [\[eq:transverse_NR_LO\]](#eq:transverse_NR_LO){reference-type="eqref" reference="eq:transverse_NR_LO"}. The first term in Eq. [\[eq:transverse_NR_LO\]](#eq:transverse_NR_LO){reference-type="eqref" reference="eq:transverse_NR_LO"}, proportional to $\boldsymbol{p}^\perp$, appears at next-to-leading-order in the high-$q$ reduction and is expected to contribute less at large momentum transfer. Its coefficient matches the corresponding term in Eq. [\[eq:current_p1\]](#eq:current_p1){reference-type="eqref" reference="eq:current_p1"} in the $q\rightarrow 0$ limit.

Focusing on the dominant contributions at large $q$, the prefactor $(2m\tau_{qe})\alpha(q)/q^2$ in the LO high-$q$ expansion should be compared to the factor $1/2m$ appearing in Eq. [\[eq:transverse_NR_LO\]](#eq:transverse_NR_LO){reference-type="eqref" reference="eq:transverse_NR_LO"}. Therefore, the relative suppression factor in the LO transverse response function is $$\frac{R_T^{\rm high-q}}{R_T^{\rm low-q}}\propto\left( \frac{4m^2\tau_{qe} \alpha(q)}{q^2} \right)^2.$$ This factor, plotted in Fig. [2](#fig:R_T_factors){reference-type="ref" reference="fig:R_T_factors"}, is always less than one and decreases with increasing values of $q$, leading to a suppression of the transverse response. Already at $q\approx 400$ MeV/$c$ the suppression is around $10\%$. At $q=700$ MeV/$c$, the factor is $\sim 0.71$, and it drops to $\sim0.37$ at $q=1500$ MeV$/c$.

In the limit of $q\gg m$, the factor scales as $2m^2/q^2$, vanishing for large $q$. This leads to a significant reduction in the transverse response function due to relativistic effects -- an effect that cannot be captured by the low-$q$ nonrelativistic reduction.

<figure id="fig:R_T_factors">
<div class="center">
<embed src="figures/R_T_factors.pdf" />
</div>
<figcaption> <span id="fig:R_T_factors" label="fig:R_T_factors"></span> Ratio of the transverse responses obtained using the LO high-<span class="math inline"><em>q</em></span> and LO low-<span class="math inline"><em>q</em></span> expansion schemes for the one-body current operator. See text for explanations.</figcaption>
</figure>
