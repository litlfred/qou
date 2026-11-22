---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-027-28-sign-problem
section_title: "Sign Problem"
section_number: 2.8
pages: 59-61
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.868
latex_coverage_ratio: 0.983
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secSignProblem label="secSignProblem"}

Since wave functions for fermions are antisymmetric under interchange of the particles, they necessarily can change sign. Except for a few special cases where the Monte Carlo sampling can be arranged so that sign changes for two types of fermions occur together, fermion quantum Monte Carlo has a sign or phase problem ([@Umrigar2007PRL; @Alhassid1994PRL; @LiZiXiang2019a]). This means that for a long enough path it is possible to propagate from a region where the wave function is positive to one where it is negative (or has a different phase). In such a case as the total imaginary time for the path increases, these sign changes make the signal to noise ratio decay exponentially, or, for a fixed amount of computer time, the variance increases exponentially with the total imaginary time.

For the light nuclei here, there would be no sign problem if the potential were spin-isospin independent. In that case, the four spin-isospin states proton up, proton down, neutron up, neutron down would not be mixed by the interaction, and can be interpreted as different kinds of particles. The spatial part of the wave function would be positive definite.

Realistic interactions change the spin and isospin, but the fact that the wave function is still predominantly in this "s-shell" means that the fermion sign problem is weak. As shown in this work, for imaginary times that converge the system to the ground state, the fraction of negative paths is small and we simply ignore the sign problem. That is, our calculations need no approximations to deal with the fermion sign problem[^1].

Extensions of this method to larger systems will necessary require dealing with a stronger sign or phase problem. We expect that the approximate methods developed for GFMC and AFDMC can be applied. Those methods include fixed node approximation ([@Moskowitz1982a; @JBAnderson2008]), constrained-path approximation ([@ZhangShiwei2003PRL; @Gandolfi2009PRCa; @Motta2018]), fixed-phase approximation ([@Carlson87a]), eigenvector continuation method ([@DLee2018PRL]), etc.

# Monte Carlo Algorithms {#compalgorithm}

In this chapter, we introduce how we sample the probability distribution $P_{lr}(\mathcal{R})$ in Eq.([\[PlrR\]](#PlrR){reference-type="ref" reference="PlrR"}) and also our algorithm for performing the other parts of the PIMC calculations, the sampling is based on a Markov chain process ([@Ceperley95a; @HammondMCbook]) along with the Metropolis algorithm ([@Metropolis53a; @Kalos1986a]).\

[^1]: In PIMC calculation, the sign problem is equivalent to say that the $B_{lr} (\mathcal{R})$ in Eq.([\[Blrsimpform\]](#Blrsimpform){reference-type="ref" reference="Blrsimpform"}) we sampled may frequently oscillate between 1 and -1, which can make the $\langle B_{lr} (\mathcal{R}) \rangle$ in Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}) close to zero and therefore lead to a big error bar. However, In our light nuclei PIMC calculation, e.g. the $^4$He calculation, we find $\langle B_{lr} (\mathcal{R}) \rangle \approx 0.9$ which means there are only about $5\%$ of the $B_{lr} (\mathcal{R})$ samples flip their signs from 1 to -1. So we do not have any serious sign problems in this work, partially because our total imaginary time is not big, and also we are summing over all the spin isospin states and this makes the sign flipping less likely to happen.
