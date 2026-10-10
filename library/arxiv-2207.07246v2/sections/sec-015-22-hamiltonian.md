---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-015-22-hamiltonian
section_title: "Hamiltonian"
section_number: 2.2
pages: 29-33
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
In this work, the Hamiltonian H of our light nuclei calculations is non-relativistic.
It can be written as,
H =
A∑
i=1
p2
i
2m +
∑
i<j
Vij, (2.17)
where A is total number of nucleons in the system, pi =−iℏ∇i is the momentum
of particle i in real space. The complete two body interaction for a given ij pair of
particles, Vij, is composed of the nucleon-nucleon interaction VNN
ij and the electric
magnetic force VEM
ij ,
Vij =VNN
ij +VEM
ij . (2.18)
By using both the local chiral interaction with N 2LO (Gezerlis et al. (2014); Lynn
et al. (2017); Lonardoni et al. (2018b)) and the Argonnev′
6 (AV6’) interaction (Wiringa
and Pieper (2002)), we use PIMC to calculate the ground state properties of light
nuclei such as 2H, 3H, 3He and 4He. The nucleon-nucleon interaction is written as,
VNN
ij =
7∑
p=1
vp(rij)Op
ij, (2.19)
where rij is the length of rij, vp(rij) is the radial function for the pth operator, and
they are diﬀerent for chiral and AV6’ interactions. The ﬁrst 6 of the operators Op
ij are
19
1,τi·τj,σi·σj,σi·σjτi·τj, Sij and Sijτi·τj, whereσ andτ are spin and isospin
operators. The tensor force Sij which comes from one-pion-exchange (OPE) is ,
Sij = 3σi· ˆrσj· ˆr−σi·σj, (2.20)
where ˆr is the unit vector of rij. Note that the spin term σi·σj = 2Pσ
ij− 1 and isospin
termτi·τj = 2Pτ
ij− 1 wherePσ
ij andPτ
ij are spin and isospin exchange operators. The
tensor force ﬂips the spins of nucleons.
The AV6’ is a local interaction, which is a six operator truncation of the full
Argonne AV18 NN interaction (Wiringa et al. (1995)) which consists of 18 operators.
The prime symbol means that the parameters in AV6’ are reﬁtted and therefore they
are diﬀerent from those in AV18. The AV6’ only contain the ﬁrst 6 operators, it does
not have the 7 th operator O7
ij, so its v7(rij) = 0.
When we say a potential is local, the word ‘local’ means the operators can be
determined once the positions of particles are given. If an interaction contains mostly
local operators, it is a local interaction. If an interaction contains some non-local
operators, usually like momentum operatorp and/or powers ofp, it is ‘non-local’. This
is because momentum operator in real space is a diﬀerential operator, if it operates on
a function f(x) then we need to calculate the derivative of the function f′(x). The
value off(x) is not enough to determine f′(x), we need to know the value of f(x +dx)
at x +dx so that we can calculate f′(x), so the information at the local point x is not
enough, information at x +dx is needed, so it is called ‘non-local’. If an interaction
containspn, then in order to compute f (n)(x) at x, we need to know all the non-local
information of f(x +dx), f(x + 2dx), ..., f(x +ndx), so as the integer n increase, the
interaction will become more and more ‘non-local’.
Chiral interactions from ChEFT are obtained based on a momentum expansion so
they are naturally non-local, so computing them is usually not easy for real space QMC
20
methods. However, it was shown that up to N 2LO, we are able to obtain a mostly
local version of chiral interaction (Gezerlis et al. (2013)) which is suitable for QMC
calculations (Lynn et al. (2014); Gezerlis et al. (2014); Lynn et al. (2017); Lonardoni
et al. (2018a,b)). For chiral local N 2LO interaction, it has the same 6 local operators
as AV6’, just with diﬀerent radial functions. However it has the 7 th operator in the
VNN
ij in Eq.(2.19), and it is the spin-orbit term (Lonardoni et al. (2018b)) which is
O7
ij =L·S, (2.21)
whereL is the relative angular momentum operator and S is the total spin operator,
L = 1
2ℏ(ri−rj)× (pi−pj), (2.22)
S = 1
2(σi +σj). (2.23)
With the radial function v7(rij), the spin-orbit interaction vLS(rij) is,
vLS(rij) =v7(rij)L·S, (2.24)
The complete chiral N2LO interaction also has a three body interaction (Lonardoni
et al. (2018b)), V3b = ∑
i<j<kVijk, which to the linear order approximation in the
propagator can be straightforwardly added in light nuclei PIMC calculations. Since
our PIMC calculation is mainly a benchmark test, we did not include three body
interaction in this work.
For the electromagnetic (EM) force VEM
ij , here we only consider the Coulomb force
vC(rij) between proton and proton (pp) which contains the proton charge form factor,
VEM
ij =vC(rij)Pp
iPp
j. (2.25)
where Pp
i = (1 + τiz)/2 is the proton projection operator and τiz is the isospin z
operator of ith particle. Coulomb interaction is long range and the NN interaction is
short range (typically less than 2 fm).
21
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48
/s48
/s50/s48/s48
/s52/s48/s48
/s54/s48/s48
/s56/s48/s48
/s49/s48/s48/s48
/s49/s50/s48/s48
/s49/s52/s48/s48
/s49/s54/s48/s48
/s49/s56/s48/s48
/s50/s48/s48/s48
/s50/s50/s48/s48
/s50/s52/s48/s48
/s50/s54/s48/s48
/s32/s65/s86/s54/s39
/s32/s78
/s50
/s76/s79/s32/s40/s82
/s48
/s61/s49/s46/s48/s32/s102/s109/s41
/s32/s78
/s50
/s76/s79/s32/s40/s82
/s48
/s61/s49/s46/s50/s32/s102/s109/s41
/s67/s111/s117/s108/s111/s109/s98
/s83/s112/s105/s110/s45/s79/s114/s98/s105/s116
/s84 /s101/s110/s115/s111/s114/s45/s73/s115/s111/s115/s112/s105/s110
/s84 /s101/s110/s115/s111/s114
/s83/s112/s105/s110/s45/s73/s115/s111/s115/s112/s105/s110
/s83/s112/s105/s110
/s73/s115/s111/s115/s112/s105/s110
/s82/s97/s100/s105/s97/s108/s32/s70/s117/s110/s99/s116/s105/s111/s110/s115/s32/s118
/s112 
/s40/s114/s41/s32/s40/s77/s101/s86/s41
/s114/s32/s40/s102/s109 /s41
/s67/s101/s110/s116/s114/s97/s108
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48
/s45/s50/s48
/s48
/s50/s48
/s52/s48
/s54/s48
/s56/s48
/s49/s48/s48
/s114/s32/s40/s102/s109/s41
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48
/s45/s49/s48/s48
/s45/s56/s48
/s45/s54/s48
/s45/s52/s48
/s45/s50/s48
/s48
/s50/s48
/s114/s32/s40/s102/s109/s41
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48
/s45/s56/s48
/s45/s54/s48
/s45/s52/s48
/s45/s50/s48
/s48
/s50/s48
/s52/s48
/s114/s32/s40/s102/s109/s41
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48
/s45/s50/s48
/s45/s49/s48
/s48
/s49/s48
/s50/s48
/s51/s48
/s114/s32/s40/s102/s109/s41
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48
/s45/s49/s48/s48
/s45/s56/s48
/s45/s54/s48
/s45/s52/s48
/s45/s50/s48
/s48
/s50/s48
/s52/s48
/s114/s32/s40/s102/s109/s41
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48
/s45/s50/s48
/s45/s49/s48
/s48
/s49/s48
/s50/s48
/s51/s48
/s52/s48
/s53/s48
/s114/s32/s40/s102/s109/s41
/s48 /s53 /s49/s48 /s49/s53 /s50/s48 /s50/s53 /s51/s48 /s51/s53 /s52/s48
/s48/s46/s48
/s48/s46/s50
/s48/s46/s52
/s48/s46/s54
/s48/s46/s56
/s49/s46/s48
/s49/s46/s50
/s49/s46/s52
/s49/s46/s54
/s49/s46/s56
/s50/s46/s48
/s114/s32/s40/s102/s109/s41
Figure 2.2: Radial functions of the AV6’ and the chiral N 2LO interaction.
The total potential energy operator V is,
V =
∑
i<j
Vij =
∑
i<j
(VNN
ij +VEM
ij ). (2.26)
Fig. 2.2 shows the radial function of each operator in AV6’ and chiral N 2LO
interaction. For the chiral N2LO interactions, their spectral-function-regularization
(SFR) cutoﬀ ˜Λ is chosen to be 1000 MeV, and we list the radial functions for coordinate-
space cutoﬀ R0 = 1.0 fm and R0 = 1.2 fm cases (Gezerlis et al. (2014)). We ﬁnd that
22
the chiral N 2LO interactions are much softer than AV6’ interaction. Usually a soft
potential is computationally more easy to simulate than hard ones. Because for soft
potentials the chance that we meet with very big or very small values of potentials are
much lower than hard ones, and this may lead to less variance (smaller error bar) in
the results.
