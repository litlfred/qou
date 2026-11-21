---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-011-validation
section_title: "Validation"
section_number: null
pages: 7-8
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.994
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
[]{#sec:validation label="sec:validation"}

[ADoNIS]{.smallcaps} implements the same underlying physics choices as ACHILLES, enabling a direct validation against its predictions. Ref. [@Isaacson:2025cnk] compares ACHILLES with a broad set of measurements; here we reproduce representative comparisons with [ADoNIS]{.smallcaps} and ACHILLES overlaid, spanning different probes, interaction channels, target nuclei and beam energies.

Figure [1](#fig:val_minerva){reference-type="ref" reference="fig:val_minerva"} shows the MINERvA CC0$\pi$ sample on $^{12}$C at $\langle E_\nu\rangle \approx 3$ GeV, generated for the signal definition of Ref. [@MINERvA:2018hba]. The observables span lepton kinematics, hadron kinematics and the transverse kinematic imbalance (TKI) variables that correlate the two. At MINERvA energies both quasi-elastic and resonant interactions contribute substantially, with excellent agreement observed in both. Agreement holds equally for other beams, binnings and signal definitions. For instance, we showcase the T2K CC0$\pi$ and CC1$\pi^+$ samples of Refs. [@T2K:2018rnz] and [@T2K:2021naz] in Figs. [\[fig:val_t2k_cc0pi\]](#fig:val_t2k_cc0pi){reference-type="ref" reference="fig:val_t2k_cc0pi"} and [\[fig:val_t2k_cc1pi\]](#fig:val_t2k_cc1pi){reference-type="ref" reference="fig:val_t2k_cc1pi"} of Appendix [\[app:validation\]](#app:validation){reference-type="ref" reference="app:validation"}.

Figure [2](#fig:val_uboone_nc2d){reference-type="ref" reference="fig:val_uboone_nc2d"} showcases the double-differential cross section for NC 1$\pi^0$Xp production measured by MicroBooNE [@MicroBooNE:2024pdj], and demonstrates that equivalent predictions are also achieved for the two generators for neutral-current observables on Ar. Analogous agreement in charged-current MicroBooNE TKI observables [@MicroBooNE:2023tzj] is also presented in Fig. [\[fig:val_uboone_cc1p\]](#fig:val_uboone_cc1p){reference-type="ref" reference="fig:val_uboone_cc1p"} in Appendix [\[app:validation\]](#app:validation){reference-type="ref" reference="app:validation"}.

The last two comparisons isolate single ingredients. Figure [3](#fig:val_ee){reference-type="ref" reference="fig:val_ee"} shows inclusive $(e,e')$ cross sections on $^{12}$C and $^{40}$Ar at $2.222$ GeV, in the configuration of the Jefferson Lab E12-14-012 measurements [@Murphy:2019wed; @JeffersonLabHallA:2022cit; @JeffersonLabHallA:2022ljj]: an electromagnetic probe of known kinematics, on both target nuclei, separated into quasi-elastic and resonant contributions. Exclusive electron-scattering observables from e4$\nu$ [@CLAS:2021neh], which confront the neutrino-energy estimators against a beam of known energy, are given in Fig. [\[fig:val_e4nu\]](#fig:val_e4nu){reference-type="ref" reference="fig:val_e4nu"} of Appendix [\[app:validation\]](#app:validation){reference-type="ref" reference="app:validation"}. Lastly, Fig. [4](#fig:val_pinuc){reference-type="ref" reference="fig:val_pinuc"} shows $\pi^+$--nucleus absorption and reaction cross sections in the configuration of Refs. [@ASHERY; @LADS:2000pzh; @DUET], where the pions come from a tagged hadron beam rather than an interaction vertex, so that the cascade is exercised on its own.

Taken together, these comparisons show that the differentiable reformulation preserves the underlying physics predictions.

![ADoNIS (solid) vs. ACHILLES (dashed). MINERvA CC0$\pi$ on $^{12}$C at $\langle E_\nu\rangle \approx 3$ GeV, with the signal definition of Ref. [@MINERvA:2018hba]: the TKI variables $\delta\alpha_T$, $p_n$, $\delta p_T$ and $\delta\phi_T$, and the proton and muon kinematics.](fig09_minerva_cc0pi_noratio){#fig:val_minerva width="\\linewidth"}

![ADoNIS (solid) vs. ACHILLES (dashed). MicroBooNE NC 1$\pi^0$Xp on $^{40}$Ar [@MicroBooNE:2024pdj]: the double-differential cross section $d^2\sigma/d\cos\theta_{\pi^0}\,dp_{\pi^0}$, in slices of $\cos\theta_{\pi^0}$.](fig11_uboone_nc1pi0_doublediff_noratio){#fig:val_uboone_nc2d width="\\linewidth"}

![ADoNIS (solid) vs. ACHILLES (dashed). Inclusive $(e,e')$ cross section $d\sigma/d\omega$ on $^{12}$C and $^{40}$Ar at a beam energy of $2.222$ GeV and $\theta_{e'}\approx 15.5^\circ$ [@Murphy:2019wed; @JeffersonLabHallA:2022cit; @JeffersonLabHallA:2022ljj], separated into quasi-elastic and resonant contributions.](fig01_ee_domega_noratio){#fig:val_ee width="\\linewidth"}

![ADoNIS (solid) vs. ACHILLES (dashed). $\pi^+$--nucleus absorption and reaction cross sections on carbon and argon as a function of pion momentum [@ASHERY; @LADS:2000pzh; @DUET], testing the intranuclear cascade in isolation.](fig03_pi_nucleus_sigma_noratio){#fig:val_pinuc width="\\linewidth"}
