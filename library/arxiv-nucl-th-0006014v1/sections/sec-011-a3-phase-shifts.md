---
doc_id: arxiv-nucl-th-0006014v1
doc_title: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn)"
section_id: sec-011-a3-phase-shifts
section_title: "Phase shifts"
section_number: A.3
pages: 21-24
source_pdf: 0006014v1.pdf
source_sha256: 208c7a6aaf628b30
toc_source: inferred
doc_brief: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn) — 56 sections: Front matter; Introduction; The model"
---
Phase shifts are determined from the on-energy-shell R-matrix through:
Spin singlet
tan 0δJ(Tlab) = −π
2 qM 0RJ(q, q)
(A33)
Uncoupled spin triplet
tan 1δJ(Tlab) = −π
2 qM 1RJ(q, q)
(A34)
For the coupled states, a unitary transformation is needed to diagonalize the two-by-two
coupled R-matrix. This requires an additional parameter, known as the ‘mixing parameter’
ǫJ. Using the convention introduced by Blatt and Biedenharn [103], the eigenphases for the
coupled channels are, in terms of the on-shell R-matrix,
tan δJ
∓(Tlab) = −π
4 qM
"
RJ
J−1,J−1 + RJ
J+1,J+1 ± RJ
J−1,J−1 −RJ
J+1,J+1
cos 2ǫJ
#
(A35)
tan 2ǫJ(Tlab) =
2RJ
J+1,J−1
RJ
J−1,J−1 −RJ
J+1,J+1
.
Here, all R-matrix elements carry the arguments (q, q) where q denotes the c.m. on-energy-
shell momentum. Based upon correct (relativistic) kinematical considerations, the momen-
tum q and the nucleon mass M to be used in the above formulae are determined to be:
Proton-proton scattering:
q2 = 1
2MpTlab ,
(A36)
M = Mp .
(A37)
Neutron-neutron scattering:
q2 = 1
2MnTlab ,
(A38)
M = Mn .
(A39)
Neutron-proton scattering:
q2 =
M2
pTlab(Tlab + 2Mn)
(Mp + Mn)2 + 2TlabMp
,
(A40)
M = 2MpMn
Mp + Mn
.
(A41)
In the above, Mp denotes the proton mass, Mn the neutron mass (see Table I for their
accurate numerical values) and Tlab is the kinetic energy of the incident nucleon in the
laboratory system.
An alternative convention for the phase parameters has been used by Stapp et al. [104],
known as ‘bar’ phase shifts. These are related to the Blatt-Biedenharn parameters by
¯δJ
+ + ¯δJ
−= δJ
+ + δJ
−
sin(¯δJ
−−¯δJ
+) = tan 2¯ǫJ/tan 2ǫJ
(A42)
sin(δJ
−−δJ
+) = sin 2¯ǫJ/sin 2ǫJ
In this paper, all phase shifts shown in tables or ﬁgures are in the ‘bar’ convention, even
though we omit the bar in our notation.
The above formulae apply to the calculation of phase shifts when only the short-range
nuclear force is taken into account (and no electromagnetic interaction). This is, in general,
appropriate for nn and np scattering. We also note that the above momentum space method
is exactly equivalent to calculations conducted in r-space where the radial Schr¨odinger equa-
tion,
" d2
dr2 + q2 −L(L + 1)
r2
−MV
#
χL(r; q) = 0 ,
(A43)
is solved for the radial wave function χL(r; q) which is then matched to the appropriate
asymptotic form of the wave function to obtain the phase shift. When no long-range potential
is involved, the asymptotic wave functions are Riccati-Bessel functions [105].
In pp scattering, the long-range Coulomb potential must be taken into account. The
asymptotic form of the wave function then is
χL(r; q) ∝FL(η′, qr) + tan δC
L GL(η′, qr)
(A44)
with FL and GL the regular and irregular Coulomb functions [105]. By δC we denote the
phase shift of the nuclear plus Coulomb interaction with respect to Coulomb wave functions;
that is, in the notation of Ref. [46], δC ≡δC
C+N. The parameter η′ is the “relativistic” η
deﬁned by [106,107,46]
η′ = α
vlab
= Mp
2q α′ ,
(A45)
with
α′ = αE2
q + q2
MpEq
,
(A46)
and α = 1/137.035989 [8]. The total potential V that appears in Eq. (A43) is now the sum
of the nuclear potential VN and the Coulomb potential VC; i. e.,
V = VN + VC ,
(A47)
where we use the “relativistic” Coulomb potential [107]
VC = α′
r .
(A48)
Since we conduct our calculations in momentum space, we do not solve Eq. (A43) and, thus,
do not have a numerical χ(r; q) available that can be matched directly to the asymptotic
form Eq. (A44). However, there are ways to perform this matching within the framework
of momentum space calculations.
We follow here the method proposed by Vincent and
Phatak [108] in which the potential is divided into a short-range part VS and a long-range
part VL; i. e.,
V = VS + VL
(A49)
with
VS = (VN + VC)θ(R −r) ,
(A50)
VL = VCθ(r −R) ,
(A51)
where R is to be chosen such that the short-range nuclear potential has vanished for r > R
(R ≈10 fm is an appropriate choice); and θ is the usual Heaviside step function. First,
one calculates the phase shift (denoted by δS
L) that is produced by VS alone. Notice that
VS is of range R and consists of the nuclear potential plus the Coulomb potential cut oﬀat
r = R. There is no problem in performing numerically the Bessel transformation of a cutoﬀ
Coulomb potential to produce the momentum space version of this potential for the various
partial waves. Since VS is of ﬁnite range, the momentum space formalism can be used to
calculate δS
L. The asymptotic wave function associated with VS and δS
L is
χS
L(r; q) ∝FL(η′ = 0, qr) + tan δS
LGL(η′ = 0, qr)
(A52)
which should match smoothly the asymptotic function Eq. (A44) at r = R.
Note that
FL(η′ = 0, qr) and GL(η′ = 0, qr) are equal to Riccati-Bessel functions.
Matching the
logarithmic derivatives yields the desired formula for the phase shift δC
L :
tan δC
L = [FL(0), FL(η′)] + tan δS
L[GL(0), FL(η′)]
[GL(η′), FL(0)] + tan δS
L[GL(η′), GL(0)] ,
(A53)
where the square brackets denote the Wronskian
[FL(0), FL(η′)] ≡
"
FL(0)dFL(η′)
dr
−FL(η′)dFL(0)
dr
#
r=R
(A54)
and FL(0) ≡FL(η′ = 0, qr), FL(η′) ≡FL(η′, qr); similarly for GL.
All pp phase shifts shown in this paper are Coulomb phase shifts, δC, as deﬁned and
calculated above. However, we like to stress that, for the calculation of observables (e. g.,
to obtain the χ2 in regard to experimental data), we use electromagnetic phase shifts, as
necessary, which we obtain by adding to the Coulomb phase shifts the eﬀects from two-
photon exchange, vacuum polarization, and magnetic moment interactions as calculated
by the Nijmegen group [46,47]. This is important for 1S0 below 30 MeV and negligible
otherwise.
