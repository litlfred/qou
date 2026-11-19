---
doc_id: arxiv-1506.06747v3
doc_title: "Cottingham formula and nucleon polarizabilities"
section_id: sec-033-b3-low-energy-expansion
section_title: "B.3 Low-energy expansion"
section_number: null
pages: 22-23
source_pdf: 1506.06747v3.pdf
source_sha256: c44709743db78865
toc_source: outline
doc_brief: "Cottingham formula and nucleon polarizabilities — The diﬀerence between the electromagnetic self-energies of proton and neutron can be calculated with the Cottingham formula, which expresses the"
---
The elastic intermediate states generate poles in T µν.
In the Mandelstam variables the poles are located at
10If the time-ordered product of the currents is replaced by
the retarded current commutator, crossing symmetry instead
relates the amplitude to its complex conjugate [15].
s = m2 and u = m2. We refer to these contributions as
Born terms and denote them by T µν
B ,
T µν = T µν
B + ¯T
µν .
(B.23)
The decomposition is not unique [38, 40, 102]. The es-
sential property of the Born terms is that they account
for the elastic singularities. This ensures that the re-
mainder, ¯T
µν, is regular at qi = qf = 0 and can thus
be expanded in a Taylor series in powers of the photon
momenta and energies, which the low-energy expansion
treats as small. The construction described below leads
to Born terms that are conserved, so that this also holds
for the remainder:11
qf
µ ¯T
µν = qi
ν ¯T
µν = 0 .
(B.24)
Keeping P ≡1
2(pi+pf) ﬁxed, momentum conserva-
tion determines the initial and ﬁnal nucleon momenta
in terms of the photon variables qi, qf. However, un-
less P vanishes, energy conservation leads to a nonlin-
ear constraint on the photon energies, so that it is not
consistent to treat all of these as quantities of O(q).
The problem disappears for P = 0, i.e. in the Breit
frame: energy conservation then implies ωi = ωf = ω,
so that the kinematics is unambiguously determined by
the independent variables ω, qi, qf, which all count as
quantities of O(q). This is why the Breit frame is the
preferred frame of reference for the low-energy expan-
sion. For real Compton scattering, a transparent dis-
cussion of this issue is given in [113].
In the Breit frame, the Taylor series in powers of
the variables ω, qi, qf takes the form:
¯T
µν = ¯T
µν
0
+ ¯T
µν
1
+ ¯T
µν
2
+ . . .
with
¯T
µν
n = O(qn) .
(B.25)
The symmetry (B.22) implies that the even terms of the
series ¯T
µν
0 , ¯T
µν
2 , . . . are proportional to the unit matrix
in spin space, while the odd terms ¯T
µν
1 , ¯T
µν
3 , . . . exclu-
sively contain spin-dependent terms and do not con-
tribute to the spin average.
11In general, it is not a trivial matter to impose current con-
servation on the Born terms. If one for instance evaluates the
one-particle singularities in the space components T ab
B and
determines the remaining components of T µν
B by solving the
constraints qf
µ T µν
B
= qi
ν T µν
B
= 0, one in general arrives at
a representation for the Born terms that contains kinematic
singularities. The presence of kinematic singularities in the
Born terms complicates the analysis because the remainder
¯
T µν is then not regular at qi = qf = 0. Compton scattering
on the pion illustrates the problem: the one-particle singular-
ities do not generate a term proportional to gµν, but unless a
regular term of this type is allowed for, the representation of
the Born terms can be consistent with current conservation
only if it contains kinematic singularities.
23
We now turn to the consequences of Lorentz invari-
ance for the low-energy expansion. If the photon ener-
gies and momenta are small of O(q), the momentum
transferred to the nucleon is small as well. We thus
only need to consider Lorentz frames where the nucleon
momenta are also small of O(q). The standard choices
(Laboratory, centre-of-mass system, Breit frame) all be-
long to this category. If a Lorentz transformation Λ is
to connect two such frames, then the relative velocity
must be small, so that the standard decomposition into
a boost and a rotation, Λ = BR only involves a small
boost. Hence it suﬃces to analyze the transformation
properties under rotations and under small boosts.
The behaviour under rotations is trivial, because the
corresponding Wigner rotations in the initial and ﬁnal
states are identical, W(R, pi) = W(R, pf) = R. Hence
they leave the spin-independent part of the amplitude
alone and transform the matrices σ = {σ1, σ2, σ3} oc-
curring in the spin-dependent part like a vector.
To analyze the properties of small boosts, the
SL(2, C) representation of the Lorentz group is more
convenient than the one acting on the coordinates and
momenta. Consider the matrix B = exp( 1
2v · σ) ∈
SL(2, C), which represents a pure Lorentz transforma-
tion with a small velocity v = O(q). The product of
two such boosts is given by BB′ = 1 + 1
2w · σ + 1
8w2 +
i
4(v × v′) · σ + O(q3), with w = v + v′. At O(q), this
is a pure Lorentz transformation,12 but at O(q2), the
product in addition contains a small Wigner rotation:
W = 1 + i
4(v × v′) · σ + O(q4).
The essential point here is that, for the pure Lorentz
transformation needed to remove the relative velocity of
the two systems, the Wigner rotations generated in the
initial and ﬁnal states are at most of order q2. Accord-
ingly, the Lorentz invariance condition (B.18) implies
that, if Λ is a boost that only generates velocities of
O(q), the individual terms of the low-energy expansion
transform like ordinary tensors – up to higher order
corrections:
Bµ
αBν
β ¯T
αβ
n (pf, qf|pi, qi) = ¯T
µν
n (Bpf, Bqf|Bpi, Bqi)
+ O(qn+2) .
(B.26)
The corrections only matter if the expansion is taken
beyond next-to-leading order. In particular, the lead-
ing even term of the series is proportional to the unit
matrix in spin space even if the reference system is not
identiﬁed with the Breit frame.
12The fact that the velocity addition is modiﬁed only shows
up at O(q3).
