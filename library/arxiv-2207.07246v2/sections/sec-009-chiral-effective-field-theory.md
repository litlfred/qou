---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-009-chiral-effective-field-theory
section_title: "Chiral effective field theory"
section_number: null
pages: 14-15
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.98
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Since the 1990s, the importance of NN interactions derived from chiral effective field theory (ChEFT) has been realized by more and more people. The idea of ChEFT was proposed in 1979 by Steven Weinberg ([@WEINBERG1979327]) and after his proposal about how to treat the nuclear interaction at the chiral limit ([@WEINBERG1990288; @WEINBERG19913]) ChEFT has been rapidly developed in nuclear physics ([@Epelbaum2009a; @MACHLEIDT20111]). The nuclear interactions derived from ChEFT are connected with the fundamental theory of QCD by the broken chiral symmetry. This is an example of 'symmetry dictates interaction' ([@Yang1980a]). To derive the nuclear interaction from ChEFT, one has to identify the relevant symmetries of low-energy QCD first. Then, one needs to construct the most general Lagrangian including those symmetries and symmetry breakings. After that, one needs to do a low momentum expansion and design the scheme to collect the important contributions. The scheme is called chiral perturbation theory (ChPT). Finally, one calculates those Feynman diagrams of the important contributions order by order, in terms of an expansion in the small external momenta over the large scale, $(\frac{Q}{\Lambda_{\chi}})^\nu$. Here Q means the nucleon three-momentum or pion four-momentum or a pion mass which is around 140 MeV, $\Lambda_\chi$ is the chiral symmetry breaking scale (hadronic scale) which is about 1 GeV, $\nu$ is the power of the order. Determining the power $\nu$ is called power counting. $\nu=0$ terms are the called the leading order (LO) which contributes the most to the nuclear interaction. There are no $\nu=1$ terms due to parity and time-reversal invariance, so the next-to-leading order (NLO) terms are for $\nu=2$. The next-to-next-to-leading order (N$^2$LO) terms are for $\nu=3$, and this is where a nonvanishing 3NF occurs ([@Klock1994a; @Epelbaum2002PRC]). The next-to-next-to-next-to-leading order (N$^3$LO) are for $\nu=3$ and that is where a 4NF occurs. Note that $(\frac{Q}{\Lambda_{\chi}})<1$, and the 2NF occurs at $\nu=0$, the 3NF occurs at $\nu=3$, and the 4NF occurs at $\nu=4$. $(\frac{Q}{\Lambda_{\chi}})^0 \gg (\frac{Q}{\Lambda_{\chi}})^3 \gg (\frac{Q}{\Lambda_{\chi}})^4$, therefore ChPT explains the hierarchy of nuclear force $2NF \gg 3NF \gg 4NF$ which we knew empirically before. Because the Chiral interaction are based on momentum expansion $(\frac{Q}{\Lambda_{\chi}})^\nu$, it naturally carries the momentum dependence. It is worth mentioning that ([@Gerzerlis13a]) up to N$^2$LO (beginning from N$^3$LO, non-local operators cannot be avoided however their effects should be negligible and can be treated perturbatively), one can write down a mostly local version of the chiral interaction[^1]. The local chiral interaction will be particularly useful for any quantum Monte Carlo (QMC) method in continuous space which includes the method used in this work.

[^1]: That is, the momentum dependence is predominantly determined by the momentum transfer which Fourier transforms to a local in space potential
