---
doc_id: arxiv-2510.21576v1
doc_title: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation"
section_id: sec-006-comparing-low--and-high-momentum-transfer-nonrel
section_title: "Comparing low- and high-momentum transfer nonrelativistic reductions"
section_number: null
pages: 5-6
source_pdf: 2510.21576v1.pdf
source_sha256: 17a79b59d590c8da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.981
doc_brief: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation — 16 sections: Relativistic corrections for lepto; Introduction; Electron-nucleus scattering cross"
---
[]{#sec:comparing label="sec:comparing"}

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
