---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-005-hard-scattering-amplitudes
section_title: "Hard-scattering amplitudes"
section_number: null
pages: 4-6
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
At the interaction vertex the event is weighted by the
squared electroweak amplitude for the selected channel:
quasi-elastic scattering, governed by the nucleon axial
and vector form factors, and resonant pion production,
described by the dynamical coupled-channels amplitudes
used in ACHILLES [28, 86]. Evaluating these ampli-
tudes is computationally expensive and, in the case of
the tabulated coupled-channels amplitudes, is not writ-
ten to be differentiated. Rather than autodifferentiate
through that evaluation,ADoNIScaptures its depen-
dence on the parameters of interest at generation time.
The reweighting construction.The hadron current is
linear in the quantities through which the physics param-
eters enter,
Hb =
X
i
FiHi,b,(3)
whereblabels the nucleon spin combination, theH i,b
are unit currents fixed by the event kinematics and spin
state, and theF i encode the parameter dependence:
form factors in the quasi-elastic case, and more gener-
ally form factors and other amplitude strengths in the
resonant case. The squared amplitude is therefore an
exact quadratic form in theF i,
|M|2 =
X
ij
FiFjMij, M ij = Re
X
ab
(La·Hi,b)∗(La·Hj,b),
(4)
whereL a is the leptonic current for lepton spin combina-
tiona, andaandbrun over the lepton and nucleon spin
combinations, respectively. The symmetric matrixM ij
depends only on the kinematics, not on the physics pa-
rameters, so it is assembled once at generation and stored
per event. The vertex factor of Eq. 1 is then
rvertex
i (θ) = F(θ)⊤MF(θ)
F(θ 0)⊤MF(θ 0),(5)
whereθ 0 denotes the nominal values. This is an iden-
tity rather than a fit: the underlying amplitude calcula-
tion is never rerun after generation, the weight is exactly
unity at nominal, and because every parameter enters
only through the smooth mapθ7→F, the construc-
tion is exact for arbitrary simultaneous variations and
differentiable to any order. For quasi-elastic scattering,
F={F 1,F 2,FA,FP}, soMis 4×4; the resonant chan-
nel is treated analogously, with separate vector, axial and
pion-pole contributions for each partial wave.
Where the parameters of interest affect only a subset
of these contributions, the quadratic separates exactly.
5
SplittingFinto the components that vary,F var, and
those held at their nominal values,F fix,
|M|2 =F⊤
varMvvFvar + 2F⊤
varv+c,(6)
withv=M vfF 0
fix andc=F 0⊤
fix MffF 0
fix, so that only
(Mvv,v,c) need be stored. The fixed contributions are
compressed intovandcrather than discarded, and the
record grows or shrinks with the list of parameters ex-
posed.
The quasi-elastic current.Quasi-elastic scattering pro-
ceeds through the one-body weak current. For charged-
current scattering it takes the standard form [135],
Jµ = ¯u(p′)
h
F1γµ + iF2
2mN
σµνqν
+FAγµγ5 + FP
mN
qµγ5
i
u(p),(7)
withqthe four-momentum transfer. Neutral-current
elastic scattering has the same four current structures,
so the quadratic construction of Eq. 4 applies unchanged;
only the electroweak combinations entering their coeffi-
cients differ. In particular, the vector contributions de-
pend on different proton and neutron form-factor com-
binations, while the axial contribution changes sign be-
tween proton and neutron. Strange form factors are not
included in ACHILLES and are therefore also absent
fromADoNIS.
The vector form factorsF 1 andF 2 describe the charge
and magnetisation distributions of the nucleon and are
fixed by electron scattering;F A andF P are the axial
and induced pseudoscalar form factors. In addition to
the parameters entering these form factors themselves,
ADoNISintroduces two overall scaling parameters:S QE
V
scalesF 1 andF 2 together, whileS QE
A scalesF A andF P
together.
Vector form factors.F 1 andF 2 are built from the
Sachs electric and magnetic form factors,
F1 = GE +τG M
1 +τ , F 2 = GM−GE
1 +τ ,(8)
withτ=Q 2/4m2
N. These are taken from the Kelly
parametrisation [128], in which each Sachs form factor
is a ratio of polynomials inτ,
G(τ) = 1 +a 1τ
1 +b 1τ+b 2τ 2 +b 3τ 3,(9)
fitted to elastic electron–proton data and constructed
to fall with the correct power ofQ 2 at large momen-
tum transfer. The four parametersµ p,µ n,G p
E andG n
E
scaleG p
M,G n
M,G p
E andG n
E individually, and enter Eq. 5
through the linear relations above.
Axial form factor.The axial form factor is taken as az-
expansion, the model-independent parametrisation that
maps the analytic domain ofF A(Q2) onto the unit disc,
z(Q2) =
p
tc +Q 2−√tc−t 0p
tc +Q 2 +√tc−t 0
, F A =
X
k
akzk,
(10)
witht c = 9m2
π the three-pion production threshold and
t0 a fixed expansion point. The coefficients are those
of Ref. [50], obtained from neutrino–deuteron data. Be-
cause this form has no axial mass,M QE
A acts instead
through the ratio of two dipoles,
F dip
A (Q2;MA) = −gA
(1 +Q 2/M2
A)2,
r(Q2;MA) = F dip
A (Q2;MA)
F dip
A (Q2; 1.0 GeV)
,(11)
evaluated at the momentum transferQ 2 of each event,
which is stored in the event record, and multiplying the
axial block in Eq. 5. It therefore deforms the axialQ 2
dependence about the nominal in the direction an axial
mass would, and is unity atM A = 1.0 GeV by con-
struction. OnlyM 2
A appears, so the ratio is even inM A.
The induced pseudoscalar follows fromF A by the pion-
pole dominance relationF P = 2m2
NFA/(Q2 +m 2
π) and is
therefore carried along by bothS QE
A andM QE
A .
Resonant vertex.Single-pion production is de-
scribed by the ANL–Osaka dynamical coupled-channels
model [28]. Rather than summing independent Breit–
Wigner resonances, it solves coupled scattering equations
for the meson–baryon channelsπN,ηN,KΛ andKΣ si-
multaneously, so that resonant and non-resonant contri-
butions and their interference emerge from one unitary
amplitude. OnlyπNis produced at the interaction ver-
tex; the remaining channels enter through the coupled-
channel solution rather than as generated final states.
The amplitude is decomposed into partial waves labelled
L2I2J by the orbital angular momentum, isospin and to-
tal angular momentum of the pion–nucleon pair; fourteen
are tabulated,
S11, S31, P11, P13, P31, P33, D13,
D15, D33, D35, F15, F17, F35, F37,
each containing the resonances with the corresponding
quantum numbers. All fourteen contribute to the nomi-
nalADoNISprediction, and each can carry an indepen-
dent differentiable normalisation because the amplitude
is linear in that contribution. For simplicity, the studies
below vary onlyS ∆, which scales theP 33 partial wave
that contains the ∆(1232) resonance and dominates pion
production at accelerator energies.
Beyond the partial-wave normalisations,F pp scales the
longitudinal pion-pole term of the charged-current reso-
nant current, analogous to the induced pseudoscalar con-
tribution discussed above. The axial current is controlled
byC A
5 andM RES
A : the former scales its overall strength,
while the latter modifies itsQ 2 dependence using the
same dipole-ratio construction introduced forM QE
A .
Neutral-current resonant production uses the same
DCC decomposition. The partial-wave normalisations
and the axial parametersC A
5 andM RES
A are common
to charged- and neutral-current production. The differ-
ences lie in the electroweak current: the vector contribu-
tion uses the corresponding neutral-current combination
6
of isovector and isoscalar components, and the pion-pole
term is absent. Consequently,F pp affects only charged-
current resonant events.
In this way, the event-dependent ingredients of the
amplitude are evaluated once at generation, while its
dependence on the axial masses, form-factor scales and
strengths remains explicit and can be differentiated ex-
actly at negligible fit-time cost.
