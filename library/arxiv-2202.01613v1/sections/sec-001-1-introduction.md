---
doc_id: arxiv-2202.01613v1
doc_title: "The neutron-proton mass diﬀerence"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 2202.01613v1.pdf
source_sha256: b8768b78fe84c86a
toc_source: outline
doc_brief: "The neutron-proton mass difference — 9 sections: Front matter; QCD+QED at LO; Introduction"
---
Introduction
Today many lattice QCD calculations have reached the 𝑂(1%) precision level [1], requiring to
include the Isospin Breaking (IB) Eﬀects. The leading terms of the latter come from the ∼𝑂(1%)
corrections of 𝑂( ˆ𝛼𝐸𝑀) (QED) and 𝑂( ˆ𝑚𝑑−ˆ𝑚𝑢
Λ𝑄𝐶𝐷) (strong IB or QCD). These can be taken into account
simulating 𝑢and 𝑑quarks with diﬀerent masses and including QED in the action [2, 3]. However,
a convenient approach consists in expanding the path integral with respect to the isospin symmetry
breaking parameters. In this setup, any observable in the full theory (QCD+QED) is the sum of
its isosymmetric part and the IBEs. This philosophy is the heart of the RM123 method [4–6] used
in the present work. For a given observable, the slopes with respect to the IB couplings are found
using the isosymmetric gauge conﬁgurations, and the IB correction at Leading Order (LO) is a
linear combination of these slopes with the appropriate charge factors and counterterms. In this
work the eﬀect of IB on the hadronic spectum is investigated with focus on 𝑀𝑛−𝑀𝑝, the mass
diﬀerence between neutron and proton. We also deﬁne a scheme for the separation of strong IB
and QED contributions. Though conventional, this separation provides physical intuition about the
sizes of the two eﬀects.
We use a mixed action approach in the tmQCD regularization over the 𝑁𝑓= 2 + 1 + 1 ETMC
gauge conﬁgurations [7]. In QCD+QED we adopt the electroquenched approximation and neglect
QCD disconnected diagrams. A purely hadronic renormalization scheme is adopted, using the
masses of 𝜋s, 𝐾s and Ω−as normalization parameters to set the scale, tune the counterterms and
reach the physical point.
The results found in this work are the following. We obtain 𝑀𝑛−𝑀𝑝= 1.73(69) MeV ,
(𝑀𝑛−𝑀𝑝)(𝑄𝐸𝐷) = −1.16(25) MeV and (𝑀𝑛−𝑀𝑝)(𝑄𝐶𝐷) = 3.10(59) MeV . We also get a
prediction for the masses of nucleons, 𝑀𝑛= 0.961(20) GeV , 𝑀𝑝= 0.959(20) GeV and for the
𝜋𝑁sigma term 𝜎𝜋𝑁= 43.2(1.4) MeV . The uncertainties are only statistical and obtained using
the jackknife resampling technique.
The paper is organized as follows. In sec. (2) we brieﬂy recap the main features of the RM123
method and set our notation for the IBEs. In sec. (3) we discuss the tuning of counterterms and give
our prescription for the separation between strong IB and QED. In sec. (4) and (5) we respectively
give the details of the simulations and of the analysis for the above observables. Finally in sec. (6)
we give our summary and outlooks.
2.
QCD+QED at LO
In the continuum, the QCD+QED Lagrangian L can be written as:
L = L0 −Δ𝑚𝑢𝑑¯𝑞𝜏3𝑞+ 𝑒𝐴𝜇¯𝑞𝛾𝜇Q𝑞
.
(1)
The ﬁrst term, L0, is symmetric under 𝑆𝑈(2)𝐼(isoQCD theory) and chargeless under 𝑈(1)𝐸𝑀,
while the rest are isospin breaking terms. We write 𝑚𝑢= 𝑚𝑢𝑑−Δ𝑚𝑢𝑑, 𝑚𝑑= 𝑚𝑢𝑑+ Δ𝑚𝑢𝑑. and
denote the up-down doublet with 𝑞= (𝑢, 𝑑)𝑇. 𝜏3 is the third Pauli matrix and Q = 𝜏3
2 + 1
6 . At LO in
IB we expand the path integral in 𝑒2 and Δ𝑚𝑢𝑑(including 𝑂(𝑒2) counterterms for the divergences
of QED diagrams [8]). The ﬁne structure constant ˆ𝛼𝐸𝑀renormalizes at higher orders with respect
to our expansion, and we can safely use the value 𝛼𝐸𝑀= 𝑒2/(4𝜋) = 1/137.035999084 from [9].
2
𝑀𝑛−𝑀𝑝in Lattice QCD+QED at LO in IB
Simone Romiti
On the lattice we use a mixed action approach as in [6]. This leads to the presence of counterterms
for both the physical and critical masses, whose tuning is discussed in sec. (3). The LIBE in a
generic hadronic mass can then be written as:
Δ𝑀𝐻=

𝑒2 ¯ΔEM +
∑︁
𝑓
𝑎Δ𝑚𝑐𝑟
𝑓¯ΔC
𝑓+
∑︁
𝑓
𝑎Δ𝑚𝑓¯ΔM
𝑓

𝑀𝐻
,
(2)
where the ¯ΔEM and ¯Δ𝑥
𝑓(𝑥= C, M) (for a ﬂavor 𝑓) representthe slopes induced bythe coupling in front
of them. Note that at the order we are working, these can be evaluated in the isosymmetric theory.
The slopes can be found individually from the corresponding corrections ¯Δ𝑥in those euclidean
correlators whose isoQCD ground state has mass 𝑀(0)
𝐻. In fact for large times 𝐶𝐻(𝑡) ∼𝑒−𝑀𝐻𝑡, and
it’s easy to show that the mass slope’s eﬀective curve is given by:
¯Δ𝑥𝑀𝐻= −𝜕𝑡
"
¯Δ𝑥𝐶𝐻(𝑡)
𝐶(0)
𝐻(𝑡)
#
,
(3)
where 𝜕𝑡𝑓(𝑡) = 𝑓(𝑡+ 1) −𝑓(𝑡) (in lattice units). At ﬁnite time extent this formula is valid in
absence of backward signals, i.e. for baryonic correlators with deﬁnite parity [10, 11]. In mesonic
correlators however each forward signal is paired with a backward one, and the above formula gets
slightly modiﬁed [6]. In this work we extract the mass slopes from a ﬁt to a constant of these
eﬀective curves in their plateau intervals. In (2.1) are shown the expressions of the mass corrections
in terms of Feynman diagrams.
We conclude this section saying that QED is introduced in a non-compact way [2], i.e. gener-
ating the photon ﬁeld 𝐴𝜇instead on the gauge link variables 𝐸( 𝑓)
𝜇
= exp(𝑖𝑞𝑓𝐴𝜇)), and regularizing
the infrared divergence in the photon propagator using the QEDL prescription [12], i.e. removing
the ®𝑘= 0 mode. QED on a torus 𝑇× 𝐿3 introduces Finite Volume Eﬀects (FVEs) in the hadronic
spectrum, with polynomial behavior in 1/𝐿[3, 13–15], and the QED mass correction of an hadron
obeys the following asymptotic formula:
Δ𝑀(𝑇, 𝐿)
𝑇,𝐿→∞
−−−−−−→Δ𝑀(∞) −𝑄2𝛼𝐸𝑀

𝜅
2𝑀𝐿

1 +
2
𝑀𝐿

+ 𝑂
𝛼𝐸𝑀
𝐿3

.
(4)
𝜅≈2.837297, 𝑄is the charge of the hadron in units of 𝑒and the 𝑀in the denominators can be
set equal to 𝑀(∞) at this order in 𝛼𝐸𝑀. The terms ∼1/𝐿and 1/𝐿2 are universal, namely depend
only on the electric charge and mass of the hadron, with spin and structure-dependent terms starting
only at higher orders. At ﬁxed ensemble, we use this property to remove these universal FVEs from
the mass corrections caused by the combination of diagrams coming from the interaction with the
electromagnetic ﬁeld (EM).
3
𝑀𝑛−𝑀𝑝in Lattice QCD+QED at LO in IB
Simone Romiti
