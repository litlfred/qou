---
doc_id: arxiv-2510.21576v1
doc_title: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation"
section_id: sec-005-high-momentum-transfer-nonrelativistic-reduction
section_title: "High-momentum transfer nonrelativistic reduction"
section_number: null
pages: 4-5
source_pdf: 2510.21576v1.pdf
source_sha256: 17a79b59d590c8da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.997
doc_brief: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation — 16 sections: Relativistic corrections for lepto; Introduction; Electron-nucleus scattering cross"
---
[]{#sec:relativistic_current label="sec:relativistic_current"} For momentum transfer $q \sim m$ or greater, relativistic effects become important in two main ways. First, the electromagnetic current operators require a proper nonrelativistic reduction. Second, the final states, which play a significant role in the nuclear response functions, may include high-momentum knocked-out nucleons, whose kinetic energies should be calculated relativistically for accurate results. In this section, we focus on determining the nonrelativistic reduction of the electromagnetic currents at high-momentum transfer. The results obtained here are general and applicable in any microscopic modeling of the nucleus. The treatment of final states' relativistic kinematics within the STA framework is discussed separately in Sec. [\[sec:relativistic_kinematics\]](#sec:relativistic_kinematics){reference-type="ref" reference="sec:relativistic_kinematics"}.

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
