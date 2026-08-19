---
doc_id: arxiv-nucl-th-0006014v1
doc_title: "The high-precision, charge-dependent Bonn nucleon-nucle on potential (CD-Bonn) R. Machleidt ∗"
section_id: sec-024-3-phase-shifts
section_title: "Phase shifts"
section_number: 3
pages: 21-23
source_pdf: 0006014v1.pdf
source_sha256: 208c7a6aaf628b30
doc_brief: "The high-precision, charge-dependent Bonn nucleon-nucle on potential (CD-Bonn) R. Machleidt ∗ — 35 sections: Scattering equation . . . . . . . ; R-matrix and partial wave decompos; Phase shifts . . ."
---
Phase shifts are determined from the on-energy-shell R-matrix through:
Spin singlet
tan 0δJ (Tlab) = −π
2qM 0RJ (q,q ) (A33)
Uncoupled spin triplet
tan 1δJ (Tlab) = −π
2qM 1RJ (q,q ) (A34)
For the coupled states , a unitary transformation is needed to diagonalize the two- by-two
coupledR-matrix. This requires an additional parameter, known as th e ‘mixing parameter’
ǫJ . Using the convention introduced by Blatt and Biedenharn [1 03], the eigenphases for the
coupled channels are, in terms of the on-shell R-matrix,
tan δJ
∓(Tlab) = −π
4qM
[
RJ
J−1,J −1 +RJ
J+1,J +1 ± RJ
J−1,J −1 −RJ
J+1,J +1
cos 2ǫJ
]
(A35)
tan 2ǫJ (Tlab) = 2RJ
J+1,J −1
RJ
J−1,J −1 −RJ
J+1,J +1
.
Here, all R-matrix elements carry the arguments ( q,q ) where q denotes the c.m. on-energy-
shell momentum. Based upon correct (relativistic) kinemat ical considerations, the momen-
tum q and the nucleon mass M to be used in the above formulae are determined to be:
Proton-proton scattering:
q2 = 1
2MpTlab, (A36)
M =Mp. (A37)
21
Neutron-neutron scattering:
q2 = 1
2MnTlab, (A38)
M =Mn. (A39)
Neutron-proton scattering:
q2 = M 2
pTlab(Tlab + 2Mn)
(Mp +Mn)2 + 2TlabMp
, (A40)
M = 2MpMn
Mp +Mn
. (A41)
In the above, Mp denotes the proton mass, Mn the neutron mass (see Table I for their
accurate numerical values) and Tlab is the kinetic energy of the incident nucleon in the
laboratory system.
An alternative convention for the phase parameters has been used by Stapp et al. [104],
known as ‘bar’ phase shifts. These are related to the Blatt-B iedenharn parameters by
¯δJ
+ + ¯δJ
− =δJ
+ +δJ
−
sin(¯δJ
− − ¯δJ
+) = tan 2¯ǫJ/tan 2ǫJ (A42)
sin(δJ
− −δJ
+) = sin 2¯ǫJ/sin 2ǫJ
In this paper, all phase shifts shown in tables or ﬁgures are i n the ‘bar’ convention, even
though we omit the bar in our notation.
The above formulae apply to the calculation of phase shifts w hen only the short-range
nuclear force is taken into account (and no electromagnetic interaction). This is, in general,
appropriate for nn andnp scattering. We also note that the above momentum space metho d
is exactly equivalent to calculations conducted in r-space where the radial Schr¨ odinger equa-
tion,
[
d2
dr2 +q2 −L(L + 1)
r2 −MV
]
χL(r;q) = 0 , (A43)
is solved for the radial wave function χL(r;q) which is then matched to the appropriate
asymptotic form of the wave function to obtain the phase shift. When no long-range potential
is involved, the asymptotic wave functions are Riccati-Bes sel functions [105].
In pp scattering, the long-range Coulomb potential must be taken into account. The
asymptotic form of the wave function then is
χL(r;q) ∝FL(η′,qr ) + tanδC
LGL(η′,qr ) (A44)
with FL and GL the regular and irregular Coulomb functions [105]. By δC we denote the
phase shift of the nuclear plus Coulomb interaction with res pect to Coulomb wave functions;
that is, in the notation of Ref. [46], δC ≡ δC
C+N . The parameter η′ is the “relativistic” η
deﬁned by [106,107,46]
η′ = α
vlab
= Mp
2q α′, (A45)
22
with
α′ =αE2
q +q2
MpEq
, (A46)
and α = 1/137.035989 [8]. The total potential V that appears in Eq. (A43) is now the sum
of the nuclear potential VN and the Coulomb potential VC; i. e.,
V =VN +VC, (A47)
where we use the “relativistic” Coulomb potential [107]
VC = α′
r . (A48)
Since we conduct our calculations in momentum space, we do no t solve Eq. (A43) and, thus,
do not have a numerical χ(r;q) available that can be matched directly to the asymptotic
form Eq. (A44). However, there are ways to perform this match ing within the framework
of momentum space calculations. We follow here the method pr oposed by Vincent and
Phatak [108] in which the potential is divided into a short-r ange part VS and a long-range
part VL; i. e.,
V =VS +VL (A49)
with
VS = (VN +VC)θ(R −r), (A50)
VL =VCθ(r −R), (A51)
where R is to be chosen such that the short-range nuclear potential h as vanished for r >R
(R ≈ 10 fm is an appropriate choice); and θ is the usual Heaviside step function. First,
one calculates the phase shift (denoted by δS
L) that is produced by VS alone. Notice that
VS is of range R and consists of the nuclear potential plus the Coulomb poten tial cut oﬀ at
r =R. There is no problem in performing numerically the Bessel tr ansformation of a cutoﬀ
Coulomb potential to produce the momentum space version of t his potential for the various
partial waves. Since VS is of ﬁnite range, the momentum space formalism can be used to
calculate δS
