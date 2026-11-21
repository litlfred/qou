---
doc_id: lattice2021-543
doc_title: "The neutron-proton mass diﬀerence"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 2-4
source_pdf: LATTICE2021_543.pdf
source_sha256: 3a255daa50ebd5a4
toc_source: outline
doc_brief: "The neutron-proton mass difference — 9 sections: Front matter; QCD+QED at LO; Introduction"
---
Introduction
Today many lattice QCD calculations have reached the 푂(1%) precision level [1], requiring to
include the Isospin Breaking (IB) Eﬀects. The leading terms of the latter come from the ∼푂(1%)
corrections of 푂( ˆ훼EM) (QED) and 푂( ˆ푚푑−ˆ푚푢
ΛQCD ) (strong IB or QCD). These can be taken into account
simulating 푢and 푑quarks with diﬀerent masses and including QED in the action [2, 3]. However,
a convenient approach consists in expanding the path integral with respect to the isospin symmetry
breaking parameters. In this setup, any observable in the full theory (QCD+QED) is the sum of
its isosymmetric part and the IBEs. This philosophy is the heart of the RM123 method [4–6] used
in the present work. For a given observable, the slopes with respect to the IB couplings are found
using the isosymmetric gauge conﬁgurations, and the IB correction at Leading Order (LO) is a
linear combination of these slopes with the appropriate charge factors and counterterms. In this
work the eﬀect of IB on the hadronic spectum is investigated with focus on 푀푛−푀푝, the mass
diﬀerence between neutron and proton. We also deﬁne a scheme for the separation of strong IB
and QED contributions. Though conventional, this separation provides physical intuition about the
sizes of the two eﬀects.
We use a mixed action approach in the tmQCD regularization over the 푁푓= 2 + 1 + 1 ETMC
gauge conﬁgurations [7]. In QCD+QED we adopt the electroquenched approximation and neglect
QCD disconnected diagrams. A purely hadronic renormalization scheme is adopted, using the
masses of 휋s, 퐾s and Ω−as normalization parameters to set the scale, tune the counterterms and
reach the physical point.
The results found in this work are the following. We obtain 푀푛−푀푝= 1.73(69) MeV ,
(푀푛−푀푝)QED = −1.16(25) MeV and (푀푛−푀푝)QCD = 3.10(59) MeV . We also get a predic-
tion for the masses of nucleons, 푀푛= 0.961(20) GeV , 푀푝= 0.959(20) GeV and for the 휋푁
sigma term 휎휋푁= 43.2(1.4) MeV . The uncertainties are only statistical and obtained using the
jackknife resampling technique.
The paper is organized as follows. In sec. (2) we brieﬂy recap the main features of the RM123
method and set our notation for the IBEs. In sec. (3) we discuss the tuning of counterterms and give
our prescription for the separation between strong IB and QED. In sec. (4) and (5) we respectively
give the details of the simulations and of the analysis for the above observables. Finally in sec. (6)
we give our summary and outlooks.
2.
QCD+QED at LO
In the continuum, the QCD+QED Lagrangian L can be written as:
L = L0 −Δ푚푢푑¯푞휏3푞+ 푒퐴휇¯푞훾휇Q푞
.
(1)
The ﬁrst term, L0, is symmetric under 푆푈(2)퐼(isoQCD theory) and chargeless under 푈(1)EM,
while the rest are isospin breaking terms. We write 푚푢= 푚푢푑−Δ푚푢푑, 푚푑= 푚푢푑+ Δ푚푢푑. and
denote the up-down doublet with 푞= (푢, 푑)푇. 휏3 is the third Pauli matrix and Q = 휏3
2 + 1
6 . At LO in
IB we expand the path integral in 푒2 and Δ푚푢푑(including 푂(푒2) counterterms for the divergences
of QED diagrams [8]). The ﬁne structure constant ˆ훼EM renormalizes at higher orders with respect
to our expansion, and we can safely use the value 훼EM = 푒2/(4휋) = 1/137.035999084 from [9].
2
PoS(LATTICE2021)543
푀푛−푀푝in Lattice QCD+QED at LO in IB
Simone Romiti
On the lattice we use a mixed action approach as in [6]. This leads to the presence of counterterms
for both the physical and critical masses, whose tuning is discussed in sec. (3). The LIBE in a
generic hadronic mass can then be written as:
Δ푀퐻=

푒2 ¯ΔEM +
Õ
푓
푎Δ푚푐푟
푓¯ΔC
푓+
Õ
푓
푎Δ푚푓¯ΔM
푓

푀퐻
,
(2)
where the ¯ΔEM and ¯Δ푥
푓(푥= C, M) (for a ﬂavor 푓) representthe slopes induced bythe coupling in front
of them. Note that at the order we are working, these can be evaluated in the isosymmetric theory.
The slopes can be found individually from the corresponding corrections ¯Δ푥in those euclidean
correlators whose isoQCD ground state has mass 푀(0)
퐻. In fact for large times 퐶퐻(푡) ∼푒−푀퐻푡, and
it’s easy to show that the mass slope’s eﬀective curve is given by:
¯Δ푥푀퐻= −휕푡
"
¯Δ푥퐶퐻(푡)
퐶(0)
퐻(푡)
#
,
(3)
where 휕푡푓(푡) = 푓(푡+ 1) −푓(푡) (in lattice units). At ﬁnite time extent this formula is valid in
absence of backward signals, i.e. for baryonic correlators with deﬁnite parity [10, 11]. In mesonic
correlators however each forward signal is paired with a backward one, and the above formula gets
slightly modiﬁed [6]. In this work we extract the mass slopes from a ﬁt to a constant of these
eﬀective curves in their plateau intervals. In (2.1) are shown the expressions of the mass corrections
in terms of Feynman diagrams.
We conclude this section saying that QED is introduced in a non-compact way [2], i.e. gener-
ating the photon ﬁeld 퐴휇instead on the gauge link variables 퐸( 푓)
휇
= exp(푖푞푓퐴휇)), and regularizing
the infrared divergence in the photon propagator using the QEDL prescription [12], i.e. removing
the ®푘= 0 mode. QED on a torus 푇× 퐿3 introduces Finite Volume Eﬀects (FVEs) in the hadronic
spectrum, with polynomial behavior in 1/퐿[3, 13–15], and the QED mass correction of an hadron
obeys the following asymptotic formula:
Δ푀(푇, 퐿)
푇,퐿→∞
−−−−−−→Δ푀(∞) −푄2훼EM

휅
2푀퐿

1 +
2
푀퐿

+ 푂
훼EM
퐿3

.
(4)
휅≈2.837297, 푄is the charge of the hadron in units of 푒and the 푀in the denominators can be
set equal to 푀(∞) at this order in 훼EM. The terms ∼1/퐿and 1/퐿2 are universal, namely depend
only on the electric charge and mass of the hadron, with spin and structure-dependent terms starting
only at higher orders. At ﬁxed ensemble, we use this property to remove these universal FVEs from
the mass corrections caused by the combination of diagrams coming from the interaction with the
electromagnetic ﬁeld (EM).
3
PoS(LATTICE2021)543
푀푛−푀푝in Lattice QCD+QED at LO in IB
Simone Romiti
