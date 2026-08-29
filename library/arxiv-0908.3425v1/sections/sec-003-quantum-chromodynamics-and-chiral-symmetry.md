---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-003-quantum-chromodynamics-and-chiral-symmetry
section_title: "Quantum chromodynamics and chiral symmetry"
section_number: null
pages: 4-6
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
QCD is the gauge theory of the strong interactions [Gross and Wilczek, 1973], [Weinberg, 1973],
[Fritzsch et al., 1973] with color SU(3) as the underlying ga uge group. Historically, the color degree
of freedom was introduced into the quark model to account for the Pauli principle in the description of
baryons as three-quark states. The matter ﬁelds of QCD are th e so-called quarks which are spin-1/2
fermions, with six diﬀerent ﬂavors ( u,d,s,c,b,t ) in addition to their three possible colors (see Table
2). Since quarks have not been observed as asymptotically fr ee states, the meaning of quark masses
and their numerical values are tightly connected with the me thod by which they are extracted from
hadronic properties (see Ref. [Manohar and Sachrajda, 2008 ] for a thorough discussion).
2.1.1 The QCD Lagrangian
The QCD Lagrangian can be obtained from the Lagrangian for fr ee quarks by applying the gauge
principle with respect to the group SU(3) of all unitary, uni modular, 3 × 3 matrices. Denoting the
quark ﬁeld components by qf,A,α, where f = 1, · · ·, 6 refers to the ﬂavor index, A = 1, 2, 3 to the color
index, and α = 1, · · ·, 4 to the Dirac spinor index, respectively, the “free” quark L agrangian without
interaction may be regarded as the sum of 6 × 3 = 18 free fermion Lagrangians:
Lfree quarks =
6∑
f =1
3∑
A=1
4∑
α,α′=1
¯qf,A,α(γµ
αα′i∂µ −mfδαα′)qf,A,α′. (1)
4
Flavor u d s
Charge [e] 2/3 −1/3 −1/3
Mass [MeV] 1.5 − 3.3 3.5 − 6.0 70 − 130
Flavor c b t
Charge [e] 2/3 −1/3 2/3
Mass [GeV] 1.27+0.07
−0.11 4.20+0.17
−0.07 171.2 ± 2.1
Table 2: Quark ﬂavors and their charges and masses. See [Mano har and Sachrajda, 2008] for details.
Suppressing the Dirac spinor index and introducing for each quark ﬂavor f a color triplet
qf =



qf,1
qf,2
qf,3


, (2)
the gauge principle is applied with respect to the group SU(3 ), i.e., all qf are subject to the same local
SU(3) transformation:
qf ↦→q′
f = exp
(
−i
8∑
a=1
Θ a
λc
a
2
)
qf =Uq f, (3)
where the eightλc
a denote Gell-Mann matrices acting in color space and the Θ a are smooth, real functions
in Minkowski space. Whenever convenient, we will make use of the summation convention implying a
summation over repeated indices. Introducing eight gauge p otentials Aaµ, transforming as
Aµ ≡ A aµ
λc
a
2 ↦→ A′
µ =UAµU † + i
g3
∂µUU †, (4)
the covariant derivative of the quark ﬁeld, by construction , transforms as the quark ﬁeld:
Dµqf ≡ (∂µ +ig3Aµ)qf ↦→(Dµqf )′ =D′
µq′
f =UD µqf. (5)
In Eq. (5), g3 denotes the strong coupling constant. In order to treat the g auge potentials as dynamical
degrees of freedom, one deﬁnes a generalization of the ﬁeld s trength tensor to the non-Abelian case as
Gaµν =∂µAaν −∂νAaµ −g3fabcAbµAcν, (6)
where, suppressing the superscript c in the Gell-Mann matrices, the standard totally antisymmet ric
SU(3) structure constants are given by (see Table 3)
fabc = 1
4iTr([λa,λ b]λc). (7)
Given Eq. (4), the ﬁeld strength tensor transforms under SU( 3) as
Gµν ≡ G aµν
λc
a
2 ↦→UGµνU †. (8)
The QCD Lagrangian obtained by applying the gauge principle to the free Lagrangian of Eq. (1), ﬁnally,
reads
LQCD =
∑
f = u,d,s,
c,b,t
¯qf (iD /−mf )qf − 1
4 GaµνGµν
a . (9)
5
abc 123 147 156 246 257 345 367 458 678
fabc 1 1
2 − 1
2
1
2
1
2
1
2 − 1
2
1
2
√
3 1
2
√
3
Table 3: Totally antisymmetric non-vanishing structure co nstants of SU(3): [ λa
2, λb
2 ] = ifabc
λc
2 .
From the point of view of gauge invariance the strong-intera ction Lagrangian could also involve a
term of the type
Lθ = g2
3 ¯θ
64π2ǫµνρσ Gµν
a Gρσ
a , ǫ 0123 = 1, (10)
where ǫµνρσ denotes the totally antisymmetric Levi-Civita tensor. The so-called θ term of Eq. (10)
implies an explicit P andCP violation of the strong interactions which, for example, wo uld give rise to
an electric dipole moment of the neutron. The present empiri cal information indicates that the θ term
is small and, in the following, we will omit Eq. (10) from our d iscussion.
