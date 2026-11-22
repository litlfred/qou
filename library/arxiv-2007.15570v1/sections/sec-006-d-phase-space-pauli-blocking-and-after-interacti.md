---
doc_id: arxiv-2007.15570v1
doc_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_id: sec-006-d-phase-space-pauli-blocking-and-after-interacti
section_title: "D Phase space, Pauli blocking and after-interaction"
section_number: null
pages: 5-6
source_pdf: 2007.15570v1.pdf
source_sha256: 6e46f4346a29fd83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.989
doc_brief: "A quantum Monte Carlo based approach to intranuclear cascades — 16 sections: Front matter; A quantum Monte Carlo based approa; I Introduction"
---
If an interaction occurred, the phase space of the outgoing particles is generated using fully differential nucleon-nucleon cross sections. Note that, at the moment, we only include protons and neutrons in our INC model. Pauli blocking enforces Fermi-Dirac statistics for the nucleons and amounts to testing whether their final-state momenta are above the Fermi momentum. Two different models of the Pauli exclusion principle have been approximately implemented. The *global* and *local* Pauli blocking routines essentially forbid a scattering if the momentum of any of the final state particles is below the average Fermi momentum (for the global Fermi gas model) or the local Fermi momentum (for the local Fermi gas model), respectively. We emphasize again that, although we have implemented the global Fermi gas model, we do not report any results using it.

If the interaction took place, the outgoing particles are both treated as propagating particles, and a formation zone is set for each of them [@Landau:1953gr; @Stodolsky:1975qq] (see also Ref. [@Golan:2012wx]). The formation zone is a length or period of time in which a particle does not interact with any nucleons. This models the coherence and interference of interactions in quantum mechanics. The formation zone is given by $$\delta t = \frac{E'}{m_N^2-p\cdot p'},$$ where $m_N=938$ MeV is the nucleon mass, $E'$ is the energy of the outgoing nucleon, and $p$ and $p'$ are the four momenta of the incoming and outgoing nucleon respectively.
