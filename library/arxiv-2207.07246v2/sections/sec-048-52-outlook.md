---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-048-52-outlook
section_title: "Outlook"
section_number: 5.2
pages: 119-121
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.991
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
We hope our $^4$He calculation may be served as a benchmark test for future PIMC calculations of larger nuclei.
The reason to do larger nuclei is because we can first test how good the nucleon-nucleon interaction is, then we can try to predict the properties of neutron rich nuclei which are most likely generated in supernovae,
or in the laboratories\footnote{Such as the Facility for Rare Isotope Beams (FRIB) at Michigan State University.}.
However, larger nuclei PIMC calculations will be more complicated and computational expensive than the light nuclei calculations presented in this work.
We estimate that without significant improvement,
our PIMC may take similar computational cost as GFMC does.
We can try to do several things to make the calculations more accessible.

We can try to increase the time step and reduce the beads needed in PIMC and therefore save computation time.
In fact, in our PIMC calculations, the time step $\Delta \tau$ are about an order of magnitude larger than those used in DMC based methods.
If a pair-product propagator (\cite{Ceperley95a,SchmidtLee95a,Pudliner1997PRC,CarlsonRMP15a}) is used, it may enable us to use even bigger time steps, this can reduce the number of beads in PIMC calculation and save computation time.

We can try to reduce the size of the spin-isospin basis.
We may separate the interaction into two parts, one part conserves total isospin such as the AV6' NN operators,
and other part includes isospin breaking terms, such as the Coulomb interaction.
We can first use a good isospin basis for the Hamiltonian with these nuclear interactions only,
because the number of isospin basis states can be somewhat smaller than the charge basis we use now.
We can save the spatial and other relevant configurations,
and then, we can use them to calculate the isospin breaking parts perturbatively (\cite{Lonardoni2018PRC}).

We may also try to combine AFDMC ideas to efficiently sample the spin isospin states instead of summing over them.
If this can be made possible it will significantly reduce the computation time for PIMC calculations of larger nuclei.

A nuclear PIMC finite temperature calculation of $^4$He or neutron matter including three-body interactions is also possible.
That can be a pioneering step towards QMC calculations in continuous space for a finite temperature nuclear equation of state (\cite{LWChen2008a,Chen2010PRC}).

However, large nuclei and finite temperature nuclear matter PIMC calculations will inevitably lead to large variance due to sign problem unless approximate methods like adding fixed phase or fixed node constraints are used.
The sign problem has no known general fix yet.
Improving the trial wave function and the short-time propagator, and constraining the path can somewhat make the sign problem less severe or eliminate it giving an approximate result.

Last but not least, even though we will face sign problem, and, even with the most powerful supercomputers today, there are still problems in QMC that seem to make calculating large nuclei or the equation of state at finite temperature not accessible at the current stage, those messes simply mean there are big opportunities.
I simply cannot imagine human beings cannot go far beyond the current situation (\cite{Laughlin2000}).
And I would like to use Steven Weinberg's advice (\cite{Weinberg2003}) to end my dissertation, which is also what I learned from my advisor professor Kevin E. Schmidt these years:

`` ... go for the messes --- that's where the action is. ''



















\newpage

{\singlespace



\phantomsection
\addcontentsline{toc}{part}{REFERENCES}
\bibliographystyle{asudis}
