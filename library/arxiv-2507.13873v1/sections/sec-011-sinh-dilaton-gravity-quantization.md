---
doc_id: arxiv-2507.13873v1
doc_title: "Probing the singularity at the holographic screen via q-holography"
section_id: sec-011-sinh-dilaton-gravity-quantization
section_title: "Sinh dilaton gravity quantization"
section_number: null
pages: 31-34
source_pdf: 2507.13873v1.pdf
source_sha256: fa1d38d08dc4976a
toc_source: outline
doc_brief: "Probing the singularity at the holographic screen via q-holography — We study the emergence of q-deformed spacetime in a lower-dimensional gravitational system whose asymptotic region geometrizes the"
---
Sinh dilaton gravity quantization
In order to be self-contained, we follow here a more direct approach based on the canonical
phase space quantization of the theory, which will allow us to directly identify the boundary
dynamics and the associated symmetry algebra. A similar analysis was carried out for sine
dilaton gravity in [59, 60], so we will not repeat the full set of equations here, but rather
summarize the key steps leading to the derivation of the gravitational Hamiltonian for sinh
dilaton gravity.
The above formulation of the action (3.1) is convenient to directly take the JT limit as
b →0. Here it is convenient to rescale πb2Φ →Φ and take the latter to be Φ ∼1, such that
the whole action is multiplied by 1/b2, and the b parameter governs the semiclassical saddle
as ℏ∼b2:
S = −1
πb2
1
2
Z
M
d2x√g (ΦR + sinh(2Φ))+
I
∂M
dτ
√
h

ΦK −
r
cosh(2Φ) −1
2

. (B.18)
This leads to an effective rescaled dilaton potential V (Φ) →πb2V (Φ). The corresponding
rescaled energy and temperature can be deduced from the generic thermodynamic relations
E = cosh(2Φh)
4πb2
,
β =
4π
sinh(2Φh).
(B.19)
In performing canonical quantization of general dilaton gravities, an apparent difficulty
arises from the fact that there is no unique geodesic connecting two arbitrary boundary
points [102]. To address this, in our case it is more natural to consider geodesic distances
measured in a Weyl-rescaled geometry ds2
eff = ds2e−2Φ. Writing the metric in conformal
gauge as ds2 = ds2
flate2ρ, this effective metric
ds2
eff = ds2e−2Φ = ds2
flate2ρ−2Φ = ds2
flate2bφ,
(B.20)
30
corresponds to the one associated with the Liouville field φ in the original Liouville grav-
ity formulation. Indeed the Liouville equation admits AdS2 conformal factors as classical
solutions. This leads to an effective AdS2 black hole geometry in which the renormalized
geodesic length L between the two boundaries is well-defined:
L =
Z
geodesic
dseff =
Z
geodesic
dsflat ebφ.
(B.21)
A canonical transformation is then performed in phase space, replacing the original vari-
ables, namely the ADM energy EADM and its conjugate two-sided boundary time coordinate
T, with a new pair: the renormalized Einstein-Rosen bridge length L (B.21) and its conju-
gate momentum P. Specifically, one requires the canonical symplectic form in the original
coordinates to be of the form ω = dT ∧dEADM. Upon rescaling the coordinates to obtain
a nice saddle, we have
ω = dT ∧dEADM = sinh(2Φh)
2πb2
dT ∧dΦh =
1
2πb2dP ∧dL,
(B.22)
such that after quantization, πb2 takes the role of ℏ. One can easily prove that the canonical
transformations which ensure (B.22) are
L = 2 log
cosh (T sinh(2Φh)/4)
sinh(2Φh)

,
P = −log [cosh(2Φh) + sinh(2Φh) tanh (T sinh(2Φh)/4)] ,
(B.23)
where L is indeed the length of a Cauchy slice in a two-sided AdS2 black hole at the same
inverse temperature as the original sinh dilaton gravity black hole.
We now invert the relations (B.23) and express the gravity Hamiltonian (3.3) in terms
of the new phase space variables L and P, obtaining:
4πb2HADM = cosh(P) + e−LeP
2
.
(B.24)
A remarkable feature is that, by performing a Legendre transform of the Hamiltonian (B.24),
one obtains the action of the so-called q-Liouville system. The latter is part of a more
general theory, consisting of three coordinates xa = (L/2, β, γ) and three corresponding
momenta pa = (P, pβ, pβ), known as the q-Schwarzian [36, 35]. This six-dimensional phase
space reduces to the two-dimensional phase space of the system (B.24) upon imposing two
constraints, which were interpreted as Brown–Henneaux boundary conditions at the two
asymptotic boundaries of the two-sided gravitational system [36, 35]. The q-Schwarzian
system has classically 6 conserved charges which, upon quantization, satisfy two copies
of the SLq(2) algebra (A.20). In conclusion, by showing that the boundary dynamics of
31
Liouville gravity reduce to the constrained version (B.24) of the q-Schwarzian, which is
basically the simplest dynamical system encoding the desired symmetry algebra, we argue
that Liouville gravity may serve as a natural bulk gravitational dual capable of reproducing
the two-point function obtained in the main text.
All amplitudes in sinh dilaton gravity, and in particular the matter two-point function
we are interested in, can be obtained by quantizing the system (B.24). From the symplectic
form (B.22), the associated Poisson brackets {L, P} = 2πb2, become upon quantization
[L, P] = 2πib2ℏ. Setting ℏ≡1 by absorbing it in the definition πb2ℏ→πb2, we see that b2
effectively governs the semiclassical regime. By realizing the canonical commutation relation
by setting P = −2πib2 d
dL, the Schrödinger equation associated with the Hamiltonian (B.24)
becomes
ψs(L/2 + iπb2) +

1 + eiπb2e−L
ψs(L/2 −iπb2) = 2 cosh(2πbs)ψs(L/2),
(B.25)
where, for convenience, we have introduced a new energy variables Φh = πbs. The additional
factor e2πib2 is an order ambiguity in the quantization procedure. This difference equation
appeared before within the context of the relativistic Toda chain [91]. The solution to this
difference equation (B.25) is known and becomes unique once we require it to also satisfy the
dual equation obtained by the transformation b →1/b.14 This requirement is not manifest
at the level of the classical action, which is not invariant under this duality, but it emerges
in the structure of the quantum amplitudes of Liouville gravity [25, 27].15 The boundary-to-
boundary propagator of a matter scalar field in the bulk of sinh dilaton gravity is dual to the
insertion of the operator e−∆L in the q-Liouville path integral [36]. Once the gravitational
eigenfunctions are known, the matrix element of this operator between two fixed energy
states s1 and s2 can be computed, yielding:
Z +∞
−∞
dϕ ψs1(ϕ) ψ∗
s2(ϕ) e−2∆ϕ = Sb(b∆± is1 ± is2)
Sb(2b∆)
,
(B.27)
where the shorthand notation a ± b ± c indicates the product over all combinations of signs.
Taking the limit ∆→0 the expression above reduces to the orthogonality relation between
14For completeness, the solution is given by [91, 25, 27]
ψs(L/2) = e−isL/b
Z
C
dξ Sb(−iξ)Sb(−iξ −2is)e−πi(ξ2+2sξ)e−iξL/b,
(B.26)
where C denotes an appropriate integration contour.
15Liouville gravity has a quantum group theoretic description in terms of the modular double
Uq(sl(2, R)) ⊗U˜q(sl(2, R)) Hopf algebra [27, 103], building on the same structure present in 2d Liouville
CFT [98, 99].
32
the eigenfunctions, from which one can extract the Liouville gravity density of states:
ρ(s) = sinh(2πbs) sinh
2πs
b

.
(B.28)
These two ingredients form the fundamental building blocks of the Liouville gravity two-
point function (3.9) and the partition function (3.6).
C
