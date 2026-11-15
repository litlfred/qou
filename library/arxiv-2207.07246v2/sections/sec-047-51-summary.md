---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-047-51-summary
section_title: "Summary"
section_number: 5.1
pages: 118-119
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.984
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#summary label="summary"}

This work is mainly to answer one of the questions in section [\[secBackground\]](#secBackground){reference-type="ref" reference="secBackground"}: how to solve the many-body problem? Our answer is, using the path integral quantum Monte Carlo method. In nuclear physics, although continuous space light nuclei calculations for $A\leq 4$ have been studied before by GFMC ([@Carlson88a; @WiringaPieper02a]), this is the first work using PIMC. The code is now publicly available and open source ([@CRgitrepov6pimc1]).

By using multiple sampling algorithms, multi-level sampling most of the time, and occasionally the regular sampling described in section [\[secSamplingMethod\]](#secSamplingMethod){reference-type="ref" reference="secSamplingMethod"}, as well as the optimized calculation and updating strategies described in section [\[secCalcPath\]](#secCalcPath){reference-type="ref" reference="secCalcPath"} and section [\[secUpdateStrat\]](#secUpdateStrat){reference-type="ref" reference="secUpdateStrat"}, we successfully performed our ground state nuclear PIMC calculation of light nuclei, based on the local chiral N$^2$LO interaction and the AV6' interaction. From our analysis in section [\[setup\]](#setup){reference-type="ref" reference="setup"} and as well as calculation of the potential along the beads shown in Fig. [\[potential\]](#potential){reference-type="ref" reference="potential"}, we can conclude that our choice of the total imaginary time $\tau=0.2$ MeV$^{-1}$ indeed projected out the ground state, so our results are reliable. As discussed in section [\[setup\]](#setup){reference-type="ref" reference="setup"}, the time step $\Delta \tau$ we use is $10^{-4} \sim 10^{-3} \textrm{ MeV}^{-1}$ which are about 5 times bigger than GFMC calculations. This indicates that PIMC calculations are less sensitive to $\Delta \tau$ than GFMC is, due to the time step error structure of the PIMC expectation value such as Eq.([\[PIMCUSdetail\]](#PIMCUSdetail){reference-type="ref" reference="PIMCUSdetail"}) or Eq.([\[PIMCUN2LOdetail\]](#PIMCUN2LOdetail){reference-type="ref" reference="PIMCUN2LOdetail"}).

Our PIMC ground state energies of light nuclei are consistent with the results from GFMC and AFDMC as shown in Tables [\[TablePIMC2\]](#TablePIMC2){reference-type="ref" reference="TablePIMC2"} and [\[TablePIMCN2LO\]](#TablePIMCN2LO){reference-type="ref" reference="TablePIMCN2LO"}. For operators which do not commute with Hamiltonian and therefore usually cannot be obtained from DMC based methods such as GFMC and AFDMC without tradeoffs, we calculated the particle number density distribution $\rho(r)$, rms radii, and the angle averaged response functions. Our results are comparable with the GFMC results.
