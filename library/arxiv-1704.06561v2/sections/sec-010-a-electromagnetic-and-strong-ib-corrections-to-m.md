---
doc_id: arxiv-1704.06561v2
doc_title: "Leading isospin-breaking corrections to pion, kaon and charmed-meson masses with Twisted-Mass fermions"
section_id: sec-010-a-electromagnetic-and-strong-ib-corrections-to-m
section_title: "A Electromagnetic and strong IB corrections to MD+ - MD0"
section_number: null
pages: 31-36
source_pdf: 1704.06561v2.pdf
source_sha256: e1d800fa0b122dbb
toc_source: outline
doc_brief: "Leading isospin-breaking corrections to pion, kaon and charmed-meson masses with Twisted-Mass fermions — 16 sections: Front matter; I Introduction; II Simulation details"
---
Within the quenched QED approximation and the RM123 prescription described in Section III,
the QED contribution to the D-meson mass splitting is given by

M2
D+ −M2
D0
QED = 8παemMD [MD+ −MD0]em ,
(79)
where
[MD+ −MD0]em = (qu −qd)qc∂t
−(q2
d −q2
u)∂t
+
−(δmcrit
d
−δmcrit
u
)∂t
+ ZP
 1
Zd
−1
Zu

mℓ∂t
(80)
with the green lines representing the charm quark propagator.
In Fig. 14 the data for

M2
D+ −M2
D0
QED are shown before and after the subtraction of the
universal FSEs, given by Eq. (43). It can be clearly seen that, as in the case of the pion and kaon
mass splittings, the universal FSE correction is quite large, approaching ≃30% at the heaviest
light-quark masses.
0
0.01
0.02
0.03
0.04
ml (GeV)
0.006
0.008
0.01
0.012
0.014
0.016
0.018
0.02
[M
2
D
+ - M
2
D
0]
QED (GeV
2)
β=1.90, L/a=20
β=1.90, L/a=24
β=1.90, L/a=32
β=1.95, L/a=24
β=1.95, L/a=32
β=2.10, L/a=48
FIG. 14: Results for the D-meson mass splitting

M 2
D+ −M 2
D0
QED versus the renormalized light-quark
mass mℓ, obtained using Eq. (80) in the quenched QED approximation. Brown full points correspond to
the data without any correction for FSEs, while open markers represent the lattice data corrected by the
universal FSEs given by Eq. (43).
From now on we always refer to the data for

M2
D+ −M2
D0
QED as to the QED part of the
charged/neutral D-meson mass splitting already subtracted by the universal FSEs.
We have performed combined chiral, continuum and inﬁnite volume extrapolations adopting
the following ﬁtting function

M2
D+ −M2
D0
QED = 4παem

AD
0 + AD
1 mℓ+ DDa2 + F D MD
L3

,
(81)
where AD
0 , AD
1 , DD and F D are free parameters. In Fig. 15 we show the results obtained using
the combined ﬁtting function (81).
0.01
0.02
0.03
0.04
0.05
ml (GeV)
0.008
0.01
0.012
0.014
0.016
0.018
0.02
[M
2
D
+ - M
2
D
0]
QED (GeV
2)
β=1.90, L/a=20
β=1.90, L/a=24
β=1.90, L/a=32
β=1.95, L/a=24
β=1.95, L/a=32
β=2.10, L/a=48
physical point
FIG. 15: Results for the D-meson mass splitting

M 2
D+ −M 2
D0
QED versus the renormalized light-quark
mass mℓ. The empty markers correspond to the data after the subtraction of the universal FSEs, while the
ﬁlled markers represent the lattice data corrected also by the SD FSEs obtained in the ﬁtting procedure. The
solid lines correspond to the results of the combined ﬁt (81) obtained in the inﬁnite volume limit at each
value of the lattice spacing. The black asterisk represents the D-meson mass splitting extrapolated at the
physical pion mass mℓ= mud = 3.70(17) MeV and to the continuum limit, while the red area identiﬁes the
corresponding uncertainty at the level of one standard deviation.
At the physical pion mass and in the continuum and inﬁnite volume limits our result in the MS
scheme at a renormalization scale equal to µ = 2 GeV is

M2
D+ −M2
D0
QED = 9.03 (0.84)stat+fit (1.65)disc (0.12)chir (0.07)FSE (0.45)qQED · 10−3 GeV2 ,
= 9.03 (0.84)stat+fit (1.65)syst (0.45)qQED · 10−3 GeV2 ,
= 9.03 (1.90) · 10−3 GeV2 ,
(82)
where
• ()stat+fit indicates the statistical uncertainty including also the ones induced by the ﬁtting
procedure and by the determination of the input parameters of Table II;
• ()disc is the uncertainty due to discretization eﬀects estimated by comparing the results
assuming either DD̸ = 0 or DD = 0 in Eq. (81);
• ()chir is the error coming from including (AD
1̸ = 0) or excluding (AD
1 = 0) the linear term in
the light-quark mass;
• ()FSE is the uncertainty due to FSE estimated by comparing the results obtained including
(F D̸ = 0) or excluding (F D = 0) the phenomenological term for the SD FSEs;
• ()qQED is the estimate of the eﬀects due to the quenched QED approximation (5%) taken
from Refs. [13, 29] and extended to the case of charmed mesons.
We need now to compute the QCD contribution

M2
D+ −M2
D0
QCD = 2MD ZP ( bmd −bmu) ∂t
,
(83)
where for ( bmd −bmu) we make use of the result (66). The lattice data for

M2
D+ −M2
D0
QCD are
shown in Fig. 16 and FSEs are visible. Thus the data have been ﬁtted according to the following
simple Ansatz:

M2
D+ −M2
D0
QCD = A
D
0 + A
D
1 mℓ+ D
Da2 + F
D
M
2
16π2f2
0
e−ML
(ML)3/2 ,
(84)
where we recall M
2 = 2B0mℓ. The results of the linear ﬁt (84) with the four free parameters A
D
0 ,
A
D
1 , D
D and F
D, are shown in Fig. 16.
At the physical pion mass and in the continuum and inﬁnite volume limits we get

M2
D+ −M2
D0
QCD (MS, 2 GeV) = 11.41 (99)stat+fit (21)disc (13)chir (9)FSE · 10−3 GeV2
= 11.41 (99)stat+fit (26)syst · 10−3 GeV2 ,
= 11.41 (1.02) · 10−3 GeV2 .
(85)
where
0
0.01
0.02
0.03
0.04
ml (GeV)
0.008
0.01
0.012
0.014
0.016
0.018
0.02
0.022
[M
2
D
+ - M
2
D
0]
QCD (GeV
2)
β=1.90, L/a=24
β=1.90, L/a=32
β=1.95, L/a=24
β=1.95, L/a=32
β=2.10, L/a=48
physical point
FIG. 16: Results for the QCD contribution

M 2
D+ −M 2
D0
QCD versus the renomalized light-quark mass mℓ.
The empty markers correspond to the lattice data, while the ﬁlled ones represent the data corrected for the
FSEs obtained in the ﬁtting procedure (84). The solid lines correspond to the results of the combined ﬁt (84)
obtained in the inﬁnite volume limit at each value of the lattice spacing. The black asterisk represents the IB
slope extrapolated at the physical pion mass mℓ= mud = 3.70(17) MeV and to the continuum limit, while
the red area identiﬁes the corresponding uncertainty at the level of one standard deviation.
• ()stat+fit indicates the statistical uncertainty including also the ones induced by the ﬁtting
procedure and by the determination of the input parameters of Table II;
• ()disc is the uncertainty due to discretization eﬀects estimated by including (D
D̸ = 0) or
excluding (D
D = 0) the discretization term in Eq. (84);
• ()chir is the error coming from including (A
D
1̸ = 0) or excluding (A
D
1 = 0) the linear term in
the light-quark mass.
• ()FSE is the uncertainty obtained including (F
D̸ = 0) or excluding (F
D = 0) the FSE term
in Eq. (84).
Thus, putting together the results (82) and (85) we get the prediction
MD+ −MD0 = 5.47 (30)stat+fit (40)disc (6)chir (3)FSE (12)qQED MeV ,
= 5.47 (30)stat+fit (42)syst (12)qQED MeV ,
= 5.47 (53) MeV ,
(86)
which is consistent with the experimental value MD+ −MD0 = 4.75(8) MeV [19] within ≃1.4
standard deviations.
B.
