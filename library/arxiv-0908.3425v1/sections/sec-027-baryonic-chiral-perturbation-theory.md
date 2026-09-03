---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-027-baryonic-chiral-perturbation-theory
section_title: "Baryonic chiral perturbation theory"
section_number: null
pages: 49-52
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
4.1 Lagrangian
So far we have considered the purely mesonic sector involvin g the interaction of Goldstone bosons with
each other and with the external ﬁelds. Now we want to describ e matrix elements with a single baryon
in the initial and ﬁnal states.
4.1.1 Transformation properties of the ﬁelds
Our aim is the most general description of the interaction of baryons with Goldstone bosons and external
ﬁelds at low energies. For that purpose we not only need to spe cify the transformation behavior of the
Goldstone bosons and external ﬁelds but also of the remainin g dynamical ﬁelds entering the Lagrangian.
Our discussion follows Refs. [Georgi, 1984], [Gasser et al. , 1988]. Consider the nucleon doublet and the
octet of 1
2
+
baryons (see Fig. 2),
Ψ =
(
p
n
)
, (169)
B =
8∑
a=1
Baλa√
2 =




1
√
2Σ 0 + 1√
6Λ Σ + p
Σ − − 1√
2Σ 0 + 1√
6 Λ n
Ξ − Ξ 0 − 2√
6Λ



. (170)
Each entry of Ψ and B, respectively, is a complex, four-component Dirac ﬁeld. In contradistinction
to the case of the Goldstone-boson matrix φ of Eq. (88), we have B ⁄= B†. The representation of the
isospin group SU(2) V and the ﬂavor group SU(3) V on {Ψ } and {B}, respectively, is given by
Ψ ↦→V Ψ , V ∈ SU(2)V, (171)
B ↦→VBV †, V ∈ SU(3)V, (172)
i.e., Ψ transforms under the fundamental representation of SU(2) and B transforms under the adjoint
representation of SU(3). Starting from Eqs. (171) and (172) we will discuss realizations of SU(2) L ×
SU(2)R and SU(3) L × SU(3)R on {Ψ } and {B}, respectively.
Let us begin with G = SU(2) L × SU(2)R. Recall that the transformation of Eq. (85),
U ↦→RUL †,
deﬁnes a nonlinear realization of G on {U}. Introducing u2 =U, we deﬁne the SU(2)-valued function
K(L,R,U ) by
u ↦→u′ =
√
RUL † ≡RuK −1(L,R,U ), i.e., K(L,R,U ) = u′−1Ru =
√
RUL †−1
R
√
U. (173)
49
The transformation
ϕ(g) :
(
U
Ψ
)
↦→
(
U ′
Ψ ′
)
=
(
RUL †
K(L,R,U )Ψ
)
(174)
deﬁnes an operation of the group G on the set {(U, Ψ) }. This is true, because (a) the identity of G
leaves any pair (U, Ψ) invariant and (b) the transformation satisﬁes the homomo rphism property
ϕ(g1)ϕ(g2)
(
U
Ψ
)
= ϕ(g1)
(
R2UL †
2
K(L2,R 2,U )Ψ
)
=
(
R1R2UL †
2L†
1
K(L1,R 1,R 2UL †
2)K(L2,R 2,U )Ψ
)
=
(
R1R2U(L1L2)†
K(L1L2,R 1R2,U )Ψ
)
=ϕ(g1g2)
(
U
Ψ
)
,
where we made use of
K(L1,R 1,R 2UL †
2)K(L2,R 2,U ) = K((L1L2), (R1R2),U ).
Note that for a general group element g = (L,R ) ∈ G the transformation behavior of Ψ depends on
U. The exception to this rule is the case of an isospin transfor mation R = L = V , where, because of
U ′ =u′2 =VuV †VuV † =Vu 2V † =VUV †, one has u′ =VuV †. Comparing with Eq. (173), we obtain
K −1(V,V,U ) = V † or K(V,V,U ) = V . This is consistent with our starting point that Ψ transform s
linearly as an isospin doublet under the isospin subgroup H = SU(2) V ofG = SU(2) L × SU(2)R. Recall
that the symmetry of the vacuum determines the multiplet str ucture of the spectrum [Coleman, 1966].
ForG = SU(3) L × SU(3)R one uses
ϕ(g) :
(
U
B
)
↦→
(
U ′
B′
)
=
(
RUL †
K(L,R,U )BK †(L,R,U )
)
, (175)
whereK is deﬁned completely analogously to Eq. (173) after inserti ng the corresponding SU(3) matrices.
The generalization to other multiplets is straightforward . One ﬁrst speciﬁes the transformation
behavior under the subgroup H in terms of V and V †. In order to ﬁnd the transformation behavior
under G one simply replaces V →K and V † →K †.
4.1.2 Baryonic eﬀective Lagrangian at lowest order
Given the dynamical ﬁelds of Eqs. (174) and (175) and their tr ansformation properties, we will now
discuss the most general eﬀective baryonic Lagrangian at lo west order. We will start with the eﬀective
πN Lagrangian L(1)
πN which we demand to have a local SU(2)L × SU(2)R × U(1)V symmetry. The
transformation behavior of the external ﬁelds is given in Eq . (49), whereas U and the nucleon doublet
transform as (
U(x)
Ψ( x)
)
↦→
(
VR(x)U(x)V †
L (x)
exp[−iΘ( x)]K[VL(x),V R(x),U (x)]Ψ( x)
)
. (176)
The local character of the transformation implies that we ne ed to introduce a covariant derivative DµΨ
with the usual property that it transforms in the same way as Ψ ,
DµΨ = ( ∂µ + Γ µ −iv(s)
µ )Ψ , (177)
where the so-called connection is given by
Γ µ = 1
2
[
u†(∂µ −irµ)u +u(∂µ −ilµ)u†
]
. (178)
50
Since K not only depends on VL and VR but also on U, the covariant derivative contains besides the
external ﬁelds also u and u† and their derivatives. At O(q) there exists another Hermitian building
block, the so-called vielbein,
uµ ≡i
[
u†(∂µ −irµ)u −u(∂µ −ilµ)u†
]
, (179)
which under parity transforms as an axial vector, uµ ↦→ −uµ, and under SU(2) L × SU(2)R × U(1)V ,
transforms as uµ ↦→Ku µK †.
The structure of the most general eﬀective πN Lagrangian describing processes with a single nucleon
in the initial and ﬁnal states is of the type ¯Ψ ˆOΨ, where ˆO is an operator acting in Dirac and ﬂavor space,
transforming under SU(2) L × SU(2)R × U(1)V asKˆOK †. The Lagrangian must be a Hermitian Lorentz
scalar which is even under the discrete symmetries C, P , and T . The most general such Lagrangian
with the smallest number of derivatives is given by [Gasser e t al., 1988]
L(1)
πN = ¯Ψ
(
iD /−m + gA
2 γµγ5uµ
)
Ψ . (180)
It contains two parameters not determined by chiral symmetr y: the chiral limit m of the nucleon
mass mN and the chiral limit gA of the axial-vector coupling constant gA. The physical value of gA is
determined from neutron beta decay and is given by gA = 1.2695 ± 0.0029. The overall normalization
of the Lagrangian is chosen such that in the case of no externa l ﬁelds and no pion ﬁelds it reduces to
that of a free nucleon of mass m.
Similarly as in the mesonic case, the Lagrangian L(1)
πN has predictive power once the two pa-
rameters have been identiﬁed. For example, a tree-level cal culation of pion-nucleon scattering pro-
duces the famous Weinberg-Tomozawa relation for the s-waveπN -scattering lengths [Weinberg, 1966],
[Tomozawa, 1966],
aI = − Mπ
8π(1 +µ)F 2π
[
I(I + 1) − 3
4 − 2
]
, (181)
where I = 1/2 or I = 3/2 refers to the total isospin of the πN system. As in ππ scattering, the s-wave
πN -scattering lengths vanish in the chiral limit, i.e., Golds tone bosons interact “weakly” with other
hadrons in the zero-energy and mass limit.
Since the nucleon mass mN does not vanish in the chiral limit, the zeroth component ∂0 of the
partial derivative acting on the nucleon ﬁeld does not produ ce a “small” quantity. This results in
new features of the chiral power counting in the baryonic sec tor. The counting of the external ﬁelds
as well as of covariant derivatives acting on the mesonic ﬁel ds remains the same as in mesonic chiral
perturbation theory. On the other hand, the counting of bili nears ¯ΨΓΨ is probably easiest understood
by investigating the matrix elements of positive-energy pl ane-wave solutions to the free Dirac equation
in the Dirac representation:
ψ(+)(t,⃗ x) = exp( −ip ·x)
√
E +mN
(
χ
⃗ σ·⃗ p
E+mN
χ
)
, (182)
where χ denotes a two-component Pauli spinor and pµ = (E,⃗ p) with E =
√
⃗ p2 +m2
N . In the low-
energy limit, i.e., for non-relativistic kinematics, the l ower (small) component is suppressed as |⃗ p|/mN
in comparison with the upper (large) component. For the anal ysis of the bi-linears it is convenient to
divide the 16 Dirac matrices into even and odd ones, E = {
/BD ,γ 0,γ 5γi,σ ij} and O = {γ5,γ 5γ0,γ i,σ i0}
[Foldy and Wouthuysen, 1950], respectively, where odd matr ices couple large and small components but
not large with large, whereas even matrices do the opposite. Finally,i∂µ acting on the nucleon solution
produces pµ which we write symbolically as pµ = (mN,⃗0) + (E −mN,⃗ p), where we count the second
51
term as O(q), i.e., as a small quantity. We are now in the position to summ arize the chiral counting
scheme for the (new) elements of baryon chiral perturbation theory [Krause, 1990]:
Ψ , ¯Ψ = O(q0), DµΨ = O(q0), (iD /−m)Ψ = O(q),
/BD ,γ µ,γ 5γµ,σ µν = O(q0), γ5 = O(q), (183)
where the order given is the minimal one. For example, γµ has both an O(q0) piece,γ0, as well as an O(q)
piece,γi. Note that because of the additional spin degree of freedom t he baryonic eﬀective Lagrangian
contains both odd and even chiral orders. A rigorous non-rel ativistic reduction may be achieved in
the framework of the Foldy-Wouthuysen method [Foldy and Wou thuysen, 1950], [Fearing et al., 1994]
or the heavy-baryon approach [Jenkins and Manohar, 1991], [ Bernard et al., 1992a].
The construction of the SU(3) L × SU(3)R Lagrangian proceeds similarly except for the fact that the
baryon ﬁelds are contained in the 3 × 3 matrix of Eq. (170) transforming as KBK †. As in the mesonic
sector, the building blocks are written as products transfo rming as K · · ·K † with a trace taken at the
end. The lowest-order Lagrangian reads [Georgi, 1984], [Kr ause, 1990]
L(1)
M B = Tr
[
¯B (iD /−M0)B
]
−D
2 Tr
(
¯Bγ µγ5{uµ,B }
)
− F
2 Tr
(
¯Bγ µγ5[uµ,B ]
)
, (184)
where M0 denotes the mass of the baryon octet in the chiral limit. The c ovariant derivative of B is
deﬁned as
DµB =∂µB + [Γ µ,B ], (185)
with Γ µ of Eq. (178) [for SU(3) L × SU(3)R]. The constants D andF may be determined by ﬁtting the
semi-leptonic decays B →B′ +e− + ¯νe at tree level [Borasoy, 1999]:
D = 0.80, F = 0.50. (186)
