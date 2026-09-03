---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-008-green-functions-chiral-ward-identities-and-gener
section_title: "Green functions, chiral Ward identities, and generating functional"
section_number: null
pages: 9-15
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
For conserved currents, the spatial integrals of the charge densities are time independent, i.e., in a
quantized theory the corresponding charge operators commu te with the Hamilton operator. These
operators are generators of inﬁnitesimal transformations on the Hilbert space of the theory. The mass
eigenstates should organize themselves in degenerate mult iplets with dimensionalities corresponding to
irreducible representations of the Lie group in question. F or the moment, we assume that the dynamical
system described by the Hamiltonian does not lead to a sponta neous symmetry breakdown. We will
come back to this point later. Which irreducible representa tions ultimately appear, and what the actual
energy eigenvalues are, is determined by the dynamics of the Hamiltonian. For example, SU(2) isospin
9
symmetry of the strong interactions reﬂects itself in degen erate SU(2) multiplets such as the nucleon
doublet, the pion triplet, and so on. Ultimately, the actual masses of the nucleon and the pion should
follow from QCD.
It is also well-known that symmetries imply relations betwe en S-matrix elements. For example, ap-
plying the Wigner-Eckart theorem to pion-nucleon scatteri ng, assuming the strong-interaction Hamilto-
nian to be an isoscalar, it is suﬃcient to consider two isospi n amplitudes describing transitions between
states of total isospin I = 1/2 or I = 3/2. All the dynamical information is contained in these isosp in
amplitudes and the results for physical processes can be exp ressed in terms of these amplitudes together
with geometrical coeﬃcients, namely, the Clebsch-Gordan c oeﬃcients.
In quantum ﬁeld theory, the objects of interest are the Green functions which are vacuum expectation
values of time-ordered products. Later on, we will also refe r to matrix elements of time-ordered products
between states other than the vacuum as Green functions. The physical scattering amplitudes are
obtained from the Green functions using the reduction forma lism [Lehmann et al., 1955]. Symmetries
provide strong constraints not only for scattering amplitu des, i.e. their transformation behavior, but,
more generally speaking, also for Green functions and, in pa rticular, among Green functions. Even if
a symmetry is broken, i.e., the inﬁnitesimal generators are time dependent, conditions related to the
symmetry-breaking terms can still be obtained using equal- time commutation relations.
The symmetry currents relevant to the global SU(3) L×SU(3)R×U(1)V of QCD are given in Eqs. (17),
(18), and (21). Moreover, since we also want to discuss expli cit symmetry breaking, we introduce the
scalar and pseudoscalar densities
Sa = ¯qλaq, P a =i¯qγ5λaq, a = 0, · · ·, 8, (34)
where λ0 =
√
2/3 /BD . For example, linear combinations of Sa and Pa are needed to describe the diver-
gences of the currents in Eqs. (33). Whenever it is more conve nient, we will also use
S(x) = ¯q(x)q(x), P (x) = i¯q(x)γ5q(x), (35)
instead of S0 and P0.
For example, the following Green functions of the “vacuum” s ector
⟨0|T [Aµ
a(x)Pb(y)]|0⟩,
⟨0|T [Pa(x)J µ(y)Pc(z)]|0⟩,
⟨0|T [Pa(w)Pb(x)Pc(y)Pd(z)]|0⟩
are related to pion decay, the pion electromagnetic form fac tor (J µ is the electromagnetic current),
and pion-pion scattering, respectively. One may also consi der similar time-ordered products evaluated
between a single nucleon in the initial and ﬁnal states in add ition to the vacuum Green functions. This
allows one to discuss properties of the nucleon as well as dyn amical processes involving a single nucleon,
such as
⟨N|J µ(x)|N⟩ ↔ nucleon electromagnetic form factors ,
⟨N|Aµ
a(x)|N⟩ ↔ axial form factor + induced pseudoscalar form factor ,
⟨N|T [J µ(x)J ν(y)]|N⟩ ↔ Compton scattering,
⟨N|T [J µ(x)Pa(y)]|N⟩ ↔ pion electroproduction.
Generally speaking, a chiral Ward identity relates the dive rgence of a Green function containing at
least one factor of V µ
a orAµ
a to some linear combination of other Green functions. The ter minology chiral
refers to the underlying SU(3) L × SU(3)R group. To make this statement more precise, let us consider
10
as a simple example the two-point Green function involving a n axial-vector current and a pseudoscalar
density,
Gµ
AP,ab(x,y ) = ⟨0|T [Aµ
a(x)Pb(y)]|0⟩= Θ( x0 −y0)⟨0|Aµ
a(x)Pb(y)|0⟩+ Θ( y0 −x0)⟨0|Pb(y)Aµ
a(x)|0⟩, (36)
and evaluate the divergence
∂x
µGµ
AP,ab(x,y ) = ∂x
µ[Θ( x0 −y0)⟨0|Aµ
a(x)Pb(y)|0⟩+ Θ( y0 −x0)⟨0|Pb(y)Aµ
a(x)|0⟩]
= δ(x0 −y0)⟨0|Aa
0(x)Pb(y)|0⟩ −δ(x0 −y0)⟨0|Pb(y)Aa
0(x)|0⟩
+Θ( x0 −y0)⟨0|∂x
µAµ
a(x)Pb(y)|0⟩+ Θ( y0 −x0)⟨0|Pb(y)∂x
µAµ
a(x)|0⟩
= δ(x0 −y0)⟨0|[Aa
0(x),P b(y)]|0⟩+ ⟨0|T [∂x
µAµ
a(x)Pb(y)]|0⟩,
where we made use of ∂x
µΘ( x0 −y0) = δ(x0 −y0)g0µ = −∂x
µΘ( y0 −x0). This simple example already
shows the main features of (chiral) Ward identities. From th e diﬀerentiation of the theta functions one
obtains equal-time commutators between a charge density an d the remaining quadratic forms. The
results of such commutators are a reﬂection of the underlyin g symmetry. As a second term, one obtains
the divergence of the current operator in question. If the sy mmetry is perfect, such terms vanish
identically. If the symmetry is only approximate, an additi onal term involving the symmetry breaking
appears. For a soft breaking such a divergence can be treated as a perturbation.
The time ordering of n + 1 pointsx,x 1, · · ·,x n gives rise to (n + 1)! distinct orderings, each involving
products of n theta functions. Via induction, the generalization of the a bove simple example to an
(n + 1)-point Green function is symbolically of the form
∂x
µ⟨0|T {J µ(x)A1(x1) · · ·An(xn)}|0⟩=
⟨0|T {[∂x
µJ µ(x)]A1(x1) · · ·An(xn)}|0⟩
+δ(x0 −x0
1)⟨0|T {[J0(x),A 1(x1)]A2(x2) · · ·An(xn)}|0⟩
+δ(x0 −x0
2)⟨0|T {A1(x1)[J0(x),A 2(x2)] · · ·An(xn)}|0⟩
+ · · · +δ(x0 −x0
n)⟨0|T {A1(x1) · · ·[J0(x),A n(xn)]}|0⟩, (37)
where J µ stands generically for any of the Noether currents.
The discussion so far assumes that one explicitly works out t he particular chiral Ward identity one
is interested in. However, there is an elegant way of obtaini ng all chiral Ward identities from a single
expression. To that end we introduce into the Lagrangian of Q CD the couplings of the nine vector
currents, eight axial-vector currents, nine scalar quark d ensities, and nine pseudoscalar quark densities
to external c-number ﬁelds [Gasser and Leutwyler, 1985]:
L = L0
QCD + Lext, (38)
where
Lext =
8∑
a=1
vµ
a ¯qγµ
λa
2 q +vµ
(s)
1
3 ¯qγµq +
8∑
a=1
aµ
a ¯qγµγ5
λa
2 q −
8∑
a=0
sa ¯qλaq +
8∑
a=0
pai¯qγ5λaq
= ¯qγµ(vµ + 1
3vµ
(s) +γ5aµ)q − ¯q(s −iγ5p)q. (39)
The 35 real functions vµ
a (x),vµ
(s)(x),aµ
a(x),sa(x), and pa(x), will collectively be denoted by [ v,a,s,p ]. A
precursor of this method was already used by Bell and Jackiw [ Bell and Jackiw, 1969] in their discussion
of the anomalous divergences in the π0 →γγ decay. The Green functions of the vacuum sector may be
combined in the generating functional
exp(iZ[v,a,s,p ]) = ⟨0|T exp
[
i
∫
d4x Lext(x)
]
|0⟩0. (40)
11
Note that both the quark ﬁeld operators q in Lext and the ground state |0⟩refer to the chiral limit,
indicated by the subscript 0 in Eq. (40). A particular Green f unction is then obtained through a
functional derivative with respect to the external ﬁelds. A s an example, suppose we are interested in
the scalar u-quark condensate in the chiral limit, ⟨0|¯uu|0⟩0. We express ¯uu as
¯uu = 1
2
√
2
3 ¯qλ0q + 1
2 ¯qλ3q + 1
2
1√
3 ¯qλ8q
and obtain
⟨0|¯u(x)u(x)|0⟩0 = i
2


√
2
3
δ
δs0(x) + δ
δs3(x) + 1√
3
δ
δs8(x)

 exp(iZ[v,a,s,p ])
⏐
⏐
⏐
⏐
⏐
⏐
v=a=s=p=0
.
From the generating functional, we can even obtain Green fun ctions of the “real world,” where
the quark ﬁelds and the ground state are those with ﬁnite quar k masses. For example, the two-point
function of two axial-vector currents of the “real world,” i .e., for s = diag(mu,m d,m s), and the “true
vacuum” |0⟩, is given by
⟨0|T [Aµ
a(x)Aν
b (0)]|0⟩= ( −i)2 δ2
δaa µ(x)δab ν(0) exp(iZ[v,a,s,p ])
⏐
⏐
⏐
⏐
⏐
v=a=p=0,s=diag(mu,md,ms)
. (41)
Note that the left-hand side involves the quark ﬁelds and the ground state of the “real world,” whereas
the right-hand side is the generating functional deﬁned in t erms of the quark ﬁelds and the ground state
of the chiral limit. The actual value of the generating funct ional for a given conﬁguration of external
ﬁelds v, a, s, and p reﬂects the dynamics generated by the QCD Lagrangian.
The (inﬁnite) set of all chiral Ward identities resides in an invariance of the gener ating functional
under a local transformation of the external ﬁelds [Gasser and Leutwyler , 1984], [Leutwyler, 1994]. The
use of local transformations allows one to also consider div ergences of Green functions. We require
L of Eq. (38) to be a Hermitian Lorentz scalar, to be even under P , C, and T , and to be invariant
under local chiral transformations. In fact, it is suﬃcient to consider P and C, only, because T is then
automatically incorporated owing to the CPT theorem.
Under parity, the quark ﬁelds transform as
qf (t,⃗ x) P↦→γ0qf (t, −⃗ x), (42)
and the requirement of parity conservation,
L(t,⃗ x) P↦→ L(t, −⃗ x), (43)
leads, using the results of Table 4, to the following constra ints for the external ﬁelds,
vµ P↦→vµ, v µ
(s)
P↦→v(s)
µ , a µ P↦→ −aµ, s P↦→s, p P↦→ −p. (44)
In Eq. (44) it is understood that the arguments change from ( t,⃗ x) to (t, −⃗ x).
Similarly, under charge conjugation the quark ﬁelds transf orm as
qf,α
C↦→Cαβ ¯qf,β, ¯qf,α
C↦→ −qf,βC −1
βα, (45)
where the subscripts α and β are Dirac spinor indices,
C =iγ2γ0 =





0 0 0 −1
0 0 1 0
0 −1 0 0
1 0 0 0





12
Γ /BD γµ σµν γ5 γµγ5
γ0Γγ0
/BD γµ σµν −γ5 −γµγ5
Table 4: Transformation properties of the Dirac matrices Γ u nder parity.
Γ /BD γµ σµν γ5 γµγ5
−CΓ TC /BD −γµ −σµν γ5 γµγ5
Table 5: Transformation properties of the Dirac matrices Γ u nder charge conjugation.
is the usual charge conjugation matrix, and f refers to ﬂavor. Taking Fermi statistics into account, one
obtains
¯q ΓFq = −¯qC Γ TCF Tq,
where F denotes a matrix in ﬂavor space. In combination with Table 5 i t is straightforward to show
that invariance of Lext under charge conjugation requires the transformation prop erties
vµ
C→ −vT
µ, v (s)
µ
C→ −v(s)T
µ , a µ
C→aT
µ, s,p C→sT,p T, (46)
where the transposition refers to the ﬂavor space.
Finally, we need to discuss the requirements to be met by the e xternal ﬁelds under local SU(3) L ×
SU(3)R ×U(1)V transformations. In a ﬁrst step, we write Eq. (39) in terms of the left- and right-handed
quark ﬁelds. Using the projection operators of Eq. (11) the L agrangian of Eq. (39) reads
L = L0
QCD + ¯qLγµ
(
lµ + 1
3v(s)
µ
)
qL + ¯qRγµ
(
rµ + 1
3v(s)
µ
)
qR − ¯qR(s +ip)qL − ¯qL(s −ip)qR. (47)
Equation (47) remains invariant under local transformations
qR ↦→ exp
(
−iΘ( x)
3
)
VR(x)qR,
qL ↦→ exp
(
−iΘ( x)
3
)
VL(x)qL, (48)
where VR(x) and VL(x) are independent space-time-dependent SU(3) matrices, pr ovided the external
ﬁelds are subject to the transformations
rµ ↦→VRrµV †
R −i∂µVRV †
R,
lµ ↦→VLlµV †
L −i∂µVLV †
L,
v(s)
µ ↦→v(s)
µ −∂µΘ ,
s +ip ↦→VR(s +ip)V †
L,
s −ip ↦→VL(s −ip)V †
R. (49)
The derivative terms in Eq. (49) serve the same purpose as in t he construction of gauge theories, i.e.,
they cancel analogous terms originating from the kinetic pa rt of the quark Lagrangian. Note that the
external currents are coupled with an “opposite” sign in com parison with our convention for gauge
theories.
13
There is another, yet, more practical aspect of the local inv ariance, namely: such a procedure allows
one to also discuss a coupling to external gauge ﬁelds in the t ransition to the eﬀective theory to be
discussed later. For example, a coupling of the electromagn etic ﬁeld to point-like fundamental particles
results from gauging a U(1) symmetry. Here, the correspondi ng U(1) group is to be understood as a
subgroup of a local SU(3) L × SU(3)R. Another example deals with the interaction of the light qua rks
with the charged and neutral gauge bosons of the weak interac tions.
Let us consider both examples explicitly. The coupling of qu arks to an external electromagnetic
ﬁeld Aµ is given by
rµ =lµ = −eQAµ, (50)
where Q = diag(2/3, −1/3, −1/3) is the quark charge matrix and e> 0 the elementary charge:
Lext = −eAµ(¯qLQγµqL + ¯qRQγµqR) = −eAµ ¯qQγ µq = −eAµ
(2
3 ¯uγµu − 1
3
¯dγµd − 1
3 ¯sγµs
)
.
On the other hand, if one considers only the two-ﬂavor versio n of QCD one has to insert for the external
ﬁelds
rµ =lµ = −eτ3
2 Aµ, v (s)
µ = −e
2 Aµ. (51)
In the description of semi-leptonic interactions such as π− → µ−¯νµ, π− → π0e−¯νe, or neutron
decay n → pe− ¯νe one needs the interaction of quarks with the massive charged weak bosons W ±
µ =
(W1µ ∓iW2µ)/
√
2,
rµ = 0, l µ = − g√
2 (W +
µT+ + H.c.), (52)
where H.c. refers to the Hermitian conjugate and
T+ =



0 Vud Vus
0 0 0
0 0 0


.
Here, Vij denote the elements of the Cabibbo-Kobayashi-Maskawa quar k-mixing matrix describing the
transformation between the mass eigenstates of QCD and the w eak eigenstates [Amsler et al., 2008],
|Vud| = 0.97418 ± 0.00027, |Vus| = 0.2255 ± 0.0019.
At lowest order in perturbation theory, the Fermi constant i s related to the gauge coupling g and the
W mass as
GF =
√
2 g2
8M 2
W
= 1.16637(1) × 10−5 GeV−2. (53)
Making use of
¯qLγµW +
µT+qL = 1
2 W +
µ [Vud ¯uγµ(1 −γ5)d +Vus ¯uγµ(1 −γ5)s],
we see that inserting Eq. (52) into Eq. (47) leads to the stand ard charged-current weak interaction in
the light-quark sector,
Lext = − g
2
√
2
{
W +
µ [Vud¯uγµ(1 −γ5)d +Vus ¯uγµ(1 −γ5)s] + H.c.
}
.
The situation is slightly diﬀerent for the neutral weak inte raction. Here, the three-ﬂavor version
requires a coupling to the singlet axial-vector current whi ch, because of the anomaly of Eq. (33), we
14
have dropped from our discussion. On the other hand, in the tw o-ﬂavor version the axial-vector current
part is traceless and we have
rµ = e tan(θW )τ3
2 Zµ,
lµ = − g
cos(θW )
τ3
2 Zµ +e tan(θW )τ3
2 Zµ,
v(s)
µ = e tan(θW )
2 Zµ, (54)
where θW is the weak angle. With these external ﬁelds, we obtain the st andard weak neutral-current
interaction
Lext = − g
2 cos(θW ) Zµ
(
¯uγµ
{[ 1
2 − 4
3 sin2(θW )
]
/BD − 1
2γ5
}
u + ¯dγµ
{[
−1
2 + 2
3 sin2(θW )
]
/BD + 1
2γ5
}
d
)
,
where we made use of e =g sin(θW ).
