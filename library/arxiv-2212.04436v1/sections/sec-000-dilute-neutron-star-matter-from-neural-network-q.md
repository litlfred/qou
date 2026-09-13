---
doc_id: arxiv-2212.04436v1
doc_title: "Dilute neutron star matter from neural-network quantum states"
section_id: sec-000-dilute-neutron-star-matter-from-neural-network-q
section_title: "Dilute neutron star matter from neural-network quantum states"
section_number: null
pages: 1-6
source_pdf: 2212.04436v1.pdf
source_sha256: 0f98a851d030ec05
doc_brief: "Dilute neutron star matter from neural-network quantum states — 1 sections: Dilute neutron star matter from ne"
---
Bryce Fore,1 Jane M. Kim, 2 Giuseppe Carleo, 3 Morten Hjorth-Jensen, 2, 4 and Alessandro Lovato 5, 6, 7
1Physics Division, Argonne National Laboratory, Argonne, IL 60439, USA
2Department of Physics and Astronomy and Facility for Rare Isotope Beams,
Michigan State University, East Lansing, MI 48824, USA
3Institute of Physics, ´Ecole Polytechnique F´ ed´ erale de Lausanne (EPFL), CH-1015 Lausanne, Switzerland
4Department of Physics and Center for Computing in Science Education, University of Oslo, N-0316 Oslo, Norway
5Physics Division, Argonne National Laboratory, Argonne, IL 60439
6Computational Science Division, Argonne National Laboratory, Argonne, IL 60439
7INFN-TIFPA Trento Institute of Fundamental Physics and Applications, 38123 Trento, Italy
(Dated: December 9, 2022)
Low-density neutron matter is characterized by fascinating emergent quantum phenomena, such
as the formation of Cooper pairs and the onset of superﬂuidity. We model this density regime
by capitalizing on the expressivity of the hidden-nucleon neural-network quantum states combined
with variational Monte Carlo and stochastic reconﬁguration techniques. Our approach is competitive
with the auxiliary-ﬁeld diﬀusion Monte Carlo method at a fraction of the computational cost. Using
a leading-order pionless eﬀective ﬁeld theory Hamiltonian, we compute the energy per particle of
inﬁnite neutron matter and compare it with those obtained from highly realistic interactions. In
addition, a comparison between the spin-singlet and triplet two-body distribution functions indicates
the emergence pairing in the 1S0 channel.
Introduction. Multi-messenger astronomy has opened
new windows into the state of matter at densities and
isospin asymmetries that cannot be directly probed
by terrestrial experiments [1–4]. Concurrently, nuclear
many-body theory has made considerable progress in
computing the nucleonic-matter equation of state at den-
sities corresponding to the inner core of neutron stars
starting from realistic Hamiltonians [5–10]. Comparisons
between theoretical predictions and astrophysical obser-
vation pose stringent constraints on models of nuclear
dynamics, particularly three-nucleon forces [11].
In this work, we focus on lower densities, ρ ≲ 0.04
fm−3, which are relevant to the phenomenology of the
stellar inner crust and outer core. In this region, both
conditions for superﬂuidity — strong Fermi degeneracy
and an attractive interaction between neutron pairs in
the 1S0 channel — are believed to be met [12–14]. In
addition to lowering the system’s energy, the formation of
Cooper pairs plays a critical role in neutrino emission [15,
16], and the phenomenology of glitches [17]. Pairing is
also relevant in modeling neutron-rich nuclei, which are
the subject of intense experimental activities [18].
Quantum Monte Carlo approaches [19], and in partic-
ular the auxiliary-ﬁeld diﬀusion Monte Carlo (AFDMC)
method [20] have been extensively applied to accurately
compute neutron-matter properties [6, 7, 21]. In the low-
density regime, AFDMC calculations have convincingly
shown a depletion of the superﬂuid gap with respect to
the Bardeen–Cooper–Schrieﬀer theory [22, 23]. However,
because of the fermion sign problem, AFDMC predic-
tions depend upon the starting variational wave function.
For instance, the superﬂuid phase must be assumeda pri-
ori by using pfaﬃan wave functions [24].
Neural-network quantum states [25] (NQS) have
gained popularity in solving the Schr¨ odinger equation
of atomic nuclei both in real space [26–30] and in the
occupation-number formalism [31]. In this work, we in-
troduce a periodic NQS suitable to model both the nor-
mal and superﬂuid phases of neutron matter. The ansatz
is based on the “hidden-nucleon” architecture, which can
model the ground-state wave functions of nuclei up to
16O with high accuracy [29]. Inspired by chemistry ap-
plications [32, 33], we further improve the expressivity
of the hidden-nucleon NQS using generalized backﬂow
correlations, which generalize both the pfaﬃan and the
spin-dependent backﬂow of Ref. [34].
Our model of nuclear dynamics is the leading-order
pionless eﬀective ﬁeld theory ( /πEFT) Hamiltonian of
Ref. [35], which qualitatively reproduces the binding en-
ergies of nuclei with up to A = 90 nucleons. Arguments
based on the expansion around the unitary limit [36],
and Brueckner-Hartree-Fock calculations of inﬁnite nu-
clear matter [37], indicate that /πEFT should provide ac-
curate energies of dilute neutron matter. We test this
hypothesis by comparing the /πEFT energy per particle
against the sophisticated Argonne v18 [38] plus Urbana
IX [39] (AV18+UIX) Hamiltonian used in the Akmal-
Pandharipande-Ravenhall (APR) [40] equation of state.
To better quantify the role of dynamical correlations,
we evaluate the two-body spatial distribution functions,
separating the spin-triplet and spin-singlet channels. We
analyze the self-emergence of pairing correlations, not
explicitly included in the NQS ansatz, as a function of
neutron-matter density.
Method. We model the interactions among neutrons
through the leading-order /πEFT Hamiltonian “o” of
Ref. [35]. The two-body contact potential is designed to
reproduce the np scattering lengths and eﬀective ranges
in the S/T = 0/1 and 1/0 channels. Thus, it yields a
neutron-neutron scattering length of ann = −22.5 fm,
arXiv:2212.04436v1  [nucl-th]  8 Dec 2022
2
slightly larger than the experimental value of −18.9(4)
fm, see [41] and references therein, while the eﬀective
range is well reproduced. The Hamiltonian also contains
a repulsive three-body force that ensures the stability of
nuclei.
We approximate the ground-state solution of the nu-
clear many-body problem with an NQS ansatz that be-
longs to the hidden-fermion family [42], recently general-
ized to continuum Hilbert spaces and applied to atomic
nuclei in Ref. [29]. In addition to the visible spatial and
spin coordinates of the A neutrons, R ={r1... rA} and
S ={sz
1...s z
A}, the Hilbert space contains ﬁctitious Ah
hidden-nucleon degrees of freedom. In this work we use
Ah = A = 14 so that the system is as ﬂexible as possi-
ble, but in practice we have also found using as few as
8 hidden nucleons gives very similar results. The wave
function can be conveniently expressed in a block matrix
form as
ΨHN (R,S )≡ det
[φv(R,S ) φv(Rh,S h)
χh(R,S ) χh(Rh,S h)
]
. (1)
As in Ref. [29], φv(R,S ) is the A×A matrix represent-
ing visible single-particle orbitals computed on the visible
coordinates while the Ah×Ah matrix χh(Rh,S h) yields
the amplitudes of hidden orbitals evaluated on the co-
ordinates of the Ah hidden nucleons. Finally, χh(R,S )
and φv(Rh,S h) are Ah×A and A×Ah matrices giving
the amplitudes of hidden orbitals on visible coordinates
and visible orbitals on hidden coordinates, respectively.
All the above matrices are expressed in terms of deep
neural networks with diﬀerentiable activation functions
— see Ref. [29] for additional details. To respect the
Pauli principle, the coordinates of the hidden nucleons
must be permutation-invariant functions of the visible
ones. We enforce this symmetry by using a Deep-Sets
architecture [43, 44] with logsumexp pooling.
Inspired by the success of quantum-chemistry NQS [32,
33], we augment the ﬂexibility of the ansatz by perform-
ing a generalized backﬂow transformation to the visible
coordinates entering the upper-left block of the hidden-
nucleon matrix: φv(R,S )→φv( ˜R, ˜S). We use the Deep-
Sets architecture again to enforce fermion anti-symmetry
(˜ri, ˜sz
i ) =ρbf
(
ri,s z
i, log
(∑
j
exp(φbf(rj,s z
j)
))
. (2)
To further augment the expressivity, each visible single-
particle orbital uses its own ρbf andφbf neural networks.
We simulate inﬁnite neutron matter using 14 particles
in a box with periodic boundary conditions. Following
Ref. [45], the latter are imposed by mapping the spatial
coordinates onto periodic functions by
ri→
(
sin
(2πri
L
)
, cos
(2πri
L
))
(3)
which ensures the wave function is continuous and diﬀer-
entiable at the box boundary. Here L is the size of the
simulation periodic box, and the sin and cos functions
are applied element-wise to ri. Finite-size eﬀects due
to the tail corrections of two- and three-body potentials
are accounted for by summing the contributions given by
neighboring cells to the simulation box [46].
Evaluating the expectation values of quantum mechan-
ical operators, including the Hamiltonian, requires car-
rying out multi-dimensional integration over the spatial
and spin coordinates of the neutrons. To this aim, we
exploit Monte Carlo quadrature and sample R and S
from|ΨHN (R,S )|2 using the Metropolis-Hastings algo-
rithm [47] — additional details can be found in the sup-
plemental material of Ref. [27]. The best variational
parameters deﬁning the NQS are found by minimiz-
ing the system’s energy, which we carry out using the
R(oot)M(ean)S(quared)Prop(agation)-enhanced version
of the stochastic-reconﬁguration optimization method in-
troduced in Ref. [29].
Results and discussion. We ﬁrst benchmark the ex-
pressivity of the hidden-nucleon NQS for periodic sys-
tems by comparing the energy per particle of inﬁnite
neutron matter against “conventional” variational Monte
Carlo (VMC), and both constrained-path and AFDMC
results. The variational wave function used in state-of-
the-art neutron-matter studies, see for example [7, 21],
contains a spin-independent Jastrow factor that multi-
plies a Slater determinant augmented by spin-dependent
backﬂow correlations. The constrained-path approxi-
mation, commonly employed to alleviate the AFDMC
fermion-sign problem [19], brings about a bias in the
ground-state energy estimate [6, 21]. Exact results can be
obtained by performing unconstrained propagations, but
the statistical error grows exponentially with the imagi-
nary time.
0 1000 2000 3000 4000
Optimization Steps
6.4
6.5
6.6
6.7
6.8
6.9
7.0
Energy per Particle (MeV)
NQS
DMC (unconstrained)
DMC (constrained)
VMC
Hartree-Fock
FIG. 1. NQS training data in neutron matter at ρ = 0.04
fm−3 (data points) compared with Hartree-Fock (dotted line),
conventional VMC (dashed line), constrained-path ADMC
(dash-dotted line) and unconstrained-path ADMC results
(solid line).
3
0.010 0.015 0.020 0.025 0.030 0.035 0.040
Density (fm −3)
4
6
8
10
12
14Energy (MeV)
/πEFT
A V18+UIX
Fermi Gas
FIG. 2. Low-density neutron-matter /πEFT equation of state
as obtained with the hidden-nucleon NQS (solid green circles)
compared with FHNC/SOC calculations with the AV18+UIX
Hamiltonian (red triangles) and the non-interacting Fermi
Gas (solid blue line).
As shown in Fig. 1 for ρ = 0.04 fm −3, after ≃ 2000
stochastic-reconﬁguration steps, the NQS ansatz con-
verges to the virtually exact unconstrained AFDMC en-
ergy, using a fraction of its computing time: about
100 hours on NVIDIA-A100 GPUs vs approximately
1.2 million hours on Intel-KNL CPUs. Notice that the
constrained-path approximation violates the variational
principle. In contrast, variational Monte Carlo calcula-
tions based on the NQS never yield energies below that
of the Hamiltonian’s ground state. Comparing with the
Hartree-Fock approximation, it appears that the hidden-
nucleon ansatz captures the overwhelming majority of
the correlation energy.
In Fig. 2, we compare the/πEFT energies obtained with
the NQS ansatz against Fermi hypernetted chain/single-
operator chain calculations that take as input the so-
phisticated AV18+UIX Hamiltonian, consistent with the
celebrated APR equation of state [40]. For all densities
considered, /πEFT and AV18+UIX are in excellent agree-
ment, the maximum diﬀerence being always below 0 .30
MeV per particle — both of them provide energies much
below the non-interacting Fermi gas. These minor diﬀer-
ences are likely because model “o” yields a slightly larger
nn scattering length than the experimental value and,
therefore, more attraction in neutron matter. The latter
is not compensated for by the three-body force, whose
repulsive contribution is at most 0.25 MeV per neutron.
Once trained on the systems’ energy, the NQS
can be used to accurately evaluate a variety of
quantum-mechanical observables, such as the spin-singlet
and triplet two-body distribution functions deﬁned in
Ref. [48]. Figure 3 shows these distributions at ρ = 0.01
fm−3 (panel a) and ρ = 0.04 fm −3 (panel b). The sig-
niﬁcant increase in the spin-singlet channel compared to
the non-interacting Fermi Gas indicates that the NQS
wave function can capture the emergence of the 1S0
neutron pairing, despite not being explicitly encoded in
the ansatz. Consistent with the behavior of the pair-
ing gap [13, 22], the enhancement is more prominent at
ρ = 0.01 fm −3 than ρ = 0.04 fm −3. On the other hand,
at these densities, no pairing correlations are present in
the spin-triplet channel.
Conclusions – In this work, we have put forward an
NQS suitable to model the normal and superﬂuid phases
of inﬁnite neutron matter in a uniﬁed fashion. We im-
prove the expressivity of the hidden-nucleon ansatz of
Ref. [29] by adding state-dependent generalized back-
ﬂow correlations, whose inclusion has proven beneﬁcial
in condensed-matter applications [32, 33]. Periodic-box
boundary conditions are imposed by mapping the spatial
coordinates of the neutrons onto periodic functions.
Combined with Monte Carlo techniques to sample the
Hilbert space and the stochastic-reconﬁguration algo-
rithm to optimize the variational parameters, the NQS
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5
r [fm]
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
g(r)
(a)
Singlet Fermi Gas
Triplet Fermi Gas
Singlet NQS
Triplet NQS
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5
r [fm]
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
g(r)
(b)
Singlet Fermi Gas
Triplet Fermi Gas
Singlet NQS
Triplet NQS
FIG. 3. Spin-singlet and triplet two-body distribution func-
tions at ρ = 0.01 fm −3 (panel a) and ρ = 0.04 fm −3 (panel
b). The NQS calculations (solid symbols) are compared with
non-interacting Fermi Gas results.
4
yields energies per particle of low-density neutron mat-
ter that are in excellent agreement with unconstrained
AFDMC calculations at a fraction of the computa-
tional cost. In contrast, the computationally-inexpensive
AFDMC constrained-path approximation brings about
appreciable violations of the variational principle.
We have shown that /πEFT yields a low-density neu-
tron matter equation of state that is remarkably close to
the APR one [40]. This ﬁnding paves the way for more
systematic comparisons between dilute neutron matter
and Fermi gas around the unitary limit. In addition, it
enables studies of phenomena relevant to understand the
inner crust and the outer core of neutron stars, such as
pairing and superﬂuidity, using relatively simple models
of nuclear dynamics.
Finally, we have analyzed the possible onset of Cooper
pairing in the neutron medium. Speciﬁcally, the NQS
two-body distribution functions corresponding to pairs of
neutrons in the spin-singlet 1S0 channel exhibit a clear
enhancement at small inter-particle distances with re-
spect to the non-interacting case, which is absent in the
spin-triplet channel. Consistent with pairing-gap calcu-
lations [13, 22, 23], this behavior is more prominent at
smaller densities. Note that this feature has not been en-
coded in the NQS; rather, it is a self-emerging quantum
mechanical phenomenon.
As a future development, we plan on including more
sophisticated interactions, including highly-realistic phe-
nomenological ones such as AV18 + UIX and the local,
chiral-EFT potentials of Ref. [6, 21, 49]. The ﬂexibility of
the NQS ansatz will also be tested in isospin-asymmetric
nucleonic matter at low densities, where strong clustering
is expected to occur [50].
Acknowledgments. We thank R. Wiringa for provid-
ing us the AV18+UIX FHNC/SOC energies. We are
also grateful to O. Benhar, S. Gandolﬁ, A. Kievsky,
and M. Piarulli for many illuminating discussions. A.
L. and B.F. are supported by the U.S. Department of
Energy, Oﬃce of Science, Oﬃce of Nuclear Physics, un-
der contracts DE-AC02-06CH11357, the DOE Early Ca-
reer Award program, the NUCLEI SciDAC program, and
Argonne LDRD awards. J.M.K. and M.H.-J. are sup-
ported by the U.S. National Science Foundation Grants
No. PHY-1404159 and PHY-2013047. Numerical calcu-
lations were performed using resources of the Laboratory
Computing Resource Center at Argonne National Lab-
oratory, and the computers of the Argonne Leadership
Computing Facility via the ALCC grant “Short Range
Correlations from a Quantum Monte Carlo perspective.”
[1] B. P. Abbott et al. (LIGO Scientiﬁc Collaboration and
Virgo Collaboration), “GW170817: Observation of Grav-
itational Waves from a Binary Neutron Star Inspiral,”
Phys. Rev. Lett. 119, 161101 (2017), arXiv:1710.05832
[gr-qc].
[2] B. P. Abbott et al. (LIGO Scientiﬁc Collaboration and
Virgo Collaboration), “Multi-messenger Observations of
a Binary Neutron Star Merger,” Astrophys. J. 848, L12
(2017), arXiv:1710.05833 [astro-ph.HE].
[3] Andrea Sabatucci and Omar Benhar, “Tidal Deforma-
tion of Neutron Stars from Microscopic Models of Nu-
clear Dynamics,” Phys. Rev. C 101, 045807 (2020),
arXiv:2001.06294 [nucl-th].
[4] Peter Senger, “Probing dense nuclear matter in the labo-
ratory: Experiments at fair and nica,” Universe 7 (2021),
10.3390/universe7060171.
[5] C. Drischler, A. Carbone, K. Hebeler, and A. Schwenk,
“Neutron matter from chiral two- and three-nucleon cal-
culations up to N 3LO,” Phys. Rev. C 94, 054307 (2016),
arXiv:1608.05615 [nucl-th].
[6] M. Piarulli, I. Bombaci, D. Logoteta, A. Lovato, and
R. B. Wiringa, “Benchmark calculations of pure neu-
tron matter with realistic nucleon-nucleon interactions,”
Phys. Rev. C 101, 045801 (2020), arXiv:1908.04426
[nucl-th].
[7] D. Lonardoni, I. Tews, S. Gandolﬁ, and J. Carl-
son, “Nuclear and neutron-star matter from local chi-
ral interactions,” Phys. Rev. Res. 2, 022033 (2020),
arXiv:1912.09411 [nucl-th].
[8] W. G. Jiang, A. Ekstr¨ om, C. Forss´ en, G. Hagen, G. R.
Jansen, and T. Papenbrock, “Accurate bulk properties of
nuclei fromA = 2 to∞ from potentials with ∆ isobars,”
Phys. Rev. C 102, 054301 (2020), arXiv:2006.16774
[nucl-th].
[9] Francesca Sammarruca and Randy Millerson, “Overview
of symmetric nuclear matter properties from chiral inter-
actions up to fourth order of the chiral expansion,” Phys.
Rev. C 104, 064312 (2021), arXiv:2109.01985 [nucl-th].
[10] H. Heiselberg and M. Hjorth-Jensen, “Phases of dense
matter in neutron stars,” Phys. Rep. 328, 237 (2000).
[11] Andrea Sabatucci, Omar Benhar, Andrea Maselli, and
Costantino Pacilio, “Sensitivity of neutron star observa-
tions to three-nucleon forces,” Phys. Rev. D 106, 083010
(2022), arXiv:2206.11286 [astro-ph.HE].
[12] Armen Sedrakian, John W Clark, and
Mark Alford, Pairing in Fermionic Systems
(WORLD SCIENTIFIC, 2006)
https://www.worldscientiﬁc.com/doi/pdf/10.1142/6194.
[13] Omar Benhar and Giulia De Rosi, “Superﬂuid Gap
in Neutron Matter from a Microscopic Eﬀective In-
teraction,” J. Low Temp. Phys. 189, 250–261 (2017),
arXiv:1705.06607 [nucl-th].
[14] D. J. Dean and M. Hjorth-Jensen, “Pairing in nuclear
systems: from neutron stars to ﬁnite nuclei,” Rev. Mod.
Phys. 75, 607 (2003).
[15] Dima G. Yakovlev and C. J. Pethick, “Neutron star cool-
ing,” Ann. Rev. Astron. Astrophys. 42, 169–210 (2004),
arXiv:astro-ph/0402143.
[16] Dany Page, Madappa Prakash, James M. Lattimer, and
Andrew W. Steiner, “Rapid Cooling of the Neutron Star
in Cassiopeia A Triggered by Neutron Superﬂuidity in
Dense Matter,” Phys. Rev. Lett. 106, 081101 (2011),
arXiv:1011.6142 [astro-ph.HE].
[17] C. Monrozeau, J. Margueron, and N. Sandulescu,
“Nuclear superﬂuidity and cooling time of neutron-star
crust,” Phys. Rev. C 75, 065807 (2007), arXiv:nucl-
th/0703064.
5
[18] Fr´ ed´ eric Nowacki, Alexandre Obertelli, and Alfredo
Poves, “The neutron-rich edge of the nuclear landscape:
Experiment and theory.” Prog. Part. Nucl. Phys. 120,
103866 (2021), arXiv:2104.06238 [nucl-th].
[19] J. Carlson, S. Gandolﬁ, F. Pederiva, Steven C. Pieper,
R. Schiavilla, K. E. Schmidt, and R. B. Wiringa, “Quan-
tum Monte Carlo methods for nuclear physics,” Rev.
Mod. Phys. 87, 1067 (2015), arXiv:1412.3081 [nucl-th].
[20] K. E. Schmidt and S. Fantoni, “A quantum Monte Carlo
method for nucleon systems,” Phys. Lett. B 446, 99–103
(1999).
[21] A. Lovato, I. Bombaci, D. Logoteta, M. Piarulli,
and R. B. Wiringa, “Benchmark calculations of in-
ﬁnite neutron matter with realistic two- and three-
nucleon potentials,” Phys. Rev. C 105, 055808 (2022),
arXiv:2202.10293 [nucl-th].
[22] S. Gandolﬁ, A. Yu. Illarionov, S. Fantoni, F. Pederiva,
and K. E. Schmidt, “Equation of state of superﬂuid neu-
tron matter and the calculation of S(0)-1 pairing gap,”
Phys. Rev. Lett. 101, 132501 (2008), arXiv:0805.2513
[nucl-th].
[23] Stefano Gandolﬁ, Georgios Palkanoglou, Joseph Carlson,
Alexandros Gezerlis, and Kevin E. Schmidt, “The 1S0
Pairing Gap in Neutron Matter,” Condens. Mat. 7, 19
(2022), arXiv:2201.01308 [nucl-th].
[24] M. Bajdich, L. Mitas, G. Drobny, L. K. Wagner, and
K. E. Schmidt, “Pfaﬃan pairing wave functions in elec-
tronic structure quantum Monte Carlo,” Phys. Rev. Lett.
96, 130201 (2006), arXiv:cond-mat/0512327.
[25] Giuseppe Carleo and Matthias Troyer, “Solving the
quantum many-body problem with artiﬁcial neural net-
works,” Science 355, 602–606 (2017).
[26] J. W. T. Keeble and A. Rios, “Machine learning
the deuteron,” Phys. Lett. B 809, 135743 (2020),
arXiv:1911.13092 [nucl-th].
[27] Corey Adams, Giuseppe Carleo, Alessandro Lovato, and
Noemi Rocco, “Variational Monte Carlo Calculations
of A≤4 Nuclei with an Artiﬁcial Neural-Network Cor-
relator Ansatz,” Phys. Rev. Lett. 127, 022502 (2021),
arXiv:2007.14282 [nucl-th].
[28] Alex Gnech, Corey Adams, Nicholas Brawand, Giuseppe
Carleo, Alessandro Lovato, and Noemi Rocco, “Nuclei
with up to A = 6 nucleons with artiﬁcial neural net-
work wave functions,” Few Body Syst. 63, 7 (2022),
arXiv:2108.06836 [nucl-th].
[29] A. Lovato, C. Adams, G. Carleo, and N. Rocco, “Hidden-
nucleons neural-network quantum states for the nuclear
many-body problem,” (2022), arXiv:2206.10021 [nucl-
th].
[30] Y. L. Yang and P. W. Zhao, “A consistent descrip-
tion of the relativistic eﬀects and three-body interactions
in atomic nuclei,” Phys. Lett. B 835, 137587 (2022),
arXiv:2206.13208 [nucl-th].
[31] Mauro Rigo, Benjamin Hall, Morten Hjorth-Jensen,
Alessandro Lovato, and Francesco Pederiva, “Solving
the nuclear pairing model with neural network quantum
states,” (2022), arXiv:2211.04614 [nucl-th].
[32] Jan Hermann, Zeno Sch¨ atzle, and Frank No´ e, “Deep-
neural-network solution of the electronic Schr¨ odinger
equation,” Nature Chemistry 12, 891–897 (2020).
[33] David Pfau, James S. Spencer, Alexander G. D. G.
Matthews, and W. M. C. Foulkes, “Ab initio solution of
the many-electron Schr¨ odinger equation with deep neural
networks,” Physical Review Research 2, 033429 (2020),
arXiv:1909.02487 [physics.chem-ph].
[34] L. Brualla, S. Fantoni, A. Sarsa, K. E Schmidt, and S. A.
Vitiello, “Spin orbit induced backﬂow in neutron matter
with auxiliary ﬁeld diﬀusion Monte Carlo,” Phys. Rev. C
67, 065806 (2003), arXiv:nucl-th/0304042.
[35] R. Schiavilla, L. Girlanda, A. Gnech, A. Kievsky, A. Lo-
vato, L. E. Marcucci, M. Piarulli, and M. Viviani, “Two-
and three-nucleon contact interactions and ground-state
energies of light- and medium-mass nuclei,” Phys. Rev.
C 103, 054003 (2021), arXiv:2102.02327 [nucl-th].
[36] Sebastian K¨ onig, Harald W. Grießhammer, H. W. Ham-
mer, and U. van Kolck, “Nuclear Physics Around the
Unitarity Limit,” Phys. Rev. Lett. 118, 202501 (2017),
arXiv:1607.04623 [nucl-th].
[37] A. Kievsky, M. Viviani, D. Logoteta, I. Bombaci,
and L. Girlanda, “Correlations imposed by the unitary
limit between few-nucleon systems, nuclear matter and
neutron stars,” Phys. Rev. Lett. 121, 072701 (2018),
arXiv:1806.02636 [nucl-th].
[38] Robert B. Wiringa, V. G. J. Stoks, and R. Schiavilla,
“An Accurate nucleon-nucleon potential with charge in-
dependence breaking,” Phys. Rev. C 51, 38–51 (1995),
arXiv:nucl-th/9408016.
[39] B. S. Pudliner, V. R. Pandharipande, J. Carlson, and
Robert B. Wiringa, “Quantum Monte Carlo calculations
of A <= 6 nuclei,” Phys. Rev. Lett. 74, 4396–4399
(1995), arXiv:nucl-th/9502031.
[40] A. Akmal, V. R. Pandharipande, and D. G. Raven-
hall, “The Equation of state of nucleon matter and neu-
tron star structure,” Phys. Rev. C 58, 1804–1828 (1998),
arXiv:nucl-th/9804027.
[41] R. Machleidt and D.R. Entem, “Chiral eﬀective ﬁeld the-
ory and nuclear forces,” Phys. Rep. 503, 1 (2011).
[42] Javier Robledo Moreno, Giuseppe Carleo, Antoine
Georges, and James Stokes, “Fermionic wave functions
from neural-network constrained hidden states,” Pro-
ceedings of the National Academy of Sciences of the
United States of America 119, e2122059119 (2022).
[43] Manzil Zaheer, Satwik Kottur, Siamak Ravanbakhsh,
Barnabas Poczos, Ruslan Salakhutdinov, and Alexander
Smola, “Deep Sets,” arXiv e-prints , arXiv:1703.06114
(2017), arXiv:1703.06114 [cs.LG].
[44] Edward Wagstaﬀ, Fabian B. Fuchs, Martin Engelcke, In-
gmar Posner, and Michael Osborne, “On the Limita-
tions of Representing Functions on Sets,” arXiv e-prints
, arXiv:1901.09006 (2019), arXiv:1901.09006 [cs.LG].
[45] Gabriel Pescia, Jiequn Han, Alessandro Lovato, Jianfeng
Lu, and Giuseppe Carleo, “Neural-network quantum
states for periodic systems in continuous space,” Phys.
Rev. Res. 4, 023138 (2022), arXiv:2112.11957 [quant-ph].
[46] A. Sarsa, S. Fantoni, K. E. Schmidt, and F. Pederiva,
“Neutron matter at zero temperature with auxiliary ﬁeld
diﬀusion Monte Carlo,” Phys. Rev. C68, 024308 (2003),
arXiv:nucl-th/0303035 [nucl-th].
[47] Nicholas Metropolis, Arianna W. Rosenbluth, Mar-
shall N. Rosenbluth, Augusta H. Teller, and Edward
Teller, “Equation of State Calculations by Fast Comput-
ing Machines,” J. Chem. Phys. 21, 1087–1092 (1953).
[48] S. Gandolﬁ, A. Yu Illarionov, F. Pederiva, K. E. Schmidt,
and S. Fantoni, “Equation of state of low-density neutron
matter, and the 1s0 pairing gap,” Physical Review C -
Nuclear Physics 80, 045802 (2009).
[49] M. Piarulli et al., “Light-nuclei spectra from chi-
ral dynamics,” Phys. Rev. Lett. 120, 052503 (2018),
6
arXiv:1707.02883 [nucl-th]. [50] John W. Negele and D. Vautherin, “Neutron star mat-
ter at subnuclear densities,” Nucl. Phys. A 207, 298–320
(1973).
