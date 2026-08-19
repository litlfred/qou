---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-009-basic-concepts-of-scattering-theory
section_title: "Basic concepts of scattering theory"
section_number: null
pages: 19-23
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
First of all, we give a basic introduction into scattering theory which follows [55, 56]. Starting point of
non-relativistic quantum mechanics is the corresponding Schrödinger equation, which has the subsequent
13
Chapter 2 Theory
form in the center-of-mass frame,
[
− 1
2µ∆ + V (⃗r)]
Ψ(⃗r) = EΨ(⃗r). (2.24)
µ is the reduced mass, V(⃗r ) is the interaction potential and E is the eigenenergy for the eigenfunction
Ψ(⃗r ). The dispersion relation between scattering energy and scattering momentum reads E =⃗q 2/(2µ).
In the standard approach, one assumes an incoming wave function Ψin in z-direction while the outgoing
wave function Ψout is a scattered spherical wave function. In the long-range limit, the potential vanishes
or its absolute value has to fall oﬀ faster than the centrifugal potential, namely r−2 with r =|⃗r|. Then the
asymptotic wave function can be described by the superposition,
Ψ(⃗r) r→∞
−→ exp (iqz) + f (θ,φ ) exp (iqr)
r . (2.25)
f (θ,φ ) is the scattering amplitude depending only on the anglesθ andφ. Due to the particular choice of
the incoming wave function, the momentum⃗q is given by⃗q = (0, 0, q) which simpliﬁes the calculations
and particularly the partial wave decomposition. But it is also possible to investigate the more general
case, where Ψ(⃗r ) must be replaced by Ψ(⃗q,⃗r ). Although it is theoretically possible to solve Eq. (2.24)
and impose the asymptotic boundary conditions of Eq. (2.25), one can also rewrite the ﬁrst equation
using Green’s function. The free Green’s function is given by
G
(
⃗r,⃗r′)
=− µ
2π
exp
(
iq|⃗r−⃗r′|
)
|⃗r−⃗r′| , (2.26)
and fulﬁlls the following equation
[ 1
2µ∆ + E + iϵ
]
G
(
⃗r−⃗r′)
=δ
(
⃗r−⃗r′)
. (2.27)
Using the Green’s function one transforms the diﬀerential equation in Eq. (2.24) into an integral equation
for the wave function, the so-called Lippmann-Schwinger equation,
Ψ(⃗r) = exp (iqz) +
∫
d⃗r′G
(
⃗r,⃗r′)
V
(
⃗r′)
Ψ
(
⃗r′)
. (2.28)
While in the latter equation one still uses the explicit wave function, one can also rewrite the problem in
terms of operators only. Therefore, we deﬁne the general T-matrix
Tβα(E′, E) =
⟨
Ψ0
(
E′,β
)⏐⏐⏐⏐ Vint
⏐⏐⏐⏐Ψ
(
E,α
)⟩
, (2.29)
whereα,β are quantum numbers of the system, Vint the interaction potential and Ψ0(E′,β ) is a solution
of the free system with energy E′ and quantum numberβ. Furthermore, Ψ is a solution of the Lippmann-
Schwinger equation according to Eq. (2.28) with energy E and quantum numberα. Using the deﬁnition
of the Green’s function, we write the equivalent Lippmann-Schwinger equation for the T-matrix,
T(E) = Vint + VintG(E)T(E), (2.30)
whereas T(E) is the on-shell version of Eq. (2.29) and G(E) the on-shell version of the Green’s function
in momentum space with E = E′.
14
2.2 Scattering Theory
Most generally, a scattering state is described by the propagation of the incoming state through the
interaction represented by the S-matrix,
Ψout(E) = S Ψin(E). (2.31)
Alternatively, the S-matrix is given as the overlap of two free state solutions,
⟨
Ψ0
(
Eβ,β
)⏐⏐⏐⏐ S
⏐⏐⏐⏐Ψ0
(
Eα,α
)⟩
, (2.32)
already indicating that one can still use free state solutions as basis states and think about a superposition
of such states for the scattering solution. As the scattering matrix should be the unit matrix in the case of
vanishing scattering potential, it is convenient to split the matrix into two terms,
⟨
Ψ0
(
Eβ,β
)⏐⏐⏐⏐ S
⏐⏐⏐⏐Ψ0
(
Eα,α
)⟩
=
⟨
Ψ0
(
Eβ,β
)⏐⏐⏐⏐ Ψ0
(
Eα,α
)⟩
|                        {z                        }
=δα,β
−2πiδ
(
Eα− Eβ
)
Tβα
(
Eα, Eβ
)
. (2.33)
The ﬁrst term is related to the amplitude, where the particle passes the interaction region without scattering
whereas the second term includes all scattering information.
In the case of radially symmetric potentials, one can decompose the problem into solutions according
to the spherical harmonics. Spherical harmonics are a system of eigenfunctions, which are deﬁned on the
sphere and which correspond to eigenfunctions of the angular momentum operator,
ˆL2Yl,lz
(θ,φ ) = l(l + 1)Yl,lz
(θ,φ ), (2.34)
ˆLzYl,lz
(θ,φ ) = lzYl,lz
(θ,φ ), (2.35)
with the orbital angular momentum quantum numberl = 0, 1, 2,... and the magnetic momentum quantum
number lz =−l,−l + 1,..., l. Such a system generates an inﬁnite basis of eigenfunctions and any solution
of the Schrödinger equation can be identiﬁed with the good quantum numbers l, lz. Details on the
properties and construction of the spherical harmonics Yl,lz are found in App. A. On the one hand, the
decomposition into partial waves already facilitates the problem as the degrees of freedom are reduced
to the radial one. On the other hand, it also introduces a reasonable hierarchy of partial waves as the
lowest-lying partial waves are the most important ones for scattering processes while higher order partial
waves hardly contribute to the full scattering wave. The reason is that the angular momentum contribution
to the kinetic part l(l + 1)/(2µr2) rises with higher angular momentum and serves as a barrier between
the incoming particle and the interaction region such that any interaction is more and more suppressed
with larger l.
To be speciﬁc, the wave function is divided into a radial part and a spherical part by the ansatz
Ψ(⃗r) =
∑
l
ul (r)
r Pl (cosθ), (2.36)
where the system is chosen such that only the spherical harmonics with m = 0 contribute whereas
Pl(cosθ) are the Legendre polynomials. Furthermore, ul is the solution of the radial part,
− 1
2µ∆r + l(l + 1)
2µr2 + V(r)
 ul(r) = Eul(r). (2.37)
The free system with V(r) = 0 has two independent solutions, which consist of the Bessel functions of
15
Chapter 2 Theory
the ﬁrst and second kind, jl(qr) and nl(qr),
us
l (qr) = (qr) jl(qr), (2.38)
uc
l (qr) = (qr)nl(qr). (2.39)
As the solutions are ∝ sin(qr− lπ/2) and∝− cos(qr− lπ/2) for large (qr), the real solution can be
approximated by a superposition of the two free solutions, leading to
ul(r)
r→∞
−−−−→A sin
(
qr− lπ
2
)
− B cos
(
qr− lπ
2
) r→∞
−−−−→sin
(
qr− lπ
2 +δl
)
. (2.40)
δl is the phase shift and it can be read oﬀ from the coeﬃcients A, B immediately by
tanδl = B
A. (2.41)
Alternatively, one expands the incoming partial wave of Eq. (2.25), rearranges the solution and uses
Eq. (2.41) to get the form
ul(r)→ 2l + 1
2q i2l+1 [
exp(−iqr)− (−1)l exp(2iδl) exp(+iqr)
]
. (2.42)
Due to the orthogonality of the spherical harmonics, one can not only separate the contributions of the
wave function according to their angular momentum, but also the Lippmann-Schwinger equation as well
as the scattering matrix S l themselves. For example, the S-matrix for angular momentum l reads
S l = exp(2iδl
). (2.43)
Then the full scattering matrix S is given by the sum S = ∑
l S l. In the former Eqs. (2.38) to (2.40)
we see that momentum q and position r always appear as a pair (qr) and one could think about the
very low-energy limit of the equations. The Wronskian method uses the asymptotic wave function
of Eq. (2.40) with and without interaction at zero momentum approximation and gives the following
equation,
q2l+1 cot(δl) =− 1
as
+ re
2 q2 +O(q4), (2.44)
with as the scattering length and re the eﬀective range. The term on the left can be analytically expanded
around zero-momentum as the phase shift is δl∝ q2l+1 for q→ 0. It can be shown that the scattering
length is the zero of the asymptotic wave function in the zero-energy limit. In the case of repulsive or
only weakly attractive potentials, the scattering length and the eﬀective range are indeed approximately
in the range of the potential. The eﬀective range expansion can be linked to the scattering matrix,
S l = exp(2iδl) = 1 + 2iq2l+1 1
q2l+1 cot(δl
)− iq2l+1, (2.45)
and the projected scattering amplitude
fl = (2l + 1)q2l
q2l+1 cotl (δ)− iq2l+1, (2.46)
whereas fl is given by f (θ) = ∑
l flPl(cosθ). Bound states appear as poles in the scattering amplitude
16
2.2 Scattering Theory
of Eq. (2.46) and due to the eﬀective range expansion, the leading-order approximation of the binding
energy in terms of the scattering length is given by
EB = 1
2µa2
s
. (2.47)
Though the eﬀective range expansion is very well established only for S waves, we have shown the
general form for arbitrary angular momentum in three dimension and it can be further generalized for
arbitrary dimension as well. Details on the method can be found in [57] and references therein.
