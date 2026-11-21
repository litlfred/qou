---
doc_id: arxiv-2510.21576v1
doc_title: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation"
section_id: sec-004-low-momentum-transfer-nonrelativistic-reduction
section_title: "Low-momentum transfer nonrelativistic reduction"
section_number: null
pages: 3-4
source_pdf: 2510.21576v1.pdf
source_sha256: 17a79b59d590c8da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.99
doc_brief: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation — 16 sections: Relativistic corrections for lepto; Introduction; Electron-nucleus scattering cross"
---
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
