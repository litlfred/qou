---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-017-spherical-wall-and-radial-projection
section_title: "Spherical wall and radial projection"
section_number: null
pages: 32-36
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
Lüscher’s eﬀective range expansion is the appropriate method for low energy and zero angular mo-
mentum. Although nowadays there are extensions to higher partial waves and one could also improve
the predictability range by including higher terms in the eﬀective range expansion, we choose another
approach to describe two-particle scattering in a box. By imposing a spherical wall as a boundary
condition at r≈ RW in the cubic box, one can almost enforce spherical symmetry on the system and the
solutions will be standing waves which also cover a large range of momenta. As we have a localized
26
3.4 Scattering on the lattice
interaction, in the area between the interaction and the spherical wall the solution can be decomposed
into spherical harmonics using Eqs. (2.40) and (2.41),
[cosδl jl (qr)− sinδlnl (qr)] Yl,lz
(θ,φ ). (3.22)
Due to the inﬁnite spherical wall, the wave function must vanish for r = RW leading to the condition,
cos(δl
) jl
(qRW
) = sin(δl
) nl
(qRW
), (3.23)
which deﬁnes the phase shift,
δl = arctan
[ jl
(qRW
)
nl
(qRW
)
]
. (3.24)
This equation is exact in the continuum. Nevertheless, there is some ambiguity due to the ﬁnite distance
between lattice points making it necessary to ﬁne tune RW for each solution.
The upper equation is only valid for uncoupled channels like in the case of spin zero partial waves.
If there is a system of coupled channels, one has to include both channels simultaneously. A detailed
derivation of the expressions can be found in [61] and we brieﬂy summarize the results in the following.
As shown in Subsec. 2.2.2 we can rewrite the wave function in terms of an incoming and outgoing wave
function as well as the S-matrix. Imposing the spherical wall gives rise to two standing waves ΨI and ΨII
which are independent and which have the form
ΨI/II = 1
kI/II r

AI/II
j−1 sin
(
kI/II r− j−1
2 π + ∆I/II
j−1
)
AI/II
j+1 sin
(
kI/II r− j+1
2 π + ∆I/II
j+1
)
, (3.25)
with energies EI/II =⃗q (I/II )2/(2µ). The hard wall boundary condition is imposed by
− ∆ j±1 = qRW− j± 1
2 π. (3.26)
This is linked to the mixing angle by
tan
(
−∆I/II
j−1 +δ j−1
)
tan
(
−∆I/II
j+1 +δ j+1
)
= tan2 (
ϵ j
)
, (3.27)
AI/II
j−1 tan
(
ϵ j
)
=−AI/II
j+1
sin
(
−∆I/II
j+1 +δ j+1
)
sin
(
−∆I/II
j−1 +δ j−1
). (3.28)
For smallϵ j and for two solutions with qI≈ qII the former equations can be simpliﬁed and the mixing
angle is given as
ϵ j =
AI
j+1
AI
j−1
sin
(
δ j+1−δ j−1
)
, (3.29)
where the amplitudes AI
j±1 are calculated by the overlap of the standing wave and the corresponding
spherical harmonic close to the spherical wall.
This method only uses the binding energy as input for the phase shift calculation and some approxima-
tions are necessary particularly for the calculation of coupled channel phase shifts and mixing angles. In
[83] a new method was proposed. Generally speaking, one takes advantage of the wave function itself as
input and hence, one reduces the inevitable simpliﬁcations particularly for the mixing angle.
In order to calculate phase shifts with respect to their partial wave decomposition eﬃciently, we reverse
27
Chapter 3 Nuclear Lattice E ﬀective Field Theory
Nr. 1 2 3 4 5 ...
|⃗r| 0
√
2
√
3 2
√
5 ...
#|⃗r| 1 6 12 8 6 ...
Table 3.3: Radial projection and binning for the ﬁrst radii. The second line gives the value of the radii and the third
line gives the counting of points with the respective radius.
the ordering. While in the standard approach, one ﬁrst calculates the spectrum and then assigns each
solution to a partial wave, one could also ﬁrst project the system onto the respective (coupled) partial
wave and then solve the system. As the projection onto the partial waves only keeps the radial part of the
wave function, the system is much smaller than before, and the phase shift is directly ﬁtted to the radial
wave function. In the following we give details in the case of uncoupled as well as coupled channels.
The change from a three-dimensional basis to a radial one is made by binning all points with the same
radius R and total angular momentum as well as orbital angular momentum and spin according to the
partial wave. The respective projection operator reads
⏐⏐⏐R, j, jz, l, s
⟩
=
∑
|⃗R|=R,sz,lz
C j, jz
l,lz,s,sz
Yl,lz
( ˆR
)⏐⏐⏐⏐⃗R
⟩
⊗
⏐⏐⏐sz
⟩
, (3.30)
whereas C j, jz
l,lz,s,sz
are the usual Clebsch-Gordan coe ﬃcients. While the radial norm in the continuum
would be just proportional to r2, one has to count the number of points for every possible radius and
construct the norm according to the number of points. The ﬁrst number of points per radius are shown in
Tab. 3.3. The norm respecting the number of points per radius as well as the quantum number due to the
partial waves reads
N
j, jz
l,s (R) =
⟨
R, j, jz, l, s| R, j, jz, l, s
⟩
. (3.31)
The projection operator and the norm correction are applied to all operatorsO
(⃗R
)
resulting in,
O (R) j, jz
l,s =
[
N j, jz
l,s (R)
]− 1
2 ⟨
R, j, jz, l, s
⏐⏐⏐O
(⃗R
)⏐⏐⏐R, j, jz, l, s
⟩[
N j, jz
l,s (R)
]− 1
2
. (3.32)
After applying the projection operator to all operators, the eigensystem is solved e ﬃciently. The
eigenvalue corresponds to the energy of the system, and the eigenfunction is identiﬁed with a superposition
of Bessel functions outside of the interaction region for the speciﬁc partial wave of interest. Instead of
using Eqs. (2.40) and (3.24), we rewrite the respective function in terms of the Hankel functions h±
l ,
which are a linear combination of the former ones, and the constants A and B,
ψl (r)∝ Ah−
l (pr) + Bh+
l (pr). (3.33)
The explicit form of the Hankel functions are moved to App. A. These functions are identiﬁed as incoming
and outgoing wave functions linked to the S-matrix in Eq. (2.32). Then the phase shift is calculated from
B = S lA = exp(2iδl
) A. (3.34)
The procedure is shown schematically in Figs. 3.2 and 3.3. Firstly, a spherical wall is imposed at
RW, which generates standing waves. Secondly, all nodes with the same radius are binned together. The
interaction region is close to the origin in region I, while we calculate the phase shift from the wave
28
3.4 Scattering on the lattice
⃗R W
⃗R O
⃗R I
⃗ r a
Figure 3.2: Schematic sketch of the radial wall and spherical projection method. Left ﬁgure: The spherical wall
is introduced at|⃗RW|. In the case of radial projection, the wave function is measured at all lattice points ⃗r with
|⃗RI|<|⃗r|<|⃗RO|. Right ﬁgure: All lattice nodes and operators with the same radius are merged with respect to their
partial wave spherical harmonic [83].
0 5 1 01 52 02 53 0-4-3-2-101 
effective potential for          uncoupled channels 
V
J (r)  (MeV)r
 (fm)I
IIIIIR W RO RI 
Figure 3.3: Sketch of an example potential in spherical projection [83].
function in region II, which is bordered by RI and RO. Though this approach is straightforward for
uncoupled channels, it does not work in the coupled-channel system, which relates partial waves with
j = l± 1. This means that the coeﬃcients of Eqs. (3.33) and (3.34) are vector like, A = (A j−1, A j+1) and
B = (B j−1, B j+1). Correspondingly, one needs two independent solutions (Ψ j−1, Ψ j+1) to determine phase
shifts and mixing angles. In the previous case this was achieved by using diﬀerent solutions which have
approximately the same energy and neglect this diﬀerence. But this method is not applicable, because
the solutions of Eq. (2.31) have exactly the same energy and they are dependent on each other. By
introducing the Hermitian but time-reversal symmetry breaking auxiliary potential,
V→ V +
( 0 iVaux
−iVaux 0
)
, (3.35)
in region III of Fig. 3.2, the solutions decouple to ψ andψ∗ with the same energy and the conjugate
equation for the S-matrix determination reads
A∗ = S B∗. (3.36)
29
Chapter 3 Nuclear Lattice E ﬀective Field Theory
Rewriting the S-matrix in terms of A, B gives
S = [B A ∗][ A B ∗]−1. (3.37)
where S is deﬁned according to the Stapp parametrization of Eq. (2.53). Then again, the phase shifts as
well as the mixing angles are ﬁtted to Eq. (3.37).
In this thesis we calculate the nucleon-nucleon phase shift and mixing angle in the following manner.
At LO, we use the spherical projection method for the determination of phase shifts and mixing angles
while we use only the energy information for the perturbative inclusion of NLO and N2LO potentials in
the calculation of the phase shift. As we cannot solve the mixing angle perturbatively for higher orders,
we use again the spherical projection for these calculations.
