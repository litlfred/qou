---
doc_id: arxiv-1704.06561v2
doc_title: "Leading isospin-breaking corrections to pion, kaon and charmed-meson masses with Twisted-Mass fermions"
section_id: sec-014-a-numerical-evaluation-of-the-diagrams-a---e
section_title: "A Numerical evaluation of the diagrams ??(a) - ??(e)"
section_number: null
pages: 42-47
source_pdf: 1704.06561v2.pdf
source_sha256: e1d800fa0b122dbb
toc_source: outline
doc_brief: "Leading isospin-breaking corrections to pion, kaon and charmed-meson masses with Twisted-Mass fermions — 16 sections: Front matter; I Introduction; II Simulation details"
---
In this paper we consider QED at O (αem), evaluating explicitly the fermionic connected dia-
grams contributing to meson masses.
For the diagrams 1(a) and 1(b) the numerical cost scales badly with the volume. Therefore,
stochastic approaches are needed to avoid computing explicitly the integrals over the beginning
and end of the photon propagator, the cost of which would be exceedingly too large for realistic
volumes. Here we adopt a variation of the technique used in Ref. [8].
Let us ﬁrst recall the technique used in the past.
For the sake of simplicity let us discuss the case of the “exchange” diagram 1(a) for a bilinear
¯ψΓψ:
δCexch (t) ≡
X⃗
x,y1,y2
⟨S (0; y1) Vµ (y1) S (y1;⃗x, t) ΓS (⃗x, t; y2) Vν (y2) S (y2; 0) Γ⟩Gµν (y1, y2) .
The nested summation over y1 and y2 is prohibitively costly and scales like V 2. We can split them
into two separate summations, each scaling as V , by introducing a set of real stochastic ﬁelds
ηµ (x) = ±1 ∀µ, x . The expectation value of the product of two ﬁelds is given by:
lim
n→∞
1
n
n
X
i=1
ηi
µ (x) ηi
ν (y) = δµνδ (x, y) ,
(A1)
from which we can write the photon propagator as:
Gµν (y1, y2) = lim
n→∞
1
n
n
X
i=1
φi
µ (y1) ηi
ν (y2) ,
where φi
µ (y1) = Gµρ (y1, y3) ηi
ρ (y3). Taking advantage of the γ5 hermiticity of the quark propaga-
tor, the correlation function can be obtained in the Feynman gauge by evaluating:
δCexch (t) ≡lim
n→∞
1
n
n
X
i=1
X
µ,⃗x

SVµφi
µ † (⃗x, t; 0) γ5ΓSVµηi
µ (⃗x, t; 0) Γγ5

,
(A2)
where
SVµϕµ (⃗x, t; 0) ≡S (⃗x, t; y) Vµ (y) ϕµ (y) S (y; 0)
is a sequential propagator, in which the component µ of the (conserved) vector current coupled
to the external ﬁeld ϕ has been inserted over all possible points of the quark line. For the case
of interest, in which ϕ can be either η or φ, this can computed by solving an appropriate Dirac
equation, with a numerical cost similar to that of computing S (z; 0). It is actually possible to
obtain the same correlation function by considering
δCexch (t) ≡lim
n→∞
1
n
n
X
i=1
X⃗
x

SV φi † (⃗x, t; 0) γ5ΓSV ηi (⃗x, t; 0) Γγ5

,
(A3)
where the sum over the Lorentz index µ has been absorbed inside a single sequential propagator:
SV ϕ (⃗x, t; 0) ≡S (⃗x, t; y)
"X
µ
Vµ (y) ϕµ (y)
#
S (y; 0) .
The diﬀerence between Eq. (A2) and Eq. (A3) corresponds to the terms

SV φi
µ † (⃗x, t; 0) γ5ΓSV ηi
ν (⃗x, t; 0) Γγ5

µ̸ = ν,
which average to zero in the Feynman gauge.
We checked that in the PS channel, this terms
are of negligible entity, so that Eq. (A3) is four time more eﬃcient than Eq. (A2). In short, the
calculation of δCexch with this framework requires to compute three propagators, and average
over several (ideally inﬁnite) stochastic sources η. This is the method adopted in Ref. [8].
In this work we have adopted a slightly diﬀerent approach. Instead of using Eq. (A1), we deﬁne
the photon propagator in terms of expectation value of the time-orderd product of photon ﬁelds:
Gµν (y1, y2) = ⟨Aµ (y1) Aν (y2)⟩,
where the photon ﬁeld Aµ (y) must be generated from the distribution of probability:
P (A) dA ∝exp

−Aµ (y1) G−1
µν (y1, y2) Aν (y2)

.
This can be readily obtained drawing each mode of the photon ﬁeld in momentum space in
which the probability distribution is local in k, as was ﬁrst noted in Ref. [3]:
P

˜A

d ˜A ∝exp
h
−˜Aµ (k) ˜G−1
µν (k) ˜Aν (k)
i
.
After the local change of variable ˜Bρ (k) =
q
G−1
ρν (k) ˜Aν (k) each component of ˜B can be drawn
independently:
P

˜B

d ˜B ∝exp
h
−˜B2
µ (k)
i
,
and the value of ˜Aµ (k) can be constructed via
˜Aν (k) =
q
˜Gρν (k) ˜Bρ (k) .
The matrix
q
˜Gρν (k) can be easily computed, and for the Wilson action in the Feynman gauge
it amounts simply to
q
˜Gρν (k) = δρν
r
1
ˆk2 .
In this way the correlation function can be computed as:
δCexch (t) ≡lim
n→∞
1
n
n
X
i=1
X
µ,⃗x

SV Ai
µ (⃗x, t; 0)
† γ5ΓSV Ai
µ (⃗x, t; 0) Γγ5

,
or through a single sequential propagator SAi, in a way similar to Eq. (A3). This has a clear
beneﬁt: only two quark inversions are required to compute the exchange diagram. The case of the
PS channel is of special interest, since in this case the correlation function is obtained by computing
δCexch
PP (t) ≡lim
n→∞
1
n
n
X
i=1
X⃗
x
D

SAi (⃗x, t; 0)

2E
.
The result is a factor 50% more precise than the corresponding one computed with η −φ
representation of the propagator.
A similar reasoning suggests that the diagram 1(b) for the “self-energy” can be obtained by
computing
δCself (t) ≡lim
n→∞
1
n
n
X
i=1
X⃗
x

SV Ai V Ai (⃗x, t; 0)
† γ5ΓS (⃗x, t; 0) Γγ5

,
with the sequential propagator deﬁned recursively as
SV Ai V Ai (⃗x, t; 0) ≡S (⃗x, t; y)
"X
µ
Vµ (y) Ai
µ (y)
#
SV Ai (y; 0) .
The “tadpole” diagram 1(c) instead can be obtained immediately at the cost of a single se-
quential propagator, without introducing any additional stochastic noise at all, by noting that the
relation
δCT (t) ≡
X
µ,⃗x
D
STµ (⃗x, t; 0)
† γ5ΓS (⃗x, t; 0) Γγ5
E
=
X⃗
x
D
ST (⃗x, t; 0)
† γ5ΓS (⃗x, t; 0) Γγ5
E
,
holds exactly, i.e. without relying on gauge symmetry.
In summary, the QED corrections to meson masses can be computed through four inversions,
namely those required to obtain the propagators S, SV Ai, SV Ai V Ai and ST . An additional propa-
gator SPS, corresponding to the PS insertion, is needed to compute the correction due to the shift
of the critical mass, diagram 1(d), which arises speciﬁcally in our Twisted-Mass setup. Moreover,
in order to take into account the mass diﬀerence between u and d quarks, an additional inversion is
needed to compute the sequential propagator SS in which the scalar density is inserted, as depicted
in diagram 1(e).
We note that working in the isosymmetric theory, there is no need to compute this diagrams
for u or d quark separately2.
Therefore, the number of light inversions, which dominates the numerical cost, is given by
#INV = 4QED + 1TM + 1MASS = 6. Finally, we remark that in order to improve the quality of
2 More speciﬁcally in the twisted-mass regularization and for the correlators analyzed in this work, we can obtain the
d-quark propagator (regularized with an r-parameter having opposite sign to the one of the u-quark) by employing
the r-γ5 symmetry of the propagator: Su = γ5S†
dγ5.
the signal, we employed sixteen diﬀerent time source positions, using a diﬀerent realization of the
photon ﬁeld Aµ per source position. For the stochastic source for the quark interpolator we used
Z2 noise, diluted in spin but not in color. Hence a total number of 4spin × 6prop × 16time = 384
Dirac equations has been solved for each gauge conﬁguration.
[1] S. Aoki et al., Eur. Phys. J. C 77 (2017) no.2, 112 [arXiv:1607.00299 [hep-lat]].
[2] M. Antonelli et al. [FlaviaNet Working Group on Kaon Decays Collaboration], Eur. Phys. J. C 69
(2010) 399 [arXiv:1005.2323 [hep-ph]].
[3] A. Duncan, E. Eichten and H. Thacker, Phys. Rev. Lett. 76 (1996) 3894 [hep-lat/9602005].
[4] T. Blum, R. Zhou, T. Doi, M. Hayakawa, T. Izubuchi, S. Uno, N. Yamada, Phys. Rev. D82
(2010)
094508. [arXiv:1006.1311 [hep-lat]].
[5] G.M. de Divitiis et al., JHEP 1204 (2012) 124 [arXiv:1110.6294 [hep-lat]].
[6] T. Ishikawa, T. Blum, M. Hayakawa, T. Izubuchi, C. Jung and R. Zhou, Phys. Rev. Lett. 109 (2012)
072002 [arXiv:1202.6018 [hep-lat]].
[7] S. Aoki, K. I. Ishikawa, N. Ishizuka, K. Kanaya, Y. Kuramashi, Y. Nakamura, Y. Namekawa and
M. Okawa et al., Phys. Rev. D 86 (2012) 034507 [arXiv:1205.2961 [hep-lat]].
[8] G. M. de Divitiis, R. Frezzotti, V. Lubicz, G. Martinelli, R. Petronzio, G. C. Rossi, F. Sanﬁlippo and
S. Simula et al., Phys. Rev. D 87 (2013) 114505 [arXiv:1303.4896 [hep-lat]].
[9] S. Borsanyi et al., Science 347 (2015) 1452 [arXiv:1406.4088 [hep-lat]].
[10] M. G. Endres, A. Shindler, B. C. Tiburzi and A. Walker-Loud, Phys. Rev. Lett. 117 (2016) no.7,
072002 [arXiv:1507.08916 [hep-lat]].
[11] Z. Fodor, C. Hoelbling, S. D. Katz, L. Lellouch, A. Portelli, K. K. Szabo and B. C. Toth, Phys. Lett.
B 755 (2016) 245 [arXiv:1502.06921 [hep-lat]].
[12] R. Horsley et al., J. Phys. G 43, no. 10, 10LT02 (2016) [arXiv:1508.06401 [hep-lat]].
[13] Z. Fodor et al., Phys. Rev. Lett. 117 (2016) no.8, 082001 [arXiv:1604.07112 [hep-lat]].
[14] P. Boyle, V. G¨ulpers, J. Harrison, A. J¨uttner, A. Portelli and C. Sachrajda, arXiv:1612.05962 [hep-lat].
[15] A. Patella, arXiv:1702.03857 [hep-lat].
[16] R. Baron et al. [ETM Coll.], JHEP 1006 (2010) 111 [arXiv:1004.5284 [hep-lat]].
[17] R. Baron et al. [ETM Coll.], PoS LATTICE 2010 (2010) 123 [arXiv:1101.0518 [hep-lat]].
[18] R. F. Dashen, Phys. Rev. 183 (1969) 1245.
[19] C. Patrignani et al. [Particle Data Group], Chin. Phys. C 40 (2016) no.10, 100001.
[20] N. Carrasco et al. [ETM Coll.], Nucl. Phys. B 887 (2014) 19 [arXiv:1403.4504 [hep-lat]].
[21] J. Gasser, A. Rusetsky, I. Scimemi, Eur. Phys. J. C32 (2003) 97-114. [hep-ph/0305260].
[22] J. Bijnens, Phys. Lett. B 306 (1993) 343 [arXiv:hep-ph/9302217].
[23] M. Hayakawa and S. Uno, Prog. Theor. Phys. 120 (2008) 413 [arXiv:0804.2044 [hep-ph]].
[24] C. McNeile and C. Michael [UKQCD Collaboration], Phys. Rev. D 73 (2006) 074506 [hep-lat/0603007].
[25] S. Aoki, K. i. Nagai, Y. Taniguchi and A. Ukawa, Phys. Rev. D 58 (1998) 074505 [hep-lat/9802034].
[26] Z. Davoudi and M. J. Savage, Phys. Rev. D 90 (2014) no.5, 054503 [arXiv:1402.6741 [hep-lat]].
[27] N. Tantalo, V. Lubicz, G. Martinelli, C. T. Sachrajda, F. Sanﬁlippo and S. Simula, arXiv:1612.00199
[hep-lat].
[28] R. Horsley et al., JHEP 1604, 093 (2016) [arXiv:1509.00799 [hep-lat]].
[29] A. Portelli et al., PoS LATTICE 2011 (2011) 136 [arXiv:1201.2787 [hep-lat]].
[30] G. Colangelo, S. Lanz, H. Leutwyler and E. Passemar, Phys. Rev. Lett. 118 (2017) no.2, 022001
[arXiv:1610.03494 [hep-ph]].
[31] S. Basak et al. [MILC Collaboration], PoS LATTICE 2015, 259 (2016) [arXiv:1606.01228 [hep-lat]].
[32] J. Gasser and H. Leutwyler, Nucl. Phys. B 250, 465 (1985).
[33] J. Gasser and H. Leutwyler, Phys. Lett. B 184 (1987) 83.
[34] J. Bijnens and K. Ghorbani, JHEP 0711 (2007) 030 [arXiv:0709.0230 [hep-ph]].
[35] R. Frezzotti, G. Rossi and N. Tantalo, arXiv:1612.02265 [hep-lat].
