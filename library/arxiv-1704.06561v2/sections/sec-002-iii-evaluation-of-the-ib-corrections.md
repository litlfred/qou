---
doc_id: arxiv-1704.06561v2
doc_title: "Leading isospin-breaking corrections to pion, kaon and charmed-meson masses with Twisted-Mass fermions"
section_id: sec-002-iii-evaluation-of-the-ib-corrections
section_title: "III Evaluation of the IB corrections"
section_number: null
pages: 8-11
source_pdf: 1704.06561v2.pdf
source_sha256: e1d800fa0b122dbb
toc_source: outline
doc_brief: "Leading isospin-breaking corrections to pion, kaon and charmed-meson masses with Twisted-Mass fermions — 16 sections: Front matter; I Introduction; II Simulation details"
---
According to the approach of Ref. [8] the e.m. and strong IB corrections to the mass of a PS
meson with charge Qe can be written as
MPSQ = MPS + [δMPSQ]QED + [δMPS]QCD
(20)
with
[δMPSQ]QED ≡4παem [δMPSQ]em + ... ,
(21)
[δMPS]QCD ≡( bmd −bmu) [δMPS]IB + ... ,
(22)
where the ellipses stand for higher order terms in αem and ( bmd −bmu), while MPS stands for the PS
meson mass corresponding to the renormalized quark masses in the isosymmetric QCD theory. The
separation in Eq. (20) between the QED and QCD contributions, [δMPSQ]QED and [δMPS]QCD,
is prescription and renormalization scheme and scale dependent [21, 22], as it will be speciﬁed in
a while.
Throughout this work we adopt the quenched QED approximation, which neglects the sea-quark
electric charges and corresponds to consider only (fermionic) connected diagrams. Including the
contributions coming from the insertions of the e.m. current and tadpole operators, of the PS and
scalar densities (see Refs. [5, 8]) the basic diagrams are those depicted schematically in Fig. 1. The
insertion of the PS density is related to the the e.m. shift of the critical mass present in lattice
formulations breaking chiral symmetry, as in the case of Wilson and twisted-mass fermions.
(a)
(b)
(c)
(d)
(e)
FIG. 1: Fermionic connected diagrams contributing at O(e2) and O(md−mu) to the IB corrections to meson
masses: exchange (a), self energy (b), tadpole (c), pseudoscalar insertion (d) and scalar insertion (e).
In order to evaluate the diagrams (1a)-(1e) the following correlators are considered:
δCJ(t) =
X⃗
x,y1,y2
⟨0|T
n
φ†
PS(⃗x, t) Jµ(y1)Jµ(y2) φPS(0)
o
|0⟩,
(23)
δCT (t) =
X⃗
x,y
⟨0|T
n
φ†
PS(⃗x, t) T(y) φPS(0)
o
|0⟩,
(24)
δCPf (t) =
X⃗
x,y
⟨0|T
n
φ†
PS(⃗x, t) iψf(y)γ5ψf(y) φPS(0)
o
|0⟩,
(25)
δCSf (t) = −
X⃗
x,y
⟨0|T
n
φ†
PS(⃗x, t)

ψf(y)ψf(y)

φPS(0)
o
|0⟩,
(26)
where f = {u, d, s, c},
Jµ(y) =
X
f
qf
1
2
 ¯ψf(y)(γµ −iτ 3γ5)Uµ(y)ψf(y + aˆµ)
+
¯ψf(y + aˆµ)(γµ + iτ 3γ5)U†
µ(y)ψf(y)
i
(27)
is the (lattice) conserved e.m. current, and
T(y) =
X
f
q2
f
X
ν
1
2
 ¯ψf(y)(γν −iτ 3γ5)Uν(y)ψf(y + aˆν)
−
¯ψf(y + aˆν)(γν + iτ 3γ5)U†
ν(y)ψf(y)
i
(28)
is the tadpole operator with φPS(x) = iψf1(x)γ5ψf2(x) being the interpolating ﬁeld for a PS meson
composed by two valence quarks f1 and f2 with charges q1e and q2e. In our twisted-mass setup
the Wilson parameters of the two valence quarks are chosen to be opposite (r1 = −r2) in order to
guarantee that discretization eﬀects on MPS are of order O(a2mΛQCD).
Within the quenched QED approximation the correlator δCJ(t) corresponds to the sum of the
diagrams (1a)-(1b), while the correlators δCT (t), δCPf (t) and δCSf (t) represent the contributions
of the diagrams (1c), (1d) and (1e), respectively. The removal of the photon zero-mode is done
according to QEDL [23], i.e. the photon ﬁeld Aµ in momentum space satisﬁes Aµ(k0,⃗k =⃗0) ≡0
for all k0.
The statistical accuracy of the meson correlators is based on the use of the so-called “one-
end” stochastic method [24], which includes spatial stochastic sources at a single time slice chosen
randomly. Four stochastic sources (diagonal in the spin variable and dense in the color one) were
adopted per each gauge conﬁguration.
A new technique for the lattice evaluation of the photon insertion in the diagrams (a)-(c) of
Fig. 1 and an estimate of the computational cost are presented in the Appendix A.
In our analysis the correlators δCj(t) with j = {J, T, PS, S} are divided by the tree-level one
C(t) ≡
X⃗
x
⟨0|T
n
φ†
PS(⃗x, t)φPS(0)
o
|0⟩,
(29)
obtaining at large time distances, where the PS ground-state is dominant,
δCj(t)
C(t)
−−−−−−−−−−−−→
t>>a,(T−t)>>a
δZj
PS
ZPS
+ δMj
PS
MPS
fPS(t)
(30)
where ZPS ≡⟨0|φPS(0)|PS⟩and
fPS(t) ≡MPS
T
2 −t
 e−MP St −e−MP S(T−t)
e−MP St + e−MP S(T−t) −1 −MPS
T
2
(31)
is almost a linear function of the Euclidean time t. Thus, the various e.m. and strong IB corrections
to the PS mass, δMj
PS (j = J, T, Pf, Sf), can be extracted from the slope of the corresponding
ratios δCj(t)/C(t) at large time distances (see Table III for the chosen ﬁtting intervals).
The diﬀerence between the bare quark mass bµf in QCD+QED and the bare mass µf in isosym-
metric QCD is related to the corresponding diﬀerence between the renormalized masses bmf and
mf by
bµf −µf = bmf
bZmf
−mf
Zm
=
1
Zm
"
Zm
bZmf
bmf −mf
#
(32)
where bZmf (Zm) is the mass renormalization constant in QCD+QED (QCD). By deﬁning
Zm
bZmf
= 1 + 4παem
1
Zf
(33)
we get
bµf −µf =
1
Zm
[ bmf −mf] + 4παem
1
ZmZf
bmf .
(34)
For our maximally twisted-mass setup one has Zm = 1/ZP , while for 1/Zf we use the perturbative
result at leading order in αem in the MS scheme at the renormalization scale µ, given by [25]
1
Zf
(MS, µ) =
q2
f
16π2 [6log(aµ) −22.596] .
(35)
Once multiplied by the bare quantity δMSf
PS related to the insertion of the scalar density, the ﬁrst
term in the r.h.s. of Eq. (34) generates a ﬁnite term, which in our prescription [8] deﬁnes the QCD
correction
[δMPS]QCD (MS, µ) =
X
f=f1,f2
ZP (MS, µ)

bmf(MS, µ) −mf(MS, µ)

δMSf
PS .
(36)
The second term in the r.h.s. of Eq. (34) generates a logarithmic divergent contribution that, when
included in the QED correction, compensates the corresponding divergence of the self-energy and
tadpole diagrams. At leading order in αem and ( bmd −bmu) one has
[δMPSQ]QED (MS, µ) = 4παem


δMJ
PS + δMT
PS +
X
f=f1,f2
δmcrit
f
δMPf
PS
+
X
f=f1,f2
ZP (MS, µ)
Zf(MS, µ) mf(MS, µ) δMSf
PS


,
(37)
where δmcrit
f
is the e.m. shift of the critical mass for the quark ﬂavor f, which will be discussed
in details in the next Section. Note that, since we require bmf(MS, 2 GeV) = mf(MS, 2 GeV) for
f = (ud), s, c, the r.h.s. of Eq. (36) at the scale µ = 2 GeV receives a non-vanishing contribution
only when a valence light quark u or d is present in the PS meson (since md = mu = mud). In
that case [δMPS]QCD (MS, 2 GeV) is proportional to ( bmd −bmu)(MS, 2 GeV), as anticipated in
Eq. (22). When PSQ = π0,+ the contributions coming from the u and d quarks cancel out and
[δMπ]QCD (MS, 2 GeV) = 0 at leading order in ( bmd −bmu)(MS, 2 GeV).
A.
