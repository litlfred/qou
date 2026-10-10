---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-010-validation
section_title: "Validation"
section_number: null
pages: 7-8
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.975
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
[]{#sec:validation label="sec:validation"}

[ADoNIS]{.smallcaps} implements the same underlying physics choices as ACHILLES, enabling a direct validation against its predictions. Ref. [@Isaacson:2025cnk] compares ACHILLES with a broad set of measurements; here we reproduce representative comparisons with [ADoNIS]{.smallcaps} and ACHILLES overlaid, spanning different probes, interaction channels, target nuclei and beam energies.

Figure [1](#fig:val_minerva){reference-type="ref" reference="fig:val_minerva"} shows the MINERvA CC0$\pi$ sample on $^{12}$C at $\langle E_\nu\rangle \approx 3$ GeV, generated for the signal definition of Ref. [@MINERvA:2018hba]. The observables span lepton kinematics, hadron kinematics and the transverse kinematic imbalance (TKI) variables that correlate the two. At MINERvA energies both quasi-elastic and resonant interactions contribute substantially, with excellent agreement observed in both. Agreement holds equally for other beams, binnings and signal definitions. For instance, we showcase the T2K CC0$\pi$ and CC1$\pi^+$ samples of Refs. [@T2K:2018rnz] and [@T2K:2021naz] in Figs. [\[fig:val_t2k_cc0pi\]](#fig:val_t2k_cc0pi){reference-type="ref" reference="fig:val_t2k_cc0pi"} and [\[fig:val_t2k_cc1pi\]](#fig:val_t2k_cc1pi){reference-type="ref" reference="fig:val_t2k_cc1pi"} of Appendix [\[app:validation\]](#app:validation){reference-type="ref" reference="app:validation"}.

Figure [2](#fig:val_uboone_nc2d){reference-type="ref" reference="fig:val_uboone_nc2d"} showcases the double-differential cross section for NC 1$\pi^0$Xp production measured by MicroBooNE [@MicroBooNE:2024pdj], and demonstrates that equivalent predictions are also achieved for the two generators for neutral-current observables on Ar. Analogous agreement in charged-current MicroBooNE TKI observables [@MicroBooNE:2023tzj] is also presented in Fig. [\[fig:val_uboone_cc1p\]](#fig:val_uboone_cc1p){reference-type="ref" reference="fig:val_uboone_cc1p"} in Appendix [\[app:validation\]](#app:validation){reference-type="ref" reference="app:validation"}.

The last two comparisons isolate single ingredients. Figure [3](#fig:val_ee){reference-type="ref" reference="fig:val_ee"} shows inclusive $(e,e')$ cross sections on $^{12}$C and $^{40}$Ar at $2.222$ GeV, in the configuration of the Jefferson Lab E12-14-012 measurements [@Murphy:2019wed; @JeffersonLabHallA:2022cit; @JeffersonLabHallA:2022ljj]: an electromagnetic probe of known kinematics, on both target nuclei, separated into quasi-elastic and resonant contributions. Exclusive electron-scattering observables from e4$\nu$ [@CLAS:2021neh], which confront the neutrino-energy estimators against a beam of known energy, are given in Fig. [\[fig:val_e4nu\]](#fig:val_e4nu){reference-type="ref" reference="fig:val_e4nu"} of Appendix [\[app:validation\]](#app:validation){reference-type="ref" reference="app:validation"}. Lastly, Fig. [4](#fig:val_pinuc){reference-type="ref" reference="fig:val_pinuc"} shows $\pi^+$--nucleus absorption and reaction cross sections in the configuration of Refs. [@ASHERY; @LADS:2000pzh; @DUET], where the pions come from a tagged hadron beam rather than an interaction vertex, so that the cascade is exercised on its own.

Taken together, these comparisons show that the differentiable reformulation preserves the underlying physics predictions.

<figure id="fig:val_minerva" data-latex-placement="htbp">
<img src="fig09_minerva_cc0pi_noratio" />
<figcaption>ADoNIS (solid) vs. ACHILLES (dashed). MINERvA CC0<span class="math inline"><em>π</em></span> on <span class="math inline"><sup>12</sup></span>C at <span class="math inline">⟨<em>E</em><sub><em>ν</em></sub>⟩ ≈ 3</span> GeV, with the signal definition of Ref. <span class="citation" data-cites="MINERvA:2018hba"></span>: the TKI variables <span class="math inline"><em>δ</em><em>α</em><sub><em>T</em></sub></span>, <span class="math inline"><em>p</em><sub><em>n</em></sub></span>, <span class="math inline"><em>δ</em><em>p</em><sub><em>T</em></sub></span> and <span class="math inline"><em>δ</em><em>ϕ</em><sub><em>T</em></sub></span>, and the proton and muon kinematics.</figcaption>
</figure>

<figure id="fig:val_uboone_nc2d" data-latex-placement="htbp">
<img src="fig11_uboone_nc1pi0_doublediff_noratio" />
<figcaption>ADoNIS (solid) vs. ACHILLES (dashed). MicroBooNE NC 1<span class="math inline"><em>π</em><sup>0</sup></span>Xp on <span class="math inline"><sup>40</sup></span>Ar <span class="citation" data-cites="MicroBooNE:2024pdj"></span>: the double-differential cross section <span class="math inline"><em>d</em><sup>2</sup><em>σ</em>/<em>d</em>cos <em>θ</em><sub><em>π</em><sup>0</sup></sub> <em>d</em><em>p</em><sub><em>π</em><sup>0</sup></sub></span>, in slices of <span class="math inline">cos <em>θ</em><sub><em>π</em><sup>0</sup></sub></span>.</figcaption>
</figure>

<figure id="fig:val_ee" data-latex-placement="htbp">
<img src="fig01_ee_domega_noratio" />
<figcaption>ADoNIS (solid) vs. ACHILLES (dashed). Inclusive <span class="math inline">(<em>e</em>, <em>e</em><sup>′</sup>)</span> cross section <span class="math inline"><em>d</em><em>σ</em>/<em>d</em><em>ω</em></span> on <span class="math inline"><sup>12</sup></span>C and <span class="math inline"><sup>40</sup></span>Ar at a beam energy of <span class="math inline">2.222</span> GeV and <span class="math inline"><em>θ</em><sub><em>e</em><sup>′</sup></sub> ≈ 15.5<sup>∘</sup></span> <span class="citation" data-cites="Murphy:2019wed JeffersonLabHallA:2022cit JeffersonLabHallA:2022ljj"></span>, separated into quasi-elastic and resonant contributions.</figcaption>
</figure>

<figure id="fig:val_pinuc" data-latex-placement="htbp">
<img src="fig03_pi_nucleus_sigma_noratio" />
<figcaption>ADoNIS (solid) vs. ACHILLES (dashed). <span class="math inline"><em>π</em><sup>+</sup></span>–nucleus absorption and reaction cross sections on carbon and argon as a function of pion momentum <span class="citation" data-cites="ASHERY LADS:2000pzh DUET"></span>, testing the intranuclear cascade in isolation.</figcaption>
</figure>
