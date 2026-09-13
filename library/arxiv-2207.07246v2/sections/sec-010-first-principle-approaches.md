---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-010-first-principle-approaches
section_title: "First principle approaches"
section_number: null
pages: 16-20
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
First principle, or ab initio calculations are referring to those methods which are aiming
at directly solving the Schr ¨odinger equation of the system. The no-core shell-model
(NCSM) (Navr´ atilet al. (2009); Barrett et al. (2013)), coupled cluster theory (Hagen
et al. (2014)), and quantum Monte Carlo method (QMC) (Carlson et al. (2015)) are
by far the three most successful and most mentioned methods. Each of them have
their own advantages in their ability to approach speciﬁc problems.
6
NCSM is basically a method for solving for the eigenvalues of the Hamiltonian
matrix in the time-independent Schr ¨odinger equation, by adding the truncated Jacobi-
coordinate and/or the single-nucleon Slater determinant Harmonic oscillator (HO)
Hamiltonian to the original NCSM Hamiltonian, and therefore use a truncated HO
basis to calculate the modiﬁed Hamiltonian matrix. The eﬀects from HO Hamiltonian
are subtracted in order to get correct results. The number of HO basis has to be
truncated to make NCSM calculable. However that raises a problem. If the potential
is hard instead of soft 3 , then the truncated momentum for the HO basis may not
be high enough for the hard potential and the calculation will not converge. Usually
NCSM works best with a soft potential.
Coupled cluster method is mostly used to calculate the properties of closed-shell
or nearly closed-shell nuclei. It deﬁnes a similarity-transformed Hamiltonian ¯H =
e−THNeT whereHN is a normal ordered Hamiltonian derived from the original Hamil-
tonianH, andT is the cluster operator. It ﬁnds the ground state by using a variational
method to minimize the energy functional E(L,T )≡⟨φ|Le−THNeT|φ⟩ =⟨φ|L ¯H|φ⟩,
where L is the de-excitation operator and |φ⟩ is a trial state. The variation of E(L,T )
with respect to the truncated operator L yields a set of so called coupled clusters with
singles and doubles (excitations) approximation (CCSD) equations. Solving for the
cluster amplitudes from T in those CCSD equations, one can show that they give
the ground state energy E0 =⟨φ| ¯H|φ⟩. We can also do variations with respect to the
cluster amplitudes in T , that will yield other sets of equations. The solved coeﬃcients
fromL in those equations can be used to solve for the excited energies or other physics
quantities. In coupled cluster calculations, ¯H needs to be expanded by using the Baker-
Campbell-Hausdorﬀ (BCH) expansion H =HN + [HN,T ] + 1
2! [[HN,T ],T ] +.... and
3By ‘soft’ we mean the potential remain relatively small when the distance r between the nucleons
r→ 0 and it varies not too abruptly with r. ‘Hard’ is the opposite.
7
this can be represented by diagrams just like the Feynman diagrams in high energy
physics. For ground state calculations, the diagrams with three or more body nature
will vanish so one only needs to calculate those with two-body nature. This feature
makes the coupled cluster method computationally attractive. The computational
cost in coupled cluster are mainly in solving those non-linear CCSD equations, and
the number of the equations depends on the size of the basis. So, with the current
technique, it must truncate the basis (usually HO basis) in its model space, especially
for medium and large nuclei calculations. Consequently, like NCSM, it works best with
soft potentials, otherwise one needs to modify the potential in some way to make it
soft.
Unlike NCSM which aims at solving for the eigenvalues of the eﬀective Hamiltonian
matrix and the coupled-cluster method which requires solving for many non-linear
equations, QMC methods seeks the solution of many-body system from the stochastic
process called the Monte Carlo (MC) method (Kalos and Whitlock (1986)), and so
QMC codes can naturally be made highly parallel and therefore particularly suited
for modern high performance computing. QMC methods are among the most trusted
methods since approximations, if any, can be well characterized. In the last 30 years,
signiﬁcant progress has been made either in continuous space time (Carlson et al.
(2015)) or on the lattice (Lee (2009); Epelbaum et al. (2012)). Nuclear QMC methods
have achieved wide success in accurately calculating the properties of light nuclei and
neutron matter using realistic nuclear interactions such as the Argonne potentials
(Wiringa et al. (1995); Wiringa and Pieper (2002)) and the ChEFT potentials (Lynn
et al. (2014); Gezerlis et al. (2014); Lynn et al. (2017); Lonardoni et al. (2018a,b)).
QMC methods in continuous space are called continuum QMC. In this work,
we focus on continuum QMC. These methods are mainly variational Monte Carlo 4
4Brief introductions to VMC is in Appendix A.
8
(VMC), Diﬀusion Monte Carlo (DMC) 5 (Hammond et al. (1994)) and path integral
Monte Carlo (Ceperley (1995)). DMC and PIMC both project out the ground state
from the trial wave function by applying the short imaginary time propagator e−H∆τ
repeatedly until all the excited states are removed, but in a diﬀerent way which will
be introduced in chapter 2. Usually one begins from VMC to ﬁnd some optimized
parameters in the trial wave function that minimize the expectation value of the energy.
One starts the DMC or PIMC from the optimized trial wave function to project out
the ground state.
Green’s function Monte Carlo (GFMC) (Carlson (1987)) and auxiliary ﬁeld diﬀusion
Monte Carlo 6 (AFDMC) (Schmidt and Fantoni (1999)) are both DMC methods, and
they are among the most successful ones in nuclear physics. GFMC for bosons was
introduced by Malvin Kalos (Kalos et al. (1974)), nowadays the GFMC for nuclear
physics is the one introduced in late 1980s by Joseph Carlson (Carlson (1987)) who
included the spin and isospin degrees of freedom for nucleons.
In GFMC, for a system of A nucleons with Z protons, charge conservation gives
CZ
A≡ A!
Z!(Z−A)! isospin states, and 2A spin states, so the trial wave function is composed
of 2ACZ
A = 2A×A!
Z!(Z−A)! spin/isospin basis states. GFMC yields very accurate results
because it sums over all the spin isospin states, but the number of basis states for
the wave function will be too big for heavy nuclei to be calculable. For this reason, at
the current stage, GFMC calculations are not able to go far beyond 12C because the
computational cost is too high 7 .
AFDMC in nuclear physics was invented in late 1990s by Kevin E. Schmidt and
Stefano Fantoni (Schmidt and Fantoni (1999)). The idea was to use a trial wave function
5Brief introductions to DMC is in Appendix B.
6Brief introductions to AFDMC is in Appendix C.
7For 12C, GFMC cost about 130 million core hours (Lovato et al. (2020)) on the MIRA supercom-
puter at Argonne National Laboratory located in Lemont, Illinois, USA.
9
that scales better than GFMC’s, and sample the spin isospin states by introducing
auxiliary variables (ﬁelds) using a Hubbard-Stratonovich (HS) transformation (Carlson
et al. (2015)) of the operators in the potential. A convenient form of wave functions
in AFDMC is a Slater determinant which has A single-particle orbitals, so the wave
function is a determinant of an A×A matrix and the computational cost is the order
of A3 operations (Wikipedia contributors (2020a)) which is signiﬁcantly cheaper than
GFMC’s. Another choice can be the Pfaﬃan pairing wave function (Bajdich et al.
(2006)) which also scales as O(A3). Currently, including 3NF from ChEFT, AFDMC
was able to accurately calculate nuclei up to 16O (Lonardoni et al. (2018a)), and it
has calculated systems with up to 100 nucleons interacting with a 2NF.
