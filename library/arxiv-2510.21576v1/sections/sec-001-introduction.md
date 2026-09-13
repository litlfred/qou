---
doc_id: arxiv-2510.21576v1
doc_title: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 2510.21576v1.pdf
source_sha256: 17a79b59d590c8da
doc_brief: "Relativistic corrections for lepton-nucleus scattering in the short-time approximation — 7 sections: Relativistic corrections for lepto; Introduction; Short-time approximation"
---
In recent years, significant progress has been made in
calculating inclusive cross sections for lepton scattering
from nuclei [1, 2] using the microscopic, orab initio,
approach [3]. This framework allows for the inclusion
of many-nucleon correlations and electroweak currents,
which are essential for delivering theoretical predictions
that explain the available experimental data. Specifi-
cally, nuclear wave functions are determined by solving
the many-nucleon Hamiltonian, which typically includes
a kinetic term arising from the sum of the kinetic ener-
gies of individual nucleons, as well as two- and three-body
potentials that describe the correlations between nucle-
ons in pairs and triplets. The interaction with exter-
nal electroweak probes, such as electrons and neutrinos,
is expressed by one- and two-nucleon current operators,
which describe the coupling of the probe with individual
nucleons and pairs of correlated nucleons.
Due to the increasing computational cost associated
with a larger number of nucleons, theab initiomethod
has primarily been applied to light nuclei [2, 4–13]. Only
recently have calculations for systems with a mass num-
berA= 40 appeared in the literature [14, 15]. These
studies have highlighted the importance of many-nucleon
effects in accurately explaining the available experimen-
tal data.
Despite these advancements, there are two key limita-
tions within this approach. First, traditional methods are
generally limited to studying inclusive processes. Specifi-
∗ landreol@odu.edu
† ronen@wustl.edu
‡ chambers-wall@wustl.edu
§ agnech@odu.edu
¶ saori@wustl.edu
∗∗ m.piarulli@wustl.edu
cally, these methods rely on integral properties of the nu-
clear electroweak response functions, which are extracted
by unfolding the integral transforms. For example,
QMC calculations, specifically Green’s Function Monte
Carlo (GFMC) calculations, exploit the Euclidean trans-
form [5–10], while the coupled-cluster (CC) approach
uses the Lorentz integral transform (LIT) method [11–
13].
Second, theab initioframework is inherently nonrel-
ativistic, as it solves the many-body Schr¨ odinger equa-
tion. Relativistic effects in the electroweak currents are
typically treated perturbatively by expanding the covari-
ant single-nucleon currents in powers ofq/m, whereqis
the momentum transferred by the external electroweak
probe andmis the nucleon mass. Relativistic effects may
also be phenomenologically included in two-nucleon cor-
relations. In fact, the two-nucleon interactions typically
adopted in QMC calculations,i.e., the Argonnev 18 [16],
contain parameters that are fitted to nucleon-nucleon
scattering data, including data that involve center-of-
mass energy up to around 300 MeV, and reproduce the
phase shifts up to∼1 GeV where relativistic effects may
become significant.
Despite theapproximatedinclusions of relativistic ef-
fects, this approach fails to agree with the data at high
values of momentum transfer. The importance of a
proper relativistic treatment of the electroweak currents
has recently been highlighted in the context of electron
scattering from trinucleon systems [17], where QMC-
based calculations – namely the GFMC and the Short-
Time-Approximation (STA) – of cross sections were com-
pared with those obtained with the Spectral Function
method [18–20]. The latter adopts fully covariant single
nucleon currents and accounts for relativistic kinematics
in the final-state energies, thus correctly reproducing the
experimental data at highqvalues, while QMC calcula-
tions were in agreement with data up to values ofq≃600
MeV/c.
arXiv:2510.21576v1  [nucl-th]  24 Oct 2025
2
To address these limitations, two approaches have been
explored for incorporating relativistic effects in nonrela-
tivisticab initioQMC calculations. One relies on boost
transformations [21]. This approach has been applied,
for example, in combination with nuclear electroweak re-
sponses obtained from GFMC calculations, leading to
improvements in the description of scattering at higher
momentum transfers [22, 23].
The second approach, which is the focus of this work,
is based on the Short-Time Approximation (STA) [24]
factorization scheme, where the external probe interacts
only with pairs of correlated nucleons. This enables us
to extend theab initioapproach for nuclear electroweak
responses and cross sections to larger nuclei without los-
ing essential two-nucleon dynamics. The STA has been
validated through comparisons with exact theoretical re-
sults and experimental data of electron scattering from
light nuclei with mass numbersA= 3,4 and 12 [17, 24–
26], showing good agreement with the data up to values
of momentum transferq∼600 MeV/c. The STA fac-
torization scheme consistently incorporates two-nucleon
correlations and currents while isolating the interaction
vertex, thus allowing for a direct treatment of relativistic
effects.
Specifically, relativistic effects are included in the
single-nucleon current operator and in the treatment of
the two-nucleon final state kinematics. The nonrelativis-
tic reduction of the covariant single-nucleon electromag-
netic current is carried out using an expansion scheme
where the momentum transferqis no longer considered
as a small perturbative scale, as in traditional calcula-
tions [4, 27–29]. Instead, it assumes that the momentum
qcarried by the probe can be large and transferred to
the scattered nucleon, while only the momentum of the
struck nucleon inside the nucleus is small and is treated
perturbatively. This approach allows for a more accurate
theoretical description of relativistic effects ensuring bet-
ter agreement with experimental data at highq-values.
We note that a similar approach has been developed,
e.g., in Ref. [30] to study single nucleon electron scatter-
ing and 2H(e,e′p)nreactions. We will discuss some of
the differences in the relevant section.
The theoretical framework developed in this work is
directly relevant for current and future experimental pro-
grams in neutrino-nucleus scattering [31, 32] and can be
extended beyond the light nuclei studied here. Electron
scattering provides a valuable testing ground for nuclear
models applicable to neutrino physics, due to the wealth
of experimental data and the absence of complications
related to leptonic energy reconstruction [33]. Although
the STA has been validated for nuclei up toA= 12
within the Variational Monte Carlo (VMC) approach,
its algorithm can be exported to computational meth-
ods utilized to study heavier systems. For the Deep Un-
derground Neutrino Experiment (DUNE), which uses a
40Ar target, future developments of the STA approach
in combination with the Auxiliary Field Diffusion Monte
Carlo [34] many-body computational method, will allow
for lepton-nucleus studies toward medium-mass nuclei
contributing to a better modeling of neutrino-nucleus in-
teractions at the few-GeV energy scale. Continued devel-
opment of theoretical approaches that properly account
for relativistic effects and two-nucleon currents and cor-
relations in nuclear systems beyond the light mass region
are required to reduce uncertainties in neutrino energy re-
construction that are crucial for DUNE’s oscillation mea-
surements.
Similarly, this framework allows us to address observ-
ables measured in ongoing and future electron scattering
experiments at Jefferson Lab [35, 36]. Extension of the
STA framework to compute the cross section measured
in short-range correlation experiments [37] as well as Pri-
makoff production of pseudoscalar mesons [38] are also
possible and will be considered in future works. The de-
velopment of theab-initiotechnique such as the STA is
crucial to understanding and describing the experiments
with light nuclei at Jefferson JLab and in the future at
EIC [39].
The inclusion of relativistic effects at the vertex within
the framework of the STA is the focus of this paper.
The paper is organized as follows. Section II describes
nuclear response functions and inclusive cross sections.
In Section III, we discuss the covariant single-nucleon
electromagnetic current and its nonrelativistic reduction
suitable for largeq-values. Section IV outlines the STA
method. The relativistic treatment of two-nucleon final
state kinematics is discussed in Section V. Results and
comparisons with experimental data for inclusive electron
scattering are provided in Section VI, while in Section VII
we summarize our conclusions and outline the next stage
in this program of extending the kinematic reach of the
STA.
II. ELECTRON-NUCLEUS SCATTERING
CROSS SECTION
The inclusive double-differential cross section for elec-
tron scattering from a nucleus is written in terms of the
longitudinal,R L, and transverse,R T , response functions
as:
 d2σ
dε′dΩ

e
=
dσ
dΩ

M
"Q2
q2
2
RL(q,ω)
+

tan2 θ
2 + 1
2
Q2
q2

RT (q,ω)

,
(1)
whereε′ is the electron’s final energy and Ω is the scat-
tering solid angle. The Mott cross section is given by
dσ
dΩ

M
=
 αcos (θ/2)
2ε′ sin2 (θ/2)
2
,(2)
whereq=p e−p′
e andqdenote the three-momentum
transfer and its magnitude, respectively, andp e (p′
e)
is the momentum of the incoming (outgoing) electron.
3
The energy transfer is denoted byω=ε−ε ′, while
Q2 =q 2−ω 2, andθis the electron scattering angle. The
longitudinal and transverse response functions of Eq. (1)
describe the transition from an initial,|Ψ 0⟩, to a final nu-
clear state,|Ψ f⟩, of a nucleus with mass numberAand
initial (final) energyE 0 (Ef). Specifically,
RL(q,ω) =R 00(q,ω),(3)
and
RT (q,ω) =R xx(q,ω) +R yy(q,ω),(4)
where
Rµν(q,ω) =
X
f
⟨Ψ0|Jµ†(q,ω)|Ψf⟩⟨Ψf|Jν(q,ω)|Ψ 0⟩
×δ(E 0 +ω−E f),
(5)
and the sum runs on all possible final hadronic states,
both bound and in the continuum.
The currentJ µ(q,ω) describes the interaction between
the probe and the nucleus and it is expanded as a sum
of many-nucleon operators as
Jµ =
X
i
jµ
i +
X
i<j
jµ
ij +... ,(6)
wherej µ
i is a one-body operator acting on thei-th nu-
cleon and the sum runs over all the nucleons in the sys-
tem. The two-body component,j µ
ij, acts on nucleon cor-
related pairs,ij, and the corresponding sum goes over all
pairs in the system. As in conventional calculations, we
neglect terms that act on more than two nucleons and
chooseqto be along thez-axis.
The focus of this work is on an improved treatment
of the one-body current operators at high values of mo-
mentum transferq. For two-body currents, we em-
ploy the most recent formulation described at length in
Refs. [2, 24, 25, 34, 40] and references therein. These
will not be discussed further here; interested readers are
referred to those sources for more details.
The computational methods used in this work are de-
scribed in Refs. [24, 25]. Our calculations employ a nu-
clear Hamiltonian consisting of the Argonnev 18 two-
nucleon interaction [16] together with the Urbana IX
three-nucleon interaction [41]. The ground state wave
function includes two- and three-body correlations in-
duced by the Hamiltonian.
III. ONE-BODY ELECTROMAGNETIC
CURRENT
The covariant relativistic expression for the one-body
electromagnetic current operator is given by [4]
jµ = ¯u(p′s′)

F1γµ +iσµνqν
F2
2m

u(ps),(7)
wherep(p ′) is the initial (final) nucleon momentum with
massmand spins(s ′) and we omit, here and in the
following, the index that specifies thei-th nucleon. The
Dirac spinors and gamma matrices are denoted byuand
γµ, respectively, with ¯u=u †γ0 andσ µν = i
2[γµ,γν].
The 4-vector energy-momentum transfer is given byqν =
(ω,q).
The Dirac and Pauli form factors [42],F 1(Q2) and
F2(Q2), characterize the electromagnetic structure of the
nucleon and are expressed in terms of the electric and
magnetic Sachs form factorsG p,n
E/M(Q2) [43] of the pro-
ton and neutron,
Fp,n
1 = Gp,n
E +τG p,n
M
1 +τ , F p,n
2 = Gp,n
M −Gp,n
E
1 +τ ,(8)
whereτ=Q 2/4m2 is a kinematic factor. The nucleon’s
identity – whether it is a proton (p) or a neutron (n)
– is specified by the nucleon isopsin projection operator
(1±τ z)/2, withτ z denoting the third component of the
nucleon isospin operator. In what follows, for ease of
reading, we omit thep/nsuperscript and implicitly as-
sume the appropriate isospin projection operator acting
on the nucleon.
A. Low-momentum transfer nonrelativistic
reduction
Traditional many-body calculations [2, 4] adopt a non-
relativistic reduction of the single-nucleon covariant cur-
rent given in Eq. (7). The expansion is based on the
assumption that bothpandp ′ (and thusq) are small
compared to the nucleon mass. At leading order (LO),
this approach leads to the following expressions in co-
ordinate space for the charge,ρ=j 0, and current,j ⊥,
operators:
ρ=G Eeiq·r,(9)
j⊥ =eiq·r
GE
m p⊥−i GM
2m (q×σ)

,(10)
whereO⊥ =O−(O· ˆq)ˆqis the component of the operator
Operpendicular to the momentum transferq, andris
its spatial coordinate. Additionally, in coordinate space
p=−i∇and acts directly on the wave function (for
sub-leading terms involving powers ofp, particular care
must be taken when performing the Fourier transform
from momentum to coordinate space).
Typically, in addition to the LO term given above, the
single-nucleon charge operator includes the Darwin-Foldy
and spin-orbit terms, also accounting for relativistic ef-
fects [4]:
ρ=
"
GEp
1 +Q 2/4m2−i 2GM−GE
4m2 q·(σ×p)
#
eiq·r.
(11)
4
Using the expansion parameter discussed above, that
isq/m∼p/m∼p ′/m≪1, subleading terms of the
one-body charge and current operators, beyond LO, have
been derived,e.g., in Refs. [28, 29]. However, the ex-
pansion is limited to low-momentum-transfer kinematics
and consequently fails to accurately describe processes at
high energy. An appropriate expansion scheme for these
regimes is described in the next subsection.
B. High-momentum transfer nonrelativistic
reduction
For momentum transferq∼mor greater, relativistic
effects become important in two main ways. First, the
electromagnetic current operators require a proper non-
relativistic reduction. Second, the final states, which play
a significant role in the nuclear response functions, may
include high-momentum knocked-out nucleons, whose ki-
netic energies should be calculated relativistically for ac-
curate results. In this section, we focus on determining
the nonrelativistic reduction of the electromagnetic cur-
rents at high-momentum transfer. The results obtained
here are general and applicable in any microscopic mod-
eling of the nucleus. The treatment of final states’ rela-
tivistic kinematics within the STA framework is discussed
separately in Sec. V.
Our starting point is the covariant expression of the
one-body current operator given in Eq. (7). At low-
momentum transferq, its nonrelativistic reduction at
leading order is given in Eqs. (9) and (10) which are accu-
rate forq≪m. Sub-leading terms extend the currents’
validity up to moderateq, but the expansion breaks down
at larger momenta since it assumesq/m≪1. Even the
inclusion of sub-leading terms fails to overcome this lim-
itation. To address this, we adopt a different strategy –
introduced in Ref. [30] – in which only the initial nucleon
momentumpis assumed to be small. This is justified
in the quasi-elastic kinematic regime where the struck
nucleon is initially at low momentum but receives a mo-
mentumqfrom the probing lepton, which can be large.
Thus, we avoid the assumption that the nucleon final mo-
mentump′ is small and expand the covariant current only
inp/m. The resulting expressions are then valid for any
value of momentum transferqprovided thatp/m≪1.
To carry out this nonrelativistic reduction we begin by
defining the spinors and their normalizations
u(ps) =N(p)
 1
σ·p
E+m

χs,(12)
whereχ s andE=
p
p2 +m 2 are the nucleon spin state
and energy, respectively, whileNis a normalization fac-
tor chosen so thatu †u= 1. Specifically, for a nucleon
with momentumpand energyE, the normalization fac-
tor reads:
N(p) =
r
E+m
2E .(13)
An expansion of the normalization factor inp/myields
N(p)→1 at leading order.
For the final state, wherep ′ =p+q, we make no
assumption on the size ofp ′ andq. Thus, at leading
order the normalization factor of the final nucleon spinor
reads:
N(p′) =
r
E′ +m
2E′ →
sp
q2 +m 2 +m
2
p
q2 +m 2 ≡α(q).(14)
Sub-leading corrections arise from further expanding in
p/m.
This expansion scheme is also applied to the factors
(E+m) −1 and (E′ +m)−1 entering the spinors, and to
the energy transferωdefined as:
ω=E ′−E=
p
p′2 +m 2−
p
p2 +m 2.(15)
We note that this formulation assumes that both the ini-
tial and final nucleons are on-shell. While different con-
ventions exist, the impact of off-shell corrections near the
quasi-elastic peak is expected to be minimal [44].
The nucleon form factorsF 1(Q2) andF 2(Q2) appear-
ing in the covariant expression of the electromagnetic cur-
rent – Eq. (7) – must also be treated consistently since
they depend on the nucleon momentum throughQ 2. At
leading order inp/m, this effectively corresponds to eval-
uating the form factors at the quasi-elastic peak, that is
atp= 0, or equivalently atQ 2 =Q 2
qe with
Q2
qe = 2m
p
q2 +m 2−m

.(16)
Then the form factor expressions become:
GE(Q2
qe) =F 1(Q2
qe)−τ qeF2(Q2
qe),(17)
GM(Q2
qe) =F 1(Q2
qe) +F 2(Q2
qe),(18)
with
τqe = Q2
qe
4m2 =
p
q2 +m 2−m
2m .(19)
By expanding the covariant electromagnetic current in
p/mwhile treating the momentum transferqexactly, we
obtain the following expressions at leading order (LO),
∼(p/m) 0:
ρ(0) =α(q)G E(Q2
qe)eiq·r,(20)
j(0)
⊥ = 2mτqe
q2 GM(Q2
qe)α(q)i(σ×q)e iq·r.(21)
The next-to-leading-order (NLO) expressions include
terms of the order∼(p/m) 1 and are given by:
5
ρ(1) = α(q)τqe
m2(2τqe + 1)2(τqe + 1) [(2τqe + 1)GM−τqeGE]q·p− α(q)
(τqe + 1)
2GM−GE
4m2 iq·(σ×p),(22)
j(1)
⊥ =
 α(q)
m(τqe + 1)
h
GE + τqe
2 GM
i
p⊥ +
 α(q)τqe
m(τqe + 1)
1
2GE−GM

i(σ×p) ⊥
+
 α(q)
4m3(τqe + 1)2(2τqe + 1)2

−GE
1
2(2τqe + 1)2 +GM(2τ 2
qe−1)

(p·q) (iσ×q)
+
 α(q)
8m3(τqe + 1)2 (GM−GE)

(σ·q)(iq×p),(23)
where we dropped the overalleiq·r factor for ease of read-
ing. Note that also at NLO the Sachs form factors are
evaluated at the quasielastic peak, so in the equations
aboveG E/M≡G E/M(Q2
qe). Corrections beyond this ap-
proximation will appear at the next order.
The nucleonic form factorsGE/M are described by em-
pirical functions, typically constrained through fits to ex-
perimental data. In principle, their expansion around
the quasielastic peak introduces terms that should be in-
cluded for consistency. For example, terms linear inp,
when combined with the operator structures of Eqs. (20)
and (21), would contribute at NLO. While these contri-
butions could be determined explicitly for a given param-
eterization, this lies beyond the scope of this work.
The expansion presented here closely follows the ap-
proach developed in Ref. [30], but for some differences
arising from the use of different conventions. In par-
ticular, we adopt the normalization conditionu †u= 1,
which leads to the normalization factor given in Eq. (13).
The same convention is effectively used, for example, in
Ref. [45] (see Eqs. (2.2), (2.3), and (2.5) therein). This
convention is consistent with the definition of cross sec-
tion given in Eq. (1). Ref. [30], on the other hand, uses
the normalization factorN=
p
(E+m)/(2m), a con-
vention also adopted in Ref. [46] (see Eq. (A.6) in that
reference). As a result, their corresponding expression
for the cross section includes additional kinematics fac-
tors compared with the definition given in Eq. (1).
While the different conventions lead to distinct expres-
sions in the response functions and currents, they do not
affect the cross sections at LO inp/m. For example,
Ref. [30] reports an increase in the longitudinal response
function (relative to the longitudinal response calculated
with the LO charge operator of Eq. (9) obtained by ex-
panding inq/m), whereas we find a decrease. Despite
this, the corresponding cross sections agree at this order.
Another difference that affects the formal expressions at
NLO and beyond is related to the treatment of the energy
transferωgiven in Eq. (15), which we expand to allow
for a more efficient implementation in QMC calculations.
As a consistency check, we have verified that our con-
ventions for both the spinor normalization and the cross-
section reproduce the well-known Rosenbluth cross sec-
tion in the limit of a single nucleon at rest in the initial
state. This verification is detailed in App. A
Here, we have focused exclusively on the one-body cur-
rent operator. A similar treatment should be in principle
applied to two-body currents. However, within the low-
momentum transfer expansion scheme, the two-body vec-
tor and charge currents scale asp/m[29, 45], therefore,
corrections to their standard formulations are expected
to be small overall. For an expansion of two-body meson
exchange currents see,e.g., Ref. [47].
C. Comparing low- and high-momentum transfer
nonrelativistic reductions
In this section, we compare the low-momentum trans-
fer nonrelativistic reduction at LO of the single nucleon
charge and current operators – given in Eqs. (9) and (10)
– with the corresponding expressions obtained in the
high-momentum transfer regime – Eqs. (20) and (21).
We start with the charge operator. Here, the main
difference is the additional factorα(q) in the LO high-q
result of Eq. (20). Sinceα(q)→1 forq→0, the two
results coincide forq≪m. However,α(q)<1 for all
values ofq, and its deviation from unity increases with
increasingq, leading to a suppression in the longitudinal
response at LO. Specifically, the longitudinal response
– which involves a current-current correlator – scales as
α(q)2 in the high-qexpansion scheme, whereas in the
low-qreduction the scaling prefactor is simply one. The
ratio of the longitudinal responses obtained in the two
different schemes, namely
Rhigh−q
L
Rlow−q
L
∝α(q) 2,(24)
is plotted in Fig. 1 as a function ofq. The reduction
becomes increasingly pronounced at highq. For example,
α2 = 0.9 forq= 700 MeV/c, andα 2 = 0.77 forq= 1500
MeV/c, and, in the limit ofq≫m,α 2→1/2.
We can also compare the low-qresult at LO with the
Darwin-Foldy contribution to the charge operator, given
by the first term in Eq. (11). In this case, the resulting
ratio of longitudinal responses is proportional to
RDF
L
Rlow−q
L
∝ 1
(1 +Q 2qe/4m2),(25)
and it is also plotted in Fig. 1 for comparison. The LO
high-qexpression (solid blue line) and the Darwin-Foldy
6
0 500 1000 1500 2000 2500 3000
q [MeV/c]
0.5
0.6
0.7
0.8
0.9
1.0
Rhigh q
L
Rlow q
L
RDF
L
Rlow q
L
FIG. 1: Ratio of the longitudinal responses obtained
using:i) the high- and low-qexpansion schemes for the
one-body charge orator at LO (blue solid line); andii)
the Darwin-Foldy correction to the charge operator and
the low-qexpansion at LO (orange dashed line). See
text for explanation.
(orange dashed line) term agree well up to moderate val-
ues of momentum transfer. Differences arise atq≳500
MeV/c. In this regime, the Darwin-Foldy prefactor de-
creases more rapidly thanα(q), resulting in a stronger
suppression in the longitudinal response. Consequently,
the high-qnonrelativistic reduction leads to compara-
tively larger longitudinal response functions. For exam-
ple, atq= 1500 MeV/cthere is a∼10% enhancement.
Moreover, in the limit ofq≫m, the Darwin-Foldy term
goes to zero, unlikeα 2(q), leading to significant differ-
ences.
We now turn our attention to the transverse cur-
rent operator and compare its LO low-momentum trans-
fer expression, Eq. (10), with the LO high-momentum
result, Eq. (21). In the limit ofq→0, the factor
(2mτqe)/q2→1/2m, and the expression in Eq. (21) re-
duces to the second term in Eq. (10). The first term in
Eq. (10), proportional top⊥, appears at next-to-leading-
order in the high-qreduction and is expected to con-
tribute less at large momentum transfer. Its coefficient
matches the corresponding term in Eq. (23) in theq→0
limit.
Focusing on the dominant contributions at largeq,
the prefactor (2mτ qe)α(q)/q 2 in the LO high-qexpan-
sion should be compared to the factor 1/2mappearing
in Eq. (10). Therefore, the relative suppression factor in
the LO transverse response function is
Rhigh−q
T
Rlow−q
T
∝
4m2τqeα(q)
q2
2
.(26)
This factor, plotted in Fig. 2, is always less than one
and decreases with increasing values ofq, leading to a
0 500 1000 1500 2000 2500 3000
q [MeV/c]
0.2
0.4
0.6
0.8
1.0
Rhigh q
T
Rlow q
T
FIG. 2: Ratio of the transverse responses obtained
using the LO high-qand LO low-qexpansion schemes
for the one-body current operator. See text for
explanations.
suppression of the transverse response. Already atq≈
400 MeV/cthe suppression is around 10%. Atq= 700
MeV/c, the factor is∼0.71, and it drops to∼0.37 at
q= 1500 MeV/c.
In the limit ofq≫m, the factor scales as 2m 2/q2, van-
ishing for largeq. This leads to a significant reduction
in the transverse response function due to relativistic ef-
fects – an effect that cannot be captured by the low-q
nonrelativistic reduction.
