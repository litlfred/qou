---
doc_id: arxiv-1112.5179v1
doc_title: "Prepared for submission to JHEP 3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA "
section_id: sec-017-53-non-abelian-line-defects
section_title: "Non-abelian line defects"
section_number: 5.3
pages: 52-62
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA 2Trinity College, Cambridge CB2 1TQ, UK — We"
---
There are natural ways to use the three-dimensional theoriesTM to deﬁne domain walls in the
UV for four-dimensionalN = 2SU (2) gauge theories. A full account of that construction will
be the subject of a future publication [61]. For now, we will content ourselves with sketching
some interesting directions of inquiry. For simplicity, we will focus on the example of SU (2)
N = 2∗ SYM.
We would like to establish a very concrete parallel between the general structure of
Pestun’sS4 partition function and the reﬁned index. In the presence of line defects or domain
29Furthermore,Ihyper =IYI ˜Y , while obvious, can be given a neat interpretation: in order to describe a
hypermultiplet on the whole space, one can start with Dirichlet boundary conditions on ˜Y for a half-space,
and Dirichlet boundary conditions on Y for the second half-space, and “glue” them together by a Y− ˜Y+ 3d
superpotential integrated over the equator. Here Y− and ˜Y+ denote the boundary values of Y and ˜Y from
the two sides. This “gluing” prescription is akin to the idea that a gauge theory on the full space can be
reconstructed from the gauge theory on two half-spaces with Dirichler boundary conditions by gauging the
diagonal ﬂavor symmetry at the boundary
– 51 –
walls at the equator, localization reduces Pestun’s partition function to a matrix element of
a self-adjoint operator [36–38]
⟨ZS| ˆO|ZN⟩≡
∫
dν(a′)dν(a) ¯Zinst(a′)O(a′,a )Zinst(a) (5.16)
Here Zinst(a) is the instanton partition function (together with the tree-level contribution)
for the gauge theory, which is naturally thought of as a wavefunction, |ZN⟩ = Zinst(a), and
⟨ZS| is the complex conjugate; dν(a) is the one-loop integration measure, and O(a′,a ) is an
integration kernel that encodes the eﬀect of the domain wall or line defect. For domain walls,
O(a′,a ) is basically the S3 partition function of the domain wall 3d degrees of freedom. For
’tHooft-Wilson line defects L,O(a,a′) is a sum over delta functions, so that ˆO takes the form
of a sum over shift operators
ˆOL =
∑
n
Rn(a)e2πn∂a (5.17)
The functions Rn(a) can in principle be computed from the geometry of monopole moduli
spaces, as they account for “bubbling monopole” conﬁgurations near the line defect [69] that
interpolate between the “bare” ’tHooft monopole magnetic ﬂux and an Abelian magnetic ﬂux
n/2.
A simple way to understand the physical meaning of the matrix element is to realize
the conﬁguration starting from two hemispheres with Dirichlet boundary conditions for the
gauge ﬁelds, and then glue together the hemispheres, along with any extra degrees of freedom
at the equator, by gauging appropriate 3d ﬂavor symmetries. In particular, it is natural to
see the wavefunction|ZN⟩ as the partition function on a hemisphere with Dirichlet boundary
conditions. Notice that the notion of Dirichlet boundary condition is not S-duality invariant,
but depends on a choice of weakly coupled duality frame. Hence |ZN⟩ transforms in inter-
esting ways under S-duality, while the S4 partition function⟨ZS|ZN⟩ is S-duality invariant.
Incidentally, in the gluing procedure one also has to pick adequate boundary conditions for
the hypers, as discussed before. Diﬀerent choices split the one-loop measure in diﬀerent way
among North and South hemisphere, and change the normalization of the wavefunctions.
In the context of AGT [35], the wavefunctions are identiﬁed with BPZ conformal blocks,
and the matrix elements with 2d CFT correlation functions. The operators OL coincide with
the so-called Verlinde line operators, or with topological defects in the 2d CFT. Crucially,
they can be computed explicitly through a laborious algorithm [36, 37], sidestepping the
diﬃcult localization calculations of gauge theory. The whole structure described above can
be deformed to generic b, though the corresponding deformation S4
b of the S4 geometry has
not been described yet. We will need the generalized formulae in the following. The simplest
’tHooft-Wilson loop for N = 2∗ SYM is the operator of magnetic charge 1 and electric
charges,
ˆO1,s = sinπb(2a−Q−µ)
sinπb(2a−Q) eiπb(2a−Q)s−b
2∂a + sinπb(2a−Q +µ)
sinπb(2a−Q) e−iπb(2a−Q)s+b
2∂a. (5.18)
– 52 –
It is self-adjoint against the standard Liouville measure dν(a) = sinπb(2a−Q) sinπ/b(2a−
Q)da, as long as the mass parameter µ lies in the physical line Q/2 +iR. Notice that the
ﬁrst factor in the measure cancels against the denominators in ˆO1,s and the second factor
in the measure commutes with the shift operators. The opposite is true for a second family
of operators, obtained from ˆO1,s by b→ b−1. The operator is explicitly symmetric under
a→ Q−a but not under µ→ Q−µ, due to an asymmetric split of the one-loop factors
between North and South hemispheres. The symmetry µ→ Q−µ can be implemented by
conjugation by an appropriate rescaling factor.
In order to set up our analogy, we can break down the calculation of the index of a 4d
theory, possibly in the presence of a domain wall on the equator of the S3 or of line defects,
by ﬁrst deﬁning a “half-index” IIm(q,ζ, Γ) as the index of the 4d gauge theory on half of S3
with Dirichlet boundary conditions. This will be a function of the fugacities and magnetic
ﬂuxes ζ,m associated to the 3d ﬂavor symmetries and of the choice of S-duality frame Γ.
The full index of the 4d theory can be recovered by combining the half-indices for the two
hemispheres with the measure for a three-dimensional non-abelian gauge theory:
(IIS|IIN)≡
∑
m
∮ dζ
2πiζ ∆m(ζ)IIm(q,ζ,N )IIm(q,ζ,S ). (5.19)
In the absence of ’tHooft operators in the bulk, we expect IIm(q,ζ, Γ) to be non-zero only at
m = 0. The measure ∆ 0(ζ) is the usual Vandermonde measure. In the presence of ’tHooft
loops, we will have contributions at non-zero (possibly half-integral) m and we will ﬁnd a
natural generalization of the measure,
∆m(ζ) = 1
2(qm/2ζ−q−m/2ζ−1)(q−m/2ζ−qm/2ζ−1). (5.20)
How can we add ’tHooft operators to the half-index? The hard way would be to do a
careful localization computation, taking into account bubbling monopole contributions that
screen the magnetic charge at the pole, giving a variety of possible Abelian ﬂuxes m at the
equator. But there is a shortcut. We can try to borrow the calculation of Rn(a) from the
Verlinde loop operators. Notice that if we assume the existence of a dictionary, these are
very constrained. Namely, the OPE of line defects and the Ward identities satisﬁed when
they are brought to collide with domain walls must take the same form for the S4
b partition
function and for the index, upon the dictionary established in the rest of this paper between
vector-multiplet vevs and fugacities, and 2πib2→ ℏ. In particular, we will map
eiπb(2a−Q)→ ˆx+ =qm/2ζ e b∂a→ ˆp+ =e∂m+ ℏ
2∂logζ eiπb(2m−Q)→η (5.21)
We can replace (ˆx+, ˆp+) with (ˆx−, ˆp−) for operators acting from the opposite side of the
equator.
We are led to conjecture that the half-index in the presence of a ’tHooft-Wilson loop L
can be computed by acting on the half-index in the absence of the loop with the image of
– 53 –
ˆOL under the above dictionary. Let’s consider a concrete example. The 4d index of SU (2)
N = 2∗ is
I(η,q ) =
∮ dζ
4πiζ (1−ζ2)(1−ζ−2) (5.22)
×
∞∏
n=0
(
1−qn+1)2(
1− qn+1
ζ2
)2(
1−ζ2qn+1)2
(
1−η−1qn+ 1
2
)(
1−ηqn+ 1
2
)(
1− qn+ 1
2
ηζ2
)(
1− ηqn+ 1
2
ζ2
)(
1− ζ2qn+ 1
2
η
)(
1−ηζ 2qn+ 1
2
),
and the half-index is
IIm(ζ,η,q ) =δm,0
∞∏
n=0
(
1−qn+1)(
1− qn+1
ζ2
)(
1−ζ2qn+1)
(
1−η−1qn+ 1
2
)(
1− η−1qn+ 1
2
ζ2
)(
1−η−1ζ2qn+ 1
2
), (5.23)
so that
I(η,q ) =
∑
m
∮ dζ
2πiζ ∆m(ζ)IIm(q,ζ,η )IIm(q,ζ,η −1). (5.24)
Now we can act with a Wilson loop operator, 2 cos πb(2a−Q)→ qm/2ζ +q−m/2ζ−1,
following (5.21). We get that the half-index in the presence of a Wilson loop is simply
multiplied by the appropriate character, thanks to the δm,0 constraint:
ˆO0,1IIm(ζ,η,q ) =
(
ζ +ζ−1)
IIm(ζ,η,q ). (5.25)
On the other hand, if we act with the translated ’tHooft-Wilson operator
ˆO1,s = qm/2−1/4ζη−1/2−q−m/2+1/4ζ−1η1/2
qm/2ζ−q−m/2ζ−1 q−s/4qsm/2ζsp−1/2
+
+ qm/2+1/4ζη 1/2−q−m/2−1/4ζ−1η−1/2
qm/2ζ−q−m/2ζ−1 q−s/4q−sm/2ζ−sp1/2
+ , (5.26)
we get
ˆO1,sIIm(ζ,η,q ) =q1/4η1/2(
ζsδm,1/2 +ζ−sδm,−1/2
) ∞∏
n=0
(
1−qn+1)(
1− qn+3/2
ζ2
)(
1−ζ2qn+3/2)
(
1−η−1qn+ 1
2
)(
1− η−1qn+1
ζ2
)
(1−η−1ζ2qn+1)
.
(5.27)
Several useful cancellations led to a simple result. We would have derived the same result if
we had used (ˆx−, ˆp−) in the dictionary, as it should be: the half-index for a bare hemisphere
should intertwine the line defects acting on opposite sides of the equator. Notice that we
chose a measure ∆m(ζ) = 1
2(x+−x−1
+ )(x−−x−1
− ), which mimics the properties of the Liouville
measure.
– 54 –
We can now compare the index in the presence of two basic Wilson loops, one for each
hemisphere,
Iel(η,q ) =
∮ dζ
4πiζ (1−ζ2)(1−ζ−2) (5.28)
×
∞∏
n=0
(ζ +ζ−1)2(
1−qn+1)2(
1− qn+1
ζ2
)2(
1−ζ2qn+1)2
(
1−η−1qn+ 1
2
)(
1−ηqn+ 1
2
)(
1− qn+ 1
2
ηζ2
)(
1− ηqn+ 1
2
ζ2
)(
1− ζ2qn+ 1
2
η
)(
1−ηζ 2qn+ 1
2
),
with the index in the presence of two ’tHooft loops (of zero electric charge) ,
I(η,q ) = 2
∮ dζ
4πiζ (1−q1/2ζ2)(1−q1/2ζ−2) (5.29)
×
∞∏
n=0
(
1−qn+1)2(
1− qn+3/2
ζ2
)2(
1−ζ2qn+3/2)2
(
1−η−1qn+ 1
2
)(
1−ηqn+ 1
2
)(
1− qn+1
ηζ2
)(
1− ηqn+1
ζ2
)(
1− ζ2qn+1
η
)
(1−ηζ 2qn+1)
.
The factor of 2 arises from the sum of the abelian contributions of magnetic charge ±1/2.
We absorbed the factors q1/4η1/2q1/4η−1/2 in the measure. Amazingly, the two results agree,
computationally, to as high an order as we could check in the q expansion. This is a striking
veriﬁcation that our prescription of the line defects is compatible with S-duality.
6 The index as SL(2, C) Chern-Simons theory
Throughout the preceding sections, there have been various hints that the index IM(m,e ;q)
of a theory TM may have some relation to complex Chern-Simons theory on M itself, i.e.
Chern-Simons theory with complex gauge group SL(2, C). For example, the constructions
of TM andIM involve choosing a polarization on the phase space P∂M , and this is precisely
the phase space of complex Chern-Simons theory on a 3-manifold M with boundary [70, 71].
In addition, the ﬂat SL(2, C) connections in the bulk of M, which project to the Lagrangian
submanifoldLM,
LM = {ﬂat SL(2, C) connections on ∂M that extend to M}
∩
P∂M = {ﬂat SL(2, C) connections on ∂M},
correspond to spaces of SUSY vacua for TM [8, 19]; and these ﬂat connections on M are
the classical solutions to Chern-Simons theory. Moreover, we saw in Sections 4 and 5 that a
quantization of the Lagrangian’s deﬁning equations, ˆLM, provides diﬀerence operators that
annihilate the index. This again is an expected property of Chern-Simons wavefunctions: the
constraints describing classical solutions (LM) become promoted to quantum operators ( ˆLM)
that annihilate the quantum wavefunctions [28].
– 55 –
To be even more suggestive, consider the tetrahedron index in the electric fugacity basis
(3.3). Note that in the deﬁnition of the index as a partition function onS2×S1, the parameter
q =eℏ is real, while ζ =eiθ is a pure phase. We can then recombine m and θ into complex
variables, as in Section 3 :
Z = m
2 ℏ +iθ, Z = m
2 ℏ−iθ, (6.1)
or
z =eZ =q
m
2ζ, z =eZ =q
m
2ζ−1 ; (6.2)
so that the tetrahedron index takes the form
I∆(m;q,ζ ) =I∆(z,z;q) =
∞∏
r=0
1−qr+1z−1
1−qrz−1 . (6.3)
If we deﬁne Z∆(z;q)≡ ∏
r≥1(1−qrz−1) for |q| < 1, and allow ourselves the “Fock space
reorganization”∏
r≥1(1−q−rz) =∏
r≥0(1−qrz)−1, we would then have an index
I∆(z,z;q) “=” Z∆(z;q)Z∆(z;q−1), (6.4)
factorized into identical holomorphic and antiholomorphic pieces.
Such a factorization is familiar from the studies of SL(2, C) Chern-Simons partition
functions in [28–30]. More generally, the physical Chern-Simons partition function on a 3-
manifoldM would be a sum over classical ﬂat connectionsα with ﬁxed boundary conditionsx,
ZCS
M (x,x;q) =
∑
α
nα¯αZα
M(x;q)Z ¯α
M(x;q−1), (6.5)
and with nα¯α real and diagonal. 30 In the case of the tetrahedron, there is a unique ﬂat
connection at ﬁxed boundary condition x =z, and so a single term in (6.5). Note that (6.5)
has a symmetry under complex conjugation and exchange of q and q−1, which looks like ρ
symmetry (2.24) for the index.
Our goal in this section is to make the relation between SL(2, C) Chern-Simons theory
and the index as precise as possible. There actually exist several inequivalent quantizations
of complex Chern-Simons theory — corresponding to diﬀerent real symplectic structures on
the complex phase space P∂M — and we will see that one special choice is related to the
generalized indexIM(m;q,ζ ). An interesting open question is to understand what the other
quantizations might mean. In Section 6.3, we will give a “top-down,” qualitative view of
the equivalence between Chern-Simons theory and the index by considering the theory of
M5-branes in the geometry S1×S2×M and applying various known dualities.
30Explicit expansions of this type, not for indices but for the closely related ellipsoid partition functions of
some theories in class R, have recently appeared in [72].
– 56 –
6.1 Quantization at k = 0
Let’s begin by reviewing a few facts about Chern-Simons theory with gauge group GC =
SL(2, C) [28, 71, 73]. The most general complex bulk action on a 3-manifold M is
SCS(M) = t
8π
∫
M
Tr
(
AdA + 2
3A3
)
+
˜t
8π
∫
M
Tr
(
AdA + 2
3A
3)
, (6.6)
whereA is a local gC = sl(2, C)-valued one-form, deﬁned modulo the standard gauge trans-
formationsA→ g−1Ag +g−1dg. Unlike the case of real Chern-Simons theory, the complex
action here contains both holomorphic and antiholomorphic terms, and each comes with its
own coupling constant, here t and ˜t. Let us write
t =k +is, ˜t =k−is. (6.7)
A priori, k and s are independent complex parameters. However, independence of the path
integral measure exp
[
iSCS (M)
]
under large gauge transformations forces k to be an integer.
Moreover, unitarity — the statement that the path integral be conjugated under a change of
orientation on M — requires s∈ R.31
If the boundary of M is nonempty, then the Chern-Simons path integral on M is a
wavefunction in a boundary Hilbert spaceH∂M . This space is the quantization of the classical
phase space associated to the boundary,
P∂M ≃
{
ﬂat connectionsA on ∂M
}
. (6.8)
This space is endowed with a real symplectic structure induced from the Chern-Simons action:
ωk,s = t
8π Ω +
˜t
8π Ω, (6.9)
where Ω =
∫
∂M Tr
(
δA∧ δA) is a holomorphic symplectic form. By setting Ω = ωI−iωK, we
could also write this as
ωk,s = k
4πωI + s
4πωK. (6.10)
Here ωI and ωK coincide with two of the standard real symplectic forms on P∂M , viewed as
a hyperkahler manifold [74], hence the notation. It turns out that, as cohomology classes,
[ωK] = 0 while [ ωI/(4π)]∈ H2(P∂M ; Z) for any 2d boundary ∂M . Thus, as long as k∈ Z,
we have [ωk,s/(2π)]∈H2(∂M ; Z), and the pair (P∂M,ωk,s) is quantizable ( cf. [75]).
The Hilbert space H∂M is the quantization of (P∂M,ωk,s). However, this quantization
depends critically on the relative values of k and s. To illustrate this dependence more
concretely, let us consider a “model” phase space P≃ C∗× C∗, with coordinates x and p,
and a holomorphic symplectic form
Ω = 2dp
p ∧ dx
x . (6.11)
31An alternative unitarity structure with s∈iR was also discussed in [71]. However, it does not appear to
have direct relevance for 3d indices.
– 57 –
It is also convenient to take logarithms
X = logx, P = logp, (6.12)
deﬁned modulo 2πiZ .P is the actual phase space for the boundary ∂∆ of a tetrahedron —
thinking of ∂∆ as a four-punctured sphere, with unit SL(2, C) holonomy eigenvalues at each
puncture [19] — and it can be used as a building block to approximate the phase space of any
more complicated boundary [61]. For example, the phase space of a torus is PT 2≃P /Z2,
while for a genus g≥ 2 surface with s punctures an open patch of the phase space looks like
a quotient ofP3g−3+s. The coordinates z and p can be thought of as models for eigenvalues
of general SL(2, C) holonomies.
Now, to demonstrate the sensitivity of quantization to the values of k,s , suppose ﬁrst
that we quantize (P,ωk,s) for a choice of coupling constants s = 0 andk⁄= 0. In other words,
we choose the real symplectic form
ωk,0 = k
4πωI = k
2π
[
d Re(P )∧d Re(X)−d Im(P )∧d Im(X)
]
. (6.13)
Thus, writingP = C∗
1× C∗
2≃ (R1× R2)×(S1
1×S1
2), (6.13) indicates that the two noncompact
real directions are canonically conjugate to each other, as are the twoS1 directions. Moreover,
it is easy to see that [ ωk,0/(2π)] ∈ H2(P; Z), since
∫
S1
1×S1
2
ωk,0 = −2πk. If we choose a
polarization such that (say) Re(Z) and Im(Z) are both “positions” while Re( P ) and Im(P )
serve as “momenta,” the Hilbert space becomes
Hk,0 ≃ L2(R)⊗L2(Zk), (6.14)
with an inﬁnite-dimensional factor coming from quantization ofR1×R2, and a|k|-dimensional
factor coming from quantization of the compact S1
1×S1
2. The latter factor is much like the
Hilbert space of Chern-Simons theory with compact gauge group SU (2).
The choices = 0 andk⁄= 0 turns out not to be the relevant one for the 3d index. Rather,
we conjecture that the index is related to Chern-Simons theory quantized in the opposite limit
k = 0 and s⁄= 0. The Hilbert space in this case looks very diﬀerent, and we will proceed to
analyze it for the remainder of this section. The general situation k,s⁄= 0 is a slightly twisted
variation of k = 0, s⁄= 0; it would be interesting to see if it were related to a generalization
of the index.
The real symplectic structure at k = 0 is
ω0,s = s
4πωK = i
ℏdP∧dX− i
ℏdP∧dX (6.15)
=−2
ℏ
[
d ReP∧d ImX +d ImP∧d ReX
]
, (6.16)
with
ℏ≡ 4π
s . (6.17)
– 58 –
Then, we see that the coordinate on each noncompact R factor inP is canonically conjugate
to the coordinate on a compact S1. In fact, we could more naturally write the phase space
(P,ω 0,s) as T∗(S1
1×S1
2), with the standard symplectic form of a cotangent bundle. In order
to quantize (P,ω 0,s) we must choose a polarization, and there are several nice choices, sum-
marized in Table 1. The polarizations diﬀer in the combinations of compact and noncompact
coordinates that are designated as positions and momenta.32 This choice is somewhat distinct
from the coarser distinction of Z vs. P as position and momentum, and the related Sp(2, Z)
action that featured prominently in the construction of theories TM and indicesIM. We will
return to the Sp(2, Z) action in Section 6.2.
Positions Momenta Hilbert spaceH≡H 0,s
a) Im X, ImP (S1
1×S1
2) −2 ReP, 2 ReX (R2× R1) L2(S1)×L2(S1)
b) Im X, ReX (S1
1× R1) −2 ReP, −2 ImP (R2×S1
2) L2(S1)×L2(Z)
c) Re P, ImP (R2×S1
2) 2 Im X, 2 ReX (S1
1× R1) L2(Z)×L2(S1)
d) Re X, ReP (R1× R2) −2 ImP, 2 ImX (S1
2×S1
1) L2(Z)×L2(Z)
Table 1. Real polarizations and Hilbert spaces at k = 0. All Hilbert spaces are isomorphic, and
related by compact Fourier transform.
Two of the polarizations in Table 1 may begin to look familiar from our discussion of
indices. In particular, in polarization (d), the compactness of the momenta quantizes the
position coordinates Re X and ReP . Speciﬁcally, we ﬁnd
ReX =m ℏ
2, ReP =e ℏ
2, m, e ∈ Z , (6.18)
so that wavefunctions inH are just complex-valued functions of the two integers ( m,e ) and
the real parameter ℏ. This appears identical to the form of the index in a “charge basis”
(2.5). Alternatively, if we treat both real and imaginary parts of Z as positions, as in (b), the
wavefunctions become non-holomorphic functions of x = exp(ReX +i ImX). The compact
momentum ImP still quantizes ReZ∈ ℏ
2 Z, so
x =q
m
2ζ , with q≡eℏ, m∈ Z ; ζ =eiθ≡ei ImX. (6.19)
Therefore, wavefunctions in polarization (b) look like indices in an electric fugacity basis (2.3).
To go from one polarization to another, one should use Fourier transform, f (b)(x, ¯x; ℏ) =
f (b)(m,ζ ; ℏ) =∑
e∈Zf (d)(m,e ; ℏ)ζe, just as described below (2.5).
Further conﬁrmation of the relation between Chern-Simons wavefunctions and indices
comes from analyzing the algebra of operators acting on the Hilbert spaces in Table 1. In any
32In the terminology of geometric quantization, all the polarizations in Table 1 are real polarizations. One
advantage of this is that quantum wavefunctions can then be expressed as standard functions, rather than
sections of a line bundle, cf. [71].
– 59 –
polarization, the coordinates X,X,P, P become promoted to operators with commutation
relations [ ˆP, ˆX
]
= ℏ,
[ ˆP, ˆX
]
=−ℏ,
[ ˆP, ˆX
]
=
[ ˆP, ˆX
]
= 0. (6.20)
These relations can be read oﬀ directly from the form (6.15) of ω0,s. One can then work out
the action of the operators on wavefunctions, in various polarizations. In particular, acting
on f (d)(m,e ; ℏ) we ﬁnd
ˆX =m ℏ
2−∂e, ˆP =e ℏ
2 +∂m, ˆX =m ℏ
2 +∂e, ˆP =e ℏ
2−∂m (6.21)
whereas acting on f (b)(m,ζ ; ℏ) we have
ˆX =X, ˆP = ℏ∂X, ˆX =X, ˆP =−ℏ∂X. (6.22)
Even in the ( b) polarization, it is nice to note that the compactness of the position Im Z
necessarily quantizes the spectrum of the conjugate momentum operator ˆReP = 1
2
( ˆP + ˆP
)
=
e ℏ
2, e∈ Z.
It should be evident that the operator algebra just described is identical to the alge-
bra of index operators from Sections 2.5 and 3.3, with the identiﬁcation ( ˆX, ˆX, ˆP, ˆP ) =
( ˆX+, ˆX−, ˆP+, ˆP−). With this information in hand, we can move beyond Hilbert spaces and
compare the actual wavefunctions of nontrivial 3-manifolds. As reviewed at the beginning of
this section (and in many other places), the classical solutions to complex Chern-Simons the-
ory on M cut out a Lagrangian submanifold LM in the boundary phase space P∂M ; and the
quantum wavefunction ofM is annihilated by a quantization of the deﬁning equations for the
Lagrangian, ˆLM·ZM = 0. The quantizationLM→ ˆLM is universal in Chern-Simons theory,
in the sense that it does not depend on a certain real or complex form of the gauge group,
or on choices of polarization, cf. [28, 76]. Therefore, we can borrow results of [31], where La-
grangians were quantized in analytically continued Chern-Simons theory, and simply apply
them to ﬁnd quantized Lagrangians in the present case of physical SL(2, C) Chern-Simons at
k = 0.
The simplest example of such quantization is for a tetrahedron itself. The phase space
is just our model phase space, P∂∆ =P with standard coordinates x = z, p = z′′, and the
classical LagrangianL∆ is cut out by the equationz′′ +z−1−1 = 0. Since the real symplectic
form ω0,s manifestly breaks the holomorphic structure of P, it is perhaps better to write the
Lagrangian as
L∆ : z′′ +z−1− 1 = 0, z′′ +z−1− 1 = 0. (6.23)
Then quantization with respect to ω0,s produces operators ˆL∆+ = ˆz′′ + ˆz−1− 1, ˆL∆− =
ˆz
′′
+ˆz
−1
−1 that must annihilate the tetrahedron wavefunction. (As usual, we deﬁne ˆz = exp ˆZ,
etc.) In polarization (b), the equations determine
ZCS
∆ (z,z; ℏ) =
∞∏
r=0
1−qr+1z−1
1−qrz−1 (6.24)
– 60 –
up to an overall function of q. Given the dictionary z = q
m
2ζ of (6.19), this establishes the
equivalence of the Chern-Simons wavefunction with the index in an electric fugacity basis, up
to normalization.
In order to understand SL(2, C) Chern-Simons theory on a more general 3-manifold
M with boundary, we can decompose M into ideal tetrahedra, and then try to apply the
symplectic gluing framework of [31]. This requires deﬁning an aﬃne symplecticSp(∗, Z) action
on the tetrahedron Hilbert spaces H =H0,s of Table 1 and their products. It also requires
an appropriate quantum version of symplectic reduction, in order to implement gluing. We
will describe these operations in Section 6.2. Of course, we will ﬁnd that they coincide with
the operations on the index IM found in Section 2, so that Chern-Simons wavefunctions can
be constructed using the index-gluing rules of Section 4.1. Moreover, asking for SL(2, C)
Chern-Simons wavefunctions at k = 0 to be independent of a triangulation (invariant under
2-3 moves) even ﬁxes the normalization of the single-tetrahedron wavefunction (6.24) to agree
with that of the tetrahedron index. Taken together, these facts constitute an axiomatic proof33
that the index of TM is equivalent to an SL(2, C) Chern-Simons wavefunction,IM =ZCS
M .
We may ﬁnally note that SL(2, C) Chern-Simons theory has an obvious conjugation
symmetry, stemming from the symmetry of the action (6.6). It acts on a semi-classical phase
space (P,ωk,s) as complex conjugation and simultaneous exchange of t and ˜t, to preserve
the symplectic form (6.9). In the case k = 0, this means ℏ→− ℏ, or q→ q−1. Following
the dictionary (6.19) or (6.1), we see that complex conjugation is precisely ρ symmetry for
the index, from Section 2.4. Interestingly, the action of conjugation on wavefunctions suﬀers
from the same “Fock space reorganization” subtleties as the index — discussed brieﬂy, for
example, in Section 6.5 of [42].
