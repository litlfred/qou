---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-4
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.994
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
Effective field theory (EFT) is a powerful tool in the description of the strong interactions at low energies. The central idea is due to Weinberg [@Weinberg:1978kz]:

> \"\... if one writes down the most general possible Lagrangian, including all terms consistent with assumed symmetry principles, and then calculates matrix elements with this Lagrangian to any given order of perturbation theory, the result will simply be the most general possible S--matrix consistent with analyticity, perturbative unitarity, cluster decomposition and the assumed symmetry principles.\"

In general, an EFT is an approximation to a (more) fundamental theory, designed to be valid in a certain kinematical domain. Instead of solving the underlying theory, the processes under investigation are described in terms of a suitable set of effective degrees of freedom, dominating the phenomena in the particular energy region. In the context of the strong interactions, the underlying theory is quantum chromodynamics (QCD)---a gauge theory with color SU(3) as the gauge group. Under normal conditions, the fundamental degrees of freedom of QCD, namely, quarks and gluons, do not show up as free particles. One assumes that any asymptotically observed hadron must be in a color-singlet state, i.e., a physically observable state is invariant under SU(3) color transformations. The strong increase of the running coupling for large distances possibly provides a mechanism for the color confinement.

For the low-energy properties of the strong interactions and the setting up of a corresponding EFT description, another phenomenon is of vital importance. The masses of the up and down quarks and, to a lesser extent, also of the strange quark are sufficiently small that the dynamics of QCD in the chiral limit, i.e., for massless quarks, is believed to resemble that of the "real" world. Although a rigorous mathematical proof is not yet available, there are good reasons to assume that a dynamical spontaneous symmetry breaking emerges from the chiral limit. Examples of indications for this to happen are the comparatively small masses of the pseudoscalar octet, the absence of a parity doubling in the low-energy spectrum of hadrons, and a non-vanishing scalar singlet quark condensate.

According to the Goldstone theorem, a breakdown of the chiral $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$ symmetry at the Lagrangian level to the $\mbox{SU(3)}_V$ symmetry in the ground state implies the existence of eight massless pseudoscalar Goldstone bosons. The finite masses of the pseudoscalar octet of the real world are attributed to the explicit chiral symmetry breaking due to the quark masses in the QCD Lagrangian. Due to the vanishing of the Goldstone boson masses in the chiral limit in combination with their vanishing interactions in the zero-energy limit, a derivative and quark-mass expansion is the natural scenario for an EFT. The corresponding method is called (mesonic) chiral perturbation theory (ChPT) [@Gasser:1983yg], with the Goldstone bosons as the relevant effective degrees of freedom (see Table [1](#1:table_QCD_EFT){reference-type="ref" reference="1:table_QCD_EFT"}).

::: center
::: {#1:table_QCD_EFT}
                            Fundamental theory               Effective field theory
  ----------------------- ---------------------- ----------------------------------------------
   Theoretical framework           QCD                                ChPT
    Degrees of freedom      Quarks and gluons          Goldstone bosons (+ other hadrons)
        Parameters         $g_3$ + quark masses   Low-energy coupling constants + quark masses

  : Comparison of QCD and ChPT.
:::

[]{#1:table_QCD_EFT label="1:table_QCD_EFT"}
:::

Using these effective degrees of freedom, physical quantities are calculated in terms of an expansion in $q/\Lambda_\chi$, where $q$ stands for momenta or masses of the pseudoscalar octet that are smaller than the energy/mass scale $\Lambda_\chi={\cal O}(1\,\mbox{GeV})$ associated with spontaneous symmetry breaking. Since an EFT is based on the most general Lagrangian, which includes all terms that are compatible with the symmetries of the underlying theory, the corresponding Lagrangian contains an infinite number of terms, where each term is accompanied by a low-energy coupling constant (LEC). The method that allows one to decide which terms contribute in a calculation up to a certain accuracy is called Weinberg's power counting. In the mesonic sector, the combination of dimensional regularization with the modified minimal subtraction scheme of ChPT leads to a straightforward correspondence between the loop expansion and the chiral expansion in terms of momenta and quark masses at a fixed ratio. In actual calculations only a finite number of terms in the expansion in $q/\Lambda_\chi$ has to be considered and thus one has predictive power. What distinguishes the EFT approach from purely phenomenological approaches is the possibility of a systematic improvement. Mesonic ChPT has been tremendously successful and may be considered as a full-grown and mature area of low-energy particle physics.

The situation gets more complicated once other hadronic degrees of freedom beyond the Goldstone bosons are considered. Together with such hadrons, another scale of the order of the chiral symmetry breaking scale $\Lambda_\chi$ enters the problem and the methods of the pure Goldstone-boson sector cannot be transferred one to one. For example, in the extension to the one-nucleon sector the correspondence between the loop expansion and the chiral expansion, at first sight, seems to be lost: higher-loop diagrams can contribute to terms as low as ${\cal O}(q^2)$ [@Gasser:1987rb]. For a long time this was interpreted as the absence of a systematic power counting in the relativistic formulation of ChPT. However, over the last decade new developments in devising a suitable renormalization scheme have led to a simple and consistent power counting for the renormalized diagrams of a manifestly Lorentz-invariant approach.

The purpose of this article is to first provide a pedagogical introduction to the basic concepts of ChPT and to then present the more recent developments of a manifestly Lorentz-invariant approach to the one-nucleon sector. It is definitely *not* intended to give a survey of the vast literature on ChPT and its various extensions in terms of chiral effective field theories. For further information the interested reader is referred to review articles and lecture notes addressing different topics with various priorities [@Bijnens:1993xi], [@Georgi:1994qn], [@Ecker:1994gg], [@Pich:1995bw], [@Bernard:1995dp], [@Hemmert:1997ye], [@Burgess:1998ku], [@Scherer:2002tk], [@Scherer:2005ri], [@Epelbaum:2005pn], [@Bijnens:2006zp], [@Bernard:2006gx], [@Bernard:2007zu].

The article is organized as follows. Section [\[section_chiral symmetry\]](#section_chiral symmetry){reference-type="ref" reference="section_chiral symmetry"} contains a discussion of the chiral symmetry of QCD, spontaneous symmetry breaking, and the Goldstone theorem. In Sec. [\[section_mchpt\]](#section_mchpt){reference-type="ref" reference="section_mchpt"}, the basic concepts of mesonic ChPT are developed. Section [\[section_bchpt\]](#section_bchpt){reference-type="ref" reference="section_bchpt"} is devoted to baryonic ChPT. The power-counting problem is illustrated and solutions in terms of suitable renormalization conditions are presented. Section [\[section_applications\]](#section_applications){reference-type="ref" reference="section_applications"} contains a few selected applications of the manifestly Lorentz-invariant approach to nucleon properties.
