---
doc_id: 5s032x
doc_title: "The standard model symmetry and qubit entanglement"
section_id: sec-007-three-qubits-and-the-octonionic-hopf-fibration
section_title: "Three Qubits and the Octonionic Hopf Fibration"
section_number: null
pages: 12-16
source_pdf: 5S032X.pdf
source_sha256: 17761383781f7bdc
doc_brief: "The standard model symmetry and qubit entanglement — quantum description."
---
Due to the normalization|o0|2 +|o1|2 = 1, an octonionic qubit defines a point on the sphere S15. There again exists
a map taking points of the sphere to the extended octonionic plane,
ho
1 : S15 −→ O∪{∞}
(o0,o 1) −→ o0o−1
1
, (36)
which can then be projected to S8 by means of
ho
2 : O∪{∞} −→ S8
o0o−1
1 −→ (xi)i=1...9
, (37)
once more with P9
i=1x2
i = 1. As before, this is just the map taking ( o0,o 1) to the ‘Bloch-vector’ coordinates,
h2◦h1 (o0,o 1) = (xi)i=1...9. (38)
This realizes S15 as an S7-fibration over an S8 base,
S15 S7
−→S8, (39)
and as in the previous case, the map reduces to a projection into the complex subspace of O in case the state is
separable into a single-qubit and two-qubit state. Hence, the base space S8 contains the (projective) state of one
qubit, along with entanglement degrees of freedom, while the fiber contains the state of the leftover two qubits.
C. Spin(9) and SU (3) × SU (2) × U(1)/Z6
As with the previous two sections, there exists a generalization of the connection between the spin-groups and Hopf
fibrations to the octonionic case. One can arrive at an analogous description of the group Spin(9) in terms of matrices
of the form given in Eq. (15), with Lc replaced by Lo, denoting left-multiplication by octonions. However, we can
also again simply note that the octonionic Hopf fibration can be equivalently given as [62]
S15 S7
−→S8≡ Spin(9)
Spin(7)
Spin(8)
Spin(7)
−→ Spin(9)
Spin(8). (40)
Then, one must find the subgroup of Spin(9) respecting a split O≃ C⊕ C3, that is, singling out an octonion
imaginary direction. It was shown by Dubois-Violette and Todorov [27] (see also [26, 63, 64]), and put into a more
explicit form by Krasnov [28], that this is just the gauge group of the Standard Model, SU (3)×SU (2)×U(1)/Z6.
We will not give the full argument here, and refer to the cited literature instead. However, as in the quaternionic
case, there is an intuitive way of viewing the group’s action on the base space of the Hopf fibration. Under the
split O≃ C⊕ C3, the coordinates xi split into two sets, {x1,x 2,x 9} from the singled-out complex subspace, and
{x3,x 4,x 5,x 6,x 7,x 8} from the additional octonionic complex directions (the entanglement degrees of freedom). Here,
13
the first set characterizes one qubit, while the second gives the entanglement with the other two. Thus, we must look
at the transformations that do not mix these sets.
As before, the triplet {x1,x 2,x 9} is acted on by rotations from SO(3)≃ SU (2). We now use the embedding of
U(1)×SU (3) into SU (4), given by
(α,g )−→

α−3 0
0 αg,

(41)
where α∈ U(1) and g∈ SU (3) [28]. With SU (4)≃ Spin(6), this then acts on the six remaining directions, as
required.
Finally, from the above embedding, one sees that the O2-spinor splits into two representations, with the single
factor of C being associated to an SU (3)-singlet of U(1)-charge−1, and the C3 associated to a SU (3) triplet of
U(1)-charge 1
3, both transforming as a doublet under SU (2) [28]. Consequently, the octonionic qubit can be seen
to contain precisely one generation of left-handed particles with the quantum numbers of the Standard Model, after
being split into a leptonic part from the factor C and a quark part from C3.
V. ENT ANGLEMENT AND MASSIVE P AR TICLES
The above has given us a way to interpret the degrees of freedom contained within a single octonionic qubit as
the left-handed part of one generation of the fermion content of the Standard Model, transforming under the gauge
symmetry SU (3)×SU (2)×U(1)/Z6 in the appropriate way, after singling out a complex direction and splitting O
into C⊕ C3.
However, some ambiguity still exists about the coordinates{x1,x 2,x 9}: if we view the octonionic spinor as spanning
the 9-dimensional heavenly sphere, these coordinates should be interpreted as the spatial coordinates upon dimensional
reduction by means of singling out a special complex direction; yet, they are acted upon by the SU (2)-part of the
Standard Model symmetry.
What comes to our aid is the observation that only half the particle content—the left-handed part—of the Standard
Model is subject to theSU (2)-symmetry: the Standard Model is a chiral theory. Hence, if we instead view{x1,x 2,x 9}
as spanning the 3-dimensional celestial sphere, only the U(1)×SU (3)-symmetry remains, and the O2-spinor models
a right-handed generation instead.
It then seems suggestive to move on to O4≃ C16, which is indeed large enough to accommodate a full generation
of Standard Model fermions.
But let us first step back and observe that, so far, we have only considered pure states. These, as discussed above,
give rise to light-like vectors (in 3 + 1, 5 + 1, and 9 + 1 dimensions respectively). Hence, these can, at best, model
massless particles propagating at the speed of light. However, we can appeal here to an observation due to Kiosses
[65] and Morikoshi [66]: while a pure density matrix will have a Bloch vector of norm 1, a mixed-state density matrix
defines a point at the interior of the Bloch sphere—and hence, in the correspondence above, a time-like direction
within the light-cone, in other words, the propagation of a massive particle.
Let us for the moment consider a single, unnormalized spinor
|ψ⟩ =

a
b

, (42)
such that a,b∈ C,|a|2 +|b|2 =k0. Its density matrix is
ρψ = 1
2

k0 +k3 k1−ik2
k1 +ik2 k0−k3

, (43)
which yields
det(ρ) =k2
0−k2
1−k2
2−k2
3 = 0. (44)
We can find a linearization of this equation of the form
 
k0−
3X
i=1
kiσi
!
|ψ⟩ = 0. (45)
Acting on this from the left with ⟨ψ| recovers Eq. 44. This has the form of a Weyl-equation in the momentum
representation; hence, we have renamed our coordinates xi→ki to illustrate this interpretation.
14
Explicitly, theki are:
k0 =|a|2 +|b|2
k1 =a∗b +b∗a
k2 =−i(a∗b−b∗a)
k3 =|a|2−|b|2
(46)
Now, consider again an entangled state of the form
|Ψ⟩ =a|00⟩ +b|01⟩ +c|10⟩ +d|11⟩, (47)
with⟨Ψ|Ψ⟩ = K0. We can compute the Ki by appealing to the 4 × 4-matrix representation of the quaternion Pauli
matrices
σq
1 =


0 0 1 0
0 0 0 1
1 0 0 0
0 1 0 0

, σ q
2 =


0 0 i 0
0 0 0 −i
−i 0 0 0
0 i 0 0

,
σq
3 =


0 0 0 1
0 0 −1 0
0 −1 0 0
1 0 0 0

, σ q
4 =


0 0 0 i
0 0 i 0
0 −i 0 0
−i 0 0 0

, (48)
σq
5 =


1 0 0 0
0 1 0 0
0 0 −1 0
0 0 0 −1

.
This yields the following:
K0 =⟨Ψ| Ψ⟩ =|a|2 +|b|2 +|c|2 +|d|2
K1 =⟨Ψ|σq
1|Ψ⟩ =a∗c +b∗d +c∗a +d∗b
K2 =⟨Ψ|σq
2|Ψ⟩ =i(a∗c−b∗d−c∗a +d∗b)
K3 =⟨Ψ|σq
3|Ψ⟩ =a∗d−b∗c−c∗b +d∗a
K4 =⟨Ψ|σq
4|Ψ⟩ =i(a∗d +b∗c−c∗b−d∗a)
K5 =⟨Ψ|σq
5|Ψ⟩ =|a|2 +|b|2−|c|2−|d|2
(49)
With these,|Ψ⟩ obeys the Weyl equation
 
K0−
5X
i=1
Kiσq
i
!
|Ψ⟩ = 0. (50)
Now let us introduce two (non-normalized) qubits
|ψA⟩ =

a
c

,
|ψB⟩ =

b
d

,
(51)
which combine into the four-component spinor
|ΨAB⟩ =|ψA⟩⊕| ψB⟩ =


a
c
b
d

. (52)
(Compare the action of SU (2)×U(1) in Eq. (31) and the resulting decomposition of the quaternionic spinor.) With
these, we see that the components K0, K1, K2 and K5 can be decomposed:
K0 =kA
0 +kB
0 =⟨ψA|ψA⟩ +⟨ψB|ψB⟩
K1 =kA
1 +kB
1 =⟨ψA|σ1|ψA⟩ +⟨ψB|σ1|ψB⟩
K2 =−kA
2 +kB
2 =−⟨ψA|σ2|ψA⟩ +⟨ψB|σ2|ψB⟩
K5 =kA
5 +kB
5 =⟨ψA|σ3|ψA⟩ +⟨ψB|σ3|ψB⟩
(53)
15
If now K3 =K4 = 0 (that is, the state is separable), this leads to two equations of the form of Eq. (45) for |ψA⟩ and
|ψB⟩.
Furthermore, we note that we can write
K3 +iK4 = 2(d∗a−b∗c)
=−2i⟨ψB|σ2|ψA⟩
K3−iK4 = 2(a∗d−c∗b)
= 2i⟨ψA|σ2|ψB⟩
(54)
which leads us to
K3 =−i⟨ψB|σ2|ψA⟩ +i⟨ψA|σ2|ψB⟩
K4 =−⟨ψB|σ2|ψA⟩−⟨ ψA|σ2|ψB⟩. (55)
Let us now make the replacement |ψA⟩→| ψ′
A⟩ =σ2|ψA⟩. This finally yields:
K0 =⟨ψ′
A|ψ′
A⟩ +⟨ψB|ψB⟩
K1 =−⟨ψ′
A|σ1|ψ′
A⟩ +⟨ψB|σ1|ψB⟩
K2 =−⟨ψ′
A|σ2|ψ′
A⟩ +⟨ψB|σ2|ψB⟩
K3 =−i⟨ψB|ψ′
A⟩ +i⟨ψ′
A|ψB⟩
K4 =−⟨ψB|ψ′
A⟩−⟨ ψ′
A|ψB⟩
K5 =−⟨ψ′
A|σ3|ψ′
A⟩ +⟨ψB|σ3|ψB⟩
(56)
We can then write Eq. (50) for |ΨAB⟩ in the following block matrix form

K012 +K1σ1 +K2σ2 +K5σ3 (K4−iK3)12
(K4 +iK3)12 K012−K1σ1−K2σ2−K5σ3

|ψ′
A⟩
|ψB⟩

= 0, (57)
If we now introduce
me±iϕ
2 =−K4∓iK3, (58)
we obtain,
(K0 +K1σ1 +K2σ2 +K5σ3)|ψ′
A⟩ =me−iϕ
2|ψB⟩,
(K0−K1σ1−K2σ2−K5σ3)|ψB⟩ =meiϕ
2|ψ′
A⟩, (59)
or, after multiplication of the first with eiϕ
2 [65],
(K0 +K1σ1 +K2σ2 +K5σ3)eiϕ
2|ψ′
A⟩ =m|ψB⟩,
(K0−K1σ1−K2σ2−K5σ3)|ψB⟩ =meiϕ
2|ψ′
A⟩, (60)
where we see that|ψA⟩ picks up a U(1) phase factor from the rotation through the circle m2 =K2
3 +K2
4 by an angle
ϕ. This, we recall, is the U(1) of the SU (2)×U(1)-subgroup of Spin(5) respecting the split H≃ C⊕ C. If we thus
want to keep this as a symmetry of the theory, we should require that it remains invariant under such transformations.
Consequently, we see that the symmetry preserving the split indeed acts as a gauge transformation.
This identification of the U(1) phase with electric charge is also made by Budinich [67], where the above equation
is interpreted as describing the proton and the neutron.
Absorbing the phase factor into our definition of|ψ′
A⟩, this can be brought into a more standard form by introducing
|Ψ′
AB⟩ =

|ψB⟩
|ψ′
A⟩

(61)
together with the matrices γi in the chiral representation
γ0 =

0 12
12 0

, γi =

0 σi
−σi 0

, (62)
which finally yields the Dirac equation
 4X
i=0
γipi−m
!
|Ψ′
AB⟩ = 0, (63)
16
where we have for ease of notation relabeledK5→p3, and otherwiseKi→pi. Note that, to recover K2
0−P
iK2
i = 0,
we must act on this from the left with
D
eΨ′
AB

 =|Ψ′
AB⟩†γ0.
Now introducing
γ5 =iγ0γ1γ2γ3 =

−12 0
0 12

(64)
and the left- and right-chiral projectors
PL = 1
2(14−γ5) =

12 0
0 0

,
PR = 1
2(14 +γ5) =

0 0
0 12

,
(65)
we identify the left- and right-chiral components, |ψL⟩ = PL|Ψ′
AB⟩ =|ψB⟩ and|ψR⟩ = PR|Ψ′
AB⟩ =|ψ′
A⟩. Hence,
the entangled two-qubit state can be interpreted as a left- and a right-handed spinor in 3 + 1 dimensions of mass m,
with m2 =K2
3 +K2
4 =K2
0−K2
1−K2
2−K2
5. For vanishing entanglement, we again obtain two separate instances of
S2, parametrizing two points, two lightrays on the celestial sphere in three dimensional space.
Consequently, we have two different interpretations of the two-qubit state: in the interpretation given in Sec. III,
we obtain the internal symmetries of a left-handed fermion generation (without color degrees of freedom, i. e.
SU (2)×U(1)/Z2), while the interpretation in this section yields the spatial degrees of freedom of a left- and a
right-handed fermion, together with the internal U(1) of the right-handed part.
Putting both together, then, yields all the right ingredients for a unified description of a full generation (again,
without the color symmetry). As H4≃ C8, this means that we need a three-qubit state, however, now interpreted in
terms of two copies of the construction referring to the quaternionic Hopf fibration.
This then suggests an extension of these observations to the octonionic case. The move from O2 to O4 is equivalent
to moving from a three-qubit to a four-qubit state. This gives rise to two copies of the octonionic Hopf fibration—
which may be motivated due to the fact that there is no fourth fibration, and thus, the construction as presented in
this paper finds its natural endpoint there.
As discussed in Sec. IV C, the coordinates after singling out a complex direction split into two sets,{K0,K 1,K 2,K 9}
and{K3,K 4,K 5,K 6,K 7,K 8} in the notation of this section, and with the norm K0 made explicit. These obey
K2
0−K2
1−K2
2−K2
9 =K2
3 +K2
4 +K2
5 +K2
6 +K2
7 +K2
8, (66)
where the right half (giving the ‘mass term’ as in Eq. (58)) is acted on by the SO(6) ≃ SU (4) into which the
SU (3)×U(1)-part of the Standard Model symmetry is embedded, as in Eq. (41). Thus, we see that the octonionic qubit
can be interpreted, analogously to the quaternionic one, as the left-handed part of one family of fermions transforming
under the full Standard Model symmetry SU (3)×SU (2)×U(1)/Z6, or as a right-handed part, together with the
energy-momentum four-vectors of the left- and right-handed fermion, transforming under the residual SU (3)×U(1)-
symmetry. Putting both together, then, seems well poised to yield the description of a full generation of fermions.
However, we leave the full formulation of the model for future work.
We note here that in this form, the model is also closely related to that proposed by Budinich [67].
