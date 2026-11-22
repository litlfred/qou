---
doc_id: arxiv-2008.05806v2
doc_title: "Sum rule for the Compton amplitude and implications for the proton-neutron mass diﬀerence"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2008.05806v2.pdf
source_sha256: 4e1f9af118ba81b1
toc_source: outline
doc_brief: "Sum rule for the Compton amplitude and implications for the proton-neutron mass difference — The Cottingham formula expresses the lead- ing contribution of the electromagnetic interaction to the"
---
Introduction . . . . . . . . . . . . . . . . . . . . . . .
1
2
Lorentz invariance, kinematic zeros . . . . . . . . . .
3
3
Dispersion relations
. . . . . . . . . . . . . . . . . .
3
4
Reggeon dominance
. . . . . . . . . . . . . . . . . .
4
5
Sum rule for the subtraction function
. . . . . . . .
5
6
Wick rotation . . . . . . . . . . . . . . . . . . . . . .
5
7
Decomposition of the mass shift . . . . . . . . . . . .
6
8
Operator product expansion . . . . . . . . . . . . . .
6
9
Leading Wilson coeﬃcients
. . . . . . . . . . . . . .
7
10 Diﬀerence between proton and neutron . . . . . . . .
8
11 Perturbation theory
. . . . . . . . . . . . . . . . . .
8
12 Moments of the structure functions . . . . . . . . . .
9
13 Prediction for the constant C . . . . . . . . . . . . .
9
14 Renormalization
. . . . . . . . . . . . . . . . . . . .
10
15 Subleading divergence . . . . . . . . . . . . . . . . .
11
16 Input used for the structure functions
. . . . . . . .
11
17 Polarizabilities, ¯S(0) . . . . . . . . . . . . . . . . . .
13
18 Subtraction function at low Q2 . . . . . . . . . . . .
14
19 Intermediate values of Q2 . . . . . . . . . . . . . . .
14
20 Vector Meson Dominance
. . . . . . . . . . . . . . .
16
21 Asymptotics . . . . . . . . . . . . . . . . . . . . . . .
16
22 Numerical evaluation of the mass diﬀerence . . . . .
18
22.1 Form factors, mel . . . . . . . . . . . . . . . . .
18
22.2 Contribution from the subtraction function
. .
18
22.3 Contributions from the dispersion integrals
. .
18
22.4 Result for mQED and mQCD
. . . . . . . . . . .
18
23 Comparison with Lattice calculations . . . . . . . . .
19
24 Comparison with other evaluations of the Cotting-
ham formula
. . . . . . . . . . . . . . . . . . . . . .
19
24.1 Contributions from the elastic part . . . . . . .
20
24.2 Contributions from the subtraction function . .
20
25 Summary and conclusions . . . . . . . . . . . . . . .
21
A Form of the Wilson coeﬃcient for spin 2 . . . . . . .
23
B
Operator product expansion for free quarks . . . . .
24
C
Derivation of the sum rule . . . . . . . . . . . . . . .
25
1 Introduction
In the framework of the Standard Model, the fact that
proton and neutron have nearly the same mass is ex-
plained as consequence of an approximate symmetry:
isospin [1]. The symmetry is broken explicitly because
the two lightest quarks neither have the same charge nor
the same mass. The violation of the symmetry is very
weak, because the e.m. coupling e as well as the diﬀer-
ence between mu and md are small. The weak interac-
tion provides the neutron mass with an imaginary part
and generates a shift of the real part as well, but these
eﬀects are tiny and will be neglected. The Standard
Model then reduces to QED+QCD. In that framework,
the expansion of the mass diﬀerence between proton
and neutron in powers of e starts with
mp −mn = mQCD + mQED + O(e4) ,
(1)
where mQCD is what remains if e is turned oﬀand is
proportional to mu −md, while mQED stands for the
term of order e2. It is well-known that the splitting
of the physical masses into an electromagnetic and a
strong part is not unique. In our analysis, the ambiguity
2
shows up through the scale of the logarithm occurring
in the e.m. renormalization of the quark masses and
will be discussed in detail.
As shown by Cottingham [2], the leading contribu-
tion of the e.m. interaction to the mass of a particle
is given by an integral over the spin averaged forward
Compton scattering amplitude,
T µν(p, q) = i
2
Z
d4x eiq·x⟨p|T jµ(x)jν(0)|p⟩.
(2)
This amplitude is determined by QCD. If the mass of
a particle is expanded in powers of the e.m. coupling
constant e, the explicit expression for the term of order
e2 is formally given by1
mγ =
ie2
2m(2π)4
Z
d4q
1
q2 + iǫ T µ
µ(p, q) .
(3)
There are two problems with this formula: (i) The
short distance properties of QCD imply that the ampli-
tude T µ
µ(p, q) does not fall oﬀrapidly enough at large
values of q for the integral to converge. (ii) T µ
µ(p, q) does
not obey an unsubtracted dispersion relation – causality
alone determines the Compton amplitude through the
structure functions of lepton-nucleon scattering only up
to a subtraction function. The asymptotic behaviour in
the deep inelastic region is now fully understood on the
basis of asymptotic freedom, but the properties of the
subtraction function are still under debate.
Elitzur and Harari [3] pointed out that if the ex-
change of Reggeons correctly describes the asymptotic
behaviour in the limit ν →∞at ﬁxed q2 – an as-
sumption we refer to as Reggeon dominance – then the
subtraction function obeys a sum rule which fully de-
termines it through the cross section of lepton-nucleon
scattering. Their paper appeared in 1970, at a time
when the origin of the ∆I = 1 mass diﬀerences within
the isospin multiplets was totally mysterious: evalua-
tions of the Cottingham formula invariably led to the
conclusion that the proton should be heavier than the
neutron and hence unstable.
In 1975 Gasser and Leutwyler [4] then showed
that the mystery disappears if the popular conviction,
according to which the strong interaction conserves
isospin, is dismissed. They showed that a coherent pic-
ture of isospin breaking can be reached within the
Quark Model, provided the masses of the two lightest
quarks are not only very small but also very diﬀerent.
At that time, the experimental results on deep inelas-
tic scattering were consistent with the scaling laws of
1We ﬁx the normalization of the one-particle states with
⟨p′, s′|p, s⟩= 2p0(2π)3δ3(⃗p′ −⃗p)δs′s and m is the mass of the
particle. The spin averaged matrix element of the operator O
is abbreviated with ⟨p|O|p⟩≡1
2
P
s⟨p, s|O|p, s⟩.
Bjorken [5]. The implications of Reggeon dominance
were worked out in this framework, using models to
substitute the lack of experimental information in part
of phase space, with the result mQED = 0.7±0.3 MeV [4].
Lattice calculations of the proton-neutron mass dif-
ference are very demanding and became feasible only
in the 21st century. Early calculations were consistent
with the result obtained from the Cottingham formula,
but more recent evaluations indicate higher values for
mQED – we will compare the available results with the
outcome of our calculation in section 23.
In 2012, Walker-Loud, Carlson and Miller [6] per-
formed a new evaluation of the Cottingham formula.
They claimed that the analysis in [4] is inconsistent and
replaced our sum rule by a model where the subtrac-
tion function T1(0, q2) is parametrized with a simple
algebraic formula. This paper triggered renewed inter-
est and several authors investigated the matter [7–10].
We will discuss these works in section 24. A critical
examination of some of the claims made in [6] can be
found in appendix E of [11] and in [12,13].
The discovery of QCD and asymptotic freedom led
to a fully transparent picture for the properties of the
Compton amplitude in the region where both ν and q2
are large and where the divergence of the Cottingham
formula arises [14–17]. In Ref. [18], we showed that the
formal relation (3) can be rewritten in such a way that
the divergences are under full theoretical control, ex-
clusively concern the contribution from the subtraction
function and are absorbed in the e.m. renormalization
of quark masses and QCD coupling constant. The aim
of the present paper is to describe the analysis under-
lying these statements in detail.
The presentation is organized as follows. In a ﬁrst
part, sections 2–7, we discuss the mathematical un-
derpinnings: decomposition of the Compton amplitude,
dispersion relations, sum rule for the subtraction func-
tion, Wick rotation, mass formulae. The second part,
sections 8–13, deals with the operator product expan-
sion, which governs the behaviour of the amplitudes at
large momenta. The renormalization of the mass diﬀer-
ence is discussed in sections 14 and 15, whereas the data
concerning the structure functions used in our work and
the numerical determination of the subtraction function
and of the mass diﬀerence are described in sections 16–
22. Sections 23 and 24 compare the outcome of our
analysis with results obtained on the lattice and with
other recent evaluations of the Cottingham formula. A
summary and conclusions are provided in section 25.
The Appendices contain material concerning the oper-
ator product expansion as well as a detailed derivation
of the sum rule for the subtraction function that plays
a central role in the present work.
