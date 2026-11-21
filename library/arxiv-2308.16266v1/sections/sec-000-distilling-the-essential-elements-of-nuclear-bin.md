---
doc_id: arxiv-2308.16266v1
doc_title: "Distilling the essential elements of nuclear binding via neural-network quantum states"
section_id: sec-000-distilling-the-essential-elements-of-nuclear-bin
section_title: "Distilling the essential elements of nuclear binding via neural-network quantum states"
section_number: null
pages: 1-7
source_pdf: 2308.16266v1.pdf
source_sha256: 59f0cbfb48d717bb
toc_source: outline
doc_brief: "Distilling the essential elements of nuclear binding via neural-network quantum states — 2 sections: Distilling the essential elements ; Appendix: Wigner-Eckart"
---
Alex Gnech,1, 2 Bryce Fore,3 and Alessandro Lovato2, 3, 4
1European Center for Theoretical Studies in Nuclear Physics and Related Areas (ECT*)
and Fondazione Bruno Kessler Strada delle Tabarelle 286, I-38123 Villazzano (TN), Italy
2INFN-TIFPA Trento Institute of Fundamental Physics and Applications, 38123 Trento, Italy
3Physics Division, Argonne National Laboratory, Argonne, IL 60439, USA
4Computational Science Division, Argonne National Laboratory, Argonne, IL 60439, USA
(Dated: September 1, 2023)
In pursuing the essential elements of nuclear binding, we compute ground-state properties of
atomic nuclei with up to A = 20 nucleons, using as input a leading order pionless effective field theory
Hamiltonian. A variational Monte Carlo method based on a new, highly-expressive, neural-network
quantum state ansatz is employed to solve the many-body Schr¨odinger equation in a systematically
improvable fashion. In addition to binding energies and charge radii, we accurately evaluate the
magnetic moments of these nuclei, as they reveal the self-emergence of the shell structure, which is
not a priori encoded in the neural-network ansatz. To this aim, we introduce a novel computational
protocol based on adding an external magnetic field to the nuclear Hamiltonian, which allows the
neural network to learn the preferred polarization of the nucleus within the given magnetic field.
Introduction.—
Understanding
emerging
nuclear
properties from the interactions among protons and neu-
trons is a longstanding challenge of nuclear theory [1].
To address this complex problem,
accurate nuclear
Hamiltonians
have
been
constructed
either
within
phenomenological approaches [2, 3] or by leveraging the
broken chiral symmetry of QCD [4–11].
Sophisticated
potentials are spin-isospin dependent, typically entail
high-momentum components, and involve several fitting
parameters, usually determined on light nuclear systems.
Quantum many-body methods solve the Schr¨odinger
equation associated with these Hamiltonians with con-
trolled approximations, leading to remarkable success in
computing nuclei across the nuclear chart [12–19]. How-
ever, important questions remain unanswered.
For in-
stance, no existing Hamiltonian can simultaneously re-
produce with high precision the properties of light nu-
clear systems, the charge radii of medium-mass nuclei,
and the neutron-matter equation of state [20–24].
The quest for distilling the “essential elements of nu-
clear binding” has arisen from these challenges, seeking
the simplest nuclear Hamiltonian yielding binding ener-
gies and charge radii across the nuclear chart with few
percent errors [25].
Arguments based on the unitary
limit, large Nc, and SU(4) symmetry [25–28] suggest
that such a Hamiltonian could be derived within pion-
less effective field theory (/πEFT) [29].
In Ref. [25] it
was proven that a SU(4)-symmetric Hamiltonian, with a
non-local three-body force, can accurately model ground-
state properties of several nuclei up to A = 40 nucleons
and neutron matter up to saturation density. Similarly,
the leading-order (LO) /πEFT Hamiltonian “o” developed
in Ref. [30] reproduces reasonably well the binding ener-
gies of various closed-shell nuclei and yields a neutron
matter equation of state that is remarkably close to real-
istic Hamiltonians [31] at low densities.
In this work, we carry out an in-depth assessment
of the proposed essential Hamiltonians by computing
ground-state properties of nuclei with up to A = 20 nu-
cleons. In addition to their binding energies and radii,
we analyze their magnetic moments, which determine the
interactions of nuclei with external magnetic fields and
contribute to the hyperfine structure in the electronic
spectra of the atom [32]. Owing to the significant dif-
ference between the g factors associated with the orbital
and spin angular momenta of protons and neutrons, they
are an ideal test-bed for nuclear models [33].
Variational Monte Carlo (VMC) and Green’s function
Monte Carlo (GFMC) calculations of light nuclei carried
out with realistic Hamiltonians demonstrated the need
for two-body contributions in the electromagnetic cur-
rents [34, 35]. Owing to the exponential growth of the
spin-isospin basis [17], the GFMC is limited to A ≤12
nuclei. The authors of Ref. [36] used the auxiliary-field
diffusion Monte Carlo (AFDMC) to evaluate magnetic
moments of nuclei up to 17F using chiral-EFT Hamil-
tonians and consistent currents. However, the AFDMC
cannot reach much larger systems, owing to the fermion-
sign problem, which is exacerbated by the use of over-
simplified variational wave functions [37].
To overcome these limitations, building on the suc-
cess of earlier works [38–41],
we solve the nuclear
many-body Schr¨odinger equation in a systematically-
improvable fashion using a VMC method based on a
neural-network quantum state (NQS) ansatz.
The ex-
pressivity of the hidden-nucleon NQS, initially developed
to model the ground-state wave functions of 3H, 3He,
4He, and 16O [42], and dilute neutron matter [31], is
augmented through neural backflow transformations [43].
The latter are realized by a simplified version of the
permutation-equivariant message-passing neural network
(MPNN), recently adopted to compute the homogeneous
electron gas [44] and cold Fermi gases [45]. To reliably
evaluate the nuclear magnetic moments, we introduce
arXiv:2308.16266v1  [nucl-th]  30 Aug 2023
a novel computational protocol that allows the NQS to
learn the preferred polarization of the nucleus.
Methods.—
We model the interactions among pro-
tons and neutrons with the LO /πEFT Hamiltonian, “o”,
developed in Ref. [30]. The nucleon-nucleon potential re-
produces the np scattering lengths and effective ranges in
the S/T = 0/1 and 1/0 channels, and it vanishes in odd
partial waves. We assume the electromagnetic compo-
nent to only include the Coulomb force between finite-size
protons. A repulsive three-body force is needed to stabi-
lize the systems with more than two nucleons against the
Thomas collapse. AFDMC and VMC-NQS calculations
showed that the choice R3 = 1.0 fm for the three-nucleon
regulator overbinds 16O and heavier nuclei [30, 42]. To
counter it, we opt for R3 = 1.1 fm, as the extended range
introduces additional repulsion in heavier systems.
We introduce X = {x1 . . . xA} to denote the set of
single-particle coordinates xi = {ri, sz
i , tz
i }, which de-
scribe the spatial positions and the z-projection of the
spin-isospin degrees of freedom of the A nucleons. The
hidden-nucleon wave function [42, 46] reads
ΨHN(X) ≡det
ϕv(X) ϕv(Xh)
ϕh(X) ϕh(Xh)

,
(1)
where, ϕv and ϕh denote the visible and hidden orbitals,
while X and Xh are the A visible and the Ah hidden
coordinates. Hence, the dimension of the sub-matrices
ϕv(X), ϕv(Xh), ϕh(X), and ϕh(Xh) are A × A, Ah × A,
A×Ah, and Ah ×Ah, respectively. As a major departure
from Ref. [42], all the above matrices are complex val-
ued, and two separate deep neural networks with differ-
entiable activation functions parametrize the logarithm
of their moduli and phases.
To respect fermion anti-
symmetry, the coordinates of the hidden nucleons Xh
are permutation-invariant functions of the visible ones.
We enforce this symmetry using a Deep-Sets architec-
ture [47, 48] with logsumexp pooling.
As in recent neutron-matter studies [31], we improve
the flexibility of the ansatz by applying equivariant back-
flow transformations to pre-process the single-nucleon co-
ordinates and include correlation effects. These transfor-
mations are implemented by means of a simplified version
of the MPNN employed in Refs. [44, 45]
yi = h

xi,
X
j
m(xi, xj)

.
(2)
Due to the universality of the hidden-nucleon ansatz,
the single, albeit enlarged Slater determinant in Eq.(1)
is sufficient for modeling the ground-state wave function
of both closed- and open-shell nuclei, regardless of their
deformation. This characteristic represents a significant
advantage compared to “conventional” quantum Monte
Carlo methods, where multiple Slater determinants are
required to model open-shell systems [49, 50]. In stark
2H
3H
3He 4He
6Li
7Li
7Be 12C
15N 15O 16O 17O 20Ne
8
7
6
5
4
3
2
1
E/A (MeV)
Exp
VMC-NQS
2H
3H
3He 4He
6Li
7Li
7Be 12C
15N 15O 16O 17O 20Ne
1.6
1.8
2.0
2.2
2.4
2.6
2.8
3.0
3.2
r2
ch (fm)
FIG. 1.
VMC-NQS energy per particle (upper panel) and
charge radii (lower panel) of selected nuclei with up to A = 20
nucleons as obtained from the LO EFT Hamiltonian “o” of
Ref. [30] with R3 = 1.1 fm compared with experimental data.
contrast with the majority of nuclear many-body meth-
ods, the shell structure of the nucleus is not directly en-
coded in the NQS, as the parameters of the network are
randomly initialized and no pre-training on a Hartree-
Fock wave function is performed. All ground-state prop-
erties self-emerge during the training of the network,
which is performed by minimizing the variational energy
of the system. For this purpose, we employ the stochastic
reconfiguration algorithm [51] with regularization based
on the RMSprop method [42].
The expectation value
of the Hamiltonian and other quantum-mechanical op-
erators of interest is evaluated stochastically using the
Metropolis-Hastings algorithm detailed in the Supple-
mental Material of Ref. [39], sampling both the spatial
and spin-isospin coordinates of the A nucleon
Results.—
The upper panel of Fig. 1 displays the
ground-state energies per nucleon of selected A ≤20
nuclei obtained solving the ground-state of the /πEFT
Hamiltonian with the VMC-NQS method.
The agree-
ment between the computed and experimental values is
remarkably good, given the simplicity of the /πEFT in-
put Hamiltonian.
Notably, our ground-state energies
are closer to experimental values than those obtained in
Ref. [36] with the AFDMC method and N2LO chiral-EFT
interactions. Additionally, we do not observe the increas-
ing overbinding with the number of nucleons reported in
no-core shell model calculations that use as input differ-
ent N2LO two- and three-body forces [52]. Nevertheless,
12C and 15O are under-bound by about 0.6 MeV per
nucleon, while 6He, 8Li, 8B, 9C, and 17F are unstable
against breakup into smaller clusters. This behavior sug-
gests an excessive repulsion from the input Hamiltonian,
as increasing the flexibility of the NQS by considering
more hidden nucleons does not significantly improve the
variational energies.
In the lower panel of Fig. 1, we show the charge radii
of the same nuclei, which are are derived from the esti-
mates for the point-proton radii taking into account the
finite-size of the nucleons and the Darwin-Foldy correc-
tion. Here we neglect both the one-body spin-orbit cor-
rection of Ref. [53] and two-body terms in the charge op-
erator [54]. While the overall trend of experimental data
is well reproduced, 2H, 4He, and 16O are slightly smaller
than experiments. On the other hand, consistent with
the ground-state energies, the radii of 6Li, 7Li, 7Be, and
12C are too large — there is no available experimental
data for 15O. In contrast to many-body methods relying
on the harmonic-oscillator basis expansion [55], the ra-
dius converges quickly in our VMC-NQS calculations due
to the stability of the method. Hence, the discrepancies
between theoretical calculations and experimental data
are likely to be ascribed to deficiencies in the input LO
/πEFT Hamiltonian.
At LO in the electroweak current operator, the expec-
tation value of the magnetic moment is given by
µ = ⟨ΨHN| P
i P p
i Lz
i + (µS + µV τ z
i )σz
i |ΨHN⟩
⟨ΨHN|ΨHN⟩
.
(3)
In the above equation, Lz
i = −i(ri × ∇i)z is the pro-
jection of the orbital angular momentum on the z axis,
while µS = 0.8798 µN and µV = 4.0759 µN, and µN
is the nuclear magneton. The above definition assumes
that the wave function of the nucleus has well defined
total angular momentum J and maximal projection on
the z axis:
Jz = J.
Since the LO /πEFT Hamilto-
nian that we employ does not contain tensor or spin-
orbit interactions, its ground state is an eigenstate of
the total spin S and total orbital angular momentum
L and it is degenerate in their projections Sz and Lz:
|ΨHN; L, S⟩= P
LzSz cL,S
LzSz|L, Lz; S, Sz⟩.
The total polarization of the system Sz is conveniently
fixed in the Metropolis Hastings Sampling. Hence, since
the ground states of 2H, 3H, 3He, and 6Li are all L =
0 (and hence Lz = 0), they are also eigenstates of J
and Jz.
On the other hand, evaluating the magnetic
moments of heavier nuclei requires projecting the NQS
onto a given value of Lz. To this aim, we have devised
a three-stage algorithm. i) A standard SR minimization
of the variational energy is carried out to find a good
0
500
1000 1500 2000 2500 3000 3500 4000 4500
1.3
1.4
1.5
1.6
J
(a)
0
500
1000 1500 2000 2500 3000 3500 4000 4500
0.6
0.8
1.0
1.2
1.4
1.6
Jz
(b)
0
500
1000 1500 2000 2500 3000 3500 4000 4500
Iterations
2.8
2.9
3.0
3.1
[
N]
(c)
Bz = 0
Bz = 2.5
FIG. 2. Total angular momentum, its projection on the z-
axis, and the magnetic moment of 7Li while projecting the
NQS onto the state with J, Jz = 3/2, 3/2. The magnetic field
Bz = 2.5 MeV is switched off after 2500 iterations as indicated
by the vertical green line. The orange dashed lines represent
the target values J = 3/2 and, Jz = 3/2.
approximation for the nuclear ground state. ii) A small
external magnetic field is added to the Hamiltonian, H →
H −BzLz, and another energy minimization is carried
out to resolve the degeneracy favoring larger values of Lz.
iii) The magnetic field is switched off, and additional SR
steps are performed to remove the spurious excitations in
the NQS generated by the external magnetic field. This
procedure allows us to select the state with Lz = L, and
hence J = Jz, provided that S and L be aligned.
Fig. 2 illustrates the last two stages of the algorithm
applied to 7Li, with a ground state of Jπ = 3/2+. Pan-
els (a) and (b) show that, towards the end of the sec-
ond stage, the magnetic field generates components in
the NQS with J > 3/2, causing the expectation val-
ues of J and Jz to exceed the target values. However,
upon switching off the magnetic field, the SR algorithm
projects out the excited-states contamination, leading
both J and Jz to converge to the desired values. Panel
(c) shows that the external magnetic field enhances the
expectation value of the magnetic moment, stabilizing it
to a converged value when Bz is set to zero.
The NQS wave function of
15O(Jπ
= 1/2+) and
15N(Jπ = 1/2+) are a superposition of J = 1/2 and
3/2. To extract the physical value of the magnetic mo-
ment for nuclei with J < L+S, we first project the NQS
along all allowed Lz for a given L. In order to converge
to a non-maximal value of Lz, i.e.
|Lz| < L, we add
to the Hamiltonian the term Bz|ˆLz −¯Lz|, where ¯Lz is
the target Lz. Once the corresponding matrix elements
⟨L, Lz, S, Sz|µz|L, Lz, S, Sz⟩are computed, we take ad-
vantage of the Wigner-Eckart theorem to estimate the
expectation value of the magnetic moment as defined in
Eq. (3) [see supplemental materials for more details].
2H
3H
3He
6Li
7Li
7Be
15N
15O
17O
2
1
0
1
2
3
(
N)
Exp
VMC-NQS
FIG. 3.
Magnetic moments of selected A ≤20 nuclei ob-
tained from VMC-NQS calculations compared with experi-
mental data.
As shown in Fig. 3, theoretical calculations reproduce
experimental data very well, implying that the input LO
/πEFT Hamiltonian encapsulates the essential elements
of nuclear structure. This agreement also confirms the
correctness of the algorithm discussed for selecting the
polarization of the nucleus.
Finally, it indicates that
NSQ can learn the shell structure of the nucleus, which
is genuinely self-emerging as it was not encoded in the
variational ansatz. The minor discrepancies observed in
3H, and 3He, are consistent with GFMC, AFDMC and
HH results [35, 36, 56] and may well be resolved when
two-body currents are included in the calculation.
Conclusions –
With the overarching aim of elucidat-
ing the essential aspects of nuclear binding, we accurately
computed ground-state properties of atomic nuclei con-
taining up to A = 20 nucleons using as input the LO
/πEFT Hamiltonian “o” of Ref. [30]. To achieve precise
solutions to the many-body Schr¨odinger equation, we em-
ployed a VMC method based on the versatile hidden-
nucleon NQS framework, introduced in Ref. [42]. Tak-
ing inspiration from condensed-matter studies [44, 45],
we significantly enhanced the convergence and expres-
sive power of the original hidden-nucleon ansatz by em-
ploying equivariant backflow transformations based on
MPNN to preprocess the single-nucleon coordinates and
incorporate correlation effects.
In line with the findings of Ref. [25], which employed
a spin-isospin independent, non-local, SU(4)-symmetric
Hamiltonian, our computed binding energies typically
exhibit deviations of only a few percent from experi-
mental values. This level of precision is particularly re-
markable considering the simplicity of the input Hamil-
tonian, especially when compared to the more sophis-
ticated N2LO chiral-EFT interactions that struggle to
replicate ground-state energies with comparable accu-
racy [36]. Furthermore, the /πEFT model “o” considered
in this work — albeit with a slightly different value for
the three-body force regulator — yields a neutron-matter
equation of state that closely resembles the one obtained
from the highly-realistic Argonne v18 plus Urbana IX po-
tentials [31]. This contrasts with the ∆-full chiral-EFT
Hamiltonian “NV2+Ia,” which provides an accurate en-
ergy spectrum for A ≤12 nuclei [11], yet falters in accu-
rately modeling infinite neutron matter [24]. We ascribe
the surprising accuracy of our “essential” Hamiltonian to
a combination of two factors: i) the two-body potential
reproduces peripheral, low-energy nucleon-nucleon scat-
tering, and ii) the three-body force prevents nucleons
from packing too closely, making low-momentum observ-
ables, such as binding energies and radii, insensitive to
short-range details of the nuclear force.
Unlike quantum many-body methods based on single-
particle basis expansion [12, 55], and akin to conventional
QMC methods, NQS have no difficulties in capturing the
slowly-decaying tails of nuclear wave functions, which
play a crucial role in reproducing charge radii. Our the-
oretical calculations align reasonably well with experi-
ments, although some discrepancies are present. Hence,
similar to high-precision chiral-EFT forces [57], charge
radii offer additional insights into nuclear dynamics not
provided by binding energies alone [58, 59].
Lastly, we introduced an innovative computational
protocol to assess magnetic moments, amenable to NQS.
It involves adding to the nuclear Hamiltonian an exter-
nal magnetic field, which projects the NQS onto a spec-
ified value of the orbital angular momentum along the
z axis. Our computed magnetic dipole moments are in
good agreement with experimental data; the discrepan-
cies observed in 3H and 3He are likely to be resolved with
the inclusion of two-body currents [35, 36, 56]. Beyond
serving as an additional test for the underlying Hamilto-
nian, this concordance reveals how nucleons self-organize
within shells, a structural aspect of the nucleus that is
not explicitly embedded within the NQS ansatz but re-
veal its flexibility.
Acknowledgments –
We are grateful to Giuseppe
Carleo, Patrick Fasano, Jordan Fox, Antoine Georges,
Alejandro Kievsky, Jane Kim, Tommaso Morresi, Gabriel
Pescia, Michele Viviani, and Robert B. Wiringa for many
illuminating discussions.
AL and BF are supported
by the U.S. Department of Energy, Office of Science,
Office of Nuclear Physics, under contracts DE-AC02-
06CH11357, by the Department of Energy Early Ca-
reer Award Program, by the NUCLEI SciDAC Program,
and Argonne LDRD awards.
We gratefully acknowl-
edge the computing resources provided on Swing, a high-
performance computing cluster operated by the Labora-
tory Computing Resource Center at Argonne National
Laboratory. We also acknowledge the use of resources of
the National Energy Research Scientific Computing Cen-
ter (NERSC), a U.S. Department of Energy Office of Sci-
ence User Facility located at Lawrence Berkeley National
Laboratory, operated under Contract No.
DE-AC02-
05CH11231 using NERSC award NP-ERCAP0023221.
[1] H. Hergert, “A Guided Tour of ab initio Nuclear
Many-Body Theory,” Front. in Phys. 8, 379 (2020),
arXiv:2008.05061 [nucl-th].
[2] Robert B. Wiringa, V. G. J. Stoks,
and R. Schiavilla,
“An Accurate nucleon-nucleon potential with charge in-
dependence breaking,” Phys. Rev. C 51, 38–51 (1995),
arXiv:nucl-th/9408016.
[3] R. Machleidt, “The High precision, charge dependent
Bonn nucleon-nucleon potential (CD-Bonn),” Phys. Rev.
C 63, 024001 (2001), arXiv:nucl-th/0006014.
[4] D. R. Entem and R. Machleidt, “Accurate charge depen-
dent nucleon nucleon potential at fourth order of chiral
perturbation theory,” Phys. Rev. C 68, 041001 (2003),
arXiv:nucl-th/0304018.
[5] E. Epelbaum, W. Glockle,
and Ulf-G. Meissner, “The
Two-nucleon system at next-to-next-to-next-to-leading
order,” Nucl. Phys. A 747, 362–424 (2005), arXiv:nucl-
th/0405048.
[6] A.
Gezerlis,
I.
Tews,
E.
Epelbaum,
S.
Gandolfi,
K. Hebeler, A. Nogga,
and A. Schwenk, “Quantum
Monte Carlo Calculations with Chiral Effective Field
Theory Interactions,” Phys. Rev. Lett. 111, 032501
(2013), arXiv:1303.6243 [nucl-th].
[7] J. E. Lynn, I. Tews, J. Carlson, S. Gandolfi, A. Gezerlis,
K. E. Schmidt, and A. Schwenk, “Chiral Three-Nucleon
Interactions in Light Nuclei, Neutron-α Scattering, and
Neutron Matter,” Phys. Rev. Lett. 116, 062501 (2016),
arXiv:1509.03470 [nucl-th].
[8] E. Epelbaum, H. Krebs,
and U. G. Meißner, “Preci-
sion nucleon-nucleon potential at fifth order in the chi-
ral expansion,” Phys. Rev. Lett. 115, 122301 (2015),
arXiv:1412.4623 [nucl-th].
[9] M. Piarulli, L. Girlanda, R. Schiavilla, R. Navarro P´erez,
J. E. Amaro,
and E. Ruiz Arriola, “Minimally nonlo-
cal nucleon-nucleon potentials with chiral two-pion ex-
change including ∆resonances,” Phys. Rev. C 91, 024003
(2015), arXiv:1412.6446 [nucl-th].
[10] D. R. Entem, R. Machleidt,
and Y. Nosyk, “High-
quality two-nucleon potentials up to fifth order of the
chiral expansion,” Phys. Rev. C 96, 024004 (2017),
arXiv:1703.05454 [nucl-th].
[11] M.
Piarulli
et
al.,
“Light-nuclei
spectra
from
chi-
ral dynamics,” Phys. Rev. Lett. 120, 052503 (2018),
arXiv:1707.02883 [nucl-th].
[12] Bruce R. Barrett, Petr Navratil, and James P. Vary, “Ab
initio no core shell model,” Prog. Part. Nucl. Phys. 69,
131–181 (2013).
[13] G. Hagen, T. Papenbrock, M. Hjorth-Jensen, and D. J.
Dean, “Coupled-cluster computations of atomic nuclei,”
Rept. Prog. Phys. 77, 096302 (2014), arXiv:1312.7872
[nucl-th].
[14] H. Hergert, S. K. Bogner, T. D. Morris, A. Schwenk, and
K. Tsukiyama, “The In-Medium Similarity Renormaliza-
tion Group: A Novel Ab Initio Method for Nuclei,” Phys.
Rept. 621, 165–222 (2016), arXiv:1512.06956 [nucl-th].
[15] Arianna Carbone, Andrea Cipollone, Carlo Barbieri, Ar-
nau Rios,
and Artur Polls, “Self-consistent Green’s
functions formalism with three-body interactions,” Phys.
Rev. C 88, 054326 (2013), arXiv:1310.3688 [nucl-th].
[16] Evgeny Epelbaum, Hermann Krebs, Dean Lee, and Ulf-
G. Meissner, “Ab initio calculation of the Hoyle state,”
Phys. Rev. Lett. 106, 192501 (2011), arXiv:1101.2547
[nucl-th].
[17] J. Carlson, S. Gandolfi, F. Pederiva, Steven C. Pieper,
R. Schiavilla, K. E. Schmidt, and R. B. Wiringa, “Quan-
tum Monte Carlo methods for nuclear physics,” Rev.
Mod. Phys. 87, 1067 (2015), arXiv:1412.3081 [nucl-th].
[18] T. D. Morris, J. Simonis, S. R. Stroberg, C. Stumpf,
G. Hagen, J. D. Holt, G. R. Jansen, T. Papenbrock,
R. Roth,
and A. Schwenk, “Structure of the light-
est tin isotopes,” Phys. Rev. Lett. 120, 152503 (2018),
arXiv:1709.02786 [nucl-th].
[19] Baishan Hu et al., “Ab initio predictions link the neutron
skin of 208Pb to nuclear forces,” Nature Phys. 18, 1196–
1200 (2022), arXiv:2112.01125 [nucl-th].
[20] Sven Binder, Joachim Langhammer, Angelo Calci, and
Robert Roth, “Ab Initio Path to Heavy Nuclei,” Phys.
Lett. B 736, 119–123 (2014), arXiv:1312.5685 [nucl-th].
[21] D. Lonardoni, A. Lovato, Steven C. Pieper,
and R. B.
Wiringa, “Variational calculation of the ground state of
closed-shell nuclei up to A = 40,” Phys. Rev. C 96,
024326 (2017), arXiv:1705.04337 [nucl-th].
[22] Francesca Sammarruca and Randy Millerson, “Overview
of symmetric nuclear matter properties from chiral inter-
actions up to fourth order of the chiral expansion,” Phys.
Rev. C 104, 064312 (2021), arXiv:2109.01985 [nucl-th].
[23] Y. Nosyk, D. R. Entem,
and R. Machleidt, “Nucleon-
nucleon potentials from ∆-full chiral effective-field-theory
and implications,” Phys. Rev. C 104, 054001 (2021),
arXiv:2107.06452 [nucl-th].
[24] A. Lovato,
I. Bombaci,
D. Logoteta,
M. Piarulli,
and R. B. Wiringa, “Benchmark calculations of in-
finite neutron matter with realistic two- and three-
nucleon potentials,” Phys. Rev. C 105, 055808 (2022),
arXiv:2202.10293 [nucl-th].
[25] Bing-Nan Lu, Ning Li, Serdar Elhatisari, Dean Lee,
Evgeny Epelbaum,
and Ulf-G. Meißner, “Essential el-
ements for nuclear binding,” Phys. Lett. B 797, 134863
(2019), arXiv:1812.10928 [nucl-th].
[26] A. Kievsky,
M. Viviani,
D. Logoteta,
I. Bombaci,
and L. Girlanda, “Correlations imposed by the unitary
limit between few-nucleon systems, nuclear matter and
neutron stars,” Phys. Rev. Lett. 121, 072701 (2018),
arXiv:1806.02636 [nucl-th].
[27] Dean
Lee
et
al.,
“Hidden
Spin-Isospin
Exchange
Symmetry,”
Phys.
Rev.
Lett.
127,
062501
(2021),
arXiv:2010.09420 [nucl-th].
[28] A. Kievsky, L. Girlanda, M. Gattobigio,
and M. Vi-
viani, “Efimov Physics and Connections to Nuclear
Physics,” Ann. Rev. Nucl. Part. Sci. 71, 465–490 (2021),
arXiv:2102.13504 [nucl-th].
[29] Paulo F. Bedaque and Ubirajara van Kolck, “Effective
field theory for few nucleon systems,” Ann. Rev. Nucl.
Part. Sci. 52, 339–396 (2002), arXiv:nucl-th/0203055.
[30] R. Schiavilla, L. Girlanda, A. Gnech, A. Kievsky, A. Lo-
vato, L. E. Marcucci, M. Piarulli, and M. Viviani, “Two-
and three-nucleon contact interactions and ground-state
energies of light- and medium-mass nuclei,” Phys. Rev.
C 103, 054003 (2021), arXiv:2102.02327 [nucl-th].
[31] Bryce Fore, Jane M. Kim, Giuseppe Carleo, Morten
Hjorth-Jensen,
Alessandro Lovato,
and Maria Pi-
arulli, “Dilute neutron star matter from neural-network
quantum states,” Phys. Rev. Res. 5, 033062 (2023),
arXiv:2212.04436 [nucl-th].
[32] Guy
Emery,
“Hyperfine
structure,”
in
Springer Handbook of Atomic, Molecular, and Optical Physics,
edited by Gordon Drake (Springer New York, New York,
NY, 2006) pp. 253–260.
[33] Aage Bohr and Ben R Mottelson, Nuclear Structure
(World
Scientific
Publishing
Company,
1998)
https://www.worldscientific.com/doi/pdf/10.1142/3530.
[34] L. E. Marcucci, Muslema Pervin, Steven C. Pieper,
R. Schiavilla,
and R. B. Wiringa, “Quantum Monte
Carlo calculations of magnetic moments and M1 tran-
sitions in A<=7 nuclei including meson-exchange cur-
rents,” Phys. Rev. C 78, 065501 (2008), arXiv:0810.0547
[nucl-th].
[35] S. Pastore, Steven C. Pieper, R. Schiavilla,
and R. B.
Wiringa, “Quantum Monte Carlo calculations of elec-
tromagnetic moments and transitions in A ≤9 nuclei
with meson-exchange currents derived from chiral ef-
fective field theory,” Phys. Rev. C 87, 035503 (2013),
arXiv:1212.3375 [nucl-th].
[36] J. D. Martin, S. J. Novario, D. Lonardoni, J. Carlson,
S. Gandolfi, and I. Tews, “Auxiliary field diffusion Monte
Carlo calculations of magnetic moments of light nuclei
with chiral EFT interactions,” (2023), arXiv:2301.08349
[nucl-th].
[37] S. Gandolfi, A. Lovato, J. Carlson,
and Kevin E.
Schmidt, “From the lightest nuclei to the equation of
state of asymmetric nuclear matter with realistic nu-
clear interactions,” Phys. Rev. C 90, 061306 (2014),
arXiv:1406.3388 [nucl-th].
[38] J. W. T. Keeble and A. Rios, “Machine learning
the deuteron,” Phys. Lett. B 809, 135743 (2020),
arXiv:1911.13092 [nucl-th].
[39] Corey Adams, Giuseppe Carleo, Alessandro Lovato, and
Noemi Rocco, “Variational Monte Carlo Calculations
of A≤4 Nuclei with an Artificial Neural-Network Cor-
relator Ansatz,” Phys. Rev. Lett. 127, 022502 (2021),
arXiv:2007.14282 [nucl-th].
[40] Alex Gnech, Corey Adams, Nicholas Brawand, Giuseppe
Carleo, Alessandro Lovato,
and Noemi Rocco, “Nuclei
with up to A = 6 nucleons with artificial neural net-
work wave functions,” Few Body Syst. 63, 7 (2022),
arXiv:2108.06836 [nucl-th].
[41] Y. L. Yang and P. W. Zhao, “A consistent descrip-
tion of the relativistic effects and three-body interactions
in atomic nuclei,” Phys. Lett. B 835, 137587 (2022),
arXiv:2206.13208 [nucl-th].
[42] Alessandro Lovato, Corey Adams, Giuseppe Carleo, and
Noemi Rocco, “Hidden-nucleons neural-network quan-
tum states for the nuclear many-body problem,” Phys.
Rev. Res. 4, 043178 (2022), arXiv:2206.10021 [nucl-th].
[43] Di Luo and Bryan K. Clark, “Backflow transformations
via neural networks for quantum many-body wave func-
tions,” Phys. Rev. Lett. 122, 226401 (2019).
[44] Gabriel Pescia, Jannes Nys, Jane Kim, Alessandro Lo-
vato,
and Giuseppe Carleo, “Message-Passing Neural
Quantum States for the Homogeneous Electron Gas,”
(2023), arXiv:2305.07240 [quant-ph].
[45] Jane Kim, Gabriel Pescia, Bryce Fore, Jannes Nys,
Giuseppe Carleo,
Stefano Gandolfi,
Morten Hjorth-
Jensen,
and
Alessandro
Lovato,
“Neural-network
quantum states for ultra-cold Fermi gases,”
(2023),
arXiv:2305.08831 [cond-mat.quant-gas].
[46] Javier
Robledo
Moreno,
Giuseppe
Carleo,
Antoine
Georges, and James Stokes, “Fermionic wave functions
from neural-network constrained hidden states,” Pro-
ceedings of the National Academy of Sciences of the
United States of America 119, e2122059119 (2022).
[47] Manzil Zaheer, Satwik Kottur, Siamak Ravanbakhsh,
Barnabas Poczos, Ruslan Salakhutdinov, and Alexander
Smola, “Deep Sets,” arXiv e-prints , arXiv:1703.06114
(2017), arXiv:1703.06114 [cs.LG].
[48] Edward Wagstaff, Fabian B. Fuchs, Martin Engelcke, In-
gmar Posner,
and Michael Osborne, “On the Limita-
tions of Representing Functions on Sets,” arXiv e-prints
, arXiv:1901.09006 (2019), arXiv:1901.09006 [cs.LG].
[49] D. Lonardoni, S. Gandolfi, J. E. Lynn, C. Petrie, J. Carl-
son, K. E. Schmidt,
and A. Schwenk, “Auxiliary field
diffusion Monte Carlo calculations of light and medium-
mass nuclei with local chiral interactions,” Phys. Rev. C
97, 044318 (2018), arXiv:1802.08932 [nucl-th].
[50] Stefano Gandolfi, Diego Lonardoni, Alessandro Lovato,
and Maria Piarulli, “Atomic nuclei from quantum Monte
Carlo calculations with chiral EFT interactions,” Front.
in Phys. 8, 117 (2020), arXiv:2001.01374 [nucl-th].
[51] Sandro Sorella, “Wave function optimization in the vari-
ational Monte Carlo method,” Phys. Rev. B 71, 241103
(2005).
[52] P. Maris et al., “Light nuclei with semilocal momentum-
space regularized chiral interactions up to third order,”
Phys. Rev. C 103, 054001 (2021), arXiv:2012.12396
[nucl-th].
[53] A. Ong, J. C. Berengut,
and V. V. Flambaum, “The
Effect of spin-orbit nuclear charge density corrections due
to the anomalous magnetic moment on halonuclei,” Phys.
Rev. C 82, 014320 (2010), arXiv:1006.5508 [nucl-th].
[54] A. Lovato, S. Gandolfi, Ralph Butler, J. Carlson, Ew-
ing Lusk, Steven C. Pieper, and R. Schiavilla, “Charge
Form Factor and Sum Rules of Electromagnetic Response
Functions in 12C,” Phys. Rev. Lett. 111, 092501 (2013),
arXiv:1305.6959 [nucl-th].
[55] Mark
A.
Caprio,
Patrick
J.
Fasano,
and
Pieter
Maris, “Robust ab initio prediction of nuclear electric
quadrupole observables by scaling to the charge radius,”
Phys. Rev. C 105, L061302 (2022), arXiv:2206.09307
[nucl-th].
[56] A. Gnech and R. Schiavilla, “Magnetic structure of few-
nucleon systems at high momentum transfers in a chi-
ral effective field theory approach,” Phys. Rev. C 106,
044001 (2022).
[57] V. Som`a, P. Navr´atil, F. Raimondi, C. Barbieri,
and
T. Duguet, “Novel chiral Hamiltonian and observables
in light and medium-mass nuclei,” Phys. Rev. C 101,
014318 (2020), arXiv:1907.09790 [nucl-th].
[58] R. F. Garcia Ruiz et al., “Unexpectedly large charge radii
of neutron-rich calcium isotopes,” Nature Phys. 12, 594
(2016), arXiv:1602.07906 [nucl-ex].
[59] ´A. Koszor´us et al., “Charge radii of exotic potassium iso-
topes challenge nuclear theory and the magic character
of N = 32,” Nature Phys. 17, 439–443 (2021), [Erratum:
Nature Phys. 17, 539 (2021)], arXiv:2012.01864 [nucl-ex].
[60] R. L. Workman and Others (Particle Data Group), “Re-
view of Particle Physics,” PTEP 2022, 083C01 (2022).
