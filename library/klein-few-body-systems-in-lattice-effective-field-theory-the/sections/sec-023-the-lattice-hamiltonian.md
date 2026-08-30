---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-023-the-lattice-hamiltonian
section_title: "The lattice Hamiltonian"
section_number: null
pages: 46-49
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
To set the stage and to introduce our notations, we ﬁrst discuss the free Hamiltonian. Its discretized form
reads
Hfree = 1
2mN
∑
⃗n,i, j
∑
ˆl
2ω0a†
i, j
(⃗n) ai, j
(⃗n) +
3∑
k=1
(−1)k
× ωk
[
a†
i, j
(⃗n) ai, j
(
⃗n + kˆl
)
+ a†
i, j
(⃗n) ai, j
(
⃗n− kˆl
)]}
.
(4.1)
Here, ai, j, a†
i, j are the fermionic annihilation and creation operators with spin and isospin indices i, j,
respectively, mN = (mp + mn)/2 denotes the nucleon mass and ˆl is a unit vector in spatial direction. The
summation is over all lattice points⃗n on the L3 lattice. We use a stretchedO(am)-improved action and its
coeﬃcientsωk are summarized in Tab. 4.1, see e.g. Refs. [109, 110]. m indicates the number of hopping
points beyond next-neighbor interaction used in the Laplacian discretization in each spatial direction
and we use m = 4 throughout this chapter. The stretching factor N is introduced to minimize the errors
arising from the discretized dispersion relations on the lattice especially for large momenta where the
discretization does not approximate the continuum relation E = ⃗p 2/(2mN) anymore. While there is some
arbitrariness on the exact choice of N depending on the values of the respective momentum, N = 3.5 is a
sensible choice.
O(a4) O(a2)
ω0 N· 1
9 + 49
36 o0 0
ω1 N· 1
6 + 3
2 o1
4
3
ω2 N· 1
15 + 3
20 o2
1
6
ω3 N· 1
90 + 1
90 o3 0
Table 4.1: The ωi are the coeﬃcients for the lattice discretization of the Laplacian and the dispersion relation
whereas the oi appear in the momentum components of the one-pion-exchange potential. Both depend on the
stretching factor N.
40
4.2 The lattice Hamiltonian
The interaction potential consists of two/three terms in the pionless/pionful theory at lowest order. The
contact interaction consists of two terms which can be chosen as
Hcont = 1
2
∑
⃗n
Cρa†,a (⃗n)ρa†,a (⃗n) + CI
∑
I
ρa†,a
I
(⃗n)ρa†,a
I
(⃗n)
 , (4.2)
where the terms are summed over all lattice sites ⃗n and the isospin index I = 1, 2, 3. These terms
appear in both versions of the EFT considered here. In the pionful theory, one has in addition the
one-pion-exchange potential
HOPE =− g2
A
8F2
π
∑
S 1,S 2,I
∑
⃗n1,⃗n2
GS 1S 2
(⃗n1−⃗n2
)ρa†,a
S 1,I
(⃗n1
)ρa†,a
S 2,I
(⃗n2
) , (4.3)
withgA the axial-vector coupling constant and Fπ the pion decay constant. S 1, S 2 are the respective spin
indices which run from 1 to 3. The corresponding lattice density operators read
ρa†,a (⃗n) = a†
i, j
(⃗n) ai, j
(⃗n), (4.4)
ρa†,a
I
(⃗n) = a†
i, j
(⃗n)τI, j j′ai, j
(⃗n), (4.5)
ρa†,a
S,I
(⃗n) = a†
i, j
(⃗n)σS,ii′τI, j j′ai, j
(⃗n), (4.6)
and GS 1S 2(⃗n) represents the pion propagator times the pion-nucleon vertex and is deﬁned as
GS 1S 2
(⃗n) = 1
L3
∑
⃗p
exp(−i⃗p·⃗n)ν
(
pS 1
)
ν
(
pS 2
)
1 + 2
qπ
3∑
k=1
∑
l
(−1)kωk cos(kp l
)
(4.7)
with qπ = M2
π + 6ω0.ν(pS 1),ν(pS 2) are the discretized momentum components of the ﬁrst and second
pion ﬁeld which yields ν(pl) = o1 sin(pl)− o2 sin(2pl) = pl(1 +O(p4
l )) with the coeﬃcients summarized
in Tab. 4.1. We only use an O(a2) discretization, because we do not want to expand the respective
interaction too much. A further improved momentum approximation is linked to a further expanded
derivative in position space including more interactions at distinct lattice points and the locality of the
pion-nucleon interaction is lost. These momenta arise from the pion ﬁeld derivative in the pion nucleon
LagrangianLπN =−gA/(2Fπ)N†⃗τ· (⃗σ·⃗∇ )⃗πN. To arrive at Eq. (4.7), we note that the pion propagator is
derived from the discrete action for instantaneous pions which takes the form [32]
Sππ
(πI
) =

m2
π
2 + 3ω0

∑
⃗n
πI
(⃗n)πI
(⃗n) +
∑
⃗n,ˆl,k
(−1)kωkπI
(⃗n)πI
(
⃗n + kˆl
)
. (4.8)
This is reparametrized byπ′
I(⃗n ) =√qππI(⃗n ). Finally, the new pion action reads
Sππ
(
π′
I
)
= 1
2
∑
⃗n
π′
I
(⃗n)π′
I
(⃗n) + 1
qπ
∑
⃗n,ˆl,k
(−1)kωkπ′ (⃗n)π′
I
(
⃗n + kˆl
)
(4.9)
41
Chapter 4 Regularization Methods for Nuclear Lattice E ﬀective Field Theory
and the respective pion propagator reads
Dπ
(⃗p) =
1 + 2
qπ
3∑
k=1
∑
l
(−1)k cos(kp l
)

−1
. (4.10)
Furthermore, we introduce a Gaussian smearing
f (⃗p) = 1
f0
exp
[
−b ˜ν(⃗p)
2
]
(4.11)
with a stretchedO(a4) improved discretization
˜ν(⃗p) = 2
3∑
k=0
3∑
l=1
(−1)kωk cos(kp l) = ⃗p 2 [
1 +O
(
p6)]
, (4.12)
where the error estimation is valid for N = 0 and the coeﬃcients given in Tab. 4.1. f0 is necessary
for normalization reasons and is given by f0 = (1/L3)∑
⃗p exp[−b˜ν(⃗p )/2]. This smearing modiﬁes the
contact interaction in momentum space according to
Hcont = 1
2
∑
⃗p
f (⃗p)
Cρa†,a (⃗p)ρa†,a (⃗p) + CI
∑
I
ρa†,a
I
(⃗p)ρa†,a
I
(⃗p)
 . (4.13)
Such a smearing was introduced in Ref. [32] to reduce the eﬀect of high momentum contributions and
remove the clustering instability of the contact interaction. As the leading order (LO) contribution is
iterated to all orders, such a smearing sums up some of the higher order corrections. All other higher
order corrections are then treated in perturbation theory (as long as the lattice spacing is su ﬃciently
large). Here, we concentrate on the lowest order and leave the discussion of the treatment of the higher
order eﬀects to Chap. 5. In any case, the smearing of the LO contact terms is a useful tool to improve the
description of the S-waves in a very eﬃcient way without including all higher-order terms in a chiral
counting scheme. In general, it is not necessary that the smeared contact interactions for the 1S 0- and
3S 1-channel have the same smearing function, f (⃗p). However, this is important for auxiliary-ﬁeld Monte
Carlo lattice simulations. Without the same smearing function for the two channels, the Monte Carlo
simulation would have a far bigger problem with sign oscillations. For this reason we consider only one
smearing function for both channels. The fact that we can approximately describe the eﬀective ranges for
both channels using only one smearing function can be viewed as a feature of the approximate SU(4)
Wigner symmetry of the two-nucleon interaction.
In continuum chiral EFT it is necessary to regularize the one-pion-exchange potential due to its
singularity at very small distances. We will show that such a singularity also appears for small lattice
spacings and we will regularize it in position space as suggested in Ref. [22]
˜f (⃗r) =
1− exp
−⃗r 2
2b


n
, (4.14)
where the denominator is motivated byFq{exp[−r2/(2b)]}∝ exp(−bq2/2). Here, b is a ﬁtting parameter
while n is a free parameter.
In the following we study the two-nucleon system for diﬀerent lattice spacings. Therefore we use the
ﬁnite-volume formulas for the binding energy and the eﬀective range expansion given by Lüscher [84,
42
