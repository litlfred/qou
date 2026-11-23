---
doc_id: physrevd111094513
doc_title: "Lattice QCD calculation of the Compton amplitude subtraction function"
section_id: sec-014-appendix-a-details-of-lattice-operator-product-e
section_title: "APPENDIX A: DETAILS OF LATTICE OPERATOR PRODUCT EXPANSION"
section_number: null
pages: 9-13
source_pdf: PhysRevD.111.094513.pdf
source_sha256: c05dfaef1f1c2f98
toc_source: outline
doc_brief: "Lattice QCD calculation of the Compton amplitude subtraction function — 16 sections: Lattice QCD calculation of the Com; I. INTRODUCTION; II. BACKGROUND"
---
OPERATOR PRODUCT EXPANSION
Applying the fundamental thesis of the operator product
expansion (OPE), the time-ordered product of two local
operators, O1ðzÞ and O2ð0Þ, can be represented by a single
local operator in the limit z →0. Writing this single
operator in terms of a standard basis of operators, fOng,
the OPE can be expressed as
lim
z→0T fO1ðzÞO2ð0Þg ¼
X
n
CnðzÞOnð0Þ;
ðA1Þ
where the Wilson coefficients CnðzÞ are c-number func-
tions. Provided the external momentum of the system is
small compared to the separation scale 1=z, the perturba-
tive, short-distance physics is entirely encoded within the
Wilson coefficients, while the nonperturbative, long-dis-
tance physics is entirely contained within the operators. Of
course, since QCD is an asymptotically free theory, the
strong coupling constant αs is small at the scale of z, and
thus the Wilson coefficients CnðzÞ can be computed
perturbatively.
In practice, Eq. (A1) is replaced with its momentum-
space counterpart,
Z
d4zeiq·zT fO1ðzÞO2ð0Þg ¼
X
n
CnðqÞOnð0Þ;
ðA2Þ
where CnðqÞ are the Fourier-transformed Wilson coeffi-
cients. To ensure the CnðqÞ coefficients exclusively encode
the perturbative, short-distance physics, q must be large
compared to the momentum of the external state. As for the
standard basis in the continuum, fOng, it is conventional to
select a basis where each operator is fully symmetric and
traceless, thereby ensuring linear independence and pre-
venting cross-dimensional operator mixing.
Turning to the forward Compton amplitude, the ultimate
objective of this appendix is to perform a lattice operator
product expansion (LOPE) for a proton. By the very nature
of the OPE, the external state of the system only contributes
to the matrix elements, not the operators or Wilson
coefficients themselves. Thus, for the sake of clarity, we
can perform the calculation with a single quark external
state of momentum pμ with charge Q ¼ 1 and generalize to
a proton at the end by adding quark flavors and associated
charges.
To begin, recall the definition of the spin-averaged
forward Compton amplitude,
Tμν ¼ i
Z
d4zeiq·zhpjT fVμðzÞVνð0Þgjpi:
ðA3Þ
Wick rotating to Euclidean space, Eq. (A3) becomes [55]
TEμν ¼
Z
d4zEe−iðq·zÞEhpjT fVEμðzÞVEνð0Þgjpi;
ðA4Þ
where VEμ ¼ ¯ψγEμψ. For the sake of convenience, we
will suppress the explicit Euclidean notation moving
forward. At tree-level and zeroth order in the strong
coupling constant αs, only two contraction terms con-
tribute to Eq. (A4), and thus the Compton amplitude can be
written as
TLμν ¼ ¯uðpÞγμ ˜SWðp þ qÞγνuðpÞ þ ¯uðpÞγν ˜SWðp −qÞγμuðpÞ:
ðA5Þ
Here we have defined the dimensionless Wilson propagator,
˜SWðkÞ ¼ −iγμ sinðakμÞ þ aMðk; m0Þ
P
μ sin2ðakμÞ þ a2M2ðk; m0Þ ;
ðA6Þ
for
aMðk; m0Þ ¼ am0 þ r
X
τ
½1 −cosðakτÞ;
ðA7Þ
with r denoting the Wilson parameter and m0 the bare quark
mass. Having now acquired a suitable form for TLμν, we are
now in a position to commence the OPE. Firstly, consider the
explicit form of the momentum-space Wilson propagators
˜SWðp  qÞ from Eq. (A6),
˜SWðp  qÞ ¼ am0 þ rP
α½1 −cosðapα  aqαÞ −iP
α γα sinðapα  aqαÞ
P
τ sin2ðapτ  aqτÞ þ ½am0 þ rP
τð1 −cosðapτ  aqτÞÞ2 :
ðA8Þ
Expanding the trigonometric functions and isolating all p-dependence in sμ ≡sinðapμÞ, Eq. (A8) becomes
˜SWðp  qÞ ¼ am0 þ rP
α½1  sinðaqαÞsα −cosðaqαÞ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 −s2α
p
 −iP
αγα½cosðaqαÞsα  sinðaqαÞ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 −s2α
p

P
τ½cosðaqτÞsτ  sinðaqτÞ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 −s2τ
p
2 þ ½am0 þ rP
τð1  sinðaqτÞsτ −cosðaqτÞ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 −s2τ
p
Þ2 ;
ðA9Þ
where we have used cosðapμÞ ¼ þ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 −s2μ
q
, choosing the positive square root since cosðapμÞ > 0 for very small pμ. In the
continuum OPE, the calculation proceeds by expanding the denominator of the propagator as a power series in ω ¼
2p · q=Q2 in the unphysical (i.e. ω < 1) region. Given the added complexity of the lattice propagator, this standard
approach is unfeasible. Rather, we proceed by expanding the denominator of Eq. (A9), ˜Sdn
Wðp  qÞ, in small pμ (hence small
sμ). Doing so, we find
˜Sdn
Wðp  qÞ ≡
1
P
τ½cosðaqτÞsτ  sinðaqτÞ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 −s2τ
p
2 þ ½am0 þ rP
τð1  sinðaqτÞsτ −cosðaqτÞ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 −s2τ
p
Þ2
¼
1
Ωðq; m0Þ ∓
1
Ω2ðq; m0Þ
X
τ
2 sinðaqτÞ½cosðaqτÞ þ raMðq; m0Þsτ þ Oðs2Þ;
ðA10Þ
where we define
Ωðq; m0Þ ¼
X
ρ
sin2ðaqρÞ þ a2M2ðq; m0Þ:
ðA11Þ
Substituting Eqs. (A10) and (A9) back into Eq. (A5), and further expanding the numerator terms
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 −s2τ
p
¼ 1 þ Oðs2Þ, we
arrive at the following form:
TLOPE
μν
¼
1
Ωðq; m0Þ ¯uðpÞγμ

−i
X
α
cosðaqαÞγαsα −i
X
α
sinðaqαÞγα þ r
X
α
sinðaqαÞsα þ aMðq; m0Þ

γν
×

1 −
2
Ωðq; m0Þ
X
τ
sinðaqτÞ½cosðaqτÞ þ raMðq; m0Þsτ

uðpÞ
þ
1
Ωðq; m0Þ ¯uðpÞγν

−i
X
α
cosðaqαÞγαsα þ i
X
α
sinðaqαÞγα −r
X
α
sinðaqαÞsα þ aMðq; mÞ

γμ
×

1 þ
2
Ωðq; m0Þ
X
τ
sinðaqτÞ½cosðaqτÞ þ raMðq; m0Þsτ

uðpÞ þ Oðs2Þ:
ðA12Þ
Rewriting Eq. (A12) yields
TLOPE
μν
¼
1
Ωðq; m0Þ ¯uðpÞ

−iγμ
X
α
½cosðaqαÞγαsα þ sinðaqαÞγαγν −iγν
X
α
½cosðaqαÞγαsα −sinðaqαÞγαγμ
þ r
X
α
sinðaqαÞsαðγμγν −γνγμÞ þ aMðq; m0Þðγμγν þ γνγμÞ

uðpÞ
þ
2
Ω2ðq; m0Þ
X
τ
Xτðq; m0Þ¯uðpÞ

i
X
α
sinðaqαÞ½γμγαγν þ γνγαγμsτ −aMðq; m0Þðγμγν −γνγμÞsτ

uðpÞ þ Oðs2Þ;
ðA13Þ
where Xτðq; m0Þ ¼ sinðaqτÞ½cosðaqτÞ þ raMðq; m0Þ. Applying the anticommutation relation for Euclidean gamma
matrices, fγμ; γνg ¼ 2δμνI, and the identity γμγτγν ¼ δμτγν þ δτνγμ −δμνγτ þ ϵσμτνγσγ5, we can write Eq. (A13) as
TLOPE
μν
¼
−2i
Ωðq; m0Þ ¯uðpÞ

cosðaqμÞsμγν þ cosðaqνÞsνγμ −δμν
X
α
cosðaqαÞsαγα þ
X
α
ϵσμαν sinðaqαÞγσγ5
þ r
X
α
sinðaqαÞsασμν þ iaMðq; m0Þδμν

uðpÞ þ
4i
Ω2ðq; m0Þ
X
τ
Xτðq; m0Þ¯uðpÞ

sinðaqμÞsτγν þ sinðaqνÞsτγμ
−δμν
X
α
sinðaqαÞsτγα þ aMðq; m0Þsτσμν

uðpÞ þ Oðs2Þ:
ðA14Þ
Thus far, we have neglected the spin-averaged nature of the amplitude under consideration. Having sufficiently expanded
the
expression,
we
can
now
separate
the
amplitude
into
a
symmetric
and
antisymmetric
component:
TLOPE
μν
¼ TLOPE
fμνg þ TLOPE
½μν . Then, accounting for spin-averaging, we discard the antisymmetric term, leaving
TLOPE
fμνg ¼
−2i
Ωðq; m0Þ ¯uðpÞ

cosðaqμÞsμγν þ cosðaqνÞsνγμ −δμν
X
α
cosðaqαÞsαγα þ iaMðq; m0Þδμν

uðpÞ
þ
4i
Ω2ðq; m0Þ
X
τ
Xτðq; m0Þ¯uðpÞ

sinðaqμÞsτγν þ sinðaqνÞsτγμ −δμν
X
α
sinðaqαÞsτγα

uðpÞ þ Oðs2Þ:
ðA15Þ
In discretized Euclidean space, we associate sinðapμÞ ↔−iaD
↔
μ, where D
↔
μ ¼ ð⃗D −⃖DÞ=2, since pμ is associated
with −i∂μ in continuous Euclidean spacetime. The covariant derivative here is, of course, the lattice covariant derivative
(i.e. finite difference operator), which reduces to the continuum covariant derivative in the limit a →0. Defining
TLOPE
fμνg ¼ hpjtLOPE
fμνg jpi, Eq. (A15) becomes
tLOPE
fμνg ¼
2ai
Ωðq;m0Þ

cosðaqμÞ ¯ψγνiD
↔
μψ þ cosðaqνÞ ¯ψγμiD
↔
νψ −δμν
X
α
cosðaqαÞ ¯ψγαiD
↔
αψ −iMðq;m0Þδμν ¯ψψ

−
4ai
Ω2ðq;m0Þ
X
τ
Xτðq;m0Þ

sinðaqμÞ ¯ψγνiD
↔
τψ þ sinðaqνÞ ¯ψγμiD
↔
τψ −δμν
X
α
sinðaqαÞ ¯ψγαiD
↔
τψ

þ OðD2Þ:
ðA16Þ
We are now in the position to construct symmetric and traceless operators of the form,
OS ¼ ¯ψψ;
OVμ1…μn ¼ ¯ψ½ð−1Þn−1γfμ1iD
↔
μ2…iD
↔
μngψ −traces;
ðA17Þ
which we define in such a way so that, in the limit a →0, these reduce to the standard continuum operators. Unlike the
continuum OPE, Eq. (A16) has additional q-dependent trigonometric coefficients which interfere with the construction of
such operators. Thus, we expand the trigonometric functions as
tLOPE
fμνg ¼
2a
Ωðq; m0Þ Mðq; m0Þδμν ¯ψψ þ
2ai
Ωðq; m0Þ

½1 −2sin2ðaqμ=2Þ ¯ψγνiD
↔
μψ þ ½1 −2sin2ðaqνÞ ¯ψγμiD
↔
νψ
−δμν
X
α
½1 −2sin2ðaqαÞ ¯ψγαiD
↔
αψ

−
4ai
Ω2ðq; m0Þ
X
τ
Xτðq; m0Þ

sinðaqμÞ ¯ψγνiD
↔
τψ þ sinðaqνÞ ¯ψγμiD
↔
τψ −δμν
X
α
sinðaqαÞ ¯ψγαiD
↔
τψ

þ OðD2Þ
¼ 2aMðq; m0Þ
Ωðq; m0Þ δμνOS þ
−2a2i
Ωðq; m0Þ

OVμν −1
2 δμν ¯ψi
=
Dψ

þ
−4ai
Ωðq; m0Þ

sin2ðaqμ=2Þ ¯ψγνiD
↔
μψ þ sin2ðaqνÞ ¯ψγμiD
↔
νψ −δμν
X
α
sin2ðaqαÞ ¯ψγαiD
↔
αψ

−
4ai
Ω2ðq; m0Þ
X
τ
Xτðq; m0Þ

sinðaqμÞ ¯ψγνiD
↔
τψ þ sinðaqνÞ ¯ψγμiD
↔
τψ −δμν
X
α
sinðaqαÞ ¯ψγαiD
↔
τψ

þ OðD2Þ: ðA18Þ
At leading order in a, ¯ψ
=
Dψ ¼ m0OS, and thus Eq. (A18) becomes
tLOPE
fμνg ¼
2a
Ωðq;m0Þδμν
1
2m0 þ r
a
X
τ
½1 −cosðaqτÞ

OS −
2ai
Ωðq;m0ÞOVμν
−
4ai
Ωðq;m0Þ

sin2ðaqμ=2Þ ¯ψγνiD
↔
μψ þ sin2ðaqνÞ ¯ψγμiD
↔
νψ −δμν
X
α
sin2ðaqαÞ ¯ψγαiD
↔
αψ

−
4ai
Ω2ðq;m0Þ
X
τ
Xτðq;m0Þ

sinðaqμÞ ¯ψγνiD
↔
τψ þ sinðaqνÞ ¯ψγμiD
↔
τψ −δμν
X
α
sinðaqαÞ ¯ψγαiD
↔
τψ

þ OðD2Þ:
ðA19Þ
This is as far as we can reasonably progress. The terms in
the second line of Eq. (A19) cannot be converted into
operators of the form Eq. (A17) as a result of interference
from the trigonometric terms. However, for our purposes,
we need not progress any further. Rather, we restrict our
attention to only the terms at zeroth order in the covariant
derivative,
tLOPE
fμνg ¼
2a
Ωðq; m0Þ δμν
1
2 m0 þ r
a
X
τ
½1 −cosðaqτÞ

OS
þ OðDÞ
¼ C0ðq; m0ÞδμνOS þ OðDÞ;
ðA20Þ
where C0ðq; m0Þ is the Wilson coefficient for the zeroth
order term in the Compton amplitude OPE expansion. Then
the full amplitude becomes
TLOPE
fμνg ¼ C0ðq; m0Þδμνhpj ¯ψψjpi þ OðDÞ;
ðA21Þ
where the matrix element hpj ¯ψψjpi ∝a. There are two
components to Eq. (A21), a continuum component of order
Oð1=aÞ which, together with the matrix element, survives
the continuum limit, and a lattice component which
vanishes in the limit a →0. The continuum component
is given by
lim
a→0 aC0ðq; m0Þ ¼
m0
q2 þ m2
0
;
ðA22Þ
which simply corresponds to the first term of Eq. (A20). To
determine the pure “discretization contribution” to the
lattice Compton amplitude, ΔTfμνg, we can therefore
simply remove this term, leaving
ΔTfμνg ¼
2r
Ωðq;m0Þδμν
X
τ
½1 −cosðaqτÞhpjOSjpi þ OðDÞ;
ðA23Þ
which entirely vanishes in the continuum. We can apply
this same result to the subtraction function by selecting the
component μ ¼ ν ¼ 3 with ω ¼ 0 so that Eq. (3) reduces to
T33 ¼ S1ðQ2Þ. Since we select the μ ¼ ν ¼ 3 component,
we also incorporate the factor of ð−iÞ2 that was neglected
during the Wick rotation (μ ¼ 3 component of the vector
current picks up factor of −i in shifting from Minkowski to
Euclidean space). Finally, we introduce a factor of (−1) for
the sake of general clarity, and correct for this change of
sign by adding the correction in Eq. (18), as opposed to
subtracting it. Thus, for a quark state, we can define a
“correction term” to the subtraction function,
ΔS1 ≡CWðq; m0Þhpj ¯ψψjpi;
ðA24Þ
where
CWðq; m0Þ ≡2rP
τ½1 −cosðaqτÞ
Ωðq; m0Þ
ðA25Þ
is the discretized “Wilson coefficient.” This final result can
be applied to the proton by simply extending to multiple
quark flavors with their associated charges, and introducing
a renormalization factor, ZV, to the vector currents. It
should be noted that this does not contribute additional
terms in the Wick expansion of Eq. (A4) from the product
of two different currents because terms from these con-
tractions are of twist t ≥4 and thus do not contribute at
leading order.
