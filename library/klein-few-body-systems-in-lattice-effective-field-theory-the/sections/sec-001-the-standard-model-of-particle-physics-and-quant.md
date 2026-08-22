---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-001-the-standard-model-of-particle-physics-and-quant
section_title: "The standard model of particle physics and quantum chromodynamics"
section_number: null
pages: 7-8
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
chromodynamics
The standard model of particle physics consists of the fundamental particles and the fundamental forces.
The particles are quarks on the one hand and leptons on the other hand. The quarks consist of (u)p,
(d)own, (s)trange, (c)harm, (b)ottom and (t)op quarks and they interact via gluons. Besides, the leptons
consist of electron, muon and tau as well as electron neutrino, muon neutrino and tau neutrino. Leptons
and quarks interact via the photon (electromagnetic force), the W±-, Z-boson (weak force), or the Higgs
boson. From a gauge theory perspective, the standard model can be described as a
SU(3)C× SU(2)L× U(1)Y (1.1)
gauge theory, where SU(3)C is the color gauge invariance in the strong sector, and SU(2)L× U(1)Y is the
gauge group of the electroweak sector, which uniﬁes the weak force [SU(2)L], and the electromagnetic
force [U(1)Y] via the Higgs mechanism. In this thesis we do concentrate on quantum chromodynamics
(QCD), the theory describing the strong force and being the SU(3)C part of Eq. (1.1).
The QCD Lagrangian reads
LQCD =
3∑
A=1
6∑
f =1
4∑
α,α′=1
¯qα, f,A
(
γµ
α,α′iDµ− m fδα,α′
)
qα′, f,A +Lgluon, (1.2)
where f is the ﬂavor index for the six spin-half quarks, α is the Dirac spinor index, and A is the color
index. The above written Lagrangian is globally invariant under SU(3) color gauge transformations. The
theory is made locally invariant under gauge transformations by the introduction of gauge ﬁelds Aa
µ and
the covariant derivative,
∂µ→ Dµ =∂µ− igλa
2 Aa
µ, (1.3)
whereλa are the SU(3) Gell-Mann matrices. The kinetic gluon term is
Lgluon =−1
4Ga
µνGµν
a , (1.4)
with the gluon ﬁeld strength tensor Ga
µν = ∂µAa
ν−∂νAa
µ +g f abcAb
µAc
ν. f abc are the SU(3) structure
constants. By comparison with abelian gauge theories like quantum electrodynamics, the non-abelian
1
Chapter 1 Introduction and Motivation
structure leads to phenomena like gluon self-interaction, quark conﬁnement and asymptotic freedom.
The strong coupling constant is deﬁned by αS =g2/(4π). In contrast to quantum electrodynamics, where
the coupling constant runs weakly and is small,αEM≈ 1/137, the coupling constantαS runs strongly
depending on the momentum scale of the system. Its theoretical and experimental values are shown in
Fig. 1.1.
0
0.2
0.4
0.6
0.8
1
10
-1
1 10
Q (GeV)
!g1(Q)/"
Bjorken sum rule constraint
AdS/QCD
!g1/" Hall A/CLAS
!g1/" JLab CLAS (2008)
!g1/" JLab CLAS (2014)
!g1(#)/" OPAL
!F3/"
!g1/" DESY HERMES
!g1/" CERN COMPASS
!g1/" SLAC E142/E143
!g1/" SLAC E154/E155
!g1/" JLab RSS
!g1/" CERN SMC
GDH limit
Figure 1.1: Running coupling constant for the strong forceαS . Figure taken from [1].
Although QCD can be solved perturbatively for Q> 1 GeV due to asymptotic freedom, this is not the
case in the low-energy region, whereαS≈ 1. This strong coupling is responsible for quark conﬁnement
