---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S"
section_id: sec-009-model-dependencies-in-two-body-magnetic-densitie
section_title: "Model dependencies in two-body magnetic densities"
section_number: null
pages: 12-16
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
doc_brief: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S — 21 sections: Front matter; Theory; Introduct"
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.956
---
<figure id="fig:dens.comp.iv">
<div class="center">
<embed src="mdens-comp.pdf" style="width:45.0%" />
</div>
<figcaption>Two-body VMC magnetic densities arising from the NLO (blue circles), N2LO-<span class="math inline"><em>Δ</em></span> (orange squares), and the N3LO(NM) IV (green triangles) contributions for <span class="math inline"><sup>3</sup></span>H computed with model Ia<span class="math inline"><sup>⋆</sup></span> (filled symbols) and IIb<span class="math inline"><sup>⋆</sup></span> (open symbols) as a function of interparticle spacing <span class="math inline"><em>r</em><sub><em>i</em><em>j</em></sub></span>. </figcaption>
</figure>

<figure id="fig:dens.comp.is">
<div class="center">
<embed src="mdens-comp-is.pdf" style="width:45.0%" />
</div>
<figcaption>Two-body VMC magnetic densities arising from the N3LO(MIN) IS (blue circles), and the N3LO(OPE) IS (orange squares) contributions for <span class="math inline"><sup>6</sup></span>Li computed with model Ia<span class="math inline"><sup>⋆</sup></span> (filled symbols) and IIb<span class="math inline"><sup>⋆</sup></span> (open symbols) as a function of interparticle spacing <span class="math inline"><em>r</em><sub><em>i</em><em>j</em></sub></span>.</figcaption>
</figure>

Up to this point, we have analyzed the densities only for one model; however, it is important to assess the cutoff dependence, which is evidently important in the integrated two-body contributions. To that end, we compare the dominant IV contributions to the $^3$H magnetic moment in Fig. [1](#fig:dens.comp.iv){reference-type="ref" reference="fig:dens.comp.iv"}. The effect of the softer cutoff in the Ia$^{\star}$ regulator on the NLO(OPE) and N2LO($\Delta)$ currents is, unsurprisingly, to reduce the two-body magnetic density at short distances; however, the tail of the density is unaffected by the cutoff function. Thus, taking a softer cutoff quenches the overall magnitude of the matrix element. This particularly impacts the N2LO($\Delta)$ current which is of shorter-range than the NLO contribution due to the presence of the intermediate $\Delta$-isobar. The soft cutoff removes strength from the N2LO($\Delta$) magnetic moment around its peak, resulting in a large quenching of the contribution in model Ia$^{\star}$ relative to model IIb$^{\star}$. The N3LO(NM) contribution, however, is enhanced when using the softer cutoff of model Ia$^{\star}$. The contact density is broadened for the softer cutoff while preserving the overall magnitude. This effect is likely due to a combination of having a broader Gaussian representation of the $\delta$-function and a larger density of short-range IV pairs.

A similar broadening of the contact densities is observed in Fig. [2](#fig:dens.comp.is){reference-type="ref" reference="fig:dens.comp.is"} which shows the IS densities plotted for $^6$Li. For the long-range N3LO(OPE) IS contribution, the correlation functions $I_1(x)$ and $I_2(x)$ are particularly sensitive to the choice of regulator, as was previously observed in Ref. [@Schiavilla:2018udt]. This can move the node in the density and change the overall sign of the contribution to the magnetic moment from this current, as shown in the figure.

From the model comparison, it is clear that altering the short-range dynamics with different cutoffs significantly impacts two-body magnetic moments. Clearly, if one takes a cutoff that is too small, it will spoil the convergence behavior of the higher-order contributions due to significant quenching of the NLO and N2LO($\Delta)$ terms. This quenching is compensated for by a larger N3LO(NM) IV fit contribution and thus is not seen if one looks only at the total magnetic moment; however, if one were to perform the calculation up to NLO in the current, evidently the model dependence would induce an error much larger than the naive expectation from power counting. Given this significant model dependence of the two-body contributions and the particular importance of the IV piece in predicting magnetic structure, it is crucial to investigate this cutoff dependence more rigorously in the future.

## Magnetic form factors and high-momentum structure {#sec:ff}

::: figure*
![${}^3\text{H}$](h3_order_by_order_nviib.pdf){width="\\linewidth"}

![${}^3\text{He}$](he3_order_by_order_nviib.pdf){width="\\linewidth"}

![${}^6\text{Li}$](li6_order_by_order_nviib.pdf){width="\\linewidth"}

\

![${}^7\text{Li}$](li7_order_by_order_nviib.pdf){width="\\linewidth"}

![${}^7\text{Be}$](be7_order_by_order_nviib.pdf){width="\\linewidth"}

![${}^8\text{Li}$](li8_order_by_order_nviib.pdf){width="\\linewidth"}

\

![${}^8\text{B}$](b8_order_by_order_nviib.pdf){width="\\linewidth"}

![${}^9\text{Li}$](li9_order_by_order_nviib.pdf){width="\\linewidth"}

![${}^9\text{Be}$](be9_order_by_order_nviib.pdf){width="\\linewidth"}

\

![${}^9\text{B}$](b9_order_by_order_nviib.pdf){width="\\linewidth"}

![${}^9\text{C}$](c9_order_by_order_nviib.pdf){width="\\linewidth"}

![${}^{10}\text{B}$](b10_order_by_order_nviib.pdf){width="\\linewidth"}
:::

::: figure*
![${}^7\text{Li}$](li7multipoles.pdf){width="\\linewidth"}

![${}^7\text{Be}$](be7multipoles.pdf){width="\\linewidth"}

![${}^8\text{Li}$](li8multipoles.pdf){width="\\linewidth"}

\

![${}^8\text{B}$](b8multipoles.pdf){width="\\linewidth"}

![${}^9\text{Li}$](li9multipoles.pdf){width="\\linewidth"}

![${}^9\text{Be}$](be9multipoles.pdf){width="\\linewidth"}

\

![${}^9\text{B}$](b9multipoles.pdf){width="\\linewidth"}

![${}^9\text{C}$](c9multipoles.pdf){width="\\linewidth"}

![${}^{10}\text{B}$](b10multipoles.pdf){width="\\linewidth"}
:::

The magnetic form factor has been computed using the same interactions and currents used for the magnetic moments. In Fig. [\[fig:MFF_IIb_co\]](#fig:MFF_IIb_co){reference-type="ref" reference="fig:MFF_IIb_co"}, we present the results for all the nuclei showing the contributions of the currents order-by-order for the NV2+3-IIb$^\star$ interaction compared to data where available. We also include predicted magnetic form factors of radioactive isotopes, because while there are presently no data for comparison, novel techniques have recently made it possible to study electron scattering from radioactive nuclei [@Tsukada:2023].

In Fig. [\[fig:MFF_multipole_IIb\]](#fig:MFF_multipole_IIb){reference-type="ref" reference="fig:MFF_multipole_IIb"} we present the multipole contributions to the magnetic form factors for the nuclei with $J>1$ computed with the full currents at N3LO and the NV2+3-IIb$^\star$. Similar results are obtained for the other interaction and current models considered.

Finally, we estimated the truncation error, limiting our analysis to the error associated with the chiral expansion of the electromagnetic currents, assuming the power counting adopted in Refs. [@Pastore:2008ui; @Pastore:2009is; @Pastore:2011ip; @Piarulli:2012bn; @Schiavilla:2018udt; @Gnech:2022vwr]. The calculation of the full chiral truncation error would require an analysis of the chiral expansion in both the interaction and currents, together; however, for the nuclear interactions considered in this work, this is not presently possible.

In order to estimate the truncation error we use the prescription of Ref. [@Epelbaum:2014efa; @Epelbaum:2014sza] applied to $$\label{eq:mff_tilde}
    \tilde F_M(q)=\sqrt{2\pi(2J+1)}\frac{2m_N}{q}\langle J J,J -\!J |1 0\rangle F_M(q)\,.$$ For this analysis, we select a value of $\Lambda_b=700$ MeV and, for the characteristic scale of momentum $Q$, we follow Ref. [@Philips2016] by setting it to the typical momentum transfer $(A-1)/A\,q$, for the nucleus of mass number $A$. In Fig. [\[fig:MFF_err\]](#fig:MFF_err){reference-type="ref" reference="fig:MFF_err"}, we plot the error bands at LO (orange), NLO (green), N2LO (blue) and N3LO(red). Note that we do not renormalize the results to a specific value of the magnetic moment.

Below we discuss in detail the results obtained for each nucleus studied.
