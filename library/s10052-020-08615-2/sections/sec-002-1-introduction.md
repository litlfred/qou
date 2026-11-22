---
doc_id: s10052-020-08615-2
doc_title: "Sum rule for the Compton amplitude and implications for the proton–neutron mass difference"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: s10052-020-08615-2.pdf
source_sha256: 23becb0b1a2e7f1b
toc_source: outline
doc_brief: "Sum rule for the Compton amplitude and implications for the proton–neutron mass difference — The Cottingham formula expresses the leading contribution of the electromagnetic interaction to the"
---
Introduction . . . . . . . . . . . . . . . . . . . . .
1
2
Lorentz invariance, kinematic zeros
. . . . . . . .
3
3
Dispersion relations . . . . . . . . . . . . . . . . .
3
4
Reggeon dominance . . . . . . . . . . . . . . . . .
4
5
Sum rule for the subtraction function . . . . . . . .
5
6
Wick rotation . . . . . . . . . . . . . . . . . . . .
5
7
Decomposition of the mass shift . . . . . . . . . .
6
8
Operator product expansion . . . . . . . . . . . . .
6
9
Leading Wilson coefﬁcients
. . . . . . . . . . . .
7
10 Difference between proton and neutron . . . . . . .
8
11 Perturbation theory . . . . . . . . . . . . . . . . .
8
12 Moments of the structure functions . . . . . . . . .
9
13 Prediction for the constant C . . . . . . . . . . . . 10
14 Renormalization . . . . . . . . . . . . . . . . . . . 10
15 Subleading divergence
. . . . . . . . . . . . . . . 11
16 Input used for the structure functions . . . . . . . . 11
17 Polarizabilities, ¯S(0)
. . . . . . . . . . . . . . . . 12
18 Subtraction function at low Q2 . . . . . . . . . . . 13
19 Intermediate values of Q2
. . . . . . . . . . . . . 14
20 Vector meson dominance . . . . . . . . . . . . . . 15
a e-mail: rusetsky@hiskp.uni-bonn.de (corresponding author)
21 Asymptotics . . . . . . . . . . . . . . . . . . . . . 16
22 Numerical evaluation of the mass difference . . . . 17
22.1 Form factors, mel
. . . . . . . . . . . . . . . 17
22.2 Contribution from the subtraction function . . 18
22.3 Contributions from the dispersion integrals . . 18
22.4 Result for mQED and mQCD . . . . . . . . . . 18
23 Comparison with Lattice calculations
. . . . . . . 18
24 Comparison with other evaluations of the Cotting-
ham formula . . . . . . . . . . . . . . . . . . . . . 19
24.1 Contributions from the elastic part . . . . . . 19
24.2 Contributions from the subtraction function
. 20
25 Summary and conclusions
. . . . . . . . . . . . . 21
Appendix A: Form of the Wilson coefﬁcient for spin 2
23
Appendix B: Operator product expansion for free quarks 23
Appendix C: Derivation of the sum rule
. . . . . . . . 24
References . . . . . . . . . . . . . . . . . . . . . . . . 25
1 Introduction
In the framework of the Standard Model, the fact that pro-
ton and neutron have nearly the same mass is explained as
consequence of an approximate symmetry: isospin [1]. The
symmetry is broken explicitly because the two lightest quarks
neither have the same charge nor the same mass. The viola-
tion of the symmetry is very weak, because the e.m. coupling
e as well as the difference between mu and md are small. The
weak interaction provides the neutron mass with an imagi-
nary part and generates a shift of the real part as well, but
these effects are tiny and will be neglected. The Standard
Model then reduces to QED + QCD. In that framework, the
expansion of the mass difference between proton and neutron
in powers of e starts with
m p −mn = mQCD + mQED + O(e4),
(1)
123
where mQCD is what remains if e is turned off and is propor-
tional to mu −md, while mQED stands for the term of order
e2. It is well-known that the splitting of the physical masses
into an electromagnetic and a strong part is not unique. In
our analysis, the ambiguity shows up through the scale of the
logarithm occurring in the e.m. renormalization of the quark
masses and will be discussed in detail.
As shown by Cottingham [2], the leading contribution of
the e.m. interaction to the mass of a particle is given by an
integral over the spin averaged forward Compton scattering
amplitude,
T μν(p, q) = i
2

d4x eiq·x⟨p|T jμ(x) jν(0)|p⟩.
(2)
This amplitude is determined by QCD. If the mass of a par-
ticle is expanded in powers of the e.m. coupling constant e,
the explicit expression for the term of order e2 is formally
given by1
mγ =
ie2
2m(2π)4

d4q
1
q2 + iϵ T μ
μ(p, q).
(3)
There are two problems with this formula: (i) The
short distance properties of QCD imply that the amplitude
T μ
μ(p, q) does not fall off rapidly enough at large values of
q for the integral to converge. (ii) T μ
μ(p, q) does not obey an
unsubtracted dispersion relation – causality alone determines
the Compton amplitude through the structure functions of
lepton-nucleon scattering only up to a subtraction function.
The asymptotic behaviour in the deep inelastic region is now
fully understood on the basis of asymptotic freedom, but the
properties of the subtraction function are still under debate.
Elitzur and Harari [3] pointed out that if the exchange of
Reggeons correctly describes the asymptotic behaviour in
the limit ν →∞at ﬁxed q2 – an assumption we refer to
as Reggeon dominance – then the subtraction function obeys
a sum rule which fully determines it through the cross sec-
tion of lepton-nucleon scattering. Their paper appeared in
1970, at a time when the origin of the ΔI = 1 mass differ-
ences within the isospin multiplets was totally mysterious:
evaluations of the Cottingham formula invariably led to the
conclusion that the proton should be heavier than the neutron
and hence unstable.
Gasser and Leutwyler [4] then showed that the mystery
disappears if the popular conviction, according to which
the strong interaction conserves isospin, is dismissed. They
showed that a coherent picture of isospin breaking can be
reached within the Quark Model, provided the masses of the
two lightest quarks are not only very small but also very dif-
ferent. At that time, the experimental results on deep inelastic
1 We ﬁx the normalization of the one-particle states with ⟨p′, s′|p, s⟩=
2p0(2π)3δ3(p′ −p)δs′s and m is the mass of the particle. The spin aver-
aged matrix element of the operator O is abbreviated with ⟨p|O|p⟩≡
1
2

s⟨p, s|O|p, s⟩.
scattering were consistent with the scaling laws of Bjorken
[5]. The implications of Reggeon dominance were worked
out in this framework, using models to substitute the lack
of experimental information in part of phase space, with the
result mQED = 0.7 ± 0.3 MeV [4].
Lattice calculations of the proton–neutron mass difference
are very demanding and became feasible only in the 21st
century. Early calculations were consistent with the result
obtained from the Cottingham formula, but more recent eval-
uations indicate higher values for mQED – we will compare
the available results with the outcome of our calculation in
Sect. 23.
Walker-Loud et al. [6] performed a new evaluation of the
Cottingham formula. They claimed that the analysis in [4] is
inconsistent and replaced our sum rule by a model where the
subtraction function T1(0, q2) is parametrized with a simple
algebraic formula. This paper triggered renewed interest and
several authors investigated the matter [7–10]. We will dis-
cuss these works in Sect. 24. A critical examination of some
of the claims made in [6] can be found in appendix E of [11]
and in [12,13].
The discovery of QCD and asymptotic freedom led to a
fully transparent picture for the properties of the Compton
amplitude in the region where both ν and q2 are large and
where the divergence of the Cottingham formula arises [14–
17]. In Ref. [18], we showed that the formal relation (3) can
be rewritten in such a way that the divergences are under full
theoreticalcontrol,exclusivelyconcernthecontributionfrom
the subtraction function and are absorbed in the e.m. renor-
malization of quark masses and QCD coupling constant. The
aim of the present paper is to describe the analysis underlying
these statements in detail.
The presentation is organized as follows. In a ﬁrst part,
Sects. 2–7, we discuss the mathematical underpinnings:
decomposition of the Compton amplitude, dispersion rela-
tions, sum rule for the subtraction function, Wick rotation,
mass formulae. The second part, Sects. 8–13, deals with the
operator product expansion, which governs the behaviour of
the amplitudes at large momenta. The renormalization of the
mass difference is discussed in Sects. 14 and 15, whereas the
data concerning the structure functions used in our work and
the numerical determination of the subtraction function and
of the mass difference are described in Sects. 16–22. Sections
23 and 24 compare the outcome of our analysis with results
obtained on the lattice and with other recent evaluations of
the Cottingham formula. A summary and conclusions are
provided in Sect. 25. The Appendices contain material con-
cerning the operator product expansion as well as a detailed
derivation of the sum rule for the subtraction function that
plays a central role in the present work.
123
