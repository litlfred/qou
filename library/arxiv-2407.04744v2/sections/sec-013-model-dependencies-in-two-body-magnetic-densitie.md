---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods"
section_id: sec-013-model-dependencies-in-two-body-magnetic-densitie
section_title: "Model dependencies in two-body magnetic densities"
section_number: null
pages: 12-16
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.821
doc_brief: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods — 26 sections: Magnetic structure of A 10 nuclei ; Introduction; Theory"
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
