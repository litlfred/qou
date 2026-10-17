---
doc_id: arxiv-2510.21576v1
doc_title: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation"
section_id: sec-002-short-time-approximation
section_title: "Short-time approximation"
section_number: null
pages: 6-8
source_pdf: 2510.21576v1.pdf
source_sha256: 17a79b59d590c8da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.994
---
[]{#sec:STA label="sec:STA"}

In this section, we briefly sketch the Short-Time-Approximation (STA) algorithm in the context of Variational Monte Carlo calculations and defer the interested reader to Refs. [@Pastore:2019urn; @Andreoli:2024ovl] for more details. We also compare our results with those of Refs. [@Pastore:2019urn; @Andreoli:2021cxo], which used the low-$q$ nonrelativistic reduction of the single-nucleon covariant current.

The STA evaluates the response functions within a factorization scheme that includes two-nucleon dynamics at the interaction vertex [@Pastore:2019urn]. The response function, Eq. [\[eq:hardonictensor\]](#eq:hardonictensor){reference-type="eqref" reference="eq:hardonictensor"}, can be expressed as $$\begin{aligned}
\begin{split}
    R^{\mu\nu}(\boldsymbol{q},\omega)=&\int_{-\infty}^\infty\frac{dt}{2\pi}e^{i(\omega+E_0)t}
    \\
    &\times\langle \Psi_0 |J^{\mu\dagger}(\boldsymbol{q},\omega)e^{-iHt}J^\nu(\boldsymbol{q},\omega)| \Psi_0 \rangle\, ,
    \end{split}
\end{aligned}$$ where the sum over the final states and the energy-conserving delta are replaced by the real-time propagator. For short times, the propagator can be expanded to retain only correlations involving two nucleons that interact with the probe via one- and two-body currents. The corresponding current-current correlator is approximated as:

$$\begin{aligned}
 \label{eq:currcurrcorr}
    \begin{split}
        J^{\mu\dagger}e^{-iHt}J^\nu\approx&\sum_i j^{\mu\dagger}_ie^{-i\,h_{ij}t}j^\nu_i+\sum_{i\neq j}j^{\mu\dagger}_ie^{-i\,h_{ij}t}j^\nu_j
        \\
        &+\sum_{i\neq j}\left(j_i^{\mu\dagger}e^{-i\,h_{ij}t}j_{ij}^\nu+j^{\mu\dagger}_{ij}e^{-i\,h_{ij}t}j_i^\nu\right)
        \\
        &+\sum_{i<j} j_{ij}^{\mu\dagger}e^{-i\,h_{ij}t}j_{ij}^\nu \, , 
    \end{split}
\end{aligned}$$ where $h_{ij}=t_i+t_j+v_{ij}$ includes the single-nucleon kinetic energies and the two-body interaction $v_{ij}$, the Argonne $v_{18}$ in the present study. The second line represents the so called *interference term* between one- and two-body currents, which is known to provide important corrections to the transverse response function [@Carlson:2001mp].

Because the correlated $ij$ pair is factorized from the remaining $A-2$ nucleons, the response function can be written in terms of a response density $D(e,E_{\mathrm{c.m.}})$: $$\begin{aligned}
\label{eq:integration_eE}
    \begin{split}
    R^{\mu\nu}=&\int de\int_0^\infty dE_{\mathrm{c.m.}}D^{\mu\nu}(e,E_{\mathrm{c.m.}})
    \\
    &\times\delta(\omega+E-e-E_{\mathrm{c.m.}}) \, .
    \end{split}
\end{aligned}$$ where $e$ is the relative energy of the active pair, $E_{\mathrm{c.m.}}$ its center-of-mass energy in the final state, and $E$ its average initial energy (set to zero in the present work).

The corresponding response density involves the two-nucleon propagator $g$: $$\begin{aligned}
\label{eq:density_eE}
D^{\mu\nu}&(e,E_{\mathrm{c.m.}}) =
4 m^{3/2} \sqrt{E_{\mathrm{c.m.}}} 
\int d^3R' d^3r' d^3R d^3r d^{3}R_{A-2}
\nonumber \\ & \times
\sum_{\alpha_{A-2}} 
\sum_{\alpha_1,\alpha_2}
\sum_{\alpha_1',\alpha_2'}
\Big[ \langle \Psi_i | j_L^{\mu\dagger} | \ensuremath{\boldsymbol{R}}', \ensuremath{\boldsymbol{r}}' ,\alpha_1' \alpha_2', \ensuremath{\boldsymbol{R}}_{A-2}, \alpha_{A-2} \rangle
\nonumber \\ &\times
g(e,E_{\mathrm{c.m.}},\ensuremath{\boldsymbol{r}},\ensuremath{\boldsymbol{r}}',\ensuremath{\boldsymbol{R}},\ensuremath{\boldsymbol{R}}',\alpha_1,\alpha_2,\alpha_1',\alpha_2')
\nonumber \\ &\times
\langle \ensuremath{\boldsymbol{R}}, \ensuremath{\boldsymbol{r}} ,\alpha_1 \alpha_2, \ensuremath{\boldsymbol{R}}_{A-2} , \alpha_{A-2} | 
 j_R^\nu | \Psi_i \rangle \Big]\, ,
\end{aligned}$$ where $\ensuremath{\boldsymbol{r}}$ and $\ensuremath{\boldsymbol{r}}'$ describe the relative coordinate of the active pair, $\ensuremath{\boldsymbol{R}}$ and $\ensuremath{\boldsymbol{R}}'$ its c.m. coordinate, and $\alpha_1$, $\alpha_1'$, $\alpha_2$ and $\alpha_2'$ the spin and isospin of the pair. $\ensuremath{\boldsymbol{R}}_{A-2}$ is for the location of the remaining particles and $\alpha_{A-2}$ for their spin and isospin. The abbreviated notation with $j_L$ and $j_R$ is used to indicate the sum of all contributions from Eq. [\[eq:currcurrcorr\]](#eq:currcurrcorr){reference-type="eqref" reference="eq:currcurrcorr"}.

In its full form, the propagator $g$ includes continuum and bound two-nucleon states of the Argonne $v_{18}$, thus ensuring consistency between the two-nucleon correlations and two-nucleon electromagnetic currents at the interaction vertex, required for a consistent determination of the interference term [@Pastore:2019urn].

In the present work, however, we employ a simplified free-propagator where final state interactions are neglected and the nucleons in the final state are described by plane-waves. This approximation allows us to focus on relativistic corrections at the one-body vertex but it introduces an inconsistency: the interference term between one- and two-body currents is no longer treated consistently with two-nucleon correlations. The effects of this inconsistency and the improvement expected when using a correlated-propagator are discussed in Ref. [@Pastore:2019urn] and will be revisited in future work.

Using a free-propagator, the response density reduces to: $$\begin{aligned}
&D^{\mu\nu}(e,E_{\mathrm{c.m.}}) =
2 m^3 \sqrt{e E_{\mathrm{c.m.}}} 
\int d^3R' d^3r' d^3R d^3r d^{3}R_{A-2}
\nonumber \\ & \times
 \sum_{\alpha} \Big[
\langle \Psi_i | j_L^{\mu\dagger} | \ensuremath{\boldsymbol{R}}', \ensuremath{\boldsymbol{r}}', \ensuremath{\boldsymbol{R}}_{A-2}, \alpha \rangle
\nonumber \\ &\times
g(e,E_{\mathrm{c.m.}},|\ensuremath{\boldsymbol{r}}-\ensuremath{\boldsymbol{r}}'|,|\ensuremath{\boldsymbol{R}}-\ensuremath{\boldsymbol{R}}'|)
\langle \ensuremath{\boldsymbol{R}}, \ensuremath{\boldsymbol{r}} , \ensuremath{\boldsymbol{R}}_{A-2} , \alpha | 
 j_R^\nu | \Psi_i \rangle \Big]\, ,
\end{aligned}$$ where $\alpha$ denotes the spin and isospin degrees of freedom of all $A$ nucleons, with a real-time propagator now given by: $$\begin{aligned}
&g(e,E_{\mathrm{c.m.}},|\ensuremath{\boldsymbol{r}}-\ensuremath{\boldsymbol{r}}'|,|\ensuremath{\boldsymbol{R}}-\ensuremath{\boldsymbol{R}}'|)
\nonumber \\ &=
\frac{1}{4\pi^4}
 j_0\left(\sqrt{4m E_{\mathrm{c.m.}}}|\ensuremath{\boldsymbol{R}}'-\ensuremath{\boldsymbol{R}}|\right)
j_0\left(\sqrt{me}\left|\ensuremath{\boldsymbol{r}}'-\ensuremath{\boldsymbol{r}}\right|\right)\, ,
\end{aligned}$$ where $j_0$ is the zeroth-order spherical Bessel function.

# Relativistic Final-States Kinematics {#sec:relativistic_kinematics}

We now turn our attention to relativistic effects in the energies of the active nucleons in the final state. Since we are restricting our attention to the quasi-elastic peak, the dominant contribution to the cross section arises from electrons scattering from low-momentum nucleons in the ground state. Relativistic effects in the treatment of the ground state wave function are therefore not considered. They may become important in kinematics that probe large-momentum initial-state nucleons, for example in experiments studying short-range correlations [@Hen:2016kwk]. Similarly, we do not include relativistic corrections to the final-state wave functions, but only to the energies of the active nucleons in the final state.

Kinematical relativistic effects of this kind cannot be easily introduced in most *ab initio* methods, such as the GFMC, which are inherently nonrelativistic. The STA, however, allows their implementation due to the factorization of the final states. Specifically, relativistic expressions for the energies of the two active nucleons are introduced in the energy-conserving delta function $\delta(\omega+E-e-E_{\mathrm{c.m.}})$ appearing in Eq. [\[eq:integration_eE\]](#eq:integration_eE){reference-type="eqref" reference="eq:integration_eE"}. This requires expressing the response density in terms of the single-particle momenta (or energies) rather than the corresponding relative and c.m. variables. The latter could be recovered with the inclusion of the angular dependence between the nucleon momenta, a development that is underway.

With the free-propagator, the response function in terms of the single-nucleon momenta, $p_1$ and $p_2$, becomes: $$\begin{aligned}
\label{eq:integration_k1k2}
    \begin{split}
    R^{\mu\nu}=&\int_0^\infty dp_1 \int_0^\infty dp_2 D^{\mu\nu}(p_1,p_2)
    \\
    &\times\delta\left(\omega+E-\sqrt{p_1^2+m^2}-\sqrt{p_2^2+m^2}+2m\right)\, ,
    \end{split}
\end{aligned}$$ where the response density reads: $$\begin{aligned}
\label{eq:density_p1p2}
D^{\mu\nu}&(p_1,p_2) =
p_1^2 p_2^2
\sum_{\alpha} \int d^3r_1' d^3r_2' d^3r_1 d^3r_2 d^3R_{A-2}
\nonumber \\ & \times
\langle \Psi_i | j_L^{\mu\dagger} | \ensuremath{\boldsymbol{r}}_1', \ensuremath{\boldsymbol{r}}_2', \ensuremath{\boldsymbol{R}}_{A-2}, \alpha \rangle
\nonumber \\ &\times
g(p_1,p_2,|\ensuremath{\boldsymbol{r}}_1-\ensuremath{\boldsymbol{r}}_1'|,|\ensuremath{\boldsymbol{r}}_2-\ensuremath{\boldsymbol{r}}_2'|)
\nonumber \\ &\times
\langle \ensuremath{\boldsymbol{r}}_1, \ensuremath{\boldsymbol{r}}_2 , \ensuremath{\boldsymbol{R}}_{A-2}, \alpha| 
 j_R^\nu | \Psi_i \rangle\, ,
\end{aligned}$$ with the free-propagator given by: $$\begin{aligned}
\label{eq:2b_prop_p1p2_nofsi}
&g(p_1,p_2,|\ensuremath{\boldsymbol{r}}_1-\ensuremath{\boldsymbol{r}}_1'|,|\ensuremath{\boldsymbol{r}}_2-\ensuremath{\boldsymbol{r}}_2'|)
\nonumber \\ &=
\frac{1}{4\pi^4}
 j_0(p_1|\ensuremath{\boldsymbol{r}}_1'-\ensuremath{\boldsymbol{r}}_1|)
 j_0(p_2|\ensuremath{\boldsymbol{r}}_2'-\ensuremath{\boldsymbol{r}}_2|)\, .
\end{aligned}$$ If nonrelativistic energies were used in Eq. [\[eq:integration_k1k2\]](#eq:integration_k1k2){reference-type="eqref" reference="eq:integration_k1k2"}, the expression would reduce exactly to Eq. [\[eq:integration_eE\]](#eq:integration_eE){reference-type="eqref" reference="eq:integration_eE"}. The simultaneous inclusion of correlated-propagator with relativistic kinematical effects is deferred to future work.

The two response densities, $D^{\mu\nu}(e,E_{\mathrm{c.m.}})$ and $D^{\mu\nu}(p_1,p_2)$, exhibit different behaviors. In the quasi-elastic regime, the dominant contribution to the cross section is due to the interaction of the probe with a single low-momentum nucleon. Consequently, one of the active nucleons carries a momentum $\sim q$ after the interaction, while the other remains unperturbed. As a result, $D^{\mu\nu}(e,E_{\mathrm{c.m.}})$ exhibits a single peak around $e=E=q^2/4m$, while $D^{\mu\nu}(p_1,p_2)$ has two peaks, one around $p_1=q$ and $p_2=0$, and the other around $p_2=q$ and $p_1=0$. These features are displayed in Figs. [\[fig:density_eE\]](#fig:density_eE){reference-type="ref" reference="fig:density_eE"} and [\[fig:density_e1e2\]](#fig:density_e1e2){reference-type="ref" reference="fig:density_e1e2"} for the transverse response densities in $^4$He at $q=700$ MeV/$c$.

When folded with the appropriate energy-conserving delta function -- either using relativistic or nonrelativistic energies for the two active nucleons in the final state, the integrated response densities give rise to response functions with distinct features. The solid blue and dashed red lines in the right panel of Fig. [\[fig:density_e1e2\]](#fig:density_e1e2){reference-type="ref" reference="fig:density_e1e2"} indicate the positions where the conditions $\omega+E=\sqrt{p_1^2+m^2}+\sqrt{p_2^2+m^2}-2m$ and $\omega+E=p_1^2/2m +p_2^2/2m$, respectively, are satisfied for a given value of $\omega$. In the relativistic case, the peak of the response function is obtained at $\omega\sim\sqrt{q^2+m^2}-m$ (neglecting binding effects), compared with $\omega \sim q^2/2m$ in the nonrelativistic case. Thus, relativistic kinematics shift the peak to lower values $\omega$, with the shift increasing for large values of $q$.

The shape of the peak is also affected. In the nonrelativistic limit, the width of the quasi-elastic peak is given by $\Delta \omega\sim 2\,pq/m$, where $p$ is the typical momentum of the nucleon inside the nucleus, while in the relativistic case the width narrows to $\Delta \omega\sim 2\,pq/\sqrt{q^2+m^2}$. The integral of the response function over $\omega$ (*i.e.*, the sum rule) remains unchanged by these relativistic kinematical effects, since the delta function does not alter the result of the integration as long as $D^{\mu\nu}$ does not depend on $\omega$ (which holds in this work based on $\omega$-independent currents and nucleonic form factors). As a result, the narrowing of the peak implies a corresponding increase of its height to conserve the sum rule. In summary, relativistic kinematics effects for final-state energies lead to a shift toward lower values of $\omega$, with increased peak height and reduced width.

::: figure*
![image](figures/transverse_he4_eE_700.png){width="1\\linewidth"}
:::

::: figure*
![image](figures/transverse_he4_p1p2_700.png){width="1\\linewidth"}
:::
