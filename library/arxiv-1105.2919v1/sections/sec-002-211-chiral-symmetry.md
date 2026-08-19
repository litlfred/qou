---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral effective field theory and nuclear forces"
section_id: sec-002-211-chiral-symmetry
section_title: "Chiral symmetry"
section_number: 2.1.1
pages: 7-9
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
doc_brief: "Chiral effective field theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The QCD Lagrangian reads
LQCD = ¯q(iγµDµ−M )q− 1
4Gµν,aGµν
a (2.1)
7
with the gauge-covariant derivative
Dµ =∂µ−igλa
2Aµ,a (2.2)
and the gluon ﬁeld strength tensor 2
Gµν,a =∂µAν,a−∂νAµ,a +gfabcAµ,bAν,c. (2.3)
In the above, q denotes the quark ﬁelds and M the quark mass matrix. Further, g is the strong coupling
constant and Aµ,a are the gluon ﬁelds. The λa are the Gell-Mann matrices and the fabc the structure
constants of theSU (3)color Lie algebra (a,b,c = 1,..., 8); summation over repeated indices is always implied.
The gluon-gluon term in the last equation arises from the non-Abelian nature of the gauge theory and is
the reason for the peculiar features of the color force.
The masses of the up (u), down (d), and strange (s) quarks are [115]:
mu = 2 .5± 0.8 MeV, (2.4)
md = 5 ± 0.9 MeV, (2.5)
ms = 101 ± 25 MeV. (2.6)
These masses are small as compared to a typical hadronic scale, i.e., a scale of low-mass hadrons which are
not Goldstone bosons, e.g., mρ = 0.78 GeV≈ 1 GeV.
It is therefore of interest to discuss the QCD Lagrangian in the limit of vanishing quark masses:
L0
QCD = ¯qiγµDµq− 1
4Gµν,aGµν
a . (2.7)
Deﬁning right- and left-handed quark ﬁelds,
qR =PRq, q L =PLq, (2.8)
with
PR = 1
2(1 +γ5), P L = 1
2(1−γ5), (2.9)
we can rewrite the Lagrangian as follows:
L0
QCD = ¯qRiγµDµqR + ¯qLiγµDµqL− 1
4Gµν,aGµν
a . (2.10)
Restricting ourselves now to up and down quarks, we see that L0
QCD is invariant under the global unitary
transformations
qR =
( uR
dR
)
↦−→gRqR = exp
(
−iΘR
i
τi
2
)( uR
dR
)
(2.11)
and
qL =
( uL
dL
)
↦−→gLqL = exp
(
−iΘL
i
τi
2
)( uL
dL
)
, (2.12)
where τi (i = 1, 2, 3) are the generators of SU (2)ﬂavor, the usual Pauli spin matrices with commutation
relations [τi
2,τj
2
]
=iϵijkτk
2 , (2.13)
andgR andgL are elements of SU (2)R andSU (2)L, respectively. In conclusion: The right- and left-handed
components of massless quarks do not mix. This is SU (2)R×SU (2)L symmetry, also known as chiral
symmetry. Noether’s Theorem implies the existence of six conserved currents; three right-handed currents
Rµ
i = ¯qRγµτi
2qR with ∂µRµ
i = 0 (2.14)
2ForSU (N) group indices, we use Latin letters, ...,a,b,c,...,i,j,k,... , and, in general, do not distinguish between sub-
scripts and superscripts.
8
and three left-handed currents
Lµ
i = ¯qLγµτi
2qL with ∂µLµ
i = 0. (2.15)
It is useful to consider the following linear combinations; namely, three vector currents
Vµ
i =Rµ
i +Lµ
i = ¯qγµτi
2q with ∂µVµ
i = 0 (2.16)
and three axial-vector currents
Aµ
i =Rµ
i−Lµ
i = ¯qγµγ5
τi
2q with ∂µAµ
i = 0, (2.17)
which got their names from the fact that they transform under parity as vector and axial-vector current
densities, respectively. The vector transformations are given by
q =
( u
d
)
↦−→exp
(
−iΘV
i
τi
2
)( u
d
)
, (2.18)
which are isospin rotations and, therefore, invariance under vector transformations can be identiﬁed with
isospin symmetry.
There are six conserved charges,
QR
i =
∫
d3xR 0
i =
∫
d3xq†
R(t,⃗ x)τi
2qR(t,⃗ x) with dQR
i
dt = 0 (2.19)
and
QL
i =
∫
d3xL 0
i =
∫
d3xq†
L(t,⃗ x)τi
2qL(t,⃗ x) with dQL
i
dt = 0, (2.20)
or, alternatively,
QV
i =
∫
d3xV 0
i =
∫
d3xq†(t,⃗ x)τi
2q(t,⃗ x) with dQV
i
dt = 0 (2.21)
and
QA
i =
∫
d3xA 0
i =
∫
d3xq†(t,⃗ x)γ5
τi
2q(t,⃗ x) with dQA
i
dt = 0. (2.22)
The QL
i and QR
i satisfy the commutation relations of the Lie algebra of SU (2)R×SU (2)L (chiral algebra),
[
QR
i ,QR
j
]
=iϵijkQR
k,
[
QL
i,QL
j
]
=iϵijkQL
k,
[
QR
i ,QL
j
]
= 0. (2.23)
ForQV
i and QA
i , the commutation relations read,
[
QV
i ,QV
j
]
=iϵijkQV
k,
[
QA
i ,QA
j
]
=iϵijkQV
k,
[
QV
i ,QA
j
]
=iϵijkQA
k . (2.24)
For reasons of completeness, we mention that massless u and d quarks satisfy an even larger symmetry
group, namely, SU (2)R×SU (2)L×U(1)V ×U(1)A. While the U(1)V symmetry corresponds to quark
number conservation, theU(1)A is broken on the quantum level (“U(1)A anomaly”) and is not a symmetry
of the system.
