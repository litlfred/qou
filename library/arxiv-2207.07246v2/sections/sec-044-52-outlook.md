---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-044-52-outlook
section_title: "Outlook"
section_number: 5.2
pages: 119-121
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
We hope our 4He calculation may be served as a benchmark test for future PIMC
calculations of larger nuclei. The reason to do larger nuclei is because we can ﬁrst
test how good the nucleon-nucleon interaction is, then we can try to predict the
properties of neutron rich nuclei which are most likely generated in supernovae, or in
the laboratories 1 . However, larger nuclei PIMC calculations will be more complicated
and computational expensive than the light nuclei calculations presented in this
work. We estimate that without signiﬁcant improvement, our PIMC may take similar
computational cost as GFMC does. We can try to do several things to make the
calculations more accessible.
We can try to increase the time step and reduce the beads needed in PIMC and
therefore save computation time. In fact, in our PIMC calculations, the time step ∆ τ
are about an order of magnitude larger than those used in DMC based methods. If a
pair-product propagator (Ceperley (1995); Schmidt and Lee (1995); Pudliner et al.
(1997); Carlson et al. (2015)) is used, it may enable us to use even bigger time steps,
this can reduce the number of beads in PIMC calculation and save computation time.
We can try to reduce the size of the spin-isospin basis. We may separate the
interaction into two parts, one part conserves total isospin such as the AV6’ NN
operators, and other part includes isospin breaking terms, such as the Coulomb
interaction. We can ﬁrst use a good isospin basis for the Hamiltonian with these
1Such as the Facility for Rare Isotope Beams (FRIB) at Michigan State University.
109
nuclear interactions only, because the number of isospin basis states can be somewhat
smaller than the charge basis we use now. We can save the spatial and other relevant
conﬁgurations, and then, we can use them to calculate the isospin breaking parts
perturbatively (Lonardoni et al. (2018b)).
We may also try to combine AFDMC ideas to eﬃciently sample the spin isospin
states instead of summing over them. If this can be made possible it will signiﬁcantly
reduce the computation time for PIMC calculations of larger nuclei.
A nuclear PIMC ﬁnite temperature calculation of 4He or neutron matter including
three-body interactions is also possible. That can be a pioneering step towards QMC
calculations in continuous space for a ﬁnite temperature nuclear equation of state (Li
et al. (2008); Chen et al. (2010)).
However, large nuclei and ﬁnite temperature nuclear matter PIMC calculations will
inevitably lead to large variance due to sign problem unless approximate methods like
adding ﬁxed phase or ﬁxed node constraints are used. The sign problem has no known
general ﬁx yet. Improving the trial wave function and the short-time propagator, and
constraining the path can somewhat make the sign problem less severe or eliminate it
giving an approximate result.
Last but not least, even though we will face sign problem, and, even with the most
powerful supercomputers today, there are still problems in QMC that seem to make
calculating large nuclei or the equation of state at ﬁnite temperature not accessible
at the current stage, those messes simply mean there are big opportunities. I simply
cannot imagine human beings cannot go far beyond the current situation (Laughlin
and Pines (2000)). And I would like to use Steven Weinberg’s advice (Weinberg (2003))
to end my dissertation, which is also what I learned from my advisor professor Kevin
E. Schmidt these years:
“ ... go for the messes — that’s where the action is. ”
110
