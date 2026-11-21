---
doc_id: arxiv-2510.21576v1
doc_title: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation"
section_id: sec-007-short-time-approximation
section_title: "Short-time approximation"
section_number: null
pages: 6-7
source_pdf: 2510.21576v1.pdf
source_sha256: 17a79b59d590c8da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.988
doc_brief: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation — 16 sections: Relativistic corrections for lepto; Introduction; Electron-nucleus scattering cross"
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
