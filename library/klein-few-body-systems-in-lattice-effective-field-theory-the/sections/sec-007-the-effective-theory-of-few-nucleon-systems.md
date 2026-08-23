---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-007-the-effective-theory-of-few-nucleon-systems
section_title: "The effective theory of few-nucleon systems"
section_number: null
pages: 15-19
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
In this section we construct the most general Lagrangian of the same symmetry properties as the
underlying theory, QCD, focusing on the nucleon-nucleon interaction. We summarize the Lagrangian for
nucleons and pions up to N2LO in the power counting framework. Afterward we will use this Lagrangian
to construct all nucleon-nucleon interactions up to N2LO [39]. In the following we restrict ourselves
to the SU(2) case, where only u- and d-quarks exist while all other quarks are integrated out. Then the
symmetry of QCD in the chiral limit is
SU(2)L× SU(2)R× U(1)V, (2.1)
where the subscript denotes left-handed and right-handed transformations in the SU(2) sector while only
vector transformations are allowed in the U(1) sector. The Lagrangian should be invariant under such a
symmetry even though the ground state of the theory should be invariant only under SU(2)V× U(1)V
due to spontaneous symmetry breaking. Note that any continuous symmetry transformation leaving the
Lagrangian invariant is linked to a conserved current. While a classical analysis results in a conserved
current also for axial transformations in the U(1) sector, quantum corrections cancel the conservation and
give rise to anomalies [40–42].
Before turning to the nucleon-nucleon interaction, we review the general ideas of ChPT in the meson
sector. A possible realization is the so-called non-linear realization, where the pion ﬁelds ⃗π are organized
in an exponential expression,
U = exp
( i⃗π·⃗τ
F0
)
. (2.2)
Here,⃗τ are the isospin Pauli matrices and U has the transformation behaviour under chiral symmetry,
U→ RUL†, (2.3)
where R and L are SU(2) matrices. The chiral symmetry breaking quark masses are implemented as well,
and we treat their respective chiral symmetry transformation as if it is a spurion ﬁeld building block,
M =
(mu 0
0 md
)
, M→ RML†. (2.4)
9
Chapter 2 Theory
The leading-order Lagrangian in the pion sector reads
L(0)
π = F2
0
4 Tr
(
DµUDµU†)
+ F2
0 B0
2 Tr
(
MU† + M†U
)
, (2.5)
whereas B0 is proportional to the quark condensate⟨¯qq⟩. The covariant derivative is constructed such
that the Lagrangian is locally invariant. However, neglecting external currents, it is given byDµ =∂µ in
the meson sector. By expanding Eq. (2.5) and assuming the isospin limit mu = md = ˆm, we can identify
the pion mass term,
M2
π = 2B0 ˆm. (2.6)
In the pion-nucleon sector, the relativistic Lagrangian at LO reads
L(0) = Ψ†
(
i/D− m0 + gA
2 γµγ5uµ
)
Ψ, (2.7)
with m0 the nucleon mass in the chiral limit, gA the pion-nucleon coupling constant also in the chiral
limit and the covariant derivatives without external currents,
Dµ =∂µ + 1
2
(
u†∂µu + u∂µu†)
, (2.8)
with u2 = U and uµ the so-called chiral vielbein uµ = i(u†∂µu− u∂µu†). The nucleons are summarized in
Ψ = (p, n)T . Beside the leading-order Lagrangian, one needs the next-to-leading-order one as well, and
in its relativistic formulation it reads [43],
L(1) = c1Tr(χ+
) Ψ†Ψ + c3
2 Tr
(
uµuµ
)(
Ψ†Ψ
)
− c4
4 Ψ†γµγν [
uµ, uν
]
Ψ +... . (2.9)
χ+ contains the quark masses and it readsχ†
+ = u†χu† + uχ†u withχ = 2B0M. The low-energy coupling
constants c1, c3 and c4 can be determined from pion-nucleon scattering observables like phase shifts or
cross sections [44, 45]. Nowadays, the best method to pin down the LECs is the dispersive approach
using Roy-Steiner equations [46]. Note that there are seven independent terms, but we only show the
terms necessary in our analyses.
Including quantum corrections in the form of Feynman loop diagrams in baryon ChPT would lead
to an inconsistent power counting scheme. This can be solved by the HBChPT approach or the EOMS
renormalization scheme. As the nucleon-nucleon interaction is highly non-relativistic, one can use the
former one. This is done by splitting the nucleon spinor into a heavy component and a light component.
Finally, one can use only the light component in the Lagrangian. Details on this method and its application
to pion-nucleon Lagrangians can be found in [15, 47].
Starting point for the nucleon-nucleon interaction is Weinberg’s Lagrangian in its chiral expansion for
nucleon ﬁelds Ψ and pion ﬁelds⃗π at LO, NLO and N2LO. Subsequently, we give the Lagrangian in its
non-relativistic form, as we concentrate on the nucleon-nucleon interaction,
L(0) =1
2∂µ⃗π∂µ⃗π− 1
2 M2
π⃗π 2 + Ψ†
i∂0 +⃗σ

gA√
2Fπ
(
⃗σ·⃗∇
)(⃗τ·⃗π)
− 1
F2
π
⃗τ·
(
⃗π× ˙⃗π
) Ψ
− 1
2CS
(
Ψ†Ψ
)(
Ψ†Ψ
)
− 1
2CT
(
Ψ†⃗σ Ψ
)
·
(
Ψ†⃗σ Ψ
)
− 1
2CU
(
Ψ†⃗τ Ψ
)
·
(
Ψ†⃗τ Ψ
)
(2.10)
− 1
2CV
(
Ψ†⃗σ⃗τ Ψ
)
··
(
Ψ†⃗σ⃗τ Ψ
)
+... ,
10
2.1 The e ﬀective theory of few-nucleon systems
L(1) =Ψ†
4c1M2
π− 2c1
F2
π
M2
π⃗π 2 + c2
F2
π
˙⃗π 2 + c3
F2
π
∂µ⃗π·∂µ⃗π− c4
2F2
π
ϵi jkϵabcσiτa
(
∇ jπb
)(∇kπc
)
 Ψ
− D
4Fπ
(
Ψ†Ψ
)(
Ψ†⃗σ⃗τ Ψ
)
·⃗∇⃗π− E
2
(
ΨΨ†)(
Ψ⃗τ Ψ†)
·
(
Ψ⃗τ Ψ†)
+... , (2.11)
L(2) =Ψ†

⃗∇ 2
2mΨ
 +... . (2.12)
⃗σ are the Pauli matrices in the spin space,gA is the pion-nucleon coupling constant and m, Mπ are the
nucleon and pion masses in the isospin limit. The superscript denotes the counting in the Weinberg power
counting scheme.
For the counting of any interaction we have to incorporate the vertices, propagators and loops in the
right way. Weinberg’s power counting formula reads
ν =−4 + 2N + 2L +
∑
i
Vi∆i, ∆i = di + 1
2 ni− 2. (2.13)
ν represents the power of (Q/Λ) whereas N is the number of nucleons and L is the number of pion
loops. Additionally, the number of vertices of type i are given by Vi. ∆i can be calculated from the
number of nucleon operators ni and the number of pion masses/ derivatives, di. ∆i is always equal or
larger than zero and there is only a ﬁnite number of diagrams at each orderν. This enables Weinberg’s
statement on eﬀective theories, which can be solved order-by-order with a ﬁnite number of potential
terms. LO calculations take into account all diagrams with ν = 0, while NLO and N2LO calculations use
all diagrams up toν = 2 andν = 4. Note that we have only included NLO corrections to pion-nucleon
interaction in Eq. (2.11). Short-range corrections were included later by various groups, e.g. [48–51].
The free part of the nucleon Lagrangian is of order 2, which is just an artifact of the non-relativistic
approach and it will be included at leading order [14]. Then the free leading-order nucleon Lagrangian
reads
Lfree
N = Ψ†
i∂0 +
⃗∇2
2m
 Ψ (2.14)
From Eq. (2.10) we derive the pion propagator,
Sπ = 1
⃗q 2 + M2
π + iϵ
, (2.15)
and Eq. (2.14) gives the non-relativistic nucleon propagator,
S N = 1
E0− ⃗q 2
2m + iϵ
. (2.16)
With this in mind we can construct all respective potential terms up to N2LO as shown in Fig. 2.1. In
Fig. 2.1 all possible terms are shown but not all terms contribute necessarily to the potential at given order.
For example, the next-to-leading-order contributions to the three-body force vanish as they do not produce
any new topology or cancel each other. Details can be found in [52]. Using unitary transformations [51],
the leading order potential reads
V(0) =− g2
A
4F2
π
⃗σ1·⃗q⃗σ2·⃗q
⃗q 2 + M2
π
⃗τ1·⃗τ2 + CS + CT⃗σ1·⃗σ2 + CU⃗τ1·⃗τ2 + CV⃗σ1·⃗σ2⃗τ1·⃗τ2. (2.17)
11
Chapter 2 Theory
Figure 2.1: Chiral expansion of two-and three-body forces up to N2LO. Solid dots, ﬁlled circles and squares denote
vertices with ∆i = 0, 1 and 2 according to Eq. (2.13). Figure taken from [52].
Here, ⃗q is the momentum transfer ⃗q = ⃗p− ⃗p′ with the relative incoming and outgoing momenta,
⃗p (′) = (⃗p (′)
1 −⃗p (′)
2 )/2. The index 1, 2 stands for the respective particle. Due to the antisymmetry condition
of fermions, one can reduce the number of terms in Eq. (2.17) to two. Popular choices are the terms
proportional to CS and CT , or CS and CU. At NLO, we have a loop contribution from the two-pion
exchange potential (TPEP),
V(1)
TPEP =− ⃗τ1·⃗τ2
384π2F4
π
L (q)
M2
π
(
5g4
A− 4g2
A− 1
)
+⃗q 2 (
24g4
A− 10g2
A− 1
)
+ 48g4
AM4
π
4M2
π +⃗q 2

− 3g4
A
64π2F4
π
L (q)
(
⃗σ1·⃗q⃗σ2·⃗q−⃗σ1·⃗σ2⃗q 2)
,
(2.18)
where q =|⃗q| and L(q) is a loop function which normally depends on a momentum cutoﬀ ˜Λ. Alternatively,
if combined with dimensional regularization, one can use the following inﬁnite cutoﬀ expression,
L(q) = lim
˜Λ→∞
θ
( ˜Λ− 2Mπ
) ω
2q log
˜Λ2ω2 + q2s2 + 2 ˜Λωs
4M2
π
( ˜Λ + q2)
=
√
4M2
π + q2
2q log
√
4M2
π + q2 + q
√
4M2
π + q2− q
=
√
4M2
π + q2
q log
√
4M2
π + q2 + q
2Mπ
,
(2.19)
withω =
√
4M2
π + q2 and s =
√
˜Λ− 4M2
π.
Beside the TPEP, short-range interactions appear and there are 14 terms which fulﬁll the symmetry
12
