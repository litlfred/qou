---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-043-51-summary
section_title: "Summary"
section_number: 5.1
pages: 118-119
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
This work is mainly to answer one of the questions in section 1.1: how to solve the
many-body problem? Our answer is, using the path integral quantum Monte Carlo
method. In nuclear physics, although continuous space light nuclei calculations for
A≤ 4 have been studied before by GFMC (Carlson (1988); Wiringa and Pieper
(2002)), this is the ﬁrst work using PIMC. The code is now publicly available and
open source (Chen and Schmidt (2020)).
By using multiple sampling algorithms, multi-level sampling most of the time, and
occasionally the regular sampling described in section 3.2, as well as the optimized
calculation and updating strategies described in section 2.7.3 and section 3.3, we
successfully performed our ground state nuclear PIMC calculation of light nuclei, based
on the local chiral N 2LO interaction and the AV6’ interaction. From our analysis in
section 4.1.1 and as well as calculation of the potential along the beads shown in Fig.
4.5, we can conclude that our choice of the total imaginary time τ = 0.2 MeV−1 indeed
projected out the ground state, so our results are reliable. As discussed in section 4.1.1,
the time step ∆τ we use is 10−4∼ 10−3 MeV−1 which are about 5 times bigger than
GFMC calculations. This indicates that PIMC calculations are less sensitive to ∆ τ
than GFMC is, due to the time step error structure of the PIMC expectation value
such as Eq.(2.78) or Eq.(2.81).
Our PIMC ground state energies of light nuclei are consistent with the results
from GFMC and AFDMC as shown in Tables 4.1 and 4.2. For operators which do not
108
commute with Hamiltonian and therefore usually cannot be obtained from DMC based
methods such as GFMC and AFDMC without tradeoﬀs, we calculated the particle
number density distributionρ(r), rms radii, and the angle averaged response functions.
Our results are comparable with the GFMC results.
