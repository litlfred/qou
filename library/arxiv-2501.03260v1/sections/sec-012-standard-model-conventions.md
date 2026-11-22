---
doc_id: arxiv-2501.03260v1
doc_title: "Preons, Braid Topology, and Representations of Fundamental Particles"
section_id: sec-012-standard-model-conventions
section_title: "Standard Model Conventions"
section_number: null
pages: 27-32
source_pdf: 2501.03260v1.pdf
source_sha256: 510ae5435ae95664
toc_source: outline
doc_brief: "Preons, Braid Topology, and Representations of Fundamental Particles — In particle phenomenology, preon models study compositional rules of standard model interactions."
---
Standard Model Conventions
In this appendix, we review some well-established facts about SU(3)c × SU(2)L × U(1)Y
gauge theory, in order to establish the conventions used in the main text. This overview
can be found in standard texts such as [51].
SU(3)c × SU(2)L × U(1)Y gauge theory contains a spectrum of particles described
by quantum ﬁelds under the representations of SL(2, C) × SU(3) × SU(2) × U(1) once
including the spin degrees of freedom. By using the chiral representations of the Lorentz
group, the (p, q) representation of SL(2, C) has left-chiral spinors as (2, 1), vector ﬁelds
Group
SL(2, C)
SU(3)c
SU(2)L
Spin(3)F
Fundamental
α
i
a
I
Adjoint
[ab]
A
i
[IJ]
Table 3: Indices for various reprentations of Lie groups for spacetime and the standard
model. Note that α = 1, 2, a = 1, 2, i = 1, 2, 3, I = 1, 2, 3, and A = 1, . . . 8.
as (2, 2), and scalars as (1, 1). Note that technically, a Weyl spinor in D = 3 + 1 is
a complex spinor, which implies that the complex conjugate state is also included. In
other words, a left-chiral particle also contains degrees of freedom for the CPT-conjugate
right-chiral anti-particle (1, 2), which would always have opposite charges.
The standard model contains three generations of fermions, including the left-chiral
quarks qia, the left-chiral leptons la, and the left-chiral charge conjugate of the up quark
ui, down quark di, and electron e, generalized to three families. While the standard model
was deﬁned to have massless neutrinos, it is now understood that at least two generations
of neutrinos are massive. The status of right-chiral neutrinos is unknown. Since the braids
for right-chiral neutrinos are natural, we consider the possibility of right-chiral neutrinos
and will remain agnostic about the details of mass assignment to see if the helon model
provides any constraints or clues. The bosons include the 12 vector gauge bosons and
the electroweak Higgs ﬁeld, which lead to the gluons gA, the W-bosons W ±, the Z-boson
Z, and the photon A as gauge vector bosons and the Higgs ﬁeld H as a scalar below the
electroweak scale.
The interactions of the standard model can be described by Feynman diagrams, whose
interaction rules can be read oﬀfrom the action S or Lagrangian (density) L.
The
Lagrangian for the standard model can be broken into the following pieces,
LSM = Lgauge + Lfermion + LHiggs + HY ukawa.
(37)
The vector boson Lagrangian contains the SU(3) × SU(2) × U(1) gauge bosons,
Lgauge = −1
4tr (GµνGµν + WµνW µν + BµνBµν) ,
(38)
where the gluon ﬁeld strength Gµν, the weak ﬁeld strength Wµν, and the weak hypercharge
ﬁeld strength Bµν are matrix ﬁelds with respect to the SU(3), SU(2), and U(1) gauge
ﬁelds, respectively. The vector potentials are given by Gµ = GA
µT A
3 , Wµ = W i
µT i
2, and
Bµ,
Gµν = GA
µνT A = ∂µGν −∂νGµ + [Gµ, Gν],
(39)
Wµν = W i
µνT i = ∂µWν −∂νWµ + [Wµ, Wν],
(40)
Bµν = ∂µBν −∂νBµ.
(41)
Upon spontaneous symmetry breaking of SU(2)L × U(1)Y →U(1)em, the W 0- and B-
bosons get mixed to give the Z-boson and photon. The vacuum expectation value (vev)
of the electroweak Higgs relates to the Higgs mass. Weinberg’s mixing angle rotates the
W 0 and B bosons to the Z and γ bosons, which also relates to the diﬀerence of the mass
of the Z and W ± bosons. The gluons, W-bosons, and B-boson correspond to the following
representations of SU(3) × SU(2) × U(1): (8, 1)0 ⊕(1, 3)0 ⊕(1, 1)0. The Higgs ﬁeld is in
the (1, 2)1/2 representation.
The fermionic Lagrangian can be expressed either all as left-chiral ﬁelds or a mix of
left-chiral weak isospin doublets and right-chiral singlets. Complex conjugation allows
for the two to be related. Since the 16 spinor of Spin(10) GUT uniﬁes the ﬁrst gener-
ation of fermions with the right-chiral neutrino into a single representation (for a single
generation), it is customary to work with the all left-chiral formulation. The fermionic
Lagrangian is written (in terms of ﬂavor eigenstates)
Lfermion = iq†¯σµDµq + il†¯σµDµl + iu†¯σµDµu + id†¯σµDµd + ie†¯σµDµe + iν†¯σµDµν). (42)
The representations corresponding to these left-chiral ﬁelds describe the index structure
of the ﬁelds for the ﬁrst generation
q = qia
α : (3, 2)1/6,
l = la
α : (1, 2)−1/2,
u = ui
α : (3, 1)−2/3,
d = di
α : (3, 1)1/3,
e = eα : (1, 1)1,
ν = να : (1, 1)0.
(43)
where d as a left-chiral state is the charge conjugated right-chiral fermion.
The interactions of the fermions are encoded in the covariant derivatives, which are
given by
Dµq = (∂µ −ig3Gµ −ig2Wµ −iYqBµ) q,
(44)
Dµl = (∂µ −ig2Wµ −iYlBµ) l,
(45)
Dµu = (∂µ −ig3Gµ −iYuBµ) u,
(46)
Dµd = (∂µ −ig3Gµ −iYdBµ) d,
(47)
Dµe = (∂µ −iYeBµ) e,
(48)
Dµν = ∂µν.
(49)
Since the spinor equations of motion contain γµDµλ for diﬀerent spinors λ, the covariant
derivatives above encode the interactions between the fermions and gauge bosons. Section
5.2 focuses on testing these interactions in the helon model.
References
[1] S. Hossenfelder. Minimal length scale scenarios for quantum gravity. Living Reviews
in Relativity, 16(1):2, 2013.
[2] S. P. Kumar and M. B. Plenio. On quantum gravity tests with composite particles.
Nature Communications, 11(1):3900, 2020.
[3] A Lees. The electron in classical general relativity theory. The London, Edinburgh,
and Dublin Philosophical Magazine and Journal of Science, 28(189):385–395, 1939.
[4] P. A. M. Dirac. An extensible model of the electron. Proceedings of the Royal Society
of London. Series A. Mathematical and Physical Sciences, 268(1332):57–67, 1962.
[5] P. A. M. Dirac.
Particles of ﬁnite size in the gravitational ﬁeld.
Proceedings
of the Royal Society of London. Series A. Mathematical and Physical Sciences,
270(1342):354–356, 1962.
[6] P. A. M. Dirac. Quantised singularities in the electromagnetic ﬁeld. Proceedings of
the Royal Society of London. Series A, Containing Papers of a Mathematical and
Physical Character, 133(821):60–72, 1931.
[7] Jogesh C. Pati and Abdus Salam. Lepton Number as the Fourth Color. Phys. Rev.,
D10:275–289, 1974. [Erratum: Phys. Rev.D11,703(1975)].
[8] M. A. Shupe. A Composite Model of Leptons and Quarks. Phys. Lett. B, 86:87–92,
1979.
[9] Haim Harari. A Schematic Model of Quarks and Leptons. Phys. Lett. B, 86:83–86,
1979.
[10] Haim Harari and Nathan Seiberg. A Dynamical Theory for the Rishon Model.
Phys. Lett. B, 98:269–273, 1981.
[11] Risto Raitio. A Model of Lepton and Quark Structure. Phys. Scripta, 22:197, 1980.
[12] M. Lehto and R. Raitio. A Gauge Theory of Quark and Lepton Constituents. Phys.
Scripta, 25:239, 1982.
[13] H. Fritzsch and G. Mandelbaum. Weak Interactions as Manifestations of the Sub-
structure of Leptons and Quarks. Phys. Lett. B, 102:319–322, 1981.
[14] Itzhak Bars. Theoretical and Phenomenological Constraints on Preons, Models and
Supergroups. Nucl. Phys. B, 208:77–121, 1982.
[15] Piotr Zenczykowski. The Harari-Shupe preon model and nonrelativistic quantum
phase space. Phys. Lett. B, 660:567–572, 2008.
[16] Risto Raitio. Supersymmetric Preons and the Standard Model. Nucl. Phys. B,
931:283–290, 2018.
[17] J. Lambek. Four-vector representation of fundamental particles. Int. J. Theor.
Phys., 39:2253–2258, 2000.
[18] Sundance O. Bilson-Thompson. A Topological model of composite preons. 3 2005.
[19] Sundance O. Bilson-Thompson, Fotini Markopoulou, and Lee Smolin. Quantum
gravity and the standard model. Class. Quant. Grav., 24:3975–3994, 2007.
[20] Sundance Bilson-Thompson, Jonathan Hackett, Lou Kauﬀman, and Lee Smolin.
Particle Identiﬁcations from Symmetries of Braided Ribbon Network Invariants. 4
2008.
[21] Sundance Bilson-Thompson, Jonathan Hackett, and Louis H. Kauﬀman. Particle
Topology, Braids, and Braided Belts. J. Math. Phys., 50:113505, 2009.
[22] Sundance Bilson-Thompson, Jonathan Hackett, Louis Kauﬀman, and Yidun Wan.
Emergent Braided Matter of Quantum Geometry. SIGMA, 8:014, 2012.
[23] Sundance Bilson-Thompson. Braided topology and the emergence of matter. J.
Phys. Conf. Ser., 360:012056, 2012.
[24] B. Coecke and R. Duncan. Interacting quantum observables: categorical algebra
and diagrammatics. New Journal of Physics, 13(4):043016, 2011.
[25] J. Gorard, M. Namuduri, and X. D. Arsiwalla. Zx-calculus and extended hyper-
graph rewriting systems i: A multiway approach to categorical quantum informa-
tion theory. arXiv preprint arXiv:2010.02752, 2020.
[26] J. Gorard, M. Namuduri, and X. D. Arsiwalla. Zx-calculus and extended wolfram
model systems ii: fast diagrammatic reasoning with an application to quantum
circuit simpliﬁcation. arXiv preprint arXiv:2103.15820, 2021.
[27] S. Montangero and E. Montangero.
Introduction to tensor network methods.
Springer, 2018.
[28] C. Zapata-Carratalá and X. D. Arsiwalla. An invitation to higher arity science.
arXiv preprint arXiv:2201.09738, 2022.
[29] C. Zapata-Carratalã, M. Schich, T. Beynon, and X. D. Arsiwalla. Hypermatrix
algebra and irreducible arity in higher-order systems: Concepts and perspectives.
Advances in Complex Systems (ACS), 26(06):1–22, 2023.
[30] C. Zapata-Carratalá, X. D. Arsiwalla, and T. Beynon. Diagrammatic calculus and
generalized associativity for higher-arity tensor operations. Theoretical Computer
Science, 1020:114915, 2024.
[31] X. D. Arsiwalla. Homotopic foundations of wolfram models. Wolfram Community,
2020.
[32] X. D. Arsiwalla, J. Gorard, and H. Elshatlawy.
Homotopies in multiway
(non-deterministic) rewriting systems as n-fold categories.
arXiv preprint
arXiv:2105.10822, 2021.
[33] X. D. Arsiwalla, H. Elshatlawy, and D. Rickles. Pregeometry, formal language and
constructivist foundations of physics. arXiv preprint arXiv:2311.03973, 2023.
[34] D. Rickles, H. Elshatlawy, and X. D. Arsiwalla. Ruliology: Linking computation,
observers and physical law. arXiv preprint arXiv:2308.16068, 2023.
[35] X. D. Arsiwalla and J. Gorard. Pregeometric spaces from wolfram model rewriting
systems as homotopy types. International Journal of Theoretical Physics, 63(4):83,
2024.
[36] X. D. Arsiwalla, D. Chester, and L. H. Kauﬀman. On the operator origins of classi-
cal and quantum wave functions. Quantum Studies: Mathematics and Foundations,
11:193–215, 2024.
[37] D. Chester, X. D. Arsiwalla, L. H. Kauﬀman, M. Planat, and K. Irwin. Quantization
of a new canonical, covariant, and symplectic hamiltonian density.
Symmetry,
16(3):316, 2024.
[38] J. S. Carter, L. H. Kauﬀman, and M. Saito. Structures and diagrammatics of four
dimensional topological lattice ﬁeld theories. Advances in mathematics, 146(1):39–
100, 1999.
[39] M. Aganagic, A. Klemm, M. Marino, and C. Vafa. The topological vertex. Com-
munications in mathematical physics, 254:425–478, 2005.
[40] X. D. Arsiwalla, R. Boels, M. Marino, and A. Sinkovics.
Phase transitions in
q-deformed 2d yang-mills theory and topological strings.
Physical Review D,
73(2):026005, 2006.
[41] X. D. Arsiwalla. More rings to rule them all: fragmentation, 4d ↔5d and split-
spectral ﬂows. Journal of High Energy Physics, 2008(02):066, 2008.
[42] X. D. Arsiwalla. Entropy functions with 5d chern-simons terms. Journal of High
Energy Physics, 2009(09):059, 2009.
[43] X. D. Arsiwalla. Supersymmetric black holes as probes of quantum gravity. PhD
Thesis, University of Amsterdam, 2010.
[44] Nick Salter. Ropes, fractions, and moduli spaces. The Mathematical Intelligencer,
pages 1–8, 2024.
[45] Z. Bern, J.J.M. Carrasco, and Henrik Johansson. New Relations for Gauge-Theory
Amplitudes. Phys.Rev., D78:085011, 2008.
[46] C. Furey. Uniﬁed Theory of Ideals. Phys. Rev., D86:025024, 2012.
[47] C. Furey. Standard model physics from an algebra? PhD thesis, Waterloo U., 2016.
[48] N. Furey and M. J. Hughes. One generation of standard model Weyl representations
as a single copy of R⊗C⊗H⊗O. Phys. Lett. B, 827:136959, 2022.
[49] E. A. Ivanov and J. Niederle. Gauge Formulation of Gravitation Theories. 2. The
Special Conformal Case. Phys. Rev. D, 25:988, 1982.
[50] James E. Humphreys.
Introduction to Lie Algebras and Representation Theory,
volume 9 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1972.
[51] Steven Weinberg. The Quantum Theory of Fields, volume 2. Cambridge University
Press, 1995.
