---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-005-6-spin-isospin-projection-and-parametrizations
section_title: "Spin-isospin projection and parametrizations"
section_number: 6
pages: 13-15
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
---
For a ﬁxedNN channel it is convenient to use the eﬀec-
tive Lagrangian (11), withψ a nucleon ﬁeld for which the
combinationψ†ψ has deﬁnite spin and isospin (S,I ). The
Pauli principle dictates that only isospin-triplet t≡ (0, 1)
and isospin-singlet s ≡ (1, 0) are allowed combinations.
We use subscripts “s” and “t” here in reference to isospin,
with a warning that the same subscripts are sometimes
used in reference to spin. To go beyond the description
of an isolated two-nucleon system, it is desirable to treat
both combinations on the same footing. To this end, it is
convenient to introduce a nucleon ﬁeld N that is a dou-
blet in both spin and isospin space, along with projection
operators
(Ps)i =σ2σiτ 2/
√
8 , ( Pt)A =σ2τ 2τA/
√
8, (32)
where σi (τA) denotes the three Pauli matrices in spin
(isospin) space, and we have used lower- (upper-) case
14
indices to further distinguish the two spaces. The La-
grangian for the NN system can then be written as
L =N†
(
i∂0 + ∇2
2mN
)
N− C0s
2 (NTPsN)†(NTPsN)
− C0t
2 (NTPtN)†(NTPtN) +··· , (33)
where the ellipses represent analogous terms withC2s/t as
well as higher-order operators. Fierz rearrangements can
be used to generate equivalent interactions. Analogously,
Eq. (27) is generalized to the nuclear case by introducing
two dibaryon ﬁelds—one for each NN S-wave channel—
using the same projection operators Ps,t (Bedaque and
van Kolck, 1998).
The two channels are somewhat diﬀerent concerning
both sign and magnitude of the scattering lengths. How-
ever, it has been customary to treat both a−1
s and|at|−1
as Mlo, although we return to this issue in Sec. II.B.7.
The ERE, Eq. (12b), has a certain radius of conver-
gence, set by the nearest singularity to the expansion
pointk2 = 0. The pion-exchange cut on the imaginary k
axis starting atmπ/2 leaves the deuteron pole within the
radius of convergence of the ERE, and indeed it is well
known that the properties of this pole can be expressed in
terms of the ERE parameters (Goldberger and Watson,
1967), cf. Sec. II.B.1. For example, the deuteron binding
momentum is
γd = 1
as
(
1 + rs
2as
+···
)
. (34)
Alternatively, and this is in fact what was done ﬁrst his-
torically (Bethe, 1949), one can perform the ERE directly
about this pole ( i.e., about the point iγd in the complex
momentum plane),
k cotδd(k) =−γd + ρd
2
(
k2 +γ2
d
)
+··· , (35)
where ρd ≃ 1.765 fm (de Swart et al. , 1995) is the
deuteron eﬀective range. The motivation for using
Eq. (35) instead of the ERE about zero momentum is
that it captures the exact location of the pole already at
LO. Grießhammer (2004) extended the procedure to the
1S0 channel, where it is possible to deﬁne the ERE about
the virtual-state pole.
The ﬁrst detailed comparison of the 3S1 phase shift ob-
tained in Pionless EFT with empirical values was carried
out up to N2LO by Chen et al. (1999a), with LECs ﬁtted
to Eq. (35). In Fig. 7 we show results ﬁtted to Eq. (12b)
instead, which are qualitatively similar: convergence is
seen at low energies and already at NLO a very good de-
scription is achieved. The corresponding results for 1S0
up to N 2LO were presented by Beane et al. (2001b).
3
S
1
δ(k)	(deg)
60
80
100
140
160
 180
0
10
20
30
40
pionless	LO
pionless	NLO
pionless	N
2
LO
PWA
						chiral	O(Q
0
)
chiral	O(Q
2
)
chiral	O(Q
3
)
chiral	EM500
δ(k)	(deg)
20
30
40
50
60
70
E
lab
	(MeV)
60
100
140
180
Figure 7 The NN scattering phase shiftδ as a function of the
nucleon laboratory energy Elab in the 3S1 partial wave for
Pionless EFT and Chiral EFT at various orders (Long and
Yang, 2012a) (results kindly provided by C.-J. Yang), and
the chiral potential “EM500” (Entem and Machleidt, 2003).
For comparison we show the partial-wave analysis (PWA)
of Navarro P´ erezet al. (2013), with error bars smaller than
the symbols.
7. Coulomb eﬀects and other isospin breaking
Since almost all nuclear systems involve more than one
proton, the inclusion of electromagnetic eﬀects is gener-
ally important. In the low-energy regime, the dominant
eﬀect is given by “Coulomb photons”, i.e., the familiar,
static potential (∼ α/r) between charged particles. It
originates from the replacement of derivatives in the ef-
fective Lagrangian with covariant ones,
Dµ =∂µ + ieAµ ˆQ, (36)
where ˆQ is an appropriate charge operator ( e.g., ˆQ =
(1 +τ3)/2 for nucleons). The Coulomb photon-nucleon
coupling ie comes from the gauging of the nucleon time
derivative in Eq. (33), while the Coulomb-photon “prop-
agator” is i/(q2+λ2), whereλ is an IR-regulating photon
mass that is eventually taken to zero. Finer electromag-
netic eﬀects enter through operators with more covariant
derivatives and also directly through the ﬁeld strength,
or alternatively the electric (Ei =∂0Ai−∂iA0) and mag-
netic (Bi =ϵijm∂jAm) ﬁelds.
Kong and Ravndal (1999b, 2000) were the ﬁrst to study
proton-proton (pp) scattering in Pionless EFT. The chal-
lenge here lies in the fact that the Coulomb interaction
is important at very low energies: we see from Eq. (8)
for the Coulomb potential V ∼ e2/Q2 that Coulomb is
nonperturbative for Q <∼ αmN/2≡kC, which is in the
low-energy region of Pionless EFT. Subtracting the pure-
15
Coulomb amplitude TC from the full amplitude T , one
can write
TSC =T−TC =− 4π
mN
e2iσC
k cotδpp(k)− ik (37)
in terms of the “subtracted”pp phase shiftδpp(k) and the
pure-Coulomb phase shiftσC = arg Γ(1 + iη). Renormal-
ization can be carried out by matching to the “Coulomb-
modiﬁed” ERE (Bethe, 1949),
C2
η (k cotδpp(k)− ik) +αmNH(η)
=− 1
app
+ rpp
2 k2 +··· , (38)
whereapp≃− 7.8 fm andrpp≃ 2.8 fm (Bergervoet et al.,
1988) are the ERE parameters,C2
η = 2πη[exp(2πη)−1]−1
is the Sommerfeld factor in terms of η = kC/k, and
H(η) = ℜ[ψ(1 + iη)]− lnη + iC2
η/(2η) in terms of the
digamma function ψ. It should be emphasized that
the pp scattering amplitude, and thus also the eﬀec-
tive range parameters, are always deﬁned in the presence
of the Coulomb interaction and cannot be divided into
strong and electromagnetic parts in a model-independent
way (Kong and Ravndal, 1999b; Gegelia, 2004). For par-
ticles with non-unit charges the deﬁnition of the Coulomb
momentumkC is generalized in Sec. III, see Eq. (69).
In Pionless EFT, TSC is obtained by replacing all
empty bubbles in Fig. 3 with the dressed one shown in
Fig. 8. The initial and ﬁnal-state Coulomb interactions
are accounted for by the construction in Eq. (37). “Dress-
ing” here refers to resumming the Coulomb interaction to
all orders between each pair of C0 vertices, which Kong
and Ravndal (1999b, 2000) were able to do using a known
analytic expression for the pure Coulomb Green’s func-
tion. With dimensional regularization,
4π
mNCpp
0 (µ) = 1
app
−µ +αmN
(1
ε + ln µ
αmN
+ const.
)
.
(39)
The term linear in the renormalization scaleµ comes from
the PDS prescription, but Coulomb exchange now intro-
duces an additional logarithmic divergence, reﬂected in
the pole in ε = d− 3, where d is the number of spa-
tial dimensions. Range corrections have been considered
at NLO by Kong and Ravndal (2000) and at N 2LO by
Ando et al. (2007). An equivalent formulation in terms
of a pp dibaryon exists (Ando and Birse, 2010). The RG
analysis of Birse et al. (1999) discussed in Sec. II.B.4 has
also been extended to the charged-particle sector (Bar-
ford and Birse, 2003; Ando and Birse, 2008).
The LEC Cpp
0 = C0t + ∆C0(+) in Eq. (39) con-
tains an isospin-dependent contribution ∆ C0(+), which
is a short-range (or “indirect”) electromagnetic eﬀect.
The EFT includes also isospin breaking from the quark
masses (van Kolck, 1993, 1995). While electromagnetic
interactions break isospin more generally (“charge depen-
dence”), eﬀects linear in the quark masses break charge
= + + + · · ·
Figure 8 Bubble diagram dressed with Coulomb exchange
(wavy line).
symmetry (a rotation of π around the second axis in
isospin space) speciﬁcally. Introducing the projectors
P(±) = ( P 1
t ∓ iP 2
t )/
√
2 onto the pp/nn channel, the
isospin-breaking Lagrangian takes the form
Lib =δmNN†τ3N− ∆C0(+)
2 (NTP(+)N)†(NTP(+)N)
− ∆C0(−)
2 (NTP(−)N)†(NTP(−)N) +··· . (40)
NDA (9) indicates that the neutron-proton mass split-
ting δmN =O(ε ¯m,αmN/(4π)). It is well known that
the two types of contributions are comparable in mag-
nitude, ε ¯m∼ αmN/4π, valid up to a (scale-dependent)
factor of a few, but have opposite signs, the quark masses
tilting the balance in favor of the neutron. The mass-
splitting term can be removed by a redeﬁnition of the
nucleon ﬁeld (Friar et al. , 2004), and reappears as an
O(δmN/mN) eﬀect in the nucleon kinetic term. The
most important quark-mass eﬀects in the NN system lie
in the short-range LECs ∆ C0(±). The reduced quark
mass is ( ε ¯m)red = ε ¯m/Mhi and, together with the S-
to-S-wave enhancement discussed in Sec. II.B.2, leads
to (ann− at)/at ∼ ∆C0(−)/C0t = O(ε ¯ma t) ≃ 0.2,
cf. (K¨ oniget al., 2016). A similar contribution exists for
∆C0(+) which is, however, dominated by the electromag-
netic contribution ∆C0(+)/C0t =O(αmNat), consistent
with Eq. (39).
For most of the region of validity of Pionless EFT,
Q >∼ αmN and all electromagnetic interactions are ex-
pected to be perturbative. In this region, Q >∼ 1/at
as well. K¨ onig et al. (2016) developed an expansion in
powers of αmN/Q and 1/(Qat) in addition to the stan-
dard Q/Mhi expansion. For simplicity, they paired the
expansions by taking αmN ∼ a−1
t =O(M2
lo/Mhi) and
ε ¯m =O(M3
lo/M2
hi). In this case, LO in the 1S0 chan-
nel consists of the isospin-symmetric unitary amplitude,
that is, Eq. (12a) with k cotδt = 0. The ﬁrst short-range
and electromagnetic corrections break isospin symmetry
at NLO, reproducing app and leading to equal scattering
lengths in the other two 1S0 isospin channels. In addi-
tion, at NLO there is the standard, isospin-symmetricC2t
interaction, while quark-mass eﬀects (and the nn split-
ting fromnp) ﬁrst enter at N2LO. This is consistent with
the observed relation rpp≃rt.
