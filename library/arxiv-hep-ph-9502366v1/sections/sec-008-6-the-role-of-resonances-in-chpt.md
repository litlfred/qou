---
doc_id: arxiv-hep-ph-9502366v1
doc_title: "Chiral Perturbation Theory"
section_id: sec-008-6-the-role-of-resonances-in-chpt
section_title: "The role of resonances in ChPT"
section_number: 6
pages: 21-25
source_pdf: 9502366v1.pdf
source_sha256: 56df064956ca03f8
toc_source: inferred
doc_brief: "Chiral Perturbation Theory — An introduction to the basic ideas and methods of Chiral Perturbation Theory is presented."
---
It seems rather natural to expect that the lowest-mass resonances, such as ρ
mesons, should have an important impact on the physics of the pseudoscalar bosons.
In particular, the low-energy singularities due to the exchange of those resonances
should generate sizeable contributions to the chiral couplings.
This can be easily
understood, making a Taylor expansion of the ρ propagator:
1
p2 −M 2ρ
= −1
M 2ρ

1 + p2
M 2ρ
+ . . .

,
(p2 < M 2
ρ).
(6.1)
Below the ρ-mass scale, the singularity associated with the pole of the resonance
propagator is replaced by the corresponding momentum expansion.
The exchange
of virtual ρ mesons should result in derivative Goldstone couplings proportional to
powers of 1/M 2
ρ.
A systematic analysis of the role of resonances in the ChPT Lagrangian has
been performed by Ecker et al (1989a) [see also Donoghue et al 1989]. One writes
ﬁrst a general chiral-invariant Lagrangian L(U, V, A, S, P), describing the couplings of
meson resonances of the type V (1−−), A(1++), S(0++) and P(0−+) to the Goldstone
bosons, at lowest-order in derivatives. The coupling constants of this Lagrangian are
phenomenologically extracted from physics at the resonance-mass scale. One has then
an eﬀective chiral theory deﬁned in the intermediate-energy region. The generating
functional (3.19) is given in this theory by the path-integral formula
exp {iZ} =
Z
DU(φ) DV DA DS DP exp

i
Z
d4x L(U, V, A, S, P)

.
(6.2)
The integration of the resonance ﬁelds results in a low-energy theory with only
Goldstone bosons, i.e. the usual ChPT Lagrangian. At lowest-order, this integration
can be explicitly performed by expanding around the classical solution for the
resonance ﬁelds.
The formal procedure to introduce higher-mass states in the chiral Lagrangian
was ﬁrst discussed by Coleman et al (1969) and Callan et al (1969). The wanted
ingredient for a non-linear representation of the chiral group is the compensating
SU(3)V transformation h(φ, g) which appears under the action of G on the coset
representative u(φ) [see equations (3.2) to (3.4)]:
u(φ)
G
−→gR u(φ) h†(φ, g) = h(φ, g) u(φ) g†
L .
(6.3)
In practice, we shall only be interested in resonances transforming as octets or
singlets under SU(3)V . Denoting the resonance multiplets generically by R =⃗λ⃗R/
√
2
(octet) and R1 (singlet), the non-linear realization of G is given by
R
G
−→h(φ, g) R h(φ, g)† ,
R1
G
−→R1 .
(6.4)
Since the action of G on the octet ﬁeld R is local, we are led to deﬁne a covariant
derivative
∇µR = ∂µR + [Γµ, R] ,
(6.5)
with
Γµ = 1
2

u†(∂µ −irµ)u + u(∂µ −iℓµ)u†	
(6.6)
ensuring the proper transformation
∇µR
G
−→h(φ, g) ∇µR h(φ, g)† .
(6.7)
Without external ﬁelds, Γµ is the usual natural connection on coset space.
To determine the resonance-exchange contributions to the eﬀective chiral
Lagrangian, we need the lowest-order couplings to the pseudoscalar Goldstones which
are linear in the resonance ﬁelds. It is useful to deﬁne objects transforming as SU(3)V
octets:
uµ ≡iu†DµUu† = u†
µ ,
χ± ≡u†χu† ± uχ†u ,
(6.8)
f µν
±
= uF µν
L u† ± u†F µν
R u .
Invoking P and C invariance, the relevant lowest-order Lagrangian can be written as
(Ecker et al 1989a)
LR =
X
R=V,A,S,P
{LKin(R) + L2(R)} ,
(6.9)
with kinetic terms⋆
LKin(R=V, A) = −1
2 ⟨∇λRλµ∇νRνµ −M 2
R
2 RµνRµν⟩−1
2 ∂λR1,λµ∂νRνµ
1 + M 2
R1
4
R1,µνRµν
1 ,
LKin(R=S, P) = 1
2 ⟨∇µR∇µR −M 2
RR2⟩+ 1
2∂µR1∂µR1 −M 2
R1
2
R2
1 ,
(6.10)
⋆
The vector and axial-vector mesons are described in terms of antisymmetric tensor ﬁelds Vµν and
Aµν (Gasser and Leutwyler 1984, Ecker et al 1989a) instead of the more familiar vector ﬁelds.
where MR, MR1 are the corresponding masses in the chiral limit. The interactions
L2(R) read
L2[V (1−−)] = FV
2
√
2 ⟨Vµνf µν
+ ⟩+ iGV
√
2 ⟨Vµνuµuν⟩,
(6.11)
L2[A(1++)] = FA
2
√
2 ⟨Aµνf µν
−⟩,
(6.12)
L2[S(0++)] = cd ⟨Suµuµ⟩+ cm ⟨Sχ+⟩+ ˜cd S1 ⟨uµuµ⟩+ ˜cm S1 ⟨χ+⟩, (6.13)
L2[P(0−+)] = idm ⟨Pχ−⟩+ i ˜dm P1⟨χ−⟩.
(6.14)
All coupling constants are real.
The octet ﬁelds are written in the usual matrix
notation
Vµν =⃗
λ
√
2⃗
Vµν =


1
√
2ρ0
µν +
1
√
6ω8,µν
ρ+
µν
K∗+
µν
ρ−
µν
−1
√
2ρ0
µν +
1
√
6ω8,µν
K∗0
µν
K∗−
µν
K
∗0
µν
−2
√
6ω8,µν

,
(6.15)
and similarly for the other octets. We observe that for V and A only octets can couple
whereas both octets and singlets appear for S and P (always to lowest order p2).
From the measured decay rates for ρ0 →e+e−and ρ →2π, one can determine the
vector couplings |FV | = 154 MeV and |GV | = 69 MeV. Since the pions are far from
being soft, chiral corrections to GV are expected to be important. We can estimate
the size of these corrections from the electromagnetic form factor of the pion, which
is known to be well-reproduced by vector-meson dominance (VMD):
F π±
V (t) ≈
M 2
ρ
M 2
ρ −t ,
(6.16)
i.e. ⟨r2⟩π±
V
≈6/M 2
ρ = 0.4 fm2, to be compared with the measured value ⟨r2⟩π±
V
=
0.439 ± 0.008 fm2.
The exchange of a ρ meson between the GV and FV vertices,
generates a contribution to the electromagnetic pion radius (Ecker et al 1989a):
⟨r2⟩π±
V
= 6FV GV /(f 2M 2
V ).
Taking, MV
= Mρ, the success of the na¨ıve VMD
formula (6.16) requires GV FV > 0 and |GV | ≈|f 2
π/FV | = 55 MeV. Including also
the contribution from chiral loops (Gasser and Leutwyler 1985), reduces this estimate
to |GV | = 53 MeV, which is the value we shall adopt. The axial parameters can be
ﬁxed using the old Weinberg (1967b) sum rules: F 2
A = F 2
V −f 2
π = (123 MeV)2 and
M 2
A = M 2
V F 2
V /F 2
A = (968 MeV)2.
V exchange generates contributions to L1, L2, L3, L9 and L10, while A exchange
only contributes to L10 (Ecker et al 1989a):
LV
1 = G2
V
8M 2
V
,
LV
2 = 2LV
1 ,
LV
3 = −6LV
1 ,
LV
9 = FV GV
2M 2
V
,
LV +A
10
= −F 2
V
4M 2
V
+ F 2
A
4M 2
A
.
(6.17)
The resulting values of the Li couplings (Ecker et al 1989a) are summarized in
table 2, which compares the diﬀerent resonance-exchange contributions with the
phenomenologically determined values of Lr
i(Mρ).
The results shown in the table
clearly establish a chiral version of vector (and axial-vector) meson dominance:
whenever they can contribute at all, V and A exchange seem to completely dominate
the relevant coupling constants.
Table 2. V , A, S, S1 and η1 contributions to the coupling constants Lr
i in units of
10−3. The last column shows the results obtained using the relations (6.19).
i
Lr
i (Mρ)
V
A
S
S1
η1
Total
Totalc)
1
0.4 ± 0.3
0.6
0
−0.2
0.2b)
0
0.6
0.9
2
1.4 ± 0.3
1.2
0
0
0
0
1.2
1.8
3
−3.5 ± 1.1
−3.6
0
0.6
0
0
−3.0
−4.9
4
−0.3 ± 0.5
0
0
−0.5
0.5b)
0
0.0
0.0
5
1.4 ± 0.5
0
0
1.4a)
0
0
1.4
1.4
6
−0.2 ± 0.3
0
0
−0.3
0.3b)
0
0.0
0.0
7
−0.4 ± 0.2
0
0
0
0
−0.3
−0.3
−0.3
8
0.9 ± 0.3
0
0
0.9a)
0
0
0.9
0.9
9
6.9 ± 0.7
6.9a)
0
0
0
0
6.9
7.3
10
−5.5 ± 0.7
−10.0
4.0
0
0
0
−6.0
−5.5
a) Input.
b) Large-NC estimate.
c) With (6.19)
There are diﬀerent phenomenologically successful models in the literature for V
and A resonances [tensor-ﬁeld description (Gasser and Leutwyler 1984, Ecker et al
1989a), massive Yang–Mills (Meißner 1988), hidden gauge formulation (Bando et al
1988), etc.].
It can be shown (Ecker et al 1989b) that all models are equivalent
(i.e.
they give the same contributions to the Li), provided they incorporate the
appropriate QCD constraints at high energies.
Moreover, with additional QCD-
inspired assumptions of high-energy behaviour, such as an unsubtracted dispersion
relation for the pion electromagnetic form factor, all V and A couplings can be
expressed in terms of fπ and MV only (Ecker et al 1989b):
FV =
√
2fπ ,
GV = fπ/
√
2 ,
FA = fπ ,
MA =
√
2MV . (6.18)
In that case, one has
LV
1 = LV
2 /2 = −LV
3 /6 = LV
9 /8 = −LV +A
10
/6 = f 2
π/(16M 2
V ) .
(6.19)
The last column in table 2 shows the predicted numerical values of the Li couplings,
using the relations (6.19).
The exchange of scalar resonances generates the contributions (Ecker et al 1989a):
LS+S1
1
= −c2
d
6M 2
S
+
˜c2
d
2M 2
S1
,
LS
3 =
c2
d
2M 2
S
,
LS+S1
4
= −cdcm
3M 2
S
+ ˜cd˜cm
M 2
S1
,
LS
5 = cdcm
M 2
S
,
LS+S1
6
= −c2
m
6M 2
S
+
˜c2
m
2M 2
S1
,
LS
8 =
c2
m
2M 2
S
.
(6.20)
Since the experimental information is quite scarce in the scalar sector, one needs to
assume that the couplings L5 and L8 are due exclusively to scalar-octet exchange, to
determine the scalar-octet couplings cd and cm. Taking MS = Ma0 = 983 MeV, the
scalar-octet contributions to the other Li (i = 1, 3, 4, 6) are then ﬁxed. Moreover, one
can then predict Γ(a0 →ηπ) = 59 MeV, in good agreement with the experimental
value Γ(a0 →ηπ) ≈Γ(a0) = (57 ± 11) MeV. The S1-exchange contributions can be
expressed in terms of the octet parameters using large-NC arguments. For NC = ∞,
MS1 = MS, | ˜cd| = |cd|/
√
3 and | ˜cm| = |cm|/
√
3 (Ecker et al 1989a); therefore, octet-
and singlet-scalar exchange cancel in L1, L4 and L6. Although the results in table 2
cannot be considered as a proof for scalar dominance, they provide at least a convincing
demonstration of its consistency.
Neglecting the higher-mass 0−+ resonances, the only remaining meson-exchange is
the one associated with the η1, which generates a sizeable contribution to L7 (Gasser
and Leutwyler 1985, Ecker et al 1989a):
Lη1
7 = −
˜d2
m
2M 2η1
.
(6.21)
The magnitude of this contribution can be calculated from the quark-mass expansion
of M 2
η and M 2
η′, which ﬁxes the η1 parameters in the large Nc limit (Ecker et al 1989a):
Mη1 = 804 MeV, | ˜dm| = 20 MeV. The ﬁnal result for L7 is in close agreement with its
phenomenological value.
The combined resonance contributions appear to saturate the Lr
i almost entirely
(Ecker et al 1989a). Within the uncertainties of the approach, there is no need for
invoking any additional contributions. Although the comparison has been made for
µ = Mρ, a similar conclusion would apply for any value of µ in the low-lying resonance
region between 0.5 and 1 GeV.
