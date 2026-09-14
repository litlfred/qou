---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-025-28-sign-problem
section_title: "Sign Problem"
section_number: 2.8
pages: 59-61
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
Since wave functions for fermions are antisymmetric under interchange of the
particles, they necessarily can change sign. Except for a few special cases where the
Monte Carlo sampling can be arranged so that sign changes for two types of fermions
occur together, fermion quantum Monte Carlo has a sign or phase problem (Umrigar
et al. (2007); Alhassid et al. (1994); Li and Yao (2019)). This means that for a long
enough path it is possible to propagate from a region where the wave function is
positive to one where it is negative (or has a diﬀerent phase). In such a case as the
total imaginary time for the path increases, these sign changes make the signal to
noise ratio decay exponentially, or, for a ﬁxed amount of computer time, the variance
increases exponentially with the total imaginary time.
For the light nuclei here, there would be no sign problem if the potential were
spin-isospin independent. In that case, the four spin-isospin states proton up, proton
down, neutron up, neutron down would not be mixed by the interaction, and can be
interpreted as diﬀerent kinds of particles. The spatial part of the wave function would
be positive deﬁnite.
Realistic interactions change the spin and isospin, but the fact that the wave
function is still predominantly in this “s-shell” means that the fermion sign problem
49
is weak. As shown in this work, for imaginary times that converge the system to the
ground state, the fraction of negative paths is small and we simply ignore the sign
problem. That is, our calculations need no approximations to deal with the fermion
sign problem 8 .
Extensions of this method to larger systems will necessary require dealing with a
stronger sign or phase problem. We expect that the approximate methods developed for
GFMC and AFDMC can be applied. Those methods include ﬁxed node approximation
(Moskowitz et al. (1982); Anderson (1995)), constrained-path approximation (Zhang
and Krakauer (2003); Gandolﬁ et al. (2009); Motta and Zhang (2018)), ﬁxed-phase
approximation (Carlson (1987)), eigenvector continuation method (Frameet al. (2018)),
etc.
8In PIMC calculation, the sign problem is equivalent to say that the Blr(R) in Eq.(2.100) we
sampled may frequently oscillate between 1 and -1, which can make the ⟨Blr(R)⟩ in Eq.(2.87) close
to zero and therefore lead to a big error bar. However, In our light nuclei PIMC calculation, e.g. the
4He calculation, we ﬁnd ⟨Blr(R)⟩≈ 0.9 which means there are only about 5% of the Blr(R) samples
ﬂip their signs from 1 to -1. So we do not have any serious sign problems in this work, partially
because our total imaginary time is not big, and also we are summing over all the spin isospin states
and this makes the sign ﬂipping less likely to happen.
50
Chapter 3
